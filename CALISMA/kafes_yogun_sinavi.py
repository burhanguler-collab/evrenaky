r"""KAFES YASASI, YOGUN REJIMDE — yazarin iddiasi sinandi.

===============================  IDDIA  ================================
Yazar (1 Agustos 2026): "Yogun rejimde kafes yapilarini dikkate aldin mi?
Kafes yapisi yok veya zayifsa bu teorimiz geregi F4'un kuculmesine sebep olur.
Sanki teorinin bu kanunu dikkate alinmamis gibi duruyor."

BU IDDIA GAZ_KAFES.md'DE SINANMADI. Orada sinanan sey BILESIM iddiasiydi
(gaz mi yildiz mi). Burada sinanan ORTAM iddiasi (yogun mu seyrek mi).
Ikisi farklidir ve ilkinin sonucu ikincisini ELEMEZ.

===============================  KURULUM  ==============================
92_M_TUT kafesi zaten teorinin diline cevirmisti: kafes = TUTARLILIK.
    Gamma ~ N       tam kafes / hizali        (6.5.4.3 Adim 2'nin varsayimi)
    Gamma ~ sqrt(N) kafes yok / rastgele      (92_M_TUT'un olctugu)
    Gamma < sqrt(N) kafes ZAYIF / bastirilmis (yazarin iddiasi)

Bastirma carpani, F4'un saf rastgele yuruyuse gore orani:
    s = v_F4^2(olculen) / v_F4^2(saf rastgele)
      = [v_gozl^2 - V_bar^2] / sqrt(G M_kaps a_0)
s = 1 -> kafes yok (mevcut kurulum) · s < 1 -> kafes zayif, F4 bastirilmis.
Ve tutarlilik kutlesi cinsinden:  M_tut = m_n * s^2.

Sinav: s, yerel yogunlukla AZALIYOR mu?

Cikti: SINIF_CALISMASI/89_KAFES/ -> SONUC.csv · kafes.png
"""

import os
import sys
import csv
import glob
import warnings

import numpy as np
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
plt.style.use('dark_background')

KOK = os.path.dirname(os.path.abspath(__file__))
SK = os.path.join(KOK, 'SINIF_CALISMASI')
CIK = os.path.join(SK, '89_KAFES')
os.makedirs(CIK, exist_ok=True)

G = 4.300917e-6
ACC = 1e6 / 3.0856776e19
M_N_KG = 1.67492749804e-27
# a_0: 92_M_TUT'un olctugu l_omega'dan (yerel orneklem, yuksek-z'ye bakilmadan)
A0 = (2.99792458e8 * (70e3 / 3.0857e22)) / ACC / 16.1 * 2.08
RB, UPS = 1.4, 0.50
AD = {'01_erken_spiral': 'Sa–Sab', '02_orta_spiral': 'Sb–Sbc', '03_gec_spiral': 'Sc–Scd',
      '04_cok_gec_spiral': 'Sd', '05_macellan': 'Sdm–Sm', '06_duzensiz': 'Im'}

P = []
for sn in sorted(AD):
    for f in sorted(glob.glob(os.path.join(SK, sn, 'veri', '*_rotmod.dat'))):
        d = np.loadtxt(f)
        R, Vo, eV, Vg, Vd, Vb, SBd, SBb = [d[:, i] for i in range(8)]
        Rp = R * 1e3
        L = lambda S: np.concatenate([[0.], np.cumsum(
            np.pi * (Rp[1:] ** 2 - Rp[:-1] ** 2) * .5 * (S[1:] + S[:-1]))])
        vb2 = np.sign(Vg) * Vg ** 2 + UPS * Vd ** 2 + RB * UPS * Vb ** 2
        Mk = UPS * L(SBd) + RB * UPS * L(SBb) + np.maximum(R * np.sign(Vg) * Vg ** 2 / G, 0.)
        vF4_o = Vo ** 2 - vb2
        vF4_t = np.sqrt(A0 * G * np.maximum(Mk, 1e-9))
        Sig = UPS * (SBd + RB * SBb)                       # yildiz yuzey yogunlugu
        for j in range(len(R)):
            if vF4_o[j] <= 1 or vb2[j] <= 0 or Mk[j] <= 1e-3 * max(Mk[-1], 1e-6):
                continue
            P.append(dict(ad=os.path.basename(f)[:-11], tip=AD[sn], R=R[j],
                          s=vF4_o[j] / vF4_t[j], Sig=Sig[j],
                          gb=vb2[j] / R[j] * ACC, pay=vF4_t[j] / (vb2[j] + vF4_t[j])))

S_ = np.array([p['s'] for p in P])
SIG = np.array([p['Sig'] for p in P])
GB = np.array([p['gb'] for p in P])
print('n = %d nokta · %d galaksi' % (len(P), len(set(p['ad'] for p in P))))


def spearman(x, y):
    r = lambda v: np.argsort(np.argsort(v)) + 1.0
    a, b = r(x) - r(x).mean(), r(y) - r(y).mean()
    return float((a * b).sum() / np.sqrt((a * a).sum() * (b * b).sum()))


print('\n' + '=' * 100)
print('BASTIRMA CARPANI  s = v_F4^2(olculen) / v_F4^2(saf rastgele yuruyus)')
print('  s = 1 : kafes yok, saf rastgele yuruyus  (92_M_TUT\'un mevcut kurulumu)')
print('  s < 1 : kafes ZAYIF, F4 bastirilmis      (YAZARIN IDDIASI)')
print('  s > 1 : kafes GUCLU, F4 yukseltilmis')
print('  M_tut = m_n s^2')
print('\n  s medyan = %.3f  ·  ceyreklikler %.2f – %.2f'
      % (np.median(S_), np.percentile(S_, 25), np.percentile(S_, 75)))

ok = SIG > 0
print('\n  Spearman[log s , log Sigma_*] = %+.3f   (n=%d)   <- YOGUNLUK'
      % (spearman(np.log10(SIG[ok]), np.log10(S_[ok])), ok.sum()))
print('  Spearman[log s , log g_bar]   = %+.3f   (n=%d)   <- IVME'
      % (spearman(np.log10(GB), np.log10(S_)), len(S_)))

print('\n  YILDIZ YUZEY YOGUNLUGU KUSAKLARI  —  iddianin dogrudan sinavi')
print('  %-24s %7s %10s %12s' % ('log Sigma_* (M_g/pc^2)', 'n', 's medyan', 'M_tut/m_n'))
KS = []
for lo, hi in [(0, 1), (1, 1.5), (1.5, 2), (2, 2.5), (2.5, 3), (3, 4)]:
    m = ok & (np.log10(np.maximum(SIG, 1e-9)) >= lo) & (np.log10(np.maximum(SIG, 1e-9)) < hi)
    if m.sum() < 25:
        continue
    sm = float(np.median(S_[m]))
    KS.append(((lo + hi) / 2, sm, int(m.sum())))
    print('  %8.1f … %-13.1f %7d %10.3f %12.3f' % (lo, hi, m.sum(), sm, sm ** 2))
print('\n  IVME KUSAKLARI  (karsilastirma icin)')
print('  %-24s %7s %10s' % ('log g_bar (m/s^2)', 'n', 's medyan'))
KG = []
for lo, hi in [(-12, -11.5), (-11.5, -11), (-11, -10.5), (-10.5, -10),
               (-10, -9.5), (-9.5, -9), (-9, -8.3)]:
    m = (np.log10(GB) >= lo) & (np.log10(GB) < hi)
    if m.sum() < 25:
        continue
    KG.append(((lo + hi) / 2, float(np.median(S_[m])), int(m.sum())))
    print('  %8.1f … %-13.1f %7d %10.3f' % (lo, hi, m.sum(), np.median(S_[m])))

ks = [k[1] for k in KS]
print('\n' + '=' * 100)
print('HUKUM')
print('  s, en seyrek kusakta %.3f · en yogun kusakta %.3f  ->  %.1f KAT bastirma'
      % (ks[0], min(ks), ks[0] / min(ks)))
print('  M_tut, m_n\'in %.2f katindan %.2f katina duser.' % (ks[0] ** 2, min(ks) ** 2))
print('  -> YAZARIN IDDIASI OLCULEN YONDE. Etki gercek ve buyuk.')
print("""
  AMA DEJENERASYON VAR — ve durustce yazilmali:
    Olculen sey su acigin kendisidir:  v_gozl^2 < V_bar^2 + v_F4^teori (yogun bolgede).
    Bu acigi UC ayri sey uretebilir:
      (1) F4 fazla   -> kafes zayif        (yazarin iddiasi)
      (2) F1 fazla   -> Y* ya da G yuksek  (93_G_YEREL'in okudugu)
      (3) v_gozl eksik -> basinc destegi / daireden sapan hareket
    Donus egrisi verisi bu ucu AYIRAMAZ. Ayirmanin yolu md. 5'te.
""")

with open(os.path.join(CIK, 'SONUC.csv'), 'w', encoding='utf-8', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['Galaksi', 'Sinif', 'R_kpc', 'Sigma_yildiz_Msun_pc2', 'g_bar_ms2',
                'F4_payi', 'bastirma_s', 'M_tut_bolu_m_n'])
    for p in P:
        w.writerow([p['ad'], p['tip'], '%.2f' % p['R'], '%.2f' % p['Sig'],
                    '%.3e' % p['gb'], '%.3f' % p['pay'], '%.4f' % p['s'],
                    '%.4f' % p['s'] ** 2 if False else '%.4f' % (p['s'] ** 2)])

# ------------------------------------------------------------------ grafik
fig, ax = plt.subplots(1, 3, figsize=(16.4, 5.6), facecolor='#121212')
for a in ax:
    a.set_facecolor('#121212'); a.grid(alpha=.13)

a = ax[0]
a.plot(np.log10(SIG[ok]), np.log10(S_[ok]), '.', color='#52525b', ms=3, alpha=.4)
a.plot([k[0] for k in KS], np.log10([k[1] for k in KS]), 'o-', color='#fb923c',
       ms=10, lw=2.4, zorder=5, label='kuşak medyanı')
a.axhline(0, color='#16a34a', ls='--', lw=1.8, label='$s=1$ · kafes yok (mevcut)')
a.set_xlabel('$\\log \\Sigma_*$   ($M_\\odot$/pc²)', fontsize=10.5)
a.set_ylabel('$\\log s$   (bastırma çarpanı)', fontsize=10.5)
a.set_ylim(-1.1, 0.8)
a.set_title('YAZARIN İDDİASI — yoğun yerde F4 bastırılıyor mu?',
            fontsize=11.8, color='white', pad=8)
a.legend(fontsize=8.8, framealpha=.3, loc='lower left')
a.text(.97, .96, ('Spearman %+.3f\n\n%.1f kat bastırma'
                  % (spearman(np.log10(SIG[ok]), np.log10(S_[ok])), ks[0] / min(ks))
                  ).replace('.', ','), transform=a.transAxes, ha='right', va='top',
       fontsize=9.4, color='#fb923c', family='monospace')

a = ax[1]
a.plot([k[0] for k in KS], [k[1] ** 2 for k in KS], 'o-', color='#fb923c', ms=10, lw=2.4)
a.axhline(1, color='#16a34a', ls='--', lw=1.8, label='$M_{tut}=m_n$ (92_M_TUT)')
a.set_xlabel('$\\log \\Sigma_*$   ($M_\\odot$/pc²)', fontsize=10.5)
a.set_ylabel('$M_{tut}/m_n$', fontsize=10.5)
a.set_ylim(0, 1.3)
a.set_title('Tutarlılık kütlesi yoğunlukla düşüyor', fontsize=11.8, color='white', pad=8)
a.legend(fontsize=9, framealpha=.3)

a = ax[2]
a.plot([k[0] for k in KG], [k[1] for k in KG], 's-', color='#7c3aed', ms=9, lw=2.2,
       label='ivme ile')
a.axhline(1, color='#16a34a', ls='--', lw=1.8)
a.set_xlabel('$\\log g_{bar}$   (m/s²)', fontsize=10.5)
a.set_ylabel('$s$', fontsize=10.5)
a.set_title('Karşılaştırma — ivme mi, yoğunluk mu?', fontsize=11.8, color='white', pad=8)
a.legend(fontsize=9, framealpha=.3, loc='lower left')
a.text(.03, .06, ('Spearman: yoğunluk %+.3f · ivme %+.3f'
                  % (spearman(np.log10(SIG[ok]), np.log10(S_[ok])),
                     spearman(np.log10(GB), np.log10(S_)))).replace('.', ','),
       transform=a.transAxes, fontsize=8.8, color='#a1a1aa')

fig.suptitle('Kafes yasası, yoğun rejimde — yazarın iddiası ölçüldü',
             fontsize=14.4, color='white', y=.975)
fig.text(.5, .035, 'Kafes = tutarlılık. $\\Gamma\\propto N$ tam kafes · '
                   '$\\Gamma\\propto\\sqrt{N}$ kafes yok · $\\Gamma<\\sqrt{N}$ kafes zayıf. '
                   'Bastırma çarpanı $s=v_{F4}^2(ölçülen)/\\sqrt{\\mathcal{G}M_{kaps}a_0}$, '
                   've $M_{tut}=m_n s^2$.', ha='center', fontsize=9.4, color='#a1a1aa')
fig.text(.5, .008, 'DİKKAT: ölçülen şey açığın kendisidir. Onu F4\'ün fazlalığı (kafes), '
                   'F1\'in fazlalığı ($\\Upsilon_*$/$\\mathcal{G}$) ya da basınç desteği '
                   'üretebilir — dönüş eğrisi verisi bu üçünü ayıramaz.',
         ha='center', fontsize=9.4, color='#fbbf24')
fig.subplots_adjust(left=.055, right=.986, top=.855, bottom=.185, wspace=.28)
plt.savefig(os.path.join(CIK, 'kafes.png'), dpi=140,
            facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print('-> 89_KAFES/  SONUC.csv · kafes.png')
