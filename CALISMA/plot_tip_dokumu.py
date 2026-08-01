"""TIP TIP DOKUM: "cuce/duzensiz" blogunu acmak.

Neden. Onceki analizlerde 163 galaksi ya butun halinde ya da iki bloga (spiral /
cuce-duzensiz) ayrilmisti. Blok ortalamalari iki gercegi gizliyordu:

  (1) Teorinin EN GUCLU sonucu Im (duzensiz) tipindedir ve blok icinde kayboluyordu.
      Blok olarak +2,5 sigma gorunen sey, ayrilinca Im'de tek basina +3,3 sigma.
  (2) Y*'in "sisirilmesi" GENEL bir kusur degil, Sm/Sdm'ye OZGUDUR.
      Sm: medyan Y* = 1,68, %39'u tavanda.  Spiral: 0,64, %9.  Im: 0,98, %27.

Yontem. SPARC ana katalogundan Hubble tipi (T) okunur ve her tip ayri raporlanir:
  T=0 S0 | 1-7 Sa-Sd (spiral) | 8 Sdm | 9 Sm | 10 Im | 11 BCD
Hicbir tip bloklanmaz, hicbir altorneklem secilmez — secim yapmamak icin hepsi verilir.

SONUC (Y* serbest <=2,0 ; LCDM k=2 ; ayrica Y* bantli 0,3-0,8):

  tip          N   Y* bant disi  medyan Y*  tavanda | Evr onde serbest   bantli
  S0           3        33%        0.64       0%    |   3/3              2/3
  SPIRAL      91        44%        0.64       9%    |  42/91 (-0.7s)    38/91 (-1.6s)
  Sdm          9        78%        1.41      33%    |   5/9  (+0.3s)     4/9  (-0.3s)
  Sm          23        91%        1.68      39%    |  13/23 (+0.6s)     6/23 (-2.3s)
  Im          33        79%        0.98      27%    |  26/33 (+3.3s)    19/33 (+0.9s)
  BCD          4        75%        1.08       0%    |   1/4              2/4

Okunusu. Teorinin evi Im'dir; Sm ise hem Y*'i en cok sisirdigi hem bant altinda
en sert coktugu tiptir. Ikisi ayni blokta toplanirsa ikisi de gorunmez olur.
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
H_RED, RB, UST = 0.7, 1.4, 2.0
SPS = (0.3, 0.8)
VERI = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'veri')
GRP = [('S0', [0]), ('Sa–Sd\n(spiral)', [1, 2, 3, 4, 5, 6, 7]), ('Sdm', [8]),
       ('Sm', [9]), ('Im', [10]), ('BCD', [11])]


def katalog():
    ham = open(os.path.join(VERI, '_sparc.mrt'), encoding='utf-8', errors='replace').read().split('\n')
    a = [i for i, x in enumerate(ham) if x.startswith('----')][-1]
    K = {}
    for L in ham[a + 1:]:
        p = L.split()
        if len(p) >= 19:
            try:
                K[p[0]] = int(p[1])
            except ValueError:
                pass
    return K


KT = katalog()
D = []
for f in sorted(glob.glob(os.path.join(VERI, '*_rotmod.dat'))):
    d = np.loadtxt(f)
    ad = os.path.basename(f)[:-11]
    if d.ndim < 2 or len(d) < 6 or ad not in KT:
        continue
    R, Vo, eV, Vg, Vd, Vb, SBd, SBb = [d[:, i] for i in range(8)]
    eV = np.maximum(eV, 1.0)
    if np.any(R <= 0) or Vo.max() <= 0:
        continue
    Rp = R * 1e3
    L = lambda S: np.concatenate([[0.0], np.cumsum(
        np.pi * (Rp[1:] ** 2 - Rp[:-1] ** 2) * 0.5 * (S[1:] + S[:-1]))])
    D.append(dict(g=ad, T=KT[ad], R=R, Vo=Vo, eV=eV, Vg=Vg, Vd=Vd, Vb=Vb,
                  Ld=L(SBd), Lb=L(SBb), N=len(R)))

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
        return None, None
    mv = g(d['R'], *p)
    if not np.all(np.isfinite(mv)):
        return None, None
    return p, np.sum(((mv - d['Vo']) / d['eV']) ** 2) / max(d['N'] - 2, 1)


EV = lambda d, lo, hi: go(d, lambda R, y, lb, _d=d: np.sqrt(
    np.maximum(Vbar2(_d, y), 1e-9) + (10 ** lb) * Mkaps(_d, y)),
    [min(max(0.5, lo), hi), -6.4], [lo, -12], [hi, -1])
LC = lambda d, lo, hi: go(d, lambda R, y, lg, _d=d: np.sqrt(
    np.maximum(Vbar2(_d, y), 1e-9) + v_nfw2(R, 10 ** lg)),
    [min(max(0.5, lo), hi), 11.0], [lo, 7.0], [hi, 13.5])

sig = lambda k, n: (k - n / 2.0) / np.sqrt(n / 4.0)
S = []
for ad, ts in GRP:
    Y, w1, w2, n = [], 0, 0, 0
    for d in D:
        if d['T'] not in ts:
            continue
        pe, ce = EV(d, 0.05, UST)
        pl, cl = LC(d, 0.05, UST)
        _, cb = EV(d, *SPS)
        _, lb = LC(d, *SPS)
        if pe is None or pl is None:
            continue
        Y.append(pe[0]); n += 1; w1 += ce < cl
        if cb is not None and lb is not None:
            w2 += cb < lb
    if n < 2:
        continue
    Y = np.array(Y)
    S.append(dict(ad=ad, n=n, dis=np.mean((Y < SPS[0]) | (Y > SPS[1])), med=np.median(Y),
                  tav=np.mean(Y > UST - .02), w1=w1, w2=w2, s1=sig(w1, n), s2=sig(w2, n)))

print("TIP TIP DOKUM — %d galaksi, hicbir tip bloklanmadi" % sum(x['n'] for x in S))
print("=" * 96)
print("  %-14s %4s | %10s %8s %8s | %16s %16s" %
      ('tip', 'N', 'Y* bant dışı', 'medyan', 'tavanda', 'Evr önde serbest', 'Evr önde bantlı'))
for x in S:
    print("  %-14s %4d | %9.0f%% %8.2f %7.0f%% | %7d/%-4d %+.1fs %7d/%-4d %+.1fs"
          % (x['ad'].replace('\n', ' '), x['n'], 100 * x['dis'], x['med'], 100 * x['tav'],
             x['w1'], x['n'], x['s1'], x['w2'], x['n'], x['s2']))
print("=" * 96)
im = [x for x in S if x['ad'] == 'Im'][0]
sm = [x for x in S if x['ad'] == 'Sm'][0]
print("BULGU 1: teorinin en guclu sonucu Im'dedir — %d/%d = %%%.0f, %+.1f sigma"
      % (im['w1'], im['n'], 100 * im['w1'] / im['n'], im['s1']))
print("         ve bant altinda pozitif kalan TEK tip odur (%+.1f sigma)" % im['s2'])
print("BULGU 2: Y* sisirmesi Sm'ye ozgudur — medyan %.2f, %%%.0f'i tavanda; bant altinda %+.1f sigma"
      % (sm['med'], 100 * sm['tav'], sm['s2']))

# ------------------------------ Grafik ---------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15.4, 6.3), facecolor='#121212')
x = np.arange(len(S))

ax1.set_facecolor('#121212')
ax1.axhspan(SPS[0], SPS[1], color='#4ade80', alpha=.17, zorder=1)
col = ['#4ade80' if v['med'] <= SPS[1] else '#f87171' for v in S]
ax1.bar(x, [v['med'] for v in S], .58, color=col, zorder=4)
for i, v in enumerate(S):
    ax1.text(i, v['med'] + .045, '%.2f' % v['med'], ha='center', fontsize=10,
             color=col[i], fontweight='bold')
    ax1.text(i, .06, 'tavanda\n%%%.0f' % (100 * v['tav']), ha='center', fontsize=8.2, color='#dddddd')
ax1.text(.985, (SPS[0] + SPS[1]) / 2 / ax1.get_ylim()[1], '', transform=ax1.transAxes)
ax1.text(len(S) - .4, np.mean(SPS), 'popülasyon\nsentezi', color='#4ade80', fontsize=8.8,
         ha='right', va='center')
ax1.set_xticks(x); ax1.set_xticklabels(['%s\nN=%d' % (v['ad'], v['n']) for v in S], fontsize=9.4)
ax1.set_ylabel('Medyan fitlenen $\\Upsilon_*$', fontsize=11)
ax1.set_title('$\\Upsilon_*$ şişmesi genel değil — Sm/Sdm\'ye özgü', fontsize=12.5, color='white', pad=9)
ax1.grid(alpha=.13, axis='y')

ax2.set_facecolor('#121212')
w = .36
for j, (key, skey, c, lab) in enumerate([('w1', 's1', '#4ade80', '$\\Upsilon_*$ serbest'),
                                         ('w2', 's2', '#f87171', '$\\Upsilon_*$ bantlı')]):
    p = [100 * v[key] / v['n'] for v in S]
    ax2.bar(x + (j - .5) * w, p, w, color=c, label=lab, zorder=4)
    for i, v in enumerate(S):
        ax2.text(i + (j - .5) * w, p[i] + 1.8, '%+.1f$\\sigma$' % v[skey], ha='center',
                 fontsize=8.4, color=c)
ax2.axhline(50, color='#cccccc', ls='--', lw=1.2, zorder=5)
ax2.text(.015, .545, 'beraberlik', transform=ax2.transAxes, fontsize=8.4, color='#cccccc')
ax2.set_xticks(x); ax2.set_xticklabels([v['ad'] for v in S], fontsize=9.6)
ax2.set_ylabel('Evrenakı\'nın önde olduğu galaksi (%)', fontsize=11)
ax2.set_ylim(0, 118)
ax2.set_title('Teorinin evi Im — ve bant altında pozitif kalan tek tip',
              fontsize=12.5, color='white', pad=9)
ax2.legend(fontsize=9, framealpha=.25, loc='upper left')
ax2.grid(alpha=.13, axis='y')

fig.suptitle('Hubble Tipine Göre Tam Döküm: "Cüce/Düzensiz" Bloğu Neyi Gizliyordu?',
             fontsize=14, color='white', y=.985)
fig.text(.5, .042, 'Blok olarak $+2{,}5\\sigma$ görünen sonuç ayrılınca: **Im tek başına '
                   '$+3{,}3\\sigma$**, Sm ise bant altında $-2{,}3\\sigma$.', ha='center',
         fontsize=9.4, color='#999999')
fig.text(.5, .012, 'Hiçbir tip bloklanmamış, hiçbir altörneklem seçilmemiştir — seçim yapmamak için '
                   'hepsi verilmektedir. BCD ($N=4$) ve S0 ($N=3$) istatistik taşımaz.',
         ha='center', fontsize=9.4, color='#999999')
plt.tight_layout(rect=[0, .072, 1, .952])
plt.savefig('tip_dokumu.png', dpi=145, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print("Grafik 'tip_dokumu.png' olarak kaydedildi.")
