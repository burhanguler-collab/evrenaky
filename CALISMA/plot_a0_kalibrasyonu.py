"""a_0 ODUNC KATSAYIDAN KURTULUYOR: cH0/2pi -> cH0*(rho0/rhon)^2.

Sorun. 6.5.4.5'in ilk yazimi a_0 = c*H_0/(2*pi) idi. Teorinin sagladigi sey
yalnizca cH_0 MERTEBESIDIR (H_0 zaten envanterde: S_kosmik = 3*rho_0*H_0).
Boyutsuz 2pi ise MOND literaturundeki sayisal rastlantidan ODUNC alinmisti ve
teorinin hicbir yerinden turetilmemistir.

Kurulum. b galaksi basina fitlenmez, yasadan alinir:
    l_omega = sqrt(G*M_bar/a_0)
    v^2(R)  = V_bar^2(Y*) + G*M_kaps(R)/l_omega
Boylece galaksi basina TEK serbest parametre kalir: Y*. a_0 kureseldir — tum
ornekleme uygulanan tek bir sayi, galaksi basina serbestlik eklemez.

Karsilastirilan iki deger (163 galaksi, ikisi de k=1):
    ODUNC    a_0 = cH_0/2pi                  = 1.082e-10 m/s^2 -> 4.5624
    TEORIDEN a_0 = cH_0*(rho_0/rho_n)^2      = 4.249e-11 m/s^2 -> 2.9404
                 = cH_0/16
rho_0/rho_n = 1/4 uydurma degil, teorinin TURETILMIS sonucudur (Ek C satir 5;
M-1'in rho_0 = P_0/c^2 hal denklemi ve P_0 = (1/4)*rho_n*c^2 sabitlemesi).

Ayrica: serbest tarama optimumu cH_0/16.1 idi; teori degeri (FITLENMEMIS) onu
marjinal olarak GECER (2.9404 < 2.9514). Yani sayi veriye ayarlanmadi, veriyle
ortustu. Diger iki kuresel sabit kaldirac degildir — kutle ussu p=0.50 zaten
optimal, Y_kovan/Y_disk orani duyarsiz.

UYARI: bu bir TURETIM DEGIL, henuz bir ESLESMEDIR. (rho_0/rho_n) oraninin neden
KARESI gectigi turetilmemistir; bu yapilana kadar Ek C rozeti [S] kalir, [T]
verilemez (7.4 md.12/g). BTFR normalizasyon gerilimi de cozulmemistir (md.12/h).
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
KPC_M = 3.0856776e19
ACC = 1e6 / KPC_M
CH0 = (C_SI * (70e3 / 3.0857e22)) / ACC
RHO_N = 2.702e17                  # kg/m^3  nukleon oz yogunlugu
RHO_0 = 6.07e33 / C_SI ** 2       # kg/m^3  P_0/c^2
A0_ESKI = CH0 / (2 * np.pi)                    # odunc: MOND'dan alinan 2pi
A0_YENI = CH0 * (RHO_0 / RHO_N) ** 2           # TEORIDEN: cH0*(rho0/rhon)^2 = cH0/16
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
    Rpc = R * 1e3
    L = lambda SB: np.concatenate([[0.0], np.cumsum(
        np.pi * (Rpc[1:] ** 2 - Rpc[:-1] ** 2) * 0.5 * (SB[1:] + SB[:-1]))])
    return dict(g=os.path.basename(f)[:-11], R=R, Vo=Vo, eV=eV, Vg=Vg, Vd=Vd, Vb=Vb,
                Ld=L(SBd), Lb=L(SBb), N=len(R), V=float(Vo.max()))


Vbar2 = lambda d, Y: np.sign(d['Vg']) * d['Vg'] ** 2 + Y * d['Vd'] ** 2 + RB * Y * d['Vb'] ** 2
Mkaps = lambda d, Y: Y * d['Ld'] + RB * Y * d['Lb'] + np.maximum(d['R'] * np.sign(d['Vg']) * d['Vg'] ** 2 / G, 0.0)


def model(d, a0):
    """Tek serbest parametre: Y*. l_omega yasadan gelir, a_0 disaridan verilir."""
    def f(R, Y, _d=d, _a=a0):
        M = Mkaps(_d, Y)
        Mb = M[-1]
        if Mb <= 0:
            return np.full_like(R, 1e3)
        lom = np.sqrt(G * Mb / _a)
        return np.sqrt(np.maximum(Vbar2(_d, Y), 1e-9) + G * M / lom)
    try:
        p, _ = curve_fit(f, d['R'], d['Vo'], sigma=d['eV'], p0=[0.5],
                         bounds=([0.05], [3.0]), maxfev=300000)
    except Exception:
        return None
    mv = f(d['R'], *p)
    if not np.all(np.isfinite(mv)):
        return None
    c2 = float(np.sum(((mv - d['Vo']) / d['eV']) ** 2))
    return dict(Y=p[0], mv=mv, c2i=c2 / max(d['N'] - 1, 1))


S = []
for f in sorted(glob.glob(os.path.join(VERI, '*_rotmod.dat'))):
    d = yukle(f)
    if d is None or d['N'] < 6:
        continue
    A = model(d, A0_ESKI)
    B = model(d, A0_YENI)
    if A and B:
        S.append((d, A, B))
S.sort(key=lambda t: t[0]['V'])
NG = len(S)
cA = np.array([s[1]['c2i'] for s in S])
cB = np.array([s[2]['c2i'] for s in S])
iyi = int(np.sum(cB < cA))

print("a_0 KALIBRASYONU — %d galaksi, her ikisinde de k=1 (yalniz Y*)" % NG)
print("=" * 78)
print("  ODUNC   a_0 = cH_0/2pi   = %.3e m/s^2 : medyan chi2_ind = %.4f ; kabul<1: %d"
      % (A0_ESKI * ACC, np.median(cA), int(np.sum(cA < 1))))
print("  TEORIDEN a_0 = cH_0/%.1f  = %.3e m/s^2 : medyan chi2_ind = %.4f ; kabul<1: %d"
      % (CH0 / A0_YENI, A0_YENI * ACC, np.median(cB), int(np.sum(cB < 1))))
print("  iyilesen galaksi: %d/%d (%%%.0f)" % (iyi, NG, 100 * iyi / NG))
print("  medyan chi2 azalmasi: %%%.0f" % (100 * (1 - np.median(cB) / np.median(cA))))
print("  rho_0/rho_n = %.4f  ->  katsayi = (rho_0/rho_n)^-2 = %.2f" % (RHO_0 / RHO_N, (RHO_N / RHO_0) ** 2))
print("=" * 78)

NC = 12
NR = int(np.ceil(NG / NC))
H = NR * 1.42 + 1.70
fig = plt.figure(figsize=(NC * 1.85, H), facecolor='#121212')
gs = GridSpec(NR, NC, hspace=0.62, wspace=0.30,
              left=0.016, right=0.996, top=1 - 1.38 / H, bottom=0.012)
for idx, (d, A, B) in enumerate(S):
    a = fig.add_subplot(gs[idx // NC, idx % NC])
    a.set_facecolor('#121212')
    for sp in a.spines.values():
        sp.set_color('#3a3a3a')
        sp.set_linewidth(0.6)
    a.set_xticks([])
    a.set_yticks([])
    a.errorbar(d['R'], d['Vo'], yerr=d['eV'], fmt='o', color='#ffcc00', ms=1.5,
               elinewidth=0.5, capsize=0, zorder=6)
    a.plot(d['R'], np.sqrt(np.maximum(Vbar2(d, B['Y']), 0)), ':', color='#777777',
           lw=0.8, zorder=2)
    a.plot(d['R'], A['mv'], '--', color='#f472b6', lw=1.0, zorder=4)
    a.plot(d['R'], B['mv'], '-', color='#4ade80', lw=1.3, zorder=5)
    kz = B['c2i'] < A['c2i']
    a.set_title(d['g'], fontsize=5.6, color='#4ade80' if kz else '#f472b6', pad=1.6)
    a.text(0.03, 0.93, '%.0f' % d['V'], transform=a.transAxes, fontsize=4.6,
           color='#888888', va='top')
    a.text(0.97, 0.06, '%.1f→%.1f' % (A['c2i'], B['c2i']), transform=a.transAxes,
           fontsize=4.4, color='#aaaaaa', ha='right', va='bottom')
    a.set_xlim(0, d['R'].max() * 1.04)
    a.set_ylim(0, max(d['Vo'].max(), A['mv'].max(), B['mv'].max()) * 1.30)

fig.text(0.5, 1 - 0.30 / H, r'$a_0$ Ödünç Katsayıdan Kurtuluyor: $cH_0/2\pi \;\rightarrow\; cH_0(\rho_0/\rho_n)^2$ '
                            '(%d galaksi, her ikisi de $k=1$, hiçbir yeni serbestlik yok)' % NG,
         ha='center', fontsize=15, color='white')
fig.text(0.5, 1 - 0.66 / H,
         r'pembe kesik: $a_0=cH_0/2\pi$ (ödünç katsayı)  ·  yeşil düz: $a_0=cH_0(\rho_0/\rho_n)^2=cH_0/16$ (teoriden, fitlenmemiş)  ·  '
         'sarı: ölçüm  ·  gri noktalı: baryonlar  ·  başlık rengi = daha iyi olan  ·  '
         'sağ alt: $\\chi^2_{ind}$ önce→sonra',
         ha='center', fontsize=8.6, color='#999999')
fig.text(0.5, 1 - 0.98 / H,
         'medyan $\\chi^2_{ind}$: %.2f → %.2f  (%%%.0f azalma)  ·  '
         'kabul edilebilir fit: %d → %d galaksi  ·  iyileşen: %d/%d'
         % (np.median(cA), np.median(cB), 100 * (1 - np.median(cB) / np.median(cA)),
            int(np.sum(cA < 1)), int(np.sum(cB < 1)), iyi, NG),
         ha='center', fontsize=9.6, color='#4ade80')
plt.savefig('a0_kalibrasyonu_galeri.png', dpi=135, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print("Grafik 'a0_kalibrasyonu_galeri.png' olarak kaydedildi.")
