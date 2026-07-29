import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

plt.style.use('dark_background')

# --- Cüce Küresel (Dwarf Spheroidal) Galaksi Efektif Yörünge Hızı Verileri ---
# Örnek: Fornax Cüce Küresel Galaksisi
# Cüce küreseller, karanlık maddenin evrende en yoğun olduğu düşünülen yerlerdir.
# Yarıçapları çok küçüktür (1-2 kpc) ama hız dağılımları (efektif hız) düz kalır.
r_obs = np.array([0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6]) # kpc
v_obs = np.array([15, 17, 18, 18.5, 18, 18.5, 18, 17.5]) # km/s (Efektif Dairesel Hız Vc)

v_err = np.random.uniform(1, 2, len(v_obs))

# Modeller
def model_newton(r, A):
    return np.sqrt(A / r)

# Küresel olduğu için eksenel kuvvet (B) sıfırdır. 
# Hızın düz kalmasının sebebi artan kütle dağılımıdır (A(r) orantılıdır r ile).
def model_evrenaki(r, A_const):
    return np.full_like(r, A_const)

# Fit
popt_newton, _ = curve_fit(model_newton, r_obs, v_obs, p0=[100])
popt_evrenaki, _ = curve_fit(model_evrenaki, r_obs, v_obs, p0=[18])

# Çizim
r_plot = np.linspace(0.1, 2.0, 200)

fig = plt.figure(figsize=(10, 6), facecolor='#121212')
ax = fig.add_subplot(111)
ax.set_facecolor('#121212')

plt.errorbar(r_obs, v_obs, yerr=v_err, fmt='o', color='#ffff00', label='Fornax Cüce Küresel Efektif Hız Verisi', capsize=4, zorder=5)

plt.plot(r_plot, model_newton(r_plot, *popt_newton), label='Klasik Çekim Fit ($v = \\sqrt{A/r}$)', color='#ff5555', linestyle='--', linewidth=2)
plt.plot(r_plot, model_evrenaki(r_plot, *popt_evrenaki), label='Evrenakı (Artan Kütle Dağılımı B=0)', color='#55aaff', linewidth=2.5)

plt.title('Cüce Küresel Galaksi (Fornax) Kütleçekim Potansiyeli Testi', fontsize=14, pad=15, color='white')
plt.xlabel('Merkezden Uzaklık - r (kpc)', fontsize=12, color='#cccccc')
plt.ylabel('Efektif Dairesel Hız - Vc (km/s)', fontsize=12, color='#cccccc')

ax.spines['bottom'].set_color('#444444')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#444444')
ax.tick_params(axis='x', colors='#aaaaaa')
ax.tick_params(axis='y', colors='#aaaaaa')
plt.grid(True, alpha=0.15, color='white')

plt.xlim(0, 2.0)
plt.ylim(0, 25)

legend = plt.legend(fontsize=12, facecolor='#1a1a1a', edgecolor='#333333', loc='lower right')
for text in legend.get_texts():
    text.set_color("white")

plt.tight_layout()
plt.savefig('fornax_kuresel_testi.png', dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
print("Grafik 'fornax_kuresel_testi.png' olarak kaydedildi.")
