import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Planetary Data
# M: Mass (kg), R: Radius (m), T: Spin Period (s), lambda: Moment of inertia factor (I/MR^2)
planets = {
    'Merkür': {'M': 3.3011e23, 'R': 2439.7e3, 'T': 58.646 * 86400, 'lambda': 0.33},
    'Venüs': {'M': 4.8675e24, 'R': 6051.8e3, 'T': -243.025 * 86400, 'lambda': 0.33},
    'Dünya': {'M': 5.972e24, 'R': 6371e3, 'T': 0.997269 * 86400, 'lambda': 0.3307},
    'Mars': {'M': 6.4171e23, 'R': 3389.5e3, 'T': 1.025957 * 86400, 'lambda': 0.366},
    'Jüpiter': {'M': 1.8982e27, 'R': 69911e3, 'T': 0.41354 * 86400, 'lambda': 0.254},
    'Satürn': {'M': 5.6834e26, 'R': 58232e3, 'T': 0.44401 * 86400, 'lambda': 0.210},
    'Uranüs': {'M': 8.6810e25, 'R': 25362e3, 'T': -0.71833 * 86400, 'lambda': 0.23},
    'Neptün': {'M': 1.0241e26, 'R': 24622e3, 'T': 0.67125 * 86400, 'lambda': 0.23}
}

names = []
masses = []
Js = []

print(f"{'Gezegen':<10} | {'Kütle (kg)':<15} | {'J (kg m^2/s)':<15}")
print("-" * 45)

for name, data in planets.items():
    # Exclude Mercury and Venus since they are tidally locked/anomalous extremely slow rotators
    # Wait, let's include them but maybe separate them in the fit
    M = data['M']
    R = data['R']
    T = abs(data['T']) # absolute value for magnitude of J
    lam = data['lambda']
    
    I = lam * M * R**2
    omega = 2 * np.pi / T
    J = I * omega
    
    names.append(name)
    masses.append(M)
    Js.append(J)
    print(f"{name:<10} | {M:<15.3e} | {J:<15.3e}")

masses = np.array(masses)
Js = np.array(Js)

# Fit for all 8 planets
log_M = np.log10(masses)
log_J = np.log10(Js)
slope_all, intercept_all, r_value_all, _, _ = linregress(log_M, log_J)

# Fit for fast rotators only (Earth, Mars, Jupiter, Saturn, Uranus, Neptune)
# Excluding Mercury and Venus due to tidal locking to the Sun
fast_idx = [2, 3, 4, 5, 6, 7]
fast_M = masses[fast_idx]
fast_J = Js[fast_idx]

slope_fast, intercept_fast, r_value_fast, _, _ = linregress(np.log10(fast_M), np.log10(fast_J))

print("\n--- FIT SONUÇLARI ---")
print(f"Tüm Gezegenler Üssü: {slope_all:.3f} (R^2 = {r_value_all**2:.3f})")
print(f"Hızlı Dönenler Üssü (Merkür/Venüs hariç): {slope_fast:.3f} (R^2 = {r_value_fast**2:.3f})")

# Theoretical relation: J ~ M^(5/3) = M^1.667
# Let's see if 5/3 is a good fit

plt.figure(figsize=(10, 6))
plt.style.use('dark_background')

# Scatter
plt.scatter(fast_M, fast_J, color='cyan', s=100, label='Hızlı Dönen Gezegenler (Serbest)')
plt.scatter(masses[0:2], Js[0:2], color='red', s=100, label='Güneş\'e Kilitli (Merkür/Venüs)')

# Fits
x_fit = np.logspace(23, 28, 100)
# Empirical fast fit
y_fast = (10**intercept_fast) * (x_fit**slope_fast)
plt.plot(x_fit, y_fast, 'c--', label=f'Deneysel Fit: J $\propto$ M^{slope_fast:.2f}')

# Theoretical 5/3 fit (pinned to Earth)
earth_M = planets['Dünya']['M']
earth_J = planets['Dünya']['lambda'] * earth_M * planets['Dünya']['R']**2 * (2 * np.pi / planets['Dünya']['T'])
const_53 = earth_J / (earth_M**(5/3))
y_53 = const_53 * (x_fit**(5/3))
plt.plot(x_fit, y_53, 'y-', linewidth=2, label=f'Teorik Evrenakı Limiti: J $\propto$ M^5/3')

# Annotations
for i, txt in enumerate(names):
    plt.annotate(txt, (masses[i], Js[i]), xytext=(10, -5), textcoords='offset points', color='white', fontsize=10)

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Kütle ($M$, kg)', fontsize=14)
plt.ylabel('Açısal Momentum ($J$, kg m$^2$/s)', fontsize=14)
plt.title('Güneş Sistemi Gezegenleri: Kütle - Spin Testi', fontsize=16)
plt.grid(True, which="both", ls="--", alpha=0.3)
plt.legend(loc='lower right', fontsize=12)

plt.tight_layout()
plt.savefig('C:/Users/ASUS/Desktop/EvrenAKI/KITAP3/websitesi/Gorseller/Kisim11/gezegen_testi.png', dpi=300)
print("\nGrafik 'gezegen_testi.png' olarak kaydedildi.")
