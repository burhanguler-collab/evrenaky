# -*- coding: utf-8 -*-
"""
GUNBERI SINAVI — YUKSEK HASSASIYET (mpmath, 60 hane)
=====================================================
Neden gerekli: presesyon, 2*pi mertebesinde iki acinin ~1e-7'lik farkidir;
apsis sabitlerinin cozumunde (Lambda2^2 - Lambda1^2 ~ 1e-8) float64 sekiz hane
iptal yer. 60 haneyle sorun tamamen kalkar.

Teorinin kendi eyleminden (GR formulu YOK):
   S = -m c0^2 int Lambda(r) sqrt(1 - V^2/c_loc^2) dt ,  c_loc = c0 Lambda^2
=> (dx/dphi)^2 = (A - B Lambda^2)/Lambda^4 - x^2 ,  x = mu/r
   A = k eps^2 , B = k = c0^2 mu^2/lam^2  (apsislerden cozulur)
Yarim yorunge acisi = int_{x1}^{x2} dx / sqrt(Phi(x))  (tanh-sinh, uc tekilligi)
Presesyon = 2*yarim - 2*pi

Iki aday:  USTEL Lambda = exp(-x)   |   LINEER Lambda = 1 - x
Analitik beklenti (bagimsiz turetim): Lambda = 1 - x + kappa x^2/2 + ... icin
   beta = (1+kappa)/2 ,  gamma = 1 ,  presesyon olcegi = (2+2gamma-beta)/3 = (7-kappa)/6
   USTEL  kappa=1 -> olcek 1      (GR ile ayni; 42.98 as/yy)
   LINEER kappa=0 -> olcek 7/6    (50.14 as/yy — dislanir)
"""
from mpmath import mp, mpf, exp, sqrt, pi, quad, sin, cos

mp.dps = 60

c0    = mpf('2.99792458e8')
AU    = mpf('1.495978707e11')
GMsun = mpf('1.32712440018e20')
mu    = GMsun/c0**2
arcsec = 180*3600/pi

def L_ustel(x):  return exp(-x)
def L_lineer(x): return 1 - x

def presesyon(Lam, a, e):
    x1 = mu/(a*(1+e))          # aphelion (kucuk x)
    x2 = mu/(a*(1-e))          # gunberi  (buyuk x)
    L1 = Lam(x1); L2 = Lam(x2)
    # A - B L1^2 = x1^2 L1^4 ;  A - B L2^2 = x2^2 L2^4
    B = (x1**2*L1**4 - x2**2*L2**4)/(L2**2 - L1**2)
    A = x1**2*L1**4 + B*L1**2
    def Phi(x):
        L = Lam(x)
        return (A - B*L**2)/L**4 - x**2
    # uc tekilligini yumusatmak icin x = m + h sin(t)
    m = (x1+x2)/2; h = (x2-x1)/2
    def integrand(t):
        x = m + h*sin(t)
        val = Phi(x)
        # sqrt(Phi) ~ h cos(t) * sqrt(Gf) ;  integrand = 1/sqrt(Gf)
        den = (x-x1)*(x2-x)
        if den <= 0:
            # uc: limit degeri, Phi'/(...) ile
            return mpf(0)
        return sqrt(den/val)/ (h*cos(t)) * (h*cos(t))  # = sqrt(den/val)
    # dphi = dx/sqrt(Phi) = h cos t dt / sqrt(Phi) ; sqrt(den)=h cos t
    # => dphi = sqrt(den/Phi) dt
    yarim = quad(integrand, [-pi/2, pi/2])
    return 2*yarim - 2*pi

print("="*84)
print("GUNBERI PRESESYONU — mpmath 60 hane, teorinin kendi eyleminden")
print("="*84)
gez = [("Merkur",      mpf('0.38709893')*AU, mpf('0.20563069'), mpf('0.2408467')),
       ("Venus",       mpf('0.72333199')*AU, mpf('0.00677323'), mpf('0.61519726')),
       ("Dunya",       mpf('1.00000011')*AU, mpf('0.01671022'), mpf('1.0000174')),
       ("Mars",        mpf('1.52366231')*AU, mpf('0.09341233'), mpf('1.8808476')),
       ("Ikaros 1566", mpf('1.0779')*AU,     mpf('0.8268'),     mpf('1.1190'))]

print(f"{'gezegen':<13}{'USTEL as/yy':>15}{'LINEER as/yy':>15}{'GR as/yy':>13}{'ustel/GR':>13}{'lin/GR':>11}")
sonuc = {}
for ad, a, e, Pyr in gez:
    n = 100/Pyr
    pu = presesyon(L_ustel,  a, e)*n*arcsec
    pl = presesyon(L_lineer, a, e)*n*arcsec
    gr = 6*pi*mu/(a*(1-e**2))*n*arcsec
    sonuc[ad] = (pu, pl, gr)
    print(f"{ad:<13}{mp.nstr(pu,8):>15}{mp.nstr(pl,8):>15}{mp.nstr(gr,8):>13}"
          f"{mp.nstr(pu/gr,10):>13}{mp.nstr(pl/gr,8):>11}")

print()
print("  Merkur olculen artik: 42.9799 +/- 0.0009 as/yy  (Park ve ark. 2017)")
pu, pl, gr = sonuc["Merkur"]
print(f"  USTEL  Merkur = {mp.nstr(pu,8)} as/yy  ->  gozlemden sapma = "
      f"{mp.nstr((pu-mpf('42.9799'))/mpf('0.0009'),4)} sigma")
print(f"  LINEER Merkur = {mp.nstr(pl,8)} as/yy  ->  gozlemden sapma = "
      f"{mp.nstr((pl-mpf('42.9799'))/mpf('0.0009'),4)} sigma")
print()
print("  Beklenen olcek (analitik): USTEL 1 (tam), LINEER 7/6 = 1.1666667")
print(f"  Olculen oran ortalamasi:   USTEL {mp.nstr(sum(sonuc[k][0]/sonuc[k][2] for k in sonuc)/len(sonuc),10)}"
      f"   LINEER {mp.nstr(sum(sonuc[k][1]/sonuc[k][2] for k in sonuc)/len(sonuc),10)}")
