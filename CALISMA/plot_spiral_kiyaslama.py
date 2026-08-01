"""YALNIZ SPIRAL OLCEKTE KIYASLAMA — GERCEK HUBBLE TIPLERIYLE.

Soru. Onceki bolumlerin karsilastirmalari SPARC'in TAMAMI uzerinden yapildi ve
orneklem cuce/duzensiz/LSB sistemleri de iceriyordu. 6.5.3.3'un iddiasi soyleydi:
"teorinin cephesi duz donus egrisi degil, Core-Cusp rejimidir." Bu betik o iddiayi
DOGRUDAN sinar: kiyaslamayi yalnizca SPIRAL olcekte tekrarlar.

Veri. SPARC ana katalogu (Lelli, McGaugh & Schombert 2016, Table 1;
astroweb.cwru.edu/SPARC/SPARC_Lelli2016c.mrt -> veri/_sparc.mrt) indirilmis ve
Hubble tipi T dogrudan okunmustur:
    T = 0 S0 | 1 Sa | 2 Sab | 3 Sb | 4 Sbc | 5 Sc | 6 Scd | 7 Sd
        8 Sdm | 9 Sm | 10 Im | 11 BCD
SPIRAL = T 1-7 (Sa-Sd).  Mercekseller (T=0) ve cuce/duzensizler (T>=8) ayri tutulur.

Onceki surumde Hubble tipi yoktu ve yapisal bir VEKIL kullanilmisti
(v_max>=80 km/s VE yildiz katkisi>gaz katkisi). Bu surum vekili gercek tiple
degistirir; betik ayrica vekilin ne kadar tuttugunu da raporlar.
"""

import sys
import os
import glob
import warnings

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

warnings.filterwarnings('ignore')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
plt.style.use('dark_background')

G = 4.300917e-6
C_SI = 2.99792458e8
ACC = 1e6 / 3.0856776e19
CH0 = (C_SI * (70e3 / 3.0857e22)) / ACC
A0 = CH0 * ((6.07e33 / C_SI ** 2) / 2.702e17) ** 2
RHO_CRIT = 3 * 0.07 ** 2 / (8 * np.pi * G)
H_RED = 0.7
RB = 1.4
VERI = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'veri')
TIP_AD = {0: 'S0', 1: 'Sa', 2: 'Sab', 3: 'Sb', 4: 'Sbc', 5: 'Sc',
          6: 'Scd', 7: 'Sd', 8: 'Sdm', 9: 'Sm', 10: 'Im', 11: 'BCD'}


def ana_katalog():
    """SPARC Table 1'i okur.

    UYARI: dosyanin byte-by-byte basligi T icin '12-13' diyor, ama gercek satirlarda
    alan bir bayt kaymistir (T, 13-14'tedir). Sabit genislikli okuma bu yuzden
    sessizce yanlis sonuc verir — herkese T=1 atar. Bunun yerine belirtec (token)
    tabanli okuma kullanilir: galaksi adlarinda bosluk yoktur, dolayisiyla
    1. belirtec ad, 2. belirtec T, sondan 4. belirtec Q'dur.
    """
    yol = os.path.join(VERI, '_sparc.mrt')
    ham = open(yol, encoding='utf-8', errors='replace').read().split('\n')
    ayr = [i for i, x in enumerate(ham) if x.startswith('----')]
    kat = {}
    for satir in ham[ayr[-1] + 1:]:
        p = satir.split()
        if len(p) < 19:
            continue
        try:
            kat[p[0]] = dict(T=int(p[1]), Q=int(p[-2]))
        except ValueError:
            continue
    if not kat:
        raise SystemExit('ana katalog ayristirilamadi')
    return kat


def yukle(f, kat):
    d = np.loadtxt(f)
    if d.ndim < 2 or len(d) < 6:
        return None
    R, Vo, eV, Vg, Vd, Vb, SBd, SBb = [d[:, i] for i in range(8)]
    eV = np.maximum(eV, 1.0)
    if np.any(R <= 0) or Vo.max() <= 0:
        return None
    ad = os.path.basename(f)[:-11]
    if ad not in kat:
        return None
    Rp = R * 1e3
    L = lambda S: np.concatenate([[0.0], np.cumsum(
        np.pi * (Rp[1:] ** 2 - Rp[:-1] ** 2) * 0.5 * (S[1:] + S[:-1]))])
    Ld, Lb = L(SBd), L(SBb)
    return dict(g=ad, T=kat[ad]['T'], Q=kat[ad]['Q'], R=R, Vo=Vo, eV=eV, Vg=Vg, Vd=Vd, Vb=Vb,
                Ld=Ld, Lb=Lb, N=len(R), V=float(Vo.max()),
                yil=float((Vd ** 2 + RB * Vb ** 2).max()), gaz=float((np.abs(Vg) ** 2).max()),
                BT=float(Lb[-1] / max(Ld[-1] + Lb[-1], 1e-9)))


Vbar2 = lambda d, Y: np.sign(d['Vg']) * d['Vg'] ** 2 + Y * d['Vd'] ** 2 + RB * Y * d['Vb'] ** 2
Mkaps = lambda d, Y: Y * d['Ld'] + RB * Y * d['Lb'] + np.maximum(
    d['R'] * np.sign(d['Vg']) * d['Vg'] ** 2 / G, 0.0)


def v_nfw2(R, M200):
    cc = 10 ** (0.905 - 0.101 * np.log10(M200 * H_RED / 1e12))
    r200 = (3 * M200 / (4 * np.pi * 200 * RHO_CRIT)) ** (1 / 3.0)
    rs = r200 / cc
    mu = lambda x: np.log(1 + x) - x / (1 + x)
    return G * M200 / R * mu(R / rs) / mu(cc)


def go(d, g, p0, lo, hi):
    try:
        p, _ = curve_fit(g, d['R'], d['Vo'], sigma=d['eV'], p0=p0, bounds=(lo, hi), maxfev=600000)
    except Exception:
        return None
    mv = g(d['R'], *p)
    if not np.all(np.isfinite(mv)):
        return None
    return float(np.sum(((mv - d['Vo']) / d['eV']) ** 2))


EV2 = lambda d, lo, hi: go(d, lambda R, Y, lb, _d=d: np.sqrt(
    np.maximum(Vbar2(_d, Y), 1e-9) + (10 ** lb) * Mkaps(_d, Y)),
    [min(max(0.5, lo), hi), -6.4], [lo, -12], [hi, -1])
LCD = lambda d, lo, hi: go(d, lambda R, Y, lg, _d=d: np.sqrt(
    np.maximum(Vbar2(_d, Y), 1e-9) + v_nfw2(R, 10 ** lg)),
    [min(max(0.5, lo), hi), 11.0], [lo, 7.0], [hi, 13.5])

kat = ana_katalog()
D = [x for x in (yukle(f, kat) for f in sorted(glob.glob(os.path.join(VERI, '*_rotmod.dat')))) if x]
print("SPARC ANA KATALOGU okundu: %d galaksi eslesti (katalogda %d kayit)" % (len(D), len(kat)))
dag = {}
for d in D:
    dag[d['T']] = dag.get(d['T'], 0) + 1
print("  Hubble tipi dagilimi: " + " · ".join(
    "%s(T=%d):%d" % (TIP_AD.get(t, '?'), t, dag[t]) for t in sorted(dag)))

# --- vekil ne kadar tuttu? ---
gercek = set(d['g'] for d in D if 1 <= d['T'] <= 7)
vekil = set(d['g'] for d in D if d['V'] >= 80 and d['yil'] > d['gaz'])
print("  VEKIL DENETIMI: gercek spiral %d, vekil %d, kesisim %d"
      % (len(gercek), len(vekil), len(gercek & vekil)))
print("    vekilin kacirdigi (gercek spiral ama vekil degil) : %d" % len(gercek - vekil))
print("    vekilin fazladan aldigi (spiral degil ama vekil)  : %d  -> %s"
      % (len(vekil - gercek), ", ".join("%s(%s)" % (g, TIP_AD.get(
          next(d['T'] for d in D if d['g'] == g), '?')) for g in sorted(vekil - gercek))[:150]))

ALT = [('SPİRAL (Sa–Sd)', [d for d in D if 1 <= d['T'] <= 7]),
       ('cüce/düzensiz (Sdm–BCD)', [d for d in D if d['T'] >= 8]),
       ('mercekssel (S0)', [d for d in D if d['T'] == 0])]
ALT = [(a, b) for a, b in ALT if len(b) >= 5]
KOS = [('$\\Upsilon_*$ serbest', 0.05, 2.0), ('$\\Upsilon_*$ bantlı', 0.3, 0.8)]
sig = lambda k, n: (k - n / 2.0) / np.sqrt(n / 4.0)

R = {}
for aad, alt in ALT:
    for kad, lo, hi in KOS:
        E, L, NN, GG = [], [], [], []
        for d in alt:
            a, b = EV2(d, lo, hi), LCD(d, lo, hi)
            if a is not None and b is not None:
                E.append(a); L.append(b); NN.append(d['N']); GG.append(d)
        E, L, NN = map(np.array, (E, L, NN))
        n = len(E)
        R[(aad, kad)] = dict(E=E, L=L, NN=NN, GG=GG, n=n, Nd=NN.sum(),
                             mE=np.median(E / np.maximum(NN - 2, 1)),
                             mL=np.median(L / np.maximum(NN - 2, 1)),
                             w=int(np.sum(E < L)), d=E.sum() - L.sum())

for aad, _ in ALT:
    print("=" * 100)
    print("%s  (%d galaksi)" % (aad, R[(aad, KOS[0][0])]['n']))
    print("  %-22s %11s %11s %10s %9s %13s" %
          ('koşul', 'medyan Evr', 'medyan ΛCDM', 'oy', 'sigma', 'dBIC ölçekli'))
    for kad, _, _ in KOS:
        r = R[(aad, kad)]
        f = min(r['E'].sum(), r['L'].sum()) / max(r['Nd'] - 2 * r['n'], 1)
        print("  %-22s %11.3f %11.3f %5d/%-4d %+8.1f %+13.0f"
              % (kad.replace('$\\Upsilon_*$', 'Y*'), r['mE'], r['mL'], r['w'], r['n'],
                 sig(r['w'], r['n']), r['d'] / f))

# --- alt tip kirilimi (spiraller icinde) ---
print("=" * 100)
print("SPIRALLER ICINDE ALT TIP KIRILIMI  (Y* serbest / bantlı, Evrenaki onde %)")
print("  %-10s %5s %16s %16s" % ('tip', 'N', 'Y* serbest', 'Y* bantlı'))
for t in range(1, 8):
    alt = [d for d in D if d['T'] == t]
    if len(alt) < 4:
        continue
    sat = []
    for kad, lo, hi in KOS:
        w = nn = 0
        for d in alt:
            a, b = EV2(d, lo, hi), LCD(d, lo, hi)
            if a is not None and b is not None:
                nn += 1; w += (a < b)
        sat.append((w, nn))
    print("  %-10s %5d %10d/%-3d %%%3.0f %10d/%-3d %%%3.0f"
          % (TIP_AD[t], len(alt), sat[0][0], sat[0][1], 100 * sat[0][0] / max(sat[0][1], 1),
             sat[1][0], sat[1][1], 100 * sat[1][0] / max(sat[1][1], 1)))
print("=" * 100)
sp_s = R[('SPİRAL (Sa–Sd)', KOS[0][0])]
sp_b = R[('SPİRAL (Sa–Sd)', KOS[1][0])]
cc_s = R[('cüce/düzensiz (Sdm–BCD)', KOS[0][0])]
cc_b = R[('cüce/düzensiz (Sdm–BCD)', KOS[1][0])]
print("HUKUM (gercek Hubble tipleriyle):")
print("  SPIRAL (Sa-Sd, n=%d) : serbest Y* oy %%%.0f (%.1f sig) | bantli Y* oy %%%.0f (%.1f sig)"
      % (sp_s['n'], 100 * sp_s['w'] / sp_s['n'], sig(sp_s['w'], sp_s['n']),
         100 * sp_b['w'] / sp_b['n'], sig(sp_b['w'], sp_b['n'])))
print("  CUCE  (Sdm-BCD, n=%d): serbest Y* oy %%%.0f (%.1f sig) | bantli Y* oy %%%.0f (%.1f sig)"
      % (cc_s['n'], 100 * cc_s['w'] / cc_s['n'], sig(cc_s['w'], cc_s['n']),
         100 * cc_b['w'] / cc_b['n'], sig(cc_b['w'], cc_b['n'])))

# ------------------------------ Grafik ---------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15.4, 6.5), facecolor='#121212')
x = np.arange(len(ALT))
w = 0.19

ax1.set_facecolor('#121212')
for i, (aad, _) in enumerate(ALT):
    for j, (off, key, col) in enumerate([(-1.5 * w, 'mE', '#4ade80'), (-0.5 * w, 'mE', '#f87171'),
                                         (0.5 * w, 'mL', '#a78bfa'), (1.5 * w, 'mL', '#6d5cc4')]):
        v = R[(aad, KOS[j % 2][0])][key]
        ax1.bar(i + off, v, w, color=col, zorder=4)
        ax1.text(i + off, v + 0.07, '%.2f' % v, ha='center', fontsize=8.6, color=col, fontweight='bold')
ax1.axhline(1.0, color='#888888', ls=':', lw=1.0, zorder=2)
ax1.text(.98, .045, 'kabul sınırı', transform=ax1.transAxes, fontsize=8.2, color='#888888', ha='right')
ax1.set_xticks(x)
ax1.set_xticklabels(['%s\n%d galaksi' % (a, R[(a, KOS[0][0])]['n']) for a, _ in ALT], fontsize=9.6)
ax1.set_ylabel('Medyan $\\chi^2_{ind}$', fontsize=11)
ax1.set_title('Teorinin evi spiraller değil', fontsize=12.5, color='white', pad=9)
from matplotlib.patches import Patch
ax1.legend(handles=[Patch(color='#4ade80', label='Evrenakı — $\\Upsilon_*$ serbest'),
                    Patch(color='#f87171', label='Evrenakı — $\\Upsilon_*$ bantlı'),
                    Patch(color='#a78bfa', label='ΛCDM — $\\Upsilon_*$ serbest'),
                    Patch(color='#6d5cc4', label='ΛCDM — $\\Upsilon_*$ bantlı')],
           fontsize=8.4, framealpha=.25, loc='upper right')
ax1.grid(alpha=.13, axis='y')

ax2.set_facecolor('#121212')
for i, (aad, _) in enumerate(ALT):
    for j, (off, col) in enumerate([(-w / 1.6, '#4ade80'), (w / 1.6, '#f87171')]):
        r = R[(aad, KOS[j][0])]
        p = 100 * r['w'] / r['n']
        ax2.bar(i + off, p, w * 1.25, color=col, zorder=4)
        ax2.text(i + off, p + 1.6, '%.0f%%\n%.1f$\\sigma$' % (p, sig(r['w'], r['n'])),
                 ha='center', fontsize=9.0, color=col)
ax2.axhline(50, color='#cccccc', ls='--', lw=1.2, zorder=5)
ax2.text(.50, .565, 'beraberlik', transform=ax2.transAxes, fontsize=8.6, color='#cccccc', ha='center')
ax2.set_xticks(x)
ax2.set_xticklabels([a.split(' (')[0] for a, _ in ALT], fontsize=10.2)
ax2.set_ylabel('Evrenakı\'nın önde olduğu galaksi (%)', fontsize=11)
ax2.set_ylim(0, 95)
ax2.set_title('Gerçek Hubble tipleriyle: tek anlamlı galibiyet\ncüce/düzensiz $+$ serbest $\\Upsilon_*$',
              fontsize=12.5, color='white', pad=9)
ax2.legend(handles=[Patch(color='#4ade80', label='$\\Upsilon_*$ serbest'),
                    Patch(color='#f87171', label='$\\Upsilon_*$ bantlı')],
           fontsize=9, framealpha=.25, loc='upper left')
ax2.grid(alpha=.13, axis='y')

fig.suptitle('Yalnızca Spiral Ölçekte Kıyaslama — Gerçek Hubble Tipleriyle (SPARC Tablo 1)',
             fontsize=14, color='white', y=.985)
fig.text(.5, .042, 'Sınıflama SPARC ana kataloğundan doğrudan okunmuştur (Lelli, McGaugh & Schombert 2016, '
                   'Tablo 1): SPİRAL $=$ Sa–Sd ($T=1$–$7$), cüce/düzensiz $=$ Sdm–BCD ($T\\geq8$), '
                   'mercekssel $=$ S0 ($T=0$).', ha='center', fontsize=9.2, color='#999999')
fig.text(.5, .012, 'Spiralde teorinin üstünlüğü yoktur. Tek istatistiksel olarak anlamlı galibiyeti '
                   'cüce/düzensiz $+$ serbest $\\Upsilon_*$ hücresidir; fotometrik $\\Upsilon_*$ '
                   'dayatılınca hiçbir tipte kazanmaz.', ha='center', fontsize=9.2, color='#999999')
plt.tight_layout(rect=[0, .072, 1, .955])
plt.savefig('spiral_kiyaslama.png', dpi=145, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print("Grafik 'spiral_kiyaslama.png' olarak kaydedildi.")
