import os
import sys
import csv
import glob
import numpy as np
import warnings

warnings.filterwarnings('ignore')

KOK = os.path.dirname(os.path.abspath(__file__))
SINIF_DIR = os.path.join(KOK, 'SINIF_CALISMASI')

G = 4.300917e-6
ACC = 1e6 / 3.0856776e19
# Evrenaki a0 (7.39e-11)
A0_EVR = 7.39e-11 / ACC
# MOND a0 (McGaugh 2016 degeri: 1.20e-10)
A0_MOND = 1.20e-10 / ACC

RB = 1.4
UPS = 0.50

siniflar = ['01_erken_spiral', '02_orta_spiral', '03_gec_spiral', 
            '04_cok_gec_spiral', '05_macellan', '06_duzensiz']

print("MOND vs EVRENAKI KARSILASTIRMASI (SIFIR SERBEST PARAMETRE)\n" + "="*70)

galaksi_sayisi = 0
evrenaki_kazanan = 0
mond_kazanan = 0

tum_rms_evr = []
tum_rms_mond = []
tum_sapma_evr = []
tum_sapma_mond = []

for s in siniflar:
    sd = os.path.join(SINIF_DIR, s)
    if not os.path.isdir(sd): continue
    
    galaksiler = []
    for f in sorted(glob.glob(os.path.join(sd, 'veri', '*_rotmod.dat'))):
        ad = os.path.basename(f)[:-11]
        d = np.loadtxt(f)
        if d.ndim < 2 or len(d) < 3: continue
        R, Vo, eV, Vg, Vd, Vb, SBd, SBb = [d[:, i] for i in range(8)]
        Rp = R * 1e3
        L = lambda S: np.concatenate([[0.0], np.cumsum(np.pi * (Rp[1:] ** 2 - Rp[:-1] ** 2) * 0.5 * (S[1:] + S[:-1]))])
        Vbar2 = np.sign(Vg) * Vg ** 2 + UPS * Vd ** 2 + RB * UPS * Vb ** 2
        Mgas = np.maximum(R * np.sign(Vg) * Vg ** 2 / G, 0.0)
        Mkaps = UPS * L(SBd) + RB * UPS * L(SBb) + Mgas
        
        galaksiler.append({'g': ad, 'R': R, 'Vo': Vo, 'Vbar2': Vbar2, 'Mkaps': Mkaps})
    
    rms_evr_sinif = []
    rms_mond_sinif = []
    sapma_evr_sinif = []
    sapma_mond_sinif = []
    kazanan_e = 0
    kazanan_m = 0
    
    for gal in galaksiler:
        vo = gal['Vo']
        vb2 = np.maximum(gal['Vbar2'], 1e-9)
        mkaps = np.maximum(gal['Mkaps'], 1e-6)
        R = gal['R']
        
        # Evrenaki (Kurulum B - Yerel Kutle F4)
        v_evr = np.sqrt(np.maximum(vb2 + np.sqrt(G * mkaps * A0_EVR), 1e-9))
        
        # MOND (Radyal Ivme Interpolasyon Fonksiyonu McGaugh 2016)
        gbar = vb2 / R
        # Ivmelerin sifir oldugu noktalarda log hatasini onlemek icin 1e-9 ile maskele
        gbar = np.maximum(gbar, 1e-12)
        g_mond = gbar / (1.0 - np.exp(-np.sqrt(gbar / A0_MOND)))
        v_mond = np.sqrt(np.maximum(g_mond * R, 1e-9))
        
        rms_evr = np.sqrt(np.mean((v_evr - vo)**2))
        rms_mond = np.sqrt(np.mean((v_mond - vo)**2))
        
        sapma_evr = np.mean((v_evr - vo)/vo)
        sapma_mond = np.mean((v_mond - vo)/vo)
        
        rms_evr_sinif.append(rms_evr)
        rms_mond_sinif.append(rms_mond)
        sapma_evr_sinif.append(sapma_evr)
        sapma_mond_sinif.append(sapma_mond)
        tum_rms_evr.append(rms_evr)
        tum_rms_mond.append(rms_mond)
        tum_sapma_evr.append(sapma_evr)
        tum_sapma_mond.append(sapma_mond)
        
        if rms_evr < rms_mond:
            kazanan_e += 1
            evrenaki_kazanan += 1
        else:
            kazanan_m += 1
            mond_kazanan += 1
            
    print(f"{s:<18} n={len(galaksiler):<3} | RMS: {np.median(rms_evr_sinif):>5.2f} vs {np.median(rms_mond_sinif):>5.2f} | Sapma: {np.median(sapma_evr_sinif)*100:>5.1f}% vs {np.median(sapma_mond_sinif)*100:>5.1f}% | Yaris: {kazanan_e:>2} (E) - {kazanan_m:>2} (M)")

print("="*70)
print(f"TOPLAM GALAKSI: {len(tum_rms_evr)}")
print(f"GENEL MEDYAN RMS - Evrenaki: {np.median(tum_rms_evr):.2f} km/s")
print(f"GENEL MEDYAN RMS - MOND    : {np.median(tum_rms_mond):.2f} km/s")
print(f"GENEL SAPMA YUZDESI        : Evrenaki %{np.median(tum_sapma_evr)*100:.1f} vs MOND %{np.median(tum_sapma_mond)*100:.1f}")
print(f"KAZANAN GALAKSI SAYISI     : Evrenaki {evrenaki_kazanan} vs {mond_kazanan} MOND")
