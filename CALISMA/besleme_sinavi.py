# -*- coding: utf-8 -*-
"""
BESLEME SINAVI — F4'un kaynagi M_kaps mi, yerel g_bar mi? (87_ETKIN_YASA is 4)

Dis kaynakli bir not (Gemini/Antigravity, 'MOND_Eritilmis_Evrenaki.md') iki beslemenin
ayristigini ve verinin g_bar-beslemeyi tercih ettigini iddia etti. Bu betik iddiayi
TEORININ KENDI BORU HATTINDAN gecirir: 94'un veri yukleme/konvansiyonlari birebir
(Ups*=0.50, kovan 0.70, ayni 141 galaksi, ayni RMS tanimi), a_0 = NIHAI kurulum.

Uc model (galaksi basina fit YOK):
  B  (resmi)  : v^2 = V_bar^2 + sqrt(G M_kaps(R) a0)   [M_kaps: fotometrik kumulatif + gaz]
  D  (g_bar)  : v^2 = V_bar^2 + sqrt(g_bar a0) R  = V_bar^2 + sqrt(V_bar^2 R a0)
  M  (MOND)   : g = g_bar / (1 - exp(-sqrt(g_bar/g_dagger))),  g_dagger = 1.2e-10 (fitli)

Olcutler: sinif basi medyan RMS · dis-yari sapma · RAR bicim egimi (artik ~ log g_bar).
Cikti: SINIF_CALISMASI/87_ETKIN_YASA/SONUC_BESLEME.csv
"""
import os, sys, glob, csv, io, warnings
import numpy as np

warnings.filterwarnings('ignore')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

KOK = os.path.dirname(os.path.abspath(__file__))
SK = os.path.join(KOK, 'SINIF_CALISMASI')
CIK = os.path.join(SK, '87_ETKIN_YASA')

G = 4.300917e-6                                   # kpc (km/s)^2 / Msun
ACC = 1e6 / 3.0856776e19                          # (km/s)^2/kpc -> m/s^2
A0 = 1.75 * (2.99792458e8 * (70e3 / 3.0857e22)) / ACC / 16.1   # NIHAI a0, (km/s)^2/kpc
GD = 1.2e-10 / ACC                                # MOND g_dagger, (km/s)^2/kpc
RB, UPS = 1.4, 0.50
AD = {'01_erken_spiral': 'Sa-Sab', '02_orta_spiral': 'Sb-Sbc', '03_gec_spiral': 'Sc-Scd',
      '04_cok_gec_spiral': 'Sd', '05_macellan': 'Sdm-Sm', '06_duzensiz': 'Im'}
print('a0 (SI) = %.3e m/s^2   g_dagger (SI) = 1.2e-10' % (A0 * ACC))

GAL = []
for sn in sorted(AD):
    for f in sorted(glob.glob(os.path.join(SK, sn, 'veri', '*_rotmod.dat'))):
        d = np.loadtxt(f)
        R, Vo, eV, Vg, Vd, Vb, SBd, SBb = [d[:, i] for i in range(8)]
        Rp = R * 1e3
        L = lambda S: np.concatenate([[0.], np.cumsum(
            np.pi * (Rp[1:] ** 2 - Rp[:-1] ** 2) * .5 * (S[1:] + S[:-1]))])
        vb2 = np.sign(Vg) * Vg ** 2 + UPS * Vd ** 2 + RB * UPS * Vb ** 2
        Mk = UPS * L(SBd) + RB * UPS * L(SBb) + np.maximum(R * np.sign(Vg) * Vg ** 2 / G, 0.)
        GAL.append(dict(ad=os.path.basename(f)[:-11], sn=sn, R=R, Vo=Vo, vb2=vb2,
                        Mk=np.maximum(Mk, 1e-6)))
print('%d galaksi' % len(GAL))

def v2_model(g, mod):
    vb2, R = g['vb2'], g['R']
    if mod == 'B':
        return vb2 + np.sqrt(A0 * G * g['Mk'])
    if mod == 'D':
        return vb2 + np.sqrt(A0 * np.maximum(vb2, 0.) * R)
    gbar = vb2 / R
    nu = np.ones_like(gbar)
    poz = gbar > 0
    nu[poz] = 1. / (1. - np.exp(-np.sqrt(gbar[poz] / GD)))
    return nu * vb2

MODS = ['B', 'D', 'M']
for g in GAL:
    m = g['R'] > np.median(g['R'])
    for mod in MODS:
        v = np.sqrt(np.maximum(v2_model(g, mod), 1e-9))
        g['rms' + mod] = float(np.sqrt(np.mean((v - g['Vo']) ** 2)))
        g['sap' + mod] = 100 * float(np.mean((v[m] - g['Vo'][m]) / g['Vo'][m]))

# ---------------- 1) sinif defteri ----------------
print('\n1) DONUS EGRISI RMS (medyan, km/s) ve dis-yari sapmasi (medyan, %)')
print('%-16s %5s | %7s %7s %7s | %7s %7s %7s' % ('sinif', 'n', 'B_rms', 'D_rms', 'M_rms', 'B_sap', 'D_sap', 'M_sap'))
for sn in sorted(AD):
    gg = [g for g in GAL if g['sn'] == sn]
    r = lambda k: float(np.median([x[k] for x in gg]))
    print('%-16s %5d | %7.2f %7.2f %7.2f | %+7.1f %+7.1f %+7.1f' % (AD[sn], len(gg),
        r('rmsB'), r('rmsD'), r('rmsM'), r('sapB'), r('sapD'), r('sapM')))
r = lambda k: float(np.median([x[k] for x in GAL]))
print('%-16s %5d | %7.2f %7.2f %7.2f | %+7.1f %+7.1f %+7.1f' % ('GENEL MEDYAN', len(GAL),
    r('rmsB'), r('rmsD'), r('rmsM'), r('sapB'), r('sapD'), r('sapM')))
kaz = {m: 0 for m in MODS}
for g in GAL:
    en = min(MODS, key=lambda m: g['rms' + m])
    kaz[en] += 1
print('galaksi basina en dusuk RMS: B=%d  D=%d  M=%d' % (kaz['B'], kaz['D'], kaz['M']))

# ---------------- 2) RAR bicim egimi ----------------
print('\n2) RAR BICIM EGIMI — artik = log10 g_obs - log10 g_ong;  egim d(artik)/d(log g_bar)')
print('   (ayni rotmod noktalari; vb2>0; egim = EKK dogrusu)')
for esik, ete in [(None, 'tum noktalar'), (-9.5, 'log g_bar < -9.5 (dusuk-ivme)')]:
    for mod in MODS:
        X, Y = [], []
        for g in GAL:
            vb2, R, Vo = g['vb2'], g['R'], g['Vo']
            v2p = v2_model(g, mod)
            iyi = (vb2 > 0) & (v2p > 0) & (Vo > 0)
            gb = np.log10(vb2[iyi] / R[iyi] * ACC)
            art = np.log10(Vo[iyi] ** 2 / R[iyi]) - np.log10(v2p[iyi] / R[iyi])
            if esik is not None:
                s = gb < esik
                gb, art = gb[s], art[s]
            X.extend(gb); Y.extend(art)
        X, Y = np.array(X), np.array(Y)
        p = np.polyfit(X, Y, 1)
        print('   [%s]  %s  n=%d  egim = %+0.4f dex/dex   medyan artik = %+0.4f' % (
            ete, mod, len(X), p[0], float(np.median(Y))))

# ---------------- 3) cikti ----------------
yol = os.path.join(CIK, 'SONUC_BESLEME.csv')
with io.open(yol, 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Galaksi', 'Sinif', 'B_rms', 'D_rms', 'M_rms', 'B_sap', 'D_sap', 'M_sap'])
    for g in GAL:
        w.writerow([g['ad'], AD[g['sn']]] + ['%.2f' % g[k] for k in
                    ('rmsB', 'rmsD', 'rmsM', 'sapB', 'sapD', 'sapM')])
print('\nyazildi: %s' % yol)
