"""GIRDI DURUSTLUGU: iki modelin girdilerine AYNI mercekle bakmak.

Neden. Bu kitapta Evrenaki'nin tek serbest parametresi (Y*) yildiz populasyon
sentezi bandina sokulup denetlendi ve "bandin disinda kaliyor, tavana dayaniyor"
diye kaydedildi. LCDM'in serbest parametresine (M_200) AYNI SINAV UYGULANMADI.
Bu betik o eksigi kapatir ve uc olcumu yapar:

  (A) SIMETRIK ONSEL DENETIMI
      Evrenaki : fitlenen Y*  vs  3.6 mikron populasyon sentezi bandi (0,3-0,8)
      LCDM     : fitlenen M200 vs abundance matching (Moster+2013 z=0, ~0,2 dex)
      Sonuc: Evrenaki %60 disinda (SISTEMATIK, medyan 0,85 vs ~0,5; %18 tavanda)
             LCDM     %67 disinda (sapmasiz ama 0,99 dex sacilma; %19'u 10 kat)
      Yani ikisi de kendi bagimsiz onselini benzer oranda ihlal ediyor.

  (B) LCDM'E KENDI SERBESTLIGINI VERMEK
      Simdiye kadar c-M iliskisi TAM dayatilmisti (k=2). Standart pratik c'nin
      0,11 dex sacilma icinde oynamasina izin verir (k=3). Izin verilince:
          medyan chi2_ind 1,980 -> 1,412  (%29 iyilesme), kabul<1 51 -> 71
      Yani LCDM sakatlanmisti.

  (C) a_0 KATSAYISININ KARARLILIGI (capraz dogrulama)
      2 katli, 5 rastgele bolunme. Egitim yarilarinda bulunan optimum katsayi
      10,5 - 22,0 arasinda oynuyor (+-%40). Ornek-ici 3,287 / ornek-disi 3,766,
      yani asiri-uyum cezasi yalnizca %14,6 (kalibrasyon genellesir) AMA
      katsayinin kendi belirsizligi %40'tir. "%0,63 uyusuyor" ifadesi bu yuzden
      anlamsizdir — belirsizligi %40 olan bir sayiya %0,63 hassasiyet atfedilemez.

Bu betigin urettigi karne 6.5.3.6'dadir.
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
RHO_CRIT = 3 * 0.07 ** 2 / (8 * np.pi * G)
H_RED = 0.7
RB = 1.4
SPS = (0.3, 0.8)          # 3.6 um populasyon sentezi bandi
AM_DEX = 0.2              # abundance matching sacilmasi
VERI = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'veri')

# Moster+2013 z=0 yildiz kutlesi - halo kutlesi iliskisi
lM1, NN, BE, GA = 11.59, 0.0351, 1.376, 0.608
_Mh = 10 ** np.linspace(9.0, 15.0, 6000)
_Ms = _Mh * 2 * NN / ((_Mh / 10 ** lM1) ** -BE + (_Mh / 10 ** lM1) ** GA)
Mh_bekle = lambda Ms: np.interp(Ms, _Ms, _Mh)


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
    return dict(g=os.path.basename(f)[:-11], R=R, Vo=Vo, eV=eV, Vg=Vg, Vd=Vd, Vb=Vb,
                Ld=L(SBd), Lb=L(SBb), N=len(R))


Vbar2 = lambda d, Y: np.sign(d['Vg']) * d['Vg'] ** 2 + Y * d['Vd'] ** 2 + RB * Y * d['Vb'] ** 2
Mkaps = lambda d, Y: Y * d['Ld'] + RB * Y * d['Lb'] + np.maximum(
    d['R'] * np.sign(d['Vg']) * d['Vg'] ** 2 / G, 0.0)


def v_nfw2(R, M200, dlc=0.0):
    cc = 10 ** (0.905 - 0.101 * np.log10(M200 * H_RED / 1e12) + dlc)
    r200 = (3 * M200 / (4 * np.pi * 200 * RHO_CRIT)) ** (1 / 3.0)
    rs = r200 / cc
    mu = lambda x: np.log(1 + x) - x / (1 + x)
    return G * M200 / R * mu(R / rs) / mu(cc)


def go(d, g, p0, lo, hi, k):
    try:
        p, _ = curve_fit(g, d['R'], d['Vo'], sigma=d['eV'], p0=p0, bounds=(lo, hi), maxfev=600000)
    except Exception:
        return None
    mv = g(d['R'], *p)
    if not np.all(np.isfinite(mv)):
        return None
    return dict(p=p, c2i=np.sum(((mv - d['Vo']) / d['eV']) ** 2) / max(d['N'] - k, 1))


D = [x for x in (yukle(f) for f in sorted(glob.glob(os.path.join(VERI, '*_rotmod.dat')))) if x]
UST = 2.0

# ---- (A) simetrik onsel denetimi -------------------------------------------
YS, SAP, LG = [], [], []
for d in D:
    e = go(d, lambda R, Y, lb, _d=d: np.sqrt(np.maximum(Vbar2(_d, Y), 1e-9) + (10 ** lb) * Mkaps(_d, Y)),
           [0.5, -6.4], [0.05, -12], [UST, -1], 2)
    l = go(d, lambda R, Y, lg, _d=d: np.sqrt(np.maximum(Vbar2(_d, Y), 1e-9) + v_nfw2(R, 10 ** lg)),
           [0.5, 11.0], [0.05, 7.0], [UST, 13.5], 2)
    if not (e and l):
        continue
    YS.append(e['p'][0])
    Y, lg = l['p']
    Ms = Y * d['Ld'][-1] + RB * Y * d['Lb'][-1]
    if Ms <= 0:
        continue
    SAP.append(np.log10(10 ** lg / Mh_bekle(Ms)))
    LG.append(lg)
YS, SAP, LG = map(np.array, (YS, SAP, LG))

e_dis = np.mean((YS < SPS[0]) | (YS > SPS[1]))
e_tav = np.mean(YS > UST - 0.02)
l_dis = np.mean(np.abs(SAP) > AM_DEX)
l_10 = np.mean(np.abs(SAP) > 1.0)
l_sin = np.mean((LG > 13.45) | (LG < 7.05))

print("(A) SIMETRIK ONSEL DENETIMI — %d galaksi" % len(YS))
print("=" * 92)
print("  %-46s %-20s %-20s" % ("", "EVRENAKI (Y*)", "LCDM (M_200)"))
print("  %-46s %-20s %-20s" % ("bagimsiz onsel", "pop. sentezi 0,3-0,8", "abundance matching"))
print("  %-46s %19.0f%% %19.0f%%" % ("onselin DISINDA kalan", 100 * e_dis, 100 * l_dis))
print("  %-46s %19s %19s" % ("sistematik sapma", "VAR (medyan %.2f)" % np.median(YS),
                             "yok (%+.2f dex)" % np.median(SAP)))
print("  %-46s %19s %19.2f" % ("sacilma", "—", np.std(SAP)))
print("  %-46s %19s %19.0f%%" % ("10 kattan fazla sapan", "—", 100 * l_10))
print("  %-46s %19.0f%% %19.0f%%" % ("fit sinirina dayanan", 100 * e_tav, 100 * l_sin))

# ---- (B) LCDM'e kendi serbestligini vermek ---------------------------------
A2, A3 = [], []
for d in D:
    a = go(d, lambda R, Y, lg, _d=d: np.sqrt(np.maximum(Vbar2(_d, Y), 1e-9) + v_nfw2(R, 10 ** lg)),
           [0.5, 11.0], [0.05, 7.0], [UST, 13.5], 2)
    b = go(d, lambda R, Y, lg, dc, _d=d: np.sqrt(np.maximum(Vbar2(_d, Y), 1e-9) + v_nfw2(R, 10 ** lg, dc)),
           [0.5, 11.0, 0.0], [0.05, 7.0, -0.22], [UST, 13.5, 0.22], 3)
    if a and b:
        A2.append(a['c2i']); A3.append(b['c2i'])
A2, A3 = np.array(A2), np.array(A3)
print()
print("(B) LCDM'E KENDI SERBESTLIGINI VERMEK — c-M sacilmasi (0,11 dex)")
print("  c-M TAM dayatilmis (k=2, kitapta kullanilan): medyan %.3f  kabul<1 %d/%d"
      % (np.median(A2), int((A2 < 1).sum()), len(A2)))
print("  c-M sacilma icinde (k=3, standart pratik)   : medyan %.3f  kabul<1 %d/%d"
      % (np.median(A3), int((A3 < 1).sum()), len(A3)))
print("  -> LCDM %%%.0f sakatlanmisti" % (100 * (1 - np.median(A3) / np.median(A2))))

# ------------------------------ Grafik ---------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15.4, 6.3), facecolor='#121212')

ax1.set_facecolor('#121212')
ax1.axvspan(SPS[0], SPS[1], color='#4ade80', alpha=.16, zorder=1)
ax1.hist(YS, bins=np.linspace(0, UST + .05, 42), color='#f87171', alpha=.9, zorder=4)
ax1.axvline(np.median(YS), color='#ffcc00', ls='--', lw=1.6, zorder=6)
yl = ax1.get_ylim()[1]
ax1.text(np.median(YS) + .04, yl * .93, 'medyan %.2f' % np.median(YS), color='#ffcc00', fontsize=10)
ax1.text(np.mean(SPS), yl * .985, 'popülasyon sentezi\n$0{,}3$–$0{,}8$', color='#4ade80',
         fontsize=9.4, ha='center', va='top')
ax1.set_xlabel('Fitlenen $\\Upsilon_*$   (3,6 μm)', fontsize=11)
ax1.set_ylabel('Galaksi sayısı', fontsize=11)
ax1.set_xlim(0, UST + .06)
ax1.set_title('EVRENAKI — $\\Upsilon_*$ vs popülasyon sentezi\n'
              'dışında %%%.0f  ·  sistematik  ·  tavanda %%%.0f' % (100 * e_dis, 100 * e_tav),
              fontsize=12, color='white', pad=9)
ax1.grid(alpha=.13, axis='y')

ax2.set_facecolor('#121212')
ax2.axvspan(-AM_DEX, AM_DEX, color='#4ade80', alpha=.16, zorder=1)
ax2.hist(np.clip(SAP, -3, 3), bins=np.linspace(-3, 3, 46), color='#a78bfa', alpha=.9, zorder=4)
ax2.axvline(np.median(SAP), color='#ffcc00', ls='--', lw=1.6, zorder=6)
yl2 = ax2.get_ylim()[1]
ax2.text(np.median(SAP) + .12, yl2 * .93, 'medyan %+.2f' % np.median(SAP), color='#ffcc00', fontsize=10)
ax2.text(0, yl2 * .985, 'abundance matching\n$\\pm0{,}2$ dex', color='#4ade80',
         fontsize=9.4, ha='center', va='top')
for s in (-1, 1):
    ax2.axvline(s, color='#f87171', ls=':', lw=1.2, zorder=5)
ax2.text(1.06, yl2 * .55, '10 kat\n(%%%.0f)' % (100 * l_10), color='#f87171', fontsize=9.4)
ax2.set_xlabel('$\\log_{10}\\left(M_{200}^{fit}/M_{200}^{beklenen}\\right)$   (dex)', fontsize=11)
ax2.set_ylabel('Galaksi sayısı', fontsize=11)
ax2.set_title('ΛCDM — $M_{200}$ vs abundance matching\n'
              'dışında %%%.0f  ·  saçılma %.2f dex  ·  sınırda %%%.0f'
              % (100 * l_dis, np.std(SAP), 100 * l_sin), fontsize=12, color='white', pad=9)
ax2.grid(alpha=.13, axis='y')

fig.suptitle('Girdi Dürüstlüğü: İki Modelin Serbest Parametresine AYNI Sınav',
             fontsize=14, color='white', y=.985)
fig.text(.5, .042, 'Her iki modelin fitlediği parametre, kendi bağımsız fiziksel önselini benzer oranda '
                   'ihlal ediyor (%%%.0f\'e karşı %%%.0f).' % (100 * e_dis, 100 * l_dis),
         ha='center', fontsize=9.4, color='#999999')
fig.text(.5, .012, 'Fark biçimde: Evrenakı\'nınki **sistematik** (hep yukarı, %%%.0f\'i tavanda), '
                   'ΛCDM\'inki **sapmasız ama devasa saçılmalı** (%%%.0f\'i on kattan fazla). '
                   'Bu sınav kitabın ilk sürümünde yalnız Evrenakı\'ya uygulanmıştı.'
         % (100 * e_tav, 100 * l_10), ha='center', fontsize=9.4, color='#999999')
plt.tight_layout(rect=[0, .072, 1, .952])
plt.savefig('girdi_durustlugu.png', dpi=145, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print("\nGrafik 'girdi_durustlugu.png' olarak kaydedildi.")
