"""TAM SPARC GALERISI (k=3) — Evrenaki'ya UCUNCU parametre eklenmis hali.

6.5.3.4'un galerisi Evrenaki'yi k=2 ile ($\\Upsilon_*$, b) gosteriyordu. Bu galeri
ucuncu parametreyi ekler: yayilma olcegi R_f (6.5.4.6).

  LCDM NFW  : Vbar^2 + NFW,  c200 Dutton & Maccio 2014 iliskisinden  -> k=2 (Y*, M200)
  Evrenaki  : Vbar^2 + b*M_kaps(R)/(1+R/R_f)                          -> k=3 (Y*, b, R_f)

DIKKAT — kazanan olcutu AIC'dir, ham ki-kare degil. Parametre sayilari farkli
oldugu icin ham chi2 karsilastirmasi Evrenaki'ya haksiz avantaj verir; AIC her
fazladan parametreyi +2 ile cezalandirir. Panel basligindaki renk AIC kazananini
gosterir; sag altta ham chi2_ind degerleri de yazilidir (LCDM/Evrenaki).

R_f ust sinira dayanan galaksilerde yayilma istenmemis demektir; o panellerde
model etkin olarak k=2'ye doner ve basliga * konur.

Veri: SPARC (Lelli, McGaugh & Schombert 2016), Rotmod_LTG. Y_bul = 1.4*Y_disk.
Siralama: V_max artan.
"""

import sys
import os
import glob
import warnings

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.optimize import curve_fit

warnings.filterwarnings('ignore')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
plt.style.use('dark_background')

G = 4.300917e-6
RHO_CRIT = 3 * 0.07 ** 2 / (8 * np.pi * G)
H_RED = 0.7
RF_UST = 3e3
VERI = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'veri')


def yukle(f):
    d = np.loadtxt(f)
    if d.ndim < 2 or len(d) < 6:
        return None
    D = dict(g=os.path.basename(f)[:-11], R=d[:, 0], Vo=d[:, 1],
             eV=np.maximum(d[:, 2], 1.0), Vg=d[:, 3], Vd=d[:, 4], Vb=d[:, 5],
             SBd=d[:, 6], SBb=d[:, 7])
    if np.any(D['R'] <= 0) or D['Vo'].max() <= 0:
        return None
    Rpc = D['R'] * 1e3
    L = lambda SB: np.concatenate([[0.0], np.cumsum(
        np.pi * (Rpc[1:] ** 2 - Rpc[:-1] ** 2) * 0.5 * (SB[1:] + SB[:-1]))])
    D['Ld'] = L(D['SBd'])
    D['Lb'] = L(D['SBb'])
    D['N'] = len(D['R'])
    D['kovan'] = bool(np.any(D['Vb'] > 0))
    D['Vmax'] = float(D['Vo'].max())
    return D


Vbar2 = lambda D, Y: np.sign(D['Vg']) * D['Vg'] ** 2 + Y * D['Vd'] ** 2 + 1.4 * Y * D['Vb'] ** 2
Mkaps = lambda D, Y: (Y * D['Ld'] + 1.4 * Y * D['Lb']
                      + np.maximum(D['R'] * np.sign(D['Vg']) * D['Vg'] ** 2 / G, 0.0))


def v_nfw2(R, M200):
    c = 10 ** (0.905 - 0.101 * np.log10(M200 * H_RED / 1e12))
    r200 = (3.0 * M200 / (4.0 * np.pi * 200.0 * RHO_CRIT)) ** (1.0 / 3.0)
    rs = r200 / c
    mu = lambda x: np.log(1.0 + x) - x / (1.0 + x)
    return G * M200 / R * mu(R / rs) / mu(c)


def ft(D, f, p0, lo, hi):
    try:
        p, _ = curve_fit(f, D['R'], D['Vo'], sigma=D['eV'], p0=p0, bounds=(lo, hi), maxfev=700000)
    except Exception:
        return None
    mv = f(D['R'], *p)
    if not np.all(np.isfinite(mv)):
        return None
    c2 = float(np.sum(((mv - D['Vo']) / D['eV']) ** 2))
    k = len(p)
    return dict(p=p, mv=mv, chi2=c2, c2i=c2 / max(D['N'] - k, 1), aic=c2 + 2 * k, k=k)


S = []
for f in sorted(glob.glob(os.path.join(VERI, '*_rotmod.dat'))):
    D = yukle(f)
    if D is None or D['N'] < 7:
        continue
    L = ft(D, lambda R, Y, lg, _D=D: np.sqrt(np.maximum(Vbar2(_D, Y), 1e-9) + v_nfw2(R, 10 ** lg)),
           [0.5, 11.0], [0.05, 7.0], [2.0, 13.5])
    E = ft(D, lambda R, Y, b, Rf, _D=D: np.sqrt(np.maximum(Vbar2(_D, Y), 1e-9)
                                                + b * Mkaps(_D, Y) / (1 + R / Rf)),
           [0.5, 6e-7, 20.0], [0.05, 1e-12, 0.3], [2.0, 1e-1, RF_UST])
    if L and E:
        S.append((D, L, E))
S.sort(key=lambda t: t[0]['Vmax'])
NG = len(S)

aic_kaz = sum(1 for _, L, E in S if E['aic'] < L['aic'])
chi_kaz = sum(1 for _, L, E in S if E['c2i'] < L['c2i'])
doy = sum(1 for _, _, E in S if E['p'][2] > 0.98 * RF_UST)
V = np.array([D['Vmax'] for D, _, _ in S])
dA = np.array([L['aic'] - E['aic'] for _, L, E in S])

print("TAM SPARC GALERISI (k=3) — %d galaksi" % NG)
print("=" * 78)
print("  Evrenaki k=3 vs LCDM k=2")
print("  AIC ile kazanan (adil olcut): Evrenaki %d/%d (%%%.0f)" % (aic_kaz, NG, 100 * aic_kaz / NG))
print("  ham chi2_ind ile             : Evrenaki %d/%d (%%%.0f)  <- adil DEGIL" % (chi_kaz, NG, 100 * chi_kaz / NG))
print("  R_f ust sinirda (yayilma istenmeyen): %d/%d (%%%.0f)" % (doy, NG, 100 * doy / NG))
print("-" * 78)
print("  medyan chi2_ind: LCDM %.2f   Evrenaki(k=3) %.2f"
      % (np.median([L['c2i'] for _, L, _ in S]), np.median([E['c2i'] for _, _, E in S])))
print("-" * 78)
print("%-16s %5s %10s %10s" % ('V_max bandi', 'n', 'Evr(AIC)', 'oran'))
for lo, hi, ad in [(0, 60, '<60'), (60, 80, '60-80'), (80, 120, '80-120'),
                   (120, 180, '120-180'), (180, 250, '180-250'), (250, 9999, '>250')]:
    m = (V >= lo) & (V < hi)
    if m.sum():
        print("%-16s %5d %10d %10s" % (ad, m.sum(), int(np.sum(dA[m] > 0)),
                                       '%.2f' % (np.sum(dA[m] > 0) / m.sum())))
print("=" * 78)

# --- GALERI ---
NC = 12
NR = int(np.ceil(NG / NC))
H = NR * 1.42 + 1.45
fig = plt.figure(figsize=(NC * 1.85, H), facecolor='#121212')
gs = GridSpec(NR, NC, hspace=0.62, wspace=0.30,
              left=0.016, right=0.996, top=1 - 1.16 / H, bottom=0.012)
for idx, (D, L, E) in enumerate(S):
    a = fig.add_subplot(gs[idx // NC, idx % NC])
    a.set_facecolor('#121212')
    for sp in a.spines.values():
        sp.set_color('#3a3a3a')
        sp.set_linewidth(0.6)
    a.set_xticks([])
    a.set_yticks([])
    a.errorbar(D['R'], D['Vo'], yerr=D['eV'], fmt='o', color='#ffcc00', ms=1.5,
               elinewidth=0.5, capsize=0, zorder=6)
    a.plot(D['R'], np.sqrt(np.maximum(Vbar2(D, E['p'][0]), 0)), ':', color='#777777',
           lw=0.8, zorder=2)
    a.plot(D['R'], L['mv'], '-.', color='#c084fc', lw=1.0, zorder=4)
    a.plot(D['R'], E['mv'], '-', color='#4ade80', lw=1.2, zorder=5)
    kz = E['aic'] < L['aic']
    yild = '*' if E['p'][2] > 0.98 * RF_UST else ''
    a.set_title('%s%s' % (D['g'], yild), fontsize=5.6,
                color='#4ade80' if kz else '#c084fc', pad=1.6)
    a.text(0.03, 0.93, '%.0f' % D['Vmax'], transform=a.transAxes, fontsize=4.6,
           color='#888888', va='top')
    a.text(0.97, 0.06, '%.1f/%.1f' % (L['c2i'], E['c2i']), transform=a.transAxes,
           fontsize=4.4, color='#aaaaaa', ha='right', va='bottom')
    a.set_xlim(0, D['R'].max() * 1.04)
    a.set_ylim(0, max(D['Vo'].max(), L['mv'].max(), E['mv'].max()) * 1.30)

fig.text(0.5, 1 - 0.30 / H,
         'Tüm SPARC Örneklemi — Evrenakı’ya Üçüncü Parametre Eklenmiş Hali '
         '($k{=}3$) · %d Galaksi' % NG, ha='center', fontsize=15, color='white')
fig.text(0.5, 1 - 0.60 / H,
         'sarı: ölçüm  ·  gri noktalı: baryonlar  ·  mor kesik-nokta: ΛCDM NFW ($k{=}2$)  ·  '
         'yeşil düz: Evrenakı $b\\,M_{kaps}/(1{+}R/R_f)$ ($k{=}3$)  ·  '
         'başlık rengi = AIC kazananı  ·  yıldız (*) = fit yayılma istemedi',
         ha='center', fontsize=8.6, color='#999999')
fig.text(0.5, 1 - 0.83 / H,
         'AIC kazananı: Evrenakı %d/%d (%%%.0f) — ham $\\chi^2$ ile %d/%d olurdu ama '
         'parametre sayısı eşit olmadığı için adil ölçüt AIC’dir  ·  sol üst: $V_{max}$  ·  '
         'sağ alt: $\\chi^2_{ind}$ ΛCDM/Evrenakı'
         % (aic_kaz, NG, 100 * aic_kaz / NG, chi_kaz, NG),
         ha='center', fontsize=8.0, color='#7dd3fc')
plt.savefig('sparc_galeri_163_k3.png', dpi=135, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print("Grafik 'sparc_galeri_163_k3.png' olarak kaydedildi (%d x %d)." % (NR, NC))
