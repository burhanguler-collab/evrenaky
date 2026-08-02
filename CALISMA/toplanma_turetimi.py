# -*- coding: utf-8 -*-
"""
TOPLANMA TURETIMI SINAVI — kayma-agirlikli koherens (87_ETKIN_YASA is 6)

Turetim zinciri (TOPLANMA_TURETIMI.md):
 1) a = a_F1 + a_F4 lineer superpozisyondan turer (M-44/M-46; capraz terim ~1e-9) — toplama borcu kapali.
 2) F4'un koherent kolonunu kaskad kurar; kaskadin kaynagi diferansiyel donmenin KAYMASIDIR.
    Kati-cisim bolgede kayma sifir -> koherent kolon beslenmez.
    Boyutsuz agirlik: w = 1 - dlnv/dlnR   (kati cisim 0, duz kol 1, Kepler 3/2)
 3) sqrt(N) koprusu koherent kesre: a_F4 = sqrt(w) * sqrt(G M_kaps a0)/R.
    w ONGORULEN v'den oz-uyumlu iterasyonla (veri kullanilmaz; taban dogmaz; w sinirli).

Sinav: S (kayma-agirlikli) vs B (w=1) — her ikisi adil kalibrasyonla (dis-yari medyan sapma=0).
Olcutler: medyan RMS · RAR bicim egimi (gozlem-ongoru) · sinif bandi · kusak artiklari.
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
print('%d galaksi' % len(GAL))

W_MAX = 1.5

def v2_S(g, k, kayma=True):
    F4taban = np.sqrt(k * A0 * G * g['Mk'])
    if not kayma:
        return g['vb2'] + F4taban
    lnR = np.log(g['R'])
    v2 = np.maximum(g['vb2'] + F4taban, 1e-9)          # baslangic: w=1
    for _ in range(6):
        lnv = 0.5 * np.log(v2)
        w = np.clip(1. - np.gradient(lnv, lnR), 0., W_MAX)
        v2 = np.maximum(g['vb2'] + np.sqrt(w) * F4taban, 1e-9)
    return v2

def metrikler(kayma, k):
    rms, sap, sinif_sap, X, Y = [], [], {}, [], []
    for g in GAL:
        v2 = v2_S(g, k, kayma)
        v = np.sqrt(v2)
        m = g['R'] > np.median(g['R'])
        rms.append(float(np.sqrt(np.mean((v - g['Vo']) ** 2))))
        s = 100 * float(np.mean((v[m] - g['Vo'][m]) / g['Vo'][m]))
        sap.append(s); sinif_sap.setdefault(g['sn'], []).append(s)
        iyi = (g['vb2'] > 0) & (g['Vo'] > 0) & (v2 > 0)
        X.extend(np.log10(g['vb2'][iyi] / g['R'][iyi] * ACC))
        Y.extend(np.log10(g['Vo'][iyi] ** 2 / g['R'][iyi]) - np.log10(v2[iyi] / g['R'][iyi]))
    X, Y = np.array(X), np.array(Y)
    egim = float(np.polyfit(X, Y, 1)[0])
    smed = [float(np.median(v)) for v in sinif_sap.values()]
    return (float(np.median(rms)), float(np.median(sap)), egim,
            max(smed) - min(smed), X, Y)

def kalibre(kayma):
    a, b = 0.2, 5.
    med = lambda k: metrikler(kayma, k)[1]
    for _ in range(45):
        m = np.sqrt(a * b)
        if med(m) < 0:
            a = m
        else:
            b = m
    return float(np.sqrt(a * b))

print('\n%12s %7s | %8s %9s %11s' % ('model', 'k_kal', 'medRMS', 'RAR_egim', 'sinif_band'))
saklanan = {}
for ad, kayma in [('B (w=1)', False), ('S (kayma-w)', True)]:
    kk = kalibre(kayma)
    r, s, e, band, X, Y = metrikler(kayma, kk)
    saklanan[ad] = (X, Y)
    print('%12s %7.3f | %8.2f %+9.4f %10.1f%%' % (ad, kk, r, e, band))

print('\nKUSAK ARTIKLARI (gozlem-ongoru, dex) — duzelme nerede?')
print('%22s | %8s %8s' % ('log g_bar kusagi', 'B', 'S'))
kus = [(-13, -11), (-11, -10.5), (-10.5, -10), (-10, -9.5), (-9.5, -9), (-9, -7)]
for lo, hi in kus:
    satir = []
    for ad in ['B (w=1)', 'S (kayma-w)']:
        X, Y = saklanan[ad]
        m = (X >= lo) & (X < hi)
        satir.append(float(np.median(Y[m])) if m.sum() > 5 else np.nan)
    print('%10.1f .. %6.1f | %+8.3f %+8.3f   (n=%d)' % (lo, hi, satir[0], satir[1],
          ((saklanan['B (w=1)'][0] >= lo) & (saklanan['B (w=1)'][0] < hi)).sum()))
