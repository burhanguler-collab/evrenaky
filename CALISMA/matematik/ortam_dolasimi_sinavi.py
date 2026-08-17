# -*- coding: utf-8 -*-
"""
ORTAM DOLASIMI SINAVI — Merkur kapanisi ortam durgunlugu varsayimina asili mi?
==============================================================================
Denetimin en ciddi bulgusu (Hat 7): Lambda_kin'deki V, YEREL ORTAMA goredir
(11.4.8.1). Ana oturumun hesabi ortami DURGUN aldi (w=0). Ama teorinin kendi
yapisi ortamin DOLASTIGINI soyluyor:
  M-9 siklostrofik denge: grad P/rho_0 = v_th^2/r ; rho_n/rho_0 = 4 (M-8)
  => v_th^2 = 4 r g => v_th = 2 v_yor   (M-37 profil teoremi ile ayni)
Merkur yorungesinde ortam ~95.7 km/s dolasiyor, Merkur 47.9 km/s.

EYLEM (ortam akisli):
  S = -m c0^2 int Lambda(r) sqrt(1 - (u^2+v^2)/c_loc^2) dt ,  u=rdot, v=r*phidot-w(r)
Korunumlar (analitik cikarim):
  S_kok = Lambda/D ,  D(r) = eps - w*lam/(c0^2 r)
  v = lam Lambda^4/(r D) ,  u^2 = c0^2 Lambda^4 (1 - Lambda^2/D^2) - lam^2 Lambda^8/(r^2 D^2)
  dphi/dr = [lam Lambda^4/(r D) + w] / (r u)
Presesyon = 2*int_{r1}^{r2} dphi/dr dr - 2pi
"""
import numpy as np
from scipy.optimize import fsolve
from scipy.integrate import quad

c0 = 2.99792458e8
AU = 1.495978707e11
GM = 1.32712440018e20
mu = GM/c0**2
arcsec = 180*3600/np.pi

def Lam(r):  return np.exp(-mu/r)

def make_w(kind, wc=0.0):
    if kind == 'sifir': return lambda r: 0.0
    if kind == 'iki':   return lambda r: 2*np.sqrt(GM/r)
    if kind == 'bir':   return lambda r: np.sqrt(GM/r)
    if kind == 'sabit': return lambda r: wc
    raise ValueError

def coz_sabitler(wfun, r1, r2):
    """u(r1)=u(r2)=0 kosullarindan eps, lam."""
    def F(p):
        eps, lam = p
        out = []
        for r in (r1, r2):
            L = Lam(r); w = wfun(r)
            D = eps - w*lam/(c0**2*r)
            out.append(c0**2*L**4*(1 - L**2/D**2) - lam**2*L**8/(r**2*D**2))
        return out
    # Newton baslangici: w=0 Kepler degerleri
    a = 0.5*(r1+r2); e = (r2-r1)/(r1+r2)
    lam0 = np.sqrt(GM*a*(1-e**2))
    eps0 = 1 - GM/(2*a*c0**2)
    return fsolve(F, [eps0, lam0], full_output=False, xtol=1e-14)

def presesyon(wfun, a, e):
    r1 = a*(1-e); r2 = a*(1+e)
    eps, lam = coz_sabitler(wfun, r1, r2)
    def dphidr(r):
        L = Lam(r); w = wfun(r)
        D = eps - w*lam/(c0**2*r)
        u2 = c0**2*L**4*(1 - L**2/D**2) - lam**2*L**8/(r**2*D**2)
        if u2 <= 0: return 0.0
        return (lam*L**4/(r*D) + w)/(r*np.sqrt(u2))
    # uc tekilligi: r = m + h sin(t)
    m = 0.5*(r1+r2); h = 0.5*(r2-r1)
    def integ(t):
        r = m + h*np.sin(t)
        L = Lam(r); w = wfun(r)
        D = eps - w*lam/(c0**2*r)
        u2 = c0**2*L**4*(1 - L**2/D**2) - lam**2*L**8/(r**2*D**2)
        den = (r-r1)*(r2-r)
        if u2 <= 0 or den <= 0: return 0.0
        # dphi = dphidr * dr ; dr = h cos t dt ; sqrt(u2) ~ sqrt(den)*g(r)
        return (lam*L**4/(r*D) + w)/r * np.sqrt(den/u2)
    val, _ = quad(integ, -np.pi/2, np.pi/2, limit=400, epsabs=1e-14, epsrel=1e-13)
    return 2*val - 2*np.pi, eps, lam

a_m, e_m, P_m = 0.38709893*AU, 0.20563069, 0.2408467
gr = 6*np.pi*mu/(a_m*(1-e_m**2))*(100/P_m)*arcsec
v_orb = np.sqrt(GM/a_m)

print("="*84)
print("ORTAM DOLASIMI SINAVI — Merkur presesyonu")
print("="*84)
print(f"  GR/gozlem referansi = {gr:.4f} as/yy ; olculen 42.9799 +/- 0.0009")
print(f"  Merkur yorunge hizi v_yor = {v_orb/1e3:.2f} km/s")
print(f"  Teorinin ortam dolasimi (M-9 + M-37): 2 v_yor = {2*v_orb/1e3:.2f} km/s")
print()
print(f"{'kurulum':<46}{'as/yy':>12}{'oran/GR':>10}{'sigma':>14}")
for ad, kind in [("(A) w = 0        durgun ortam (ana oturum)", 'sifir'),
                 ("(B) w = 2 v_yor  M-9 siklostrofik denge",   'iki'),
                 ("(C) w = 1 v_yor  tam kavrama",               'bir')]:
    try:
        p, eps, lam = presesyon(make_w(kind), a_m, e_m)
        p = p*(100/P_m)*arcsec
        print(f"  {ad:<44}{p:>12.4f}{p/gr:>10.5f}{(p-42.9799)/0.0009:>14.4g}")
    except Exception as ex:
        print(f"  {ad:<44}  HATA: {ex}")
print()
print("  Sabit (tegetsel olmayan) ortam kaymasi taramasi:")
print(f"{'w_sabit (m/s)':>16}{'as/yy':>14}{'sigma':>14}")
for wc in [0.0, 0.1, 0.32, 1.0, 10.0, 100.0]:
    try:
        p, _, _ = presesyon(make_w('sabit', wc), a_m, e_m)
        p = p*(100/P_m)*arcsec
        print(f"{wc:>16.2f}{p:>14.4f}{(p-42.9799)/0.0009:>14.4g}")
    except Exception as ex:
        print(f"{wc:>16.2f}   HATA: {ex}")
