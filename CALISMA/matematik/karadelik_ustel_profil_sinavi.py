# -*- coding: utf-8 -*-
"""
KARADELIK USTEL PROFIL SINAVI — entalpi-baglasimli deplasman yaniti
====================================================================
Aday (karadelik_cozum_calismasi.md): deplasman alani basinca degil ENTALPIYE
lineer baglanir (stiff ortamin dogal degiskeni; M-3' entalpi h = c0^2 ln rho):
    C*chi = -P0 * ln(P/P0)   ==>   P(r) = P0 * exp(-4*mu/r),  mu = G*M/c0^2
    c_loc(r) = c0 * exp(-2*mu/r)      [oran bicimi c^2 = P/rho, rho = rho0]
Karsilastirma: lineer yanit P = P0(1 - 4mu/r) -> c_loc = c0*sqrt(1-4mu/r).

Bu betik dogrular:
  1) Zayif alan: iki profil birinci mertebede ozdes (bukulme 1.751'' korunur).
  2) Foton kuresi & golge (Bouguer: b = n(r)*r ekstremumu):
       lineer:  r_ph = 6mu, b = 6*sqrt(3)*mu = 10.392mu  (GR'in 2 kati - DISLANIR)
       ustel :  r_ph = 2mu, b = 2e*mu = 5.437mu
       GR    :  b = 3*sqrt(3)*mu = 5.196mu   -> ustel fark +%4.6 (EHT uyumlu)
  3) Sayisal isin izleme ile golge yaricapinin analitik degerle karsilastirilmasi
     (kodda GR yok; yalniz ortam optigi dx/dt = c k, dk/dt = -(I-kk)grad c).
  4) M_min: R_rho = r_ph kesisimi -> kitaptaki 8.3 Msun formulu (anlami degisir:
     ufuk degil GOLGE esigi).
"""
import numpy as np

# ---------- analitik kontroller ----------
mu = 1.0
def n_ustel(r):  return np.exp(2*mu/r)
def n_lineer(r):
    arg = 1-4*mu/r
    return 1/np.sqrt(arg) if np.ndim(r)==0 else 1/np.sqrt(np.clip(arg,1e-12,None))

def foton_kuresi(nfun, rmin, rmax, N=400000):
    r = np.linspace(rmin, rmax, N)
    b = nfun(r)*r
    i = np.argmin(b)
    return r[i], b[i]

print("="*72)
print("1) Foton kuresi / kritik vurus parametresi (birim: mu = GM/c0^2)")
print("="*72)
r1, b1 = foton_kuresi(n_ustel, 0.5, 12)
r2, b2 = foton_kuresi(lambda r: 1/np.sqrt(np.clip(1-4*mu/r,1e-12,None)), 4.05, 30)
print(f"  ustel : r_ph = {r1:.4f} (analitik 2)   b = {b1:.4f} (analitik 2e = {2*np.e:.4f})")
print(f"  lineer: r_ph = {r2:.4f} (analitik 6)   b = {b2:.4f} (analitik 6√3 = {6*np.sqrt(3):.4f})")
print(f"  GR    : b = 3√3 = {3*np.sqrt(3):.4f}")
print(f"  -> ustel/GR = {b1/(3*np.sqrt(3)):.4f}  (+%{100*(b1/(3*np.sqrt(3))-1):.2f})   |   lineer/GR = {b2/(3*np.sqrt(3)):.4f}")

# ---------- sayisal isin izleme (golge olcumu; kodda yalniz ortam optigi) ----------
print()
print("="*72)
print("2) Sayisal isin izleme ile golge (ustel profil)")
print("="*72)
def cval(x):  # c0=1
    r = np.hypot(x[0], x[1]);  return np.exp(-2*mu/r)
def gradc(x):
    r = np.hypot(x[0], x[1]);  return np.exp(-2*mu/r)*(2*mu/r**3)*x  # d/dx[-2mu/r] * c

def izle(b, rmax=60.0, h=2e-3, adim=6_000_000):
    x = np.array([-rmax, b]); k = np.array([1.0, 0.0])
    rmin = np.hypot(*x)
    for _ in range(adim):
        c = cval(x); gc = gradc(x)
        # RK2 (yeterli): dx=c k ; dk = -(I-kk)gc
        dk = -(gc - k*(k@gc)); xm = x + 0.5*h*c*k; km = k + 0.5*h*dk; km/=np.linalg.norm(km)
        cm = cval(xm); gcm = gradc(xm); dkm = -(gcm - km*(km@gcm))
        x = x + h*cm*km; k = k + h*dkm; k /= np.linalg.norm(k)
        r = np.hypot(*x); rmin = min(rmin, r)
        if r > rmax*1.05 and (x@k) > 0:   # kacti
            return 'kacti', rmin
        if r < 0.3:                        # derine dusdu (pratikte donmus)
            return 'dustu', rmin
    return 'belirsiz', rmin

# b taramasiyla kritik b: kacan/dusen siniri
lo, hi = 4.5, 6.5
for _ in range(18):
    mid = 0.5*(lo+hi)
    durum, _ = izle(mid)
    if durum == 'dustu': lo = mid
    else: hi = mid
b_krit = 0.5*(lo+hi)
print(f"  isin-izleme kritik b = {b_krit:.4f}   (analitik 2e = {2*np.e:.4f})   sapma %{100*abs(b_krit-2*np.e)/(2*np.e):.2f}")

# ---------- zayif alan es-degerlik ----------
print()
print("="*72)
print("3) Zayif alan: n-1 karsilastirmasi (r = 1000 mu'da)")
print("="*72)
r = 1000.0
print(f"  ustel n-1  = {n_ustel(r)-1:.6e}")
print(f"  lineer n-1 = {1/np.sqrt(1-4*mu/r)-1:.6e}")
print(f"  1.mertebe 2mu/r = {2*mu/r:.6e}   -> ucu de ayni (bukulme 1.751'' korunur)")

# ---------- M_min ----------
print()
print("="*72)
print("4) M_min (R_rho = r_ph kesisimi; SI)")
print("="*72)
G = 6.674e-11; c = 2.998e8; rho_n = 2.7e17; Msun = 1.989e30
# R_rho = (3M/4 pi rho_n)^(1/3) = 2GM/c^2  =>  M^2 = (3/(4 pi rho_n)) * (c^2/2G)^3
Mmin = np.sqrt(3/(4*np.pi*rho_n)) * (c**2/(2*G))**1.5
print(f"  M_min = {Mmin/Msun:.2f} Msun  (kitaptaki 8.3 formulu — anlam: GOLGE esigi, ufuk degil)")
print(f"  Alt sinif ornegi: 3.6 Msun rho_n-govdesi: R_rho = {(3*3.6*Msun/(4*np.pi*rho_n))**(1/3)/1e3:.1f} km,"
      f"  r_ph = {2*G*3.6*Msun/c**2/1e3:.1f} km  -> foton kuresi yok, 'golgesiz kompakt govde'")
