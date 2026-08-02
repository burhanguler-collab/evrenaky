# -*- coding: utf-8 -*-
"""
GRADYAN DENKLEMI DENEMESI (tartisma icin; KITABA ISLENMEDI — kullanici karari beklenir)

G1:  v^2 = V_bar^2 + sqrt(g_bar a0) R * W,   W = min(1, a0/g_bar),  g_bar = V_bar^2/R
Adil kalibrasyon: dis-yari medyan sapma = 0  ->  k ~ 0.935 (a0_G1 ~ 6.91e-11)

Zincir: (1) rotmod defteri + sinif tablosu, (2) BTFR v3 konvansiyonlari (Vf, 121),
(3) yuksek-z (Genzel, oz-uyumlu), (4) RAR.mrt. Karsilastirma: resmi P kayitlari.
"""
import os, sys, io, csv, glob, math, warnings
import numpy as np

warnings.filterwarnings('ignore')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
KOK = os.path.dirname(os.path.abspath(__file__))
SK = os.path.join(KOK, 'SINIF_CALISMASI')
G = 4.300917e-6
ACC = 1e6 / 3.0856776e19
A0N = 1.75 * (2.99792458e8 * (70e3 / 3.0857e22)) / ACC / 16.1
RB, UPS = 1.4, 0.50
AD = {'01_erken_spiral': 'Sa-Sab', '02_orta_spiral': 'Sb-Sbc', '03_gec_spiral': 'Sc-Scd',
      '04_cok_gec_spiral': 'Sd', '05_macellan': 'Sdm-Sm', '06_duzensiz': 'Im'}

GAL = []
for sn in sorted(AD):
    for f in sorted(glob.glob(os.path.join(SK, sn, 'veri', '*_rotmod.dat'))):
        d = np.loadtxt(f)
        R, Vo, eV, Vg, Vd, Vb, SBd, SBb = [d[:, i] for i in range(8)]
        vb2 = np.sign(Vg) * Vg ** 2 + UPS * Vd ** 2 + RB * UPS * Vb ** 2
        GAL.append(dict(sn=sn, ad=os.path.basename(f)[:-11], R=R, Vo=Vo, vb2=vb2))

def v2G1(g, k):
    R = g['R']; vb2 = g['vb2']
    gb = np.maximum(vb2, 0.) / R
    F4 = np.sqrt(k * A0N * gb) * R
    Wp = np.minimum(1., np.where(gb > 0, (k * A0N) / np.maximum(gb, 1e-12), 1.))
    return np.maximum(vb2 + F4 * Wp, 1e-9)

def defter(k):
    rms, sap, X, Y, Xw, Yw = [], [], [], [], [], []
    for g in GAL:
        v2 = v2G1(g, k); v = np.sqrt(v2)
        m = g['R'] > np.median(g['R'])
        rms.append(float(np.sqrt(np.mean((v - g['Vo']) ** 2))))
        sap.append(100 * float(np.mean((v[m] - g['Vo'][m]) / g['Vo'][m])))
        iyi = (g['vb2'] > 0) & (g['Vo'] > 0)
        x = np.log10(g['vb2'][iyi] / g['R'][iyi] * ACC)
        y = np.log10(g['Vo'][iyi] ** 2 / g['R'][iyi]) - np.log10(v2[iyi] / g['R'][iyi])
        X.extend(x); Y.extend(y)
        if iyi.sum() >= 4:
            Xw.extend(x - np.mean(x)); Yw.extend(y - np.mean(y))
    X, Y, Xw, Yw = map(np.array, (X, Y, Xw, Yw))
    return (float(np.median(rms)), float(np.median(sap)),
            float(np.polyfit(X, Y, 1)[0]), float(np.polyfit(Xw, Yw, 1)[0]))

a, b = 0.2, 5.
for _ in range(46):
    m = math.sqrt(a * b)
    if defter(m)[1] < 0:
        a = m
    else:
        b = m
KG = math.sqrt(a * b)
r, s, eg, ew = defter(KG)
print('G1 adil kalibrasyon: k=%.3f  ->  a0_G1 = %.3e m/s^2' % (KG, KG * A0N * ACC))
print('1) ROTMOD DEFTERI: medRMS %.2f · RAR egim %+.4f · galaksi-ici %+.4f' % (r, eg, ew))
print('   sinif tablosu:')
for sn in sorted(AD):
    gg = [g for g in GAL if g['sn'] == sn]
    print('   %-8s %6.2f' % (AD[sn],
          float(np.median([np.sqrt(np.mean((np.sqrt(v2G1(g, KG)) - g['Vo']) ** 2)) for g in gg]))))

# ---------------- 2) BTFR v3 konvansiyonlari ----------------
def mrt(y, al):
    h = open(y, encoding='utf-8', errors='replace').read().split('\n')
    a2 = [i for i, x in enumerate(h) if x.startswith('----')][-1]
    D = {}
    for Lx in h[a2 + 1:]:
        p = Lx.split()
        if len(p) < len(al):
            continue
        try:
            D[p[0]] = {kk: float(v) for kk, v in zip(al[1:], p[1:len(al)])}
        except ValueError:
            pass
    return D

B19 = mrt(os.path.join(KOK, 'veri', '_BTFR_Lelli2019.mrt'),
          ['Name', 'lMb', 'elMb', 'Inc', 'eInc', 'Vf', 'eVf', 'V2exp', 'eV2exp', 'V2eff',
           'eV2eff', 'Vmax', 'eVmax', 'Wp20', 'eWp20', 'Wm50', 'eWm50', 'Wm50c', 'eWm50c'])
IX = {g['ad']: g for g in GAL}
N = [n for n in B19 if B19[n]['Vf'] > 0 and n in IX]
lMb = np.array([B19[n]['lMb'] for n in N])
Vf = np.array([B19[n]['Vf'] for n in N])
Rout = np.array([IX[n]['R'][-1] for n in N])
vb2o = np.array([max(IX[n]['vb2'][-1], 0.) for n in N])
gbo = vb2o / Rout

def vtamG1(k):
    F4 = np.sqrt(k * A0N * gbo) * Rout
    Wp = np.minimum(1., (k * A0N) / np.maximum(gbo, 1e-12))
    return np.sqrt(vb2o + F4 * Wp)

v = vtamG1(KG)
d = np.log10(v / Vf)
egim = np.polyfit(np.log10(v), lMb, 1)[0]
fk = lambda kk: float(np.median(np.log10(vtamG1(kk) / Vf)))
a2, b2 = 1e-2, 1e2
for _ in range(80):
    mm = math.sqrt(a2 * b2)
    if fk(mm) < 0:
        a2 = mm
    else:
        b2 = mm
print('\n2) BTFR (v3 konv., n=%d, a0_G1 ile): egim %.3f · norm %.3f · gereken a0 x%.2f (a0_G1 tabaninda)'
      % (len(N), egim, 10 ** np.median(d), math.sqrt(a2 * b2) / KG))

# ---------------- 3) YUKSEK-Z ----------------
GZ = list(csv.DictReader((l for l in open(os.path.join(KOK, 'veri', '_genzel2017_tablo1.csv'),
                                          encoding='utf-8') if not l.startswith('#'))))
ic = 0; art = []
for gz in GZ:
    Rh = float(gz['R_half_kpc']); vc = float(gz['vc_kms'])
    fg = float(gz['fDM']); ust = gz['fDM_ust_sinir_mi'].strip() == 'evet'
    ustv = float(gz['fDM_ust']); alt = float(gz['fDM_alt'])
    a0u = KG * A0N
    ss = 0.9
    for _ in range(40):
        vbar2 = (ss * vc) ** 2
        gF1 = vbar2 / Rh
        Wp = min(1., a0u / max(gF1, 1e-12))
        vF42 = math.sqrt(max(vbar2, 1e-9) * a0u * Rh) * Wp
        ss = math.sqrt(max(vc ** 2 - vF42, 1e-9)) / vc
    fP = 1 - ss ** 2
    icinde = (fP <= ustv) if ust else (alt <= fP <= ustv)
    ic += int(icinde); art.append(fP - fg)
print('3) YUKSEK-Z: %d/6 bant ici · medyan artik %+.3f' % (ic, float(np.median(art))))

# ---------------- 4) RAR.mrt ----------------
gbar, gobs = [], []
for line in io.open(os.path.join(KOK, 'veri', '_RAR.mrt'), encoding='utf-8', errors='replace'):
    p = line.split()
    if len(p) == 4:
        try:
            gbar.append(float(p[0])); gobs.append(float(p[2]))
        except ValueError:
            pass
gbar = 10 ** np.array(gbar); gobs = np.array(gobs)
a0 = KG * A0N * ACC
W = np.minimum(1., a0 / gbar)
gpred = gbar + np.sqrt(gbar * a0) * W
artr = gobs - np.log10(gpred)
print('4) RAR.mrt (n=%d): medyan artik %+.4f · bicim egimi %+.4f'
      % (len(artr), float(np.median(artr)), float(np.polyfit(np.log10(gbar), artr, 1)[0])))
