# -*- coding: utf-8 -*-
"""
VORTISITE TARAMASI — F4 beslemesinin tek-parametreli ailesi (87_ETKIN_YASA is 5)

Aile:  v_F4^2 = sqrt(G M_kaps a0) * f_geo^(alpha/2),   f_geo = V_bar^2 R / (G M_kaps)
  alpha=0  -> resmi B (skaler kutle)
  alpha=1  -> D (yerel g_bar; tam vortisite/geometri okumasi)
  ara alpha -> kismi hizalanma
Ek model E (oz-tutarli dolanim, F4'u TOPLAM akis besler):
  g = g_bar + sqrt(g a0)  ->  sqrt(g) = (sqrt(a0)+sqrt(a0+4 g_bar))/2
  (analitik: g >= a0 tabani dayatir — derin rejim verisiyle celismeli; olculur.)

ADALET: her alpha (ve E) icin a0, AYNI kriterle yeniden kalibre edilir
(141 galakside dis-yari goreli sapmanin MEDYANI = 0 — nihai a0'in kriteri).

Olcutler (hepsi kalibre a0 ile):
  1) genel medyan RMS
  2) RAR bicim egimi (rotmod noktalari, EKK)
  3) sinif bandi: sinif-medyani dis-yari sapmalarin yayilimi (max-min, yuzde puani)
"""
import os, sys, glob, warnings
import numpy as np

warnings.filterwarnings('ignore')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SK = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'SINIF_CALISMASI')
G = 4.300917e-6
ACC = 1e6 / 3.0856776e19
A0 = 1.75 * (2.99792458e8 * (70e3 / 3.0857e22)) / ACC / 16.1
RB, UPS = 1.4, 0.50
AD = {'01_erken_spiral': 'Sa-Sab', '02_orta_spiral': 'Sb-Sbc', '03_gec_spiral': 'Sc-Scd',
      '04_cok_gec_spiral': 'Sd', '05_macellan': 'Sdm-Sm', '06_duzensiz': 'Im'}

GAL = []
for sn in sorted(AD):
    for f in sorted(glob.glob(os.path.join(SK, sn, 'veri', '*_rotmod.dat'))):
        d = np.loadtxt(f)
        R, Vo, eV, Vg, Vd, Vb, SBd, SBb = [d[:, i] for i in range(8)]
        Rp = R * 1e3
        L = lambda S: np.concatenate([[0.], np.cumsum(
            np.pi * (Rp[1:] ** 2 - Rp[:-1] ** 2) * .5 * (S[1:] + S[:-1]))])
        vb2 = np.sign(Vg) * Vg ** 2 + UPS * Vd ** 2 + RB * UPS * Vb ** 2
        Mk = np.maximum(UPS * L(SBd) + RB * UPS * L(SBb)
                        + np.maximum(R * np.sign(Vg) * Vg ** 2 / G, 0.), 1e-6)
        GAL.append(dict(sn=sn, R=R, Vo=Vo, vb2=vb2, Mk=Mk))
print('%d galaksi   a0(SI)=%.3e' % (len(GAL), A0 * ACC))

def v2_alpha(g, al, k):
    B2 = k * A0 * G * g['Mk']                       # (km/s)^4
    fg = np.maximum(g['vb2'], 0.) * g['R'] / (G * g['Mk'])
    return g['vb2'] + np.sqrt(B2) * fg ** (al / 2.)

def v2_E(g, k):
    gb = np.maximum(g['vb2'], 0.) / g['R']
    a = k * A0
    sq = 0.5 * (np.sqrt(a) + np.sqrt(a + 4. * gb))
    return sq ** 2 * g['R']

def metrikler(v2f, k):
    rms, sap, sinif_sap = [], [], {}
    X, Y = [], []
    for g in GAL:
        v = np.sqrt(np.maximum(v2f(g, k), 1e-9))
        m = g['R'] > np.median(g['R'])
        rms.append(float(np.sqrt(np.mean((v - g['Vo']) ** 2))))
        s = 100 * float(np.mean((v[m] - g['Vo'][m]) / g['Vo'][m]))
        sap.append(s)
        sinif_sap.setdefault(g['sn'], []).append(s)
        iyi = (g['vb2'] > 0) & (g['Vo'] > 0)
        v2p = v2f(g, k)
        iyi &= v2p > 0
        X.extend(np.log10(g['vb2'][iyi] / g['R'][iyi] * ACC))
        Y.extend(np.log10(g['Vo'][iyi] ** 2 / g['R'][iyi]) - np.log10(v2p[iyi] / g['R'][iyi]))
    egim = float(np.polyfit(np.array(X), np.array(Y), 1)[0])
    smed = [float(np.median(v)) for v in sinif_sap.values()]
    return (float(np.median(rms)), float(np.median(sap)), egim,
            max(smed) - min(smed), smed)

def kalibre(v2f):
    a, b = 0.05, 20.
    med = lambda k: metrikler(v2f, k)[1]
    if med(a) > 0 or med(b) < 0:
        return np.nan
    for _ in range(50):
        m = np.sqrt(a * b)
        if med(m) < 0:
            a = m
        else:
            b = m
    return float(np.sqrt(a * b))

print('\n%6s %7s | %8s %9s %11s | %s' % ('alpha', 'k_kal', 'medRMS', 'RAR_egim', 'sinif_band', 'sinif medyan sapmalari (%)'))
sonuc = {}
for al in [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5]:
    f = lambda g, k, al=al: v2_alpha(g, al, k)
    kk = kalibre(f)
    r, s, e, band, smed = metrikler(f, kk)
    sonuc[al] = (kk, r, e, band)
    print('%6.2f %7.3f | %8.2f %+9.4f %10.1f%% | %s' % (
        al, kk, r, e, band, ' '.join('%+.1f' % x for x in smed)))

kk = kalibre(v2_E)
if np.isnan(kk):
    print('\nE (oz-tutarli): kalibre EDILEMEDI (medyan dis sapma hicbir k ile sifirlanmiyor)')
    r, s, e, band, smed = metrikler(v2_E, 1.0)
    print('  k=1 ile: medRMS %.2f  dis-sapma medyani %+.1f%%  (g>=a0 tabani — beklenen dislama)' % (r, s))
else:
    r, s, e, band, smed = metrikler(v2_E, kk)
    print('\nE (oz-tutarli, k=%.3f): medRMS %.2f  RAR egim %+.4f  band %.1f%%' % (kk, r, e, band))
    # taban denetimi: en dusuk gozlenen g_obs vs k*a0
    gmin = min(float(np.min(g['Vo'] ** 2 / g['R'])) for g in GAL) * ACC
    print('  taban denetimi: en dusuk g_obs = %.2e m/s^2  <->  model tabani k*a0 = %.2e' % (gmin, kk * A0 * ACC))
