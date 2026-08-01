import numpy as np
import matplotlib.pyplot as plt
import os

KOK = os.path.dirname(os.path.abspath(__file__))

# Sabitler
G = 6.67430e-11 # m^3 kg^-1 s^-2
M_sun = 1.989e30 # kg
AU = 1.496e11 # m (1 Astronomical Unit in meters)

# Gezegen Uzakliklari (AU cinsinden)
gezegenler = {
    'Merkur': 0.387,
    'Venus': 0.723,
    'Dunya': 1.000,
    'Mars': 1.524,
    'Jupiter': 5.203,
    'Saturn': 9.537,
    'Uranus': 19.191,
    'Neptun': 30.069
}
isimler = list(gezegenler.keys())
R_au = np.array(list(gezegenler.values()))
R_m = R_au * AU

# 1. Gercek Hesap (Sadece Gunes - Keplerian)
# v = sqrt(G * M_sun / R)
v_real = np.sqrt(G * M_sun / R_m) / 1000.0 # km/s

# 2. Karanlik Madde Eklenmis Hesap
# Samanyolu'nun Gunes civarindaki karanlik madde yogunlugu:
# rho_DM ~ 0.3 GeV/cm^3 = 0.008 M_sun / pc^3
# 1 M_sun = 1.989e30 kg
# 1 pc = 3.086e16 m
rho_DM = 0.008 * M_sun / (3.086e16)**3 # kg / m^3
# ~ 5.4e-22 kg/m^3

# Gunes Sistemine karanlik maddenin "galaksilerdeki dagilimi" olan NFW halesini uyguluyoruz.
# Gunes sisteminin boyutu bir galaksi halesi yaninda mikroskobik oldugu icin yogunluk sabittir.
# R yaricapindaki toplam karanlik madde kutlesi = Hacim * Yogunluk
M_dm = (4/3) * np.pi * (R_m**3) * rho_DM

# Toplam kapsanan kutle = Gunes + Karanlik Madde
M_enc = M_sun + M_dm
v_dm = np.sqrt(G * M_enc / R_m) / 1000.0 # km/s

# Farki inceleyelim
fark_km = v_dm - v_real
fark_yuzde = (fark_km / v_real) * 100

print(f"{'Gezegen':<10} | {'Uzaklik(AU)':<12} | {'V_Gercek(km/s)':<15} | {'V_KaranlikMadde':<15} | {'Fark(km/s)':<15}")
print("-" * 75)
for i in range(len(isimler)):
    print(f"{isimler[i]:<10} | {R_au[i]:<12.3f} | {v_real[i]:<15.3f} | {v_dm[i]:<15.3f} | {fark_km[i]:.3e}")

# Grafik Cizimi
plt.style.use('dark_background')
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), gridspec_kw={'height_ratios': [3, 1]})

# Ust Grafik: Hizlar
ax1.plot(R_au, v_real, 'o-', color='#3b82f6', label='Gercek (Yalnizca Gunes)', linewidth=2, markersize=8)
ax1.plot(R_au, v_dm, 'x--', color='#ef4444', label='Standart Bilim (Gunes + Karanlik Madde)', linewidth=2, markersize=8)

for i, txt in enumerate(isimler):
    ax1.annotate(txt, (R_au[i], v_real[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

ax1.set_title('Gunes Sistemi Yorunge Hizlari: Gercek vs Karanlik Madde', fontsize=14)
ax1.set_ylabel('Yorunge Hizi (km/s)', fontsize=12)
ax1.legend(fontsize=11)
ax1.grid(True, alpha=0.2)

# Alt Grafik: Farki Gosteren Zoom (Cunku ust uste biniyorlar)
ax2.plot(R_au, fark_km, 'o-', color='#22c55e', linewidth=2)
ax2.set_xlabel('Gunes\'e Uzaklik (AU)', fontsize=12)
ax2.set_ylabel('Hiz Farki (km/s)', fontsize=10)
ax2.set_title('Karanlik Maddenin Hizda Yarattigi Artis (km/s)', fontsize=11)
ax2.grid(True, alpha=0.2)

plt.tight_layout()
plt.savefig(os.path.join(KOK, 'gunes_sistemi_dm_testi.png'), dpi=150)
print("\nGrafik kaydedildi: gunes_sistemi_dm_testi.png")
