"""KOD DOGRULAMA — bizim LCDM (NFW) fitimiz yayinlanmis fitlerle tutuyor mu?

Neden. Bu calismadaki LCDM tarafinin tamami BIZIM implementasyonumuzdur; hicbir
yayinlanmis sonucla karsilastirilmadi. Dolayisiyla butun karsilastirmalar
"kodumuz dogru" varsayimina dayaniyordu ve o varsayim denetlenmedi.

Referans. Li, Lelli, McGaugh, Pawlowski, Zwaan & Schombert — "The Halo Mass
Function of Late-Type Galaxies from HI Kinematics". SPARC sitesinden indirilen
WP50_M200.mrt, galaksi basina UC halo modeli icin fitlenmis halo kutlesi verir:
    log(M_NFW)  ± hata      NFW profili
    log(M_Ein)  ± hata      Einasto profili
    log(M_DC14) ± hata      DC14 (geri-besleme ile degistirilmis) profili
Hepsi R200'de tanimli (200 x kritik yogunluk) — bizim tanimimizla ayni.

Yontem (sinif calismasinin geri kalaniyla ayni).
  Bizim fitimiz : v^2 = V_bar^2(Y*) + v_NFW^2(R; M200, c200)
                  serbest: Y* (0,05-2,0) ve M200 ;  c200 <- Dutton & Maccio 2014,
                  sacilma YOK (tam dayatilmis)
  Karsilastirma : log10(M200_bizim) - log(M_NFW)_yayinlanmis, galaksi basina

Beklenen fark kaynaklari (sifir olmasi beklenmez):
  - Li ve ark. MCMC + onsel kullanir; biz en kucuk kareler, onsel yok
  - Onlar c-M iliskisini SACILMA ICINDE serbest birakir; biz tam dayattik
  - Onlar Y* icin lognormal onsel kullanir; biz duz sinir kullandik
  - Onlar uzaklik ve egiklik icin onsel kullanir; biz sabitledik
Dolayisiyla aranan sey SIFIR FARK degil, KORELASYONUN SIKI olmasidir. Sistematik
kayma yorumlanabilir; buyuk sacilma implementasyon hatasi anlamina gelir.

Cikti: SINIF_CALISMASI/98_KOD_DOGRULAMA/ -> SONUC.csv · YONTEM.md · dogrulama.png
"""

import os
import sys
import csv
import glob
import warnings

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

warnings.filterwarnings('ignore')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
plt.style.use('dark_background')

KOK = os.path.dirname(os.path.abspath(__file__))
VERI = os.path.join(KOK, 'veri')
CIK = os.path.join(KOK, 'SINIF_CALISMASI', '98_KOD_DOGRULAMA')
os.makedirs(CIK, exist_ok=True)

G = 4.300917e-6
RHO_CRIT = 3 * 0.07 ** 2 / (8 * np.pi * G)
H_RED, RB = 0.7, 1.4
YLO, YHI = 0.05, 2.0
TIPAD = {0: 'S0', 1: 'Sa', 2: 'Sab', 3: 'Sb', 4: 'Sbc', 5: 'Sc',
         6: 'Scd', 7: 'Sd', 8: 'Sdm', 9: 'Sm', 10: 'Im', 11: 'BCD'}


def mrt_oku(yol, alan):
    """Son '----' ayiracindan sonrasini belirtec (token) tabanli okur.
    Sabit genislik KULLANILMAZ: SPARC .mrt dosyalarinda baslik bir bayt kayabiliyor
    (bkz. ana katalogun T sutunu). Galaksi adlarinda bosluk yoktur."""
    ham = open(yol, encoding='utf-8', errors='replace').read().split('\n')
    a = [i for i, x in enumerate(ham) if x.startswith('----')][-1]
    D = {}
    for L in ham[a + 1:]:
        p = L.split()
        if len(p) < len(alan):
            continue
        try:
            D[p[0]] = {k: float(v) for k, v in zip(alan[1:], p[1:len(alan)])}
        except ValueError:
            continue
    return D


YAY = mrt_oku(os.path.join(VERI, '_WP50_M200.mrt'),
              ['Name', 'WP50', 'eWP50', 'lM_NFW', 'elM_NFW', 'lM_Ein', 'elM_Ein', 'lM_DC14', 'elM_DC14'])
KAT = mrt_oku(os.path.join(VERI, '_sparc.mrt'),
              ['Name', 'T', 'D', 'eD', 'fD', 'Inc', 'eInc', 'L36', 'eL36', 'Reff', 'SBeff',
               'Rdisk', 'SBdisk', 'MHI', 'RHI', 'Vflat', 'eVflat', 'Q'])
print('yayinlanmis tablo (Li ve ark.) : %d galaksi' % len(YAY))
print('ana katalog (Lelli ve ark.)    : %d galaksi' % len(KAT))


def c200_dm14(M):
    return 10 ** (0.905 - 0.101 * np.log10(M * H_RED / 1e12))


def v_nfw2(R, M200):
    cc = c200_dm14(M200)
    r200 = (3 * M200 / (4 * np.pi * 200 * RHO_CRIT)) ** (1 / 3.)
    rs = r200 / cc
    mu = lambda x: np.log(1 + x) - x / (1 + x)
    return G * M200 / R * mu(R / rs) / mu(cc)


S = []
for f in sorted(glob.glob(os.path.join(VERI, '*_rotmod.dat'))):
    ad = os.path.basename(f)[:-11]
    if ad not in YAY or ad not in KAT:
        continue
    d = np.loadtxt(f)
    if d.ndim < 2 or len(d) < 6:
        continue
    R, Vo, eV, Vg, Vd, Vb, SBd, SBb = [d[:, i] for i in range(8)]
    eV = np.maximum(eV, 1.0)
    if np.any(R <= 0) or Vo.max() <= 0:
        continue
    V2 = lambda Y: np.sign(Vg) * Vg ** 2 + Y * Vd ** 2 + RB * Y * Vb ** 2
    g = lambda r, Y, lg: np.sqrt(np.maximum(V2(Y), 1e-9) + v_nfw2(r, 10 ** lg))
    try:
        p, _ = curve_fit(g, R, Vo, sigma=eV, p0=[0.5, 11.0], bounds=([YLO, 7.], [YHI, 13.5]), maxfev=600000)
    except Exception:
        continue
    mv = g(R, *p)
    if not np.all(np.isfinite(mv)):
        continue
    c2 = float(np.sum(((mv - Vo) / eV) ** 2))
    S.append(dict(ad=ad, T=int(KAT[ad]['T']), Q=int(KAT[ad]['Q']), N=len(R),
                  Vmax=float(Vo.max()), Ys=float(p[0]), lM=float(p[1]),
                  ci=c2 / max(len(R) - 2, 1), rms=float(np.sqrt(np.mean((mv - Vo) ** 2))),
                  yNFW=YAY[ad]['lM_NFW'], eyNFW=YAY[ad]['elM_NFW'],
                  yEin=YAY[ad]['lM_Ein'], yDC14=YAY[ad]['lM_DC14']))
print('eslesen ve fitlenen             : %d galaksi' % len(S))

lb = np.array([s['lM'] for s in S])
ly = np.array([s['yNFW'] for s in S])
ey = np.array([s['eyNFW'] for s in S])
d = lb - ly
sap = d
z = d / np.maximum(ey, 1e-3)

print('\n' + '=' * 82)
print('BIZIM log M200  vs  YAYINLANMIS log M_NFW   (dex)')
print('  medyan fark            : %+.3f dex  (= x%.2f)' % (np.median(d), 10 ** np.median(d)))
print('  ortalama fark          : %+.3f dex' % np.mean(d))
print('  sacilma (std)          : %.3f dex' % np.std(d))
print('  ortanca mutlak sapma   : %.3f dex' % np.median(np.abs(d - np.median(d))))
print('  Pearson r (log-log)    : %+.4f' % np.corrcoef(lb, ly)[0, 1])
print('  |fark| < 0,3 dex olan  : %d/%d  (%%%.0f)' % (int((np.abs(d) < .3).sum()), len(d), 100 * np.mean(np.abs(d) < .3)))
print('  |fark| < 0,5 dex olan  : %d/%d  (%%%.0f)' % (int((np.abs(d) < .5).sum()), len(d), 100 * np.mean(np.abs(d) < .5)))
print('  |fark| > 1,0 dex olan  : %d/%d' % (int((np.abs(d) > 1.).sum()), len(d)))
print('  yayinlanmis hataya gore: medyan |z| = %.1f sigma' % np.median(np.abs(z)))
kot = sorted(S, key=lambda s: -abs(s['lM'] - s['yNFW']))[:6]
print('  en buyuk 6 sapma       : %s' % ', '.join('%s(%+.2f)' % (s['ad'], s['lM'] - s['yNFW']) for s in kot))

print('\n' + '=' * 82)
print('HALO MODELI SECIMI NE KADAR ONEMLI?  (yayinlanmis uc modelin kendi arasi)')
yE = np.array([s['yEin'] for s in S]); yD = np.array([s['yDC14'] for s in S])
print('  NFW vs Einasto : medyan %+.3f dex, sacilma %.3f' % (np.median(ly - yE), np.std(ly - yE)))
print('  NFW vs DC14    : medyan %+.3f dex, sacilma %.3f' % (np.median(ly - yD), np.std(ly - yD)))
print('  -> yayinlanmis modeller kendi arasinda bu kadar oynuyor; bizim %.2f dex\'lik'
      % np.median(np.abs(d)))
print('     medyan mutlak farkimiz bu baglamda okunmalidir.')

# ---------------- SONUC.csv ----------------
with open(os.path.join(CIK, 'SONUC.csv'), 'w', encoding='utf-8', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['Galaksi', 'Tip', 'Q', 'N', 'Vmax_kms', 'BIZIM_logM200', 'BIZIM_Ystar',
                'BIZIM_chi2ind', 'BIZIM_rms', 'YAY_logM_NFW', 'YAY_hata', 'FARK_dex',
                'FARK_sigma', 'YAY_logM_Einasto', 'YAY_logM_DC14'])
    for s in sorted(S, key=lambda x: -x['Vmax']):
        w.writerow([s['ad'], TIPAD.get(s['T'], s['T']), s['Q'], s['N'], '%.1f' % s['Vmax'],
                    '%.3f' % s['lM'], '%.3f' % s['Ys'], '%.3f' % s['ci'], '%.2f' % s['rms'],
                    '%.2f' % s['yNFW'], '%.2f' % s['eyNFW'], '%+.3f' % (s['lM'] - s['yNFW']),
                    '%+.1f' % ((s['lM'] - s['yNFW']) / max(s['eyNFW'], 1e-3)),
                    '%.2f' % s['yEin'], '%.2f' % s['yDC14']])

# ---------------- grafik ----------------
fig, (a1, a2) = plt.subplots(1, 2, figsize=(14.6, 6.4), facecolor='#121212')
a1.set_facecolor('#121212')
lim = [min(lb.min(), ly.min()) - .3, max(lb.max(), ly.max()) + .3]
a1.plot(lim, lim, '--', color='#71717a', lw=1.2, zorder=2)
for dd, c in [(.3, '#3f3f46'), (.5, '#2a2a30')]:
    a1.fill_between(lim, [x - dd for x in lim], [x + dd for x in lim], color=c, alpha=.45, zorder=1)
sc = a1.scatter(ly, lb, c=[s['Vmax'] for s in S], cmap='viridis', s=42, zorder=5,
                edgecolors='#0d0d0f', linewidths=.5)
a1.errorbar(ly, lb, xerr=ey, fmt='none', ecolor='#52525b', elinewidth=.7, zorder=3)
cb = fig.colorbar(sc, ax=a1, pad=.02, fraction=.045)
cb.set_label('$V_{max}$ (km/s)', fontsize=9.5)
a1.set_xlim(lim); a1.set_ylim(lim)
a1.set_xlabel('YAYINLANMIŞ  $\\log M_{NFW}$   (Li ve ark.)', fontsize=11)
a1.set_ylabel('BİZİM  $\\log M_{200}$', fontsize=11)
a1.set_title('Galaksi başına karşılaştırma\ngri bantlar: $\\pm0{,}3$ ve $\\pm0{,}5$ dex',
             fontsize=12, color='white', pad=9)
a1.grid(alpha=.13)
a1.text(.03, .97, 'medyan fark %+.2f dex\nsaçılma %.2f dex\n$r=%+.3f$\n$|{\\rm fark}|<0{,}5$: %%%.0f'
        % (np.median(d), np.std(d), np.corrcoef(lb, ly)[0, 1], 100 * np.mean(np.abs(d) < .5)),
        transform=a1.transAxes, va='top', fontsize=9.6, color='#4ade80', family='monospace')

a2.set_facecolor('#121212')
a2.axvline(0, color='#cccccc', lw=1.2, zorder=5)
a2.hist(d, bins=np.linspace(-1.6, 1.6, 33), color='#a78bfa', alpha=.9, zorder=4)
a2.axvline(np.median(d), color='#ffcc00', ls='--', lw=1.6, zorder=6)
a2.axvspan(-.3, .3, color='#4ade80', alpha=.13, zorder=1)
yl = a2.get_ylim()[1]
a2.text(np.median(d) + .05, yl * .93, 'medyan %+.2f' % np.median(d), color='#ffcc00', fontsize=10)
a2.text(0, yl * .99, '$\\pm0{,}3$ dex', color='#4ade80', fontsize=9.4, ha='center', va='top')
a2.set_xlabel('BİZİM $-$ YAYINLANMIŞ   ($\\log M_{200}$, dex)', fontsize=11)
a2.set_ylabel('Galaksi sayısı', fontsize=11)
a2.set_title('Fark dağılımı', fontsize=12, color='white', pad=9)
a2.grid(alpha=.13, axis='y')

fig.suptitle('Kod Doğrulama: ΛCDM Tarafımız Yayınlanmış SPARC Fitleriyle Tutuyor mu? (%d galaksi)'
             % len(S), fontsize=13.8, color='white', y=.985)
fig.text(.5, .042, 'Referans: Li, Lelli, McGaugh, Pawlowski, Zwaan & Schombert — SPARC `WP50_M200.mrt`. '
                   'Sıfır fark beklenmez: onlar MCMC $+$ önsel kullanır, $c$–$M$ saçılmasını serbest '
                   'bırakır, $D$ ve $i$ için önsel koyar.', ha='center', fontsize=9.2, color='#a1a1aa')
fig.text(.5, .012, 'Aranan şey korelasyonun sıkı olmasıdır; sistematik kayma yorumlanabilir, '
                   'büyük saçılma implementasyon hatası anlamına gelir.',
         ha='center', fontsize=9.2, color='#a1a1aa')
plt.tight_layout(rect=[0, .072, 1, .955])
plt.savefig(os.path.join(CIK, 'dogrulama.png'), dpi=150, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print('\n-> 98_KOD_DOGRULAMA/  SONUC.csv · dogrulama.png')
