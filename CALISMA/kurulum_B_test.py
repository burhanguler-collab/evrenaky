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
C_SI = 2.99792458e8
ACC = 1e6 / 3.0856776e19
A0 = (C_SI * (70e3 / 3.0857e22)) / ACC / 16.1
RB = 1.4
UPS = 0.50

siniflar = ['01_erken_spiral', '02_orta_spiral', '03_gec_spiral', 
            '04_cok_gec_spiral', '05_macellan', '06_duzensiz', '99_KARMASIK']

tum_rms_A = []
tum_rms_B = []
tum_rms_B221 = []
tum_sapma_A = []
tum_sapma_B = []
tum_sapma_B221 = []

print("KURULUM B TESTI BASLIYOR (Orijinal Dosyalara Dokunulmuyor)\n" + "="*70)

for s in siniflar:
    sd = os.path.join(SINIF_DIR, s)
    if not os.path.isdir(sd): continue
    
    kat_path = os.path.join(sd, 'KATALOG.csv')
    if not os.path.exists(kat_path): continue
    kat = {r['Galaksi']: r for r in csv.DictReader(open(kat_path, encoding='utf-8'))}
    
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
    
    rms_A_sinif = []
    rms_B_sinif = []
    rms_B221_sinif = []
    
    for gal in galaksiler:
        vo = gal['Vo']
        vb2 = gal['Vbar2']
        mkaps = np.maximum(gal['Mkaps'], 1e-6)
        mb = mkaps[-1] # toplam kutle
        
        # Kurulum A (Mevcut: Toplam kütle l_omega)
        lom_A = np.sqrt(G * mb / A0)
        v_A = np.sqrt(np.maximum(vb2 + G * mkaps / lom_A, 1e-9))
        
        # Kurulum B (Yerel kütle l_omega) -> v_F4^2 = sqrt(G * Mkaps * A0)
        v_B = np.sqrt(np.maximum(vb2 + np.sqrt(G * mkaps * A0), 1e-9))
        
        # Kurulum B + 2.21x (Kalibrasyon)
        v_B221 = np.sqrt(np.maximum(vb2 + np.sqrt(2.21) * np.sqrt(G * mkaps * A0), 1e-9))
        
        rms_A = np.sqrt(np.mean((v_A - vo)**2))
        rms_B = np.sqrt(np.mean((v_B - vo)**2))
        rms_B221 = np.sqrt(np.mean((v_B221 - vo)**2))
        
        rms_A_sinif.append(rms_A)
        rms_B_sinif.append(rms_B)
        rms_B221_sinif.append(rms_B221)
        
        tum_rms_A.append(rms_A)
        tum_rms_B.append(rms_B)
        tum_rms_B221.append(rms_B221)
        
        # Sapma olcumu (medyan hata orani)
        tum_sapma_A.append(np.mean((v_A - vo)/vo))
        tum_sapma_B.append(np.mean((v_B - vo)/vo))
        tum_sapma_B221.append(np.mean((v_B221 - vo)/vo))
        
    print(f"{s:<18} n={len(galaksiler):<3} | A: {np.median(rms_A_sinif):.2f}  | B: {np.median(rms_B_sinif):.2f}  | B+2.21: {np.median(rms_B221_sinif):.2f}")

print("="*70)
print("TUM GALAKSILER (Genel Medyan)")
print(f"Toplam Galaksi Sayisi: {len(tum_rms_A)}")
print(f"Kurulum A (Mevcut) RMS    : {np.median(tum_rms_A):.2f} km/s  | Sapma: %{100*np.median(tum_sapma_A):.1f}")
print(f"Kurulum B (Yerel l_omega) : {np.median(tum_rms_B):.2f} km/s  | Sapma: %{100*np.median(tum_sapma_B):.1f}")
print(f"Kurulum B + a_0 x 2.21    : {np.median(tum_rms_B221):.2f} km/s  | Sapma: %{100*np.median(tum_sapma_B221):.1f}")
