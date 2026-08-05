import numpy as np
import matplotlib.pyplot as plt

# Constants
M_sun = 1.989e30
c = 299792458
AU = 1.496e11

# Sgr A* Data
r_obs_AU = 120
r_obs_m = r_obs_AU * AU
v_obs_km_s = 7650

# Masses
M_CDM_sun = 4.3e6
M_Evr_sun = 1.36e5

M_CDM_kg = M_CDM_sun * M_sun
M_Evr_kg = M_Evr_sun * M_sun

# Evrenaki Vortex Constant (derived earlier)
k_evr = 5.08e-16

# Radii for plot (from 10 AU to 1000 AU)
r_plot_AU = np.logspace(1, 3, 100)
r_plot_m = r_plot_AU * AU

# Evrenaki orbital velocity formula: v = k * M / r
# 1. Evrenaki Calculation with TRUE (Evrenaki) Mass
v_evr_true_m_s = k_evr * M_Evr_kg / r_plot_m
v_evr_true_km_s = v_evr_true_m_s / 1000

# 2. Evrenaki Calculation with FALSE (CDM) Mass (The Failure / Çuvallama)
v_evr_false_m_s = k_evr * M_CDM_kg / r_plot_m
v_evr_false_km_s = v_evr_false_m_s / 1000

# Let's calculate the specific velocities at S2's radius (120 AU)
v_s2_true = k_evr * M_Evr_kg / r_obs_m / 1000
v_s2_false = k_evr * M_CDM_kg / r_obs_m / 1000

print("--- EVRENAKI'NIN ÇUVALLAMA TESTİ (S2 Yıldızı) ---")
print(f"Gözlemlenen S2 Hızı: {v_obs_km_s:,.0f} km/s")
print(f"1. Evrenakı Formülü + Evrenakı Kütlesi ({M_Evr_sun:,.0f} M_sun) -> Tahmin Edilen Hız: {v_s2_true:,.0f} km/s (BAŞARILI)")
print(f"2. Evrenakı Formülü + CDM Kütlesi ({M_CDM_sun:,.0f} M_sun) -> Tahmin Edilen Hız: {v_s2_false:,.0f} km/s (ÇUVALLADI!)")
print(f"Eğer Evrenakı matematiğinde CDM kütlesi kullanılsaydı, S2 yıldızı ışık hızının %{v_s2_false*1000/c*100:.1f}'i hızında uçuyor olmalıydı!")

plt.figure(figsize=(10, 6))
plt.style.use('dark_background')

plt.plot(r_plot_AU, v_evr_false_km_s, 'r-', linewidth=2, label=f"Evrenakı Formülü + CDM Kütlesi (Uydurma {M_CDM_sun/1e6:.1f}M)\n-> Evrenakı'nın Çuvalladığı Senaryo")
plt.plot(r_plot_AU, v_evr_true_km_s, 'c-', linewidth=2, label=f"Evrenakı Formülü + Evrenakı Kütlesi ({M_Evr_sun/1e3:.0f}K)\n-> Kusursuz Uyum Senaryosu")

# Mark S2 observation
plt.scatter([r_obs_AU], [v_obs_km_s], color='yellow', s=150, zorder=5, label=f'Gerçek S2 Yıldızı Ölçümü ({v_obs_km_s} km/s)')

# Also mark the failed prediction for S2 specifically
plt.scatter([r_obs_AU], [v_s2_false], color='red', marker='x', s=150, zorder=5)
plt.annotate(f"Işık hızının %80'i!\n(İmkansız Hız)", (r_obs_AU, v_s2_false), xytext=(10, -20), textcoords='offset points', color='red')

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Yörünge Yarıçapı (AU)', fontsize=12)
plt.ylabel('Yörünge Hızı (km/s)', fontsize=12)
plt.title("Paradigma Tutarlılığı: Evrenakı Denklemlerinde CDM Kütlesi Kullanılamaz", fontsize=14)
plt.legend(loc='upper right', fontsize=10)
plt.grid(True, alpha=0.3, ls='--')

plt.tight_layout()
plt.savefig('C:/Users/ASUS/Desktop/EvrenAKI/KITAP3/websitesi/Gorseller/Kisim11/evrenaki_cuvallama_testi.png', dpi=300)
print("\nGrafik 'evrenaki_cuvallama_testi.png' olarak kaydedildi.")
