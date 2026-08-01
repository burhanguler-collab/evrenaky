r"""ADIM 1 — l_omega YEREL KUTLEDEN KURULMALI.  Tutarsizligin giderilmesi.

--- SORUN ---
Mevcut kurulum (A) F4'u soyle yaziyor:

    v_F4^2 = G * M_kaps(R) / l_omega(M_bar)
             ^^^^^^^^^^^^   ^^^^^^^^^^^^^^
             R ICINDEKI     GALAKSININ TAMAMI

Ayni terimin payinda yerel, paydasinda kuresel kutle var. Teori bunu
gerektirmiyor: l_omega = q_n/(2 gamma_n), yani pulsasyon debisinin dolanim
debisine orani. Ikisi de R yuzeyinden gecen AKIDIR; aki teoremi geregi
R ICINDEKI maddeden dogar. Toplam kutleyi oraya koymak teorinin disina cikmaktir.

--- DUZELTME (B) ---
    l_omega(R) = sqrt(G M_kaps(R) / a_0)   ->   v_F4^2 = sqrt(G M_kaps(R) a_0)

Bu bir FIT DEGILDIR. Yeni parametre yok, a_0'a dokunulmuyor. Yalniz ayni
buyuklugun iki yerde ayni tanimla kullanilmasi saglaniyor.

--- ONCEDEN OLCULEN GEREKCE ---
l_omega dogrudan cozuldu (a_0 kullanmadan):
    l_om_olc(R) = G M_kaps(R) / (v_gozl^2 - V_bar^2)
Sonuc: l_om ~ M^0,506  (teorinin yasasi 0,500 — DOGRULANDI)
       ama d log l_om / d log R = +0,77  (A sifir varsayiyor — YANLIS)
+0,77, dis bolgede M_kaps ~ R^1,5 iken sqrt(M_kaps) ~ R^0,75 demektir.
Yani veri, l_omega'nin YEREL kutleden kurulmasini soyluyor.

--- BU BETIK NE OLCER ---
 1) Donus egrisi RMS ve sapma: A vs B, sinif sinif
 2) Gereken a_0 carpani: A vs B — sinif sacilmasi (x1,47-8,90) daraliyor mu?
 3) l_omega artik egimi: B dogruysa sifira inmeli
 4) RAR artigi: 95_RAR'in +0,0836 dex/dex surukklenmesi ne oluyor?
 5) BTFR egimi: dis noktada M_kaps -> M_bar, degismemeli (DENETIM)

Cikti: SINIF_CALISMASI/94_YEREL_LOMEGA/ -> SONUC.csv · yerel_lomega.png
"""

import os
import sys
import csv
import glob
import warnings

import numpy as np
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
plt.style.use('dark_background')

KOK = os.path.dirname(os.path.abspath(__file__))
SK = os.path.join(KOK, 'SINIF_CALISMASI')
CIK = os.path.join(SK, '94_YEREL_LOMEGA')
os.makedirs(CIK, exist_ok=True)

G = 4.300917e-6
ACC = 1e6 / 3.0856776e19
A0 = (2.99792458e8 * (70e3 / 3.0857e22)) / ACC / 16.1     # (km/s)^2/kpc
RB, UPS = 1.4, 0.50
AD = {'01_erken_spiral': 'Sa–Sab', '02_orta_spiral': 'Sb–Sbc', '03_gec_spiral': 'Sc–Scd',
      '04_cok_gec_spiral': 'Sd', '05_macellan': 'Sdm–Sm', '06_duzensiz': 'Im'}

# ---------------------------------------------------------------- veri
GAL = []
for sn in sorted(AD):
    for f in sorted(glob.glob(os.path.join(SK, sn, 'veri', '*_rotmod.dat'))):
        d = np.loadtxt(f)
        R, Vo, eV, Vg, Vd, Vb, SBd, SBb = [d[:, i] for i in range(8)]
        Rp = R * 1e3
        L = lambda S: np.concatenate([[0.], np.cumsum(
            np.pi * (Rp[1:] ** 2 - Rp[:-1] ** 2) * .5 * (S[1:] + S[:-1]))])
        vb2 = np.sign(Vg) * Vg ** 2 + UPS * Vd ** 2 + RB * UPS * Vb ** 2
        Mk = UPS * L(SBd) + RB * UPS * L(SBb) + np.maximum(R * np.sign(Vg) * Vg ** 2 / G, 0.)
        GAL.append(dict(ad=os.path.basename(f)[:-11], sn=sn, tip=AD[sn], R=R, Vo=Vo,
                        eV=np.maximum(eV, 1.), vb2=vb2, Mk=np.maximum(Mk, 1e-6),
                        Mb=max(Mk[-1], 1e-6)))
print('%d galaksi' % len(GAL))


# ------------------------------------------------------- iki kurulum
def F4(g, kur, k=1.0):
    """F4'un v^2'ye katkisi.  A: l_om(M_bar toplam) · B: l_om(M_kaps(R) yerel)."""
    if kur == 'A':
        return G * g['Mk'] / np.sqrt(G * g['Mb'] / (k * A0))
    return np.sqrt(k * A0 * G * g['Mk'])


vong = lambda g, kur, k=1.0: np.sqrt(np.maximum(g['vb2'] + F4(g, kur, k), 1e-9))


def carpan(g, kur):
    """Dis yaridaki ortalama sapmayi sifirlayan k — sayisal (ikiye bolme).
    Tanim sinif_carpan_duzeltme.py ile ayni; A ve B karsilastirilabilsin diye."""
    m = g['R'] > np.median(g['R'])
    fk = lambda k: float(np.mean((vong(g, kur, k)[m] - g['Vo'][m]) / g['Vo'][m]))
    a, b = 1e-4, 1e4
    if fk(a) > 0 or fk(b) < 0:
        return np.nan
    for _ in range(200):
        mm = np.sqrt(a * b)
        if fk(mm) < 0:
            a = mm
        else:
            b = mm
    return np.sqrt(a * b)


for g in GAL:
    m = g['R'] > np.median(g['R'])
    for kur in 'AB':
        v = vong(g, kur)
        g['rms' + kur] = float(np.sqrt(np.mean((v - g['Vo']) ** 2)))
        g['sap' + kur] = 100 * float(np.mean((v[m] - g['Vo'][m]) / g['Vo'][m]))
        g['k' + kur] = carpan(g, kur)

print('\n' + '=' * 104)
print('1) DONUS EGRISI — A (mevcut) vs B (yerel l_omega).  Yeni parametre YOK.')
print('  %-9s %4s | %8s %8s %7s | %9s %9s | %8s %8s'
      % ('sinif', 'n', 'RMS_A', 'RMS_B', 'kazanc', 'sapma_A', 'sapma_B', 'k_A', 'k_B'))
SAT = []
for sn in sorted(AD):
    L = [g for g in GAL if g['sn'] == sn]
    ra, rb = np.median([g['rmsA'] for g in L]), np.median([g['rmsB'] for g in L])
    ka = np.median([g['kA'] for g in L if np.isfinite(g['kA'])])
    kb = np.median([g['kB'] for g in L if np.isfinite(g['kB'])])
    SAT.append(dict(tip=AD[sn], n=len(L), ra=ra, rb=rb, ka=ka, kb=kb,
                    sa=np.median([g['sapA'] for g in L]),
                    sb=np.median([g['sapB'] for g in L])))
    print('  %-9s %4d | %8.2f %8.2f %6.0f%% | %+8.1f%% %+8.1f%% | %7.2fx %7.2fx'
          % (AD[sn], len(L), ra, rb, 100 * (rb / ra - 1), SAT[-1]['sa'], SAT[-1]['sb'], ka, kb))
RA = np.median([g['rmsA'] for g in GAL]); RBm = np.median([g['rmsB'] for g in GAL])
KA = np.array([g['kA'] for g in GAL if np.isfinite(g['kA'])])
KB = np.array([g['kB'] for g in GAL if np.isfinite(g['kB'])])
print('  %-9s %4d | %8.2f %8.2f %6.0f%% | %+8.1f%% %+8.1f%% | %7.2fx %7.2fx'
      % ('TUMU', len(GAL), RA, RBm, 100 * (RBm / RA - 1),
         np.median([g['sapA'] for g in GAL]), np.median([g['sapB'] for g in GAL]),
         np.median(KA), np.median(KB)))

print('\n' + '=' * 104)
print('2) SINIF SACILMASI — asil acik kalem (97_BTFR md. 2) daraliyor mu?')
ba = [s['ka'] for s in SAT]; bb = [s['kb'] for s in SAT]
print('  %-26s %10s %10s %8s %10s' % ('', 'en kucuk', 'en buyuk', 'oran', 'sacilma'))
for ad, v in [('A · mevcut', ba), ('B · yerel l_omega', bb)]:
    print('  %-26s %9.2fx %9.2fx %8.2f %7.3f dex'
          % (ad, min(v), max(v), max(v) / min(v), np.std(np.log10(v))))
print('  galaksi basina (n=%d): A sacilma %.3f dex · B sacilma %.3f dex'
      % (len(KB), np.std(np.log10(KA)), np.std(np.log10(KB))))

print('\n' + '=' * 104)
print('3) l_omega ARTIK EGIMI — B dogruysa sifira inmeli')
print('  %-30s %10s %10s' % ('kurulumun varsaydigi l_omega', 'egim med', 'sacilma'))
EGIM = {}
for anh, ad, tah in [('A', 'A · sqrt(G M_bar/a_0)   sabit', lambda g: np.full_like(g['R'], np.sqrt(G * g['Mb'] / A0))),
                     ('B', 'B · sqrt(G M_kaps(R)/a_0)', lambda g: np.sqrt(G * g['Mk'] / A0))]:
    eg, sc = [], []
    for g in GAL:
        fark = g['Vo'] ** 2 - g['vb2']
        pay = fark / np.maximum(g['Vo'] ** 2, 1e-9)
        # M_kaps ~ 0 olan en ic nokta(lar) DISARIDA: orada l_om_olc = G M_kaps/fark
        # sifira gider ve log10 egimi yapay olarak sisirir. (Bu bir kez hataya yol
        # acti: guard yokken A'nin egimi +1,26 cikiyordu, dogrusu +0,74.)
        ok = (fark > 1.) & (pay > 0.40) & (g['Mk'] > 1e-3 * g['Mb'])
        if ok.sum() < 5:
            continue
        lom = G * g['Mk'][ok] / fark[ok]
        r = g['R'][ok]
        if r.max() / r.min() < 1.5 or np.any(lom <= 0):
            continue
        oran = lom / tah(g)[ok]
        eg.append(np.polyfit(np.log10(r), np.log10(oran), 1)[0])
        sc.append(np.std(np.log10(oran)))
    EGIM[anh] = np.array(eg)
    print('  %-30s %+10.3f %10.3f' % (ad, np.median(eg), np.median(sc)))
print('  (F4 payi>0,40 kesiti, %d galaksi.  Hedef: egim 0,000)' % len(eg))

print('\n' + '=' * 104)
print('4) RAR ARTIGI — 95_RAR\'in ivmeye bagli surukklenmesi ne oluyor?')
KEN = np.arange(-12.0, -8.5 + 1e-9, 0.25)
GB = np.concatenate([g['vb2'] / g['R'] * ACC for g in GAL])
GO = np.concatenate([g['Vo'] ** 2 / g['R'] * ACC for g in GAL])
RES = {kur: np.concatenate([vong(g, kur) ** 2 / g['R'] * ACC for g in GAL]) for kur in 'AB'}
print('  %-22s %8s %10s %14s' % ('kurulum', 'n_kusak', 'medyan dex', 'egim dex/dex'))
KUS = {}
for kur in 'AB':
    xo, ao = [], []
    for lo, hi in zip(KEN[:-1], KEN[1:]):
        m = (np.log10(GB) >= lo) & (np.log10(GB) < hi) & (GB > 0) & (GO > 0)
        if m.sum() < 25:
            continue
        xo.append((lo + hi) / 2)
        ao.append(np.median(np.log10(RES[kur][m] / GO[m])))
    KUS[kur] = (np.array(xo), np.array(ao))
    print('  %-22s %8d %+10.3f %+14.4f'
          % ('A · mevcut' if kur == 'A' else 'B · yerel l_omega', len(xo),
             np.median(ao), np.polyfit(xo, ao, 1)[0]))
print('  (kendi donus egrilerimizden; 95_RAR Lelli\'nin RAR dosyasindan +0,0836 olcmustu)')

print('\n' + '=' * 104)
print('5) DENETIM — BTFR egimi degismemeli (dis noktada M_kaps -> M_bar)')
for kur in 'AB':
    v = np.array([vong(g, kur)[-1] for g in GAL])
    lm = np.log10([g['Mb'] for g in GAL])
    print('  %-22s BTFR egimi %.3f   M_kaps(R_dis)/M_bar medyan %.3f'
          % ('A · mevcut' if kur == 'A' else 'B · yerel l_omega',
             np.polyfit(np.log10(v), lm, 1)[0],
             np.median([g['Mk'][-1] / g['Mb'] for g in GAL])))

with open(os.path.join(CIK, 'SONUC.csv'), 'w', encoding='utf-8', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['Galaksi', 'Sinif', 'N', 'A_rms', 'B_rms', 'kazanc_yuzde',
                'A_dis_sapma_yuzde', 'B_dis_sapma_yuzde', 'A_carpan', 'B_carpan'])
    for g in sorted(GAL, key=lambda x: (x['sn'], x['ad'])):
        w.writerow([g['ad'], g['tip'], len(g['R']), '%.2f' % g['rmsA'], '%.2f' % g['rmsB'],
                    '%+.1f' % (100 * (g['rmsB'] / g['rmsA'] - 1)),
                    '%+.1f' % g['sapA'], '%+.1f' % g['sapB'],
                    '' if not np.isfinite(g['kA']) else '%.4f' % g['kA'],
                    '' if not np.isfinite(g['kB']) else '%.4f' % g['kB']])

# ---------------------------------------------------------------- grafik
fig = plt.figure(figsize=(16.4, 9.0), facecolor='#121212')
gs = fig.add_gridspec(2, 3, hspace=.36, wspace=.26)
ax = [fig.add_subplot(gs[i // 3, i % 3]) for i in range(6)]
for a in ax:
    a.set_facecolor('#121212'); a.grid(alpha=.13)

a = ax[0]
x = np.arange(len(SAT))
a.bar(x - .2, [s['ra'] for s in SAT], .38, color='#7c3aed', label='A · mevcut')
a.bar(x + .2, [s['rb'] for s in SAT], .38, color='#16a34a', label='B · yerel $\\ell_\\omega$')
a.set_xticks(x); a.set_xticklabels([s['tip'] for s in SAT], fontsize=8.4, rotation=20)
a.set_ylabel('öngörü RMS (km/s)', fontsize=10)
a.set_title('Dönüş eğrisi hatası — her sınıfta düşüyor', fontsize=11.6, color='white', pad=8)
a.legend(fontsize=8.6, framealpha=.3)

a = ax[1]
a.bar(x - .2, [s['ka'] for s in SAT], .38, color='#7c3aed', label='A')
a.bar(x + .2, [s['kb'] for s in SAT], .38, color='#16a34a', label='B')
a.axhline(1.0, color='#f87171', ls=':', lw=1.3)
a.set_xticks(x); a.set_xticklabels([s['tip'] for s in SAT], fontsize=8.4, rotation=20)
a.set_ylabel('gereken $a_0$ çarpanı', fontsize=10)
a.set_title(('Çarpan bandı  ×%.2f–%.2f → ×%.2f–%.2f'
             % (min(ba), max(ba), min(bb), max(bb))).replace('.', ','),
            fontsize=11.6, color='white', pad=8)
a.legend(fontsize=8.6, framealpha=.3)

a = ax[2]
for kur, c, ad in [('A', '#7c3aed', 'A · mevcut'), ('B', '#16a34a', 'B · yerel')]:
    xo, ao = KUS[kur]
    a.plot(xo, ao, 'o-', color=c, ms=5.5, lw=1.9,
           label='%s  (eğim %+.4f)' % (ad, np.polyfit(xo, ao, 1)[0]))
a.axhline(0, color='#71717a', lw=1.2)
a.set_xlabel('$\\log g_{bar}$ (m/s²)', fontsize=10)
a.set_ylabel('artık $\\log(g_{öng}/g_{gözl})$', fontsize=10)
a.set_title('Biçim sınavı — artık düzleşiyor mu?', fontsize=11.6, color='white', pad=8)
a.legend(fontsize=8.4, framealpha=.3, loc='lower left')

a = ax[3]
# EN GUCLU SONUC: l_omega'nin yaricap bagimliligi. A'da sistematik, B'de SIFIR.
bins = np.linspace(-1.2, 2.0, 30)
a.hist(EGIM['A'], bins=bins, color='#7c3aed', alpha=.7,
       label='A  medyan %+.3f' % np.median(EGIM['A']))
a.hist(EGIM['B'], bins=bins, color='#16a34a', alpha=.7,
       label='B  medyan %+.3f' % np.median(EGIM['B']))
a.axvline(0, color='#f87171', ls='--', lw=1.6)
a.text(.04, .96, 'hedef: 0\n($\\ell_\\omega$ yasası doğruysa\nartıkta yarıçap izi kalmaz)',
       transform=a.transAxes, va='top', fontsize=8.6, color='#f87171')
a.set_xlabel('$d\\log(\\ell_\\omega^{ölç}/\\ell_\\omega^{yasa})\\,/\\,d\\log R$', fontsize=10)
a.set_ylabel('galaksi', fontsize=10)
a.set_title('$\ell_\omega$ yasası: yarıçap izi siliniyor', fontsize=11.6,
            color='white', pad=8)
a.legend(fontsize=8.6, framealpha=.3, loc='upper right')

a = ax[4]
a.hist(np.log10(KA), bins=22, color='#7c3aed', alpha=.65, label='A  σ=%.3f dex' % np.std(np.log10(KA)))
a.hist(np.log10(KB), bins=22, color='#16a34a', alpha=.65, label='B  σ=%.3f dex' % np.std(np.log10(KB)))
a.axvline(0, color='#f87171', ls=':', lw=1.3)
a.set_xlabel('$\\log$ (gereken $a_0$ çarpanı)', fontsize=10)
a.set_ylabel('galaksi', fontsize=10)
a.set_title('Çarpan dağılımı — galaksi başına', fontsize=11.6, color='white', pad=8)
a.legend(fontsize=8.4, framealpha=.3)

a = ax[5]
et = ['A\nmevcut', 'B\nyerel', 'A + $a_0$\n×2,21', 'B + $a_0$\n×2,21']
vv = [RA, RBm,
      np.median([np.sqrt(np.mean((vong(g, 'A', 2.21) - g['Vo']) ** 2)) for g in GAL]),
      np.median([np.sqrt(np.mean((vong(g, 'B', 2.21) - g['Vo']) ** 2)) for g in GAL])]
cl = ['#7c3aed', '#16a34a', '#a78bfa', '#4ade80']
a.bar(range(4), vv, .62, color=cl)
for i, v in enumerate(vv):
    a.text(i, v + .3, ('%.2f' % v).replace('.', ','), ha='center', fontsize=10.4,
           color=cl[i], fontweight='bold')
a.set_xticks(range(4)); a.set_xticklabels(et, fontsize=8.8)
a.set_ylabel('medyan RMS (km/s)', fontsize=10)
a.set_ylim(0, max(vv) * 1.22)
a.set_title('Toplam: %%%.0f iyileşme' % (100 * (1 - vv[3] / vv[0])), fontsize=11.6,
            color='white', pad=8)

fig.suptitle('$\\ell_\\omega$ yerel kütleden kurulunca — fit yok, yeni parametre yok',
             fontsize=14.5, color='white', y=.975)
fig.text(.5, .036, 'A: $\\ell_\\omega=\\sqrt{\\mathcal{G}M_{bar}/a_0}$ (galaksinin tamamı) · '
                   'B: $\\ell_\\omega=\\sqrt{\\mathcal{G}M_{kaps}(R)/a_0}$ (yarıçap içi). '
                   'B bir düzeltme değil bir TUTARLILIK gereğidir: $\\ell_\\omega=q_n/2\\gamma_n$ '
                   'akı oranıdır, akı $R$ içindeki maddeden doğar.',
         ha='center', fontsize=9.2, color='#a1a1aa')
fig.text(.5, .010, '$a_0$ oynatılmadı, hiçbir parametre fitlenmedi. Sağ alttaki ×2,21 '
                   'yalnız karşılaştırma içindir — beş bağımsız ölçümün ortak değeri.',
         ha='center', fontsize=9.2, color='#a1a1aa')
fig.subplots_adjust(left=.055, right=.986, top=.905, bottom=.098)
plt.savefig(os.path.join(CIK, 'yerel_lomega.png'), dpi=140,
            facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print('\n-> 94_YEREL_LOMEGA/  SONUC.csv · yerel_lomega.png')
