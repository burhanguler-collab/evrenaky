# -*- coding: utf-8 -*-
"""
ORTAM DOLASIMI SINAVI (mpmath 60 hane) — belirleyici sinav
===========================================================
Soru: Merkur kapanisi, ortamin durgun olmasi varsayimina mi asili?
Lambda_kin'in V'si YEREL ORTAMA goredir (11.4.8.1). Teorinin kendi yapisi
(M-9 siklostrofik denge + rho_n/rho_0=4) ortamin v_th = 2 v_yor ile dolastigini
soyler. Ana oturumun hesabi w=0 aldi.

Eylem:  S = -m c0^2 int Lambda(r) sqrt(1-(u^2+v^2)/c_loc^2) dt,  u=rdot, v=r phidot - w(r)
Korunumlardan (analitik):
  D(r) = eps - w lam/(c0^2 r)
  u^2 = c0^2 L^4 (1 - L^2/D^2) - lam^2 L^8/(r^2 D^2)
  dphi/dr = [lam L^4/(r D) + w]/(r u)
w=0 kontrolu, onceki formulasyona CEBIRSEL OLARAK indirgenir (dogrulandi).
"""
from mpmath import mp, mpf, exp, sqrt, pi, findroot, quad, sin

mp.dps = 60

c0 = mpf('2.99792458e8')
AU = mpf('1.495978707e11')
GM = mpf('1.32712440018e20')
mu = GM/c0**2
arcsec = 180*3600/pi

def Lam(r): return exp(-mu/r)

def w_sifir(r): return mpf(0)
def w_iki(r):   return 2*sqrt(GM/r)
def w_bir(r):   return sqrt(GM/r)
def w_sabit_fab(wc):
    wc = mpf(wc)
    return lambda r: wc

def u2(r, eps, lam, wfun):
    L = Lam(r); w = wfun(r)
    D = eps - w*lam/(c0**2*r)
    return c0**2*L**4*(1 - L**2/D**2) - lam**2*L**8/(r**2*D**2)

def coz(wfun, r1, r2):
    a = (r1+r2)/2; e = (r2-r1)/(r1+r2)
    lam0 = sqrt(GM*a*(1-e**2)); eps0 = 1 - GM/(2*a*c0**2)
    f = lambda eps, lam: (u2(r1, eps, lam, wfun), u2(r2, eps, lam, wfun))
    return findroot(f, (eps0, lam0), tol=mpf('1e-50'))

def presesyon(wfun, a, e):
    r1 = a*(1-e); r2 = a*(1+e)
    sol = coz(wfun, r1, r2)
    eps, lam = sol[0], sol[1]
    m_ = (r1+r2)/2; h_ = (r2-r1)/2
    def integ(t):
        r = m_ + h_*sin(t)
        L = Lam(r); w = wfun(r)
        D = eps - w*lam/(c0**2*r)
        U2 = c0**2*L**4*(1 - L**2/D**2) - lam**2*L**8/(r**2*D**2)
        den = (r-r1)*(r2-r)
        if U2 <= 0 or den <= 0: return mpf(0)
        return (lam*L**4/(r*D) + w)/r * sqrt(den/U2)
    val = quad(integ, [-pi/2, pi/2])
    return 2*val - 2*pi, eps, lam

a_m = mpf('0.38709893')*AU; e_m = mpf('0.20563069'); P_m = mpf('0.2408467')
gr = 6*pi*mu/(a_m*(1-e_m**2))*(100/P_m)*arcsec
v_orb = sqrt(GM/a_m)
olc = mpf('42.9799'); sg = mpf('0.0009')

print("="*86)
print("ORTAM DOLASIMI SINAVI (mpmath 60 hane)")
print("="*86)
print(f"  GR/gozlem referansi = {mp.nstr(gr,8)} as/yy ; olculen 42.9799 +/- 0.0009")
print(f"  Merkur v_yor = {mp.nstr(v_orb/1000,6)} km/s ; teorinin ortam dolasimi 2v_yor = {mp.nstr(2*v_orb/1000,6)} km/s")
print()
print(f"{'kurulum':<44}{'as/yy':>16}{'oran/GR':>14}{'sigma':>16}")
kurulumlar = [("(A) w = 0       durgun (ana oturum)", w_sifir),
              ("(B) w = 2 v_yor M-9 siklostrofik",   w_iki),
              ("(C) w = 1 v_yor tam kavrama",         w_bir)]
for ad, wf in kurulumlar:
    try:
        p, eps, lam = presesyon(wf, a_m, e_m)
        pv = p*(100/P_m)*arcsec
        print(f"  {ad:<42}{mp.nstr(pv,9):>16}{mp.nstr(pv/gr,8):>14}{mp.nstr((pv-olc)/sg,5):>16}")
    except Exception as ex:
        print(f"  {ad:<42}  HATA: {type(ex).__name__}: {ex}")
print()
print("  Sabit tegetsel ortam kaymasi (denetimin 0.32 m/s siniri):")
print(f"{'w (m/s)':>12}{'as/yy':>16}{'sigma':>16}")
for wc in ['0', '0.1', '0.32', '1', '10', '100', '1000']:
    try:
        p, _, _ = presesyon(w_sabit_fab(wc), a_m, e_m)
        pv = p*(100/P_m)*arcsec
        print(f"{wc:>12}{mp.nstr(pv,9):>16}{mp.nstr((pv-olc)/sg,5):>16}")
    except Exception as ex:
        print(f"{wc:>12}  HATA: {type(ex).__name__}")
