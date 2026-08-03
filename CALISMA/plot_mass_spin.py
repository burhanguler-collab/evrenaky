import matplotlib.pyplot as plt
import numpy as np

# Data (Mass in Solar Masses, Specific Angular Momentum j in m^2/s)
# 1 Solar Mass = 1.989e30 kg
M_sun = 1.989e30

# Planets (scaled to Solar Masses for X axis, j in m^2/s)
# Earth: M=3e-6 M_sun, j = 1.16e9
# Jupiter: M=9.5e-4 M_sun, j = 2.1e11
# Saturn: M=2.8e-4 M_sun, j = 1.6e11
# Exoplanet (Beta Pic b): M=0.011 M_sun, j = 2.5e12
planets_M = [3.0e-6, 9.5e-4, 2.8e-4, 1.1e-2]
planets_j = [1.16e9, 2.1e11, 1.6e11, 2.5e12]
planets_labels = ['Dünya', 'Jüpiter', 'Satürn', 'Beta Pic b (Ötegezegen)']

# Stars
# Sun: M=1 M_sun, j = 9.5e10 (Spun down)
# Altair (Fast rotator): M=1.8, j = 3e14
# Kraft relation average (approx j ~ M^0.67 for high mass)
stars_M = [1.0, 1.8, 2.5, 5.0]
stars_j = [9.5e10, 3e14, 8e14, 3e15]
stars_labels = ['Güneş', 'Altair', 'B-Tipi Anakol', 'O-Tipi Anakol']

# Neutron Stars
# Crab: M=1.4, j = 1.5e10
# Millisecond Pulsar: M=1.4, j = 3e11
ns_M = [1.4, 1.4]
ns_j = [1.5e10, 3e11]
ns_labels = ['Crab Pulsarı', 'Milisaniye Pulsarı']

# Black Holes (j = a* G M / c)
# G = 6.674e-11, c = 2.998e8 => G/c = 2.226e-19
# j_BH = a* * (G/c) * M_kg = a* * 2.226e-19 * M_sun * M_sm = a* * 4.43e11 * M_sm
# Let's assume near maximal spin a* = 0.9 for these examples
# Cygnus X-1: M=21 M_sun -> j = 0.9 * 4.43e11 * 21 = 8.3e12
# Sgr A*: M=4.1e6 M_sun -> j = 0.9 * 4.43e11 * 4.1e6 = 1.6e18
# M87*: M=6.5e9 M_sun -> j = 0.9 * 4.43e11 * 6.5e9 = 2.6e21
bh_M = [21, 4.1e6, 6.5e9]
bh_j = [8.3e12, 1.6e18, 2.6e21]
bh_labels = ['Cygnus X-1', 'Sgr A*', 'M87*']

# Setup plot
plt.figure(figsize=(12, 8))
plt.style.use('dark_background')

# Plot lines for theoretical limits
M_range = np.logspace(-6, 11, 100)
# Black Hole Limit (Kerr limit a*=1): j = G M / c -> j = 4.43e11 * M_sm
j_bh_limit = 4.43e11 * M_range
plt.plot(M_range, j_bh_limit, 'w--', alpha=0.5, label='Kerr Limiti (a*=1)')

# Planets/Stars Volume scaling relation (empirical J ~ M^5/3 -> j ~ M^2/3)
# To fit Jupiter (M=9.5e-4, j=2.1e11): Constant C ~ 2.1e11 / (9.5e-4)^(2/3) ~ 2.1e11 / 0.0096 ~ 2.1e13
j_planet_limit = 2.1e13 * (M_range**(2/3))
plt.plot(M_range, j_planet_limit, 'c--', alpha=0.5, label='Zarf Ölçeklenmesi (j ∝ M^2/3)')

# Plot data points
plt.scatter(planets_M, planets_j, color='cyan', s=100, label='Gezegenler ve Ötegezegenler', zorder=5, edgecolors='w')
plt.scatter(stars_M, stars_j, color='yellow', s=100, label='Yıldızlar (Zarflı)', zorder=5, edgecolors='w')
plt.scatter(ns_M, ns_j, color='magenta', s=100, label='Nötron Yıldızları (Frenlenmiş)', zorder=5, marker='s', edgecolors='w')
plt.scatter(bh_M, bh_j, color='red', s=100, label='Karadelikler (Nokta Kütle)', zorder=5, marker='*', edgecolors='w')

# Annotations
for i, txt in enumerate(planets_labels):
    plt.annotate(txt, (planets_M[i], planets_j[i]), xytext=(10, -5), textcoords='offset points', color='cyan', fontsize=9)

for i, txt in enumerate(stars_labels):
    plt.annotate(txt, (stars_M[i], stars_j[i]), xytext=(10, -5), textcoords='offset points', color='yellow', fontsize=9)

for i, txt in enumerate(ns_labels):
    plt.annotate(txt, (ns_M[i], ns_j[i]), xytext=(10, 5), textcoords='offset points', color='magenta', fontsize=9)

for i, txt in enumerate(bh_labels):
    plt.annotate(txt, (bh_M[i], bh_j[i]), xytext=(15, -5), textcoords='offset points', color='red', fontsize=9)

# Axis labels and scale
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Kütle (Güneş Kütlesi, $M_\odot$)', fontsize=14, color='white')
plt.ylabel('Özgül Açısal Momentum, $j$ (m$^2$/s)', fontsize=14, color='white')
plt.title('Gök Cisimlerinde Kütle - Spin İlişkisi ve Zarf Durumu', fontsize=16, color='white')
plt.grid(True, which="both", ls="-", alpha=0.2)
plt.legend(loc='lower right', fontsize=12)

plt.tight_layout()
plt.savefig('C:/Users/ASUS/Desktop/EvrenAKI/KITAP3/websitesi/Gorseller/Kisim11/kutle_spin_grafik.png', dpi=300)
print('Grafik başarıyla oluşturuldu.')
