import os
import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from scipy.optimize import curve_fit

KOK = os.path.dirname(os.path.abspath(__file__))
HESAP_DIR = os.path.join(KOK, 'SINIF_CALISMASI', '_HESAPLAR')
CSV_PATH = os.path.join(HESAP_DIR, 'sinif_carpan_duzeltme.csv')

# Sabitler
G = 4.300917e-6
C_SI = 2.99792458e8
ACC = 1e6 / 3.0856776e19
A0_SABIT = (C_SI * (70e3 / 3.0857e22)) / ACC / 16.1

data = []
with open(CSV_PATH, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['carpan_okunabilir'] == 'evet':
            data.append({
                'sinif': row['Sinif'],
                'klasor': row['Sinif_klasor'],
                'galaksi': row['Galaksi'],
                'k': float(row['carpan_DOGRU_sayisal']),
                'g_dis': float(row['g_bar_dis_nokta_ms2']),
                'g_med': float(row['g_bar_medyan_ms2'])
            })

if not data:
    print("Yeterli veri bulunamadi.")
    sys.exit()

k = np.array([d['k'] for d in data])
g_dis = np.array([d['g_dis'] for d in data])
g_med = np.array([d['g_med'] for d in data])

# Log-Log Uzayi
log_k = np.log10(k)
log_g = np.log10(g_dis)

# Spearman Korelasyonu
corr, pval = spearmanr(log_g, log_k)
print(f"--- KORELASYON ANALIZI ---")
print(f"Baryonik Ivme (g_dis) ile a_0 carpani (k) arasindaki Spearman korelasyonu: {corr:.3f}")

# Power-law fit: log(k) = alpha * log(g) + beta  =>  k = 10^beta * g^alpha
coeffs = np.polyfit(log_g, log_k, 1)
alpha, beta = coeffs
print(f"Fit denklemi: log(k) = {alpha:.3f} * log(g_bar) + {beta:.3f}")
print(f"Yani k = {10**beta:.3e} * (g_bar)^{alpha:.3f}")

# Orijinal vs Yeni Hata Hesaplamasi
# Ayni siniflardaki galaksilerin hiz egrilerini yukleyelim ve RMS kiyaslayalim.
# Girdiler (Vbar2, F4, vs) ayni klasorden okunmali.
def yukle(klasor):
    sd = os.path.join(KOK, 'SINIF_CALISMASI', klasor)
    kat = {r['Galaksi']: r for r in csv.DictReader(open(os.path.join(sd, 'KATALOG.csv'), encoding='utf-8'))}
    import glob
    out = {}
    for f in sorted(glob.glob(os.path.join(sd, 'veri', '*_rotmod.dat'))):
        ad = os.path.basename(f)[:-11]
        d = np.loadtxt(f)
        R, Vo, eV, Vg, Vd, Vb, SBd, SBb = [d[:, i] for i in range(8)]
        Rp = R * 1e3
        L = lambda S: np.concatenate([[0.0], np.cumsum(np.pi * (Rp[1:] ** 2 - Rp[:-1] ** 2) * 0.5 * (S[1:] + S[:-1]))])
        Vbar2 = np.sign(Vg) * Vg ** 2 + 0.5 * Vd ** 2 + 1.4 * 0.5 * Vb ** 2
        Mgas = np.maximum(R * np.sign(Vg) * Vg ** 2 / G, 0.0)
        Mkaps = 0.5 * L(SBd) + 1.4 * 0.5 * L(SBb) + Mgas
        lom_sabit = np.sqrt(G * max(Mkaps[-1], 1e-6) / A0_SABIT)
        f4_sabit = G * Mkaps / lom_sabit
        out[ad] = dict(Vo=Vo, Vbar2=Vbar2, F4_sabit=f4_sabit)
    return out

print(f"\n--- RMS IYILESTIRME ANALIZI ---")
rms_eski_liste = []
rms_yeni_liste = []

klasor_cache = {}
for d in data:
    kl = d['klasor']
    gname = d['galaksi']
    if kl not in klasor_cache:
        klasor_cache[kl] = yukle(kl)
    gal_veri = klasor_cache[kl].get(gname)
    if gal_veri:
        vo = gal_veri['Vo']
        vb2 = gal_veri['Vbar2']
        f4_eski = gal_veri['F4_sabit']
        
        # Orijinal ongoru (k=1 sabit)
        v_ong_eski = np.sqrt(np.maximum(vb2 + f4_eski, 1e-9))
        rms_eski = np.sqrt(np.mean((v_ong_eski - vo)**2))
        
        # Yeni ongoru (k fonksiyondan)
        k_func = (10**beta) * (d['g_dis'] ** alpha)
        v_ong_yeni = np.sqrt(np.maximum(vb2 + np.sqrt(k_func) * f4_eski, 1e-9))
        rms_yeni = np.sqrt(np.mean((v_ong_yeni - vo)**2))
        
        rms_eski_liste.append(rms_eski)
        rms_yeni_liste.append(rms_yeni)

med_eski = np.median(rms_eski_liste)
med_yeni = np.median(rms_yeni_liste)
print(f"Toplam incelenen guvenilir galaksi (F4 payi > %25): {len(rms_eski_liste)}")
print(f"Sabit a_0 ile elde edilen Medyan RMS: {med_eski:.2f} km/s")
print(f"Degisken a_0(g_bar) fonksiyonu ile Yeni Medyan RMS: {med_yeni:.2f} km/s")
print(f"Hata Oranindaki Iyilesme: %{100*(med_eski-med_yeni)/med_eski:.1f}")

# Grafik cizimi
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(8,6))
ax.scatter(log_g, log_k, color='#ffcc00', alpha=0.7, label='Galaksiler (hesaplanan k)')
xx = np.linspace(log_g.min(), log_g.max(), 50)
yy = alpha * xx + beta
ax.plot(xx, yy, color='#16a34a', lw=2, label=f'Fit: log(k)={alpha:.2f}*log(g)+{beta:.2f}')
ax.set_xlabel('log(Baryonik Ivme) [g_bar_dis]')
ax.set_ylabel('log(a_0 Carpani) [k]')
ax.set_title('a_0 Carpaninin Baryonik Ivmeye Bagimliligi')
ax.legend()
plt.savefig(os.path.join(KOK, 'a0_fonksiyon_testi.png'), dpi=150)
print(f"\nGrafik kaydedildi: a0_fonksiyon_testi.png")
