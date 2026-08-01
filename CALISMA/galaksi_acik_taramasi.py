r"""GALAKSI BASINA ACIGI NE ONGORUYOR? — 89_KAFES/GOZLEMSEL.md md.7 madde 1.

===============================  OLGU  =================================
Acik  D = V_bar^2 + v_F4 - v_gozl^2  varyansinin %68'i GALAKSILER ARASI.
Ve galaksi basina degisen butun BILINEN adaylar elendi:
    Y* (AYIRMA.md) · mesafe ve egiklik (GOZLEMSEL.md) · basinc destegi · kafes
Geriye adi olmayan bir %68 kaldi. Bu betik onu ONGOREN degiskeni arar.

=============================  YONTEM VE TUZAK  ========================
Galaksi basina hedef:  x = medyan(D/v_ong^2)
14 aday degisken taranir. AMA BU BIR TARAMADIR:
  - 14 degisken · n=52  ->  tesaduf en iyi |rho| ~ 0,30-0,35 verir
  - Bu yuzden "BASKA-YERE-BAKMA" duzeltmesi hesaplanir: rastgele
    permutasyonla en iyi |rho|'nun bos dagilimi kurulur.
  - Bir degisken ancak o bos dagilimi ASARSA aday sayilir.
Ayrica iki orneklem kullanilir:
    YOGUN  : yalniz log g_bar >= -10 noktalari (acigin oldugu rejim, n~52)
    TUM    : butun egri (n~137, daha guclu ama acik seyreltilmis)

Cikti: SINIF_CALISMASI/88_TARAMA/ -> SONUC.csv · tarama.png
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
CIK = os.path.join(SK, '88_TARAMA')
os.makedirs(CIK, exist_ok=True)

G = 4.300917e-6
ACC = 1e6 / 3.0856776e19
A0 = (2.99792458e8 * (70e3 / 3.0857e22)) / ACC / 16.1 * 2.08
RB, UPS = 1.4, 0.50
AD = {'01_erken_spiral': 'Sa–Sab', '02_orta_spiral': 'Sb–Sbc', '03_gec_spiral': 'Sc–Scd',
      '04_cok_gec_spiral': 'Sd', '05_macellan': 'Sdm–Sm', '06_duzensiz': 'Im'}

GAL = {}
for sn in sorted(AD):
    KAT = {r['Galaksi']: r for r in csv.DictReader(
        open(os.path.join(SK, sn, 'KATALOG.csv'), encoding='utf-8'))}
    for f in sorted(glob.glob(os.path.join(SK, sn, 'veri', '*_rotmod.dat'))):
        ad = os.path.basename(f)[:-11]
        k = KAT[ad]
        d = np.loadtxt(f)
        R, Vo, eV, Vg, Vd, Vb, SBd, SBb = [d[:, i] for i in range(8)]
        Rp = R * 1e3
        L = lambda S: np.concatenate([[0.], np.cumsum(
            np.pi * (Rp[1:] ** 2 - Rp[:-1] ** 2) * .5 * (S[1:] + S[:-1]))])
        vg2 = np.maximum(np.sign(Vg) * Vg ** 2, 0.)
        vbul = RB * UPS * Vb ** 2
        vb2 = vg2 + UPS * Vd ** 2 + vbul
        Mk = UPS * L(SBd) + RB * UPS * L(SBb) + np.maximum(R * np.sign(Vg) * Vg ** 2 / G, 0.)
        F4 = np.sqrt(A0 * G * np.maximum(Mk, 1e-9))
        ok = (vb2 > 0) & (Mk > 1e-3 * max(Mk[-1], 1e-6)) & (Vo > 0)
        if ok.sum() < 3:
            continue
        x = (vb2 + F4 - Vo ** 2) / (vb2 + F4)
        gb = np.log10(np.maximum(vb2 / np.maximum(R, 1e-9) * ACC, 1e-30))
        yg = ok & (gb >= -10)
        L36 = float(k['L36_1e9Lsun']); MHI = float(k['MHI_1e9Msun'])
        Mb = max(Mk[-1], 1e-6)
        GAL[ad] = dict(
            tip=AD[sn], n=int(ok.sum()), n_yog=int(yg.sum()),
            x_tum=float(np.median(x[ok])),
            x_yog=float(np.median(x[yg])) if yg.sum() >= 3 else np.nan,
            # --- aday degiskenler ---
            lMb=np.log10(Mb), lL36=np.log10(max(L36, 1e-4)),
            lSBeff=np.log10(max(float(k['SBeff']), 1e-3)),
            lSBdisk=np.log10(max(float(k['SBdisk']), 1e-3)),
            lRd=np.log10(max(float(k['Rdisk_kpc']), 1e-3)),
            lReff=np.log10(max(float(k['Reff_kpc']), 1e-3)),
            lVf=np.log10(max(float(k['Vflat_kms']), 1.0)),
            gaz=1.33 * MHI / max(1.33 * MHI + 0.5 * L36, 1e-9),
            T=float(k['T']), inc=float(k['Inc_deg']), Q=float(k['Q']),
            lD=np.log10(float(k['D_Mpc'])),
            lRHIRd=np.log10(max(float(k['RHI_kpc']), 1e-3)
                            / max(float(k['Rdisk_kpc']), 1e-3)),
            yog_kesri=float(np.mean(gb[ok] >= -10)),
            lkovan=np.log10(max(float(np.median(vbul[ok] / vb2[ok])), 1e-4)))

ADAY = [('log M_bar', 'lMb'), ('log L[3,6]', 'lL36'), ('log SB_eff', 'lSBeff'),
        ('log SB_disk', 'lSBdisk'), ('log R_disk', 'lRd'), ('log R_eff', 'lReff'),
        ('log V_flat', 'lVf'), ('gaz kesri', 'gaz'), ('morfoloji T', 'T'),
        ('eğiklik', 'inc'), ('SPARC Q', 'Q'), ('log mesafe', 'lD'),
        ('log R_HI/R_disk', 'lRHIRd'), ('log kovan kesri', 'lkovan')]


def spearman(x, y):
    r = lambda v: np.argsort(np.argsort(v)) + 1.0
    a, b = r(x) - r(x).mean(), r(y) - r(y).mean()
    return float((a * b).sum() / np.sqrt((a * a).sum() * (b * b).sum()))


rng = np.random.default_rng(20260801)


def bos_dagilim(X, n_deg, N=4000):
    """Baska-yere-bakma: hedefi karistirip en iyi |rho|'nun bos dagilimini kur."""
    en = np.empty(N)
    for i in range(N):
        y = rng.permutation(X[0])
        en[i] = max(abs(spearman(x, y)) for x in X[1])
    return en


for etiket, alan, nmin in [('YOGUN REJIM (log g_bar >= -10)', 'x_yog', 3),
                           ('BUTUN EGRI', 'x_tum', 3)]:
    ads = [a for a in GAL if np.isfinite(GAL[a][alan]) and GAL[a]['n_yog' if alan == 'x_yog' else 'n'] >= nmin]
    y = np.array([GAL[a][alan] for a in ads])
    print('\n' + '=' * 100)
    print('%s  ·  n = %d galaksi' % (etiket, len(ads)))
    print('  hedef: medyan(D/v_ong^2) = %+.3f · sacilma %.3f' % (np.median(y), np.std(y)))
    sira = []
    for ad, alan2 in ADAY:
        x = np.array([GAL[a][alan2] for a in ads])
        if np.std(x) == 0:
            continue
        sira.append((abs(spearman(x, y)), ad, spearman(x, y), x))
    sira.sort(reverse=True)
    en_bos = bos_dagilim((y, [s[3] for s in sira]), len(sira))
    esik95 = float(np.percentile(en_bos, 95))
    print('  BASKA-YERE-BAKMA esigi: %d degisken tarandi, tesadufi en iyi |rho|\'nun'
          % len(sira))
    print('  %%95 dilimi = %.3f. Bir degisken ancak bunu ASARSA aday sayilir.' % esik95)
    print('\n  %-22s %11s %11s %s' % ('değişken', 'Spearman', '|rho|', 'karar'))
    for a, ad, r, _ in sira:
        print('  %-22s %+11.3f %11.3f %s'
              % (ad, r, a, 'ADAY' if a > esik95 else ''))
    if sira[0][0] > esik95:
        print('\n  -> EN IYI: %s (rho=%+.3f) esigi ASIYOR. p_baska-yere ~ %.3f'
              % (sira[0][1], sira[0][2], float(np.mean(en_bos >= sira[0][0]))))
    else:
        print('\n  -> HICBIRI esigi asmiyor. Bu 14 degisken arasinda %68\'i ongoren YOK.')
    if alan == 'x_yog':
        SIRA_Y, ESIK_Y, BOS_Y, ADS_Y, Y_Y = sira, esik95, en_bos, ads, y
    else:
        SIRA_T, ESIK_T, ADS_T, Y_T = sira, esik95, ads, y

with open(os.path.join(CIK, 'SONUC.csv'), 'w', encoding='utf-8', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['Galaksi', 'Sinif', 'n_nokta', 'n_yogun', 'acik_tum', 'acik_yogun']
               + [a[0] for a in ADAY])
    for a in sorted(GAL, key=lambda z: -GAL[z]['x_tum']):
        g = GAL[a]
        w.writerow([a, g['tip'], g['n'], g['n_yog'], '%+.4f' % g['x_tum'],
                    '' if not np.isfinite(g['x_yog']) else '%+.4f' % g['x_yog']]
                   + ['%.4f' % g[k] for _, k in ADAY])

# ------------------------------------------------------------------ grafik
fig, ax = plt.subplots(1, 3, figsize=(16.4, 5.6), facecolor='#121212')
for a in ax:
    a.set_facecolor('#121212'); a.grid(alpha=.13)

a = ax[0]
yy = np.arange(len(SIRA_Y))[::-1]
cl = ['#16a34a' if s[0] > ESIK_Y else '#52525b' for s in SIRA_Y]
a.barh(yy, [s[0] for s in SIRA_Y], .62, color=cl)
a.axvline(ESIK_Y, color='#f87171', ls='--', lw=2,
          label=('başka-yere-bakma eşiği %.3f' % ESIK_Y).replace('.', ','))
for i, s in enumerate(SIRA_Y):
    a.text(.02, yy[i], s[1], va='center', ha='left', fontsize=8.2,
           color='#0a0a0a' if s[0] > ESIK_Y else '#d4d4d8', zorder=6)
a.set_yticks([])
a.set_xlabel('|Spearman|', fontsize=10.5)
a.set_xlim(0, max(max(s[0] for s in SIRA_Y), ESIK_Y) * 1.15)
a.set_title('YOĞUN REJİM · n=%d galaksi' % len(ADS_Y), fontsize=12, color='white', pad=8)
a.legend(fontsize=8.6, framealpha=.3, loc='lower right')

a = ax[1]
yy = np.arange(len(SIRA_T))[::-1]
cl = ['#16a34a' if s[0] > ESIK_T else '#52525b' for s in SIRA_T]
a.barh(yy, [s[0] for s in SIRA_T], .62, color=cl)
a.axvline(ESIK_T, color='#f87171', ls='--', lw=2,
          label=('eşik %.3f' % ESIK_T).replace('.', ','))
for i, s in enumerate(SIRA_T):
    a.text(.02, yy[i], s[1], va='center', ha='left', fontsize=8.2,
           color='#0a0a0a' if s[0] > ESIK_T else '#d4d4d8', zorder=6)
a.set_yticks([])
a.set_xlabel('|Spearman|', fontsize=10.5)
a.set_xlim(0, max(max(s[0] for s in SIRA_T), ESIK_T) * 1.15)
a.set_title('BÜTÜN EĞRİ · n=%d galaksi' % len(ADS_T), fontsize=12, color='white', pad=8)
a.legend(fontsize=8.6, framealpha=.3, loc='lower right')

a = ax[2]
a.hist(BOS_Y, bins=40, color='#52525b', alpha=.85, label='boş dağılım (karıştırma)')
a.axvline(ESIK_Y, color='#f87171', ls='--', lw=2, label='%95 dilimi')
a.axvline(SIRA_Y[0][0], color='#16a34a', lw=2.4,
          label='en iyi: %s' % SIRA_Y[0][1])
a.set_xlabel('tesadüfi en iyi |Spearman|', fontsize=10.5)
a.set_ylabel('permütasyon', fontsize=10.5)
a.set_title('Başka-yere-bakma denetimi (%d permütasyon)' % len(BOS_Y),
            fontsize=12, color='white', pad=8)
a.legend(fontsize=8.6, framealpha=.3)

fig.suptitle('Galaksi başına açığı ne öngörüyor? — 14 değişken tarandı',
             fontsize=14.4, color='white', y=.975)
fig.text(.5, .035, 'Hedef: galaksi başına medyan $D/v_{öng}^2$. Varyansın %%68\'i galaksiler '
                   'arası ve galaksi başına değişen bütün bilinen adaylar elendi '
                   '($\\Upsilon_*$, mesafe, eğiklik).', ha='center', fontsize=9.4,
         color='#a1a1aa')
fig.text(.5, .008, 'Tarama olduğu için ham $p$ değeri yanıltıcıdır: 14 değişkende tesadüfi '
                   'en iyi |rho| permütasyonla ölçüldü ve eşik ondan alındı.',
         ha='center', fontsize=9.4, color='#fbbf24')
fig.subplots_adjust(left=.03, right=.988, top=.855, bottom=.185, wspace=.16)
plt.savefig(os.path.join(CIK, 'tarama.png'), dpi=140,
            facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print('\n-> 88_TARAMA/  SONUC.csv · tarama.png')
