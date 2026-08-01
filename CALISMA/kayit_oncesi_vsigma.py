"""KAYIT-ONCESI SINAV — lambda-sogukluk, n>~40 (1 Agustos 2026).

Recete: 85_TUTARLILIK_YASASI/KAYIT_ONCESI_PROTOKOL.md — bu betik receteyi
BIREBIR uygular; kip/esik/istatistik sonuca bakilarak degistirilmez.

sigma_est = (Wp20 - Wm50)/1.2334   (Lelli+2019 BTFR katalogu, diskte)
v         = dis-yari medyan Vo (rotmod)
k         = dis-yari sapmasini sifirlayan carpan (85 tanimi)
Birincil: 6 ana sinif. Istatistik: Spearman[log k, log(v/sigma_est)],
tek yonlu permutasyon p (20000, tohum 42). Karar: p<0.05.
Gecerlilik kapisi: 18 dogrudan-sigma galaksisinde Spearman >= 0.4.

Cikti: 85_TUTARLILIK_YASASI/{KAYIT_ONCESI.csv, kayit_oncesi.png} + ekrana rapor.
"""
import os, sys, csv, glob, warnings
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

G = 4.300917e-6
C_SI = 2.99792458e8
ACC = 1e6 / 3.0856776e19
A0N = 1.75 * (C_SI * (70e3 / 3.0857e22)) / ACC / 16.1
RB = 1.4
UPS = 0.50
SABIT = 2 * (np.sqrt(2 * np.log(5)) - np.sqrt(2 * np.log(2)))   # 1.2334

# --- Lelli+2019 W kolonlari ---------------------------------------------------
W = {}
with open(os.path.join(KOK, 'veri', '_BTFR_Lelli2019.mrt'), encoding='utf-8') as fh:
    veri_basladi = False
    for sat in fh:
        if not veri_basladi:
            if sat.strip().startswith('CamB'): veri_basladi = True
            else: continue
        if len(sat) < 108: continue
        ad = sat[0:12].strip()
        try:
            wp20 = float(sat[84:90]); wm50 = float(sat[96:102])
        except ValueError:
            continue
        W[ad] = (wp20, wm50)
print('katalogdan W okunan galaksi: %d' % len(W))

ANA = ['01_erken_spiral', '02_orta_spiral', '03_gec_spiral',
       '04_cok_gec_spiral', '05_macellan', '06_duzensiz']
S0B = {'NGC4138': 'S0', 'UGC02487': 'S0', 'UGC06786': 'S0',
       'NGC1705': 'BCD', 'NGC2915': 'BCD', 'PGC51017': 'BCD', 'UGCA281': 'BCD'}

def yukle(f):
    d = np.loadtxt(f)
    if d.ndim < 2 or len(d) < 5: return None
    R, Vo, eV, Vg, Vd, Vb = [d[:, i] for i in range(6)]
    SBd, SBb = d[:, 6], d[:, 7]
    Rp = R * 1e3
    L = lambda S: np.concatenate([[0.0], np.cumsum(
        np.pi * (Rp[1:] ** 2 - Rp[:-1] ** 2) * 0.5 * (S[1:] + S[:-1]))])
    return dict(R=R, Vo=Vo, Vg=Vg, Vd=Vd, Vb=Vb, Ld=L(SBd), Lb=L(SBb))

Vbar2 = lambda d: np.sign(d['Vg']) * d['Vg'] ** 2 + UPS * d['Vd'] ** 2 + RB * UPS * d['Vb'] ** 2
Mgas = lambda d: np.maximum(d['R'] * np.sign(d['Vg']) * d['Vg'] ** 2 / G, 0.0)
Mkaps = lambda d: UPS * d['Ld'] + RB * UPS * d['Lb'] + Mgas(d)

def v_pred(d, k):
    M = np.maximum(Mkaps(d), 1e-9)
    return np.sqrt(np.maximum(Vbar2(d), 1e-9) + np.sqrt(k * A0N * G * M))

def k_coz(d):
    dis = lambda k: float(np.median(((v_pred(d, k) - d['Vo']) / d['Vo'])[d['R'] > np.median(d['R'])]))
    lo, hi = -2.0, 2.0
    if dis(10 ** lo) > 0 or dis(10 ** hi) < 0: return None
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        if dis(10 ** mid) > 0: hi = mid
        else: lo = mid
    return 10 ** (0.5 * (lo + hi))

KAYIT = []
for kls in ANA + ['99_KARMASIK']:
    for f in sorted(glob.glob(os.path.join(SC, kls, 'veri', '*_rotmod.dat'))):
        ad = os.path.basename(f)[:-11]
        if kls == '99_KARMASIK' and ad not in S0B:      # ikincil yalniz uclar
            continue
        if ad not in W: continue
        wp20, wm50 = W[ad]
        if wp20 <= 0 or wm50 <= 0: continue
        fark = wp20 - wm50
        if fark < 5.0: continue                          # protokol esigi
        d = yukle(f)
        if d is None: continue
        k = k_coz(d)
        if k is None: continue
        sig = fark / SABIT
        v = float(np.median(d['Vo'][d['R'] > np.median(d['R'])]))
        KAYIT.append(dict(g=ad, kls=(S0B.get(ad, kls)), k=k, v=v, sig=sig,
                          vs=v / sig, birincil=kls in ANA))

bir = [r for r in KAYIT if r['birincil']]
iki = [r for r in KAYIT if not r['birincil']]
print('birincil (6 ana sinif): n=%d · ikincil (uclar): n=%d' % (len(bir), len(iki)))

def spearman(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y); x, y = x[m], y[m]
    if len(x) < 4: return np.nan, 0
    rx = np.argsort(np.argsort(x)); ry = np.argsort(np.argsort(y))
    return float(np.corrcoef(rx, ry)[0, 1]), len(x)

# --- GECERLILIK KAPISI: dogrudan-sigma ortusmesi -------------------------------
DOGRUDAN = {  # SIGMA_SINAVI v2'nin uyumlanmis degerleri
  'NGC2403': 6.6, 'NGC2841': 10.4, 'NGC2903': 8.8, 'NGC2976': 8.4, 'NGC3198': 8.8,
  'NGC3521': 12.4, 'NGC5055': 8.3, 'NGC6946': 6.1, 'NGC7331': 11.5, 'NGC7793': 6.6,
  'IC2574': 5.9, 'DDO154': 6.0, 'NGC4214': 4.5, 'UGC04305': 5.2, 'NGC2366': 7.9,
  'NGC1705': 5.99, 'UGC04483': 6.8, 'DDO168': 5.9, 'UGC07559': 6.1,
}
ox, oy, oad = [], [], []
for r in KAYIT:
    if r['g'] in DOGRUDAN:
        ox.append(r['sig']); oy.append(DOGRUDAN[r['g']]); oad.append(r['g'])
rG, nG = spearman(ox, oy)
print('\nGECERLILIK KAPISI: Spearman[sigma_est, sigma_dogrudan] = %+.3f (n=%d ortusme)' % (rG, nG))
print('  ortusenler:', ', '.join(oad))
KAPI = np.isfinite(rG) and rG >= 0.4 and nG >= 8
print('  kapi (>=0.4): %s' % ('GECTI' if KAPI else 'GECEMEDI -> sinav UYGULANAMAZ'))

def perm_p(x, y, n=20000):
    r0, _ = spearman(x, y)
    rng = np.random.default_rng(42); say = 0
    y = np.asarray(y, float)
    for _ in range(n):
        r, _ = spearman(x, rng.permutation(y))
        if r >= r0: say += 1
    return r0, say / n

if KAPI:
    r0, p = perm_p([np.log10(r['vs']) for r in bir], [np.log10(r['k']) for r in bir])
    print('\n=== KAYIT-ONCESI SONUC (birincil, tek istatistik) ===')
    print('  Spearman[log k, log v/sigma_est] = %+.3f · tek yonlu perm p = %.4f · n = %d' % (r0, p, len(bir)))
    print('  KARAR (esik p<0.05): %s' % ('DOGRULANDI (bu veri turunde)' if p < 0.05 else 'DESTEKLENMEDI'))
    if iki:
        r2, n2 = spearman([np.log10(r['vs']) for r in KAYIT], [np.log10(r['k']) for r in KAYIT])
        print('  (ikincil dahil, karara girmez: rho=%+.3f, n=%d)' % (r2, len(KAYIT)))

with open(os.path.join(CIK, 'KAYIT_ONCESI.csv'), 'w', encoding='utf-8', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['galaksi', 'sinif', 'k', 'v_dis_kms', 'sigma_est_kms', 'v_sigma', 'birincil'])
    for r in KAYIT:
        w.writerow([r['g'], r['kls'], '%.3f' % r['k'], '%.1f' % r['v'],
                    '%.2f' % r['sig'], '%.2f' % r['vs'], int(r['birincil'])])
print('\n-> KAYIT_ONCESI.csv (%d satir)' % len(KAYIT))

fig, ax = plt.subplots(1, 2, figsize=(12.8, 5.8), facecolor='#121212')
for a in ax:
    a.set_facecolor('#141417')
    for sp in a.spines.values(): sp.set_color('#3f3f46')
    a.tick_params(colors='#a1a1aa', labelsize=9)
a1, a2 = ax
a1.scatter(ox, oy, s=55, color='#eab308', zorder=5)
for x, y, t in zip(ox, oy, oad):
    a1.annotate(t, (x, y), textcoords='offset points', xytext=(5, 4), fontsize=7, color='#a1a1aa')
a1.set_xlabel('$\\sigma_{est}$ = (W20−W50)/1,233 (km/s)', fontsize=10)
a1.set_ylabel('$\\sigma$ doğrudan (km/s)', fontsize=10)
a1.set_title('Geçerlilik kapısı — Spearman %+.2f (n=%d)' % (rG, nG), fontsize=11, color='w')
RENK = {'01_erken_spiral':'#f97316','02_orta_spiral':'#eab308','03_gec_spiral':'#22c55e',
        '04_cok_gec_spiral':'#06b6d4','05_macellan':'#3b82f6','06_duzensiz':'#a855f7',
        'S0':'#f43f5e','BCD':'#e11d48'}
for r in KAYIT:
    a2.scatter(r['vs'], np.log10(r['k']), s=34, color=RENK.get(r['kls'], '#71717a'),
               alpha=0.9 if r['birincil'] else 0.55,
               marker='o' if r['birincil'] else 's', zorder=5)
a2.axhline(0, color='#52525b', lw=0.8)
a2.set_xscale('log')
a2.set_xlabel('v / $\\sigma_{est}$', fontsize=10)
a2.set_ylabel('log k', fontsize=10)
if KAPI:
    a2.set_title('Kayıt-öncesi sınav — birincil n=%d · Spearman %+.2f · p=%.4f'
                 % (len(bir), r0, p), fontsize=11, color='w')
fig.suptitle('λ–soğukluk: kayıt-öncesi doğrulama (σ: Lelli+2019 çizgi genişliklerinden)',
             fontsize=12.5, color='w')
fig.tight_layout(rect=[0, 0, 1, 0.93])
plt.savefig(os.path.join(CIK, 'kayit_oncesi.png'), dpi=150, facecolor=fig.get_facecolor())
print('-> kayit_oncesi.png')
