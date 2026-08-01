"""Upsilon_* bant sinavi — NIHAI kurulumla yeniden olcum (1 Agustos 2026).

Kitabin 6.5.4.7 kayit (4)'u eski kurulumla (a0=cH0/16, v_F4^2=GM/l_om, k=1)
olculmustu. Bu betik AYNI sinavi nihai kurulumla tekrarlar:

  Evrenaki (k=1): v^2 = Vbar^2(Y) + sqrt(A0N G M_kaps(R,Y)),  yalniz Y serbest
  LCDM     (k=2): v^2 = Vbar^2(Y) + v_NFW^2(R; M200),         Y ve M200 serbest

Uc Y bandi: serbest (0,05-3,0) · populasyon sentezi (0,3-0,8) · dar (0,4-0,6).
Cikti: _HESAPLAR/upsilon_bant_nihai.csv + ekrana ozet.
"""
import os, sys, glob, csv, warnings
import numpy as np
from scipy.optimize import curve_fit

warnings.filterwarnings('ignore')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

KOK = os.path.dirname(os.path.abspath(__file__))
SC = os.path.join(KOK, 'SINIF_CALISMASI')
G = 4.300917e-6
C_SI = 2.99792458e8
ACC = 1e6 / 3.0856776e19
CH0 = (C_SI * (70e3 / 3.0857e22)) / ACC
A0N = 1.75 * CH0 / 16.1
RHO_CRIT = 3 * 0.07 ** 2 / (8 * np.pi * G)
H_RED = 0.7
RB = 1.4

def c200_dm14(M200):
    return 10 ** (0.905 - 0.101 * np.log10(M200 * H_RED / 1e12))

def v_nfw2(R, M200):
    cc = c200_dm14(M200)
    r200 = (3 * M200 / (4 * np.pi * 200 * RHO_CRIT)) ** (1 / 3.0)
    rs = r200 / cc
    mu = lambda x: np.log(1 + x) - x / (1 + x)
    return G * M200 / R * mu(R / rs) / mu(cc)

GAL = []
for sinif in ['01_erken_spiral', '02_orta_spiral', '03_gec_spiral',
              '04_cok_gec_spiral', '05_macellan', '06_duzensiz', '99_KARMASIK']:
    for f in sorted(glob.glob(os.path.join(SC, sinif, 'veri', '*_rotmod.dat'))):
        ad = os.path.basename(f)[:-11]
        d = np.loadtxt(f)
        if d.ndim < 2 or len(d) < 5:
            continue
        R, Vo, eV, Vg, Vd, Vb = [d[:, i] for i in range(6)]
        SBd, SBb = d[:, 6], d[:, 7]
        eV = np.maximum(eV, 1.0)
        Rp = R * 1e3
        L = lambda S: np.concatenate([[0.0], np.cumsum(
            np.pi * (Rp[1:] ** 2 - Rp[:-1] ** 2) * 0.5 * (S[1:] + S[:-1]))])
        GAL.append(dict(g=ad, R=R, Vo=Vo, eV=eV, Vg=Vg, Vd=Vd, Vb=Vb,
                        Ld=L(SBd), Lb=L(SBb), N=len(R)))
print('%d galaksi yuklendi' % len(GAL))

Vbar2 = lambda d, Y: np.sign(d['Vg']) * d['Vg'] ** 2 + Y * d['Vd'] ** 2 + RB * Y * d['Vb'] ** 2
Mgas = lambda d: np.maximum(d['R'] * np.sign(d['Vg']) * d['Vg'] ** 2 / G, 0.0)
Mkaps = lambda d, Y: Y * d['Ld'] + RB * Y * d['Lb'] + Mgas(d)

def fit_evr_k1(d, ylo, yhi):
    f = lambda R, Y, _d=d: np.sqrt(np.maximum(Vbar2(_d, Y), 1e-9)
                                   + np.sqrt(A0N * G * np.maximum(Mkaps(_d, Y), 1e-9)))
    try:
        p, _ = curve_fit(f, d['R'], d['Vo'], sigma=d['eV'],
                         p0=[min(max(0.5, ylo), yhi)], bounds=([ylo], [yhi]), maxfev=400000)
    except Exception:
        return None, None
    mv = f(d['R'], *p)
    ci = float(np.sum(((mv - d['Vo']) / d['eV']) ** 2) / max(d['N'] - 1, 1))
    return ci, float(p[0])

def fit_lcdm_k2(d, ylo, yhi):
    f = lambda R, Y, lg, _d=d: np.sqrt(np.maximum(Vbar2(_d, Y), 1e-9) + v_nfw2(R, 10 ** lg))
    try:
        p, _ = curve_fit(f, d['R'], d['Vo'], sigma=d['eV'],
                         p0=[min(max(0.5, ylo), yhi), 11.0],
                         bounds=([ylo, 7.0], [yhi, 13.5]), maxfev=400000)
    except Exception:
        return None, None
    mv = f(d['R'], *p)
    ci = float(np.sum(((mv - d['Vo']) / d['eV']) ** 2) / max(d['N'] - 2, 1))
    return ci, float(p[0])

BANT = [('serbest', 0.05, 3.0), ('pop.sentezi', 0.3, 0.8), ('dar', 0.4, 0.6)]
SON = {}
for ad, lo, hi in BANT:
    ev, lc, yv = [], [], []
    for d in GAL:
        ce, ye = fit_evr_k1(d, lo, hi)
        cl, _ = fit_lcdm_k2(d, lo, hi)
        if ce is not None:
            ev.append(ce); yv.append(ye)
        if cl is not None:
            lc.append(cl)
    SON[ad] = dict(evr=np.median(ev), lcdm=np.median(lc),
                   evr_ok=sum(1 for c in ev if c < 1), lcdm_ok=sum(1 for c in lc if c < 1),
                   n=len(ev), Y=np.array(yv))
    print('%-12s Evr(k=1) medyan %.2f  kabul %d/%d | LCDM(k=2) medyan %.2f  kabul %d/%d'
          % (ad, SON[ad]['evr'], SON[ad]['evr_ok'], SON[ad]['n'],
             SON[ad]['lcdm'], SON[ad]['lcdm_ok'], SON[ad]['n']))

Ys = SON['serbest']['Y']
disari = int(((Ys < 0.3) | (Ys > 0.8)).sum())
print('serbest fitte medyan Y* = %.3f ; bandin (0,3-0,8) disinda %d/%d (%%%.0f)'
      % (np.median(Ys), disari, len(Ys), 100.0 * disari / len(Ys)))
boz_e = SON['pop.sentezi']['evr'] / SON['serbest']['evr']
boz_l = SON['pop.sentezi']['lcdm'] / SON['serbest']['lcdm']
print('bant dayatilinca bozulma: Evrenaki %%%.0f  LCDM %%%.0f'
      % (100 * (boz_e - 1), 100 * (boz_l - 1)))

os.makedirs(os.path.join(KOK, '_HESAPLAR'), exist_ok=True)
with open(os.path.join(KOK, '_HESAPLAR', 'upsilon_bant_nihai.csv'), 'w',
          encoding='utf-8', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['bant', 'evr_medyan_chi2ind', 'evr_kabul', 'lcdm_medyan_chi2ind',
                'lcdm_kabul', 'n', 'medyan_Ystar_serbest', 'bant_disi'])
    for ad, lo, hi in BANT:
        s = SON[ad]
        w.writerow([ad, '%.3f' % s['evr'], s['evr_ok'], '%.3f' % s['lcdm'],
                    s['lcdm_ok'], s['n'],
                    '%.3f' % np.median(Ys) if ad == 'serbest' else '',
                    disari if ad == 'serbest' else ''])
print('-> _HESAPLAR/upsilon_bant_nihai.csv')
