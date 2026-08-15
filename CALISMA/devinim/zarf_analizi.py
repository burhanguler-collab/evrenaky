# -*- coding: utf-8 -*-
"""
K-A + K-B: Chandler yalpalamasi genlik zarfi analizi (11.7-iv'un zarf ayagi)
============================================================================
K-B: IERS EOP C01 (1900+) kutup hareketinden Chandler zarfi, derin minimumlar
     ve faz sicramalari -> A_lc tavaninin sayisallastirilmasi.
K-A: Ayni boru hattindan gecirilen MC: phi in {0, 0.5, 0.9, 1.0}
     (Q_etkin = Q_kl/(1-phi), Q_kl=70) -> derin minimum sikligi hangi rejimle
     uyumlu? (phi=1 satirini karara baglar)

Boru hatti (veri ve MC icin AYNI):
  1) 0.05 yil izgaraya interpolasyon (1900.0'dan itibaren)
  2) Kutup surklenmesi: Gauss alcak-geciren (sigma=8 yil) cikarilir
  3) Yillik salinim: f=1.0 cyc/yr demodulasyon + Gauss (sigma=3 yil) ile
     kestirilip cikarilir
  4) Chandler: f_c=0.8433 cyc/yr (T=433.0 gun) demodulasyon + Gauss
     (sigma=1.2 yil) -> karmasik zarf A(t)e^{i phi(t)}
Kenar etkisi: ilk/son 2.5 yil degerlendirme disi.
Varsayim (MC): beyaz gurultu uyarma (7 Agu faz sinaviyla ayni varsayim).
"""
import numpy as np

RNG = np.random.default_rng(20260808)
VERI = r"C:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\CALISMA\devinim\veri\eopc01_iau2000.txt"

DT     = 0.05          # yil
T0     = 1900.0
F_C    = 365.25/433.0  # Chandler frekansi, cyc/yr = 0.8435
F_A    = 1.0           # yillik
SIG_LP = 8.0           # surklenme alcak-geciren sigma (yil)
SIG_A  = 3.0           # yillik zarf sigma (yil)
SIG_C  = 1.2           # Chandler zarf sigma (yil)
KENAR  = 2.5           # yil, degerlendirme disi
Q_KL   = 70.0
PHI_SET = [0.0, 0.5, 0.9, 1.0]
M_MC   = 1000

def gauss_smooth(z, dt, sigma_yr):
    """Karmasik seri icin Gauss cekirdekli yumusatma (yansimali kenar)."""
    n = int(np.ceil(4*sigma_yr/dt))
    t = np.arange(-n, n+1)*dt
    k = np.exp(-0.5*(t/sigma_yr)**2); k /= k.sum()
    zp = np.concatenate([z[n:0:-1], z, z[-2:-n-2:-1]])
    return np.convolve(zp, k, mode='valid')

def boru_hatti(m, dt, drift=True, yillik=True):
    """m: karmasik kutup serisi -> (A, phi) Chandler zarfi."""
    t = np.arange(len(m))*dt
    if drift:
        m = m - gauss_smooth(m, dt, SIG_LP)
    if yillik:
        for f in (+F_A, -F_A):   # yillik prograd + retrograd
            dem = m*np.exp(-2j*np.pi*f*t)
            env = gauss_smooth(dem, dt, SIG_A)
            m = m - env*np.exp(2j*np.pi*f*t)
    dem = m*np.exp(-2j*np.pi*F_C*t)          # prograd Chandler
    env = gauss_smooth(dem, dt, SIG_C)
    return np.abs(env), np.unwrap(np.angle(env))

def minimumlar(t, A, taban_orani, medyan):
    """Yerel minimumlar (A < taban_orani*medyan), kenarlar disi."""
    ic = (t > t[0]+KENAR) & (t < t[-1]-KENAR)
    idx = [i for i in range(1, len(A)-1)
           if ic[i] and A[i] <= A[i-1] and A[i] <= A[i+1]
           and A[i] < taban_orani*medyan]
    # 2 yildan yakin minimumlari birlestir (en derini kalir)
    sec = []
    for i in idx:
        if sec and t[i]-t[sec[-1]] < 2.0:
            if A[i] < A[sec[-1]]: sec[-1] = i
        else:
            sec.append(i)
    return sec

# ---------------------------------------------------------------- K-B: VERI
mjd, x, y = [], [], []
with open(VERI) as f:
    for sat in f:
        if sat.lstrip().startswith('#') or not sat.strip():
            continue
        p = sat.split()
        mjd.append(float(p[0])); x.append(float(p[1])); y.append(float(p[2]))
mjd = np.array(mjd); x = np.array(x); y = np.array(y)
yil = 1858.0 + (mjd + 321.0)/365.25          # MJD 0 = 17 Kasim 1858
sec = yil >= T0
yil, x, y = yil[sec], x[sec], y[sec]

tg = np.arange(T0, yil[-1], DT)
xg = np.interp(tg, yil, x); yg = np.interp(tg, yil, y)
m  = (xg - 1j*yg)*1000.0                     # mas; prograd = +f (x - iy)

A, PH = boru_hatti(m, DT)
ic = (tg > tg[0]+KENAR) & (tg < tg[-1]-KENAR)
med = np.median(A[ic])

print("=== K-B: IERS EOP C01 zarf analizi ===")
print(f"Aralik: {tg[0]:.2f}-{tg[-1]:.2f} ({tg[-1]-tg[0]:.1f} yil, {len(tg)} ornek)")
print(f"Chandler zarf medyani: {med:.1f} mas")
print(f"Zarf min (kenar disi): {A[ic].min():.1f} mas @ {tg[ic][np.argmin(A[ic])]:.1f}")
print(f"\nMinimumlar (A < 0.45 medyan = {0.45*med:.0f} mas); faz penceresi \u00b14 yil:")
print(f"{'yil':>8} {'A_min (mas)':>12} {'A/medyan':>9} {'faz sicramasi':>14}")
for i in minimumlar(tg, A, 0.45, med):
    dn = int(4.0/DT)
    j0, j1 = max(i-dn, 0), min(i+dn, len(PH)-1)
    dphi = np.degrees((PH[j1]-PH[j0] + np.pi) % (2*np.pi) - np.pi)
    # genis pencere: minimumdan once [t-8,t-3] ve sonra [t+3,t+8] ortalama fazi
    on  = (tg >= tg[i]-8) & (tg <= tg[i]-3)
    ard = (tg >= tg[i]+3) & (tg <= tg[i]+8)
    if on.any() and ard.any():
        dphi_g = np.degrees((PH[ard].mean()-PH[on].mean() + np.pi) % (2*np.pi) - np.pi)
        gs = f"{dphi_g:6.0f}\u00b0"
    else:
        gs = "  (pencere disi)"
    print(f"{tg[i]:8.1f} {A[i]:12.1f} {A[i]/med:9.3f} {dphi:12.0f}\u00b0  genis:{gs}")

# ---------------------------------------------------------------- K-A: MC
print("\n=== K-A: Monte Carlo (ayni boru hatti, beyaz gurultu) ===")
esik = A[ic].min()/med   # verinin en derin minimumu, medyan birimi
print(f"Derin-minimum esigi: veri tabani A/medyan = {esik:.3f}")
N = len(tg); t_mc = np.arange(N)*DT
omg = 2*np.pi*F_C
print(f"{'phi':>5} {'Q_etkin':>8} {'P(>=1 derin)':>13} {'P(>=2 derin)':>13} "
      f"{'min(A)/med %5':>13} {'medyan':>7} {'%95':>7}")
for phi in PHI_SET:
    Q = np.inf if phi >= 1.0 else Q_KL/(1.0-phi)
    dec = 1.0 if not np.isfinite(Q) else np.exp(-omg*DT/(2*Q))
    a = dec*np.exp(1j*omg*DT)
    mm = np.zeros((M_MC,), complex)
    seri = np.empty((M_MC, N), complex)
    ksi = (RNG.standard_normal((M_MC, N)) + 1j*RNG.standard_normal((M_MC, N)))
    for k in range(N):
        mm = a*mm + ksi[:, k]
        seri[:, k] = mm
    n_derin = np.zeros(M_MC, int); oranlar = np.empty(M_MC)
    for r in range(M_MC):
        Ar, _ = boru_hatti(seri[r], DT, drift=False, yillik=False)
        mr = np.median(Ar[ic])
        n_derin[r] = len(minimumlar(t_mc, Ar, esik, mr))
        oranlar[r] = Ar[ic].min()/mr
    q5, q50, q95 = np.percentile(oranlar, [5, 50, 95])
    print(f"{phi:5.1f} {('inf' if not np.isfinite(Q) else f'{Q:.0f}'):>8} "
          f"{np.mean(n_derin >= 1):13.3f} {np.mean(n_derin >= 2):13.3f} "
          f"{q5:13.3f} {q50:7.3f} {q95:7.3f}")

print("\nOkuma: 'derin' esigi = verinin en derin minimumu (0.095). P(>=1 derin)")
print("sutunu, o derinlikte bir minimumun her phi rejiminde ne siklikta kendiligin-")
print("den olustugunu verir. Sutunlar phi boyunca ortusuyorsa zarf istatistigi")
print("rejimleri AYIRAMIYOR demektir (tayf dejenerasyonunun zarf karsiligi).")
