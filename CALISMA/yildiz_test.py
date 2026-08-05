import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Star Data from Fukuda (1982) / Glebocki & Gnacinski (2005)
# M: Mass (Solar Masses), R: Radius (Solar Radii), v: Average equatorial velocity (km/s)
# Note: measured v is usually <v sin i>, so real v_eq is about 4/pi (~1.27) times higher.
# Here we use approximate true v_eq values by multiplying the table values by 1.25.
# M_sun = 1.989e30 kg, R_sun = 6.957e8 m

stars = {
    'O5': {'M': 40.0, 'R': 12.0, 'v': 190 * 1.25, 'type': 'Radyatif (Kapalı)'},
    'B0': {'M': 16.0, 'R': 7.4, 'v': 200 * 1.25, 'type': 'Radyatif (Kapalı)'},
    'B5': {'M': 5.9, 'R': 3.9, 'v': 220 * 1.25, 'type': 'Radyatif (Kapalı)'},
    'A0': {'M': 2.9, 'R': 2.4, 'v': 180 * 1.25, 'type': 'Radyatif (Kapalı)'},
    'A5': {'M': 2.0, 'R': 1.7, 'v': 150 * 1.25, 'type': 'Radyatif (Kapalı)'},
    'F0': {'M': 1.6, 'R': 1.5, 'v': 100 * 1.25, 'type': 'Radyatif (Kapalı)'},
    # Kraft Break happens around F5 (1.3 M_sun)
    'F5': {'M': 1.3, 'R': 1.3, 'v': 30 * 1.25, 'type': 'Konvektif (Açık)'},
    'G0': {'M': 1.05, 'R': 1.1, 'v': 8 * 1.25, 'type': 'Konvektif (Açık)'},
    'Güneş (G2)': {'M': 1.0, 'R': 1.0, 'v': 2.0, 'type': 'Konvektif (Açık)'}, # Sun is exactly 2 km/s at equator
    'K0': {'M': 0.85, 'R': 0.85, 'v': 2.5, 'type': 'Konvektif (Açık)'},
    'M0': {'M': 0.5, 'R': 0.6, 'v': 2.0, 'type': 'Konvektif (Açık)'}
}

M_sun = 1.989e30
R_sun = 6.957e8
lam = 0.07 # typical moment of inertia factor for main sequence stars (polytrope n=3 is ~0.076)

names = []
masses = []
Js = []
periods_hr = []
types = []

print(f"{'Yıldız':<12} | {'Kütle (M_gunes)':<15} | {'Dönüş (saat)':<15} | {'J (kg m^2/s)':<15} | {'Zarf'}")
print("-" * 80)

fast_masses = []
fast_Js = []

for name, data in stars.items():
    M_kg = data['M'] * M_sun
    R_m = data['R'] * R_sun
    v_m_s = data['v'] * 1000
    
    T_s = 2 * np.pi * R_m / v_m_s
    T_hr = T_s / 3600
    
    omega = 2 * np.pi / T_s
    I = lam * M_kg * R_m**2
    J = I * omega
    
    names.append(name)
    masses.append(M_kg)
    Js.append(J)
    periods_hr.append(T_hr)
    types.append(data['type'])
    
    print(f"{name:<12} | {data['M']:<10.2f} | {T_hr:<15.1f} | {J:<15.3e} | {data['type']}")
    
    if data['type'] == 'Radyatif (Kapalı)':
        fast_masses.append(M_kg)
        fast_Js.append(J)

# Fit for radiative stars (O, B, A, F0)
fast_masses = np.array(fast_masses)
fast_Js = np.array(fast_Js)
slope_fast, intercept_fast, r_value_fast, _, _ = linregress(np.log10(fast_masses), np.log10(fast_Js))

print("\n--- FIT SONUÇLARI (Radyatif Yıldızlar - F0 ve üstü) ---")
print(f"Hızlı Dönen Yıldızlar Üssü: {slope_fast:.3f} (R^2 = {r_value_fast**2:.3f})")
# Because stars don't have constant density (radius roughly scales with mass directly for main sequence, R ~ M^0.8 for upper main sequence)
# If R ~ M^0.8, then I ~ M * M^1.6 = M^2.6. And J = I * omega. If omega is constant, J ~ M^2.6.
# Let's see what the slope actually is!

plt.figure(figsize=(12, 7))
plt.style.use('dark_background')

masses = np.array(masses)
Js = np.array(Js)

for i in range(len(names)):
    color = 'cyan' if types[i] == 'Radyatif (Kapalı)' else 'red'
    marker = 'o' if types[i] == 'Radyatif (Kapalı)' else 's'
    label_txt = 'Radyatif (Zarf Kapalı)' if i == 0 else ('Konvektif (Zarf Açık - Frenli)' if names[i] == 'F5' else "")
    
    if label_txt:
        plt.scatter(masses[i], Js[i], color=color, s=100, marker=marker, label=label_txt)
    else:
        plt.scatter(masses[i], Js[i], color=color, s=100, marker=marker)
        
    plt.annotate(f"{names[i]}\n({periods_hr[i]:.1f} sa)", (masses[i], Js[i]), 
                 xytext=(10, -10), textcoords='offset points', color='white', fontsize=9)

x_fit = np.logspace(np.log10(min(masses)), np.log10(max(masses)), 100)
y_fast = (10**intercept_fast) * (x_fit**slope_fast)
plt.plot(x_fit, y_fast, 'c--', label=f'Radyatif Fit: J $\propto$ M^{slope_fast:.2f}')

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Kütle ($M$, kg)', fontsize=14)
plt.ylabel('Açısal Momentum ($J$, kg m$^2$/s)', fontsize=14)
plt.title('Yıldızlar: Kütle - Spin Testi ve Kraft Kırılması', fontsize=16)
plt.grid(True, which="both", ls="--", alpha=0.3)
plt.legend(loc='lower right', fontsize=12)

plt.tight_layout()
plt.savefig('C:/Users/ASUS/Desktop/EvrenAKI/KITAP3/websitesi/Gorseller/Kisim11/yildiz_testi.png', dpi=300)
print("\nGrafik 'yildiz_testi.png' olarak kaydedildi.")
