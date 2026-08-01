"""R_f FIZIK MI ARTEFAKT MI? — yayilma ile warp hipotezinin yarisi.

Soru: 6.5.4'un yayilma terimi R_f, M-38'in ongordugu FIZIKSEL aki tupu
kalinlasmasi mi, yoksa dis kolun GOZLEMSEL sistematigini emen bir duzeltme mi?

Iki hipotez ayni serbestlikte (k=3) yaristirilir:
  (A) YAYILMA (fiziksel): v^2 = Vbar^2 + b*M_kaps/(1+R/R_f)
      F4'un kendisi zayiflar; duzeltme yalniz F4 katkisina uygulanir.
  (B) WARP (artefakt):    v = sqrt(Vbar^2 + b*M_kaps) * w(R),  w=1+(w1-1)(R/Rmax)^2
      Donus egrileri V = V_los/sin(i) ile cikarilir. Disk burustugunde (warp)
      gercek egiklik yaricapla degisir ve tabulanmis V CARPIMSAL olarak kayar.
      Duzeltme tum hiza uygulanir, yalniz F4'e degil. Iki hipotezin imzasi
      bu yuzden farklidir ve veri onlari ayirt edebilir.

Ek olarak kritik bir alt sinav: R_f sonsuza kacan (yayilma istemeyen) galaksiler,
warp hipotezi dogruysa KUCUK warp gerektirmelidir. Bu, hipotezin kendi ongorusudur.

Duyarlilik notu: V = V_ger*sin(i) oldugundan dV/V = -cot(i)*di. Yani warp hatasi
yuzeyden gorunen (kucuk i) galaksilerde buyuk, kenardan gorunenlerde kucuktur.
w1 = sin(i_varsayilan)/sin(i_gercek); +-15 derece warp icin w1 ~ 0.82-1.22.

Veri: SPARC (Lelli, McGaugh & Schombert 2016). Y_bul = 1.4*Y_disk.
"""

import sys
import os
import glob
import warnings

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.optimize import curve_fit
from scipy.stats import mannwhitneyu

warnings.filterwarnings('ignore')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
plt.style.use('dark_background')

G = 4.300917e-6
RF_UST = 3e3
VERI = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'veri')


def hazir(f):
    d = np.loadtxt(f)
    if d.ndim < 2 or len(d) < 8:
        return None
    R, Vo, eV, Vg, Vd, Vb, SBd, SBb = [d[:, i] for i in range(8)]
    eV = np.maximum(eV, 1.0)
    if np.any(R <= 0) or Vo.max() <= 0:
        return None
    Rpc = R * 1e3
    L = lambda SB: np.concatenate([[0.0], np.cumsum(
        np.pi * (Rpc[1:] ** 2 - Rpc[:-1] ** 2) * 0.5 * (SB[1:] + SB[:-1]))])
    return dict(g=os.path.basename(f)[:-11], R=R, Vo=Vo, eV=eV, Vg=Vg, Vd=Vd, Vb=Vb,
                Ld=L(SBd), Lb=L(SBb), N=len(R), Rm=float(R.max()))


def Vbar2(D, Y):
    return np.sign(D['Vg']) * D['Vg'] ** 2 + Y * D['Vd'] ** 2 + 1.4 * Y * D['Vb'] ** 2


def Mkaps(D, Y):
    return Y * D['Ld'] + 1.4 * D['Lb'] * Y + np.maximum(D['R'] * np.sign(D['Vg']) * D['Vg'] ** 2 / G, 0.0)


def fitle(D, f, p0, lo, hi):
    try:
        p, _ = curve_fit(f, D['R'], D['Vo'], sigma=D['eV'], p0=p0, bounds=(lo, hi), maxfev=800000)
    except Exception:
        return None
    mv = f(D['R'], *p)
    if not np.all(np.isfinite(mv)):
        return None
    chi2 = float(np.sum(((mv - D['Vo']) / D['eV']) ** 2))
    return dict(p=p, mv=mv, c2i=chi2 / max(D['N'] - len(p), 1), aic=chi2 + 2 * len(p))


S = []
for f in sorted(glob.glob(os.path.join(VERI, '*_rotmod.dat'))):
    D = hazir(f)
    if D is None or D['N'] < 8:
        continue
    A = fitle(D, lambda R, Y, b, Rf, _D=D: np.sqrt(np.maximum(Vbar2(_D, Y), 1e-9)
                                                   + b * Mkaps(_D, Y) / (1 + R / Rf)),
              [0.5, 6e-7, 20.0], [0.05, 1e-12, 0.3], [2.0, 1e-1, RF_UST])
    B = fitle(D, lambda R, Y, b, w1, _D=D: np.sqrt(np.maximum(Vbar2(_D, Y), 1e-9)
                                                   + b * Mkaps(_D, Y)) * (1 + (w1 - 1) * (R / _D['Rm']) ** 2),
              [0.5, 4e-7, 0.95], [0.05, 1e-12, 0.5], [2.0, 1e-1, 1.6])
    C = fitle(D, lambda R, Y, b, _D=D: np.sqrt(np.maximum(Vbar2(_D, Y), 1e-9) + b * Mkaps(_D, Y)),
              [0.5, 4e-7], [0.05, 1e-12], [2.0, 1e-1])
    if A and B and C:
        S.append((D, A, B, C))

aA = np.array([s[1]['aic'] for s in S])
aB = np.array([s[2]['aic'] for s in S])
cA = np.array([s[1]['c2i'] for s in S])
cB = np.array([s[2]['c2i'] for s in S])
cC = np.array([s[3]['c2i'] for s in S])
Rf = np.array([s[1]['p'][2] for s in S])
w1 = np.array([s[2]['p'][2] for s in S])
son = Rf > 0.98 * RF_UST
dA = aA - aB
NG = len(S)

print("R_f SINAVI: YAYILMA (fizik) mi WARP (artefakt) mi? — %d galaksi, ikisi de k=3" % NG)
print("=" * 88)
print("  medyan chi2_ind :  taban(k=2) %.2f   yayilma(k=3) %.2f   warp(k=3) %.2f"
      % (np.median(cC), np.median(cA), np.median(cB)))
print("  medyan AIC      :  yayilma %.1f   warp %.1f" % (np.median(aA), np.median(aB)))
print("-" * 88)
print("AYIRT EDILEBILIRLIK:")
print("  warp daha iyi (AIC)        : %d/%d (%%%.0f)" % (int(np.sum(dA > 0)), NG, 100 * np.mean(dA > 0)))
print("  |dAIC| < 2 (ayirt edilemez): %d/%d (%%%.0f)" % (int(np.sum(np.abs(dA) < 2)), NG, 100 * np.mean(np.abs(dA) < 2)))
print("  medyan dAIC (yayilma-warp) : %+.2f" % np.median(dA))
print("-" * 88)
mak = (w1 > 0.82) & (w1 < 1.22)
print("WARP GENLIGI MAKUL MU? (+-15 derece -> w1 = 0.82-1.22)")
print("  w1 yuzdelikleri : %s" % np.array2string(np.percentile(w1, [10, 25, 50, 75, 90]), precision=3))
print("  makul aralikta  : %d/%d (%%%.0f)" % (int(mak.sum()), NG, 100 * mak.mean()))
print("-" * 88)
print("KRITIK ALT SINAV — warp hipotezinin kendi ongorusu:")
print("  R_f sonsuz (yayilma istemeyen), n=%d : |w1-1| medyan = %.3f" % (int(son.sum()), np.median(np.abs(w1[son] - 1))))
print("  R_f sonlu  (yayilma isteyen),   n=%d : |w1-1| medyan = %.3f" % (int((~son).sum()), np.median(np.abs(w1[~son] - 1))))
u, pv = mannwhitneyu(np.abs(w1[son] - 1), np.abs(w1[~son] - 1))
print("  Mann-Whitney p = %.3f  ->  %s" % (pv, 'FARKLI' if pv < 0.05 else 'FARK YOK — ongoru DOGRULANMADI'))
print("=" * 88)

# --- GRAFIK ---
fig = plt.figure(figsize=(16.0, 8.6), facecolor='#121212')
gs = GridSpec(2, 3, height_ratios=[1, 1], hspace=0.38, wspace=0.28,
              left=0.058, right=0.985, top=0.885, bottom=0.09)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[0, 2])
ax4 = fig.add_subplot(gs[1, 0])
ax5 = fig.add_subplot(gs[1, 1])
ax6 = fig.add_subplot(gs[1, 2])
for a in (ax1, ax2, ax3, ax4, ax5, ax6):
    a.set_facecolor('#121212')
    for sp in ('top', 'right'):
        a.spines[sp].set_visible(False)
    for sp in ('bottom', 'left'):
        a.spines[sp].set_color('#444444')
    a.tick_params(colors='#aaaaaa', labelsize=8.4)
    a.grid(True, alpha=0.14, color='white')

# (1,2) iki ornek: iki model neredeyse cakisiyor
ORN = [s for s in S if s[0]['g'] in ('NGC3198', 'NGC2403')]
for a, s in zip((ax1, ax2), ORN):
    D, A, B, C = s
    a.errorbar(D['R'], D['Vo'], yerr=D['eV'], fmt='o', color='#ffcc00', ms=3.2,
               capsize=1.6, elinewidth=0.9, zorder=6, label='ölçüm')
    a.plot(D['R'], C['mv'], ':', color='#888888', lw=1.5, zorder=3,
           label='düzeltmesiz $\\chi^2_i$=%.2f' % C['c2i'])
    a.plot(D['R'], A['mv'], '--', color='#4ade80', lw=2.2, zorder=5,
           label='yayılma $\\chi^2_i$=%.2f' % A['c2i'])
    a.plot(D['R'], B['mv'], '-', color='#7dd3fc', lw=1.8, zorder=4,
           label='warp $\\chi^2_i$=%.2f' % B['c2i'])
    a.set_title('%s — iki düzeltme çakışıyor' % D['g'], fontsize=10.0, color='white', pad=6)
    a.set_xlabel('$R$ (kpc)', fontsize=9, color='#bbbbbb')
    a.set_ylabel('$v$ (km/s)', fontsize=9, color='#bbbbbb')
    lg = a.legend(fontsize=7.4, facecolor='#1a1a1a', edgecolor='#333333', loc='lower right')
    for t in lg.get_texts():
        t.set_color('white')

# (3) dAIC dagilimi
ax3.hist(np.clip(dA, -20, 20), bins=np.linspace(-20, 20, 33), color='#7dd3fc', alpha=0.8)
ax3.axvline(0, color='#ffffff', lw=1.3)
ax3.axvspan(-2, 2, color='#ffcc00', alpha=0.18)
ax3.text(0, ax3.get_ylim()[1] * 0.92, 'ayırt\nedilemez', ha='center', fontsize=7.6, color='#ffcc00')
ax3.set_xlabel('$\\Delta$AIC (yayılma − warp)', fontsize=9, color='#bbbbbb')
ax3.set_ylabel('galaksi sayısı', fontsize=9, color='#bbbbbb')
ax3.set_title('Veri hangisini seçiyor? — %%%.0f ayırt edilemez' % (100 * np.mean(np.abs(dA) < 2)),
              fontsize=10.0, color='white', pad=6)

# (4) medyan chi2 karsilastirma
ad4 = ['düzeltmesiz\n(k=2)', 'yayılma\n(k=3)', 'warp\n(k=3)']
v4 = [np.median(cC), np.median(cA), np.median(cB)]
ax4.bar([0, 1, 2], v4, width=0.58, color=['#888888', '#4ade80', '#7dd3fc'], alpha=0.9)
ax4.axhline(1.0, color='#ffcc00', ls=':', lw=1.4)
ax4.text(2.42, 1.04, 'kabul sınırı', fontsize=7.4, color='#ffcc00', ha='right')
for i, v in enumerate(v4):
    ax4.text(i, v + 0.04, '%.2f' % v, ha='center', fontsize=9, color='#dddddd')
ax4.set_xticks([0, 1, 2])
ax4.set_xticklabels(ad4, fontsize=8.2, color='#cccccc')
ax4.set_ylabel('medyan $\\chi^2_{ind}$', fontsize=9, color='#bbbbbb')
ax4.set_ylim(0, max(v4) * 1.25)
ax4.set_title('Her iki düzeltme de işe yarıyor', fontsize=10.0, color='white', pad=6)

# (5) w1 dagilimi vs makul warp araligi
ax5.hist(w1, bins=np.linspace(0.5, 1.6, 30), color='#f472b6', alpha=0.82)
ax5.axvspan(0.82, 1.22, color='#4ade80', alpha=0.16)
ax5.axvline(1.0, color='#ffffff', lw=1.3)
ax5.text(1.02, ax5.get_ylim()[1] * 0.93, '$\\pm15°$ warp\naralığı', fontsize=7.6, color='#4ade80')
ax5.set_xlabel('gereken $w_1=\\sin i_{var}/\\sin i_{ger}$', fontsize=9, color='#bbbbbb')
ax5.set_ylabel('galaksi sayısı', fontsize=9, color='#bbbbbb')
ax5.set_title('Gereken warp genliği — yalnız %%%.0f makul' % (100 * mak.mean()),
              fontsize=10.0, color='white', pad=6)

# (6) kritik alt sinav
d1 = np.abs(w1[son] - 1)
d2 = np.abs(w1[~son] - 1)
bp = ax6.boxplot([d1, d2], patch_artist=True, widths=0.55, showfliers=False)
for patch, cc in zip(bp['boxes'], ['#c084fc', '#4ade80']):
    patch.set_facecolor(cc)
    patch.set_alpha(0.75)
for el in ('whiskers', 'caps', 'medians'):
    for it in bp[el]:
        it.set_color('#dddddd')
ax6.set_xticklabels(['$R_f\\to\\infty$\n(yayılma yok)\nn=%d' % son.sum(),
                     '$R_f$ sonlu\n(yayılma var)\nn=%d' % (~son).sum()],
                    fontsize=8.0, color='#cccccc')
ax6.set_ylabel('gereken $|w_1-1|$', fontsize=9, color='#bbbbbb')
ax6.set_title('Kritik alt sınav: p=%.2f → **doğrulanmadı**' % pv, fontsize=10.0,
              color='#ff8888', pad=6)
ax6.text(0.5, 0.94, 'Hipotez: yayılma istemeyenler\nKÜÇÜK warp istemeliydi',
         transform=ax6.transAxes, ha='center', va='top', fontsize=7.8, color='#ff9999',
         linespacing=1.4)

fig.text(0.5, 0.955, 'Sonuç: veri iki hipotezi ayırt etmiyor — $R_f$’nin fiziksel yayılma '
                     'olduğu iddiası desteklenmiyor, ama warp hipotezi de doğrulanmıyor',
         ha='center', fontsize=10.0, color='#aaaaaa')
plt.savefig('rf_warp_sinavi.png', dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print("Grafik 'rf_warp_sinavi.png' olarak kaydedildi.")
