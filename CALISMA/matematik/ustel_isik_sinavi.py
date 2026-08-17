# -*- coding: utf-8 -*-
"""
USTEL YAPIDA ISIK: bukulme, Shapiro, golge — tam (kesilmemis) hesap
====================================================================
Ortam optigi: n_eff(r) = 1/Lambda^2 = exp(2 mu/r) ;  mu = G M/c0^2
Sapma acisi (Fermat/Bouguer, izotropik radyal koordinat):
   alpha = 2 * int_{r0}^inf  b dr / (r sqrt(n^2 r^2 - b^2))  -  pi ,  n(r0) r0 = b
Shapiro: Delta_t = (1/c0) int (n_eff - 1) ds  (yol boyunca)
Karsilastirma: GR'in tam Schwarzschild degerleri.
"""
from mpmath import mp, mpf, exp, sqrt, pi, quad, findroot, log, inf
mp.dps = 40

c0 = mpf('2.99792458e8')
GMsun = mpf('1.32712440018e20')
mu = GMsun/c0**2                      # 1476.6 m
Rsun = mpf('6.957e8')
arcsec = 180*3600/pi

def n_ustel(r):  return exp(2*mu/r)

def sapma_ustel(b):
    """alpha = 2 int_{r0}^inf b dr/(r sqrt(n^2 r^2 - b^2)) - pi"""
    f = lambda r: n_ustel(r)*r - b
    r0 = findroot(f, b)                       # donum noktasi
    def integ(t):
        # r = r0 / sin(t)?  daha kararli: r = r0 + s^2 donusumu
        r = r0 + t**2
        n = n_ustel(r)
        rad = (n*r)**2 - b**2
        if rad <= 0: return mpf(0)
        return 2*t * b/(r*sqrt(rad))
    ust = sqrt(mpf('1e14')*b)                # r ~ 1e14 b'ye kadar
    I = quad(integ, [0, sqrt(b*mpf('1e-6')), sqrt(b), sqrt(b*100), ust])
    return 2*I - pi

def sapma_GR_tam(b_sch):
    """GR'in tam sapmasi (Schwarzschild r, kapali integral)."""
    rs = 2*mu
    f = lambda r: r/sqrt(1-rs/r) - b_sch      # dikkat: b tanimi
    # GR icin standart: alpha = 2 int_{r0}^inf dr/(r^2 sqrt(1/b^2 - (1-rs/r)/r^2)) - pi
    r0 = findroot(lambda r: 1/b_sch**2 - (1-rs/r)/r**2, b_sch)
    def integ(t):
        r = r0 + t**2
        rad = 1/b_sch**2 - (1-rs/r)/r**2
        if rad <= 0: return mpf(0)
        return 2*t/(r**2*sqrt(rad))
    ust = sqrt(mpf('1e14')*b_sch)
    return 2*quad(integ, [0, sqrt(b_sch*mpf('1e-6')), sqrt(b_sch), sqrt(b_sch*100), ust]) - pi

print("="*80)
print("1) ISIK BUKULMESI — Gunes kenari (b = R_gunes)")
print("="*80)
a_u = sapma_ustel(Rsun)
a_1 = 4*mu/Rsun                               # birinci mertebe
a_gr = sapma_GR_tam(Rsun)
print(f"  birinci mertebe 4mu/b        = {mp.nstr(a_1*arcsec, 10)} as")
print(f"  USTEL (tam Fermat integrali)  = {mp.nstr(a_u*arcsec, 10)} as")
print(f"  GR (tam Schwarzschild)        = {mp.nstr(a_gr*arcsec, 10)} as")
print(f"  ustel - GR                    = {mp.nstr((a_u-a_gr)*arcsec, 6)} as")
print(f"  VLBI olcumu: 1.7510 +/- ~0.0002 as (Shapiro vd. 2004: gamma-1 < 3e-4)")
print(f"  -> ustel ile GR farki {mp.nstr(abs(a_u-a_gr)*arcsec,3)} as; olcum hassasiyetinin")
print(f"     {mp.nstr(abs(a_u-a_gr)*arcsec/mpf('0.0002'),3)} kati -> AYIRT EDILEMEZ, 1.751 korunuyor  OK")
print()

print("="*80)
print("2) IKINCI MERTEBE KATSAYISI (guclu alan icin onemli)")
print("="*80)
print("  Seri: alpha = 4mu/b + C2 (mu/b)^2 * (4mu/b) ... karsilastirmali olarak:")
for bb, ad in [(Rsun, "Gunes kenari"), (10*mu, "b = 10 mu"), (6*mu, "b = 6 mu")]:
    au = sapma_ustel(bb); ag = sapma_GR_tam(bb); a1 = 4*mu/bb
    print(f"  {ad:<16} mu/b = {mp.nstr(mu/bb,4):>10} | ustel/1.mert = {mp.nstr(au/a1,8):>12}"
          f" | GR/1.mert = {mp.nstr(ag/a1,8):>12} | ustel/GR = {mp.nstr(au/ag,8)}")
print()

print("="*80)
print("3) SHAPIRO GECIKMESI — Dunya-Mars, Gunes kenarina teget")
print("="*80)
AU = mpf('1.495978707e11')
r1, r2, b = AU, mpf('1.524')*AU, Rsun
# Delta_t = (1/c0) int (n-1) ds ; duz yol boyunca s: -sqrt(r1^2-b^2) .. +sqrt(r2^2-b^2)
s1 = -sqrt(r1**2-b**2); s2 = sqrt(r2**2-b**2)
def integ(s):
    r = sqrt(b**2+s**2)
    return n_ustel(r) - 1
I = quad(integ, [s1, -b*100, -b, 0, b, b*100, s2])
dt_ustel = 2*I/c0                     # gidis-donus
dt_1mert = 2*(2*mu/c0)*log(4*r1*r2/b**2)
print(f"  USTEL (tam)          = {mp.nstr(dt_ustel*1e6, 8)} mus")
print(f"  birinci mertebe log  = {mp.nstr(dt_1mert*1e6, 8)} mus")
print(f"  kitaptaki kayit      = 247 mus ; olculen ~250 mus (Viking)")
print()

print("="*80)
print("4) GOLGE — Sgr A* ve M87* icin mikroarcsec")
print("="*80)
Msun = mpf('1.98892e30'); G = mpf('6.67430e-11'); pc = mpf('3.0857e16')
uas = mpf(180)*3600*1e6/pi
for ad, M_, D_ in [("Sgr A*", mpf('4.297e6')*Msun, mpf('8277')*pc),
                   ("M87*",   mpf('6.5e9')*Msun,  mpf('16.8e6')*pc)]:
    m_ = G*M_/c0**2
    b_ust = 2*exp(1)*m_          # 2e mu
    b_gr  = 3*sqrt(3)*m_
    cap_u = 2*b_ust/D_*uas; cap_g = 2*b_gr/D_*uas
    print(f"  {ad:<8} mu = {mp.nstr(m_/1e9,5)}e9 m | GR golge capi = {mp.nstr(cap_g,6)} uas"
          f" | USTEL = {mp.nstr(cap_u,6)} uas | fark = +{mp.nstr((cap_u/cap_g-1)*100,4)}%")
print("  EHT olcumu: Sgr A* halka capi 51.8 +/- 2.3 uas ; M87* 42 +/- 3 uas")
print("  (halka capi = golge capi degildir; halka, golgenin hemen disindaki isima tepesidir —")
print("   EHT'nin yayinladigi kisit 'golge capi/GR ongorusu' oraninda ~%10 duzeyindedir)")
