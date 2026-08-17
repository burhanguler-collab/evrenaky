# -*- coding: utf-8 -*-
"""
TURETIM SINAVI — ustel_turetim_uc_yol.md'nin iddialarini sayisal dogrula
========================================================================
1) Tepki ussu ailesi:  dP/dchi = -C (P/P0)^n  ->  beta = 2n-1 ;  Merkur'un
   hassasiyeti n'yi ne kadar kilitler?
2) Carpimsal bilesim (Yol 2): Lambda(U1+U2) = Lambda(U1)Lambda(U2) yalniz ustelde;
   lineer yazimin ihlali ne mertebede ve GPS/LLR hassasiyetinde gorunur mu?
3) Ikinci mertebe belirsizligi: (a) Lambda=1-U ve (b) P dogrusal okumalari farkli beta veriyor mu?
"""
from mpmath import mp, mpf, exp, sqrt, pi, log, quad, sin
mp.dps = 50

c0 = mpf('2.99792458e8'); AU = mpf('1.495978707e11')
GMsun = mpf('1.32712440018e20'); mu = GMsun/c0**2
arcsec = 180*3600/pi

# ---------- 1) tepki ussu ailesi ----------
def Lam_n(x, n):
    """P = P0 [1-(1-n) 4x]^(1/(1-n)) ; Lambda = (P/P0)^(1/4)"""
    if abs(n-1) < mpf('1e-30'):
        return exp(-x)
    m = 1-n
    return (1 - 4*m*x)**(mpf(1)/(4*m))

def beta_num(n):
    """Lambda = 1 - x + kappa x^2/2 -> beta = (1+kappa)/2, sayisal ikinci turevle"""
    h = mpf('1e-12')
    L = lambda x: Lam_n(x, n)
    # kappa = L''(0)
    kappa = (L(h) - 2*L(mpf(0)) + L(-h))/h**2
    return (1+kappa)/2

def presesyon(n, a, e):
    Lam = lambda x: Lam_n(x, n)
    x1 = mu/(a*(1+e)); x2 = mu/(a*(1-e))
    L1, L2 = Lam(x1), Lam(x2)
    B = (x1**2*L1**4 - x2**2*L2**4)/(L2**2 - L1**2)
    A = x1**2*L1**4 + B*L1**2
    m_, h_ = (x1+x2)/2, (x2-x1)/2
    def f(t):
        x = m_ + h_*sin(t); L = Lam(x)
        Phi = (A - B*L**2)/L**4 - x**2
        den = (x-x1)*(x2-x1+ (x2-x))*0  # placeholder
        den = (x-x1)*(x2-x)
        if den <= 0: return mpf(0)
        return sqrt(den/Phi)
    return 2*quad(f, [-pi/2, pi/2]) - 2*pi

print("="*78)
print("1) TEPKI USSU AILESI:  beta = 2n-1  iddiasi")
print("="*78)
a_m, e_m, P_m = mpf('0.38709893')*AU, mpf('0.20563069'), mpf('0.2408467')
gr = 6*pi*mu/(a_m*(1-e_m**2))*(100/P_m)*arcsec
print(f"{'n':>8}{'beta (say.)':>14}{'beta=2n-1':>12}{'Merkur as/yy':>15}{'olcek':>10}")
for n in ['0', '0.5', '0.9', '1', '1.1', '1.5']:
    nn = mpf(n)
    b = beta_num(nn)
    pm = presesyon(nn, a_m, e_m)*(100/P_m)*arcsec
    print(f"{n:>8}{mp.nstr(b,7):>14}{mp.nstr(2*nn-1,5):>12}{mp.nstr(pm,8):>15}{mp.nstr(pm/gr,7):>10}")
print(f"\n  GR/gozlem = {mp.nstr(gr,8)} as/yy ; olculen 42.9799 +/- 0.0009")
# n'nin kilitlenmesi: dP/dn ~ ?  olcek = (7-kappa)/6 = (7-(4n-3))/6 = (10-4n)/6
# 42.9799 +/- 0.0009 -> olcek 1 +/- 0.0009/42.98 = 1 +/- 2.09e-5
# olcek = (10-4n)/6 = 1 -> n=1 ; d(olcek)/dn = -4/6 -> dn = 2.09e-5 * 6/4
dn = mpf('0.0009')/mpf('42.9799') * 6/4
print(f"  -> gozlem n'yi kilitler: n = 1.000000 +/- {mp.nstr(dn,3)}  (yani {mp.nstr(dn,3)} hassasiyetle)")

# ---------- 2) carpimsal bilesim ----------
print()
print("="*78)
print("2) CARPIMSAL BILESIM:  Lambda(U1+U2) =? Lambda(U1)*Lambda(U2)")
print("="*78)
GMearth = mpf('3.986004418e14'); Rearth = mpf('6.371e6')
U_e = GMearth/(c0**2*Rearth)            # Dunya yuzeyi
U_s = GMsun/(c0**2*AU)                  # Gunes'in Dunya yorungesindeki potansiyeli
print(f"  U_Dunya(yuzey) = {mp.nstr(U_e,6)} ,  U_Gunes(1AU) = {mp.nstr(U_s,6)}")
for ad, L in [("USTEL  e^-U", lambda U: exp(-U)), ("LINEER 1-U", lambda U: 1-U)]:
    ihlal = L(U_e)*L(U_s) - L(U_e+U_s)
    print(f"  {ad:<14} ihlal = Lambda1*Lambda2 - Lambda(U1+U2) = {mp.nstr(ihlal,6)}")
print(f"  Lineer ihlalin buyuklugu = U_e*U_s = {mp.nstr(U_e*U_s,6)}")
print("  Gozlem hassasiyetleri: optik saat karsilastirmalari ~1e-18 ; GPS ~1e-15")
print(f"  -> lineer ihlal {mp.nstr(U_e*U_s,3)} , 1e-18 bandinin"
      f" {'ALTINDA (gorunmez)' if U_e*U_s < mpf('1e-18') else 'USTUNDE (ilkece gorunur)'}")
print("  NOT: bu, lineer yazimin GOZLEMSEL degil YAPISAL sorunudur — kitabin kendi")
print("       Lambda = Lambda_grav*Lambda_kin carpimsalligiyla ikinci mertebede celisir.")

# ---------- 3) ikinci mertebe belirsizligi ----------
print()
print("="*78)
print("3) IKINCI MERTEBE BELIRSIZLIGI (mevcut kitabin iki okumasi ayrisiyor mu?)")
print("="*78)
def beta_of(Lfun):
    h = mpf('1e-12')
    kappa = (Lfun(h) - 2*Lfun(mpf(0)) + Lfun(-h))/h**2
    return (1+kappa)/2
okumalar = [("(a) Lambda = 1-U  (M-42 yazimi harfiyen)", lambda U: 1-U),
            ("(b) P = P0(1-4U) => Lambda=(1-4U)^(1/4)", lambda U: (1-4*U)**(mpf(1)/4)),
            ("(c) USTEL Lambda = e^-U", lambda U: exp(-U))]
for ad, Lf in okumalar:
    b = beta_of(Lf)
    olcek = (2+2*1-b)/3
    print(f"  {ad:<42} beta = {mp.nstr(b,6):>10}   Merkur = {mp.nstr(olcek*gr,7):>9} as/yy")
print("  -> (a) ve (b) FARKLI beta veriyor: lineer yazim ikinci mertebede TANIMSIZ.")
print("     (c) tek tutarli aile: Lambda ve P ayni fonksiyonel bicimi tasir.")
