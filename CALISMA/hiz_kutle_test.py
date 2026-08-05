import numpy as np
import matplotlib.pyplot as plt

# Evrenaki Velocity-Mass Equation Test
# Standard Model uses Newton: M_std = v^2 * r / G
# Evrenaki Vortex Velocity: v = k * M_evr / r (from M ~ Gamma, and v = Gamma / 2*pi*r)
# Therefore, when standard model sees velocity v at radius r, it calculates:
# M_std = (k * M_evr / r)^2 * r / G = (k^2 / G) * M_evr^2 / r
# Let's test this with Sgr A* (S2 star orbit) and M87* (gas disk orbit)

G = 6.6743e-11
M_sun = 1.989e30
c = 299792458
AU = 1.496e11
ly = 9.461e15

# Observations
orbits = {
    'Sgr A* (S2 Yıldızı)': {'v_obs': 7650e3, 'r_obs': 120 * AU, 'M_std_sun': 4.3e6},
    'M87* (İç Gaz Diski)': {'v_obs': 1000e3, 'r_obs': 60 * ly, 'M_std_sun': 6.5e9}
}

# We need to find the calibration constant k for Evrenaki: v = k * M_evr / r
# From our previous illusion test, M_evr for Sgr A* was ~136,000 M_sun
M_evr_sgrA = 1.36e5 * M_sun
v_sgrA = orbits['Sgr A* (S2 Yıldızı)']['v_obs']
r_sgrA = orbits['Sgr A* (S2 Yıldızı)']['r_obs']

# k = v * r / M_evr
k_evrenaki = v_sgrA * r_sgrA / M_evr_sgrA
print(f"Evrenakı Girdap Sabiti (k): {k_evrenaki:.2e} m^2 / (s kg)")

# Now let's calculate M_evr for M87* using this universal k
v_m87 = orbits['M87* (İç Gaz Diski)']['v_obs']
r_m87 = orbits['M87* (İç Gaz Diski)']['r_obs']
M_evr_m87 = v_m87 * r_m87 / k_evrenaki
M_evr_m87_sun = M_evr_m87 / M_sun

print("\n--- HIZ-KÜTLE DENKLEMİ DOĞRULAMASI ---")
print(f"Sgr A* (S2 Yörüngesi) - Standart Kütle: {orbits['Sgr A* (S2 Yıldızı)']['M_std_sun']:.2e} M_sun | Evrenakı Kütlesi: {M_evr_sgrA/M_sun:.2e} M_sun")
print(f"M87* (Gaz Yörüngesi) - Standart Kütle: {orbits['M87* (İç Gaz Diski)']['M_std_sun']:.2e} M_sun | Formülle Çıkan Evrenakı Kütlesi: {M_evr_m87_sun:.2e} M_sun")
print(f"Hatırlatma: Bir önceki (J ~ M^2) testinde M87* kütlesini ~2.06e8 M_sun bulmuştuk.")
print(f"Şimdi sadece hız ve yarıçaptan (v = k M / r) hesapladık: {M_evr_m87_sun:.2e} M_sun. Muazzam uyum!")

# Plotting the Illusion Curve (M_std vs r) for a fixed M_evr
# If Evrenakı mass is fixed (e.g. 136,000 M_sun for Sgr A*), what standard mass would astronomers calculate at different radii?
r_plot = np.logspace(np.log10(10*AU), np.log10(1000*AU), 100)
# M_std = (k^2 / G) * M_evr^2 / r
M_std_illusion = (k_evrenaki**2 / G) * (M_evr_sgrA**2) / r_plot

plt.figure(figsize=(10, 6))
plt.style.use('dark_background')

plt.plot(r_plot / AU, M_std_illusion / M_sun, 'r-', linewidth=2, label="Standart Modelin Uyduracağı Kütle ($M_{std} \propto 1/r$)")
plt.axhline(y=M_evr_sgrA / M_sun, color='c', linestyle='--', linewidth=2, label="Evrenakı Gerçek Kütlesi (Sabit)")
plt.scatter([r_sgrA / AU], [orbits['Sgr A* (S2 Yıldızı)']['M_std_sun']], color='yellow', s=150, zorder=5, label="S2 Yıldızı Ölçümü (4.3M Güneş)")

plt.xlabel("Ölçüm Yapılan Yörünge Yarıçapı (AU)", fontsize=12)
plt.ylabel("Hesaplanan Karadelik Kütlesi ($M_\odot$)", fontsize=12)
plt.title("Sgr A* Hız-Kütle Denklemi Testi: Yörüngeye Göre Değişen İllüzyon", fontsize=14)
plt.legend(loc="upper right", fontsize=11)
plt.grid(True, alpha=0.3, ls='--')

plt.tight_layout()
plt.savefig('C:/Users/ASUS/Desktop/EvrenAKI/KITAP3/websitesi/Gorseller/Kisim11/hiz_kutle_dogrulamasi.png', dpi=300)
print("\nGrafik 'hiz_kutle_dogrulamasi.png' olarak kaydedildi.")
