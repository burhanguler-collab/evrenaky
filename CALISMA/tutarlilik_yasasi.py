"""85_TUTARLILIK_YASASI — sinif bandinin mekanizmasi araniyor (1 Agustos 2026).

Plan (kullanici onayi ile):
 1. Hedef: galaksi basina gereken a0 carpani k_i (dis yari, SAYISAL cozum).
 2. Aday degiskenler (SPARC katalog + rotmod'dan): yuzey yogunluklari, gaz kesri,
    Vflat, RHI/Rdisk, M_bar, ic yukselme dikligi, egri calkantisi, egri bicimi.
 3. Iki kanal ayrimi: hizalanma (yalniz F4 olceklenir) vs ortam/G (butun v^2).
    Ayirt edici: dis yariya oturtulan TEK sayi, egrinin ic/orta kismini hangi
    kanalda daha iyi duzeltiyor?
 4. Yasa denemesi: sinif medyanlari (8 grup) uzerinden en iyi aday ile
    log k = a + b X; yasa uygulaninca sinif bandi ne kadar daraliyor?

Cikti: SINIF_CALISMASI/85_TUTARLILIK_YASASI/{SONUC.csv, tutarlilik.png} + ekrana ozet.
"""
import os, sys, glob, csv, warnings
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
plt.style.use('dark_background')

KOK = os.path.dirname(os.path.abspath(__file__))
SC = os.path.join(KOK, 'SINIF_CALISMASI')
CIK = os.path.join(SC, '85_TUTARLILIK_YASASI')
os.makedirs(CIK, exist_ok=True)

G = 4.300917e-6
C_SI = 2.99792458e8
ACC = 1e6 / 3.0856776e19
CH0 = (C_SI * (70e3 / 3.0857e22)) / ACC
A0N = 1.75 * CH0 / 16.1              # nihai a0
RB = 1.4
UPS = 0.50

S0 = ['NGC4138', 'UGC02487', 'UGC06786']
BCD = ['NGC1705', 'NGC2915', 'NGC6789', 'PGC51017', 'UGCA281']

SINIFLAR = ['01_erken_spiral', '02_orta_spiral', '03_gec_spiral',
            '04_cok_gec_spiral', '05_macellan', '06_duzensiz']

def katalog(sinif):
    yol = os.path.join(SC, sinif, 'KATALOG.csv')
    return {r['Galaksi']: r for r in csv.DictReader(open(yol, encoding='utf-8'))}

def galaksi_yukle(sinif, ad, kat):
    f = os.path.join(SC, sinif, 'veri', ad + '_rotmod.dat')
    d = np.loadtxt(f)
    if d.ndim < 2 or len(d) < 5:
        return None
    R, Vo, eV, Vg, Vd, Vb, SBd, SBb = [d[:, i] for i in range(8)]
    eV = np.maximum(eV, 1.0)
    Rp = R * 1e3
    L = lambda S: np.concatenate([[0.0], np.cumsum(
        np.pi * (Rp[1:] ** 2 - Rp[:-1] ** 2) * 0.5 * (S[1:] + S[:-1]))])
    g = dict(g=ad, R=R, Vo=Vo, eV=eV, Vg=Vg, Vd=Vd, Vb=Vb,
             Ld=L(SBd), Lb=L(SBb), SBd0=SBd[0], N=len(R))
    k = kat.get(ad, {})
    def f_(anahtar):
        try:
            v = float(k.get(anahtar, 'nan'))
            return v if np.isfinite(v) and v > 0 else np.nan
        except Exception:
            return np.nan
    g['SBeff'] = f_('SBeff'); g['SBdisk'] = f_('SBdisk')
    g['Reff'] = f_('Reff_kpc'); g['Rdisk'] = f_('Rdisk_kpc')
    g['RHI'] = f_('RHI_kpc'); g['Vflat'] = f_('Vflat_kms')
    return g

Vbar2 = lambda d, Y: np.sign(d['Vg']) * d['Vg'] ** 2 + Y * d['Vd'] ** 2 + RB * Y * d['Vb'] ** 2
Mgas = lambda d: np.maximum(d['R'] * np.sign(d['Vg']) * d['Vg'] ** 2 / G, 0.0)
Mkaps = lambda d, Y: Y * d['Ld'] + RB * Y * d['Lb'] + Mgas(d)

def v_pred(d, k):
    M = np.maximum(Mkaps(d, UPS), 1e-9)
    return np.sqrt(np.maximum(Vbar2(d, UPS), 1e-9) + np.sqrt(k * A0N * G * M))

def dis_sapma(d, k):
    m = d['R'] > np.median(d['R'])
    vp = v_pred(d, k)
    return float(np.median((vp[m] - d['Vo'][m]) / d['Vo'][m]))

def k_coz(d):
    """dis yari sapmasini sifirlayan a0 carpani (ikiye bolme, log uzayda)."""
    lo, hi = -2.0, 2.0                     # k in [0.01, 100]
    flo, fhi = dis_sapma(d, 10 ** lo), dis_sapma(d, 10 ** hi)
    if flo > 0:  return 10 ** lo, 'tavan_alt'
    if fhi < 0:  return 10 ** hi, 'tavan_ust'
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        if dis_sapma(d, 10 ** mid) > 0: hi = mid
        else: lo = mid
    return 10 ** (0.5 * (lo + hi)), 'ok'

def olc_degiskenler(d):
    M = Mkaps(d, UPS); Mb = max(M[-1], 1e-6)
    mg = Mgas(d)[-1]
    Vmax = float(d['Vo'].max())
    # ic yukselme dikligi: Vo'nun 0.8 Vmax'a ulastigi ilk yaricap / son yaricap
    idx = np.argmax(d['Vo'] >= 0.8 * Vmax)
    diklik = float(d['R'][idx] / d['R'][-1])
    # calkanti: ardisiK farklarin medyani / Vmax
    calk = float(np.median(np.abs(np.diff(d['Vo']))) / Vmax)
    # bicim: ic (son/4 yaricapa en yakin nokta) hizinin son hiza orani
    j = int(np.argmin(np.abs(d['R'] - d['R'][-1] / 4.0)))
    biçim = float(d['Vo'][j] / d['Vo'][-1])
    # etkin yuzey kutle yogunlugu: Mb / (2 pi Reff^2)  (Msun/pc^2)
    sig_eff = Mb / (2 * np.pi * (d['Reff'] * 1e3) ** 2) if np.isfinite(d['Reff']) else np.nan
    return dict(
        logMbar=np.log10(Mb),
        gazkesri=mg / Mb,
        logVflat=np.log10(d['Vflat']) if np.isfinite(d['Vflat']) else np.log10(Vmax),
        logSBeff=np.log10(d['SBeff']) if np.isfinite(d['SBeff']) else np.nan,
        logSBdisk=np.log10(d['SBdisk']) if np.isfinite(d['SBdisk']) else np.nan,
        logSigEff=np.log10(sig_eff) if np.isfinite(sig_eff) else np.nan,
        logRHI_Rd=np.log10(d['RHI'] / d['Rdisk']) if np.isfinite(d['RHI']) and np.isfinite(d['Rdisk']) else np.nan,
        diklik=diklik, calkanti=calk, bicim=biçim)

def rms(d, vp):
    return float(np.sqrt(np.mean((vp - d['Vo']) ** 2)))

# ---------------- yukle ve olc ----------------
GRUP = {}   # grup adi -> galaksi kayitlari
for s in SINIFLAR:
    kat = katalog(s)
    GRUP[s] = []
    for f in sorted(glob.glob(os.path.join(SC, s, 'veri', '*_rotmod.dat'))):
        g = galaksi_yukle(s, os.path.basename(f)[:-11], kat)
        if g: GRUP[s].append(g)
kat99 = katalog('99_KARMASIK')
for grup, adlar in (('S0', S0), ('BCD', BCD)):
    GRUP[grup] = []
    for ad in adlar:
        g = galaksi_yukle('99_KARMASIK', ad, kat99)
        if g: GRUP[grup].append(g)

KAYIT = []
for grup, gal in GRUP.items():
    for d in gal:
        k, durum = k_coz(d)
        u_m = d['R'] > np.median(d['R'])
        vp1 = v_pred(d, 1.0)
        u = float(np.median((d['Vo'][u_m] / vp1[u_m]) ** 2))
        deg = olc_degiskenler(d)
        # kanal karsilastirmasi: ayni "dis yariya oturtulmus tek sayi" ile TUM egri RMS'i
        r_taban = rms(d, vp1)
        r_k = rms(d, v_pred(d, k))            # hizalanma kanali (yalniz F4)
        r_u = rms(d, np.sqrt(u) * vp1)        # ortam/G kanali (butun v^2)
        KAYIT.append(dict(grup=grup, g=d['g'], k=k, durum=durum, u=u,
                          rms_taban=r_taban, rms_k=r_k, rms_u=r_u, **deg))
print('%d galaksi olculdu (%d grup)' % (len(KAYIT), len(GRUP)))

# ---------------- sinif medyanlari ----------------
def med(grup, alan):
    v = [r[alan] for r in KAYIT if r['grup'] == grup and np.isfinite(r[alan])]
    return float(np.median(v)) if v else np.nan

GRUPLAR = SINIFLAR + ['S0', 'BCD']
ADAYLAR = ['logSBeff', 'logSBdisk', 'logSigEff', 'gazkesri', 'logVflat',
           'logRHI_Rd', 'logMbar', 'diklik', 'calkanti', 'bicim']

logk_med = {gr: np.log10(med(gr, 'k')) for gr in GRUPLAR}
print('\nSinif medyan carpanlari (nihai a0 cinsinden):')
for gr in GRUPLAR:
    print('  %-18s k=%.2f  (log %.3f)  n=%d' % (gr, 10**logk_med[gr], logk_med[gr],
          sum(1 for r in KAYIT if r['grup'] == gr)))
band0 = max(logk_med.values()) - min(logk_med.values())
std0 = float(np.std(list(logk_med.values())))
print('BAND (8 grup): genislik %.3f dex · std %.3f dex' % (band0, std0))

def spearman(x, y):
    x, y = np.asarray(x), np.asarray(y)
    m = np.isfinite(x) & np.isfinite(y)
    x, y = x[m], y[m]
    if len(x) < 4: return np.nan, 0
    rx = np.argsort(np.argsort(x)); ry = np.argsort(np.argsort(y))
    return float(np.corrcoef(rx, ry)[0, 1]), len(x)

print('\n--- SINIF DUZEYI tarama (8 nokta; ~anlamlilik |rho|>0.74) ---')
sonuc_sinif = []
for a in ADAYLAR:
    xs = [med(gr, a) for gr in GRUPLAR]
    ys = [logk_med[gr] for gr in GRUPLAR]
    rho, n = spearman(xs, ys)
    sonuc_sinif.append((a, rho, n))
    print('  %-11s rho=%+.3f (n=%d)' % (a, rho, n))

print('\n--- GALAKSI DUZEYI (gurultu beklenir; referans) ---')
for a in ADAYLAR:
    rho, n = spearman([r[a] for r in KAYIT], [np.log10(r['k']) for r in KAYIT])
    print('  %-11s rho=%+.3f (n=%d)' % (a, rho, n))

# ---------------- kanal ayrimi ----------------
print('\n--- KANAL AYRIMI: dis yariya oturtulan tek sayi, TUM egriyi hangi kanalda duzeltir? ---')
print('%-18s %8s %8s %8s  kazanan' % ('grup', 'taban', 'F4(k)', 'G(u)'))
kanal = []
for gr in GRUPLAR:
    t = med(gr, 'rms_taban'); rk = med(gr, 'rms_k'); ru = med(gr, 'rms_u')
    kz = 'F4' if rk < ru else 'G'
    kanal.append((gr, t, rk, ru, kz))
    print('%-18s %8.2f %8.2f %8.2f  %s' % (gr, t, rk, ru, kz))
oyF4 = sum(1 for r in KAYIT if r['rms_k'] < r['rms_u'])
print('galaksi bazinda: F4 kanali %d / %d galakside daha iyi' % (oyF4, len(KAYIT)))

# ---------------- yasa denemesi (en iyi aday) ----------------
gecerli = [(a, r) for a, r, n in sonuc_sinif if np.isfinite(r)]
en = max(gecerli, key=lambda t: abs(t[1]))
aday, rho_en = en
xs = np.array([med(gr, aday) for gr in GRUPLAR])
ys = np.array([logk_med[gr] for gr in GRUPLAR])
m = np.isfinite(xs) & np.isfinite(ys)
beta, alfa = np.polyfit(xs[m], ys[m], 1)
print('\n--- YASA DENEMESI: en iyi aday %s (rho=%+.2f) ---' % (aday, rho_en))
print('  log k = %.3f + %.3f * %s' % (alfa, beta, aday))
# yasayi GALAKSI duzeyinde uygula, kalan carpanin sinif bandina bak
logk_kalan = {}
for gr in GRUPLAR:
    v = [np.log10(r['k']) - (alfa + beta * r[aday]) for r in KAYIT
         if r['grup'] == gr and np.isfinite(r[aday]) and r['durum'] == 'ok']
    logk_kalan[gr] = float(np.median(v)) if v else np.nan
band1 = max(logk_kalan.values()) - min(logk_kalan.values())
std1 = float(np.std([v for v in logk_kalan.values() if np.isfinite(v)]))
print('  BAND once: %.3f dex (std %.3f) -> yasa sonrasi: %.3f dex (std %.3f)'
      % (band0, std0, band1, std1))

# ikinci en iyi ile iki degiskenli deneme
gecerli2 = sorted(gecerli, key=lambda t: -abs(t[1]))
aday2 = gecerli2[1][0] if len(gecerli2) > 1 else None
if aday2:
    X = np.array([[med(gr, aday), med(gr, aday2)] for gr in GRUPLAR])
    mm = np.all(np.isfinite(X), axis=1) & np.isfinite(ys)
    A = np.column_stack([np.ones(mm.sum()), X[mm]])
    kat2, *_ = np.linalg.lstsq(A, ys[mm], rcond=None)
    tah = A @ kat2
    kalan2 = ys[mm] - tah
    print('  iki degiskenli (%s + %s): sinif-medyan artigi std %.3f dex'
          % (aday, aday2, float(np.std(kalan2))))

# ---------------- SONUC.csv ----------------
with open(os.path.join(CIK, 'SONUC.csv'), 'w', encoding='utf-8', newline='') as fh:
    w = csv.writer(fh)
    alanlar = ['grup', 'g', 'k', 'durum', 'u', 'rms_taban', 'rms_k', 'rms_u'] + ADAYLAR
    w.writerow(alanlar)
    for r in KAYIT:
        w.writerow([('%.4g' % r[a]) if isinstance(r[a], float) else r[a] for a in alanlar])
print('\n-> SONUC.csv (%d satir)' % len(KAYIT))

# ---------------- grafik ----------------
fig, ax = plt.subplots(2, 2, figsize=(13.5, 10.5), facecolor='#121212')
for a_ in ax.flat:
    a_.set_facecolor('#141417')
    for sp in a_.spines.values(): sp.set_color('#3f3f46')
    a_.tick_params(colors='#a1a1aa', labelsize=9)

ISIM = {'01_erken_spiral':'Sa–Sab','02_orta_spiral':'Sb–Sbc','03_gec_spiral':'Sc–Scd',
        '04_cok_gec_spiral':'Sd','05_macellan':'Sdm–Sm','06_duzensiz':'Im','S0':'S0','BCD':'BCD'}
RENK = dict(zip(GRUPLAR, ['#f97316','#eab308','#22c55e','#06b6d4','#3b82f6','#a855f7','#f43f5e','#e11d48']))

# (1) en iyi aday vs log k — sinif medyanlari
a1 = ax[0, 0]
for gr in GRUPLAR:
    x, y = med(gr, aday), logk_med[gr]
    if np.isfinite(x):
        a1.scatter(x, y, s=90, color=RENK[gr], zorder=5)
        a1.annotate(ISIM[gr], (x, y), textcoords='offset points', xytext=(7, 4),
                    fontsize=9, color='#e5e5e5')
xx = np.linspace(np.nanmin(xs[m]), np.nanmax(xs[m]), 50)
a1.plot(xx, alfa + beta * xx, '--', color='#ffcc00', lw=1.4,
        label='log k = %.2f %+.2f x' % (alfa, beta))
a1.axhline(0, color='#52525b', lw=0.8)
a1.set_xlabel(aday, fontsize=10); a1.set_ylabel('log k (gereken a0 carpani)', fontsize=10)
a1.set_title('Sinif medyanlari: %s  (Spearman %+.2f)' % (aday, rho_en), fontsize=11, color='w')
a1.legend(fontsize=9, framealpha=0.15)

# (2) kanal ayrimi
a2 = ax[0, 1]
gg = np.arange(len(GRUPLAR)); wdt = 0.27
a2.bar(gg - wdt, [k[1] for k in kanal], wdt, color='#71717a', label='taban (k=1)')
a2.bar(gg,       [k[2] for k in kanal], wdt, color='#22c55e', label='F4 kanali (hizalanma)')
a2.bar(gg + wdt, [k[3] for k in kanal], wdt, color='#a78bfa', label='G kanali (butun v²)')
a2.set_xticks(gg); a2.set_xticklabels([ISIM[g] for g in GRUPLAR], rotation=30, fontsize=8.5)
a2.set_ylabel('medyan RMS (km/s)', fontsize=10)
a2.set_title('Dis yariya oturtulan TEK sayi tum egriyi hangi kanalda duzeltir?', fontsize=10.5, color='w')
a2.legend(fontsize=8.5, framealpha=0.15)

# (3) yasa oncesi/sonrasi band
a3 = ax[1, 0]
once = [logk_med[gr] for gr in GRUPLAR]
sonra = [logk_kalan[gr] for gr in GRUPLAR]
a3.bar(gg - 0.18, once, 0.34, color='#f97316', label='once (band %.3f dex)' % band0)
a3.bar(gg + 0.18, sonra, 0.34, color='#22c55e', label='yasa sonrasi (band %.3f dex)' % band1)
a3.axhline(0, color='#52525b', lw=0.8)
a3.set_xticks(gg); a3.set_xticklabels([ISIM[g] for g in GRUPLAR], rotation=30, fontsize=8.5)
a3.set_ylabel('log k', fontsize=10)
a3.set_title('Yasa denemesi: %s' % aday, fontsize=11, color='w')
a3.legend(fontsize=9, framealpha=0.15)

# (4) galaksi duzeyi sacilim
a4 = ax[1, 1]
for gr in GRUPLAR:
    xs_ = [r[aday] for r in KAYIT if r['grup'] == gr and r['durum'] == 'ok']
    ys_ = [np.log10(r['k']) for r in KAYIT if r['grup'] == gr and r['durum'] == 'ok']
    a4.scatter(xs_, ys_, s=22, color=RENK[gr], alpha=0.75, label=ISIM[gr])
a4.plot(xx, alfa + beta * xx, '--', color='#ffcc00', lw=1.4)
a4.axhline(0, color='#52525b', lw=0.8)
a4.set_xlabel(aday, fontsize=10); a4.set_ylabel('log k (galaksi)', fontsize=10)
a4.set_title('Galaksi duzeyi (gurultu beklenir)', fontsize=11, color='w')
a4.legend(fontsize=7.5, framealpha=0.15, ncol=2)

fig.suptitle('85_TUTARLILIK_YASASI — sinif bandinin mekanizma taramasi', fontsize=14, color='w')
fig.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(os.path.join(CIK, 'tutarlilik.png'), dpi=150, facecolor=fig.get_facecolor())
print('-> tutarlilik.png')
