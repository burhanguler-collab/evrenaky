"""UPSILON_* BANT SINAVI — teorinin en agir bulgusu, galeri halinde.

Soru. a_0 artik tamamen teoriden geliyor (cH0*(rho0/rhon)^2). Geriye galaksi
basina TEK dis girdi kaliyor: Y* (3.6 mikron kutle/isik orani). Model bu tek
serbestligi KOTUYE mi kullaniyor?

Yontem. Y*'i once serbest birak (0.05-3.0), sonra yildiz populasyon sentezinin
3.6 mikron icin verdigi banda hapset (0.3-0.8), ayni fiti tekrarla. Ayni sinav
LCDM NFW icin de yapilir — o da Y* kullanir, yani karsilastirma adildir.

Sonuc.
    Y* araligi            Evrenaki (k=1)     LCDM NFW (k=2)
    serbest 0.05-3.0           2.94               1.97
    populasyon 0.3-0.8         9.99               2.58     <- Evrenaki DISLANIR
    dar 0.4-0.6               15.81               2.87
    bozulma                    %240                %31

Okunusu. Model, LCDM'den bir parametre AZ kullaniyor ama kullandigi o tek
parametreye COK DAHA FAZLA yasliyor. "Parametre ekonomisi" avantaji, parametrenin
fiziksel olarak izin verilen aralikta kalmasi kosuluna baglidir ve bu kosul su an
saglanmiyor. Bkz. 6.5.4.7 kayit (4) ve 7.4 madde 12 (j).
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
C_SI = 2.99792458e8
ACC = 1e6 / 3.0856776e19
CH0 = (C_SI * (70e3 / 3.0857e22)) / ACC
A0 = CH0 * ((6.07e33 / C_SI ** 2) / 2.702e17) ** 2      # teoriden: cH0*(rho0/rhon)^2
RHO_CRIT = 3 * 0.07 ** 2 / (8 * np.pi * G)
H_RED = 0.7
RB = 1.4
BAND = (0.3, 0.8)                                        # 3.6 um populasyon sentezi
VERI = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'veri')


def yukle(f):
    d = np.loadtxt(f)
    if d.ndim < 2 or len(d) < 6:
        return None
    R, Vo, eV, Vg, Vd, Vb, SBd, SBb = [d[:, i] for i in range(8)]
    eV = np.maximum(eV, 1.0)
    if np.any(R <= 0) or Vo.max() <= 0:
        return None
    Rpc = R * 1e3
    L = lambda SB: np.concatenate([[0.0], np.cumsum(
        np.pi * (Rpc[1:] ** 2 - Rpc[:-1] ** 2) * 0.5 * (SB[1:] + SB[:-1]))])
    return dict(g=os.path.basename(f)[:-11], R=R, Vo=Vo, eV=eV, Vg=Vg, Vd=Vd, Vb=Vb,
                Ld=L(SBd), Lb=L(SBb), N=len(R), V=float(Vo.max()))


Vbar2 = lambda d, Y: np.sign(d['Vg']) * d['Vg'] ** 2 + Y * d['Vd'] ** 2 + RB * Y * d['Vb'] ** 2
Mkaps = lambda d, Y: Y * d['Ld'] + RB * Y * d['Lb'] + np.maximum(
    d['R'] * np.sign(d['Vg']) * d['Vg'] ** 2 / G, 0.0)


def v_evr(d, Y):
    M = Mkaps(d, Y)
    return np.sqrt(np.maximum(Vbar2(d, Y), 1e-9) + G * M / np.sqrt(G * max(M[-1], 1e-6) / A0))


def v_nfw2(R, M200):
    c2 = 10 ** (0.905 - 0.101 * np.log10(M200 * H_RED / 1e12))
    r200 = (3 * M200 / (4 * np.pi * 200 * RHO_CRIT)) ** (1 / 3.0)
    rs = r200 / c2
    mu = lambda x: np.log(1 + x) - x / (1 + x)
    return G * M200 / R * mu(R / rs) / mu(c2)


def fit_evr(d, lo, hi):
    try:
        p, _ = curve_fit(lambda R, Y, _d=d: v_evr(_d, Y), d['R'], d['Vo'], sigma=d['eV'],
                         p0=[min(max(0.5, lo), hi)], bounds=([lo], [hi]), maxfev=300000)
    except Exception:
        return None
    mv = v_evr(d, p[0])
    if not np.all(np.isfinite(mv)):
        return None
    return dict(Y=p[0], mv=mv, c2i=np.sum(((mv - d['Vo']) / d['eV']) ** 2) / max(d['N'] - 1, 1))


def fit_nfw(d, lo, hi):
    f = lambda R, Y, lg, _d=d: np.sqrt(np.maximum(Vbar2(_d, Y), 1e-9) + v_nfw2(R, 10 ** lg))
    try:
        p, _ = curve_fit(f, d['R'], d['Vo'], sigma=d['eV'], p0=[min(max(0.5, lo), hi), 11.0],
                         bounds=([lo, 7.0], [hi, 13.5]), maxfev=300000)
    except Exception:
        return None
    mv = f(d['R'], *p)
    if not np.all(np.isfinite(mv)):
        return None
    return dict(Y=p[0], mv=mv, c2i=np.sum(((mv - d['Vo']) / d['eV']) ** 2) / max(d['N'] - 2, 1))


S = []
for f in sorted(glob.glob(os.path.join(VERI, '*_rotmod.dat'))):
    d = yukle(f)
    if d is None:
        continue
    A = fit_evr(d, 0.05, 3.0)          # serbest
    B = fit_evr(d, *BAND)              # banda hapsedilmis
    L1 = fit_nfw(d, 0.05, 3.0)
    L2 = fit_nfw(d, *BAND)
    if A and B and L1 and L2:
        S.append((d, A, B, L1, L2))
S.sort(key=lambda t: t[0]['V'])
NG = len(S)

cA = np.array([x[1]['c2i'] for x in S])
cB = np.array([x[2]['c2i'] for x in S])
lA = np.array([x[3]['c2i'] for x in S])
lB = np.array([x[4]['c2i'] for x in S])
YA = np.array([x[1]['Y'] for x in S])
disari = np.mean((YA < BAND[0]) | (YA > BAND[1]))

print("UPSILON_* BANT SINAVI — %d galaksi   (a_0 tamamen teoriden: cH0*(rho0/rhon)^2)" % NG)
print("=" * 84)
print("  %-30s %14s %14s" % ("Y* araligi", "Evrenaki k=1", "LCDM k=2"))
print("  %-30s %14.2f %14.2f" % ("serbest (0,05-3,0)", np.median(cA), np.median(lA)))
print("  %-30s %14.2f %14.2f" % ("populasyon sentezi (%.1f-%.1f)" % BAND, np.median(cB), np.median(lB)))
print("  %-30s %13.0f%% %13.0f%%" % ("BOZULMA",
      100 * (np.median(cB) / np.median(cA) - 1), 100 * (np.median(lB) / np.median(lA) - 1)))
print("  %-30s %14.2f %14.2f" % ("serbest medyan Y*", np.median(YA),
      np.median([x[3]['Y'] for x in S])))
print("  bandin disina cikan galaksi: %%%.0f" % (100 * disari))
print("  kabul edilebilir (<1): Evrenaki %d -> %d ;  LCDM %d -> %d"
      % (int(np.sum(cA < 1)), int(np.sum(cB < 1)), int(np.sum(lA < 1)), int(np.sum(lB < 1))))
print("=" * 84)

# ------------------------------- Galeri --------------------------------------
NC = 12
NR = int(np.ceil(NG / NC))
H = NR * 1.42 + 1.95
fig = plt.figure(figsize=(NC * 1.85, H), facecolor='#121212')
gs = GridSpec(NR, NC, hspace=0.62, wspace=0.30, left=0.016, right=0.996,
              top=1 - 1.62 / H, bottom=0.012)
for i, (d, A, B, L1, L2) in enumerate(S):
    a = fig.add_subplot(gs[i // NC, i % NC])
    a.set_facecolor('#121212')
    for sp in a.spines.values():
        sp.set_color('#3a3a3a')
        sp.set_linewidth(0.6)
    a.set_xticks([])
    a.set_yticks([])
    a.errorbar(d['R'], d['Vo'], yerr=d['eV'], fmt='o', color='#ffcc00', ms=1.5,
               elinewidth=0.5, capsize=0, zorder=6)
    a.plot(d['R'], A['mv'], '-', color='#4ade80', lw=1.25, zorder=5)     # serbest
    a.plot(d['R'], B['mv'], '-', color='#f87171', lw=1.25, zorder=4)     # banda hapsedilmis
    a.plot(d['R'], L2['mv'], '--', color='#a78bfa', lw=0.95, zorder=3)   # LCDM banda hapsedilmis
    bozuk = B['c2i'] / max(A['c2i'], 1e-9)
    a.set_title(d['g'], fontsize=5.6, pad=1.6,
                color='#f87171' if bozuk > 3 else ('#fbbf24' if bozuk > 1.5 else '#4ade80'))
    a.text(0.03, 0.93, '%.0f' % d['V'], transform=a.transAxes, fontsize=4.6,
           color='#888888', va='top')
    a.text(0.97, 0.06, '%.1f→%.1f' % (A['c2i'], B['c2i']), transform=a.transAxes,
           fontsize=4.4, color='#aaaaaa', ha='right', va='bottom')
    a.set_xlim(0, d['R'].max() * 1.04)
    a.set_ylim(0, max(d['Vo'].max(), A['mv'].max(), B['mv'].max()) * 1.30)

fig.text(0.5, 1 - 0.30 / H,
         r'$\Upsilon_*$ Bant Sınavı: Model Tek Serbestliğine Ne Kadar Yaslanıyor?  '
         '(%d galaksi, $a_0$ tamamen teoriden)' % NG,
         ha='center', fontsize=15, color='white')
fig.text(0.5, 1 - 0.62 / H,
         r'yeşil: $\Upsilon_*$ serbest (0,05–3,0)  ·  kırmızı: $\Upsilon_*$ popülasyon sentezi bandına '
         r'hapsedilmiş (0,3–0,8)  ·  mor kesik: ΛCDM NFW aynı bantta  ·  sarı: ölçüm  ·  '
         r'sağ alt: $\chi^2_{ind}$ serbest→bantlı',
         ha='center', fontsize=8.6, color='#999999')
fig.text(0.5, 1 - 0.92 / H,
         'medyan $\\chi^2_{ind}$ — Evrenakı: %.2f → %.2f (%%%.0f bozulma)   ·   '
         'ΛCDM: %.2f → %.2f (%%%.0f)   ·   serbest medyan $\\Upsilon_*$ = %.2f, '
         'galaksilerin %%%.0f\'ı bandın dışında'
         % (np.median(cA), np.median(cB), 100 * (np.median(cB) / np.median(cA) - 1),
            np.median(lA), np.median(lB), 100 * (np.median(lB) / np.median(lA) - 1),
            np.median(YA), 100 * disari),
         ha='center', fontsize=9.8, color='#f87171')
fig.text(0.5, 1 - 1.18 / H,
         'başlık rengi: yeşil = bant zarar vermiyor  ·  sarı = 1,5–3 kat bozuluyor  ·  '
         'kırmızı = 3 kattan fazla bozuluyor',
         ha='center', fontsize=8.2, color='#777777')
plt.savefig('upsilon_bant_galeri.png', dpi=135, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print("Grafik 'upsilon_bant_galeri.png' olarak kaydedildi.")
