# -*- coding: utf-8 -*-
"""
SINIF-ICI SURUKLENME SINAVI (87_ETKIN_YASA is 7)

Soru (TOPLANMA_TURETIMI.md md. 3, aday ii): RAR artik surklenmesi (kuresel egim ~ -0,043,
gozlem-ongoru) gecis BICIMININ mi, yoksa siniflar/galaksiler ARASI ofsetlerin (lambda kanali)
mi eseri?

Ayristirma — sabit-etkiler: artik = log g_obs - log g_ong (model B, adil kalibre k),
x = log g_bar. Uc katman:
  1) KURESEL egim (referans)
  2) SINIF-ICI egim: her sinifin (x, artik) ortalamalari dusulup havuzlanir
  3) GALAKSI-ICI egim: her galaksinin ortalamalari dusulup havuzlanir  <- gecis biciminin saf olcusu
  + SINIFLAR-ARASI: sinif medyanlari (x_med, artik_med) uzerinden egim (n=6)
  + GALAKSILER-ARASI: galaksi ortalamalari uzerinden egim (n=141)

Okuma kurali (onceden): galaksi-ici egim ~= kuresel -> bicim borcu gercek (aday i hedefte);
galaksi-ici ~ 0 ve galaksiler-arasi tasiyorsa -> surklenme lambda/sinif kanalinin izi,
gecis fonksiyonu aklanir.
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
K = 1.011   # B'nin adil kalibrasyonu (vortisite_taramasi.py)
AD = {'01_erken_spiral': 'Sa-Sab', '02_orta_spiral': 'Sb-Sbc', '03_gec_spiral': 'Sc-Scd',
      '04_cok_gec_spiral': 'Sd', '05_macellan': 'Sdm-Sm', '06_duzensiz': 'Im'}

VER = []   # (sinif, galaksi, x, y) nokta listeleri
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
        v2 = vb2 + np.sqrt(K * A0 * G * Mk)
        iyi = (vb2 > 0) & (Vo > 0) & (v2 > 0)
        if iyi.sum() < 4:
            continue
        x = np.log10(vb2[iyi] / R[iyi] * ACC)
        y = np.log10(Vo[iyi] ** 2 / R[iyi]) - np.log10(v2[iyi] / R[iyi])
        VER.append((sn, os.path.basename(f)[:-11], x, y))
print('%d galaksi, %d nokta' % (len(VER), sum(len(x) for _, _, x, y in VER)))

def egim(X, Y):
    return float(np.polyfit(np.array(X), np.array(Y), 1)[0])

# 1) kuresel
Xg = np.concatenate([x for _, _, x, y in VER]); Yg = np.concatenate([y for _, _, x, y in VER])
print('\n1) KURESEL egim                = %+.4f dex/dex  (n=%d)' % (egim(Xg, Yg), len(Xg)))

# 2) sinif-ici (sinif ortalamalari dusulmus)
Xs, Ys = [], []
for sn in sorted(AD):
    xs = np.concatenate([x for s, _, x, y in VER if s == sn])
    ys = np.concatenate([y for s, _, x, y in VER if s == sn])
    Xs.extend(xs - xs.mean()); Ys.extend(ys - ys.mean())
print('2) SINIF-ICI egim (sabit etki) = %+.4f dex/dex' % egim(Xs, Ys))

# 3) galaksi-ici (galaksi ortalamalari dusulmus)
Xw, Yw = [], []
gal_eg = []
for _, _, x, y in VER:
    Xw.extend(x - x.mean()); Yw.extend(y - y.mean())
    if len(x) >= 6:
        gal_eg.append(egim(x, y))
print('3) GALAKSI-ICI egim (sabit etki)= %+.4f dex/dex   [galaksi-basina egim medyani: %+.4f, n=%d]'
      % (egim(Xw, Yw), float(np.median(gal_eg)), len(gal_eg)))

# 4) arasi bilesenler
gx = [float(x.mean()) for _, _, x, y in VER]
gy = [float(y.mean()) for _, _, x, y in VER]
print('4) GALAKSILER-ARASI egim       = %+.4f dex/dex  (galaksi ortalamalari, n=%d)' % (egim(gx, gy), len(gx)))
sx, sy = [], []
print('\n   sinif tablosu:  %-8s %4s | %9s %9s %9s' % ('sinif', 'nG', 'med_x', 'med_artik', 'sinif_egim'))
for sn in sorted(AD):
    xs = np.concatenate([x for s, _, x, y in VER if s == sn])
    ys = np.concatenate([y for s, _, x, y in VER if s == sn])
    sx.append(float(np.median(xs))); sy.append(float(np.median(ys)))
    nG = sum(1 for s, _, _, _ in VER if s == sn)
    print('   %-16s %4d | %9.2f %+9.3f %+9.4f' % (AD[sn], nG, sx[-1], sy[-1], egim(xs, ys)))
print('   SINIFLAR-ARASI egim (6 medyan) = %+.4f dex/dex' % egim(sx, sy))
