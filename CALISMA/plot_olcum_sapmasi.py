"""OLCUMDEN SAPMA (km/s): hukum olcut secimine saglam mi?

Soru. Bu bolumdeki butun hukumler chi^2 uzerinden verildi. chi^2 her noktayi
1/sigma^2 ile agirliklandirir; hata cubugu kucuk galaksiler baskin cikar. SPARC'ta
o galaksiler yuksek kaliteli spirallerdir. Hukum bu agirliklandirmanin eseri mi?

Bu betik agirliksiz sinavi yapar: modelin egrisi olculen noktalardan KAC km/s
sapiyor, ve noktalarin kaci olcum hata cubugunun ICINDE kaliyor.

SONUC (163 disk galaksi, hepsi gercek SPARC verisi, Hubble tipleri ana katalogdan):

  Y* SERBEST                RMS Evr  RMS LCDM  hata ici E/L   Evr onde
    TUM DISK  (163)           5.60     6.19      65% / 59%    89/163  +1.2s   <- Evrenaki
    SPIRAL    ( 91)           8.43     7.57      53% / 58%    41/91   -0.9s   <- LCDM
    Sm        ( 23)           3.98     4.63      60% / 68%    14/23   +1.0s
    Im        ( 33)           2.77     4.48      86% / 55%    25/33   +3.0s   <- Evrenaki
  Y* BANTLI
    TUM DISK  (163)           8.80     6.73      47% / 54%    72/163  -1.5s
    SPIRAL    ( 91)          10.45     9.01      45% / 50%    37/91   -1.8s
    Sm        ( 23)           8.80     5.02      25% / 54%     7/23   -1.9s
    Im        ( 33)           4.10     4.78      62% / 55%    20/33   +1.2s

SONUC — VE BEKLENENIN TERSI. Iki olcut HER HUCREDE ayni yonu gosterir; en buyuk
fark 0,4 sigma'dir:
    hucre                    sigma km/s   sigma chi^2
    tum disk / serbest          +1.2         +1.3
    spiral   / serbest          -0.9         -0.7
    Sm       / serbest          +1.0         +0.6
    Im       / serbest          +3.0         +3.3
    tum disk / bantli           -1.5         -1.6
    spiral   / bantli           -1.8         -1.6
    Sm       / bantli           -1.9         -2.3
    Im       / bantli           +1.2         +0.9
Yani chi^2'nin 1/sigma^2 agirliklandirmasi hukmu SAPTIRMAMISTIR. Bu betigin ilk
yazimında "chi^2 ortuk olarak spirallere agirlikli, isaret degisiyor" denmisti;
BU YANLISTI ve geri cekilmistir. Olcum bunun tersini gosterir: hukum olcute
saglamdir.

Geriye kalan gercek bulgu fizikseldir: Im'de modelin noktalarinin %86'si olcum
hata cubugunun ICINDE kalir (LCDM %55). Spiralde ise LCDM onde (%58'e karsi %53).
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
H_RED, RB = 0.7, 1.4
VERI = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'veri')


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
    D.append(dict(T=KT[ad], R=R, Vo=Vo, eV=eV, Vg=Vg, Vd=Vd, Vb=Vb, Ld=L(SBd), Lb=L(SBb), N=len(R)))

Vbar2 = lambda d, Y: np.sign(d['Vg']) * d['Vg'] ** 2 + Y * d['Vd'] ** 2 + RB * Y * d['Vb'] ** 2
Mkaps = lambda d, Y: Y * d['Ld'] + RB * Y * d['Lb'] + np.maximum(
    d['R'] * np.sign(d['Vg']) * d['Vg'] ** 2 / G, 0.0)


def v_nfw2(R, M200):
    cc = 10 ** (0.905 - 0.101 * np.log10(M200 * H_RED / 1e12))
    r200 = (3 * M200 / (4 * np.pi * 200 * RHO_CRIT)) ** (1 / 3.0)
    rs = r200 / cc
    mu = lambda x: np.log(1 + x) - x / (1 + x)
    return G * M200 / R * mu(R / rs) / mu(cc)


def fit(d, g, p0, lo, hi):
    try:
        p, _ = curve_fit(g, d['R'], d['Vo'], sigma=d['eV'], p0=p0, bounds=(lo, hi), maxfev=600000)
    except Exception:
        return None
    mv = g(d['R'], *p)
    return mv if np.all(np.isfinite(mv)) else None


EV = lambda d, lo, hi: fit(d, lambda R, y, lb, _d=d: np.sqrt(
    np.maximum(Vbar2(_d, y), 1e-9) + (10 ** lb) * Mkaps(_d, y)),
    [min(max(.5, lo), hi), -6.4], [lo, -12], [hi, -1])
LC = lambda d, lo, hi: fit(d, lambda R, y, lg, _d=d: np.sqrt(
    np.maximum(Vbar2(_d, y), 1e-9) + v_nfw2(R, 10 ** lg)),
    [min(max(.5, lo), hi), 11.0], [lo, 7.0], [hi, 13.5])

GRP = [('TÜM DİSK', list(range(12))), ('SPİRAL\nSa–Sd', list(range(1, 8))), ('Sm', [9]), ('Im', [10])]
KOS = [('$\\Upsilon_*$ serbest', .05, 2.), ('$\\Upsilon_*$ bantlı', .3, .8)]
sig = lambda k, n: (k - n / 2.) / np.sqrt(n / 4.)
R = {}
for kad, lo, hi in KOS:
    for ad, ts in GRP:
        rE, rL, iE, iL, wR, wC, n = [], [], [], [], 0, 0, 0
        for d in D:
            if d['T'] not in ts:
                continue
            e, l = EV(d, lo, hi), LC(d, lo, hi)
            if e is None or l is None:
                continue
            de, dl = e - d['Vo'], l - d['Vo']
            re, rl = np.sqrt(np.mean(de ** 2)), np.sqrt(np.mean(dl ** 2))
            ce = np.sum((de / d['eV']) ** 2) / max(d['N'] - 2, 1)
            cl = np.sum((dl / d['eV']) ** 2) / max(d['N'] - 2, 1)
            rE.append(re); rL.append(rl)
            iE.append(np.mean(np.abs(de) <= d['eV'])); iL.append(np.mean(np.abs(dl) <= d['eV']))
            wR += re < rl; wC += ce < cl; n += 1
        R[(kad, ad)] = dict(n=n, rE=np.median(rE), rL=np.median(rL),
                            iE=np.median(iE), iL=np.median(iL),
                            sR=sig(wR, n), sC=sig(wC, n), wR=wR, wC=wC)

print("ÖLÇÜMDEN SAPMA — %d disk galaksi" % len(D))
for kad, _, _ in KOS:
    print("=" * 104)
    print("%s   %-14s %5s | %8s %8s | %9s %9s | %11s %11s"
          % (kad.replace('$\\Upsilon_*$', 'Y*'), '', 'N', 'RMS Evr', 'RMS ΛCDM',
             'hata içi E', 'hata içi L', 'sigma km/s', 'sigma chi2'))
    for ad, _ in GRP:
        x = R[(kad, ad)]
        print("%-14s %-14s %5d | %8.2f %8.2f | %8.0f%% %8.0f%% | %+11.1f %+11.1f"
              % ('', ad.replace('\n', ' '), x['n'], x['rE'], x['rL'],
                 100 * x['iE'], 100 * x['iL'], x['sR'], x['sC']))
print("=" * 104)
t = R[('$\\Upsilon_*$ serbest', 'TÜM DİSK')]
fark=max(abs(R[(k,a)]['sR']-R[(k,a)]['sC']) for k,_,_ in KOS for a,_ in GRP)
print("SAGLAMLIK: iki olcut arasindaki en buyuk fark %.1f sigma — hukum olcute saglamdir."%fark)
print("  (Bu betigin ilk yazimindaki 'chi^2 spirallere agirlikli, isaret degisiyor' iddiasi YANLISTI.)")

# ------------------------------ Grafik ---------------------------------------
fig, axs = plt.subplots(1, 3, figsize=(17.4, 6.2), facecolor='#121212')
x = np.arange(len(GRP))
w = .19
CS = {('$\\Upsilon_*$ serbest', 'E'): '#4ade80', ('$\\Upsilon_*$ bantlı', 'E'): '#f87171',
      ('$\\Upsilon_*$ serbest', 'L'): '#a78bfa', ('$\\Upsilon_*$ bantlı', 'L'): '#6d5cc4'}

ax = axs[0]; ax.set_facecolor('#121212')
for j, (kad, _, _) in enumerate(KOS):
    for k, (key, mm) in enumerate([('rE', 'E'), ('rL', 'L')]):
        off = (-1.5 + j + 2 * k) * w
        ax.bar(x + off, [R[(kad, a)][key] for a, _ in GRP], w, color=CS[(kad, mm)], zorder=4)
ax.set_xticks(x); ax.set_xticklabels([a for a, _ in GRP], fontsize=9.4)
ax.set_ylabel('Medyan RMS sapma  (km/s)', fontsize=11)
ax.set_title('Ölçümden sapma — düşük olan iyi', fontsize=12.5, color='white', pad=9)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=CS[(k, m)], label='%s — %s' % ('Evrenakı' if m == 'E' else 'ΛCDM',
          k.replace('$\\Upsilon_*$', '$\\Upsilon_*$'))) for k, _, _ in KOS for m in 'EL'],
          fontsize=7.8, framealpha=.25, loc='upper left')
ax.grid(alpha=.13, axis='y')

ax = axs[1]; ax.set_facecolor('#121212')
for j, (kad, _, _) in enumerate(KOS):
    for k, (key, mm) in enumerate([('iE', 'E'), ('iL', 'L')]):
        off = (-1.5 + j + 2 * k) * w
        v = [100 * R[(kad, a)][key] for a, _ in GRP]
        ax.bar(x + off, v, w, color=CS[(kad, mm)], zorder=4)
im = R[('$\\Upsilon_*$ serbest', 'Im')]
ax.annotate('Im: model noktalarının\n%%%.0f\'i ölçüm hata\nçubuğunun içinde' % (100 * im['iE']),
            xy=(3 - 1.5 * w, 100 * im['iE']), xytext=(1.55, 92), fontsize=9,
            color='#4ade80', arrowprops=dict(arrowstyle='->', color='#4ade80', lw=1.4))
ax.set_xticks(x); ax.set_xticklabels([a for a, _ in GRP], fontsize=9.4)
ax.set_ylabel('Ölçüm hata çubuğu içindeki nokta (%)', fontsize=11)
ax.set_ylim(0, 108)
ax.set_title('Doğrudan denetim — yüksek olan iyi', fontsize=12.5, color='white', pad=9)
ax.grid(alpha=.13, axis='y')

ax = axs[2]; ax.set_facecolor('#121212')
for j, (kad, _, _) in enumerate(KOS):
    for k, (key, hat) in enumerate([('sR', ''), ('sC', '///')]):
        off = (-1.5 + j + 2 * k) * w
        v = [R[(kad, a)][key] for a, _ in GRP]
        c = '#4ade80' if j == 0 else '#f87171'
        ax.bar(x + off, v, w, color=c, alpha=1 if k == 0 else .45, hatch=hat,
               edgecolor='#121212', zorder=4)
ax.axhline(0, color='#cccccc', lw=1.2, zorder=5)
ax.annotate('iki ölçüt her hücrede aynı yönü\ngösteriyor — en büyük fark $0{,}4\\sigma$',
            xy=(0, 1.25), xytext=(.40, 2.60), fontsize=9.2, color='#ffcc00',
            arrowprops=dict(arrowstyle='->', color='#ffcc00', lw=1.4))
ax.set_xticks(x); ax.set_xticklabels([a for a, _ in GRP], fontsize=9.4)
ax.set_ylabel('$\\sigma$   (yukarı $=$ Evrenakı önde)', fontsize=11)
ax.set_title('Sağlamlık: hüküm ölçüte bağlı DEĞİL\ndolu $=$ km/s   ·   taralı $=$ $\\chi^2$',
             fontsize=12.5, color='white', pad=9)
ax.grid(alpha=.13, axis='y')

fig.suptitle('Gerçek Ölçümden Sapma (km/s): Hüküm Ölçüt Seçimine Sağlam mı? (163 disk galaksi, SPARC)',
             fontsize=14, color='white', y=.985)
fig.text(.5, .042, 'Sağ panel bir sağlamlık sınavıdır: $\\chi^2$ noktaları $1/\\sigma^2$ ile '
                   'ağırlıklandırır, km/s sınavı ağırlıklandırmaz. İki ölçüt HER hücrede aynı yönü '
                   'veriyor (en büyük fark $0{,}4\\sigma$) — hüküm ölçüt seçiminin eseri değildir.',
         ha='center', fontsize=9.4, color='#999999')
fig.text(.5, .012, 'Fiziksel bulgu: Im\'de model noktalarının %86\'sı ölçüm hata çubuğunun içinde '
                   '(ΛCDM %55). Spiralde ΛCDM önde (%58\'e karşı %53). Tüm diskte serbest '
                   '$\\Upsilon_*$ ile Evrenakı, bantlı $\\Upsilon_*$ ile ΛCDM önde.',
         ha='center', fontsize=9.4, color='#999999')
plt.tight_layout(rect=[0, .072, 1, .952])
plt.savefig('olcum_sapmasi.png', dpi=145, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print("Grafik 'olcum_sapmasi.png' olarak kaydedildi.")
