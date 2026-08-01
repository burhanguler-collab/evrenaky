"""UPSILON_* BANDI REJIME GORE: teorinin tek zafer iddiasi bandi geciyor mu?

Arka plan. 6.5.3.3 sunu buluyordu: genel ustunluk YOK (%55, 1.3 sigma), ama
cuce/LSB bandinda (V_max < 80 km/s) Evrenaki 3.5 sigma ile onde. Kitabin galaktik
cephe iddiasi TAM OLARAK BURAYA dayaniyor.

Sinav. O iddia, Y*'in serbest birakilmasina kosullu mu? Y* yildiz populasyon
sentezinin 3.6 mikron icin verdigi banda (0.3-0.8) hapsedilip ayni karsilastirma
tekrarlanir. Ayni kisit LCDM'e de uygulanir — o da Y* kullanir, karsilastirma adil.

Sonuc (163 galaksi):
  rejim          Evr k=2 serbest->bantli   LCDM k=2 serbest->bantli   kazanma
  CUCE/LSB <80        0.62 -> 1.68              1.57 -> 2.28          %74 -> %56
  80-120              0.78 -> 4.90              1.56 -> 1.91          %61 -> %27
  120-180             2.16 -> 3.05              2.44 -> 2.97          %32 -> %36
  180-250             1.89 -> 3.25              1.98 -> 2.49          %48 -> %44
  >250                3.56 -> 5.42              4.17 -> 4.17          %60 -> %55
  TUMU                1.36 -> 3.45              1.97 -> 2.58          %59 -> %44

  CUCE/LSB anlamlilik: 37/50 (3.4 sigma)  ->  28/50 (0.8 sigma)  ANLAMSIZ

Okunusu. Bant her rejimde teoriye LCDM'den cok daha fazla zarar veriyor. En agir
hasar 80-120 km/s bandinda (6.3 kat, kazanma %61->%27). Cuce/LSB'de teori medyan
chi2 bakimindan HALA onde (1.68 < 2.28) ama kazanma orani anlamliligini yitiriyor.
Yani 6.5.3.3'un "3.5 sigma" basligi, Y*'in serbest olmasina KOSULLUDUR.
Bkz. 6.5.4.7 kayit (4c) ve 7.4 madde 12 (j)/(a).
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
BAND = (0.3, 0.8)
VERI = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'veri')

BINS = [('Cüce/LSB\n$<80$', 0, 80), ('$80$–$120$', 80, 120), ('$120$–$180$', 120, 180),
        ('$180$–$250$', 180, 250), ('$>250$', 250, 1e9)]


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


def _fit(d, g, p0, lo, hi, k):
    try:
        p, _ = curve_fit(g, d['R'], d['Vo'], sigma=d['eV'], p0=p0, bounds=(lo, hi), maxfev=300000)
    except Exception:
        return None
    mv = g(d['R'], *p)
    if not np.all(np.isfinite(mv)):
        return None
    return np.sum(((mv - d['Vo']) / d['eV']) ** 2) / max(d['N'] - k, 1)


def evr_k2(d, lo, hi):
    """6.5.3.3'un kurulumu: Y* ve b serbest."""
    g = lambda R, Y, lb, _d=d: np.sqrt(np.maximum(Vbar2(_d, Y), 1e-9) + (10 ** lb) * Mkaps(_d, Y))
    return _fit(d, g, [min(max(0.5, lo), hi), -5.0], [lo, -9], [hi, -1], 2)


def lcdm_k2(d, lo, hi):
    g = lambda R, Y, lg, _d=d: np.sqrt(np.maximum(Vbar2(_d, Y), 1e-9) + v_nfw2(R, 10 ** lg))
    return _fit(d, g, [min(max(0.5, lo), hi), 11.0], [lo, 7], [hi, 13.5], 2)


R = []
for f in sorted(glob.glob(os.path.join(VERI, '*_rotmod.dat'))):
    d = yukle(f)
    if d is None:
        continue
    r = dict(V=d['V'], eS=evr_k2(d, 0.05, 3.0), eB=evr_k2(d, *BAND),
             lS=lcdm_k2(d, 0.05, 3.0), lB=lcdm_k2(d, *BAND))
    if all(v is not None for v in r.values()):
        R.append(r)
V = np.array([r['V'] for r in R])
NG = len(R)

sig = lambda k, n: (k - n / 2.0) / np.sqrt(n / 4.0)
satir = []
for ad, lo, hi in BINS:
    m = (V >= lo) & (V < hi)
    sub = [r for r, q in zip(R, m) if q]
    n = len(sub)
    if n < 3:
        continue
    kS = sum(r['eS'] < r['lS'] for r in sub)
    kB = sum(r['eB'] < r['lB'] for r in sub)
    satir.append(dict(ad=ad, n=n,
                      eS=np.median([r['eS'] for r in sub]), eB=np.median([r['eB'] for r in sub]),
                      lS=np.median([r['lS'] for r in sub]), lB=np.median([r['lB'] for r in sub]),
                      wS=kS / n, wB=kB / n, sS=sig(kS, n), sB=sig(kB, n), kS=kS, kB=kB))

print("UPSILON_* BANDI REJIME GORE — %d galaksi  (Y* bandi %.1f-%.1f)" % (NG, *BAND))
print("=" * 96)
print("%-14s %4s | %-19s | %-19s | %-21s" %
      ("rejim", "N", "Evrenaki k=2", "LCDM NFW k=2", "kazanma (Evr onde)"))
print("%-14s %4s | %8s %10s | %8s %10s | %9s %11s" %
      ("", "", "serbest", "BANTLI", "serbest", "BANTLI", "serbest", "BANTLI"))
print("-" * 96)
for s in satir:
    print("%-14s %4d | %8.2f %10.2f | %8.2f %10.2f | %3d/%-3d %.1fs %3d/%-3d %.1fs"
          % (s['ad'].replace('\n', ' ').replace('$', ''), s['n'], s['eS'], s['eB'],
             s['lS'], s['lB'], s['kS'], s['n'], s['sS'], s['kB'], s['n'], s['sB']))
print("=" * 96)
d0 = satir[0]
print("CUCE/LSB — teorinin tek zafer iddiasi:")
print("  serbest : %d/%d = %%%.0f  (%.1f sigma)  ANLAMLI" % (d0['kS'], d0['n'], 100 * d0['wS'], d0['sS']))
print("  BANTLI  : %d/%d = %%%.0f  (%.1f sigma)  ANLAMSIZ" % (d0['kB'], d0['n'], 100 * d0['wB'], d0['sB']))
print("  medyan chi2 orada hala onde: %.2f < %.2f — ama kazanma orani anlamliligini yitiriyor."
      % (d0['eB'], d0['lB']))

# ------------------------------ Grafik ---------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15.6, 6.6), facecolor='#121212')
x = np.arange(len(satir))
w = 0.20

ax1.set_facecolor('#121212')
for off, key, col, lab in [(-1.5 * w, 'eS', '#4ade80', 'Evrenakı — $\\Upsilon_*$ serbest'),
                           (-0.5 * w, 'eB', '#f87171', 'Evrenakı — $\\Upsilon_*$ bantlı'),
                           (0.5 * w, 'lS', '#a78bfa', 'ΛCDM — $\\Upsilon_*$ serbest'),
                           (1.5 * w, 'lB', '#6d5cc4', 'ΛCDM — $\\Upsilon_*$ bantlı')]:
    ax1.bar(x + off, [s[key] for s in satir], w, color=col, label=lab, zorder=4)
for i, s in enumerate(satir):
    ax1.text(i - 0.5 * w, s['eB'] + 0.12, '×%.1f' % (s['eB'] / s['eS']), ha='center',
             fontsize=8.4, color='#f87171', fontweight='bold', zorder=6)
    ax1.text(i + 1.5 * w, s['lB'] + 0.12, '×%.1f' % (s['lB'] / s['lS']), ha='center',
             fontsize=8.4, color='#a78bfa', zorder=6)
ax1.axhline(1.0, color='#888888', ls=':', lw=1.0, zorder=2)
ax1.text(0.985, 0.055, 'kabul sınırı', fontsize=8, color='#888888', ha='right', transform=ax1.transAxes)
ax1.set_xticks(x)
ax1.set_xticklabels([s['ad'] for s in satir], fontsize=9.5)
ax1.set_xlabel('$v_{max}$ bandı (km/s)', fontsize=10.5)
ax1.set_ylabel('Medyan $\\chi^2_{ind}$', fontsize=11.5)
ax1.set_title('Bant her rejimde teoriye daha çok zarar veriyor', fontsize=12.5, color='white', pad=9)
ax1.legend(fontsize=8.8, framealpha=.25, loc='upper left')
ax1.grid(alpha=.13, axis='y')

ax2.set_facecolor('#121212')
for off, key, skey, col, lab in [(-w / 2, 'wS', 'sS', '#4ade80', '$\\Upsilon_*$ serbest'),
                                 (w / 2, 'wB', 'sB', '#f87171', '$\\Upsilon_*$ bantlı')]:
    ax2.bar(x + off, [100 * s[key] for s in satir], w, color=col, label=lab, zorder=4)
    for i, s in enumerate(satir):
        ax2.text(i + off, 100 * s[key] + 1.6, '%.1f$\\sigma$' % s[skey], ha='center',
                 fontsize=8.2, color=col, zorder=6)
ax2.axhline(50, color='#888888', ls='--', lw=1.1, zorder=3)
ax2.text(0.985, 0.575, 'beraberlik', fontsize=8, color='#888888', ha='right', transform=ax2.transAxes)
ax2.set_xticks(x)
ax2.set_xticklabels([s['ad'] for s in satir], fontsize=9.5)
ax2.set_xlabel('$v_{max}$ bandı (km/s)', fontsize=10.5)
ax2.set_ylabel('Evrenakı\'nın önde olduğu galaksi (%)', fontsize=11)
ax2.set_ylim(0, 92)
ax2.set_title('Cüce/LSB zaferi bandı geçemiyor: $3{,}4\\sigma \\rightarrow 0{,}8\\sigma$',
              fontsize=12.5, color='white', pad=9)
ax2.legend(fontsize=9, framealpha=.25, loc='upper right')
ax2.grid(alpha=.13, axis='y')

fig.suptitle('$\\Upsilon_*$ Popülasyon Sentezi Bandı Dayatılınca Rejim Deseni Ne Oluyor?  '
             '(%d galaksi, her iki model de $k=2$)' % NG, fontsize=14, color='white', y=.985)
fig.text(.5, .006, 'Sol paneldeki çarpanlar bozulma oranıdır. Cüce/LSB\'de teori medyan olarak hâlâ önde '
                   '(%.2f < %.2f), ama kazanma oranının anlamlılığı %.1f$\\sigma$\'dan %.1f$\\sigma$\'ya '
                   'düşerek yiter — yani 6.5.3.3\'ün başlık iddiası $\\Upsilon_*$\'ın serbest olmasına koşulludur.'
         % (d0['eB'], d0['lB'], d0['sS'], d0['sB']),
         ha='center', fontsize=9.3, color='#999999')
plt.tight_layout(rect=[0, .030, 1, .960])
plt.savefig('upsilon_bant_rejim.png', dpi=145, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print("Grafik 'upsilon_bant_rejim.png' olarak kaydedildi.")
