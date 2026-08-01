"""TARAFSIZ IZGARA: takdiri secim devre disi.

Sorun. Bu bolumdeki hukumler tek sayilarla verildi (ornegin "%55, 1,3 sigma").
Ama her hukum bir dizi TAKDIRI SECIMIN sonucuydu: Y* araligi, ust sinir,
altorneklem, kac parametreye izin verildigi. Farkli secimler farkli hukum veriyor
ve secimi yapan bendim.

Cozum. Secimi devreden cikarmak: her secim bir EKSEN olur, izgaranin TAMAMI
raporlanir, hicbir hucre secilmez.

Izgara (onceden sabitlendi, sonuclara bakilmadan):
  Y* kosulu   : serbest<=2 | serbest<=3 | bant 0,3-0,8 | genis 0,2-1,0
  esitlik     : k=2/k=2 (Evr: Y*,b   ; LCDM: Y*,M200)
                k=3/k=3 (Evr: +R_f   ; LCDM: +c sacilmasi 0,11 dex)
  altorneklem : TUMU | SPIRAL Sa-Sd | Sdm | Sm | Im   (Hubble tipi ana katalogdan)
  olcut       : galaksi basina chi2_ind oyu, binom sigma
  esik        : |sigma|>1 -> onde ; aksi halde AYIRT EDILEMEZ

SONUC — 40 hucre:  Evrenaki onde 10 · LCDM onde 12 · ayirt edilemez 18

  Iki saglam sonuc:
    Im     : 8 hucrenin 7'sinde Evrenaki onde (4'unde >2,5 sigma). En dayanikli bulgu.
    SPIRAL : 8 hucrenin 5'inde LCDM onde, 3'u beraberlik, HICBIRINDE Evrenaki onde degil.
  Geri kalan secime baglidir: "TUMU" satiri +2,3 ile -2,0 arasinda geziyor.

  Izgaranin ortaya cikardigi YENI bulgu (teorinin aleyhine): spiralde k=2 -> k=3
  gecisi Evrenaki'yi KOTULESTIRIR (-0,7 -> -2,6 ; -1,6 -> -3,5). Yani her iki tarafa
  ucuncu parametre verildiginde LCDM'in c sacilmasi, Evrenaki'nin R_f'sinden daha
  cok ise yarar. Muhtemel sebep: R_f galaksilerin %61'inde sinira dayaniyor.

GENEL KAZANAN YOKTUR. Iki cephe vardir: Im teorinin, spiral LCDM'in.
"""

import sys
import os
import glob
import warnings

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from scipy.optimize import curve_fit

warnings.filterwarnings('ignore')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
plt.style.use('dark_background')

G = 4.300917e-6
RHO_CRIT = 3 * 0.07 ** 2 / (8 * np.pi * G)
H_RED, RB = 0.7, 1.4
VERI = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'veri')

UPS = [('$\\Upsilon_*$ serbest $\\leq2$', .05, 2.), ('$\\Upsilon_*$ serbest $\\leq3$', .05, 3.),
       ('$\\Upsilon_*$ bant $0{,}3$–$0{,}8$', .3, .8), ('$\\Upsilon_*$ geniş $0{,}2$–$1{,}0$', .2, 1.)]
EST = [('$k{=}2$', 2), ('$k{=}3$', 3)]
ALT = [('TÜMÜ', list(range(12))), ('SPİRAL\nSa–Sd', list(range(1, 8))),
       ('Sdm', [8]), ('Sm', [9]), ('Im', [10])]


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


def nfw(r, M, dc=0.):
    cc = 10 ** (.905 - .101 * np.log10(M * H_RED / 1e12) + dc)
    r2 = (3 * M / (4 * np.pi * 200 * RHO_CRIT)) ** (1 / 3.)
    rs = r2 / cc
    mu = lambda x: np.log(1 + x) - x / (1 + x)
    return G * M / r * mu(r / rs) / mu(cc)


def go(d, g, p0, lo, hi, k):
    try:
        p, _ = curve_fit(g, d['R'], d['Vo'], sigma=d['eV'], p0=p0, bounds=(lo, hi), maxfev=400000)
    except Exception:
        return None
    mv = g(d['R'], *p)
    if not np.all(np.isfinite(mv)):
        return None
    return float(np.sum(((mv - d['Vo']) / d['eV']) ** 2)) / max(d['N'] - k, 1)


for uad, lo, hi in UPS:
    for ead, kk in EST:
        for d in D:
            V2 = lambda Y, _d=d: np.sign(_d['Vg']) * _d['Vg'] ** 2 + Y * _d['Vd'] ** 2 + RB * Y * _d['Vb'] ** 2
            Mk = lambda Y, _d=d: Y * _d['Ld'] + RB * Y * _d['Lb'] + np.maximum(
                _d['R'] * np.sign(_d['Vg']) * _d['Vg'] ** 2 / G, 0)
            p0 = min(max(.5, lo), hi)
            if kk == 2:
                E = go(d, lambda r, Y, lb: np.sqrt(np.maximum(V2(Y), 1e-9) + (10 ** lb) * Mk(Y)),
                       [p0, -6.4], [lo, -12], [hi, -1], 2)
                Lm = go(d, lambda r, Y, lg: np.sqrt(np.maximum(V2(Y), 1e-9) + nfw(r, 10 ** lg)),
                        [p0, 11.], [lo, 7.], [hi, 13.5], 2)
            else:
                E = go(d, lambda r, Y, lb, rf: np.sqrt(
                    np.maximum(V2(Y), 1e-9) + (10 ** lb) * Mk(Y) / (1 + r / rf)),
                    [p0, -6.4, 10.], [lo, -12, .5], [hi, -1, 30.], 3)
                Lm = go(d, lambda r, Y, lg, dc: np.sqrt(np.maximum(V2(Y), 1e-9) + nfw(r, 10 ** lg, dc)),
                        [p0, 11., 0.], [lo, 7., -.22], [hi, 13.5, .22], 3)
            d.setdefault('f', {})[(uad, ead)] = (E, Lm)

sig = lambda k, n: (k - n / 2.) / np.sqrt(n / 4.)
ROWS = [(u, e) for u, _, _ in UPS for e, _ in EST]
M = np.full((len(ROWS), len(ALT)), np.nan)
TXT = [['' for _ in ALT] for _ in ROWS]
tally = {'E': 0, 'L': 0, '=': 0}
for i, (uad, ead) in enumerate(ROWS):
    for j, (aad, ts) in enumerate(ALT):
        sub = [d for d in D if d['T'] in ts and all(v is not None for v in d['f'][(uad, ead)])]
        n = len(sub)
        if n < 5:
            TXT[i][j] = 'N<5'
            continue
        w = sum(d['f'][(uad, ead)][0] < d['f'][(uad, ead)][1] for d in sub)
        s = sig(w, n)
        M[i, j] = s
        lab = 'E' if s > 1 else ('L' if s < -1 else '=')
        tally[lab] += 1
        TXT[i][j] = '%d/%d\n%+.1f$\\sigma$' % (w, n, s)

print("TARAFSIZ IZGARA — %d hücre" % sum(tally.values()))
print("  Evrenakı önde %d · ΛCDM önde %d · ayırt edilemez %d" % (tally['E'], tally['L'], tally['=']))
for j, (aad, _) in enumerate(ALT):
    kol = M[:, j]
    kol = kol[~np.isnan(kol)]
    if len(kol) == 0:
        continue
    print("  %-14s : %d/%d hücrede Evrenakı önde ; aralık %+.1f … %+.1f"
          % (aad.replace('\n', ' '), int(np.sum(kol > 1)), len(kol), kol.min(), kol.max()))

# ------------------------------ Grafik ---------------------------------------
cmap = LinearSegmentedColormap.from_list('ml', [
    (0.00, '#7c3aed'), (0.35, '#a78bfa'), (0.46, '#3f3f46'),
    (0.54, '#3f3f46'), (0.65, '#4ade80'), (1.00, '#15803d')])
fig, ax = plt.subplots(figsize=(11.6, 8.4), facecolor='#121212')
ax.set_facecolor('#121212')
im = ax.imshow(M, cmap=cmap, vmin=-4, vmax=4, aspect='auto')
for i in range(len(ROWS)):
    for j in range(len(ALT)):
        v = M[i, j]
        c = '#e5e5e5' if np.isnan(v) or abs(v) < 2.6 else '#ffffff'
        ax.text(j, i, TXT[i][j], ha='center', va='center', fontsize=9.2, color=c,
                fontweight='bold' if (not np.isnan(v) and abs(v) > 1) else 'normal')
ax.set_xticks(range(len(ALT)))
ax.set_xticklabels(['%s\n$N{=}%d$' % (a, sum(1 for d in D if d['T'] in t)) for a, t in ALT], fontsize=10)
ax.set_yticks(range(len(ROWS)))
ax.set_yticklabels(['%s   %s' % (u, e) for u, e in ROWS], fontsize=9.4)
for k in range(2, len(ROWS), 2):
    ax.axhline(k - .5, color='#71717a', lw=1.4)
for k in range(1, len(ALT)):
    ax.axvline(k - .5, color='#3f3f46', lw=.8)
cb = fig.colorbar(im, ax=ax, pad=.02, fraction=.035)
cb.set_label('$\\sigma$   (yeşil $=$ Evrenakı önde  ·  mor $=$ ΛCDM önde  ·  gri $=$ ayırt edilemez)',
             fontsize=9.6)
ax.set_title('Tarafsız Izgara: Takdiri Seçim Devre Dışı\n'
             '$4$ $\\Upsilon_*$ koşulu $\\times$ $2$ eşitlik $\\times$ $5$ altörneklem $=$ '
             '$40$ hücre, hiçbiri seçilmedi', fontsize=13.6, color='white', pad=14)
fig.text(.5, .072, 'Hücre sayımı:   Evrenakı önde %d   ·   ΛCDM önde %d   ·   ayırt edilemez %d      '
                   '($|\\sigma|>1$ eşiği)   —   GENEL KAZANAN YOKTUR'
         % (tally['E'], tally['L'], tally['=']), ha='center', fontsize=10.6, color='#d4d4d8')
fig.text(.5, .040, 'İki sağlam sonuç:   Im — 8 hücrenin 7\'sinde Evrenakı önde (tüm analizin en '
                   'dayanıklı bulgusu).   SPİRAL — 5\'inde ΛCDM önde,',
         ha='center', fontsize=9.6, color='#999999')
fig.text(.5, .014, '3\'ü beraberlik, hiçbirinde Evrenakı önde değil.   Sdm ($N{=}9$) istatistik '
                   'taşımaz — hücreleri renkli olsa da yorumlanmamalıdır.',
         ha='center', fontsize=9.6, color='#999999')
plt.tight_layout(rect=[0, .098, 1, .995])
plt.savefig('tarafsiz_izgara.png', dpi=150, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print("Grafik 'tarafsiz_izgara.png' olarak kaydedildi.")
