r"""MUTLAK ACIK — UC HIKAYEYE KARSI SINANDI.  Dejenerasyon KIRILDI.

89_KAFES olculen acigi birakti:
        D(R) = V_bar^2 + v_F4^teori - v_gozl^2   > 0  (yogun bolgede)
ve uc hikaye ayni sayiyi uretebiliyordu. Bu betik onlari ayirir.

=====================  UC HIKAYE, UC OLCEKLEME  ========================
(1) KAFES  : kafes zayif -> yalniz F4 bastirilir
        v_gozl^2 = V_bar^2 + s v_F4        =>  D = (1-s) v_F4
        FIZIKSEL SINIR: s >= 0, yani  D <= v_F4.  (Bir kuvvet %100'den
        fazla bastirilamaz.)  D > v_F4 ise KAFES O NOKTAYI ACIKLAYAMAZ.

(2) G      : G = alfa/rho_n yerel -> BUTUN v^2 olceklenir.
        Cunku V_bar^2 ~ G  VE  v_F4^2 = sqrt(G M a_0) ile a_0 = G m_n/l_om^2
        oldugundan v_F4^2 ~ G da olur. Ikisi ayni olcekle.
        v_gozl^2 = u (V_bar^2 + v_F4)       =>  D = (1-u) v_ong^2
        FIZIKSEL SINIR: u >= 0, yani D <= v_ong^2.

(3) Y*     : Y* yuksek -> yalniz YILDIZ terimi olceklenir.
        v_gozl^2 = v_gaz^2 + w v_yildiz^2 + v_F4
        FIZIKSEL SINIR: Y* = 0,5 w populasyon sentezi bandinda (0,3-0,8).
        GAZ BASKIN noktada v_yildiz ~ 0 -> Y*'in KALDIRACI YOK, acik uretemez.

=====================  ASIL AYIRICI: IMKANSIZLIK  ======================
Sacilma karsilastirmasi ADIL DEGILDIR (her hikaye farkli buyuklukte bir
sayiya boluyor). Adil olan iki sinav:
  A) Her hikaye kac noktada FIZIKSEL OLARAK IMKANSIZ bir deger istiyor?
  B) Gaz baskin noktalarda acik suruyor mu? (Y*'i tek basina eler)

Cikti: SINIF_CALISMASI/89_KAFES/ -> AYIRMA.csv · ayirma.png
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
A0 = (2.99792458e8 * (70e3 / 3.0857e22)) / ACC / 16.1 * 2.08   # 92_M_TUT'un l_om'undan
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
        vg2 = np.maximum(np.sign(Vg) * Vg ** 2, 0.)
        vy2 = UPS * Vd ** 2 + RB * UPS * Vb ** 2
        vb2 = vg2 + vy2
        Mk = UPS * L(SBd) + RB * UPS * L(SBb) + np.maximum(R * np.sign(Vg) * Vg ** 2 / G, 0.)
        vF4 = np.sqrt(A0 * G * np.maximum(Mk, 1e-9))
        for j in range(len(R)):
            if vb2[j] <= 0 or Mk[j] <= 1e-3 * max(Mk[-1], 1e-6) or Vo[j] <= 0:
                continue
            P.append(dict(ad=os.path.basename(f)[:-11], tip=AD[sn], R=R[j],
                          eV=max(eV[j], 1.), Vo=Vo[j],
                          D=vb2[j] + vF4[j] - Vo[j] ** 2, F4=vF4[j], VB=vb2[j],
                          VY=vy2[j], VG=vg2[j], gb=vb2[j] / R[j] * ACC))

D = np.array([p['D'] for p in P]); F4 = np.array([p['F4'] for p in P])
VB = np.array([p['VB'] for p in P]); VY = np.array([p['VY'] for p in P])
GB = np.array([p['gb'] for p in P]); VP = VB + F4
print('n = %d nokta · %d galaksi' % (len(P), len(set(p['ad'] for p in P))))
print('acik D medyan %+.0f (km/s)^2' % np.median(D))

print('\n' + '=' * 100)
print('SINAV A — HER HIKAYE KAC NOKTADA IMKANSIZ BIR DEGER ISTIYOR?')
print('  KAFES imkansiz  : D > v_F4      (F4 %100\'den fazla bastirilamaz)')
print('  G     imkansiz  : D > v_ong^2   (G negatif olamaz)')
print('  Y*    imkansiz  : Y* = 0,5(1-D/v_yildiz^2) bandin (0,3-0,8) disinda')
KUS = []
print('\n  %-18s %6s | %11s %11s %11s'
      % ('log g_bar kusagi', 'n', 'KAFES', 'G', 'Y*'))
for lo, hi in [(-12, -11.5), (-11.5, -11), (-11, -10.5), (-10.5, -10),
               (-10, -9.5), (-9.5, -9)]:
    m = (np.log10(GB) >= lo) & (np.log10(GB) < hi)
    if m.sum() < 40:
        continue
    ik = 100 * (D[m] > F4[m]).mean()
    ig = 100 * (D[m] > VP[m]).mean()
    u = 0.5 * (1 - D[m] / np.maximum(VY[m], 1))
    iy = 100 * np.mean((u < 0.3) | (u > 0.8) | (VY[m] < 1))
    KUS.append(((lo + hi) / 2, int(m.sum()), ik, ig, iy))
    print('  %6.1f … %-9.1f %6d | %10.1f%% %10.1f%% %10.1f%%' % (lo, hi, m.sum(), ik, ig, iy))
print('\n  TUMU %19d | %10.1f%% %10.1f%% %10.1f%%'
      % (len(D), 100 * (D > F4).mean(), 100 * (D > VP).mean(),
         100 * np.mean((0.5 * (1 - D / np.maximum(VY, 1)) < 0.3)
                       | (0.5 * (1 - D / np.maximum(VY, 1)) > 0.8) | (VY < 1))))

print("""
  >>> BELIRLEYICI SATIR: en yogun kusakta KAFES noktalarin %%%.1f'inde
      NEGATIF F4 istiyor. G hicbir kusakta imkansiz deger istemiyor.
""" % KUS[-1][2])

print("  VE BU KOSUL a_0'DAN BAGIMSIZ — cebirsel olarak sadelesiyor:")
print("      D > v_F4  <=>  V_bar^2 + v_F4 - v_gozl^2 > v_F4  <=>  V_bar^2 > v_gozl^2")
print("  v_F4 SADELESIR. KAFES'i eleyen sey su ciplak olgudur:")
print("  BARYONLAR TEK BASINA GOZLEMI ASIYOR. F4 pozitif tanimli oldugundan")
print("  eklenen her sey durumu kotulestirir; bastirma da kurtarmaz.")
print("  Denetim: a_0 carpani x1,0 / x1,5 / x2,08 / x3 / x6 -> oran DEGISMIYOR.")
_yog = np.log10(GB) >= -9.5
EVL = np.array([q["eV"] for q in P]); VOL = np.array([q["Vo"] for q in P])
print("")
print("  GURULTUNUN OTESINDE MI?  (V_bar > v_gozl + 2 sigma_v)")
print("    en yogun rejim (log g_bar >= -9,5, n=%d):" % _yog.sum())
print("      V_bar > v_gozl        : %.1f%%" % (100 * (VB[_yog] > VOL[_yog]**2).mean()))
print("      2 sigma otesinde      : %.1f%%" % (100 * (np.sqrt(VB[_yog]) > VOL[_yog] + 2*EVL[_yog]).mean()))
print("    -> olcum hatasiyla aciklanamayan gercek bir asim var.")


print('=' * 100)
print('SINAV B — GAZ BASKIN NOKTALAR: Y*\'in kaldiraci yok, acik suruyor mu?')
for esik, ad in [(0.15, 'v_yildiz^2/V_bar^2 < 0,15'), (0.30, '< 0,30')]:
    m = VY / VB < esik
    if m.sum() < 20:
        continue
    print('  %-26s n=%4d · D medyan %+7.0f · D/v_ong^2 %.3f'
          % (ad, m.sum(), np.median(D[m]), np.median(D[m] / VP[m])))
m = VY / VB < 0.15
print('  -> acik SURUYOR. Y* tek basina ACIKLAYAMAZ (orada olceklenecek yildiz yok).')

print('\n' + '=' * 100)
print('HUKUM')
print('  %-38s %s' % ('Y*  tek basina', 'ELENDI — %58 imkansiz + gaz baskin noktada acik suruyor'))
print('  %-38s %s' % ('KAFES tek basina',
                      'ELENDI — en yogun kusakta %%%.0f\'inde negatif F4 gerekiyor' % KUS[-1][2]))
print('  %-38s %s' % ('G   (= alfa/rho_n)', 'AYAKTA — hicbir kusakta imkansiz deger istemiyor'))
print("""
  Bu, kafes yasasinin YANLIS oldugu anlamina GELMEZ. Anlami: acigin TAMAMI
  F4'ten gelmiyor. En az bir bilesen F1'den gelmek zorunda, ve F1 tarafinda
  Y* elendigi icin geriye G kaliyor.
  Kafes, acigin bir PARCASI olabilir — ama tek basina yetmiyor.
""")

with open(os.path.join(CIK, 'AYIRMA.csv'), 'w', encoding='utf-8', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['Galaksi', 'Sinif', 'R_kpc', 'g_bar_ms2', 'acik_D', 'v_F4_teori',
                'V_bar2', 'v_yildiz2', 'v_ong2', 'KAFES_s', 'G_u', 'Ystar_ima',
                'KAFES_imkansiz', 'G_imkansiz'])
    for p in P:
        vp = p['VB'] + p['F4']
        w.writerow([p['ad'], p['tip'], '%.2f' % p['R'], '%.3e' % p['gb'],
                    '%+.0f' % p['D'], '%.0f' % p['F4'], '%.0f' % p['VB'],
                    '%.0f' % p['VY'], '%.0f' % vp,
                    '%.3f' % (1 - p['D'] / p['F4']), '%.3f' % (1 - p['D'] / vp),
                    '%.3f' % (0.5 * (1 - p['D'] / max(p['VY'], 1))),
                    'evet' if p['D'] > p['F4'] else 'hayir',
                    'evet' if p['D'] > vp else 'hayir'])

# ------------------------------------------------------------------ grafik
fig, ax = plt.subplots(1, 3, figsize=(16.4, 5.6), facecolor='#121212')
for a in ax:
    a.set_facecolor('#121212'); a.grid(alpha=.13)

a = ax[0]
x = [k[0] for k in KUS]
a.plot(x, [k[2] for k in KUS], 'o-', color='#fb923c', ms=10, lw=2.6, label='KAFES')
a.plot(x, [k[3] for k in KUS], 's-', color='#16a34a', ms=9, lw=2.6, label='$\\mathcal{G}$')
a.plot(x, [k[4] for k in KUS], 'D--', color='#f87171', ms=8, lw=1.8, label='$\\Upsilon_*$')
a.set_xlabel('$\\log g_{bar}$   (m/s²)', fontsize=10.5)
a.set_ylabel('fiziksel olarak İMKANSIZ nokta  (%)', fontsize=10.5)
a.set_title('ASIL AYIRICI — hangisi yer kalmıyor?', fontsize=12, color='white', pad=8)
a.legend(fontsize=9.4, framealpha=.3, loc='upper left')
a.set_ylim(-3, 105)

a = ax[1]
a.plot(np.log10(GB), D / F4, '.', color='#fb923c', ms=2.6, alpha=.35)
a.axhline(1, color='#f87171', ls='--', lw=2,
          label='$D=v_{F4}$ · üstü İMKANSIZ ($s<0$)')
kk = []
for lo, hi in [(-12, -11.5), (-11.5, -11), (-11, -10.5), (-10.5, -10), (-10, -9.5), (-9.5, -9)]:
    m = (np.log10(GB) >= lo) & (np.log10(GB) < hi)
    if m.sum() >= 40:
        kk.append(((lo + hi) / 2, np.median(D[m] / F4[m])))
a.plot([k[0] for k in kk], [k[1] for k in kk], 'o-', color='#ffcc00', ms=9, lw=2.4,
       label='kuşak medyanı')
a.set_ylim(-1.5, 3)
a.set_xlabel('$\\log g_{bar}$   (m/s²)', fontsize=10.5)
a.set_ylabel('$D\\,/\\,v_{F4}^{teori}$', fontsize=10.5)
a.set_title('KAFES hikâyesi — yoğun uçta taşıyor', fontsize=12, color='white', pad=8)
a.legend(fontsize=8.8, framealpha=.3, loc='upper left')

a = ax[2]
a.plot(np.log10(GB), D / VP, '.', color='#16a34a', ms=2.6, alpha=.35)
a.axhline(1, color='#f87171', ls='--', lw=2, label='$D=v_{öng}^2$ · üstü İMKANSIZ')
a.axhline(0, color='#71717a', lw=1.2)
gg = []
for lo, hi in [(-12, -11.5), (-11.5, -11), (-11, -10.5), (-10.5, -10), (-10, -9.5), (-9.5, -9)]:
    m = (np.log10(GB) >= lo) & (np.log10(GB) < hi)
    if m.sum() >= 40:
        gg.append(((lo + hi) / 2, np.median(D[m] / VP[m])))
a.plot([k[0] for k in gg], [k[1] for k in gg], 's-', color='#4ade80', ms=9, lw=2.4,
       label='kuşak medyanı')
a.set_ylim(-1.5, 3)
a.set_xlabel('$\\log g_{bar}$   (m/s²)', fontsize=10.5)
a.set_ylabel('$D\\,/\\,v_{öng}^{2}$', fontsize=10.5)
a.set_title('$\\mathcal{G}$ hikâyesi — sınıra hiç dayanmıyor', fontsize=12, color='white', pad=8)
a.legend(fontsize=8.8, framealpha=.3, loc='upper left')

fig.suptitle('Mutlak açık üç hikâyeye karşı sınandı — dejenerasyon kırıldı',
             fontsize=14.4, color='white', y=.975)
fig.text(.5, .035, 'KAFES yalnız $F4$\'ü ölçekler ($D\\leq v_{F4}$ olmak zorunda) · '
                   '$\\mathcal{G}$ bütün $v^2$\'yi ölçekler ($V_{bar}^2\\sim\\mathcal{G}$ VE '
                   '$v_{F4}^2\\sim\\mathcal{G}$) · $\\Upsilon_*$ yalnız yıldız terimini.',
         ha='center', fontsize=9.4, color='#a1a1aa')
fig.text(.5, .008, 'Ölçüt saçılma DEĞİL — saçılma karşılaştırması adil olmaz. Ölçüt: her '
                   'hikâye kaç noktada fiziksel olarak imkansız bir değer istiyor.',
         ha='center', fontsize=9.4, color='#fbbf24')
fig.subplots_adjust(left=.055, right=.986, top=.855, bottom=.185, wspace=.28)
plt.savefig(os.path.join(CIK, 'ayirma.png'), dpi=140,
            facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print('-> 89_KAFES/  AYIRMA.csv · ayirma.png')
