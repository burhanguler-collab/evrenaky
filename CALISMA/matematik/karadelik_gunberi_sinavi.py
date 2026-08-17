# -*- coding: utf-8 -*-
"""
GUNBERI SINAVI (kesin) — ustel olcek yapisinin Merkur sinavi
=============================================================
Yorunge denklemi, teorinin kendi eyleminden turetilir (GR formulu YOK):
   S = -m c0^2 * int Lambda_g(r) * sqrt(1 - V^2/c_loc^2) dt ,  c_loc = c0 Lambda_g^2
Euler-Lagrange + korunumlar (E = m c0^2 Lambda/S , l = m r^2 phidot/(Lambda^3 S)):
   (du/dphi)^2 = c0^2 (eps^2 - Lambda^2)/(lam^2 Lambda^4) - u^2 = F(u)
Turevi alinirsa TEKILLIKSIZ ikinci mertebe ODE:
   u'' = F'(u)/2 = -c0^2 Lambda'(u) (2 eps^2 - Lambda^2)/(lam^2 Lambda^5) - u
Gunberinden (u'=0) baslanir, u'=0 tekrar olana dek (aphelion) integre edilir;
tam yorunge acisi = 2*dphi ; presesyon = 2*dphi - 2pi.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

c0 = 2.99792458e8
AU = 1.495978707e11
GMsun = 1.32712440018e20
mu = GMsun/c0**2
arcsec = 180*3600/np.pi

def make_lam(kind):
    if kind == 'ustel':   return (lambda u: np.exp(-mu*u)), (lambda u: -mu*np.exp(-mu*u))
    if kind == 'lineer':  return (lambda u: 1-mu*u),        (lambda u: -mu*np.ones_like(u))
    raise ValueError

def sabitler(Lam, a, e):
    """Iki apsis noktasindan eps^2 ve lam^2'yi coz."""
    u1 = 1.0/(a*(1+e)); u2 = 1.0/(a*(1-e))
    L1, L2 = Lam(u1), Lam(u2)
    A = np.array([[c0**2/L1**4, -u1**2],[c0**2/L2**4, -u2**2]])
    b = np.array([c0**2/L1**2, c0**2/L2**2])
    eps2, lam2 = np.linalg.solve(A, b)
    return eps2, lam2, u1, u2

def presesyon(kind, a, e, rtol=3e-13, atol=1e-18):
    """Apsisler arasi ORTA noktadan basla (u' != 0), iki yone integre et:
    ileri -> bir apsis, geri -> oteki apsis. Toplam = yarim yorunge acisi."""
    Lam, dLam = make_lam(kind)
    eps2, lam2, u1, u2 = sabitler(Lam, a, e)
    u0 = 0.5*(u1+u2)
    L0 = Lam(u0)
    F0 = c0**2*(eps2 - L0**2)/(lam2*L0**4) - u0**2
    up0 = np.sqrt(F0)                      # u artiyor (gunberine dogru)
    def rhs(phi, y):
        u, up = y
        L = Lam(u); dL = dLam(u)
        return [up, -c0**2*dL*(2*eps2 - L**2)/(lam2*L**5) - u]
    def apsis(phi, y): return y[1]
    apsis.terminal = True; apsis.direction = 0
    ileri = solve_ivp(rhs, [0, 20], [u0, up0], events=apsis,
                      rtol=rtol, atol=atol, method='DOP853')
    geri  = solve_ivp(rhs, [0, -20], [u0, up0], events=apsis,
                      rtol=rtol, atol=atol, method='DOP853')
    if not (ileri.t_events[0].size and geri.t_events[0].size):
        return np.nan
    yarim = ileri.t_events[0][0] - geri.t_events[0][0]
    return 2*yarim - 2*np.pi

print("="*80)
print("GUNBERI PRESESYONU — teorinin kendi eyleminden (GR formulu kullanilmadi)")
print("="*80)
gez = [("Merkur",       0.38709893*AU, 0.20563069, 0.2408467,  "42.9799 +/- 0.0009"),
       ("Venus",        0.72333199*AU, 0.00677323, 0.61519726, "8.6247"),
       ("Dunya",        1.00000011*AU, 0.01671022, 1.0000174,  "3.8387"),
       ("Ikaros 1566",  1.0779*AU,     0.8268,     1.1190,     "10.05")]
print(f"{'gezegen':<13}{'USTEL as/yy':>13}{'LINEER as/yy':>14}{'GR/gozlem':>12}{'ustel/GR':>10}{'lin/GR':>9}")
for ad, a, e, Pyr, obs in gez:
    n = 100.0/Pyr
    pu = presesyon('ustel',  a, e)*n*arcsec
    pl = presesyon('lineer', a, e)*n*arcsec
    gr = 6*np.pi*mu/(a*(1-e**2))*n*arcsec
    print(f"{ad:<13}{pu:>13.4f}{pl:>14.4f}{gr:>12.4f}{pu/gr:>10.6f}{pl/gr:>9.4f}")
print()
print("  Olculen (Merkur, GR-oncesi aciklanamayan artik): 42.9799 +/- 0.0009 as/yy")
print("  (Park ve ark. 2017, MESSENGER radyo-izleme)")
print()
print("  BEKLENTI (PPN):  presesyon olcegi = (2 + 2*gamma - beta)/3")
print("     ustel:  gamma=1, beta=1    -> olcek 1.000  -> 42.98 as/yy")
print("     lineer: gamma=1, beta=0.5  -> olcek 1.167  -> 50.14 as/yy  (DISLANIR, ~8000 sigma)")
print()

# --- ek: LLR beta sinavi ---
print("="*80)
print("EK — beta uzerindeki bagimsiz gozlem sinirlari")
print("="*80)
print("  LLR (Ay lazer telemetrisi):  beta - 1 = (1.2 +/- 1.1)e-4   [Williams+2004]")
print("  Cassini (Shapiro):           gamma - 1 = (2.1 +/- 2.3)e-5")
print("  USTEL:  beta-1 = 0 (tam)      -> her iki bantla uyumlu   OK")
print("  LINEER: beta-1 = -0.5         -> LLR bandini ~4500 sigma asar  DISLANIR")
