"""SINIFLAR ARASI CAPRAZ TANI.  Kullanim: python sinif_capraz_tani.py

Tamamlanmis butun sinif klasorlerinin HESAP/SONUC.csv dosyalarini okur ve uc soruyu
yanitlar. Hicbir yeni fit yapmaz — yalnizca kayitli sonuclari birlestirir.

  1. Evrenaki'nin sistematik eksik itimi HANGI DEGISKENLE olcekleniyor?
     (isima, gaz kesri, Vmax, disk olcegi ile korelasyon)
  2. Sapmayi sifirlayacak a_0 carpani sinif sinif ne? Tek sabit yetiyor mu?
  3. Fit, ongorudeki acigi NASIL kapatiyor?  -> Y*'in ongoru degerinden (0,50)
     ne kadar saptigina bakilir. Ayni sinav LCDM icin de yapilir.

3. sorunun cevabi bu calismanin en onemli bulgusudur ve SIMETRIKTIR:
  gec tiplerde Evrenaki Y*'i YUKARI (1,3-1,6), LCDM ise ASAGI (0,06-0,24) ceker.
  Populasyon sentezi bandi 0,3-0,8'dir; yani IKISI DE bandi ihlal eder, ters yonde.
  Dolayisiyla gec tiplerdeki fit karsilastirmasi, ayni parametreyi zit yonde
  koteye kullanan iki model arasindadir — ikisi de fiziksel olarak kabul edilebilir
  degildir.
"""

import os
import sys
import csv
import glob
import warnings

import numpy as np

warnings.filterwarnings('ignore')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
try:
    from scipy.stats import pearsonr, spearmanr
except ImportError:
    pearsonr = spearmanr = None

KOK = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'SINIF_CALISMASI')
AD = {'01_erken_spiral': 'Sa–Sab', '02_orta_spiral': 'Sb–Sbc', '03_gec_spiral': 'Sc–Scd',
      '04_cok_gec_spiral': 'Sd', '05_macellan': 'Sdm–Sm', '06_duzensiz': 'Im'}
SPS = (0.3, 0.8)

sinif, hep = [], []
for sn in sorted(AD):
    p = os.path.join(KOK, sn, 'HESAP', 'SONUC.csv')
    if not os.path.exists(p):
        continue
    kat = {x['Galaksi']: x for x in csv.DictReader(open(os.path.join(KOK, sn, 'KATALOG.csv'), encoding='utf-8'))}
    R = list(csv.DictReader(open(p, encoding='utf-8')))
    f = lambda x, k: float(x[k]) if x[k] else np.nan
    d = dict(sn=sn, ad=AD[sn], n=len(R),
             V=np.array([f(x, 'Vmax_kms') for x in R]),
             E=np.array([f(x, 'DIS_evr_sapma_yuzde') for x in R]),
             L=np.array([f(x, 'DIS_lcdm_sapma_yuzde') for x in R]),
             Ye=np.array([f(x, 'FIT_evr_Ystar') for x in R]),
             Yl=np.array([f(x, 'FIT_lcdm_Ystar') for x in R]),
             Ce=np.array([f(x, 'FIT_evr_chi2ind') for x in R]),
             Cl=np.array([f(x, 'FIT_lcdm_chi2ind') for x in R]),
             Re=np.array([f(x, 'ONG_evr_rms') for x in R]),
             Rl=np.array([f(x, 'ONG_lcdm_rms') for x in R]),
             L36=np.array([float(kat[x['Galaksi']]['L36_1e9Lsun']) for x in R]),
             MHI=np.array([float(kat[x['Galaksi']]['MHI_1e9Msun']) for x in R]),
             Rd=np.array([float(kat[x['Galaksi']]['Rdisk_kpc']) for x in R]))
    sinif.append(d)
    hep.append(d)
if not sinif:
    raise SystemExit('hicbir sinifta SONUC.csv yok')

birlestir = lambda k: np.concatenate([d[k] for d in hep])
N = sum(d['n'] for d in hep)
print('CAPRAZ TANI — %d sinif, %d galaksi' % (len(sinif), N))

print('\n' + '=' * 92)
print('1) EKSIK ITIM HANGI DEGISKENLE OLCEKLENIYOR?')
V, E, L36, MHI, Rd = (birlestir(k) for k in ('V', 'E', 'L36', 'MHI', 'Rd'))
gaz = MHI * 1.33 / np.maximum(MHI * 1.33 + 0.5 * L36, 1e-9)
print('   %-26s %11s %11s' % ('degisken', 'Pearson r', 'Spearman rho'))
sira = []
for ad, x in [('log L[3,6]', np.log10(np.maximum(L36, 1e-4))), ('gaz kesri', gaz),
              ('log Vmax', np.log10(V)), ('log R_disk', np.log10(np.maximum(Rd, 1e-2))),
              ('log M_HI', np.log10(np.maximum(MHI, 1e-4)))]:
    ok = np.isfinite(x) & np.isfinite(E)
    if pearsonr is None:
        r = np.corrcoef(x[ok], E[ok])[0, 1]
        rho = np.nan
    else:
        r, rho = pearsonr(x[ok], E[ok])[0], spearmanr(x[ok], E[ok])[0]
    sira.append((abs(r), ad, r, rho))
for _, ad, r, rho in sorted(sira, reverse=True):
    print('   %-26s %+11.3f %+11.3f' % (ad, r, rho))
en = sorted(sira, reverse=True)[0]
print('   -> en guclu iliski: %s  (r=%+.3f)' % (en[1], en[2]))
if abs(en[2]) < 0.25:
    print('      BU ZAYIFTIR. Sapma, sinanan degiskenlerin HICBIRIYLE anlamli olcude')
    print('      olceklenmiyor. Sinif ortalamalari arasinda fark VAR ama tek bir surekli')
    print('      degiskenle aciklanmiyor -> teshis KONULAMADI.')
elif abs(en[2]) < 0.45:
    print('      ORTA siddette. Yon anlamli ama sacilma buyuk; tek degiskenli bir aciklama')
    print('      icin yeterli degil.')
else:
    print('      GUCLU. Sapma bu degisken boyunca sistematik olarak degisiyor.')
print('      UYARI: isima ve gaz kesri birbirinin aynasidir; hangisi birincil AYRILAMAZ.')
print('      UYARI: bu korelasyon ORNEKLEME DUYARLIDIR — 5 sinifla +0,44 iken 6 sinifla')
print('      %+.2f oldu. Eksik ornekle konulan teshis guvenilmez.' % en[2])

print('\n' + '=' * 92)
print('2) SAPMAYI SIFIRLAYACAK a_0 CARPANI  (SAYISAL COZUM)')
# --- DUZELTME KAYDI (bu bolum bir kez YANLIS hesaplandi) -------------------
# Onceki surum sunu kullaniyordu:
#     carp = lambda e: (1 / (1 + e / 100)) ** 4      # naif 10^(-4*fark)
# Bu formul YALNIZ saf-F4 asimptotunda (v ~ a_0^(1/4)) gecerlidir. Oysa
# sinif_ongoru_vs_fit.py'nin ongorusu IKI TERIMLIDIR:
#     v_ong = sqrt(V_bar^2 + G M_kaps / l_omega)
# a_0 -> k a_0 olunca yalniz F4 terimi sqrt(k) ile olceklenir; V_bar^2 hic
# olceklenmez. Kapali formul yoktur, k sayisal cozulmelidir.
# Hata zararsiz bir kayma DEGILDI: sapmasi F4'un v^2 icindeki payina bagli
# oldugu icin F1'in baskin oldugu (yuksek ivmeli) siniflarda daha buyuktu.
# Ornek: Sb-Sbc ve Im'in sapmasi AYNI (-%6,2) ama F4 paylari 0,49 ve 0,72;
# duzeltme sirasiyla +%31 ve +%13.
# Etki: band x1,29-2,83 -> x1,47-3,76 ; tumu medyani x1,70 -> x2,21.
# Ayni hata 97_BTFR'de de yapilmisti (orada x1,63 yerine x2,02).
# Sayisal cozum sinif_carpan_duzeltme.py'de yapilir; burada OKUNUR.
DYOL = os.path.join(KOK, '_HESAPLAR', 'sinif_carpan_duzeltme.csv')
if not os.path.exists(DYOL):
    print('   ! _HESAPLAR/sinif_carpan_duzeltme.csv yok.')
    print('     Once calistirin:  python sinif_carpan_duzeltme.py')
else:
    DR = list(csv.DictReader(open(DYOL, encoding='utf-8')))
    kd = {}
    for x in DR:
        if x['carpan_DOGRU_sayisal']:
            kd.setdefault(x['Sinif'], []).append(float(x['carpan_DOGRU_sayisal']))
    hepsi = [v for L in kd.values() for v in L]
    print('   %-9s %6s %10s %10s' % ('sinif', 'n', 'DOGRU', '(naif)'))
    naif = lambda e: (1 / (1 + e / 100)) ** 4        # yalniz KIYAS icin
    for d in sinif:
        if d['ad'] in kd:
            print('   %-9s %6d %9.2fx %9.2fx'
                  % (d['ad'], len(kd[d['ad']]), np.median(kd[d['ad']]),
                     np.median(naif(d['E']))))
    tum = float(np.median(hepsi))
    print('   %-9s %6d %9.2fx %9.2fx' % ('TUMU', len(hepsi), tum, np.median(naif(E))))
    mn = min(np.median(v) for v in kd.values())
    mx = max(np.median(v) for v in kd.values())
    print('   -> carpan %.2f ile %.2f arasi degisiyor (%.1f kat). TEK SABIT YETMEZ:'
          % (mn, mx, mx / mn))
    print('      sorun yanlis bir SABIT degil, yanlis bir OLCEKLEME.')
    print('      Kitabin 6.5.4.5 BTFR gerilimi bagimsiz olarak x2,26 istemisti;')
    print('      duzeltilmis TUMU degeri x%.2f — neredeyse birebir.' % tum)
    print('      Diger sayisal olcumler: 97_BTFR x2,02 · 96_ETG x1,85 · 95_RAR x1,61')

print('\n' + '=' * 92)
print('3) FIT ACIGI NASIL KAPATIYOR?  (ongoruda Y*=0,50 sabit; pop. sentezi bandi 0,3-0,8)')
print('   %-9s %4s | %8s %9s | %8s %9s | %10s' %
      ('sinif', 'n', 'Y*_Evr', 'bant disi', 'Y*_LCDM', 'bant disi', 'Evr sapma'))
for d in sinif:
    ye, yl = d['Ye'][np.isfinite(d['Ye'])], d['Yl'][np.isfinite(d['Yl'])]
    de = 100 * np.mean((ye < SPS[0]) | (ye > SPS[1]))
    dl = 100 * np.mean((yl < SPS[0]) | (yl > SPS[1]))
    print('   %-9s %4d | %8.2f %8.0f%% | %8.2f %8.0f%% | %+9.1f%%'
          % (d['ad'], d['n'], np.median(ye), de, np.median(yl), dl, np.median(d['E'])))
print('   -> Evrenaki Y*i YUKARI ceker (acigi yildiz kutlesi sisirerek kapatir).')
print('      LCDM Y*i ASAGI ceker (halosu zaten yettigi icin yildizi siler).')
print('      IKISI DE bandi ihlal eder, TERS yonde. Gec tiplerde fit karsilastirmasi bu yuzden')
print('      fiziksel olarak kabul edilebilir iki model arasinda DEGILDIR.')

print('\n' + '=' * 92)
print('4) SINIF SINIF OZET')
print('   %-9s %4s | %13s | %13s | %11s' % ('sinif', 'n', 'ongoru RMS E/L', 'fit chi2 E/L', 'ongoru oyu'))
for d in sinif:
    oy = int(np.sum(d['Re'] < d['Rl']))
    s = (oy - d['n'] / 2) / np.sqrt(d['n'] / 4)
    print('   %-9s %4d | %5.1f / %-5.1f %s | %5.2f / %-5.2f %s | %3d/%-3d %+.1fs'
          % (d['ad'], d['n'], np.median(d['Re']), np.median(d['Rl']),
             'E' if np.median(d['Re']) < np.median(d['Rl']) else 'L',
             np.median(d['Ce']), np.median(d['Cl']),
             'E' if np.median(d['Ce']) < np.median(d['Cl']) else 'L', oy, d['n'], s))
