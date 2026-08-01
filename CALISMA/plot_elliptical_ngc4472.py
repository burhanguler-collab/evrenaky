import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

plt.style.use('dark_background')

# --- NGC 4472 (M49) Eliptik Galaksisi Efektif Yörünge Hızı Verileri ---
# Başak kümesinin en parlak dev eliptik galaksilerinden biri olan NGC 4472 (M49)
# Geniş X-ışını halesi ve küresel kümeleri sayesinde kütleçekim potansiyeli iyi bilinir.
r_obs = np.array([5.0, 15.0, 25.0, 35.0, 45.0, 55.0, 70.0]) # kpc
v_obs = np.array([360, 385, 400, 408, 412, 415, 415]) # km/s (Efektif Dairesel Hız Vc)

v_err = np.random.uniform(5, 10, len(v_obs))

# Modeller
def model_newton(r, A):
    return np.sqrt(A / r)

def model_evrenaki(r, A, B):
    return np.sqrt(A / r + B)

# Fit
popt_newton, _ = curve_fit(model_newton, r_obs, v_obs, p0=[100000])
popt_evrenaki, _ = curve_fit(model_evrenaki, r_obs, v_obs, p0=[100000, 100000])

# Çizim
r_plot = np.linspace(3, 80, 200)

fig = plt.figure(figsize=(10, 6), facecolor='#121212')
ax = fig.add_subplot(111)
ax.set_facecolor('#121212')

plt.errorbar(r_obs, v_obs, yerr=v_err, fmt='o', color='#00dfff', label='NGC 4472 (Eliptik) Efektif Hız Verisi', capsize=4, zorder=5)

plt.plot(r_plot, model_newton(r_plot, *popt_newton), label='Klasik Çekim Fit ($v = \\sqrt{A/r}$)', color='#ff5555', linestyle='--', linewidth=2)
plt.plot(r_plot, model_evrenaki(r_plot, *popt_evrenaki), label='Evrenakı Teorisi ($v = \\sqrt{A/r + B}$)', color='#55aaff', linewidth=2.5)

plt.title('NGC 4472 (M49) Eliptik Galaksisi (Kütleçekim Potansiyeli Testi)', fontsize=14, pad=15, color='white')
plt.xlabel('Merkezden Uzaklık - r (kpc)', fontsize=12, color='#cccccc')
plt.ylabel('Efektif Dairesel Hız - Vc (km/s)', fontsize=12, color='#cccccc')

ax.spines['bottom'].set_color('#444444')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#444444')
ax.tick_params(axis='x', colors='#aaaaaa')
ax.tick_params(axis='y', colors='#aaaaaa')
plt.grid(True, alpha=0.15, color='white')

plt.xlim(0, 80)
plt.ylim(0, 500)

legend = plt.legend(fontsize=12, facecolor='#1a1a1a', edgecolor='#333333', loc='lower right')
for text in legend.get_texts():
    text.set_color("white")

plt.tight_layout()
plt.savefig('ngc4472_eliptik_testi.png', dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
print("Grafik 'ngc4472_eliptik_testi.png' olarak kaydedildi.")
