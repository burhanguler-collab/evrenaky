import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Karanlık mod
plt.style.use('dark_background')

# --- M33 (Triangulum Galaksisi) Gerçek Gözlem Verileri (Yaklaşık Değerler) ---
# Yarıçap (kpc)
r_obs = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0])
# Gözlemlenen Yörünge Hızı (km/s)
v_obs = np.array([40, 65, 80, 90, 96, 101, 105, 108, 110, 112, 115, 117, 119, 120, 121])

# Hata payları (görselleştirme için ufak hata çubukları)
v_err = np.random.uniform(3, 7, len(v_obs))

# --- Modeller ---
# 1. Newton Modeli (Sadece görünür kütle): v = sqrt(A / r)
def model_newton(r, A):
    return np.sqrt(A / r)

# 2. Evrenakı Teorisi Modeli: v = sqrt(A / r + B)
# Burada B, eksenel kuvvetin (1/r) asimptotik limitini temsil eder
def model_evrenaki(r, A, B):
    return np.sqrt(A / r + B)

# --- Veriyi Modellere Uydurma (Curve Fitting) ---
# Eğrinin tepe noktasından (r=3 kpc civarı) sonrasını fit edelim, 
# çünkü iç kısımlarda katı cisim dönüşü (r ile doğru orantılı) etkilidir.
mask = r_obs >= 3.0
r_fit = r_obs[mask]
v_fit = v_obs[mask]

# Newton için A parametresini uydur (A = GM)
popt_newton, _ = curve_fit(model_newton, r_fit, v_fit, p0=[10000])

# Evrenakı için A ve B parametrelerini uydur (A = GM, B = K)
popt_evrenaki, _ = curve_fit(model_evrenaki, r_fit, v_fit, p0=[10000, 10000])

# --- Grafik Çizimi ---
r_plot = np.linspace(3, 20, 200)

fig = plt.figure(figsize=(10, 6), facecolor='#121212')
ax = fig.add_subplot(111)
ax.set_facecolor('#121212')

# Gözlem verileri (Hata çubuklarıyla)
plt.errorbar(r_obs, v_obs, yerr=v_err, fmt='o', color='#00ff88', label='M33 Gerçek Gözlem Verisi', capsize=4, zorder=5)

# Fit edilmiş modeller
plt.plot(r_plot, model_newton(r_plot, *popt_newton), label='Klasik Çekim Fit ($v = \\sqrt{A/r}$)', color='#ff5555', linestyle='--', linewidth=2)
plt.plot(r_plot, model_evrenaki(r_plot, *popt_evrenaki), label='Evrenakı Teorisi ($v = \\sqrt{A/r + B}$)', color='#55aaff', linewidth=2.5)

plt.title('M33 Galaksisi Gerçek Verileriyle Teori Testi', fontsize=14, pad=15, color='white')
plt.xlabel('Merkezden Uzaklık - r (kpc)', fontsize=12, color='#cccccc')
plt.ylabel('Yörünge Hızı - v (km/s)', fontsize=12, color='#cccccc')

# Görsel ayarlar
ax.spines['bottom'].set_color('#444444')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#444444')
ax.tick_params(axis='x', colors='#aaaaaa')
ax.tick_params(axis='y', colors='#aaaaaa')
plt.grid(True, alpha=0.15, color='white')

plt.xlim(0, 20)
plt.ylim(0, 150)

# Lejant
legend = plt.legend(fontsize=12, facecolor='#1a1a1a', edgecolor='#333333', loc='lower right')
for text in legend.get_texts():
    text.set_color("white")

plt.tight_layout()
plt.savefig('m33_gozlem_testi.png', dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
print("Grafik 'm33_gozlem_testi.png' olarak kaydedildi.")
