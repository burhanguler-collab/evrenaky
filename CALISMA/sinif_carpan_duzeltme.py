r"""ADIM 0 — SINIF a_0 CARPANLARINI SAYISAL COZ.  (naif formulun yerine)

--- NEDEN ---
sinif_capraz_tani.py:107 sunu kullaniyor:

    carp = lambda e: (1 / (1 + e / 100)) ** 4        # naif 10^(-4*fark)

Bu, 97_BTFR'nin duzeltme kaydinda GERI CEKILEN formuldur: yalniz saf-F4
asimptotunda (v ~ a_0^(1/4)) gecerlidir. Oysa sinif calismasinin ongorusu
IKI TERIMLIDIR — sinif_ongoru_vs_fit.py:124:

    v_ong = sqrt( V_bar^2(Y*)  +  G M_kaps(R) / l_omega )

a_0 -> k a_0 olunca l_omega -> l_omega/sqrt(k), yani F4 terimi sqrt(k) ile
olceklenir; V_bar^2 HIC olceklenmez. Kapali formul yoktur, k sayisal cozulur.

--- HATA NEDEN ZARARSIZ BIR KAYMA DEGIL ---
Naif formulun sapmasi F4'un v^2 icindeki payina baglidir:
  F4 baskin (cuce, gec tip)  -> naif deger dogruya yakin
  F1 baskin (buyuk sarmal)   -> naif deger cok dusuk
Yani duzeltme YUKSEK IVMELI siniflarda en buyuktur. Sinanmak istenen sey tam
olarak "carpan ivmeyle degisiyor mu" oldugundan, naif sayilar o ekseni YAPAY
olarak buker. Bu yuzden Adim 1'den once bu adim zorunludur.

--- OZ DENETIM ---
Betik once V_bar^2, M_kaps ve l_omega'yi sifirdan hesaplar, sonra kayitli
SONUC.csv'deki DIS_evr_sapma_yuzde degerini YENIDEN URETIR. Uretemezse durur.
Yani asagidaki carpanlar, sinif calismasinin kendi sayilariyla ayni zeminden
gelir; yeni bir kurulum degildir.

Bu betik HICBIR DOSYAYI DEGISTIRMEZ. Yalniz olcer ve basar.
Cikti: ekran + SINIF_CALISMASI/_HESAPLAR/sinif_carpan_duzeltme.csv
"""

import os
import sys
import csv
import glob
import warnings

import numpy as np

warnings.filterwarnings('ignore')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

KOK = os.path.dirname(os.path.abspath(__file__))
SK = os.path.join(KOK, 'SINIF_CALISMASI')
CIK = os.path.join(SK, '_HESAPLAR')
os.makedirs(CIK, exist_ok=True)

# ---- sabitler: sinif_ongoru_vs_fit.py ile BIREBIR ayni ----
G = 4.300917e-6
C_SI = 2.99792458e8
ACC = 1e6 / 3.0856776e19
A0_ESKI = (C_SI * (70e3 / 3.0857e22)) / ACC / 16.1
# NIHAI KURULUM (86_NIHAI): yerel l_omega + a_0 x1,75. Oz denetim ve carpanlar
# artik NIHAI kuruluma goredir (SONUC.csv nihai boru hattiyla yenilendi).
A0 = 1.75 * A0_ESKI
RB = 1.4
UPS = 0.50
PAY_ESIK = 0.25        # 96_ETG md.3 / 95_RAR md.4 ile ayni esik

AD = {'01_erken_spiral': 'Sa–Sab', '02_orta_spiral': 'Sb–Sbc', '03_gec_spiral': 'Sc–Scd',
      '04_cok_gec_spiral': 'Sd', '05_macellan': 'Sdm–Sm', '06_duzensiz': 'Im'}


def yukle(sn):
    """sinif_ongoru_vs_fit.py'nin veri kurulumunu birebir tekrarlar."""
    sd = os.path.join(SK, sn)
    kat = {r['Galaksi']: r for r in
           csv.DictReader(open(os.path.join(sd, 'KATALOG.csv'), encoding='utf-8'))}
    out = []
    for f in sorted(glob.glob(os.path.join(sd, 'veri', '*_rotmod.dat'))):
        ad = os.path.basename(f)[:-11]
        d = np.loadtxt(f)
        R, Vo, eV, Vg, Vd, Vb, SBd, SBb = [d[:, i] for i in range(8)]
        Rp = R * 1e3
        L = lambda S: np.concatenate([[0.0], np.cumsum(
            np.pi * (Rp[1:] ** 2 - Rp[:-1] ** 2) * 0.5 * (S[1:] + S[:-1]))])
        Vbar2 = np.sign(Vg) * Vg ** 2 + UPS * Vd ** 2 + RB * UPS * Vb ** 2
        Mgas = np.maximum(R * np.sign(Vg) * Vg ** 2 / G, 0.0)
        Mkaps = UPS * L(SBd) + RB * UPS * L(SBb) + Mgas
        out.append(dict(g=ad, R=R, Vo=Vo, Vbar2=Vbar2,
                        F4=np.sqrt(A0 * G * np.maximum(Mkaps, 1e-9)),   # NIHAI: yerel
                        lom=float(np.sqrt(G * max(Mkaps[-1], 1e-6) / A0)),
                        L36=float(kat[ad]['L36_1e9Lsun']) * 1e9))
    return out


def carpan(vb2, f4, vo):
    """mean((v_ong - v_olc)/v_olc) = 0 kokunu ikiye bolmeyle cozer.

    NOT: sinif calismasi sapmayi ORANLARIN ORTALAMASI olarak tanimlar
    (medyan log degil). Karsilastirilabilirlik icin ayni tanim korundu.
    """
    fk = lambda k: float(np.mean((np.sqrt(np.maximum(vb2 + np.sqrt(k) * f4, 1e-9))
                                  - vo) / vo))
    a, b = 1e-4, 1e4
    if fk(a) > 0 or fk(b) < 0:
        return np.nan
    for _ in range(200):
        m = np.sqrt(a * b)
        if fk(m) < 0:
            a = m
        else:
            b = m
    return np.sqrt(a * b)


naif = lambda e: (1 / (1 + e / 100)) ** 4        # geri cekilen formul (kiyas icin)

print('OZ DENETIM — kayitli DIS_evr_sapma_yuzde yeniden uretiliyor')
SAT, SINIF, EN_KOTU = [], [], 0.0
for sn in sorted(AD):
    yol = os.path.join(SK, sn, 'HESAP', 'SONUC.csv')
    if not os.path.exists(yol):
        continue
    kayit = {r['Galaksi']: r for r in csv.DictReader(open(yol, encoding='utf-8'))}
    gal = yukle(sn)
    kn, kd, pay_, sap, gb_dis, gb_med = [], [], [], [], [], []
    for d in gal:
        m = d['R'] > np.median(d['R'])                   # dis yari — kayitla ayni
        vo, vb2, f4 = d['Vo'][m], d['Vbar2'][m], d['F4'][m]
        e = 100 * float(np.mean((np.sqrt(np.maximum(vb2 + f4, 1e-9)) - vo) / vo))
        ref = float(kayit[d['g']]['DIS_evr_sapma_yuzde'])
        EN_KOTU = max(EN_KOTU, abs(e - ref))
        k = carpan(vb2, f4, vo)
        p = float(np.median(f4 / np.maximum(vb2 + f4, 1e-9)))
        kn.append(naif(ref)); kd.append(k); pay_.append(p); sap.append(ref)
        gb_dis.append(d['Vbar2'][-1] / d['R'][-1] * ACC)
        gb_med.append(float(np.median(d['Vbar2'] / d['R'])) * ACC)
        # NOT: carpanlar 4 haneyle yazilir. 2 hane yeterli GORUNUYOR ama bu CSV'yi
        # okuyan sinif_capraz_tani.py medyani YUVARLANMIS degerlerden aliyordu ve
        # Im sinifinda x1,47 yerine x1,46 basiyordu. Hassasiyet bilerek fazladir.
        SAT.append([sn, AD[sn], d['g'], '%.1f' % ref, '%.3f' % p,
                    '%.4f' % naif(ref), '' if np.isnan(k) else '%.4f' % k,
                    'evet' if p >= PAY_ESIK else 'HAYIR',
                    '%.3e' % gb_dis[-1], '%.3e' % gb_med[-1]])
    kn, kd, pay_ = np.array(kn), np.array(kd), np.array(pay_)
    ok = (pay_ >= PAY_ESIK) & np.isfinite(kd)
    SINIF.append(dict(sn=sn, ad=AD[sn], n=len(gal), sap=np.median(sap),
                      pay=np.median(pay_), naif=np.median(kn),
                      dog=np.median(kd[np.isfinite(kd)]),
                      dog_ok=np.median(kd[ok]) if ok.sum() else np.nan,
                      n_ok=int(ok.sum()),
                      gbd=np.median(gb_dis), gbm=np.median(gb_med)))
print('  en buyuk fark: %.3f yuzde puani -> %s'
      % (EN_KOTU, 'GECTI' if EN_KOTU < 0.06 else 'KALDI — kurulum eslesmedi'))
if EN_KOTU >= 0.06:
    raise SystemExit('oz denetim basarisiz; carpanlar guvenilmez.')

print('\n' + '=' * 104)
print('SINIF a_0 CARPANLARI — geri cekilen formul vs sayisal cozum')
print('  %-9s %4s %9s %8s | %9s %9s %8s | %6s'
      % ('sinif', 'n', 'sapma %', 'F4 payi', 'NAIF', 'DOGRU', 'fark', 'okunur'))
for s in SINIF:
    print('  %-9s %4d %+9.1f %8.2f | %9.2fx %8.2fx %+7.0f%% | %2d/%d'
          % (s['ad'], s['n'], s['sap'], s['pay'], s['naif'], s['dog'],
             100 * (s['dog'] / s['naif'] - 1), s['n_ok'], s['n']))
nf = np.array([s['naif'] for s in SINIF]); dg = np.array([s['dog'] for s in SINIF])
print('\n  %-24s %8s %8s %8s %8s' % ('', 'en kucuk', 'en buyuk', 'oran', 'sacilma'))
for ad, v in [('NAIF (geri cekilen)', nf), ('DOGRU (sayisal)', dg)]:
    print('  %-24s %8.2fx %7.2fx %7.2f %8.3f dex'
          % (ad, v.min(), v.max(), v.max() / v.min(), np.std(np.log10(v))))

print('\n  KARSILASTIRMA NOKTALARI')
print('    95_RAR kusak bandi (sayisal)  : x0,92 - x2,86   (sacilma 0,142 dex)')
print('    97_BTFR (sayisal)             : x2,02')
print('    96_ETG dis nokta (sayisal)    : x1,85')
print('    kitap 6.5.4.5 kaydi           : x2,26')

print('\n' + '=' * 104)
print('SINIFLARIN TIPIK IVMESI  (Adim 1 icin hazirlik — burada YORUMLANMIYOR)')
print('  %-9s %14s %14s %10s %10s'
      % ('sinif', 'log g_bar dis', 'log g_bar med', 'DOGRU', 'NAIF'))
for s in SINIF:
    print('  %-9s %14.2f %14.2f %9.2fx %9.2fx'
          % (s['ad'], np.log10(s['gbd']), np.log10(s['gbm']), s['dog'], s['naif']))

with open(os.path.join(CIK, 'sinif_carpan_duzeltme.csv'), 'w',
          encoding='utf-8', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['Sinif_klasor', 'Sinif', 'Galaksi', 'DIS_sapma_yuzde', 'F4_payi',
                'carpan_NAIF_geri_cekilen', 'carpan_DOGRU_sayisal',
                'carpan_okunabilir', 'g_bar_dis_nokta_ms2', 'g_bar_medyan_ms2'])
    w.writerows(SAT)
print('\n-> _HESAPLAR/sinif_carpan_duzeltme.csv  (%d galaksi)' % len(SAT))
print('   HICBIR calisma dosyasi degistirilmedi.')
