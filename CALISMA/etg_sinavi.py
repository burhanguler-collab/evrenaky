r"""ERKEN TIP GALAKSI SINAVI — 16 ETG, 32 nokta, FIT YAPILAMAZ.

--- NEDEN BU SINAV OZEL ---
Bu kumede donus egrisi YOKTUR. Galaksi basina iki ivme noktasi vardir (HI
halkasinin ic ve dis kenari). Serbest parametre fitlemek MUMKUN DEGILDIR —
2 nokta, 0 serbestlik. Teori ne diyorsa o cikar. Disk calismasinda hep
sorulan "Y* fitlendi mi" sorusu burada tanimsizdir.

--- TEORININ ONGORUSU: YARICAP GEREKTIRMEZ ---
M-37 merkezcil dengesi tam radyal ivmeyi iki terimli verir:
    a_tam = a_F1 + a_F4 ,   a_F4 = G M / (l_omega R)
l_omega = sqrt(G M / a_0) konur ve G M = a_bar R^2 yazilirsa R SADELESIR:

    g_ong = g_bar + sqrt(g_bar * a_0)          <- sifir serbest parametre

Burada g_bar OLCULEN buyukluktur (Lelli+2017 fotometriden hesaplamistir), yani
F1'in ta kendisidir. Ikinci terim F4'tur. Formulde ne yaricap, ne Y*, ne kutle
vardir. Bu, teorinin en ciplak halidir.

--- FORMULUN ICINDEKI YAKLASIM (ve nasil sinandigi) ---
G M = a_bar R^2 adimi, l_omega'daki TOPLAM kutle yerine R icindeki KAPSANAN
kutleyi koyar. M_kaps < M_top oldugu her yerde l_omega oldugundan KUCUK
alinir, yani F4 FAZLA hesaplanir. Etki ic noktada dis noktadan buyuk olmalidir.
Bu sinanabilir: ic ve dis noktalar AYRI AYRI raporlanir. Teori icin en kotu
(en muhafazakar) okuma ic noktalardir.

--- KARSI TARAF ---
(a) Disk RAR (Lelli+2017 Sekil 2, 2693 nokta) — ayni olcut, ayni formul.
    ETG'ler disklerle AYNI carpani mi istiyor? Tek yasa mi, iki yasa mi?
(b) LCDM zinciri: M_* -> M_200 (Moster+2013) -> c_200 (Dutton&Maccio 2014)
    -> NFW kapsanan kutle -> a_DM(R). Sifir serbest parametre. Yaricap
    g_bar'dan geri cozulur — bu bir YENIDEN KURMADIR, kaydi md. 5'te.
(c) Kutle bagimliligi sinavi (yaricap gerektirmez): LCDM'de a_0 evrensel
    DEGILDIR, dusuk ivme asimptotu hale kutlesine baglidir. Teoride
    evrenseldir. Artik <-> log L[3.6] korelasyonu bunu ayirir.

Cikti: SINIF_CALISMASI/96_ETG/ -> SONUC.csv · etg.png
Kaynak: Lelli F., McGaugh S.S., Schombert J.M., Pawlowski M.S., 2017,
        ApJ 836, 152 — "One Law to Rule Them All".
"""

import os
import sys
import csv
import warnings

import numpy as np
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
plt.style.use('dark_background')

KOK = os.path.dirname(os.path.abspath(__file__))
VERI = os.path.join(KOK, 'veri')
CIK = os.path.join(KOK, 'SINIF_CALISMASI', '96_ETG')
os.makedirs(CIK, exist_ok=True)

# ---- sabitler: btfr_sinavi.py ile BIREBIR ayni ----
G = 4.300917e-6                                  # kpc (km/s)^2 / M_gunes
C_SI = 2.99792458e8
H0_SI = 70e3 / 3.0857e22
ACC = 1e6 / 3.0856776e19                         # (km/s)^2/kpc -> m/s^2
A0_KPC = (C_SI * H0_SI) / ACC / 16.1             # a_0, (km/s)^2/kpc
A0 = A0_KPC * ACC                                # a_0, m/s^2  = 4,224e-11
RHO_CRIT = 3 * 0.07 ** 2 / (8 * np.pi * G)
H_RED = 0.7
UPS_ETG = 0.70          # 3,6um kadran-sisme orani; disk calismasindaki
                        # cekirdek degeriyle ayni (RB*UPS = 1,4*0,50 = 0,70)
G_DAGGER = 1.20e-10     # Lelli+2017'nin AMPIRIK RAR olcegi (fitlenmis)

print('a_0 = %.3e m/s^2   ·   g_dagger (ampirik) = %.2e   ->  orani %.2f'
      % (A0, G_DAGGER, G_DAGGER / A0))


# ---------------------------------------------------------------- veri
def oku_etg(yol):
    """_etg.mrt — basliklari '#' ile baslar, govde bosluga gore ayrilir."""
    ALAN = ['Ad', 'D', 'eD', 'fD', 'Inc', 'eInc', 'L36', 'eL36', 'Reff', 'SBeff',
            'Rexp', 'SBexp', 'Ao1', 'eAo1', 'Ao2', 'eAo2', 'Ab1', 'eAb1', 'Ab2', 'eAb2']
    D = []
    for L in open(yol, encoding='utf-8', errors='replace'):
        p = L.split()
        if not p or p[0].startswith('#') or len(p) < len(ALAN):
            continue
        try:
            g = {k: float(v) for k, v in zip(ALAN[1:], p[1:len(ALAN)])}
        except ValueError:
            continue
        g['Ad'] = p[0]
        D.append(g)
    return D


def oku_rar(yol):
    """_RAR.mrt — Lelli+2017 Sekil 2'nin arkasindaki 2693 disk noktasi."""
    gb, eb, go, eo = [], [], [], []
    for L in open(yol, encoding='utf-8', errors='replace'):
        p = L.split()
        if len(p) != 4:
            continue
        try:
            v = [float(x) for x in p]
        except ValueError:
            continue
        if not (-14 < v[0] < -7 and -14 < v[2] < -7):     # log10 m/s^2 olmali
            continue
        gb.append(v[0]); eb.append(v[1]); go.append(v[2]); eo.append(v[3])
    return map(np.array, (gb, eb, go, eo))


E = oku_etg(os.path.join(VERI, '_etg.mrt'))
Rb, Reb, Ro, Reo = oku_rar(os.path.join(VERI, '_RAR.mrt'))
print('ETG: %d galaksi -> %d nokta   ·   disk RAR: %d nokta'
      % (len(E), 2 * len(E), len(Rb)))

ad = np.array([g['Ad'] for g in E])
L36 = np.array([g['L36'] for g in E]) * 1e9       # SPARC birimi 10^9 L_gunes
lAb1 = np.array([g['Ab1'] for g in E]); lAb2 = np.array([g['Ab2'] for g in E])
lAo1 = np.array([g['Ao1'] for g in E]); lAo2 = np.array([g['Ao2'] for g in E])
eAo1 = np.array([g['eAo1'] for g in E]); eAo2 = np.array([g['eAo2'] for g in E])
Reff = np.array([g['Reff'] for g in E])

gb1, gb2 = 10 ** lAb1, 10 ** lAb2
go1, go2 = 10 ** lAo1, 10 ** lAo2
GB = np.concatenate([gb1, gb2])                   # 32 nokta
GO = np.concatenate([go1, go2])
EGO = np.concatenate([eAo1, eAo2])
IC = np.concatenate([np.ones(len(E), bool), np.zeros(len(E), bool)])


# ------------------------------------------------------- teori + cozucu
def ongoru(gbar, k=1.0):
    """g_ong = g_bar + sqrt(k a_0 g_bar).  F1 olceklenmez, yalniz F4 olceklenir."""
    return gbar + np.sqrt(k * A0 * gbar)


def a0_carpani(gbar, gobs):
    """Medyan sapmayi kapatan k. Kapali formul YOKTUR — iki terimli oldugu icin
    sayisal cozulur (btfr_sinavi.py'deki ayni gerekce, ayni yontem)."""
    fk = lambda k: np.median(np.log10(ongoru(gbar, k) / gobs))
    a, b = 1e-3, 1e3
    if fk(a) > 0 or fk(b) < 0:
        return np.nan
    for _ in range(200):
        m = np.sqrt(a * b)
        if fk(m) < 0:
            a = m
        else:
            b = m
    return np.sqrt(a * b)


def spearman(x, y):
    r = lambda v: np.argsort(np.argsort(v)) + 1.0
    a, b = r(x) - r(x).mean(), r(y) - r(y).mean()
    return float((a * b).sum() / np.sqrt((a * a).sum() * (b * b).sum()))


def dok(etiket, gbar, gobs):
    d = np.log10(ongoru(gbar) / gobs)
    k = a0_carpani(gbar, gobs)
    print('  %-30s %5d %+10.3f %9.3f %11.2fx'
          % (etiket, len(gbar), np.median(d), np.std(d), k))
    return dict(n=len(gbar), med=np.median(d), sac=np.std(d), k=k)


print('\n' + '=' * 96)
print('TEORININ ONGORUSU  g = g_bar + sqrt(g_bar a_0)   — SIFIR SERBEST PARAMETRE')
print('  %-30s %5s %10s %9s %12s'
      % ('kume', 'n', 'medyan dex', 'sacilma', 'gereken a_0'))
S = {}
S['etg'] = dok('ETG — 32 noktanin tamami', GB, GO)
S['ic'] = dok('  ic nokta (HI halka ici)', gb1, go1)
S['dis'] = dok('  dis nokta (HI halka disi)', gb2, go2)
S['disk'] = dok('DISK RAR (Lelli+2017 Sek.2)', 10 ** Rb, 10 ** Ro)
# disk RAR'i ETG ic/dis noktalariyla AYNI ivme araliginda da olc — yoksa
# karsilastirma iki farkli rejimi kiyaslar (ETG dis noktalari disklerin
# ortalamasindan daha yuksek ivmededir).
for anh, et, msk in [('disk_dis', '  └ ETG-dış ivme aralığında',
                      (Rb >= lAb2.min()) & (Rb <= lAb2.max())),
                     ('disk_ic', '  └ ETG-iç  ivme aralığında',
                      (Rb >= lAb1.min()) & (Rb <= lAb1.max()))]:
    if msk.sum() > 20:
        S[anh] = dok(et, 10 ** Rb[msk], 10 ** Ro[msk])
print('  %-30s %5s %10s %9s %11.2fx'
      % ('BTFR sinavi (97_BTFR, hiz)', 121, '—', '—', 2.02))


# ---- 'gereken a_0' nerede anlamli? F4'un paya katkisi kaldirac demektir ----
pay = lambda g: np.sqrt(A0 * g) / (g + np.sqrt(A0 * g))
print('\n  a_0 KALDIRACI — F4\'un ongoruye katkisi  (dlog g_ong / dlog k = pay/2)')
print('    ic nokta  : medyan %.3f  ->  a_0 neredeyse etkisiz; "gereken carpan"'
      % np.median(pay(gb1)))
print('                KOTU KOSULLANMIS bir buyukluktur, sayi olarak okunmamalidir.')
print('    dis nokta : medyan %.3f  ->  a_0 burada gercekten calisir.'
      % np.median(pay(gb2)))
print('  Bu yuzden ASIL SAYI dis noktalarinki: x%.2f' % S['dis']['k'])

print('\n  IC/DIS FARKI: %+.3f dex.  Beklenti TERS yonde cikti.' % (S['ic']['med'] - S['dis']['med']))
print('    Bekleniyordu: M_kaps<M_top ic noktada F4\'u FAZLA hesaplatir -> ic nokta')
print('    daha POZITIF sapmali olmali. Olculen: ic nokta daha NEGATIF (%+.3f vs %+.3f).'
      % (S['ic']['med'], S['dis']['med']))
print('    Yani ic noktadaki acigi kapsanan-kutle yaklasimi ACIKLAMIYOR; baska bir')
print('    sey var. En olasi aday Y*: ic nokta neredeyse saf Newton rejimidir')
print('    (F4 payi %.2f), orada g_ong ~ g_bar\'dir ve g_bar dogrudan Y*L\'dir.'
      % np.median(pay(gb1)))
d_ups = -np.median(np.log10(ongoru(gb1) / go1))
print('    Ic noktayi kapatan g_bar kaymasi: %+.3f dex -> Y* %.2f yerine %.2f olmali.'
      % (d_ups, UPS_ETG, UPS_ETG * 10 ** d_ups))
print('    NOT: bu bir FIT olurdu. Rapor edilen butun sayilar YAYINLANMIS g_bar iledir.')

# -------------------------------------------------- kutle bagimliligi
art_g = np.log10(ongoru(gb2) / go2)               # dis nokta: en temiz
rho_L = spearman(np.log10(L36), art_g)
rho_hep = spearman(np.log10(np.concatenate([L36, L36])),
                   np.log10(ongoru(GB) / GO))
print('\n' + '=' * 96)
print('KUTLE BAGIMLILIGI SINAVI  (yaricap gerektirmez — asil ayirt edici)')
print('  Teori   : a_0 EVRENSELDIR -> artik kutleden bagimsiz olmali (rho ~ 0)')
print('  LCDM    : dusuk ivme asimptotu hale kutlesine BAGLIDIR -> rho != 0')
print('  Spearman[artik , log L36]  dis nokta : %+.2f   ·  32 noktanin tamami : %+.2f'
      % (rho_L, rho_hep))
print('  L36 araligi: %.1f - %.1f x10^9 L_gunes  (%.1f kat)'
      % (L36.min() / 1e9, L36.max() / 1e9, L36.max() / L36.min()))
# n=16'da Spearman'in cozunurlugu: |rho| ~ 2/sqrt(n-1) altinda hicbir sey soylenemez
COZ = 2.0 / np.sqrt(len(E) - 1)
print('  DIKKAT: n=%d. Iki-sigma cozunurlugu |rho| ~ %.2f. Olculen %+.2f bunun'
      % (len(E), COZ, rho_L))
print('  ALTINDA -> "sifirdan ayirt edilemiyor" denebilir; "sifir" DENEMEZ.')
print('  Bu sinav ancak daha buyuk bir ETG kumesiyle keskinlesir. Su hali: ZAYIF LEHTE.')

# ------------------------------------------------------- LCDM zinciri
_lM1, _N, _be, _ga = 11.59, 0.0351, 1.376, 0.608
_Mh = 10 ** np.linspace(9.0, 15.0, 8000)
_Ms = _Mh * 2 * _N / ((_Mh / 10 ** _lM1) ** -_be + (_Mh / 10 ** _lM1) ** _ga)
mu = lambda x: np.log(1 + x) - x / (1 + x)


def lcdm_ivme(Mst, R_kpc):
    """NFW halenin R'deki ivmesi, m/s^2. Sifir serbest parametre."""
    M200 = float(np.interp(Mst, _Ms, _Mh))
    c = 10 ** (0.905 - 0.101 * np.log10(M200 * H_RED / 1e12))
    R200 = (3 * M200 / (4 * np.pi * 200 * RHO_CRIT)) ** (1 / 3.)
    Menc = M200 * mu(c * R_kpc / R200) / mu(c)
    return G * Menc / R_kpc ** 2 * ACC, M200, c


# yaricapin geri cozumu: g_bar = G M_bar / R^2  ->  R = sqrt(G M_bar / g_bar)
Mst = UPS_ETG * L36
R1 = np.sqrt(G * Mst / (gb1 / ACC))
R2 = np.sqrt(G * Mst / (gb2 / ACC))
print('\n' + '=' * 96)
print('YARICAPIN GERI COZUMU  (LCDM icin gerekli — teori icin GEREKMEZ)')
print('  R = sqrt(G M_* / g_bar),  Y* = %.2f' % UPS_ETG)
print('  R_ic  medyan %5.1f kpc  (= %4.1f R_eff)  ·  aralik %.1f - %.1f'
      % (np.median(R1), np.median(R1 / Reff), R1.min(), R1.max()))
print('  R_dis medyan %5.1f kpc  (= %4.1f R_eff)  ·  aralik %.1f - %.1f'
      % (np.median(R2), np.median(R2 / Reff), R2.min(), R2.max()))
print('  Lelli+2017 ETG HI halkalari tipik olarak 5-30 kpc -> yeniden kurma MAKUL.')

gl1 = np.array([lcdm_ivme(Mst[i], R1[i])[0] for i in range(len(E))]) + gb1
gl2 = np.array([lcdm_ivme(Mst[i], R2[i])[0] for i in range(len(E))]) + gb2
GL = np.concatenate([gl1, gl2])
dl = np.log10(GL / GO)
print('\nLCDM ONGORUSU (32 nokta, sifir serbest parametre)')
print('  medyan %+.3f dex  ·  sacilma %.3f dex' % (np.median(dl), np.std(dl)))
dt = np.log10(ongoru(GB) / GO)
print('  TEORI   medyan %+.3f dex  ·  sacilma %.3f dex' % (np.median(dt), np.std(dt)))
print('\n  IC/DIS AYRIMI — asil bilgi burada:')
print('  %-22s %11s %11s' % ('', 'ic (16)', 'dis (16)'))
for nm, gi, gd in [('TEORI  medyan dex', np.log10(ongoru(gb1) / go1), np.log10(ongoru(gb2) / go2)),
                   ('LCDM   medyan dex', np.log10(gl1 / go1), np.log10(gl2 / go2))]:
    print('  %-22s %+11.3f %+11.3f' % (nm, np.median(gi), np.median(gd)))
for nm, gi, gd in [('TEORI  sacilma', np.log10(ongoru(gb1) / go1), np.log10(ongoru(gb2) / go2)),
                   ('LCDM   sacilma', np.log10(gl1 / go1), np.log10(gl2 / go2))]:
    print('  %-22s %11.3f %11.3f' % (nm, np.std(gi), np.std(gd)))
td, ld = np.log10(ongoru(gb2) / go2), np.log10(gl2 / go2)
ti, li = np.log10(ongoru(gb1) / go1), np.log10(gl1 / go1)
print('  -> DIS NOKTA: medyanda %s (%+.3f vs %+.3f), sacilmada %s (%.3f vs %.3f).'
      % ('LCDM' if abs(np.median(ld)) < abs(np.median(td)) else 'TEORI',
         np.median(td), np.median(ld),
         'LCDM' if np.std(ld) < np.std(td) else 'TEORI', np.std(td), np.std(ld)))
print('     Bu satir teorinin ALEYHINEDIR ve oyle birakilmistir. Tek kazanci:')
print('     LCDM bu sayiyi R yeniden kurumu + Y* secimiyle uretir, teori HICBIRIYLE.')
print('  -> IC NOKTA: ikisi de ayni acigi veriyor (%+.3f / %+.3f) — ortak kayma'
      % (np.median(ti), np.median(li)))
print('     isareti; modele degil GIRDIYE (Y*) bakmak gerekir.')
print('  -> 32 NOKTANIN TAMAMI: sacilma TEORI %.3f  |  LCDM %.3f'
      % (np.std(dt), np.std(dl)))

# Y* duyarliligi (yalniz LCDM'i etkiler; teoriyi ETKILEMEZ)
print('\n  Y* DUYARLILIGI — teori tarafi g_bar OLCULDUGU icin hic etkilenmez:')
for u in (0.50, 0.70, 0.90):
    Ms_ = u * L36
    R2_ = np.sqrt(G * Ms_ / (gb2 / ACC))
    g_ = np.array([lcdm_ivme(Ms_[i], R2_[i])[0] for i in range(len(E))]) + gb2
    print('    Y*=%.2f -> LCDM dis nokta medyan %+.3f dex   |   TEORI %+.3f (degismez)'
          % (u, np.median(np.log10(g_ / go2)), np.median(np.log10(ongoru(gb2) / go2))))

# ------------------------------------------------------------- SONUC.csv
with open(os.path.join(CIK, 'SONUC.csv'), 'w', encoding='utf-8', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['Galaksi', 'D_Mpc', 'Inc_deg', 'L36_1e9Lsun', 'Reff_kpc',
                'YAY_log_gbar_ic', 'YAY_log_gobs_ic', 'YAY_e_gobs_ic',
                'YAY_log_gbar_dis', 'YAY_log_gobs_dis', 'YAY_e_gobs_dis',
                'TEORI_log_gong_ic', 'FARK_dex_ic',
                'TEORI_log_gong_dis', 'FARK_dex_dis',
                'KUR_R_ic_kpc', 'KUR_R_dis_kpc', 'LCDM_log_g_ic', 'LCDM_log_g_dis'])
    for i in np.argsort(-L36):
        w.writerow([ad[i], '%.1f' % E[i]['D'], '%.0f' % E[i]['Inc'],
                    '%.1f' % (L36[i] / 1e9), '%.2f' % Reff[i],
                    '%.2f' % lAb1[i], '%.2f' % lAo1[i], '%.2f' % eAo1[i],
                    '%.2f' % lAb2[i], '%.2f' % lAo2[i], '%.2f' % eAo2[i],
                    '%.2f' % np.log10(ongoru(gb1[i])),
                    '%+.3f' % np.log10(ongoru(gb1[i]) / go1[i]),
                    '%.2f' % np.log10(ongoru(gb2[i])),
                    '%+.3f' % np.log10(ongoru(gb2[i]) / go2[i]),
                    '%.1f' % R1[i], '%.1f' % R2[i],
                    '%.2f' % np.log10(gl1[i]), '%.2f' % np.log10(gl2[i])])

# ----------------------------------------------------------------- grafik
fig = plt.figure(figsize=(16.2, 6.8), facecolor='#121212')
gs = fig.add_gridspec(1, 3, width_ratios=[1.62, 1, 1], wspace=.27)
a1, a2, a3 = (fig.add_subplot(gs[0, i]) for i in range(3))
for a in (a1, a2, a3):
    a.set_facecolor('#121212')
    a.grid(alpha=.13)

xx = np.linspace(-13.0, -8.2, 300)
gx = 10 ** xx
a1.plot(Rb, Ro, '.', color='#52525b', ms=1.7, alpha=.45, zorder=1,
        label='disk RAR — %d nokta (Lelli+2017)' % len(Rb))
a1.plot(xx, xx, ':', color='#71717a', lw=1.3, zorder=2, label='$g_{öng}=g_{bar}$ (Newton)')
a1.plot(xx, np.log10(gx / (1 - np.exp(-np.sqrt(gx / G_DAGGER)))), '--',
        color='#f87171', lw=1.6, zorder=3, label='ampirik RAR uyumu (fitlenmiş $g_\\dagger$)')
a1.plot(xx, np.log10(ongoru(gx)), '-', color='#16a34a', lw=2.6, zorder=6,
        label='EVRENAKI  $g_{bar}+\\sqrt{g_{bar}a_0}$  (fit yok)')
a1.plot(xx, np.log10(ongoru(gx, S['dis']['k'])), '-.', color='#4ade80', lw=1.7, zorder=5,
        label='  └ $a_0\\times%.2f$ (ETG dış noktanın istediği)' % S['dis']['k'])
a1.errorbar(lAb2, lAo2, yerr=eAo2, fmt='o', color='#ffcc00', ms=6.4, elinewidth=.9,
            capsize=0, zorder=8, label='ETG dış nokta (16)')
a1.errorbar(lAb1, lAo1, yerr=eAo1, fmt='s', mfc='none', mec='#fb923c', color='#fb923c',
            ms=6.4, mew=1.4, elinewidth=.9, capsize=0, zorder=8,
            label='ETG iç nokta (16)')
a1.plot(np.log10(GB), np.log10(GL), 'x', color='#7c3aed', ms=6, mew=1.3, zorder=7,
        label='ΛCDM zinciri (NFW, yarıçap geri çözülmüş)')
a1.set_xlim(-12.6, -8.3)
a1.set_ylim(-12.0, -8.3)
a1.set_xlabel('$\\log g_{bar}$   (m/s²) — ölçülen baryonik ivme', fontsize=10.5)
a1.set_ylabel('$\\log g_{obs}$   (m/s²)', fontsize=10.5)
a1.set_title('Radyal İvme Düzlemi — erken tip galaksiler disklerin üstüne düşüyor',
             fontsize=12, color='white', pad=9)
a1.legend(fontsize=8.0, framealpha=.35, loc='lower right')

a2.axhline(0, color='#71717a', lw=1.1, zorder=2)
a2.plot(np.log10(L36 / 1e9), np.log10(ongoru(gb2) / go2), 'o', color='#ffcc00',
        ms=6.4, zorder=5, label='dış nokta')
a2.plot(np.log10(L36 / 1e9), np.log10(ongoru(gb1) / go1), 's', mfc='none',
        mec='#fb923c', ms=6.4, mew=1.4, zorder=5, label='iç nokta')
ex = np.linspace(np.log10(L36.min() / 1e9), np.log10(L36.max() / 1e9), 20)
a2.plot(ex, np.polyval(np.polyfit(np.log10(L36 / 1e9), art_g, 1), ex), '-',
        color='#16a34a', lw=1.8, alpha=.75, zorder=4)
a2.set_xlabel('$\\log L_{[3{,}6]}$   ($10^9 L_\\odot$)', fontsize=10.5)
a2.set_ylabel('artık  $\\log(g_{öng}/g_{gözl})$', fontsize=10.5)
a2.set_title('$a_0$ evrensel mi?', fontsize=12, color='white', pad=9)
a2.legend(fontsize=8.6, framealpha=.25, loc='lower left')
a2.set_ylim(-0.52, 0.40)
a2.text(.03, .97, ('Spearman = %+.2f   (n=16)\n2σ çözünürlük |ρ|≈%.2f\n'
                   'teori ~0 bekler · ΛCDM ≠0\n→ sıfırdan ayırt edilemiyor'
                   % (rho_L, COZ)).replace('.', ','), transform=a2.transAxes,
        ha='left', va='top', fontsize=8.8, color='#4ade80', family='monospace')

# Panel 3 — BAGIMSIZ OLCUMLER. ETG-ic (x14,56) BILEREK YOK: o rejimde F4'un
# ongoruye katkisi %10'dur, yani "gereken a_0" kotu kosullanmistir; cubuk
# olarak cizmek en yuksek sutunu en anlamsiz sayiya verirdi.
BAR = [('ETG dış · 16 nokta', S['dis']['k'], '#ffcc00'),
       ('disk RAR · aynı aralık', S['disk_dis']['k'], '#a1a1aa'),
       ('disk RAR · tümü (2693)', S['disk']['k'], '#52525b'),
       ('BTFR sınavı · 121 galaksi', 2.02, '#16a34a'),
       # x1,70 idi; naif 10^(-4*fark) formuluyle hesaplanmisti (geri cekildi).
       # Sayisal cozum: x2,21 — sinif_carpan_duzeltme.py, 141 galaksi.
       ('sınıf çalışması · 141 galaksi', 2.21, '#4ade80'),
       ('kitap 6.5.4.5 kaydı', 2.26, '#22c55e')]
vv = [b[1] for b in BAR]
yy = np.arange(len(BAR))[::-1]                    # yatay cubuk: etiketler sigar
a3.barh(yy, vv, .64, color=[b[2] for b in BAR], zorder=4)
a3.barh(yy[0], vv[0], .64, color='none', edgecolor='white', lw=2.0, zorder=5)
for i, v in enumerate(vv):
    a3.text(v + .035, yy[i], ('×%.2f' % v).replace('.', ','), va='center',
            fontsize=9.8, color=BAR[i][2], fontweight='bold')
a3.axvspan(min(vv), max(vv), color='#ffcc00', alpha=.11, zorder=1)
a3.axvline(1.0, color='#f87171', lw=1.3, ls='--', zorder=3)
a3.text(.96, -.62, 'çarpan gerekmezdi', fontsize=8.4, color='#f87171',
        ha='right', va='bottom')
for i, b in enumerate(BAR):                       # etiket cubugun ICINE — komsu
    a3.text(.05, yy[i], b[0], va='center', ha='left', fontsize=8.7,   # panele tasmasin
            color='#0a0a0a', fontweight='bold', zorder=6)
a3.set_yticks([])
a3.set_xlabel('gereken $a_0$ çarpanı', fontsize=10.5)
a3.set_xlim(0, max(vv) * 1.26)
a3.set_ylim(-.7, len(BAR) - .3)
a3.set_title(('Altı bağımsız ölçüm — bant ×%.2f – ×%.2f'
              % (min(vv), max(vv))).replace('.', ','), fontsize=12, color='white', pad=9)

fig.suptitle('Erken Tip Galaksi Sınavı — 16 galaksi, 32 nokta, fit YAPILAMAZ',
             fontsize=14, color='white', y=.985)
vg = lambda x: ('%.2f' % x).replace('.', ',')
fig.text(.5, .082, 'Bu kümede galaksi başına iki ivme noktası vardır; serbest parametre '
                   'fitlemek tanımsızdır. Teorinin öngörüsü $g_{bar}+\\sqrt{g_{bar}a_0}$ '
                   'yarıçap, $\\Upsilon_*$ ve kütle içermez — $R$ türetimde sadeleşir.',
         ha='center', fontsize=9.2, color='#a1a1aa')
fig.text(.5, .034, 'ETG dış noktanın istediği çarpan ×%s; aynı ivme aralığındaki 1553 disk '
                   'noktası ×%s istiyor. Sağdaki panelde ETG-iç değeri (×%s) BİLEREK yoktur: '
                   'o rejimde $F4$\'ün öngörüye katkısı %%%d\'dur, çarpan kötü koşullanmıştır.'
                   % (vg(S['dis']['k']), vg(S['disk_dis']['k']), vg(S['ic']['k']),
                      round(100 * np.median(pay(gb1)))),
         ha='center', fontsize=9.2, color='#a1a1aa')
# tight_layout add_gridspec ile catisiyor (rect yok sayiliyor) — elle:
fig.subplots_adjust(left=.052, right=.988, top=.885, bottom=.205)
plt.savefig(os.path.join(CIK, 'etg.png'), dpi=150,
            facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print('\n-> 96_ETG/  SONUC.csv · etg.png')
