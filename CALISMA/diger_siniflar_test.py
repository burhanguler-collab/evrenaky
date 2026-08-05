import numpy as np
import matplotlib.pyplot as plt

# Data for Brown Dwarfs, White Dwarfs, and Asteroids/Dwarf Planets
# M: Mass (kg), R: Radius (m), T: Spin Period (hours), lambda: Moment of inertia factor

# Constants
M_J = 1.898e27
R_J = 69911e3
M_sun = 1.989e30
R_earth = 6371e3
R_sun = 6.957e8

objects = {
    'Ceres (Asteroit)': {'M': 9.38e20, 'R': 473e3, 'T': 9.07, 'lambda': 0.33, 'type': 'Katı/Kaya'},
    'Vesta (Asteroit)': {'M': 2.59e20, 'R': 262e3, 'T': 5.34, 'lambda': 0.33, 'type': 'Katı/Kaya'},
    'Haumea (Cüce Gz.)': {'M': 4.01e21, 'R': 816e3, 'T': 3.92, 'lambda': 0.33, 'type': 'Katı/Kaya'},
    'Eris (Cüce Gz.)': {'M': 1.66e22, 'R': 1163e3, 'T': 25.9, 'lambda': 0.33, 'type': 'Katı/Kaya'},
    
    'Luhman 16A (Kahv. Cüce)': {'M': 33.5 * M_J, 'R': 0.9 * R_J, 'T': 5.05, 'lambda': 0.25, 'type': 'Gaz/Bozunmuş'},
    'Luhman 16B (Kahv. Cüce)': {'M': 28.6 * M_J, 'R': 0.9 * R_J, 'T': 2.5, 'lambda': 0.25, 'type': 'Gaz/Bozunmuş'},
    '2M1207 (Kahv. Cüce)': {'M': 25.0 * M_J, 'R': 1.0 * R_J, 'T': 10.7, 'lambda': 0.25, 'type': 'Gaz/Bozunmuş'},
    'Trappist-1 (Kırmızı Cüce)': {'M': 0.089 * M_sun, 'R': 0.121 * R_sun, 'T': 79.2, 'lambda': 0.07, 'type': 'Konvektif'}, # Very low mass star, convective
    
    'Sirius B (Beyaz Cüce)': {'M': 1.02 * M_sun, 'R': 0.0084 * R_sun, 'T': 5.5, 'lambda': 0.4, 'type': 'Kompakt'},
    '40 Eri B (Beyaz Cüce)': {'M': 0.50 * M_sun, 'R': 0.014 * R_sun, 'T': 32.4, 'lambda': 0.4, 'type': 'Kompakt'}
}
# R_sun needs to be defined
R_sun = 6.957e8
# Fix missing variable in dictionary
objects['Trappist-1 (Kırmızı Cüce)']['R'] = 0.121 * R_sun
objects['Sirius B (Beyaz Cüce)']['R'] = 0.0084 * R_sun
objects['40 Eri B (Beyaz Cüce)']['R'] = 0.014 * R_sun

names = []
masses = []
Js = []
periods = []
types = []

print(f"{'Gök Cismi':<25} | {'Kütle (kg)':<12} | {'Dönüş (saat)':<12} | {'J (kg m^2/s)':<15} | {'Sınıf'}")
print("-" * 85)

for name, data in objects.items():
    M = data['M']
    R = data['R']
    T_hr = data['T']
    lam = data['lambda']
    typ = data['type']
    
    T_s = T_hr * 3600
    omega = 2 * np.pi / T_s
    I = lam * M * R**2
    J = I * omega
    
    names.append(name)
    masses.append(M)
    Js.append(J)
    periods.append(T_hr)
    types.append(typ)
    
    print(f"{name:<25} | {M:<12.2e} | {T_hr:<12.1f} | {J:<15.3e} | {typ}")

# We will plot these along with the Earth and Jupiter to see where they fall on the J vs M graph

plt.figure(figsize=(12, 7))
plt.style.use('dark_background')

colors = {'Katı/Kaya': 'gray', 'Gaz/Bozunmuş': 'orange', 'Konvektif': 'red', 'Kompakt': 'purple'}
markers = {'Katı/Kaya': '^', 'Gaz/Bozunmuş': 'o', 'Konvektif': 's', 'Kompakt': 'D'}

for i in range(len(names)):
    plt.scatter(masses[i], Js[i], color=colors[types[i]], s=100, marker=markers[types[i]])
    plt.annotate(f"{names[i]}\n({periods[i]:.1f} sa)", (masses[i], Js[i]), 
                 xytext=(8, -8), textcoords='offset points', color='white', fontsize=9)

# Add reference planets
earth_M = 5.972e24
earth_J = 5.846e33
jup_M = 1.898e27
jup_J = 4.144e38
sun_M = 1.989e30
sun_J = 1.937e41 # Sun is convective, drops down

plt.scatter(earth_M, earth_J, color='cyan', s=100, marker='o', label='Dünya (24 sa)')
plt.scatter(jup_M, jup_J, color='cyan', s=100, marker='o', label='Jüpiter (9.9 sa)')

# Draw the theoretical line J ~ M^(5/3) passing through Earth
x_fit = np.logspace(20, 31, 100)
const_53 = earth_J / (earth_M**(5/3))
y_53 = const_53 * (x_fit**(5/3))
plt.plot(x_fit, y_53, 'y-', linewidth=2, label=f'Teorik Evrenakı Limiti: J $\propto$ M^(5/3)')

# Draw the empirical fast line J ~ M^1.87
const_187 = earth_J / (earth_M**1.87)
y_187 = const_187 * (x_fit**1.87)
plt.plot(x_fit, y_187, 'c--', linewidth=2, label=f'Gezegen-Kahverengi Cüce Fiti: J $\propto$ M^1.87')


plt.xscale('log')
plt.yscale('log')
plt.xlabel('Kütle ($M$, kg)', fontsize=14)
plt.ylabel('Açısal Momentum ($J$, kg m$^2$/s)', fontsize=14)
plt.title('Gözden Kaçan Sınıflar: Asteroitler, Kahverengi ve Beyaz Cüceler', fontsize=16)
plt.grid(True, which="both", ls="--", alpha=0.3)

# Custom legend
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='^', color='w', markerfacecolor='gray', markersize=10, label='Asteroitler (Katı)'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='orange', markersize=10, label='Kahverengi Cüceler'),
    Line2D([0], [0], marker='s', color='w', markerfacecolor='red', markersize=10, label='Kırmızı Cüce (Konvektif)'),
    Line2D([0], [0], marker='D', color='w', markerfacecolor='purple', markersize=10, label='Beyaz Cüceler (Kompakt)'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='cyan', markersize=10, label='Referans Gezegenler')
]
plt.legend(handles=legend_elements, loc='lower right', fontsize=11)

plt.tight_layout()
plt.savefig('C:/Users/ASUS/Desktop/EvrenAKI/KITAP3/websitesi/Gorseller/Kisim11/diger_siniflar.png', dpi=300)
print("\nGrafik 'diger_siniflar.png' olarak kaydedildi.")
