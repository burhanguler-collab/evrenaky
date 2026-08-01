"""TURETIM-FIT DEFTERI: chi^2'nin goremedigi hesap + Y* tavan bulgusu.

Iki soru.

(1) chi^2 ve AIC egri uydurma kalitesini olcer, TURETMEYI olcmez. Bir teori BTFR'yi
    sifir parametreyle ongoruyorsa, oteki onu geri-besleme ayariyla yakaliyorsa, AIC
    ikisine ayni notu verir. Bu defter o farki kayda gecirir.

(2) Y* gercekten ne istiyor? Bant sinavi (6.5.3.3 Sonuc 5) bandi dayatip bakiyordu.
    Buradaki daha keskin sorudur: fit, KONULAN HER TAVANA dayaniyor mu?

Sonuc (163 galaksi, SPARC).

  Kurulum                                  medyan chi2   Evr onde
  Evrenaki k=2 (Y*<=2.0, kitabin temeli)       1.568     90/163  55%  1.3 sig
  Evrenaki k=2 (Y*<=3.0)                       1.357     96/163  59%  2.3 sig
  Evrenaki k=2 (Y* bantli 0.3-0.8)             3.45      72/163  44% -1.6 sig
  LCDM NFW k=2 (Y*<=2.0)                       1.980       —
  LCDM NFW k=2 (Y* bantli)                     2.58        —

  Y* TAVAN BULGUSU: tavan 2.0 iken galaksilerin %18'i TAVANA DAYANIYOR
                    tavan 3.0 iken            %9  dayaniyor
  Yani sorun "bant dogru mu" degil; fit konulan her siniri arıyor.
  3.6 mikronda populasyon sentezi 0.3-0.8 verir; serbest medyan 0.85.

  ONEMLI DUZELTME: kitabin cuce/LSB anlamliligi 3.5 sigma yazilmis. Dogru deger
  3.1 sigma'dir — 3.5, gozlenen orandan (Wald) hesaplanmis; p=0.5 null'una karsi
  sinamada null orani kullanilmalidir: (36-25)/sqrt(50/4) = 3.11.

Turetim defteri (metinde tam hali). Ozet:
  Evrenaki turetiyor : a_0, BTFR, l_omega yasasi, duz kol (h=sabit), gorunmez madde yok
  LCDM turetiyor     : NFW profili, c200-M200 iliskisi (ikisi de N-cisim)
  LCDM fitliyor      : galaksi basina M200
  Ikisi de fitliyor  : galaksi basina Y*
  UYARI: Evrenaki'nin turetimlerinin tamami, sinandiklari AYNI donus egrilerinden
  okunmustur (a_0 eslesmesi post-hoc, l_omega yasasi ayni ornekten). LCDM'in NFW ve
  c-M girdileri ise BAGIMSIZ bir hesaptan (N-cisim) gelir. Bu, defterin en onemli
  asimetrisidir ve Evrenaki'nin aleyhinedir.
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
RHO_CRIT = 3 * 0.07 ** 2 / (8 * np.pi * G)
H_RED = 0.7
RB = 1.4
BAND = (0.3, 0.8)
VERI = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'veri')


def yukle(f):
    d = np.loadtxt(f)
    if d.ndim < 2 or len(d) < 6:
        return None
    R, Vo, eV, Vg, Vd, Vb, SBd, SBb = [d[:, i] for i in range(8)]
    eV = np.maximum(eV, 1.0)
    if np.any(R <= 0) or Vo.max() <= 0:
        return None
    Rp = R * 1e3
    L = lambda S: np.concatenate([[0.0], np.cumsum(
        np.pi * (Rp[1:] ** 2 - Rp[:-1] ** 2) * 0.5 * (S[1:] + S[:-1]))])
    return dict(R=R, Vo=Vo, eV=eV, Vg=Vg, Vd=Vd, Vb=Vb, Ld=L(SBd), Lb=L(SBb),
                N=len(R), V=float(Vo.max()))


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
    return dict(c2i=np.sum(((mv - d['Vo']) / d['eV']) ** 2) / max(d['N'] - 2, 1), Y=p[0])


evr = lambda d, lo, hi: go(d, lambda R, Y, lb, _d=d: np.sqrt(
    np.maximum(Vbar2(_d, Y), 1e-9) + (10 ** lb) * Mkaps(_d, Y)),
    [min(max(0.5, lo), hi), -6.4], [lo, -12], [hi, -1])
lcdm = lambda d, lo, hi: go(d, lambda R, Y, lg, _d=d: np.sqrt(
    np.maximum(Vbar2(_d, Y), 1e-9) + v_nfw2(R, 10 ** lg)),
    [min(max(0.5, lo), hi), 11.0], [lo, 7.0], [hi, 13.5])

S = []
for f in sorted(glob.glob(os.path.join(VERI, '*_rotmod.dat'))):
    d = yukle(f)
    if d is None:
        continue
    r = dict(V=d['V'], e2=evr(d, 0.05, 2.0), e3=evr(d, 0.05, 3.0), eB=evr(d, *BAND),
             l2=lcdm(d, 0.05, 2.0), lB=lcdm(d, *BAND))
    if all(v for v in r.values() if isinstance(v, dict)) and all(
            r[k] is not None for k in ('e2', 'e3', 'eB', 'l2', 'lB')):
        S.append(r)
NG = len(S)
V = np.array([r['V'] for r in S])
Y2 = np.array([r['e2']['Y'] for r in S])
Y3 = np.array([r['e3']['Y'] for r in S])
sig = lambda k, n: (k - n / 2.0) / np.sqrt(n / 4.0)

med = lambda k: np.median([r[k]['c2i'] for r in S])
onde = lambda a, b: int(np.sum([r[a]['c2i'] < r[b]['c2i'] for r in S]))

print("TURETIM-FIT DEFTERI ve Y* TAVAN SINAVI — %d galaksi" % NG)
print("=" * 86)
print("%-44s %11s %18s" % ("kurulum", "medyan chi2", "Evrenaki onde"))
for ad, k, ref in [("Evrenaki k=2  (Y*<=2,0 — kitabin temeli)", 'e2', 'l2'),
                   ("Evrenaki k=2  (Y*<=3,0)", 'e3', 'l2'),
                   ("Evrenaki k=2  (Y* bantli 0,3-0,8)", 'eB', 'lB'),
                   ("LCDM NFW k=2  (Y*<=2,0)", 'l2', None),
                   ("LCDM NFW k=2  (Y* bantli)", 'lB', None)]:
    if ref:
        w = onde(k, ref)
        print("%-44s %11.3f   %3d/%-3d %%%2.0f %+.1f sig"
              % (ad, med(k), w, NG, 100 * w / NG, sig(w, NG)))
    else:
        print("%-44s %11.3f %18s" % (ad, med(k), "—"))
print("-" * 86)
print("Y* TAVAN BULGUSU — fit konulan her siniri ariyor:")
for hi, Y in [(2.0, Y2), (3.0, Y3)]:
    print("  tavan %.1f : tavana dayanan %%%.0f  ·  medyan Y* %.2f  ·  bandin (0,3-0,8) disinda %%%.0f"
          % (hi, 100 * np.mean(Y > hi - 0.02), np.median(Y), 100 * np.mean((Y < 0.3) | (Y > 0.8))))
print("-" * 86)
m = V < 80
n = int(m.sum())
k2 = int(np.sum([r['e2']['c2i'] < r['l2']['c2i'] for r, q in zip(S, m) if q]))
kB = int(np.sum([r['eB']['c2i'] < r['lB']['c2i'] for r, q in zip(S, m) if q]))
print("CUCE/LSB (<80 km/s, N=%d):" % n)
print("  Y*<=2,0   : %d/%d = %%%.0f  (%.1f sigma)" % (k2, n, 100 * k2 / n, sig(k2, n)))
print("  Y* bantli : %d/%d = %%%.0f  (%.1f sigma)" % (kB, n, 100 * kB / n, sig(kB, n)))
print("  DUZELTME: kitapta 3,5 sigma yaziyor; p=0.5 null'una karsi dogru deger %.1f sigma." % sig(k2, n))
print("=" * 86)

# ------------------------------- Grafik --------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15.4, 6.4), facecolor='#121212')

ax1.set_facecolor('#121212')
etk = ['Evrenakı\n$\\Upsilon_*\\leq2{,}0$', 'Evrenakı\n$\\Upsilon_*$ bantlı',
       'ΛCDM NFW\n$\\Upsilon_*\\leq2{,}0$', 'ΛCDM NFW\n$\\Upsilon_*$ bantlı']
val = [med('e2'), med('eB'), med('l2'), med('lB')]
col = ['#4ade80', '#f87171', '#a78bfa', '#6d5cc4']
b = ax1.bar(range(4), val, 0.6, color=col, zorder=4)
for i, v in enumerate(val):
    ax1.text(i, v + 0.08, '%.2f' % v, ha='center', fontsize=11, color=col[i], fontweight='bold')
ax1.axhline(1.0, color='#888888', ls=':', lw=1.0, zorder=2)
ax1.text(0.03, 1.06, 'kabul sınırı', fontsize=8.2, color='#888888', ha='left')
ax1.set_xticks(range(4))
ax1.set_xticklabels(etk, fontsize=9.4)
ax1.set_ylabel('Medyan $\\chi^2_{ind}$  (163 galaksi, $k=2$)', fontsize=11)
ax1.set_ylim(0, max(val) * 1.24)
ax1.set_title('Hüküm kuruluma bağlı: serbest $\\Upsilon_*$ ile beraberlik,\n'
              'fotometrik bantla ΛCDM önde', fontsize=12, color='white', pad=9)
ax1.grid(alpha=.13, axis='y')
ax1.annotate('', xy=(1, med('eB')), xytext=(0, med('e2')),
             arrowprops=dict(arrowstyle='->', color='#f87171', lw=1.6, connectionstyle='arc3,rad=-.25'))
ax1.text(0.5, med('eB') * 1.02, '×%.1f' % (med('eB') / med('e2')), color='#f87171',
         fontsize=10.5, ha='center', fontweight='bold')
ax1.annotate('', xy=(3, med('lB')), xytext=(2, med('l2')),
             arrowprops=dict(arrowstyle='->', color='#a78bfa', lw=1.4, connectionstyle='arc3,rad=-.25'))
ax1.text(2.5, med('lB') * 1.04, '×%.1f' % (med('lB') / med('l2')), color='#a78bfa',
         fontsize=10.5, ha='center')

ax2.set_facecolor('#121212')
ax2.axvspan(BAND[0], BAND[1], color='#4ade80', alpha=.16, zorder=1)
ax2.hist(Y2, bins=np.linspace(0, 2.05, 42), color='#f87171', alpha=.88, zorder=4)
ax2.axvline(np.median(Y2), color='#ffcc00', ls='--', lw=1.6, zorder=6)
ax2.text(np.median(Y2) + 0.045, ax2.get_ylim()[1] * 0.93, 'medyan %.2f' % np.median(Y2),
         color='#ffcc00', fontsize=10)
ax2.text(np.mean(BAND), ax2.get_ylim()[1] * 0.965, 'popülasyon sentezi\n$0{,}3$–$0{,}8$',
         color='#4ade80', fontsize=9.4, ha='center', va='top')
ax2.annotate('tavana dayanan: %%%.0f' % (100 * np.mean(Y2 > 1.98)),
             xy=(1.99, np.histogram(Y2, bins=np.linspace(0, 2.05, 42))[0][-1] * 0.55),
             xytext=(1.42, ax2.get_ylim()[1] * 0.62), fontsize=10, color='#f87171',
             arrowprops=dict(arrowstyle='->', color='#f87171', lw=1.4))
ax2.set_xlabel('Fitlenen $\\Upsilon_*$  (3,6 μm)', fontsize=11)
ax2.set_ylabel('Galaksi sayısı', fontsize=11)
ax2.set_xlim(0, 2.08)
ax2.set_title('Fit, konulan her tavanı arıyor — sorun bandın\ndoğruluğu değil, bu',
              fontsize=12, color='white', pad=9)
ax2.grid(alpha=.13, axis='y')

fig.suptitle('$\\chi^2$ Neyi Görüyor, Neyi Görmüyor — ve $\\Upsilon_*$ Gerçekte Ne İstiyor?',
             fontsize=14, color='white', y=.985)
fig.text(.5, .006, 'Sol: hüküm $\\Upsilon_*$ kısıtına bağlıdır. Sağ: serbest fit medyanı %.2f ister, '
                   'galaksilerin %%%.0f\'ı bandın dışındadır ve %%%.0f\'ı tavana dayanır — tavan 3,0\'a '
                   'çıkarılınca %%%.0f\'ı yine dayanır. Defterin türetim tarafı 6.5.3.6\'dadır.'
         % (np.median(Y2), 100 * np.mean((Y2 < 0.3) | (Y2 > 0.8)),
            100 * np.mean(Y2 > 1.98), 100 * np.mean(Y3 > 2.98)),
         ha='center', fontsize=9.3, color='#999999')
plt.tight_layout(rect=[0, .030, 1, .955])
plt.savefig('turetim_fit_defteri.png', dpi=145, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print("Grafik 'turetim_fit_defteri.png' olarak kaydedildi.")
