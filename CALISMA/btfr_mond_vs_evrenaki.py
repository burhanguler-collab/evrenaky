import os
import sys
import numpy as np
import warnings
import glob

warnings.filterwarnings('ignore')

KOK = os.path.dirname(os.path.abspath(__file__))
VERI = os.path.join(KOK, 'veri')

G = 4.300917e-6
ACC = 1e6 / 3.0856776e19
A0_EVR = 7.39e-11 / ACC
A0_MOND = 1.20e-10 / ACC
RB, UPS = 1.4, 0.50

def mrt(yol, alan):
    ham = open(yol, encoding='utf-8', errors='replace').read().split('\n')
    a = [i for i, x in enumerate(ham) if x.startswith('----')][-1]
    D = {}
    for L in ham[a + 1:]:
        p = L.split()
        if len(p) < len(alan): continue
        try:
            D[p[0]] = {k: float(v) for k, v in zip(alan[1:], p[1:len(alan)])}
        except ValueError:
            continue
    return D

B = mrt(os.path.join(VERI, '_BTFR_Lelli2019.mrt'),
        ['Name', 'lMb', 'elMb', 'Inc', 'eInc', 'Vf', 'eVf'])

ROT = {}
for f in sorted(glob.glob(os.path.join(VERI, '*_rotmod.dat'))):
    ad = os.path.basename(f)[:-11]
    d = np.loadtxt(f)
    if d.ndim < 2 or len(d) < 6: continue
    R, Vo, eV, Vg, Vd, Vb, SBd, SBb = [d[:, i] for i in range(8)]
    if np.any(R <= 0): continue
    ROT[ad] = dict(R=R, Vb2=np.sign(Vg) * Vg ** 2 + UPS * Vd ** 2 + RB * UPS * Vb ** 2)

AD = [n for n in B if B[n]['Vf'] > 0 and n in ROT]
Mb = np.array([10 ** B[n]['lMb'] for n in AD])
lMb = np.log10(Mb)
Vf = np.array([B[n]['Vf'] for n in AD])
elMb = np.array([B[n]['elMb'] for n in AD])
Rout = np.array([ROT[n]['R'][-1] for n in AD])
Vbar2out = np.array([max(ROT[n]['Vb2'][-1], 0.0) for n in AD])

# Evrenaki (Kurulum B: Tam)
F4 = np.sqrt(G * Mb * A0_EVR)
v_evr = np.sqrt(Vbar2out + F4)

# MOND (Radyal Ivme Interpolasyonu)
gbar = np.maximum(Vbar2out / Rout, 1e-12)
g_mond = gbar / (1.0 - np.exp(-np.sqrt(gbar / A0_MOND)))
v_mond = np.sqrt(g_mond * Rout)

eg_g = np.polyfit(np.log10(Vf), lMb, 1)[0]
eg_evr = np.polyfit(np.log10(v_evr), lMb, 1)[0]
eg_mond = np.polyfit(np.log10(v_mond), lMb, 1)[0]

print("BTFR SINAVI KARSILASTIRMASI (MOND vs EVRENAKI)")
print("="*60)
print(f"Galaksi Sayisi: {len(AD)}")
print(f"Gozlenen Egim (Vf, agirliksiz): {eg_g:.3f}")
print(f"Evrenaki (Tam Kurulum) Egimi  : {eg_evr:.3f}")
print(f"MOND (Interpolasyon) Egimi    : {eg_mond:.3f}")
print("="*60)
print(f"Evrenaki Medyan Sapma (v_ong/v_olc): {np.median(v_evr / Vf):.3f}")
print(f"MOND Medyan Sapma     (v_ong/v_olc): {np.median(v_mond / Vf):.3f}")

w = 1 / np.maximum(elMb, .02) ** 2
A = np.vstack([np.log10(Vf), np.ones_like(Vf)]).T
eg_ga, _ = np.linalg.solve(A.T @ np.diag(w) @ A, A.T @ np.diag(w) @ lMb)
print(f"Gozlenen Egim (Agirlikli)          : {eg_ga:.3f}")
