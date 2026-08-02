# -*- coding: utf-8 -*-
"""
PENCERE SINAVI — Rankine penceresinin resmilesme kosumu (87_ETKIN_YASA is 8; onay: kullanici)

Resmi denklem (guncellenmis):
  v^2(R) = V_bar^2 + sqrt(G M_kaps(R) a0) * W,   W = min(1, a0/g_kaps),  g_kaps = G M_kaps/R^2
Turetim: PENCERE_TURETIMI.md (M-30 Rankine ic kolu + r0 = l_omega^etkin ozdeslestirmesi; parametresiz).

Bu betik ASAGI-AKIS sinavlarini yeniden kosar:
  1) Donus egrisi defteri (141 galaksi, sinif sinif): B (penceresiz) vs P (pencereli)
  2) lambda/sinif-carpani KARARLILIGI: galaksi basina gereken k, B vs P (sigma sinavi etkilenir mi?)
  3) BTFR: R_dis noktasinda W dagilimi (W=1 ise BTFR sonuclari analitik olarak degismez)
  4) RAR (Lelli+2017 _RAR.mrt, 2693 nokta): medyan artik + bicim egimi, pencereyle
     (W icin g_kaps yerine g_bar vekili — mrt'de kutle/yaricap yok; kayit dusulur)
  5) YUKSEK-Z (Genzel+2017, 6 galaksi): f_DM ongorusu pencereyle — birincil acik yeniden olculur

a0 = NIHAI deger x k_kal(P) = 7.39e-11 x 1.038 (adil kalibrasyon, PENCERE_TURETIMI.md).
Cikti: SINIF_CALISMASI/87_ETKIN_YASA/SONUC_PENCERE.csv
"""
import os, sys, glob, csv, io, warnings
import numpy as np

warnings.filterwarnings('ignore')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

KOK = os.path.dirname(os.path.abspath(__file__))
SK = os.path.join(KOK, 'SINIF_CALISMASI')
G = 4.300917e-6
ACC = 1e6 / 3.0856776e19
A0N = 1.75 * (2.99792458e8 * (70e3 / 3.0857e22)) / ACC / 16.1   # nihai a0
KP = 1.038                                                       # pencereli adil kalibrasyon
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
        GAL.append(dict(sn=sn, ad=os.path.basename(f)[:-11], R=R, Vo=Vo, vb2=vb2, Mk=Mk))
print('%d galaksi   a0(P) = %.3e m/s^2' % (len(GAL), KP * A0N * ACC))

def v2m(g, k, pencere):
    F4t = np.sqrt(k * A0N * G * g['Mk'])
    if not pencere:
        return np.maximum(g['vb2'] + F4t, 1e-9)
    gk = G * g['Mk'] / g['R'] ** 2
    W = np.minimum(1., (k * A0N) / gk)
    return np.maximum(g['vb2'] + W * F4t, 1e-9)

def carpan(g, pencere):
    m = g['R'] > np.median(g['R'])
    fk = lambda k: float(np.mean((np.sqrt(v2m(g, k, pencere))[m] - g['Vo'][m]) / g['Vo'][m]))
    a, b = 1e-3, 1e3
    if fk(a) > 0 or fk(b) < 0:
        return np.nan
    for _ in range(80):
        mm = np.sqrt(a * b)
        if fk(mm) < 0:
            a = mm
        else:
            b = mm
    return float(np.sqrt(a * b))

# ---------------- 1) donus egrisi defteri ----------------
print('\n1) DONUS EGRISI DEFTERI — B (k=1.011, penceresiz) vs P (k=1.038, pencereli)')
print('%-16s %4s | %8s %8s | %9s %9s' % ('sinif', 'n', 'B_rms', 'P_rms', 'B_sap%', 'P_sap%'))
for g in GAL:
    for et, k, p in [('B', 1.011, False), ('P', KP, True)]:
        v = np.sqrt(v2m(g, k, p))
        m = g['R'] > np.median(g['R'])
        g['rms' + et] = float(np.sqrt(np.mean((v - g['Vo']) ** 2)))
        g['sap' + et] = 100 * float(np.mean((v[m] - g['Vo'][m]) / g['Vo'][m]))
    g['kB'] = carpan(g, False)
    g['kP'] = carpan(g, True)
for sn in sorted(AD):
    gg = [g for g in GAL if g['sn'] == sn]
    md = lambda k: float(np.median([x[k] for x in gg]))
    print('%-16s %4d | %8.2f %8.2f | %+9.1f %+9.1f' % (AD[sn], len(gg),
          md('rmsB'), md('rmsP'), md('sapB'), md('sapP')))
md = lambda k: float(np.median([x[k] for x in GAL]))
print('%-16s %4d | %8.2f %8.2f | %+9.1f %+9.1f' % ('GENEL MEDYAN', len(GAL),
      md('rmsB'), md('rmsP'), md('sapB'), md('sapP')))

# ---------------- 2) lambda/carpan kararliligi ----------------
kb = np.array([g['kB'] for g in GAL]); kp = np.array([g['kP'] for g in GAL])
iyi = np.isfinite(kb) & np.isfinite(kp)
r = np.corrcoef(np.log(kb[iyi]), np.log(kp[iyi]))[0, 1]
orn = np.median(kp[iyi] / kb[iyi])
print('\n2) CARPAN KARARLILIGI (lambda/sigma sinavi etkilenir mi?)')
print('   log k_B <-> log k_P Pearson r = %.4f   medyan k_P/k_B = %.3f  (n=%d)' % (r, orn, iyi.sum()))
print('   sinif medyan carpanlari:')
for sn in sorted(AD):
    gg = [g for g in GAL if g['sn'] == sn and np.isfinite(g['kB']) and np.isfinite(g['kP'])]
    print('   %-14s k_B=%.3f  k_P=%.3f' % (AD[sn],
          float(np.median([g['kB'] for g in gg])), float(np.median([g['kP'] for g in gg]))))

# ---------------- 3) BTFR: R_dis'ta W ----------------
Wd = []
for g in GAL:
    gk = G * g['Mk'][-1] / g['R'][-1] ** 2
    Wd.append(min(1., KP * A0N / gk))
Wd = np.array(Wd)
print('\n3) BTFR DENETIMI — R_dis noktasinda pencere:')
print('   W=1 olan galaksi: %d/141 · medyan W = %.3f · min W = %.3f' % ((Wd >= 1.).sum(),
      float(np.median(Wd)), float(Wd.min())))
print('   W<1 olanlar (ic kesim, BTFR normuna etki):')
for g, w in zip(GAL, Wd):
    if w < 1:
        print('     %-12s W=%.2f (%s)' % (g['ad'], w, AD[g['sn']]))

# ---------------- 4) RAR (_RAR.mrt) ----------------
gbar, gobs = [], []
with io.open(os.path.join(KOK, 'veri', '_RAR.mrt'), encoding='utf-8', errors='replace') as f:
    for line in f:
        p = line.split()
        if len(p) == 4:
            try:
                a, b = float(p[0]), float(p[2])
            except ValueError:
                continue
            gbar.append(a); gobs.append(b)
gbar = 10 ** np.array(gbar); gobs = np.array(gobs)   # gbar SI, gobs log
a0 = KP * A0N * ACC
for et, W in [('B (penceresiz)', np.ones_like(gbar)),
              ('P (pencereli, g_bar vekili)', np.minimum(1., a0 / gbar))]:
    gpred = gbar + np.sqrt(gbar * a0) * W
    art = gobs - np.log10(gpred)                      # gozlem - ongoru (dex)
    x = np.log10(gbar)
    print('\n4) RAR [%s]: n=%d  medyan artik %+0.4f dex  bicim egimi %+0.4f dex/dex'
          % (et, len(art), float(np.median(art)), float(np.polyfit(x, art, 1)[0])))

# ---------------- 5) YUKSEK-Z (Genzel+2017) ----------------
print('\n5) YUKSEK-Z — f_DM = v_F4^2/v_c^2 ongorusu (pencereyle)')
print('   (W icin g_F1 = v_bar^2/R vekili; oz-uyumlu s cozumu, 40 iterasyon)')
yol = os.path.join(KOK, 'veri', '_genzel2017_tablo1.csv')
say_ic = 0; artP = []
eski = {}
with io.open(os.path.join(SK, '90_YUKSEK_Z', 'SONUC.csv'), encoding='utf-8-sig') as f0:
    for r0 in csv.DictReader(f0):
        eski[r0['Galaksi']] = float(r0['ONG_SABIT'])
with io.open(yol, encoding='utf-8', errors='replace') as f:
    for r_ in csv.DictReader(x for x in f if not x.startswith('#')):
        ad = r_[list(r_.keys())[0]]
        z = float(r_['z']); R = float(r_['R_half_kpc']); vc = float(r_['vc_kms'])
        fg = float(r_['fDM']); ust = r_['fDM_ust_sinir_mi'].strip() == 'evet'
        ustv = float(r_['fDM_ust'])
        a0u = KP * A0N            # (km/s)^2/kpc
        s = 0.9
        for _ in range(40):
            vbar2 = (s * vc) ** 2
            gF1 = vbar2 / R
            W = min(1., a0u / gF1)
            vF42 = np.sqrt(vbar2 * a0u * R) * W       # sqrt(g_F1 a0)*R*W = v_bar*sqrt(a0 R)*W
            s = np.sqrt(max(vc ** 2 - vF42, 1e-9)) / vc
        fP = 1. - s ** 2
        icinde = (fP <= ustv) if ust else (float(r_['fDM_alt']) <= fP <= ustv)
        artP.append(fP - fg)
        say_ic += int(icinde)
        print('   %-11s z=%.2f  gozlem %.2f%s  eski_ong %.3f  PENCERELI %.3f  %s'
              % (ad, z, fg, ' (ust sinir %.2f)' % ustv if ust else '',
                 eski.get(ad, float('nan')), fP, 'BANT ICINDE' if icinde else 'disari'))
print('   medyan artik (pencereli, ong-gozlem): %+0.3f  (eski kayit: +0.19 dex esdegeri +0.21)' %
      float(np.median(artP)))
print('   bant icinde: %d/6' % say_ic)

# ---------------- cikti ----------------
yol = os.path.join(SK, '87_ETKIN_YASA', 'SONUC_PENCERE.csv')
with io.open(yol, 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Galaksi', 'Sinif', 'B_rms', 'P_rms', 'B_sap', 'P_sap', 'k_B', 'k_P', 'W_Rdis'])
    for g, wd in zip(GAL, Wd):
        w.writerow([g['ad'], AD[g['sn']]] + ['%.3f' % g[k] for k in
                    ('rmsB', 'rmsP', 'sapB', 'sapP', 'kB', 'kP')] + ['%.3f' % wd])
print('\nyazildi: %s' % yol)
