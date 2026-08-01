"""VORTISITE UZUNLUGUNUN YASASI — l_omega evrensel bir sabit DEGILDIR.

6.5.4.3, F4'un genligini nukleonun dolanim debisinden turetir ve vortisite
uzunlugunu tanimlar: l_omega = q_n/(2*gamma_n). Bu ifade tek basina okundugunda
l_omega'yi bir NUKLEON sabiti gibi gosterir — ve oyle olsaydi tum galaksilerde
ayni cikmasi gerekirdi. Cikmiyor: SPARC'in 158 galaksisinde 0.22 kpc ile
22000 kpc arasinda degisiyor.

Teori l_omega'nin evrensel oldugunu IDDIA ETMEZ. Iddia ettigi sey, degisiminin
bir YASAYA uydugudur. Yasa, kozmik desarj olceginden gelir (Ek C satir 13:
S_kosmik = 3*rho_0*H_0) ve SIFIR serbest parametre icerir:

    a_0 = c*H_0/(2*pi) = 1.082e-10 m/s^2
    l_omega = sqrt( G * M_bar / a_0 )

Bu betik o yasayi tum SPARC ornekleminde sinar. Sinav iki soru sorar:
  (1) EGIM: log-log egim 1.00 mi? (yasa dogruysa oyle olmali)
  (2) SACILMA: yasa, "l_omega sabittir" varsayimindan daha mi iyi?

Onemli sonuc: v_F4^2 = G*M_bar/l_omega ile birlestirilince yasa
    v^4 = G * M_bar * a_0
verir — bu BARYONIK TULLY-FISHER iliskisidir. Yani teori BTFR'yi H_0'dan
sifir parametreyle uretir. Teori BTFR'yi VARSAYMAZ; kozmolojik a_0'dan cikarir.

Veri: SPARC (Lelli, McGaugh & Schombert 2016). Y_bul = 1.4*Y_disk; negatif V_gas
isaretli kare; hatalar gercek errV (taban 1 km/s).
"""

import sys
import os
import glob
import warnings

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.optimize import curve_fit
from scipy.stats import spearmanr

warnings.filterwarnings('ignore')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
plt.style.use('dark_background')

G = 4.300917e-6
C_SI = 2.99792458e8
KPC_M = 3.0856776e19
ACC = 1e6 / KPC_M
H0_SI = 70e3 / 3.0857e22
A0 = (C_SI * H0_SI / (2 * np.pi)) / ACC          # (km/s)^2/kpc
VERI_DIZIN = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'veri')

res = []
for f in sorted(glob.glob(os.path.join(VERI_DIZIN, '*_rotmod.dat'))):
    d = np.loadtxt(f)
    if d.ndim < 2 or len(d) < 6:
        continue
    R, Vo, eV, Vg, Vd, Vb, SBd, SBb = [d[:, i] for i in range(8)]
    eV = np.maximum(eV, 1.0)
    if np.any(R <= 0) or Vo.max() <= 0:
        continue
    Rpc = R * 1e3
    L = lambda SB: np.concatenate([[0.0], np.cumsum(
        np.pi * (Rpc[1:] ** 2 - Rpc[:-1] ** 2) * 0.5 * (SB[1:] + SB[:-1]))])
    Ld, Lb = L(SBd), L(SBb)
    Vbar2 = lambda Y: np.sign(Vg) * Vg ** 2 + Y * Vd ** 2 + 1.4 * Y * Vb ** 2
    Mkaps = lambda Y: Y * Ld + 1.4 * Y * Lb + np.maximum(R * np.sign(Vg) * Vg ** 2 / G, 0.0)
    try:
        p, _ = curve_fit(lambda RR, Y, b: np.sqrt(np.maximum(Vbar2(Y), 1e-9) + b * Mkaps(Y)),
                         R, Vo, sigma=eV, p0=[0.5, 4e-7],
                         bounds=([0.05, 1e-12], [2.0, 1e-1]), maxfev=600000)
    except Exception:
        continue
    if p[1] <= 1e-11:
        continue
    Mbar = Mkaps(p[0])[-1]
    if Mbar <= 0:
        continue
    res.append((os.path.basename(f)[:-11], G / p[1], Mbar, float(Vo.max()),
                bool(np.any(Vb > 0))))

ad = np.array([r[0] for r in res])
lom = np.array([r[1] for r in res])
Mb = np.array([r[2] for r in res])
V = np.array([r[3] for r in res])
kov = np.array([r[4] for r in res])
pred = np.sqrt(G * Mb / A0)
ora = lom / pred
lp, lo_ = np.log10(pred), np.log10(lom)
egim, kesme = np.polyfit(lp, lo_, 1)
rho, pv = spearmanr(pred, lom)
sac_yasa = float(np.std(lo_ - lp))
sac_sabit = float(np.std(lo_ - np.median(lo_)))

# --- Rapor ---
print("VORTISITE UZUNLUGUNUN YASASI — %d galaksi, SIFIR serbest parametre" % len(lom))
print("=" * 82)
print("  a_0 = c*H_0/(2*pi) = %.3e m/s^2" % (A0 * ACC))
print("  yasa: l_omega = sqrt(G*M_bar/a_0)")
print("-" * 82)
print("  korelasyon (ongoru vs olcum) : rho = %+.3f   p = %.1e" % (rho, pv))
print("  log-log egim                 : %.2f   (yasa dogruysa 1.00)" % egim)
print("  normalizasyon (medyan oran)  : %.2f" % np.median(ora))
print("  yasa etrafinda sacilma       : %.2f dex (= %.1f kat)" % (sac_yasa, 10 ** sac_yasa))
print("  'sabit' varsayiminin sacilmasi: %.2f dex (= %.1f kat)" % (sac_sabit, 10 ** sac_sabit))
print("  -> yasa, sabit varsayimindan %s" % ('DAHA IYI' if sac_yasa < sac_sabit else 'DAHA KOTU'))
print("-" * 82)
print("  l_omega olculen araligi: %.2f - %.0f kpc (%.0f kat)" % (lom.min(), lom.max(), lom.max() / lom.min()))
print("  kalan kutle egilimi (medyan oran):")
for lo2, hi2, nm in [(0, 80, 'cuce/LSB <80'), (80, 150, 'orta'), (150, 9999, 'kutleli >150')]:
    m = (V >= lo2) & (V < hi2)
    print("    %-14s n=%3d  oran = %.2f" % (nm, m.sum(), np.median(ora[m])))
print("=" * 82)

# --- GRAFIK ---
fig = plt.figure(figsize=(15.0, 7.4), facecolor='#121212')
gs = GridSpec(2, 3, width_ratios=[1.55, 1, 1], height_ratios=[1, 1],
              hspace=0.42, wspace=0.30, left=0.062, right=0.985, top=0.885, bottom=0.10)
axm = fig.add_subplot(gs[:, 0])
axr = fig.add_subplot(gs[0, 1:])
axk = fig.add_subplot(gs[1, 1])
axb = fig.add_subplot(gs[1, 2])
for a in (axm, axr, axk, axb):
    a.set_facecolor('#121212')
    for sp in ('top', 'right'):
        a.spines[sp].set_visible(False)
    for sp in ('bottom', 'left'):
        a.spines[sp].set_color('#444444')
    a.tick_params(colors='#aaaaaa', labelsize=8.5)
    a.grid(True, alpha=0.14, color='white')

# (A) olculen vs ongorulen
xx = np.logspace(np.log10(pred.min() * 0.7), np.log10(pred.max() * 1.4), 50)
axm.loglog(xx, xx, '--', color='#ffffff', lw=1.6, alpha=0.75, zorder=3,
           label='yasa: 1:1 (sıfır parametre)')
axm.loglog(xx, 10 ** np.polyval([egim, kesme], np.log10(xx)), '-', color='#4ade80', lw=2.2,
           zorder=4, label='ölçülen eğim = %.2f' % egim)
axm.axhline(np.median(lom), color='#f472b6', ls=':', lw=1.6, zorder=2,
            label='"$\\ell_\\omega$ sabit" varsayımı')
axm.scatter(pred[~kov], lom[~kov], s=26, c='#ffa040', alpha=0.75, edgecolor='none',
            zorder=5, label='kovansız')
axm.scatter(pred[kov], lom[kov], s=34, c='#7dd3fc', marker='s', alpha=0.8,
            edgecolor='none', zorder=5, label='kovanlı')
axm.set_xlabel('öngörü  $\\sqrt{\\mathcal{G}M_{bar}/a_0}$  (kpc)', fontsize=10.2, color='#cccccc')
axm.set_ylabel('ölçülen  $\\ell_\\omega$  (kpc)', fontsize=10.2, color='#cccccc')
axm.set_title('$\\ell_\\omega$ evrensel değil — yasalı  (%d galaksi)' % len(lom),
              fontsize=11.4, color='white', pad=9)
lg = axm.legend(fontsize=8.2, facecolor='#1a1a1a', edgecolor='#333333', loc='upper left')
for t in lg.get_texts():
    t.set_color('white')

# (B) artik dagilimi: yasa vs sabit
bins = np.linspace(-1.6, 1.6, 34)
axr.hist(lo_ - lp, bins=bins, color='#4ade80', alpha=0.72,
         label='yasaya göre artık  ($\\sigma=%.2f$ dex)' % sac_yasa)
axr.hist(lo_ - np.median(lo_), bins=bins, color='#f472b6', alpha=0.5,
         label='"sabit" varsayımına göre  ($\\sigma=%.2f$ dex)' % sac_sabit)
axr.axvline(0, color='#ffffff', lw=1.2, alpha=0.7)
axr.set_xlabel('$\\log_{10}(\\ell_\\omega^{ölçülen}/\\ell_\\omega^{model})$ (dex)',
               fontsize=9.4, color='#bbbbbb')
axr.set_ylabel('galaksi sayısı', fontsize=9.2, color='#bbbbbb')
axr.set_title('Yasa mı, sabit mi? — saçılma karşılaştırması', fontsize=10.6,
              color='white', pad=7)
lg2 = axr.legend(fontsize=8.0, facecolor='#1a1a1a', edgecolor='#333333', loc='upper right')
for t in lg2.get_texts():
    t.set_color('white')

# (C) kalan kutle egilimi
BX = [(0, 80, 'cüce/LSB'), (80, 150, 'orta'), (150, 9999, 'kütleli')]
xs = np.arange(3)
med = [np.median(ora[(V >= lo2) & (V < hi2)]) for lo2, hi2, _ in BX]
nn = [int(((V >= lo2) & (V < hi2)).sum()) for lo2, hi2, _ in BX]
axk.axhline(1.0, color='#ffffff', ls='--', lw=1.3, alpha=0.7)
axk.plot(xs, med, 'o-', color='#4ade80', lw=2.2, ms=8)
for x, m_, n_ in zip(xs, med, nn):
    axk.text(x, m_ + 0.07, '%.2f' % m_, ha='center', fontsize=8.6, color='#dddddd')
    axk.text(x, 0.86, 'n=%d' % n_, ha='center', fontsize=7.6, color='#888888')
axk.set_xticks(xs)
axk.set_xticklabels([b[2] for b in BX], fontsize=8.4, color='#cccccc')
axk.set_ylabel('ölçülen / öngörülen', fontsize=9.2, color='#bbbbbb')
axk.set_ylim(0.8, 2.3)
axk.set_title('Kalan sistematik', fontsize=10.2, color='white', pad=6)

# (D) BTFR
Vf = np.array([np.median(np.sort(v)[-3:]) for v in
               [np.array([vv]) for vv in V]]).ravel() if False else V
axb.loglog(Mb, Vf, 'o', ms=4.2, color='#ffa040', alpha=0.75, zorder=4, label='SPARC')
Ms = np.logspace(np.log10(Mb.min()), np.log10(Mb.max()), 40)
axb.loglog(Ms, (G * Ms * A0) ** 0.25, '-', color='#4ade80', lw=2.4, zorder=5,
           label='$v^4=\\mathcal{G}M_{bar}a_0$')
axb.set_xlabel('$M_{bar}$ ($M_\\odot$)', fontsize=9.2, color='#bbbbbb')
axb.set_ylabel('$V_{max}$ (km/s)', fontsize=9.2, color='#bbbbbb')
axb.set_title('Yasanın eşdeğeri: BTFR', fontsize=10.2, color='white', pad=6)
lg4 = axb.legend(fontsize=7.8, facecolor='#1a1a1a', edgecolor='#333333', loc='upper left')
for t in lg4.get_texts():
    t.set_color('white')

fig.text(0.5, 0.955, 'Teori $\\ell_\\omega$’nın evrensel olduğunu iddia etmez — '
                     'değişiminin $\\sqrt{\\mathcal{G}M_{bar}/a_0}$ yasasına uyduğunu iddia eder '
                     '($\\rho=%.2f$, eğim $%.2f$)' % (rho, egim),
         ha='center', fontsize=9.8, color='#aaaaaa')
plt.savefig('lomega_yasasi.png', dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print("Grafik 'lomega_yasasi.png' olarak kaydedildi.")
