"""TAM SPARC GALERISI — 163 galaksinin donus egrisi ve iki model fiti.

6.5.3.4'un tablosu sayilari verir; bu galeri EGRI SEKILLERINI verir. Ikisi birlikte
denetlenebilirlik zincirini kapatir: hangi satirin hangi egriden geldigi gorulebilir.

Her panel: sari noktalar = SPARC olcumu (gercek hata cubuklari)
           gri noktali    = baryonik katki (Y* Evrenaki fitinden)
           mor kesik-nokta = LCDM NFW (c200 Dutton & Maccio 2014 iliskisinden), k=2
           yesil duz      = Evrenaki F1+F4, k=2
Panel basligi: galaksi adi + kazanan modelin rengi.
Siralama: V_max artan — soldan saga, yukaridan asagi. Boylece 6.5.3.3'un rejim
deseni gorsel olarak okunabilir: ustteki cuce panellerde yesil, alttaki kutleli
panellerde karisik.

Veri: SPARC (Lelli, McGaugh & Schombert 2016), Rotmod_LTG. Y_bul = 1.4*Y_disk.
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
        p, _ = curve_fit(f, D['R'], D['Vo'], sigma=D['eV'], p0=p0, bounds=(lo, hi), maxfev=600000)
    except Exception:
        return None
    mv = f(D['R'], *p)
    if not np.all(np.isfinite(mv)):
        return None
    c2 = float(np.sum(((mv - D['Vo']) / D['eV']) ** 2))
    return dict(p=p, mv=mv, c2i=c2 / max(D['N'] - len(p), 1))


S = []
for f in sorted(glob.glob(os.path.join(VERI, '*_rotmod.dat'))):
    D = yukle(f)
    if D is None or D['N'] < 6:
        continue
    L = ft(D, lambda R, Y, lg, _D=D: np.sqrt(np.maximum(Vbar2(_D, Y), 1e-9) + v_nfw2(R, 10 ** lg)),
           [0.5, 11.0], [0.05, 7.0], [2.0, 13.5])
    E = ft(D, lambda R, Y, b, _D=D: np.sqrt(np.maximum(Vbar2(_D, Y), 1e-9) + b * Mkaps(_D, Y)),
           [0.5, 4e-7], [0.05, 1e-12], [2.0, 1e-1])
    if L and E:
        S.append((D, L, E))
S.sort(key=lambda t: t[0]['Vmax'])
NG = len(S)
kazE = sum(1 for _, L, E in S if E['c2i'] < L['c2i'])
print("TAM SPARC GALERISI — %d galaksi; Evrenaki onde: %d (%%%.0f)" % (NG, kazE, 100 * kazE / NG))

NC = 12
NR = int(np.ceil(NG / NC))
fig = plt.figure(figsize=(NC * 1.85, NR * 1.42 + 0.9), facecolor='#121212')
gs = GridSpec(NR, NC, hspace=0.62, wspace=0.30,
              left=0.016, right=0.996, top=1 - 0.62 / (NR * 1.42 + 0.9), bottom=0.012)
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
    kz = E['c2i'] < L['c2i']
    a.set_title('%s' % D['g'], fontsize=5.6, color='#4ade80' if kz else '#c084fc', pad=1.6)
    a.text(0.03, 0.93, '%.0f' % D['Vmax'], transform=a.transAxes, fontsize=4.6,
           color='#888888', va='top')
    a.text(0.97, 0.06, '%.1f/%.1f' % (L['c2i'], E['c2i']), transform=a.transAxes,
           fontsize=4.4, color='#aaaaaa', ha='right', va='bottom')
    a.set_xlim(0, D['R'].max() * 1.04)
    a.set_ylim(0, max(D['Vo'].max(), L['mv'].max(), E['mv'].max()) * 1.30)

fig.text(0.5, 1 - 0.20 / (NR * 1.42 + 0.9),
         'Tüm SPARC Örneklemi — %d Galaksinin Dönüş Eğrisi ve İki Model Fiti '
         '($V_{max}$ artan sırada)' % NG,
         ha='center', fontsize=15, color='white')
fig.text(0.5, 1 - 0.40 / (NR * 1.42 + 0.9),
         'sarı: ölçüm  ·  gri noktalı: baryonlar  ·  mor kesik-nokta: ΛCDM NFW ($k{=}2$)  ·  '
         'yeşil düz: Evrenakı F1+F4 ($k{=}2$)  ·  başlık rengi = kazanan  ·  '
         'sol üst: $V_{max}$  ·  sağ alt: $\\chi^2_{ind}$ ΛCDM/Evrenakı',
         ha='center', fontsize=8.6, color='#999999')
plt.savefig('sparc_galeri_163.png', dpi=135, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print("Grafik 'sparc_galeri_163.png' olarak kaydedildi (%d satir x %d kolon)." % (NR, NC))
