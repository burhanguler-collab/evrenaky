"""SIGMA SINAVI v2 — genisletilmis esleme (1 Agustos 2026).

Ongoru (LAMBDA_TURETIM.md): k (dolayisiyla lambda), diskin dinamik soguklugu
v/sigma ile ARTMALI (Spearman > 0).

v2 genisletmesi:
  - Uc kaynak: Ianjamasimanana+2012 (THINGS super-profil sigma_dar; birincil),
    Stilp+2013 (superprofil sigma_central; VLA-ANGST/THINGS), Iorio+2017 (LT medyan).
  - Kaynaklar ortak galaksilerle I12 olcegine UYUMLANIR (Stilp x0.81, Iorio x0.67 —
    ortusen galaksilerin medyan orani; kayitli).
  - 99_KARMASIK uyeleri dahil (bayrakli: dusuk veri kalitesi) — k dogrudan cozulur.
  - Kipler: TUM (n~19) · yalniz-I12 · temiz (99 haric) · sinif-medyani.

Cikti: 85_TUTARLILIK_YASASI/{VSIGMA.csv, vsigma.png} + ekrana ozet.
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

# --- sigma tablosu: (deger_kms, kaynak) --------------------------------------
# I12 = Ianjamasimanana+2012 Tablo 1 sigma_dar · S13 = Stilp+2013 Tablo 4 sigma_central
# Io17 = Iorio+2017 Tablo 2 medyan. Uyumlama: S13 x0.81, Io17 x0.67 (ortusme medyani).
SIGMA = {
  'NGC2403': (6.6, 'I12'), 'NGC2841': (10.4, 'I12'), 'NGC2903': (8.8, 'I12'),
  'NGC2976': (8.4, 'I12'), 'NGC3198': (8.8, 'I12'),  'NGC3521': (12.4, 'I12'),
  'NGC5055': (8.3, 'I12'), 'NGC6946': (6.1, 'I12'),  'NGC7331': (11.5, 'I12'),
  'NGC7793': (6.6, 'I12'), 'IC2574':  (5.9, 'I12'),  'DDO154':  (6.0, 'I12'),
  'NGC4214': (4.5, 'I12'), 'UGC04305': (5.2, 'I12'), 'NGC2366': (7.9, 'I12'),
  'NGC1705': (7.4 * 0.81, 'S13u'), 'UGC04483': (8.4 * 0.81, 'S13u'),
  'DDO168': (8.8 * 0.67, 'Io17u'), 'UGC07559': (9.1 * 0.67, 'Io17u'),
}
DOSYA99 = {'NGC4214', 'UGC04305', 'NGC2366', 'NGC1705', 'UGCA281', 'D512-2'}

def rotmod_bul(ad):
    for kls in ['01_erken_spiral', '02_orta_spiral', '03_gec_spiral', '04_cok_gec_spiral',
                '05_macellan', '06_duzensiz', '99_KARMASIK']:
        f = os.path.join(SC, kls, 'veri', ad + '_rotmod.dat')
        if os.path.exists(f): return f, kls
    return None, None

def yukle(ad):
    f, kls = rotmod_bul(ad)
    if not f: return None
    d = np.loadtxt(f)
    if d.ndim < 2 or len(d) < 5: return None
    R, Vo, eV, Vg, Vd, Vb = [d[:, i] for i in range(6)]
    SBd, SBb = d[:, 6], d[:, 7]
    Rp = R * 1e3
    L = lambda S: np.concatenate([[0.0], np.cumsum(
        np.pi * (Rp[1:] ** 2 - Rp[:-1] ** 2) * 0.5 * (S[1:] + S[:-1]))])
    return dict(g=ad, kls=kls, R=R, Vo=Vo, Vg=Vg, Vd=Vd, Vb=Vb, Ld=L(SBd), Lb=L(SBb))

Vbar2 = lambda d: np.sign(d['Vg']) * d['Vg'] ** 2 + UPS * d['Vd'] ** 2 + RB * UPS * d['Vb'] ** 2
Mgas = lambda d: np.maximum(d['R'] * np.sign(d['Vg']) * d['Vg'] ** 2 / G, 0.0)
Mkaps = lambda d: UPS * d['Ld'] + RB * UPS * d['Lb'] + Mgas(d)

def v_pred(d, k):
    M = np.maximum(Mkaps(d), 1e-9)
    return np.sqrt(np.maximum(Vbar2(d), 1e-9) + np.sqrt(k * A0N * G * M))

def k_coz(d):
    dis = lambda k: float(np.median(((v_pred(d, k) - d['Vo']) / d['Vo'])[d['R'] > np.median(d['R'])]))
    lo, hi = -2.0, 2.0
    if dis(10 ** lo) > 0: return 10 ** lo, 'tavan'
    if dis(10 ** hi) < 0: return 10 ** hi, 'tavan'
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        if dis(10 ** mid) > 0: hi = mid
        else: lo = mid
    return 10 ** (0.5 * (lo + hi)), 'ok'

KAYIT = []
for ad, (sig, kay) in SIGMA.items():
    d = yukle(ad)
    if d is None:
        print('! rotmod yok:', ad); continue
    k, durum = k_coz(d)
    if durum != 'ok':
        print('! k cozulemedi:', ad); continue
    V = float(np.median(d['Vo'][d['R'] > np.median(d['R'])]))
    KAYIT.append(dict(g=ad, kls=d['kls'], k=k, V=V, sig=sig, kay=kay,
                      vs=V / sig, temiz=ad not in DOSYA99))
print('%d galaksi eslesti (temiz %d + denetim %d)'
      % (len(KAYIT), sum(r['temiz'] for r in KAYIT), sum(not r['temiz'] for r in KAYIT)))

def spearman(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y); x, y = x[m], y[m]
    if len(x) < 4: return np.nan, 0
    rx = np.argsort(np.argsort(x)); ry = np.argsort(np.argsort(y))
    return float(np.corrcoef(rx, ry)[0, 1]), len(x)

def perm_p(x, y, n=20000):
    x, y = np.asarray(x, float), np.asarray(y, float)
    r0, _ = spearman(x, y)
    rng = np.random.default_rng(42); say = 0
    for _ in range(n):
        r, _ = spearman(x, rng.permutation(y))
        if r >= r0: say += 1
    return r0, say / n

print('\n%-10s %-18s %6s %6s %5s %7s %6s' % ('galaksi', 'sinif', 'k', 'V_dis', 'sig', 'v/sig', 'kay'))
for r in sorted(KAYIT, key=lambda t: t['vs']):
    isaret = '' if r['temiz'] else '  (99)'
    print('%-10s %-18s %6.2f %6.0f %5.1f %7.1f %6s%s'
          % (r['g'], r['kls'], r['k'], r['V'], r['sig'], r['vs'], r['kay'], isaret))

print('\n--- SINAV: Spearman[log k, log v/sigma] (ongoru: POZITIF) ---')
for etiket, alt in [('TUM', KAYIT),
                    ('yalniz I12', [r for r in KAYIT if r['kay'] == 'I12']),
                    ('temiz (99 haric)', [r for r in KAYIT if r['temiz']])]:
    r0, p = perm_p([np.log10(r['vs']) for r in alt], [np.log10(r['k']) for r in alt])
    print('  %-18s rho=%+.3f  (tek yonlu perm p=%.3f, n=%d)' % (etiket, r0, p, len(alt)))

# sinif-medyani kipi
print('\n--- SINIF-MEDYANI kipi ---')
grup = {}
for r in KAYIT:
    anah = 'BCD' if r['g'] == 'NGC1705' else r['kls']
    grup.setdefault(anah, []).append(r)
gx, gy, gad = [], [], []
for anah, üye in sorted(grup.items()):
    if anah == '99_KARMASIK':   # sinifi belirsiz denetim uyeleri medyana girmez
        continue
    gx.append(np.median([np.log10(r['vs']) for r in üye]))
    gy.append(np.median([np.log10(r['k']) for r in üye]))
    gad.append('%s(n=%d)' % (anah, len(üye)))
r0, n0 = spearman(gx, gy)
print('  gruplar: %s' % ' · '.join(gad))
print('  Spearman = %+.3f (n=%d grup)' % (r0, n0))

with open(os.path.join(CIK, 'VSIGMA.csv'), 'w', encoding='utf-8', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['galaksi', 'sinif', 'k', 'V_dis_kms', 'sigma_I12esd', 'kaynak', 'v_sigma', 'temiz'])
    for r in KAYIT:
        w.writerow([r['g'], r['kls'], '%.3f' % r['k'], '%.1f' % r['V'],
                    '%.1f' % r['sig'], r['kay'], '%.2f' % r['vs'], int(r['temiz'])])
print('-> VSIGMA.csv')

fig, a = plt.subplots(figsize=(8.6, 6.4), facecolor='#121212')
a.set_facecolor('#141417')
for sp in a.spines.values(): sp.set_color('#3f3f46')
a.tick_params(colors='#a1a1aa', labelsize=9)
for r in KAYIT:
    renk = '#22c55e' if r['temiz'] else '#f97316'
    a.scatter(r['vs'], np.log10(r['k']), s=60, color=renk, zorder=5)
    a.annotate(r['g'], (r['vs'], np.log10(r['k'])), textcoords='offset points',
               xytext=(5, 4), fontsize=7.5, color='#a1a1aa')
a.axhline(0, color='#52525b', lw=0.8)
a.set_xscale('log')
a.set_xlabel('v / $\\sigma$ (I12 ölçeğine uyumlanmış)', fontsize=10)
a.set_ylabel('log k (gereken çarpan)', fontsize=10)
rT, pT = perm_p([np.log10(r['vs']) for r in KAYIT], [np.log10(r['k']) for r in KAYIT])
a.set_title('σ sınavı v2 — n=%d · Spearman %+.2f (p=%.2f) · yeşil: temiz, turuncu: denetim(99)'
            % (len(KAYIT), rT, pT), fontsize=10.5, color='w')
fig.tight_layout()
plt.savefig(os.path.join(CIK, 'vsigma.png'), dpi=150, facecolor=fig.get_facecolor())
print('-> vsigma.png')
