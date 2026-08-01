"""FIT GIRDISI FATURASI: her fitlenen sayiyi ucretlendir, sonra kim kazaniyor?

Sorun. Medyan chi^2 parametre maliyetini gizler; galaksi basina AIC (2k) ise
163 galaksiye yayilmis bir parametrenin gercek bedelini eksik ceker. Dogru hesap
ORNEKLEM GENELINDE toplam fit girdisi sayilarak yapilir:

    K = (galaksi basina parametre) x (galaksi sayisi)
    AIC = sum(chi^2) + 2K       BIC = sum(chi^2) + K*ln(N_nokta)

BIC, AIC'den cok daha sert cezalandirir — "fit girdisi kullanani dusur" kuralinin
dogru formel karsiligi budur.

Modeller ve fit girdileri:
    Yalniz baryonlar          : Y*                    K = 163
    Evrenaki, a_0 TEORIDEN    : Y*                    K = 163   (kuresel fit YOK)
    Evrenaki, b galaksi basina: Y*, b                 K = 326
    LCDM NFW                  : Y*, M200              K = 326
LCDM'in NFW profili ve c200-M200 iliskisi N-cisim'den gelir, donus egrilerine
fitlenmemistir — bu yuzden ucretlendirilmez. Adil kurulum budur.

SONUCLAR (163 galaksi, 3299 nokta).

  Y* SERBEST (0,05-2,0)                 toplam chi2      K       BIC     dBIC
    Yalniz baryonlar                        429140     163    430461  +412833
    Evrenaki, a_0 teoriden                   57683     163     59004   +41376
    Evrenaki, b fitli                        14986     326     17627        0  <-- KAZANAN
    LCDM NFW                                 16526     326     19167    +1539

  Y* BANTLI (0,3-0,8)
    Evrenaki, b fitli                        27615     326     30256    +8278
    LCDM NFW                                 19336     326     21977        0  <-- KAZANAN

SAGLAMLIK (K esit oldugundan dBIC = dchi2):
                              Y* serbest      Y* bantli
    ham                          -1539          +8278
    hata olcekli (chi2/dof=1)     -305          +1273
    en kotu %5 kirpilmis          -178           -767   <-- HUKUM TERSINE DONUYOR
    galaksi basina oy            %55 (1.3s)     %44 (-1.6s)

KRITIK BULGU. Bantli halde ilk 10 galaksi toplam zararin %119'unu tasir; kalan
153 galakside Evrenaki ONDEDIR (dchi2 = -1557). Yani LCDM'in bant zaferi genis
bir ustunlukten degil, ~10 felaket galaksiden gelir. O 10'un yapisal imzasi
yoktur: 9'u kovansiz (B/T=0), medyan v_max 99 km/s (orneklem 110). Kovanli
galaksilerde (n=24) Evrenaki zaten ondedir (dchi2 = -527).

DURUST HUKUM. Fit girdisi ucretlendirildiginde:
  * Esit K'da (326) Evrenaki KAZANIR (serbest Y* ile dBIC -305 ... -1539).
  * Bantli Y* ile totalde LCDM kazanir, ama 153/163 galakside Evrenaki onde.
  * AMA en az fit girdisi kullanan hal (K=163, a_0 teoriden) HERKESE KAYBEDER:
    yasa serbest b'nin yerini tutmuyor (57683'e karsi 14986, 3,85 kat).
    l_omega yasasinin sacilmasi (0,38 dex = 2,4 kat) fit yerine gecmek icin
    fazla genistir. Ceza kurali teoriyi az parametreyle kazandirmiyor.
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
    Ld, Lb = L(SBd), L(SBb)
    return dict(g=os.path.basename(f)[:-11], R=R, Vo=Vo, eV=eV, Vg=Vg, Vd=Vd, Vb=Vb,
                Ld=Ld, Lb=Lb, N=len(R), V=float(Vo.max()),
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


BAR = lambda d, lo, hi: go(d, lambda R, Y, _d=d: np.sqrt(np.maximum(Vbar2(_d, Y), 1e-9)),
                           [min(max(0.5, lo), hi)], [lo], [hi])
EV1 = lambda d, lo, hi: go(d, lambda R, Y, _d=d: np.sqrt(
    np.maximum(Vbar2(_d, Y), 1e-9) + G * Mkaps(_d, Y) / np.sqrt(G * max(Mkaps(_d, Y)[-1], 1e-6) / A0)),
    [min(max(0.5, lo), hi)], [lo], [hi])
EV2 = lambda d, lo, hi: go(d, lambda R, Y, lb, _d=d: np.sqrt(
    np.maximum(Vbar2(_d, Y), 1e-9) + (10 ** lb) * Mkaps(_d, Y)),
    [min(max(0.5, lo), hi), -6.4], [lo, -12], [hi, -1])
LCD = lambda d, lo, hi: go(d, lambda R, Y, lg, _d=d: np.sqrt(
    np.maximum(Vbar2(_d, Y), 1e-9) + v_nfw2(R, 10 ** lg)),
    [min(max(0.5, lo), hi), 11.0], [lo, 7.0], [hi, 13.5])

D = [x for x in (yukle(f) for f in sorted(glob.glob(os.path.join(VERI, '*_rotmod.dat')))) if x]
MOD = [('Yalnız baryonlar', BAR, 1), ('Evrenakı — $a_0$ teoriden', EV1, 1),
       ('Evrenakı — $b$ fitli', EV2, 2), ('ΛCDM NFW', LCD, 2)]
KOS = [('$\\Upsilon_*$ serbest', 0.05, 2.0), ('$\\Upsilon_*$ bantlı', 0.3, 0.8)]

sonuc = {}
for ad, lo, hi in KOS:
    per = {}
    for nm, fn, k in MOD:
        per[nm] = [fn(d, lo, hi) for d in D]
    ok = [i for i in range(len(D)) if all(per[nm][i] is not None for nm, _, _ in MOD)]
    Nd = sum(D[i]['N'] for i in ok)
    sonuc[ad] = dict(ok=ok, Nd=Nd, per={nm: np.array([per[nm][i] for i in ok]) for nm, _, _ in MOD},
                     K={nm: k * len(ok) for nm, _, k in MOD})

print("FIT GIRDISI FATURASI — %d galaksi" % len(D))
for ad, _, _ in KOS:
    R = sonuc[ad]
    print("=" * 100)
    print("%s   (%d galaksi, %d veri noktası)" % (ad.replace('$\\Upsilon_*$', 'Y*'), len(R['ok']), R['Nd']))
    print("  %-30s %11s %6s %10s %11s %10s" % ('model', 'toplam chi2', 'K', 'chi2/dof', 'BIC', 'dBIC'))
    bic = {nm: R['per'][nm].sum() + R['K'][nm] * np.log(R['Nd']) for nm, _, _ in MOD}
    bb = min(bic.values())
    for nm, _, _ in MOD:
        c2, K = R['per'][nm].sum(), R['K'][nm]
        print("  %-30s %11.0f %6d %10.2f %11.0f %+10.0f"
              % (nm.replace('$a_0$', 'a0').replace('$b$', 'b'), c2, K, c2 / (R['Nd'] - K), bic[nm], bic[nm] - bb))
    kaz = min(bic, key=bic.get)
    print("  -> BIC KAZANANI: %s" % kaz.replace('$b$', 'b').replace('$a_0$', 'a0'))

# ---- saglamlik ve zararın kaynagi (esit K: Evr b fitli vs LCDM) --------------
print("=" * 100)
print("SAGLAMLIK — esit K (326), dBIC = dchi2 = Evrenaki - LCDM")
print("  %-30s %14s %14s" % ('olcut', 'Y* serbest', 'Y* bantli'))
sat = []
for etk in ['ham', 'hata ölçekli', 'en kötü %5 kırpılmış', 'galaksi başına oy (%)']:
    v = []
    for ad, _, _ in KOS:
        R = sonuc[ad]
        E, L = R['per']['Evrenakı — $b$ fitli'], R['per']['ΛCDM NFW']
        NN = np.array([D[i]['N'] for i in R['ok']])
        if etk == 'ham':
            v.append(E.sum() - L.sum())
        elif etk == 'hata ölçekli':
            v.append((E.sum() - L.sum()) / (min(E.sum(), L.sum()) / (R['Nd'] - 326)))
        elif etk.startswith('en kötü'):
            q = np.maximum(E / np.maximum(NN - 2, 1), L / np.maximum(NN - 2, 1))
            m = q <= np.percentile(q, 95)
            v.append(E[m].sum() - L[m].sum())
        else:
            v.append(100 * np.mean(E < L))
    sat.append((etk, v))
    print("  %-30s %+14.0f %+14.0f" % (etk, v[0], v[1]))

R = sonuc['$\\Upsilon_*$ bantlı']
E, L = R['per']['Evrenakı — $b$ fitli'], R['per']['ΛCDM NFW']
dd = E - L
srt = np.argsort(-dd)
gg = [D[R['ok'][i]] for i in srt]
kum = np.cumsum(dd[srt])
print("-" * 100)
print("BANTLI HALDE ZARARIN KAYNAGI (toplam %+.0f):" % dd.sum())
print("  %-14s %6s %6s %10s %10s %10s" % ('galaksi', 'v_max', 'B/T', 'chi2 Evr', 'chi2 LCDM', 'katki'))
for j in range(10):
    i = srt[j]
    print("  %-14s %6.0f %6.2f %10.0f %10.0f %+10.0f"
          % (gg[j]['g'], gg[j]['V'], gg[j]['BT'], E[i], L[i], dd[i]))
print("  ilk 10'un katkisi: %+.0f (toplamin %%%.0f'i) ; kalan %d galaksi: %+.0f"
      % (kum[9], 100 * kum[9] / dd.sum(), len(dd) - 10, dd.sum() - kum[9]))
BT = np.array([D[i]['BT'] for i in R['ok']])
print("  kovanli (B/T>0,01, n=%d): %+.0f  ·  kovansiz (n=%d): %+.0f"
      % (int((BT > .01).sum()), dd[BT > .01].sum(), int((BT <= .01).sum()), dd[BT <= .01].sum()))
print("=" * 100)

# ------------------------------- Grafik --------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15.6, 6.6), facecolor='#121212')

ax1.set_facecolor('#121212')
etk = [s[0] for s in sat[:3]]
x = np.arange(3)
w = 0.34
v0 = [s[1][0] for s in sat[:3]]
v1 = [s[1][1] for s in sat[:3]]
ax1.bar(x - w / 2, v0, w, color='#4ade80', label='$\\Upsilon_*$ serbest ($\\leq2{,}0$)', zorder=4)
ax1.bar(x + w / 2, v1, w, color='#f87171', label='$\\Upsilon_*$ bantlı ($0{,}3$–$0{,}8$)', zorder=4)
for i, (a, b) in enumerate(zip(v0, v1)):
    ax1.text(i - w / 2, a + (120 if a > 0 else -320), '%+.0f' % a, ha='center', fontsize=9.4, color='#4ade80')
    ax1.text(i + w / 2, b + (120 if b > 0 else -320), '%+.0f' % b, ha='center', fontsize=9.4, color='#f87171')
ax1.axhline(0, color='#cccccc', lw=1.2, zorder=5)
ax1.set_yscale('symlog', linthresh=200)
ax1.set_xticks(x)
ax1.set_xticklabels(etk, fontsize=9.6)
ax1.set_ylabel('$\\Delta$BIC $=$ Evrenakı $-$ ΛCDM   (eşit $K=326$)', fontsize=10.6)
ax1.text(.985, .965, '▲  ΛCDM kazanıyor', transform=ax1.transAxes, fontsize=10,
         color='#f87171', va='top', ha='right')
ax1.text(.985, .035, '▼  Evrenakı kazanıyor', transform=ax1.transAxes, fontsize=10,
         color='#4ade80', va='bottom', ha='right')
ax1.set_title('Bantlı hüküm kırpmayla tersine dönüyor:\n$+1273 \\rightarrow -767$',
              fontsize=12, color='white', pad=9)
ax1.legend(fontsize=9, framealpha=.25, loc='center left')
ax1.grid(alpha=.13, axis='y')

ax2.set_facecolor('#121212')
ax2.plot(np.arange(1, len(kum) + 1), kum, '-', color='#f87171', lw=2.0, zorder=5)
ax2.axhline(0, color='#cccccc', ls='--', lw=1.1, zorder=3)
ax2.fill_between(np.arange(1, 11), 0, kum[:10], color='#f87171', alpha=.22, zorder=2)
ax2.scatter([10], [kum[9]], s=70, color='#ffcc00', zorder=7)
ax2.annotate('ilk 10 galaksi:\n%+.0f  (toplamın %%%.0f\'i)' % (kum[9], 100 * kum[9] / dd.sum()),
             xy=(10, kum[9]), xytext=(34, kum[9] * 0.86), fontsize=10, color='#ffcc00',
             arrowprops=dict(arrowstyle='->', color='#ffcc00', lw=1.4))
ax2.annotate('kalan 153 galakside\nEvrenakı önde: %+.0f' % (dd.sum() - kum[9]),
             xy=(len(kum), kum[-1]), xytext=(78, kum[9] * 0.40), fontsize=10, color='#4ade80',
             arrowprops=dict(arrowstyle='->', color='#4ade80', lw=1.4))
ax2.set_xlabel('Galaksi sırası (zarara katkıya göre azalan)', fontsize=10.6)
ax2.set_ylabel('Kümülatif $\\Delta\\chi^2$  (Evrenakı $-$ ΛCDM)', fontsize=10.6)
ax2.set_title('Bant zararı 10 galaksiden geliyor,\ngeniş bir üstünlükten değil', fontsize=12,
              color='white', pad=9)
ax2.grid(alpha=.13)

fig.suptitle('Fit Girdisi Faturası: Her Fitlenen Sayı Ücretlendirilince Kim Kazanıyor? '
             '(163 galaksi, 3299 nokta)', fontsize=13.6, color='white', y=.985)
fig.text(.5, .038, 'Sol: eşit $K$ ile serbest $\\Upsilon_*$\'da Evrenakı her ölçütte kazanır; bantlı hâlde '
                   'totalde kaybeder ama kırpılınca kazanır.   Sağ: bantlı zararın tamamı ilk 10 galaksiden '
                   'gelir, o 10\'un yapısal imzası yoktur (9\'u kovansız).',
         ha='center', fontsize=9.2, color='#999999')
fig.text(.5, .008, 'En az fit girdisi kullanan hâl ($a_0$ teoriden, $K=163$) ise herkese kaybeder — '
                   '$\\ell_\\omega$ yasasının 0,38 dex saçılması serbest $b$\'nin yerini tutmuyor (57 683\'e '
                   'karşı 14 986; 3,85 kat).',
         ha='center', fontsize=9.2, color='#999999')
plt.tight_layout(rect=[0, .062, 1, .955])
plt.savefig('fit_girdisi_faturasi.png', dpi=145, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print("Grafik 'fit_girdisi_faturasi.png' olarak kaydedildi.")
