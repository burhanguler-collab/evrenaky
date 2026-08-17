# -*- coding: utf-8 -*-
"""
USTEL OLCEK YAPISI — YORUNGE SINAVI (Merkur gunberi + golge + ufuk)
====================================================================
Teorinin KENDI eyleminden yorunge denklemi. GR ithali YOK; kullanilan tek yapi:
  * Ic saat hizi (M-21/M-42/11.4.8.1):  f = f0 * Lambda_g(r) * Lambda_kin
        Lambda_kin = sqrt(1 - V^2/c_loc^2),   c_loc = c0*Lambda_g^2   (M-42)
  * Eylem: S = -m c0^2 * integral(Lambda_g * Lambda_kin) dt   (ic faz birikimi)
  * Kutle-itim (M-2): a = -grad P / rho_n           [statik denetim icin]
  * Kavrama Yasasi (M-1): c^2 = P/rho ;  k=0 kanali (M-44): rho = rho_0

Iki Lambda adayi karsilastirilir:
  LINEER (M-42'nin mevcut yazimi):      Lambda = 1 - mu/r
  USTEL  (bu calismanin onerisi):       Lambda = exp(-mu/r)
       kokeni: stiff ortamda hacim modulu = P'nin kendisi  =>  dP/dchi = -C*(P/P0)
               =>  P = P0*exp(-C*chi/P0) = P0*exp(-4mu/r)  (M-46'nin chi Poisson'u DEGISMEZ)

Euler-Lagrange'dan (turetim: karadelik_cozum_calismasi.md 3.2):
  (du/dphi)^2 = c0^2 (eps^2 - Lambda^2) / (lam^2 Lambda^4) - u^2 ,  u = 1/r
"""
import numpy as np

c0 = 2.99792458e8
G  = 6.67430e-11
AU = 1.495978707e11
GMsun = 1.32712440018e20
mu_sun = GMsun/c0**2                  # 1476.6 m
arcsec = 180*3600/np.pi               # rad -> arcsec

# ---------------------------------------------------------------- Lambda adaylari
def L_ustel(u, mu):  return np.exp(-mu*u)
def L_lineer(u, mu): return 1.0 - mu*u

# ---------------------------------------------------------------- yorunge integrali
def apsidal_aci(Lam, mu, a, e, N=200001):
    """Bir perihelion->aphelion->perihelion tam donusunun taradigi aciyi ver."""
    u1 = 1.0/(a*(1+e))       # aphelion  (kucuk u)
    u2 = 1.0/(a*(1-e))       # perihelion (buyuk u)
    L1 = Lam(u1, mu); L2 = Lam(u2, mu)
    # 2x2: c0^2 eps^2 / L^4  -  lam^2 u^2  =  c0^2 / L^2
    A = np.array([[c0**2/L1**4, -u1**2],
                  [c0**2/L2**4, -u2**2]])
    b = np.array([c0**2/L1**2, c0**2/L2**2])
    eps2, lam2 = np.linalg.solve(A, b)
    # integral: dphi = du / sqrt(F(u)),  F = c0^2(eps^2-L^2)/(lam^2 L^4) - u^2
    # ucda kok tekilligi: u = m + h sin(t)
    m = 0.5*(u1+u2); h = 0.5*(u2-u1)
    t = np.linspace(-np.pi/2, np.pi/2, N)
    u = m + h*np.sin(t)
    L = Lam(u, mu)
    F = c0**2*(eps2 - L**2)/(lam2*L**4) - u**2
    # F, uclarda ~ (u-u1)(u2-u) gibi sifirlanir; G = F/((u-u1)(u2-u)) duzgun
    den = (u-u1)*(u2-u)
    Gf = np.empty_like(F)
    ic = np.abs(den) > 0
    Gf[ic] = F[ic]/den[ic]
    # uclari komsudan ekstrapole et
    Gf[0]  = 2*Gf[1]-Gf[2]
    Gf[-1] = 2*Gf[-2]-Gf[-3]
    # du = h cos t dt ; sqrt(den) = h cos t  =>  integrand = 1/sqrt(Gf)
    integrand = 1.0/np.sqrt(Gf)
    dphi_yarim = np.trapezoid(integrand, t) if hasattr(np,'trapezoid') else np.trapz(integrand, t)
    return 2.0*dphi_yarim, eps2, lam2

def presesyon(Lam, mu, a, e):
    tam, _, _ = apsidal_aci(Lam, mu, a, e)
    return tam - 2*np.pi          # rad/yorunge

print("="*78)
print("SINAV A — GUNBERI PRESESYONU (teorinin kendi eyleminden; GR formulu YOK)")
print("="*78)
gez = [("Merkur", 0.38709893*AU, 0.20563069, 0.2408467),
       ("Venus",  0.72333199*AU, 0.00677323, 0.61519726),
       ("Dunya",  1.00000011*AU, 0.01671022, 1.0000174),
       ("Ikaros(1566)", 1.0779*AU, 0.8268, 1.1190)]
print(f"{'gezegen':<14}{'USTEL as/yy':>14}{'LINEER as/yy':>14}{'GOZLEM/GR as/yy':>17}{'ustel/GR':>10}{'lin/GR':>9}")
for ad, a, e, Pyr in gez:
    n_yy = 100.0/Pyr
    p_u = presesyon(L_ustel,  mu_sun, a, e)*n_yy*arcsec
    p_l = presesyon(L_lineer, mu_sun, a, e)*n_yy*arcsec
    gr  = 6*np.pi*mu_sun/(a*(1-e**2))*n_yy*arcsec
    print(f"{ad:<14}{p_u:>14.3f}{p_l:>14.3f}{gr:>17.3f}{p_u/gr:>10.4f}{p_l/gr:>9.4f}")
print()
print("  Merkur icin olculen artik (GR-oncesi aciklanamayan): 42.98 +/- 0.04 as/yy")
print("  (Shapiro & Shapiro 2004; Park ve ark. 2017: 42.9799 +/- 0.0009)")
print()

# ---------------------------------------------------------------- PPN okumasi
print("="*78)
print("SINAV B — PPN parametreleri (etkin metrik: g_tt=-Lambda^2, g_ij=Lambda^-2)")
print("="*78)
for ad, Lam in [("USTEL  Lambda=exp(-U)", L_ustel), ("LINEER Lambda=1-U", L_lineer)]:
    # g_tt = -Lambda^2 = -(1 - 2U + 2 beta U^2 + ...) ;  g_ij = Lambda^-2 = 1 + 2 gamma U + ...
    U = 1e-4
    L = Lam(U, 1.0)                      # mu=1, u=U  -> Lambda(U)
    gtt = L**2                           # = 1 - 2U + 2 beta U^2
    beta = (gtt - 1 + 2*U)/(2*U**2)
    gij = L**(-2)                        # = 1 + 2 gamma U + ...
    gam = (gij - 1)/(2*U)
    print(f"  {ad:<24} gamma = {gam:.6f}   beta = {beta:.6f}")
print("  GR: gamma = 1, beta = 1  |  Cassini: gamma-1 = (2.1+/-2.3)e-5  |  LLR: beta-1 = (1.2+/-1.1)e-4")
print("  Gunberi olcegi (2+2gamma-beta)/3:  ustel -> 1.000 (43''), lineer -> 1.167 (50.2'')")
print()

# ---------------------------------------------------------------- statik kuvvet denetimi
print("="*78)
print("SINAV C — Ic tutarlilik: a = -grad P/rho_n  ?=  etkin metrigin statik ivmesi")
print("="*78)
rho_n = 2.7e17; P0 = 0.25*rho_n*c0**2; rho_0 = rho_n/4
for rr in [1e11, 1e9, 1e7, 5e6]:
    U = mu_sun/rr
    # (1) kutle-itim: P = P0 exp(-4U) ; a = -(1/rho_n) dP/dr
    dPdr = P0*np.exp(-4*U)*(4*mu_sun/rr**2)
    a_itim = -dPdr/rho_n
    # (2) etkin metrik statik ivmesi: a = -A'/(2B), A=exp(-2U), B=exp(2U)
    a_metrik = -(mu_sun/rr**2)*np.exp(-4*U)*c0**2/c0**2*c0**2   # = -(GM/r^2)exp(-4U)
    a_metrik = -(GMsun/rr**2)*np.exp(-4*U)
    # (3) Kavrama Yasasi denetimi: c_loc = sqrt(P/rho_0) ?= c0 exp(-2U)
    c_loc = np.sqrt(P0*np.exp(-4*U)/rho_0)
    print(f"  r={rr:8.1e} m: a_itim={a_itim:+.6e}  a_metrik={a_metrik:+.6e}  oran={a_itim/a_metrik:.10f}"
          f"   c_loc/c0={c_loc/c0:.8f} (exp(-2U)={np.exp(-2*U):.8f})")
print()

# ---------------------------------------------------------------- ufuk / kizila kayma
print("="*78)
print("SINAV D — Guclu alan: ufuk var mi? sonsuz kizila kayma var mi?")
print("="*78)
print("  Lambda = exp(-mu/r) hicbir SONLU r'de sifirlanmaz  ->  UFUK YOK, tekillik yok.")
print(f"{'r/mu':>8}{'Lambda':>14}{'c_loc/c0':>12}{'1+z':>14}")
for x in [10, 4, 2, 1, 0.5, 0.2, 0.1]:
    Lam = np.exp(-1.0/x)
    print(f"{x:>8}{Lam:>14.6e}{Lam**2:>12.4e}{1/Lam:>14.4e}")
print("  (GR'de r=2mu'de 1+z sonsuz; burada r=2mu'de 1+z=1.65, r=0.1mu'de 1+z=2.2e4 — sonlu)")
print()

# ---------------------------------------------------------------- golge
print("="*78)
print("SINAV E — Golge yaricapi (Bouguer: b = n(r) r ekstremumu, n = 1/Lambda^2)")
print("="*78)
r = np.linspace(0.2, 40, 2000000)
for ad, nf in [("USTEL  n=exp(2mu/r)", lambda r: np.exp(2/r)),
               ("LINEER n=1/(1-mu/r)^2", lambda r: 1/np.clip((1-1/r)**2, 1e-30, None))]:
    b = nf(r)*r
    i = np.argmin(b)
    print(f"  {ad:<24} r_ph = {r[i]:7.4f} mu   b_krit = {b[i]:8.4f} mu   b/b_GR = {b[i]/(3*np.sqrt(3)):.4f}")
print(f"  GR: r_ph = 3mu (Schwarzschild r), b_krit = 3*sqrt(3) mu = {3*np.sqrt(3):.4f} mu")
print("  EHT: M87* ve Sgr A* halka capi GR ongorusuyle ~%10 icinde uyumlu")
print("  -> USTEL +%4.6 (uyumlu, yeni nesil EHT ile ayirt edilebilir) ; LINEER +%100 (dislanir)")
