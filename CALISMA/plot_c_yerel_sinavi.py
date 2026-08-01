"""POSTULAT 4 ILE HESAPLASMA: galaktik olcekte c ne kadar degisebilir?

Itiraz. Teoride sabit bir c yoktur (Postulat 4): c = sqrt(P/rho) yerel bir alan
degeridir. Oyleyse a_0 = c*H_0*(rho_0/rho_n)^2 de galaksiden galaksiye degismeli
ve 6.5.4.5'in sinavi baştan yanlis kurulmus olmalidir.

Etkinin girdigi yer. Ek M-42:
    Lambda = 1 - Phi/c^2 ;  l_loc ~ Lambda ; f_loc ~ Lambda ; c_loc = c*Lambda^2
a_0'da c iki kez gecer — bir kez acikca, bir kez de rho_0 = P_0/c^2 uzerinden.
P_0 ve rho_n sabit tutuldugunda:
    a_0 = c*H_0*(P_0/(rho_n c^2))^2  ~  c^-3
Yani teori-ici etki sapmayi BASTIRMAZ, UCE KATLAR. En elverisli varsayim.

Uc hesap yapilir:
  1) Buyukluk    : Phi/c^2 = (v/c)^2 SPARC ornekleminde ne kadar?
  2) Ileri hesap : c -> c*Lambda^2 gercekten uygulanip 163 galaksi yeniden fit
  3) Tersine     : her galaksi tam otursun diye c ne kadar degismeliydi?

Sonuc. Izin verilen |dc/c| ~ 2.7e-7 ; gereken |dc/c| ~ 0.29. Oran ~1e6.
Siniri koyan sey teorinin kendi basarisidir: ayni Lambda hem c_loc'u hem atomik
frekanslari yonetir, dolayisiyla kutlecekimsel kizila kaymayi dogru vermek
(6.2, M-42) c'yi galaktik dinamikte kilitler. Postulat 4 cignenmedi; yalnizca
c'nin bu problemde bir serbestlik OLMADIGI gosterildi. Bkz. ongoru G-6.
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

G = 4.300917e-6                      # kpc (km/s)^2 / M_sun
C_SI = 2.99792458e8                  # m/s (arka plan)
KPC_M = 3.0856776e19
ACC = 1e6 / KPC_M                    # (km/s)^2/kpc -> m/s^2
H0_SI = 70e3 / 3.0857e22             # 1/s
CH0 = (C_SI * H0_SI) / ACC           # c*H_0, model biriminde
RHO_N = 2.702e17                     # kg/m^3, nukleon oz yogunlugu
RHO_0 = 6.07e33 / C_SI ** 2          # kg/m^3, P_0/c^2
A0 = CH0 * (RHO_0 / RHO_N) ** 2      # teoriden: a_0 = c*H_0*(rho_0/rho_n)^2
RB = 1.4                             # Y_kovan / Y_disk
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


def fit(d, a0):
    """Galaksi basina tek serbest parametre: Y*. b yasadan gelir."""
    def f(R, Y, _d=d, _a=a0):
        M = Mkaps(_d, Y)
        Mb = max(M[-1], 1e-6)
        return np.sqrt(np.maximum(Vbar2(_d, Y), 1e-9) + G * M / np.sqrt(G * Mb / _a))
    try:
        p, _ = curve_fit(f, d['R'], d['Vo'], sigma=d['eV'], p0=[0.5],
                         bounds=([0.05], [3.0]), maxfev=300000)
    except Exception:
        return None
    mv = f(d['R'], p[0])
    if not np.all(np.isfinite(mv)):
        return None
    return np.sum(((mv - d['Vo']) / d['eV']) ** 2) / max(d['N'] - 1, 1)


S = [x for x in (yukle(f) for f in sorted(glob.glob(os.path.join(VERI, '*_rotmod.dat')))) if x]
NG = len(S)

# ---- 1) Buyukluk: Phi/c^2 = (v/c)^2 -----------------------------------------
eps = np.array([(d['V'] * 1e3 / C_SI) ** 2 for d in S])       # Phi/c^2
dc_izin = 2 * eps                                             # |dc_loc/c| = 2 Phi/c^2
da_izin = 6 * eps                                             # |da_0/a_0| = 3|dc/c|

print("POSTULAT 4 SINAVI — %d galaksi" % NG)
print("=" * 78)
print("1) GALAKTIK POTANSIYEL")
print("   v_max                 : %.0f – %.0f km/s" % (min(d['V'] for d in S), max(d['V'] for d in S)))
print("   Phi/c^2               : %.2e – %.2e   (medyan %.2e)" % (eps.min(), eps.max(), np.median(eps)))
print("   |dc_loc/c| = 2Phi/c^2 : %.2e – %.2e   (medyan %.2e)" % (dc_izin.min(), dc_izin.max(), np.median(dc_izin)))
print("   |da_0/a_0| = 6Phi/c^2 : %.2e – %.2e   (medyan %.2e)" % (da_izin.min(), da_izin.max(), np.median(da_izin)))

# ---- 2) Ileri hesap: c_loc = c*Lambda^2 uygulanirsa -------------------------
c_sab, c_loc = [], []
for d, e in zip(S, eps):
    a = fit(d, A0)
    b = fit(d, A0 * (1 - e) ** (-6))      # a_0 ~ c^-3, c_loc = c*Lambda^2 -> a_0 ~ Lambda^-6
    if a is not None and b is not None:
        c_sab.append(a)
        c_loc.append(b)
c_sab, c_loc = np.array(c_sab), np.array(c_loc)
print()
print("2) ILERI HESAP — c_loc = c*Lambda^2 uygulandi")
print("   c sabit    : medyan chi2_ind = %.4f   kabul<1 = %d/%d" % (np.median(c_sab), int(np.sum(c_sab < 1)), NG))
print("   c_loc M-42 : medyan chi2_ind = %.4f   kabul<1 = %d/%d" % (np.median(c_loc), int(np.sum(c_loc < 1)), NG))
print("   fark       : %.2e  ->  OLCULEBILIR ETKI YOK" % abs(np.median(c_loc) - np.median(c_sab)))

# ---- 3) Tersine: her galaksi tam otursun diye c ne kadar degismeliydi? ------
carp = []
olcek = 10.0 ** np.linspace(-3, 3, 121)
for d in S:
    best, bs = None, None
    for sc in olcek:
        r = fit(d, A0 * sc)
        if r is not None and (best is None or r < best):
            best, bs = r, sc
    carp.append(bs if bs else np.nan)
carp = np.array(carp)
ok = np.isfinite(carp)
dc_ger = np.abs(carp[ok] ** (-1 / 3.0) - 1)      # a_0 ~ c^-3 => c_ger/c = s^(-1/3)
print()
print("3) TERSINE HESAP — her galaksi tam otursun diye c ne kadar degismeliydi?")
print("   gereken a_0 carpani : %.2f – %.2f   (medyan %.2f)"
      % (np.percentile(carp[ok], 5), np.percentile(carp[ok], 95), np.median(carp[ok])))
print("   gereken |dc/c|      : %.3f – %.3f   (medyan %.3f)"
      % (np.percentile(dc_ger, 5), np.percentile(dc_ger, 95), np.median(dc_ger)))
print("   izin verilen |dc/c| : %.2e   (M-42 + kizila kayma kilidi)" % np.median(dc_izin))
print("   ORAN                : %.1e kat" % (np.median(dc_ger) / np.median(dc_izin)))
print("=" * 78)
print("SONUC: Postulat 4 cignenmedi — c hala sabit degil, hala sqrt(P/rho), hala")
print("asilabilir. Kapanan sey: galaktik donus egrisi probleminde c bir SERBESTLIK")
print("DEGILDIR. Siniri koyan, teorinin kizila kaymayi dogru vermesidir (ayni Lambda).")

# ---- Grafik ------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15.2, 6.4), facecolor='#121212')

# Sol: gereken vs izin verilen |dc/c|
v = np.array([d['V'] for d in S])
ax1.set_facecolor('#121212')
ax1.scatter(v[ok], dc_ger, s=26, color='#f472b6', alpha=.85, edgecolors='none',
            label='Verinin GEREKTİRDİĞİ  $|\\delta c/c|$', zorder=5)
ax1.scatter(v, dc_izin, s=26, color='#4ade80', alpha=.9, edgecolors='none',
            label='Teorinin İZİN VERDİĞİ  $|\\delta c/c| = 2\\Phi/c^2$   (M-42)', zorder=5)
ax1.axhline(np.median(dc_ger), color='#f472b6', ls='--', lw=1.1, alpha=.7)
ax1.axhline(np.median(dc_izin), color='#4ade80', ls='--', lw=1.1, alpha=.7)
ax1.annotate('', xy=(300, np.median(dc_ger)), xytext=(300, np.median(dc_izin)),
             arrowprops=dict(arrowstyle='<->', color='#ffcc00', lw=1.6))
ax1.text(310, 10 ** (0.5 * (np.log10(np.median(dc_ger)) + np.log10(np.median(dc_izin)))),
         '$10^{6}$ kat', color='#ffcc00', fontsize=13, va='center', fontweight='bold')
ax1.set_yscale('log')
ax1.set_xlabel('$v_{max}$  (km/s)', fontsize=11)
ax1.set_ylabel('$|\\delta c / c|$', fontsize=12)
ax1.set_title('Gereken sapma, izin verilenin bir milyon katı', fontsize=12.5, color='white', pad=9)
ax1.legend(fontsize=9, loc='center left', framealpha=.25)
ax1.grid(alpha=.14)

# Sag: chi^2 — c sabit vs c_loc
ax2.set_facecolor('#121212')
lim = [min(c_sab.min(), c_loc.min()) * .8, max(c_sab.max(), c_loc.max()) * 1.25]
ax2.plot(lim, lim, '--', color='#666666', lw=1.0, zorder=2)
ax2.scatter(c_sab, c_loc, s=30, color='#60a5fa', alpha=.85, edgecolors='none', zorder=5)
ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.set_xlim(lim)
ax2.set_ylim(lim)
ax2.set_xlabel('$\\chi^2_{ind}$  —  $c$ sabit', fontsize=11)
ax2.set_ylabel('$\\chi^2_{ind}$  —  $c_{loc}=c\\Lambda^2$ uygulandı', fontsize=11)
ax2.set_title('İleri hesap: uygulandığında hiçbir şey değişmiyor', fontsize=12.5, color='white', pad=9)
ax2.text(.04, .95, 'medyan: %.4f → %.4f\nfark: %.1e\nkabul<1: %d → %d'
         % (np.median(c_sab), np.median(c_loc), abs(np.median(c_loc) - np.median(c_sab)),
            int(np.sum(c_sab < 1)), int(np.sum(c_loc < 1))),
         transform=ax2.transAxes, fontsize=9.6, color='#4ade80', va='top', family='monospace')
ax2.grid(alpha=.14)

fig.suptitle('Postülat 4 ile Hesaplaşma: Galaktik Ölçekte $c$ Ne Kadar Değişebilir? (%d galaksi)' % NG,
             fontsize=14.5, color='white', y=.985)
fig.text(.5, .005, 'Kilidi koyan, teorinin kendi başarısıdır: aynı $\\Lambda$ hem yayılma hızını '
                   '($c_{loc}\\propto\\Lambda^2$) hem atomik frekansları ($f_{loc}\\propto\\Lambda$) yönetir; '
                   'kütleçekimsel kızıla kaymayı doğru vermek $c$\'yi galaktik dinamikte kilitler.',
         ha='center', fontsize=9.2, color='#999999')
plt.tight_layout(rect=[0, .028, 1, .962])
plt.savefig('c_yerel_sinavi.png', dpi=145, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print("Grafik 'c_yerel_sinavi.png' olarak kaydedildi.")
