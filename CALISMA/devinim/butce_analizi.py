# -*- coding: utf-8 -*-
"""
11.7-iv: Chandler yalpalamasinin AAM+OAM uyarma butcesi
========================================================
Soru: atmosfer + okyanus acisal momentum uyarmasi, gozlenen Chandler
genligini klasik Q'da tam kapatiyor mu?

Yontem (Liouville, prograd kanal):
  m(f) = H(f) chi(f),  H(f) = f_c / [(f_c - f) - i f_c/(2Q)]
  Rezonans bandindaki yalpalama varyansi:
    Var_CW = S_chi(f_c) * INT |H|^2 df = S_chi(f_c) * 2 pi Q f_c
  =>  Q* = Var_CW / (2 pi f_c S_chi(f_c))
  Q* = butcenin kapanmasi icin gereken kalite carpani. Q* klasik banttaysa
  (30-100) butce kapanir (phi ~ 0 sinirlanir); Q* >> 100 ise acik vardir ve
  phi = 1 - Q_kl/Q* dogrudan olculmus olur (11.7.6'nin kapali bagintisi).

Veri:
  - Kutup hareketi: IERS EOP C01 (1976-2025 penceresi), m = (x - i y) [rad]
  - Uyarma: ESMGFZ AAM+OAM v1.0 3h (kutle+hareket, x+iy) [boyutsuz=rad]
    (Dobslaw & Dill; ECMWF ile tutarli zorlanmis MPIOM; veri asimilasyonu yok)
On isleme (chi): gunluk ortalama; mevsimsel harmonikler (1,2,3 cyc/yr) ve
dogrusal egilim cikarilir; PSD Welch (16 yillik parca, Hann, %50 ortusme).
S_chi(f_c): f_c +/- 0.06 cyc/yr bandinin ortancasi (yillik bandi dislar).
Var_CW: zarf_analizi.py boru hattinin ayni pencerede mean(A^2) degeri.
"""
import numpy as np
import glob, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

KOK   = r"C:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\CALISMA\devinim"
T0, T1 = 1976.0, 2026.0
F_C   = 365.25/433.0          # 0.8435 cyc/yr
MAS   = 4.84813681e-9         # 1 mas -> rad

# ---------------------------------------------------- 1) chi: AAM+OAM yukle
def eamf_oku(desen):
    ts, xs, ys = [], [], []
    for f in sorted(glob.glob(desen)):
        with open(f) as fh:
            veri_basladi = False
            for sat in fh:
                p = sat.split()
                if not veri_basladi:
                    if len(p) >= 11 and p[0].isdigit() and len(p[0]) == 4:
                        veri_basladi = True
                    else:
                        continue
                if len(p) >= 11 and p[0].isdigit():
                    mjd = float(p[4])
                    ts.append(1858.0 + (mjd + 321.0)/365.25)
                    xs.append(float(p[5]) + float(p[8]))    # kutle + hareket
                    ys.append(float(p[6]) + float(p[9]))
    return np.array(ts), np.array(xs), np.array(ys)

ta, xa, ya = eamf_oku(KOK + r"\veri\eamf\ESMGFZ_AAM_*.asc")
to, xo, yo = eamf_oku(KOK + r"\veri\eamf\ESMGFZ_OAM_*.asc")
print(f"AAM: {len(ta)} kayit ({ta.min():.2f}-{ta.max():.2f})")
print(f"OAM: {len(to)} kayit ({to.min():.2f}-{to.max():.2f})")

# gunluk izgara; AAM+OAM toplami
DTg = 1.0/365.25
tg  = np.arange(max(ta.min(), to.min()), min(ta.max(), to.max()), DTg)
chi = (np.interp(tg, ta, xa) + 1j*np.interp(tg, ta, ya)
     + np.interp(tg, to, xo) + 1j*np.interp(tg, to, yo))

# egilim + mevsimsel harmonikler cikar (1,2,3 cyc/yr) — en kucuk kareler
B = [np.ones_like(tg), tg - tg.mean()]
for k in (1, 2, 3):
    B += [np.cos(2*np.pi*k*tg), np.sin(2*np.pi*k*tg)]
B = np.array(B).T
katsayi, *_ = np.linalg.lstsq(B, chi, rcond=None)
chi = chi - B @ katsayi

# ------------------------------------------- 2) S_chi(f_c): Welch (karmasik)
def welch_karmasik(z, dt, parca_yil=16.0, ortusme=0.5):
    n = len(z); npar = int(parca_yil/dt)
    adim = int(npar*(1-ortusme))
    pencere = np.hanning(npar); U = (pencere**2).sum()/npar
    S, say = None, 0
    for b in range(0, n-npar+1, adim):
        seg = z[b:b+npar]*pencere
        F = np.fft.fft(seg)*dt
        P = np.abs(F)**2/(npar*dt*U)          # iki yanli PSD [birim^2 * yil]
        S = P if S is None else S+P
        say += 1
    f = np.fft.fftfreq(npar, dt)
    return np.fft.fftshift(f), np.fft.fftshift(S/say), say

f, S, nseg = welch_karmasik(chi, DTg)
bant = (f > F_C-0.06) & (f < F_C+0.06)
S_fc = np.median(S[bant])
# karsilastirma: retrograd taraf ve genis komsular
S_ret = np.median(S[(f > -F_C-0.06) & (f < -F_C+0.06)])
print(f"\nWelch: {nseg} parca (16 yil, Hann, %50)")
print(f"S_chi(+f_c)  = {S_fc:.3e} rad^2*yil  (prograd Chandler bandi)")
print(f"S_chi(-f_c)  = {S_ret:.3e} rad^2*yil  (retrograd, kiyas)")

# ------------------------------- 3) Var_CW: ayni pencerede kutup hareketi
# (zarf_analizi.py'nin boru hatti — import modul-calistirdigi icin kopya)
DT_PM = 0.05
def gauss_smooth(z, dt, sigma_yr):
    n = int(np.ceil(4*sigma_yr/dt))
    t = np.arange(-n, n+1)*dt
    k = np.exp(-0.5*(t/sigma_yr)**2); k /= k.sum()
    zp = np.concatenate([z[n:0:-1], z, z[-2:-n-2:-1]])
    return np.convolve(zp, k, mode='valid')
def boru_hatti(m, dt, drift=True, yillik=True):
    t = np.arange(len(m))*dt
    if drift:
        m = m - gauss_smooth(m, dt, 8.0)
    if yillik:
        for fq in (+1.0, -1.0):
            dem = m*np.exp(-2j*np.pi*fq*t)
            env = gauss_smooth(dem, dt, 3.0)
            m = m - env*np.exp(2j*np.pi*fq*t)
    dem = m*np.exp(-2j*np.pi*F_C*t)
    env = gauss_smooth(dem, dt, 1.2)
    return np.abs(env), np.unwrap(np.angle(env))

mjd, x, y = [], [], []
with open(KOK + r"\veri\eopc01_iau2000.txt") as fh:
    for sat in fh:
        if sat.lstrip().startswith('#') or not sat.strip(): continue
        p = sat.split()
        mjd.append(float(p[0])); x.append(float(p[1])); y.append(float(p[2]))
mjd = np.array(mjd); yil = 1858.0 + (np.array(mjd) + 321.0)/365.25
x = np.array(x); y = np.array(y)
s = (yil >= T0-3) & (yil <= T1)                      # kenar payi ile
tp = np.arange(yil[s].min(), yil[s].max(), DT_PM)
mp = (np.interp(tp, yil[s], x[s]) - 1j*np.interp(tp, yil[s], y[s]))  # arcsec
A, _ = boru_hatti(mp*1000.0, DT_PM)                  # mas
ic = (tp >= T0) & (tp <= T1) & (tp > tp[0]+2.5) & (tp < tp[-1]-2.5)
Var_CW = np.mean((A[ic]*MAS)**2)                     # rad^2 (karmasik guc)
print(f"\n1976-2025 penceresi: Chandler zarf medyani {np.median(A[ic]):.1f} mas")
print(f"Var_CW = mean(A^2) = {Var_CW:.3e} rad^2")

# ---------------------------------------------------- 4) Q* ve phi
Qy = Var_CW/(2*np.pi*F_C*S_fc)
print(f"\n==> Q* (butceyi kapatan kalite carpani) = {Qy:.0f}")
print("    (saglanan/gereken guc orani @ Q_kl = Q_kl/Q*; 1'in ustu = fazlasiyla yeter)")
for Qkl in (30, 70, 100):
    oran = Qkl/Qy
    print(f"  Q_kl={Qkl:>3}: saglanan/gereken = {oran:.2f}x "
          f"({'butce KAPANIYOR' if oran >= 1 else 'ACIK VAR'}), "
          f"phi = 1-Q_kl/Q* = {max(0.0, 1.0-Qkl/Qy):.2f}")

# guc cinsinden
C_A = 2.63e35; OMEGA = 7.292115e-5; SIG = 2*np.pi*F_C/3.156e7  # rad/s
E_w = 0.5*C_A*OMEGA**2*Var_CW
print(f"\nE_w (pencere ort.) = {E_w:.2e} J")
for Q in (70, int(round(Qy))):
    print(f"  P(Q={Q}) = {E_w*SIG/Q/1e6:.2f} MW")

# ---------------------------------------------------- 5) duyarlilik
print("\nDuyarlilik:")
for pj in (8.0, 12.0, 20.0):
    fj, Sj, nj = welch_karmasik(chi, DTg, parca_yil=pj)
    bj = (fj > F_C-0.06) & (fj < F_C+0.06)
    Sfcj = np.median(Sj[bj])
    print(f"  parca={pj:4.0f} yil ({nj:2d} parca): S_chi(f_c)={Sfcj:.3e}  "
          f"Q*={Var_CW/(2*np.pi*F_C*Sfcj):.0f}")
for b in (0.03, 0.10):
    bj = (f > F_C-b) & (f < F_C+b)
    Sfcj = np.median(S[bj])
    print(f"  bant=+/-{b:.2f}: S_chi(f_c)={Sfcj:.3e}  Q*={Var_CW/(2*np.pi*F_C*Sfcj):.0f}")
