# -*- coding: utf-8 -*-
"""
SOGUK KAYNAK SINAVI — F4'u yalniz hizalanabilir (soguk: disk+gaz) kutle besler mi?
(87_ETKIN_YASA is 6 — toplanma/besleme turetiminin sinamasi)

Turetim onerisi (lambda ilkesinin yerel uygulamasi; yeni parametre YOK):
  C : v^2 = V_bar^2(tum madde) + sqrt(G * M_kaps^{disk+gaz} * a0)
      (F1 skaler kanal — tum kutleyi gorur; F4 hizalanma kanali — kovan beslemez)
Karsilastirma:
  B : resmi (M_kaps tum madde)

Ongoruler: (i) yuksek-g fazla-itim kuculmeli (kovan bolgeleri), (ii) derin rejim degismemeli,
(iii) kovanli galaksilerde RMS iyilesmeli. Adalet: her model ayni kriterle kalibre.
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
        gaz = np.maximum(R * np.sign(Vg) * Vg ** 2 / G, 0.)
        Mk_tum = np.maximum(UPS * L(SBd) + RB * UPS * L(SBb) + gaz, 1e-6)
        Mk_sog = np.maximum(UPS * L(SBd) + gaz, 1e-6)
        GAL.append(dict(sn=sn, R=R, Vo=Vo, vb2=vb2, MkT=Mk_tum, MkS=Mk_sog,
                        kovanli=bool(np.any(Vb > 0))))
nk = sum(g['kovanli'] for g in GAL)
print('%d galaksi (%d kovanli)   a0(SI)=%.3e' % (len(GAL), nk, A0 * ACC))

def v2f(g, mod, k):
    Mk = g['MkT'] if mod == 'B' else g['MkS']
    return g['vb2'] + np.sqrt(k * A0 * G * Mk)

def metrikler(mod, k):
    rms, sap, sinif_sap, rms_kov, rms_kvsz = [], [], {}, [], []
    X, Y = [], []
    for g in GAL:
        v2 = v2f(g, mod, k)
        v = np.sqrt(np.maximum(v2, 1e-9))
        m = g['R'] > np.median(g['R'])
        r = float(np.sqrt(np.mean((v - g['Vo']) ** 2)))
        rms.append(r)
        (rms_kov if g['kovanli'] else rms_kvsz).append(r)
        s = 100 * float(np.mean((v[m] - g['Vo'][m]) / g['Vo'][m]))
        sap.append(s); sinif_sap.setdefault(g['sn'], []).append(s)
        iyi = (g['vb2'] > 0) & (g['Vo'] > 0) & (v2 > 0)
        X.extend(np.log10(g['vb2'][iyi] / g['R'][iyi] * ACC))
        Y.extend(np.log10(g['Vo'][iyi] ** 2 / g['R'][iyi]) - np.log10(v2[iyi] / g['R'][iyi]))
    X, Y = np.array(X), np.array(Y)
    egim = float(np.polyfit(X, Y, 1)[0])
    # yuksek-g ve derin kusak medyan artiklari
    yg = float(np.median(Y[X > -9.5])); dr = float(np.median(Y[X < -10.5]))
    smed = [float(np.median(v)) for v in sinif_sap.values()]
    return dict(rms=float(np.median(rms)), sap=float(np.median(sap)), egim=egim,
                band=max(smed) - min(smed), yg=yg, dr=dr,
                rk=float(np.median(rms_kov)), rz=float(np.median(rms_kvsz)))

def kalibre(mod):
    a, b = 0.05, 20.
    f = lambda k: metrikler(mod, k)['sap']
    for _ in range(50):
        m = np.sqrt(a * b)
        if f(m) < 0: a = m
        else: b = m
    return float(np.sqrt(a * b))

print('\n%-3s %7s | %7s %9s %10s | %8s %8s | %9s %9s' % (
    'mod', 'k_kal', 'medRMS', 'RAR_egim', 'sinif_band', 'yuksek-g', 'derin', 'RMS_kovan', 'RMS_diger'))
M = {}
for mod in ['B', 'C']:
    kk = kalibre(mod)
    r = metrikler(mod, kk); M[mod] = (kk, r)
    print('%-3s %7.3f | %7.2f %+9.4f %9.1f%% | %+8.4f %+8.4f | %9.2f %9.2f' % (
        mod, kk, r['rms'], r['egim'], r['band'], r['yg'], r['dr'], r['rk'], r['rz']))

# galaksi basina kazanan (kalibre modellerle)
kB, kC = M['B'][0], M['C'][0]
kaz = {'B': 0, 'C': 0}
for g in GAL:
    rB = float(np.sqrt(np.mean((np.sqrt(np.maximum(v2f(g, 'B', kB), 1e-9)) - g['Vo']) ** 2)))
    rC = float(np.sqrt(np.mean((np.sqrt(np.maximum(v2f(g, 'C', kC), 1e-9)) - g['Vo']) ** 2)))
    kaz['C' if rC < rB else 'B'] += 1
print('\ngalaksi basina kazanan: B=%d  C=%d' % (kaz['B'], kaz['C']))
kovK = [g for g in GAL if g['kovanli']]
kazk = {'B': 0, 'C': 0}
for g in kovK:
    rB = float(np.sqrt(np.mean((np.sqrt(np.maximum(v2f(g, 'B', kB), 1e-9)) - g['Vo']) ** 2)))
    rC = float(np.sqrt(np.mean((np.sqrt(np.maximum(v2f(g, 'C', kC), 1e-9)) - g['Vo']) ** 2)))
    kazk['C' if rC < rB else 'B'] += 1
print('kovanli altkume (%d): B=%d  C=%d' % (len(kovK), kazk['B'], kazk['C']))

# BTFR yan etkisi: kovanli galaksilerde dis-nokta v_ong farki (C vs B)
fark = []
for g in kovK:
    vB = np.sqrt(np.maximum(v2f(g, 'B', kB), 1e-9))[-1]
    vC = np.sqrt(np.maximum(v2f(g, 'C', kC), 1e-9))[-1]
    fark.append(100 * (vC - vB) / vB)
print('kovanlilarda dis-nokta v_ong farki (C-B): medyan %+.1f%%  aralik [%+.1f, %+.1f]' % (
    float(np.median(fark)), min(fark), max(fark)))
