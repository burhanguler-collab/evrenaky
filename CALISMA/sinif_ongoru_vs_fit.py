"""SINIF CALISMASI — ONGORU vs FIT.  Kullanim: python sinif_ongoru_vs_fit.py 01_erken_spiral

Bu betik bir sinif klasoru icin dort egriyi ayni panele koyar:

  1. OLCUM                      SPARC donus egrisi + gercek hata cubuklari
  2. STANDART BILIM ONGORUSU    LCDM, SIFIR serbest parametre
  3. EVRENAKI ONGORUSU          teori, SIFIR serbest parametre
  4. FITLER                     ikisinin de galaksi basina fitlenmis hali

Neden onemli. Bu kitapta simdiye kadar HER iki model de fitlendi ve karsilastirma
"kim daha iyi uyduruyor" sorusuydu. Oysa iki tarafin da parametresiz bir ONGORUSU
var ve o hic kurulmadi. Fitleme yeteneginden bagimsiz olarak "kim dogruyu
onceden soyluyor" sorusu ancak boyle sorulur.

--- 2. STANDART BILIM ONGORUSU (sifir serbest parametre) ---
  Y*        = 0,50                  populasyon sentezi orta degeri (3,6 mikron)
  M_*       = Y* x L[3.6]           ana katalogdan
  M_200     <- abundance matching   Moster ve ark. 2013, z=0 (M_* verildiginde M_halo)
  c_200     <- Dutton & Maccio 2014 (M_200 verildiginde konsantrasyon)
  v^2       = V_bar^2 + v_NFW^2
  Hicbiri donus egrisine bakilarak secilmedi. Bu, LCDM'in gercek ONGORUSUDUR.

--- 3. EVRENAKI ONGORUSU (sifir serbest parametre, NIHAI kurulum) ---
  Y*        = 0,50                  ayni girdi (adil olmasi icin)
  M_kaps(R) = Y*L_disk(R) + 1,4Y*L_kovan(R) + M_gaz(R)
  a_0       = 1,75 x cH_0/16,1 = 7,39e-11 m/s^2   kuresel kalibre sabit ([S])
  v^2       = V_bar^2 + sqrt(a_0 G M_kaps(R))     (yerel bicim; l_om = sqrt(G M/a_0))
  UYARI: a_0'in katsayisi SPARC'a kalibre edilmistir; bu yuzden "tam ongoru" degil,
  "galaksi basina ongoru"dur. Ayni sey LCDM tarafi icin de gecerlidir: c-M ve
  abundance matching iliskileri de kalibre edilmis iliskilerdir. Iki taraf bu
  bakimdan denktir.

--- 4. FITLER ---
  Evrenaki  : Y* ve b serbest        (k=2)
  LCDM      : Y* ve M_200 serbest    (k=2)
  Y* siniri : 0,05 - 2,0  (kitabin temel kurulumu)

Olcutler: RMS sapma (km/s) · chi2_ind · noktalarin kaci hata cubugu icinde.

Cikti: <sinif>/HESAP/  ->  SONUC.csv · YONTEM.md · ongoru_vs_fit.png
"""

import os
import sys
import glob
import csv
import warnings

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.optimize import curve_fit

warnings.filterwarnings('ignore')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
plt.style.use('dark_background')

KOK = os.path.dirname(os.path.abspath(__file__))
SINIF = sys.argv[1] if len(sys.argv) > 1 else '01_erken_spiral'
SDIR = os.path.join(KOK, 'SINIF_CALISMASI', SINIF)
HDIR = os.path.join(SDIR, 'HESAP')
os.makedirs(HDIR, exist_ok=True)

G = 4.300917e-6                       # kpc (km/s)^2 / Msun
C_SI = 2.99792458e8
ACC = 1e6 / 3.0856776e19              # (km/s)^2/kpc -> m/s^2
CH0 = (C_SI * (70e3 / 3.0857e22)) / ACC
A0 = CH0 / 16.1                       # kitabin eski kalibre degeri (tarihsel kayit)
# --- NIHAI KURULUM (1 Agustos 2026, karar: 86_NIHAI/CALISMA.md) ---------------
# 1) l_omega YEREL kutleden kurulur (94_YEREL_LOMEGA: aki teoremi geregi;
#    yaricap izi +0,56 -> -0,025, RMS -%19, yeni parametre YOK):
#        v_F4^2 = sqrt(A0N * G * M_kaps(R))
# 2) a_0 = 1,75 x (cH_0/16,1). Turetim (92_M_TUT: a_0 = G m_n/l_om^2, l_om
#    olcumu 35,7 fm) x1,75-x2,08 bandi verir; gozlem alt ucu secer:
#    x1,75'te dis sapma 0,0, BTFR egimi 3,734 (band ICI), RMS 12,8 < LCDM 14,6.
#    x2,08 BTFR egimini band disina (3,754) tasiyordu. Kayit: toplu_defter.
A0N = 1.75 * A0                       # NIHAI a_0
RHO_CRIT = 3 * 0.07 ** 2 / (8 * np.pi * G)
H_RED = 0.7
RB = 1.4                              # Y_kovan / Y_disk (SPARC kurali)
UPS_PS = 0.50                         # populasyon sentezi orta degeri
YLO, YHI = 0.05, 2.0

# Moster+2013 z=0 : M_*(M_h)  -> ters cevirerek M_h(M_*)
_lM1, _N, _be, _ga = 11.59, 0.0351, 1.376, 0.608
_Mh = 10 ** np.linspace(9.0, 15.0, 8000)
_Ms = _Mh * 2 * _N / ((_Mh / 10 ** _lM1) ** -_be + (_Mh / 10 ** _lM1) ** _ga)
Mhalo_am = lambda Ms: float(np.interp(Ms, _Ms, _Mh))


def c200_dm14(M200):
    return 10 ** (0.905 - 0.101 * np.log10(M200 * H_RED / 1e12))


def v_nfw2(R, M200, c200=None):
    cc = c200_dm14(M200) if c200 is None else c200
    r200 = (3 * M200 / (4 * np.pi * 200 * RHO_CRIT)) ** (1 / 3.0)
    rs = r200 / cc
    mu = lambda x: np.log(1 + x) - x / (1 + x)
    return G * M200 / R * mu(R / rs) / mu(cc)


# ---------------- veri + katalog ----------------
KAT = {r['Galaksi']: r for r in csv.DictReader(open(os.path.join(SDIR, 'KATALOG.csv'), encoding='utf-8'))}
GAL = []
for f in sorted(glob.glob(os.path.join(SDIR, 'veri', '*_rotmod.dat'))):
    ad = os.path.basename(f)[:-11]
    d = np.loadtxt(f)
    R, Vo, eV, Vg, Vd, Vb, SBd, SBb = [d[:, i] for i in range(8)]
    eV = np.maximum(eV, 1.0)
    Rp = R * 1e3
    L = lambda S: np.concatenate([[0.0], np.cumsum(
        np.pi * (Rp[1:] ** 2 - Rp[:-1] ** 2) * 0.5 * (S[1:] + S[:-1]))])
    GAL.append(dict(g=ad, R=R, Vo=Vo, eV=eV, Vg=Vg, Vd=Vd, Vb=Vb,
                    Ld=L(SBd), Lb=L(SBb), N=len(R),
                    L36=float(KAT[ad]['L36_1e9Lsun']) * 1e9, T=KAT[ad]['Tip_ad'] if 'Tip_ad' in KAT[ad] else '',
                    Q=int(KAT[ad]['Q']), inc=float(KAT[ad]['Inc_deg'])))
GAL.sort(key=lambda d: -d['Vo'].max())
print('%s : %d galaksi' % (SINIF, len(GAL)))

Vbar2 = lambda d, Y: np.sign(d['Vg']) * d['Vg'] ** 2 + Y * d['Vd'] ** 2 + RB * Y * d['Vb'] ** 2
Mgas = lambda d: np.maximum(d['R'] * np.sign(d['Vg']) * d['Vg'] ** 2 / G, 0.0)
Mkaps = lambda d, Y: Y * d['Ld'] + RB * Y * d['Lb'] + Mgas(d)


def evr_ongoru(d):
    """Sifir serbest parametre — NIHAI kurulum: yerel l_omega + a_0 nihai.

    v^2 = V_bar^2 + sqrt(A0N G M_kaps(R))     [eski: + G M_kaps / l_om(M_bar)]
    Rapor kolonu icin l_omega dis noktada verilir: l_om = sqrt(G M_bar/A0N).
    """
    M = np.maximum(Mkaps(d, UPS_PS), 1e-9)
    Mb = max(M[-1], 1e-6)
    lom = np.sqrt(G * Mb / A0N)
    return np.sqrt(np.maximum(Vbar2(d, UPS_PS), 1e-9) + np.sqrt(A0N * G * M)), \
        dict(lom=lom, Mbar=Mb)


def lcdm_ongoru(d):
    """Sifir serbest parametre: Y*=0,50 ; M200 abundance matching'den ; c200 D&M14'ten."""
    Ms = UPS_PS * d['L36']
    M200 = Mhalo_am(Ms)
    return np.sqrt(np.maximum(Vbar2(d, UPS_PS), 1e-9) + v_nfw2(d['R'], M200)), \
        dict(Mstar=Ms, M200=M200, c200=c200_dm14(M200))


def fitle(d, tur):
    if tur == 'evr':
        # NIHAI biçimin 2-parametreli fiti: v^2 = Vbar^2(Y) + (10^lb) sqrt(M_kaps(Y))
        # (eski: + (10^lb) M_kaps — parametre sayisi AYNI: Y*, lb)
        f = lambda R, Y, lb, _d=d: np.sqrt(np.maximum(Vbar2(_d, Y), 1e-9)
                                           + (10 ** lb) * np.sqrt(np.maximum(Mkaps(_d, Y), 1e-9)))
        p0, lo, hi = [0.5, np.log10(np.sqrt(A0N * G))], [YLO, -8], [YHI, 2]
    else:
        f = lambda R, Y, lg, _d=d: np.sqrt(np.maximum(Vbar2(_d, Y), 1e-9) + v_nfw2(R, 10 ** lg))
        p0, lo, hi = [0.5, 11.0], [YLO, 7.0], [YHI, 13.5]
    try:
        p, _ = curve_fit(f, d['R'], d['Vo'], sigma=d['eV'], p0=p0, bounds=(lo, hi), maxfev=600000)
    except Exception:
        return None, None
    mv = f(d['R'], *p)
    return (mv, p) if np.all(np.isfinite(mv)) else (None, None)


olc = lambda d, mv, k: dict(
    rms=float(np.sqrt(np.mean((mv - d['Vo']) ** 2))),
    ci=float(np.sum(((mv - d['Vo']) / d['eV']) ** 2) / max(d['N'] - k, 1)),
    ic=float(np.mean(np.abs(mv - d['Vo']) <= d['eV'])))

S = []
for d in GAL:
    eo, ei = evr_ongoru(d)
    lo_, li = lcdm_ongoru(d)
    ef, ep = fitle(d, 'evr')
    lf, lp = fitle(d, 'lcdm')
    bar = np.sqrt(np.maximum(Vbar2(d, UPS_PS), 0))
    S.append(dict(d=d, eo=eo, lo=lo_, ef=ef, lf=lf, bar=bar, ei=ei, li=li, ep=ep, lp=lp,
                  m_eo=olc(d, eo, 0), m_lo=olc(d, lo_, 0),
                  m_ef=olc(d, ef, 2) if ef is not None else None,
                  m_lf=olc(d, lf, 2) if lf is not None else None,
                  m_bar=olc(d, bar, 0),
                  dis=(lambda m: dict(e=float(np.mean((eo[m] - d['Vo'][m]) / d['Vo'][m])),
                                      l=float(np.mean((lo_[m] - d['Vo'][m]) / d['Vo'][m]))))(d['R'] > np.median(d['R']))))

# ---------------- SONUC.csv ----------------
with open(os.path.join(HDIR, 'SONUC.csv'), 'w', encoding='utf-8', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['Galaksi', 'N', 'Q', 'Inc_deg', 'Vmax_kms',
                'ONG_evr_rms', 'ONG_evr_chi2ind', 'ONG_evr_hataici',
                'ONG_lcdm_rms', 'ONG_lcdm_chi2ind', 'ONG_lcdm_hataici',
                'FIT_evr_rms', 'FIT_evr_chi2ind', 'FIT_evr_hataici', 'FIT_evr_Ystar',
                'FIT_lcdm_rms', 'FIT_lcdm_chi2ind', 'FIT_lcdm_hataici', 'FIT_lcdm_Ystar',
                'BAR_rms', 'ONG_evr_lomega_kpc', 'ONG_lcdm_M200_Msun', 'ONG_lcdm_c200',
                'DIS_evr_sapma_yuzde', 'DIS_lcdm_sapma_yuzde'])
    for s in S:
        d = s['d']
        row = [d['g'], d['N'], d['Q'], '%.1f' % d['inc'], '%.1f' % d['Vo'].max()]
        for k in ('m_eo', 'm_lo'):
            row += ['%.2f' % s[k]['rms'], '%.3f' % s[k]['ci'], '%.2f' % s[k]['ic']]
        for k, pk in (('m_ef', 'ep'), ('m_lf', 'lp')):
            row += (['%.2f' % s[k]['rms'], '%.3f' % s[k]['ci'], '%.2f' % s[k]['ic'],
                     '%.3f' % s[pk][0]] if s[k] else ['', '', '', ''])
        row += ['%.2f' % s['m_bar']['rms'], '%.2f' % s['ei']['lom'],
                '%.3e' % s['li']['M200'], '%.2f' % s['li']['c200'],
                '%+.1f' % (100 * s['dis']['e']), '%+.1f' % (100 * s['dis']['l'])]
        w.writerow(row)

med = lambda k, f: np.median([s[k][f] for s in S if s[k]])
print('  %-34s %8s %10s %10s' % ('', 'RMS', 'chi2_ind', 'hata ici'))
for k, ad in [('m_bar', 'yalniz baryonlar (Y*=0,50)'), ('m_lo', 'STANDART BILIM ONGORUSU (k=0)'),
              ('m_eo', 'EVRENAKI ONGORUSU (k=0)'), ('m_lf', 'LCDM fit (k=2)'),
              ('m_ef', 'Evrenaki fit (k=2)')]:
    print('  %-34s %8.2f %10.2f %9.0f%%' % (ad, med(k, 'rms'), med(k, 'ci'), 100 * med(k, 'ic')))
oe = sum(1 for s in S if s['m_eo']['rms'] < s['m_lo']['rms'])
print('  ONGORU yarisi: Evrenaki %d / %d galakside daha yakin' % (oe, len(S)))
de = np.array([s['dis']['e'] for s in S]); dl = np.array([s['dis']['l'] for s in S])
print('  DIS YARIDA ISARETLI SAPMA (ongoru-olcum)/olcum:')
print('    Evrenaki : medyan %+.1f%%   altta kalan %d/%d' % (100*np.median(de), int((de<0).sum()), len(S)))
print('    LCDM     : medyan %+.1f%%   ustte kalan %d/%d' % (100*np.median(dl), int((dl>0).sum()), len(S)))

# ---------------- grafik ----------------
NC = 4
NR = int(np.ceil(len(S) / NC))
H = NR * 2.55 + 2.05
fig = plt.figure(figsize=(NC * 3.5, H), facecolor='#121212')
gs = GridSpec(NR, NC, hspace=.40, wspace=.26, left=.055, right=.985,
              top=1 - 1.62 / H, bottom=.085)
for i, s in enumerate(S):
    d = s['d']
    a = fig.add_subplot(gs[i // NC, i % NC])
    a.set_facecolor('#121212')
    for sp in a.spines.values():
        sp.set_color('#3f3f46')
    a.plot(d['R'], s['bar'], ':', color='#71717a', lw=1.1, zorder=2)
    a.plot(d['R'], s['lf'], '--', color='#c4b5fd', lw=1.1, zorder=3) if s['lf'] is not None else None
    a.plot(d['R'], s['ef'], '--', color='#86efac', lw=1.1, zorder=4) if s['ef'] is not None else None
    a.plot(d['R'], s['lo'], '-', color='#7c3aed', lw=1.9, zorder=5)
    a.plot(d['R'], s['eo'], '-', color='#16a34a', lw=1.9, zorder=6)
    a.errorbar(d['R'], d['Vo'], yerr=d['eV'], fmt='o', color='#ffcc00', ms=3.2,
               elinewidth=.9, capsize=1.6, zorder=8)
    a.set_title('%s   ($Q{=}%d$, $i{=}%.0f°$)' % (d['g'], d['Q'], d['inc']),
                fontsize=8.6, color='#e5e5e5', pad=3)
    a.text(.03, .97, 'öngörü RMS\nEvr %.1f\nΛCDM %.1f' % (s['m_eo']['rms'], s['m_lo']['rms']),
           transform=a.transAxes, fontsize=6.8, va='top',
           color='#16a34a' if s['m_eo']['rms'] < s['m_lo']['rms'] else '#a78bfa')
    a.tick_params(labelsize=6.6, colors='#a1a1aa')
    a.set_xlim(0, d['R'].max() * 1.04)
    yy = [d['Vo'].max()] + [np.nanmax(v) for v in (s['eo'], s['lo']) if v is not None]
    a.set_ylim(0, max(yy) * 1.22)
    if i % NC == 0:
        a.set_ylabel('$V$ (km/s)', fontsize=8)
    if i // NC == NR - 1:
        a.set_xlabel('$R$ (kpc)', fontsize=8)

from matplotlib.lines import Line2D
eleman = [
    Line2D([], [], color='#ffcc00', marker='o', ls='', ms=5, label='ÖLÇÜM (SPARC, gerçek hata çubukları)'),
    Line2D([], [], color='#16a34a', lw=2.2, label='EVRENAKI ÖNGÖRÜSÜ — sıfır serbest parametre'),
    Line2D([], [], color='#7c3aed', lw=2.2, label='STANDART BİLİM ÖNGÖRÜSÜ — sıfır serbest parametre'),
    Line2D([], [], color='#86efac', lw=1.3, ls='--', label='Evrenakı fit ($\\Upsilon_*$, $b$ serbest)'),
    Line2D([], [], color='#c4b5fd', lw=1.3, ls='--', label='ΛCDM fit ($\\Upsilon_*$, $M_{200}$ serbest)'),
    Line2D([], [], color='#71717a', lw=1.3, ls=':', label='yalnız baryonlar ($\\Upsilon_*=0{,}50$)')]
fig.legend(handles=eleman, loc='upper center', bbox_to_anchor=(.5, 1 - .70 / H),
           ncol=3, fontsize=9.4, framealpha=.15)
fig.text(.5, 1 - .22 / H, 'Sınıf %s — Öngörü mü, Fit mi? (%d galaksi)'
         % (SINIF.replace('_', ' ').upper(), len(S)), ha='center', fontsize=15.5, color='white')
fig.text(.5, .022, 'Her iki modelin de SIFIR serbest parametreli öngörüsü kalın çizgidir; '
                   'kesikli çizgiler galaksi başına fitlenmiş hâllerdir. Öngörülerde ortak girdi '
                   '$\\Upsilon_*=0{,}50$ (popülasyon sentezi). '
                   'Panel içi sayı: öngörünün RMS sapması (km/s), rengi daha yakın olanı gösterir.',
         ha='center', fontsize=8.8, color='#a1a1aa')
plt.savefig(os.path.join(HDIR, 'ongoru_vs_fit.png'), dpi=150,
            facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print("  -> HESAP/ongoru_vs_fit.png · SONUC.csv")

# ---------------- YONTEM.md ----------------
with open(os.path.join(HDIR, 'YONTEM.md'), 'w', encoding='utf-8') as fh:
    fh.write(("""# Yöntem — @@SINIF@@ / öngörü vs fit

Üreten betik: `sinif_ongoru_vs_fit.py` · Çıktı: `SONUC.csv`, `ongoru_vs_fit.png`

## Dört eğri

| # | Eğri | Serbest parametre | Girdiler |
|---|---|---|---|
| 1 | **ÖLÇÜM** | — | SPARC `Rotmod_LTG`, gerçek hata çubukları |
| 2 | **Standart bilim öngörüsü** | **0** | @@YS@@; $M_*=\\Upsilon_*L_{3,6}$; $M_{200}\\leftarrow$ abundance matching (Moster+2013); $c_{200}\\leftarrow$ Dutton & Macciò 2014 |
| 3 | **Evrenakı öngörüsü** | **0** | @@YS@@; yerel biçim $v_{F4}^2=\\sqrt{a_0\\mathcal{G}M_{kaps}(R)}$; $a_0=1{,}75\\,cH_0/16{,}1=7{,}39\\times10^{-11}$ m/s² (nihai, 86_NIHAI) |
| 4 | Evrenakı fit | 2 | $\\Upsilon_*$, $b$ |
| 5 | ΛCDM fit | 2 | $\\Upsilon_*$, $M_{200}$ |

Öngörülerin ikisi de **dönüş eğrisine bakmadan** kurulur. Ortak girdi $\\Upsilon_*=0{,}50$
(3,6 μm popülasyon sentezi orta değeri) — adil olması için her ikisinde aynı.

## Denklemler

Baryonik katkı (her ikisinde ortak, SPARC ayrıştırmasından):

$$V_{bar}^2 = \\mathrm{sgn}(V_{gaz})V_{gaz}^2 + \\Upsilon_* V_{disk}^2 + 1{,}4\\,\\Upsilon_* V_{kovan}^2$$

Kapsanan kütle:

$$M_{kaps}(R) = \\Upsilon_* L_{disk}(R) + 1{,}4\\,\\Upsilon_* L_{kovan}(R) + M_{gaz}(R),
\\qquad M_{gaz}(R)=\\frac{R\\,\\mathrm{sgn}(V_{gaz})V_{gaz}^2}{\\mathcal{G}}$$

Evrenakı (nihai kurulum): $\\;v^2 = V_{bar}^2 + \\sqrt{a_0\\,\\mathcal{G}M_{kaps}(R)}$
(eşdeğer yazım: $\\mathcal{G}M_{kaps}/\\ell_\\omega^{etkin}(R)$, $\\ell_\\omega^{etkin}=\\sqrt{\\mathcal{G}M_{kaps}/a_0}$)

ΛCDM: $\\;v^2 = V_{bar}^2 + v_{NFW}^2(R;M_{200},c_{200})$

## Dürüstlük kaydı — hiçbir öngörü "saf" değildir

| Büyüklük | Statü |
|---|---|
| $a_0$ ($7{,}39\\times10^{-11}$ m/s²) | biçimi türetilmiş ($\\mathcal{G}m_n/\\ell_\\omega^2$), değeri SPARC'a **kalibre**; çapraz doğrulamada katsayı $\\pm$%40 oynar |
| $c_{200}$–$M_{200}$ katsayıları | N-cisim simülasyonlarına **fitlenmiş** iki sayı |
| Abundance matching | gözlemsel kütle fonksiyonuna **fitlenmiş** dört sayı |
| $\\Upsilon_*=0{,}50$ | IMF varsayımına bağlı bandın **orta değeri**, ölçülmüş bir sayı değil |

Yani bu, "türetim vs türetim" değil **"kalibre edilmiş öngörü vs kalibre edilmiş öngörü"**
karşılaştırmasıdır. İki taraf bu bakımdan denktir ve karşılaştırma bu nedenle adildir.

## Ölçütler

- `rms` — modelin ölçümden RMS sapması (km/s), ağırlıksız
- `chi2ind` — $\\chi^2/(N-k)$; öngörüler için $k=0$, fitler için $k=2$
- `hataici` — model noktalarının kaçı ölçüm hata çubuğunun içinde ($|z|\\leq1$)

`chi2ind`'in öngörüde $k=0$ ile hesaplandığına dikkat: öngörü hiç parametre harcamadığı için
bütün noktalar serbestlik derecesidir.
""").replace('@@YS@@', '$\\Upsilon_*=0{,}50$').replace('@@SINIF@@', SINIF))
print('  -> HESAP/YONTEM.md')
