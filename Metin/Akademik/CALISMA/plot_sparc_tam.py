"""TAM SPARC ORNEKLEMI — 163 galaksi: Core-Cusp deseni gercek mi?

Bu betik, teorinin galaktik iddiasinin son sinavidir. Onceki asamalar:
  6.5.3.1  tek galaksi (NGC 3198) — vaka calismasi
  6.5.3.2  12 galaksi — l_omega ve R_f'nin evrensel OLMADIGI gosterildi
  (ara asama) 31 galaksi — cuce rejiminde 9/9 gibi carpici bir desen goruldu

O 31 galaksilik ara sonuc SECIM YANLILIGI tasiyordu: cuce ornegi elle secilmisti
ve icinde literaturun bilinen Core-Cusp problem vakalari (DDO154, IC2574, NGC3109)
vardi. Bu betik yanliligi ortadan kaldirmak icin SPARC'in TAMAMINI kullanir:
indirilebilen 173 dosyanin fit edilebilen 163'u, hicbir secim yapilmadan.

Karsilastirma ESIT SERBESTLIKTEDIR (her iki modelde k=2):
  LCDM NFW  : Vbar^2 + NFW,  c200 Dutton & Maccio 2014 iliskisinden  -> (Y*, M200)
  Evrenaki  : Vbar^2 + b*M_kaps(R)                                   -> (Y*, b)
Olcut: dchi2_ind = chi2_LCDM - chi2_Evrenaki  (pozitif = Evrenaki daha iyi)

Kazanma oranlarina binom hatasi eklenir; 0.5'ten sapmanin anlamliligi sigma
cinsinden verilir. Boylece "desen var" iddiasi goz karariyla degil olculerek
degerlendirilir.

Veri: SPARC (Lelli, McGaugh & Schombert 2016), Rotmod_LTG. Y_bul = 1.4*Y_disk.
Negatif V_gas isaretli kare ile alinir; hatalar gercektir (errV, taban 1 km/s).
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
VERI_DIZIN = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'veri')


def yukle(f):
    d = np.loadtxt(f)
    if d.ndim < 2 or len(d) < 6:
        return None
    D = dict(g=os.path.basename(f).replace('_rotmod.dat', ''),
             R=d[:, 0], Vo=d[:, 1], eV=np.maximum(d[:, 2], 1.0),
             Vg=d[:, 3], Vd=d[:, 4], Vb=d[:, 5], SBd=d[:, 6], SBb=d[:, 7])
    if np.any(D['R'] <= 0) or D['Vo'].max() <= 0:
        return None
    Rpc = D['R'] * 1e3
    L = lambda SB: np.concatenate([[0.0], np.cumsum(
        np.pi * (Rpc[1:] ** 2 - Rpc[:-1] ** 2) * 0.5 * (SB[1:] + SB[:-1]))])
    D['Ld'] = L(D['SBd'])
    D['Lb'] = L(D['SBb'])
    D['kovan'] = bool(np.any(D['Vb'] > 0))
    D['Vmax'] = float(D['Vo'].max())
    D['N'] = len(D['R'])
    return D


def Vbar2(D, Y):
    return np.sign(D['Vg']) * D['Vg'] ** 2 + Y * D['Vd'] ** 2 + 1.4 * Y * D['Vb'] ** 2


def Mkaps(D, Y):
    return (Y * D['Ld'] + 1.4 * Y * D['Lb']
            + np.maximum(D['R'] * np.sign(D['Vg']) * D['Vg'] ** 2 / G, 0.0))


def v_nfw2(R, M200):
    c200 = 10 ** (0.905 - 0.101 * np.log10(M200 * H_RED / 1e12))
    r200 = (3.0 * M200 / (4.0 * np.pi * 200.0 * RHO_CRIT)) ** (1.0 / 3.0)
    rs = r200 / c200
    mu = lambda x: np.log(1.0 + x) - x / (1.0 + x)
    return G * M200 / R * mu(R / rs) / mu(c200)


def fitle(D, f, p0, lo, hi):
    try:
        p, _ = curve_fit(f, D['R'], D['Vo'], sigma=D['eV'], p0=p0,
                         bounds=(lo, hi), maxfev=600000)
    except Exception:
        return None
    mv = f(D['R'], *p)
    if not np.all(np.isfinite(mv)):
        return None
    chi2 = float(np.sum(((mv - D['Vo']) / D['eV']) ** 2))
    return dict(p=p, chi2i=chi2 / max(D['N'] - len(p), 1))


res, atl = [], 0
for f in sorted(glob.glob(os.path.join(VERI_DIZIN, '*_rotmod.dat'))):
    D = yukle(f)
    if D is None or D['N'] < 6:
        atl += 1
        continue
    L = fitle(D, lambda R, Y, lg, _D=D: np.sqrt(np.maximum(Vbar2(_D, Y), 1e-9) + v_nfw2(R, 10 ** lg)),
              [0.5, 11.0], [0.05, 7.0], [2.0, 13.5])
    E = fitle(D, lambda R, Y, b, _D=D: np.sqrt(np.maximum(Vbar2(_D, Y), 1e-9) + b * Mkaps(_D, Y)),
              [0.5, 4e-7], [0.05, 0], [2.0, 1e-1])
    if L and E:
        res.append((D, L, E))
    else:
        atl += 1

V = np.array([D['Vmax'] for D, _, _ in res])
cL = np.array([L['chi2i'] for _, L, _ in res])
cE = np.array([E['chi2i'] for _, _, E in res])
dC = cL - cE
kov = np.array([D['kovan'] for D, _, _ in res])
adlar = np.array([D['g'] for D, _, _ in res])
NG = len(res)

BANT = [(0, 60, '<60'), (60, 80, '60–80'), (80, 120, '80–120'),
        (120, 180, '120–180'), (180, 250, '180–250'), (250, 9999, '>250')]


def binom(k, n):
    if n == 0:
        return 0.0, 0.0, 0.0
    p = k / n
    s = np.sqrt(max(p * (1 - p), 1e-9) / n)
    return p, s, (p - 0.5) / s if s > 0 else 0.0


# --- Rapor ---
print("TAM SPARC ORNEKLEMI — %d galaksi fitlendi (%d atlandi), esit serbestlik k=2" % (NG, atl))
print("=" * 90)
p_all, s_all, z_all = binom(int(np.sum(dC > 0)), NG)
print("GENEL: Evrenaki %d/%d galakside daha iyi = %%%.0f +- %%%.0f  (0.5'ten %.1f sigma)"
      % (int(np.sum(dC > 0)), NG, 100 * p_all, 100 * s_all, z_all))
print()
print("%-12s %5s %9s %14s %12s %10s %10s" % ('V_max bandi', 'n', 'Evr onde',
      'oran +- hata', 'sigma', 'med LCDM', 'med Evr'))
print("-" * 90)
for lo, hi, ad in BANT:
    m = (V >= lo) & (V < hi)
    if not m.sum():
        continue
    p, s, z = binom(int(np.sum(dC[m] > 0)), int(m.sum()))
    print("%-12s %5d %9d %14s %12s %10.2f %10.2f"
          % (ad, m.sum(), int(np.sum(dC[m] > 0)), '%.2f ± %.2f' % (p, s),
             '%+.1f' % z, np.median(cL[m]), np.median(cE[m])))
print("-" * 90)
print("\nKABA UC BANT:")
for lo, hi, ad in [(0, 80, 'CUCE/LSB <80'), (80, 150, 'ORTA 80-150'), (150, 9999, 'KUTLELI >150')]:
    m = (V >= lo) & (V < hi)
    p, s, z = binom(int(np.sum(dC[m] > 0)), int(m.sum()))
    print("  %-14s n=%3d  Evr onde %3d (%%%.0f ± %%%.0f, %.1f sigma)  medyan chi2i: LCDM %.2f / Evr %.2f"
          % (ad, m.sum(), int(np.sum(dC[m] > 0)), 100 * p, 100 * s, z,
             np.median(cL[m]), np.median(cE[m])))
print("\nKOVAN KIRILIMI:")
for kk, ad in [(False, 'kovansiz'), (True, 'kovanli ')]:
    m = kov == kk
    p, s, z = binom(int(np.sum(dC[m] > 0)), int(m.sum()))
    print("  %s n=%3d  Evr onde %3d (%%%.0f ± %%%.0f)" % (ad, m.sum(), int(np.sum(dC[m] > 0)),
                                                         100 * p, 100 * s))
print("\nFORMEL DISLAMA (chi2_ind > 10):")
print("  LCDM dislanan     : %d/%d" % (int(np.sum(cL > 10)), NG))
print("  Evrenaki dislanan : %d/%d" % (int(np.sum(cE > 10)), NG))
print("=" * 90)

# --- GRAFIK ---
fig = plt.figure(figsize=(16.5, 9.2), facecolor='#121212')
gs = GridSpec(2, 3, width_ratios=[2.0, 1, 1], height_ratios=[1.15, 1],
              hspace=0.33, wspace=0.28, left=0.062, right=0.985, top=0.895, bottom=0.085)
axm = fig.add_subplot(gs[:, 0])
axf = fig.add_subplot(gs[0, 1:])
axc = fig.add_subplot(gs[1, 1])
axh = fig.add_subplot(gs[1, 2])
for a in (axm, axf, axc, axh):
    a.set_facecolor('#121212')
    for sp in ('top', 'right'):
        a.spines[sp].set_visible(False)
    for sp in ('bottom', 'left'):
        a.spines[sp].set_color('#444444')
    a.tick_params(colors='#aaaaaa', labelsize=8.5)
    a.grid(True, alpha=0.14, color='white')

# (A) dagilim + bantli medyan
axm.axhspan(0, 12, color='#4ade80', alpha=0.05, zorder=0)
axm.axhspan(-12, 0, color='#c084fc', alpha=0.05, zorder=0)
axm.axhline(0, color='#ffffff', lw=1.2, alpha=0.5, zorder=2)
axm.scatter(V[~kov], np.clip(dC[~kov], -11.6, 11.6), s=26, c='#ffa040', alpha=0.72,
            edgecolor='none', zorder=4, label='kovansız (n=%d)' % int(np.sum(~kov)))
axm.scatter(V[kov], np.clip(dC[kov], -11.6, 11.6), s=34, c='#f472b6', marker='s',
            alpha=0.78, edgecolor='none', zorder=4, label='kovanlı (n=%d)' % int(np.sum(kov)))
bx, by, bs = [], [], []
for lo, hi, ad in BANT:
    m = (V >= lo) & (V < hi)
    if m.sum() >= 4:
        bx.append(np.sqrt(max(lo, 30) * min(hi, 400)))
        by.append(np.median(dC[m]))
        bs.append(1.253 * np.std(dC[m]) / np.sqrt(m.sum()))
axm.errorbar(bx, by, yerr=bs, fmt='o-', color='#7dd3fc', ms=8, lw=2.4, capsize=4,
             zorder=7, label='bant medyanı ± hata')
axm.set_xscale('log')
axm.set_xlim(28, 420)
axm.set_ylim(-12, 12)
axm.set_xlabel('$V_{max}$ (km/s)  —  dinamik kütlenin vekili', fontsize=10.5, color='#cccccc')
axm.set_ylabel('$\\Delta\\chi^2_{ind}=\\chi^2_{\\Lambda CDM}-\\chi^2_{Evrenak\\imath}$',
               fontsize=10.5, color='#cccccc')
axm.set_title('Tüm SPARC örneklemi — %d galaksi, eşit serbestlik ($k=2$)' % NG,
              fontsize=11.8, color='white', pad=9)
axm.text(0.015, 0.965, 'Evrenakı daha iyi', transform=axm.transAxes, ha='left', va='top',
         fontsize=10, color='#4ade80', weight='bold')
axm.text(0.015, 0.035, 'ΛCDM daha iyi', transform=axm.transAxes, ha='left', va='bottom',
         fontsize=10, color='#c084fc', weight='bold')
lg = axm.legend(fontsize=8.6, facecolor='#1a1a1a', edgecolor='#333333', loc='lower right')
for t in lg.get_texts():
    t.set_color('white')

# (B) kazanma orani + binom hatasi
xs, ps, ss, ns, ets = [], [], [], [], []
for i, (lo, hi, ad) in enumerate(BANT):
    m = (V >= lo) & (V < hi)
    if not m.sum():
        continue
    p, s, z = binom(int(np.sum(dC[m] > 0)), int(m.sum()))
    xs.append(i)
    ps.append(p)
    ss.append(s)
    ns.append(int(m.sum()))
    ets.append(ad)
axf.axhline(0.5, color='#ffffff', ls='--', lw=1.2, alpha=0.6)
axf.bar(xs, ps, yerr=ss, width=0.62, capsize=4,
        color=['#4ade80' if p > 0.5 else '#c084fc' for p in ps], alpha=0.9,
        error_kw=dict(ecolor='#dddddd', lw=1.2))
for x, p, n in zip(xs, ps, ns):
    axf.text(x, 0.035, 'n=%d' % n, ha='center', fontsize=7.8, color='#1a1a1a', weight='bold')
    axf.text(x, p + 0.045, '%.2f' % p, ha='center', fontsize=8.4, color='#dddddd')
axf.set_xticks(xs)
axf.set_xticklabels(ets, fontsize=8.4, color='#cccccc')
axf.set_ylim(0, 0.95)
axf.set_ylabel('Evrenakı’nın kazanma oranı', fontsize=9.4, color='#bbbbbb')
axf.set_xlabel('$V_{max}$ bandı (km/s)', fontsize=9.4, color='#bbbbbb')
axf.set_title('Kazanma oranı — binom hatasıyla ($0{,}5$ = beraberlik)',
              fontsize=10.6, color='white', pad=7)

# (C) bant medyan chi2
xs2 = np.arange(len(ets))
mLs = [np.median(cL[(V >= lo) & (V < hi)]) for lo, hi, ad in BANT if ((V >= lo) & (V < hi)).sum()]
mEs = [np.median(cE[(V >= lo) & (V < hi)]) for lo, hi, ad in BANT if ((V >= lo) & (V < hi)).sum()]
axc.plot(xs2, mLs, 'o-.', color='#c084fc', lw=2.0, ms=6, label='ΛCDM')
axc.plot(xs2, mEs, 'o-', color='#4ade80', lw=2.2, ms=6, label='Evrenakı')
axc.axhline(1.0, color='#ffcc00', ls=':', lw=1.2, alpha=0.7)
axc.text(0.03, 1.05, 'kabul sınırı $\\chi^2_{ind}=1$', transform=axc.get_yaxis_transform(),
         fontsize=7.2, color='#ffcc00')
axc.set_xticks(xs2)
axc.set_xticklabels(ets, fontsize=7.4, rotation=40, color='#cccccc')
axc.set_ylabel('medyan $\\chi^2_{ind}$', fontsize=9.2, color='#bbbbbb')
axc.set_title('Bant medyan uyumu', fontsize=10.2, color='white', pad=6)
lg3 = axc.legend(fontsize=8, facecolor='#1a1a1a', edgecolor='#333333', loc='upper left')
for t in lg3.get_texts():
    t.set_color('white')

# (D) formel dislama
kat = ['ΛCDM\ndışlanan', 'Evrenakı\ndışlanan', 'ikisi de\nkabul']
her = int(np.sum((cL <= 10) & (cE <= 10)))
vals = [int(np.sum(cL > 10)), int(np.sum(cE > 10)), her]
axh.bar([0, 1, 2], vals, width=0.6, color=['#c084fc', '#4ade80', '#888888'], alpha=0.9)
for i, v in enumerate(vals):
    axh.text(i, v + 2, str(v), ha='center', fontsize=9.4, color='#dddddd')
axh.set_xticks([0, 1, 2])
axh.set_xticklabels(kat, fontsize=8, color='#cccccc')
axh.set_ylabel('galaksi sayısı', fontsize=9.2, color='#bbbbbb')
axh.set_ylim(0, max(vals) * 1.22)
axh.set_title('Formel dışlama ($\\chi^2_{ind}>10$)', fontsize=10.2, color='white', pad=6)

m80 = V < 80
p80, s80, z80 = binom(int(np.sum(dC[m80] > 0)), int(m80.sum()))
fig.text(0.5, 0.955, 'Cüce/LSB rejiminde ($V_{max}<80$) Evrenakı %d/%d = %%%.0f ± %%%.0f '
                     '($%.1f\\sigma$); kütleli rejimde beraberlik'
         % (int(np.sum(dC[m80] > 0)), int(m80.sum()), 100 * p80, 100 * s80, z80),
         ha='center', fontsize=10.0, color='#aaaaaa')
plt.savefig('sparc_tam_ornek.png', dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print("Grafik 'sparc_tam_ornek.png' olarak kaydedildi.")
