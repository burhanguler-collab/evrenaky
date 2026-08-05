import numpy as np
import matplotlib.pyplot as plt

# Constants
M_sun = 1.989e30
G = 6.6743e-11
c = 299792458
Kerr_coeff = G / c # ~ 2.22e-19
Evrenaki_coeff = 2.0e-16 # A0 from the planet line (J = A0 * M^2)

# Black Hole Data: Standard Mass (M_sun) and a* (dimensionless spin)
bh_data = {
    'A0620-00 (Stellar)': {'M_std_sun': 6.6, 'a': 0.12},
    'LMC X-1 (Stellar)': {'M_std_sun': 10.9, 'a': 0.92},
    'Cyg X-1 (Stellar)': {'M_std_sun': 21.2, 'a': 0.99},
    'GW150914 (Merger)': {'M_std_sun': 62.0, 'a': 0.67},
    'GW190521 (Merger)': {'M_std_sun': 142.0, 'a': 0.72},
    'Sgr A* (SMBH)': {'M_std_sun': 4.3e6, 'a': 0.90}, # a* estimated around 0.9
    'M87* (SMBH)': {'M_std_sun': 6.5e9, 'a': 0.90}
}

names = []
M_std = []
M_evr = []
J_obs = []

print(f"{'Karadelik Adı':<20} | {'Standart Kütle (M_sun)':<22} | {'Evrenakı Kütlesi (M_sun)':<25} | {'Fark (Kat)':<10}")
print("-" * 85)

for name, data in bh_data.items():
    mass_kg = data['M_std_sun'] * M_sun
    a_star = data['a']
    
    # Calculate J based on standard Kerr metric formula J = a * (G/c) * M^2
    J = a_star * Kerr_coeff * (mass_kg**2)
    
    # Calculate Evrenaki Mass assuming the object is actually following the Zarf Kilidi (J = A0 * M^2)
    # M_evr = sqrt(J / Evrenaki_coeff)
    mass_evr_kg = np.sqrt(J / Evrenaki_coeff)
    mass_evr_sun = mass_evr_kg / M_sun
    
    ratio = data['M_std_sun'] / mass_evr_sun
    
    names.append(name)
    M_std.append(data['M_std_sun'])
    M_evr.append(mass_evr_sun)
    J_obs.append(J)
    
    print(f"{name:<20} | {data['M_std_sun']:<22.2e} | {mass_evr_sun:<25.2e} | {ratio:<10.1f}")

# Plotting the comparison
plt.figure(figsize=(10, 6))
plt.style.use('dark_background')

# X axis: Standard Mass
# Y axis: Mass
x = np.array(M_std)
y_std = np.array(M_std)
y_evr = np.array(M_evr)

plt.plot(x, y_std, 'r-o', label='Standart Model Kütlesi (Kerr Uydurması)', linewidth=2)
plt.plot(x, y_evr, 'c-s', label='Evrenakı Zarf Kilidi Gerçek Kütlesi (~30 Kat Daha Hafif)', linewidth=2)

for i in range(len(names)):
    plt.vlines(x[i], ymin=y_evr[i], ymax=y_std[i], color='gray', linestyle='--', alpha=0.5)
    plt.annotate(names[i], (x[i], y_std[i]), xytext=(-10, 10), textcoords='offset points', color='white', fontsize=9, rotation=45)

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Ölçülen (Standart) Kütle ($M_\odot$)', fontsize=12)
plt.ylabel('Kütle Karşılaştırması ($M_\odot$)', fontsize=12)
plt.title('Karadelik Kütle İllüzyonu: Standart Model vs Evrenakı', fontsize=14)
plt.grid(True, which="both", ls="--", alpha=0.3)
plt.legend(loc='upper left', fontsize=11)

plt.tight_layout()
plt.savefig('C:/Users/ASUS/Desktop/EvrenAKI/KITAP3/websitesi/Gorseller/Kisim11/karadelik_illuzyon.png', dpi=300)
print("\nGrafik 'karadelik_illuzyon.png' olarak kaydedildi.")
