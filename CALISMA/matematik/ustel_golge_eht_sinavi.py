# -*- coding: utf-8 -*-
"""
EHT GOLGE SINAVI — USTEL YAPI vs GR vs LINEER KESIM
====================================================
Ortam optigi (Evrenaki, ustel yazim):
    Lambda(r) = exp(-Phi/c0^2) = exp(-mu/r) ,  mu = G M/c0^2 ,  Phi = +GM/r (kuyu derinligi)
    c_loc = c0 Lambda^2 = c0 exp(-2mu/r)        (koordinat yayilma hizi)
    n_eff = c0/c_loc = 1/Lambda^2 = exp(+2mu/r)
Etkin yapi izotropiktir:  g_tt = -Lambda^2 c0^2 , g_ij = Lambda^-2 delta_ij
=> Bouguer/Snell degismezi  b = n(r) r = r/Lambda^2  (null jeodezik L/E ile AYNI, asagida kanitlanir)

Adaylar:
  USTEL      : n = exp(2mu/r)                  (Lambda = exp(-mu/r))
  GR-Schw    : b = r/sqrt(1-2mu/r)             (Schwarzschild radyal koordinat)
  GR-izo     : n = (1+mu/2r)^3/(1-mu/2r)       (ayni fizik, izotropik koordinat -> ayni b_krit)
  LINEER-P   : P = P0(1-4mu/r), c_loc=c0 sqrt(1-4mu/r), n=(1-4mu/r)^-1/2   [gercek lineer yanit]
  LINEER-L   : Lambda = 1-mu/r, n = (1-mu/r)^-2                            [M-42 yazimi]
"""
from mpmath import (mp, mpf, exp, sqrt, pi, quad, findroot, log, diff, sin, cos,
                    mpmathify, nstr, e as mp_e)

mp.dps = 50

# ---------- sabitler ----------
c0    = mpf('2.99792458e8')
G     = mpf('6.67430e-11')
GMsun = mpf('1.32712440018e20')          # IAU
Msun  = GMsun/G
pc    = mpf('3.0856775814913673e16')
AU    = mpf('1.495978707e11')
uas   = mpf(180)*3600*mpf('1e6')/pi      # rad -> mikroarcsec
arcmin= mpf(180)*60/pi                   # rad -> arcmin
P0    = mpf('6.07e33')
rho_n = 4*P0/c0**2

SEP = "="*94
def head(t):
    print("\n"+SEP); print(t); print(SEP)

# =====================================================================
# 1) BOUGUER DEGISMEZI ve FOTON KURESI — ANALITIK ADIMLAR
# =====================================================================
head("1) TURETIM: b = n(r) r  ve  d/dr[r exp(2mu/r)] = 0  ->  r_ph = 2mu ,  b_krit = 2 e mu")

print("""
(1a) Null jeodezik <-> Bouguer esdegerligi (mu=1 birimlerinde gosterilir):
     ds^2 = -Lambda^2 c0^2 dt^2 + Lambda^-2 (dr^2 + r^2 dphi^2)
     E = Lambda^2 c0^2 t' ,  L = Lambda^-2 r^2 phi'
     Null kosulu:  r'^2 = E^2/c0^2 - L^2 Lambda^4 / r^2
     Donum noktasi r'=0  ->  b := c0 L/E = r/Lambda^2 = n(r) r        [Bouguer'in ta kendisi]
     Foton kuresi: V_eff = L^2 Lambda^4/r^2 tepesi  <=>  W(r)=Lambda^2/r = 1/(n r) MAKSIMUMU
                   <=>  n(r) r MINIMUMU.  b_krit = min_r [ n(r) r ].

(1b) USTEL icin kapali cozum:
     d/dr [ r e^{2mu/r} ] = e^{2mu/r} (1 - 2mu/r) = 0   ->   r_ph = 2 mu
     b_krit = r_ph * e^{2mu/r_ph} = 2mu * e^1 = 2 e mu = 5.436563656... mu
     GR:  b_krit = 3 sqrt(3) mu = 5.196152423... mu
     oran = 2e/(3 sqrt 3) = 1.0462670...  ->  +4.6267 %
""")

# --- sembolik dogrulama (sympy) ---
try:
    import sympy as sp
    r, m = sp.symbols('r m', positive=True)
    for ad, nexp in [("USTEL", sp.exp(2*m/r)),
                     ("LINEER-P", (1-4*m/r)**sp.Rational(-1,2)),
                     ("LINEER-L", (1-m/r)**-2)]:
        expr = sp.simplify(sp.diff(r*nexp, r))
        kok  = sp.solve(sp.Eq(expr, 0), r)
        kok  = [k for k in kok if sp.simplify(k/m).is_positive]
        bcr  = [sp.simplify((r*nexp).subs(r, k)) for k in kok]
        print(f"  sympy {ad:<9} d/dr[n r] = {expr}")
        print(f"        r_ph = {kok}   b_krit = {bcr}")
    # GR Schwarzschild dogrudan b(r)=r/sqrt(1-2m/r)
    bgr = r/sp.sqrt(1-2*m/r)
    kok = sp.solve(sp.Eq(sp.simplify(sp.diff(bgr, r)), 0), r)
    print(f"  sympy GR-Schw   r_ph = {kok}   b_krit = {[sp.simplify(bgr.subs(r,k)) for k in kok]}")
    # GR izotropik
    niso = (1+m/(2*r))**3/(1-m/(2*r))
    kok = sp.solve(sp.Eq(sp.simplify(sp.diff(r*niso, r)), 0), r)
    kok = [k for k in kok if sp.simplify(k/m).is_positive]
    print(f"  sympy GR-izo    r_ph = {[sp.nsimplify(k/m) for k in kok]} * mu   "
          f"b_krit = {[sp.simplify(sp.radsimp((r*niso).subs(r,k)/m)) for k in kok]} * mu")
    print(f"                  (sayisal: {[sp.N((r*niso).subs(r,k)/m, 12) for k in kok]} ; "
          f"3sqrt3 = {sp.N(3*sp.sqrt(3),12)})")
except Exception as ex:
    print("  [sympy adimi atlandi]", ex)

# ---------- profil tanimlari (mu = 1 birimi) ----------
def n_ustel(x):    return exp(2/x)                     # x = r/mu
def n_linP(x):     return 1/sqrt(1-4/x)
def n_linL(x):     return 1/(1-1/x)**2
def n_griso(x):    return (1+1/(2*x))**3/(1-1/(2*x))
def b_grschw(x):   return x/sqrt(1-2/x)                # b(r) dogrudan

PROFIL = {
    "USTEL      (n=e^{2mu/r})"      : (lambda x: x*n_ustel(x), mpf('2.5')),
    "GR-Schw    (b=r/sqrt(1-2mu/r))": (b_grschw,               mpf('3.5')),
    "GR-izo     (izotropik n)"      : (lambda x: x*n_griso(x), mpf('2.0')),
    "LINEER-P   (n=(1-4mu/r)^-1/2)" : (lambda x: x*n_linP(x),  mpf('7.0')),
    "LINEER-L   (n=(1-mu/r)^-2)"    : (lambda x: x*n_linL(x),  mpf('3.5')),
}

head("1c) SAYISAL: b(r) = n(r) r fonksiyonunun minimumu (mu = 1 birimi)")
print(f"  {'profil':<32}{'r_ph/mu':>16}{'b_krit/mu':>20}{'b/b_GR':>14}{'fark %':>12}")
bGR = 3*sqrt(3)
bkrit = {}
for ad, (bf, x0) in PROFIL.items():
    rph = findroot(lambda x: diff(bf, x), x0)
    bc  = bf(rph)
    bkrit[ad] = (rph, bc)
    print(f"  {ad:<32}{nstr(rph,12):>16}{nstr(bc,14):>20}{nstr(bc/bGR,8):>14}"
          f"{nstr((bc/bGR-1)*100,6):>12}")
print(f"\n  kapali degerler:  2e = {nstr(2*mp_e,14)}   3sqrt3 = {nstr(3*sqrt(3),14)}   "
      f"6sqrt3 = {nstr(6*sqrt(3),14)}   27/4 = {nstr(mpf(27)/4,14)}")
print(f"  USTEL/GR = 2e/(3sqrt3) = {nstr(2*mp_e/(3*sqrt(3)),12)}  ->  "
      f"+{nstr((2*mp_e/(3*sqrt(3))-1)*100,6)} %")

# =====================================================================
# 2) KOORDINAT BAGIMSIZLIGI: b, asimptotik carpisma parametresi mi?
# =====================================================================
head("2) KOORDINAT BAGIMSIZLIK DENETIMI — b gercekten asimptotik carpisma parametresi mi?")

print("""
Denetim-A (ic tutarlilik): GR'in AYNI fizigi iki koordinatta.
   Schwarzschild r'sinde b_krit = 3sqrt3 mu (r_ph = 3mu).
   Izotropik r'de     r_ph = (1+sqrt3/2) mu = 1.8660 mu  AMA  b_krit = ayni 3sqrt3 mu.
   -> r_ph koordinat-bagimli, b_krit DEGIL. Karsilastirma b uzerinden yapilmalidir. (yukarida dogrulandi)
Denetim-B (operasyonel): b, uzaktaki gozlemcinin isin asimptotuna olan dik uzakligidir;
   her iki teoride de asimptotik bolge duz (n->1, Lambda->1), oradaki uzunluk = ozuzunluk.
   Golgenin acisal yaricapi = b_krit / D. Asagida sapma acisinin asimptotundan sayisal olarak dogrulanir.
""")

def sapma(bf, b, xmax=mpf('1e12')):
    """alpha(b) = 2 int b dr/(r sqrt(n^2r^2-b^2)) - pi, w=r0/r ve w=1-s^2 donusumu ile.
       bf(x) = n(x) x oldugundan integrand = 2 b s ds / sqrt(bf(r0/w)^2 - b^2 w^2)."""
    r0 = findroot(lambda x: bf(x) - b, b)
    def f(s):
        w = 1 - s**2
        if w <= 0: return mpf(0)
        rad = bf(r0/w)**2 - b**2*w**2
        if rad <= 0: return mpf(0)
        return 2*b*s/sqrt(rad)
    I = quad(f, [0, mpf('1e-8'), mpf('1e-4'), mpf('1e-2'), mpf('0.3'), mpf('0.7'), 1])
    return 2*I - pi

bf_u = PROFIL["USTEL      (n=e^{2mu/r})"][0]
bf_g = PROFIL["GR-Schw    (b=r/sqrt(1-2mu/r))"][0]
print(f"  {'b/mu':>10}{'alpha USTEL (rad)':>24}{'alpha GR (rad)':>22}{'1.mert 4mu/b':>18}{'ustel/GR':>13}")
for bb in [mpf('1e6'), mpf('1e4'), mpf(100), mpf(20), mpf(10)]:
    au = sapma(bf_u, bb); ag = sapma(bf_g, bb)
    print(f"  {nstr(bb,6):>10}{nstr(au,12):>24}{nstr(ag,12):>22}{nstr(4/bb,12):>18}{nstr(au/ag,10):>13}")
print("  -> zayif alanda her iki profil de alpha -> 4mu/b (ayni asimptotik b tanimi). OK")

# =====================================================================
# 3) GOZLEM: Sgr A* ve M87* — mikroarcsec
# =====================================================================
head("3) GOZLEMSEL KARSILASTIRMA — golge acisal capi (mikroarcsec)")

FAKTOR = {"GR": 2*3*sqrt(3), "USTEL": 2*2*mp_e, "LINEER-P": 2*6*sqrt(3), "LINEER-L": 2*mpf(27)/4}

kaynak = [
    ("Sgr A* (GRAVITY'21 onceli)", mpf('4.297e6'), mpf('0.013e6'), mpf('8277')*pc,  mpf('9')*pc),
    ("Sgr A* (Keck/Do'19 onceli)", mpf('3.951e6'), mpf('0.047e6'), mpf('7935')*pc,  mpf('50')*pc),
    ("Sgr A* (gorev verisi 4.3e6, 8.15 kpc)", mpf('4.3e6'), mpf('0.02e6'), mpf('8150')*pc, mpf('100')*pc),
    ("M87*  (yildiz dinamigi 6.2e9)", mpf('6.2e9'), mpf('0.9e9'),  mpf('16.8e6')*pc, mpf('0.8e6')*pc),
    ("M87*  (EHT'nin kendi cikarimi 6.5e9)", mpf('6.5e9'), mpf('0.7e9'), mpf('16.8e6')*pc, mpf('0.8e6')*pc),
]
tg_kayit = {}
for ad, M, dM, D, dD in kaynak:
    mu_ = G*M*Msun/c0**2
    th_g = mu_/D*uas                                 # mikroarcsec cinsinden mu/D
    rel  = sqrt((dM/M)**2 + (dD/D)**2)
    tg_kayit[ad] = (mu_, th_g, rel)
    print(f"\n  {ad}")
    print(f"    mu = {nstr(mu_,8)} m   theta_g = mu/D = {nstr(th_g,7)} uas  "
          f"(+/- {nstr(th_g*rel,4)} , %{nstr(rel*100,3)})")
    for k in ["GR", "USTEL", "LINEER-P", "LINEER-L"]:
        cap = FAKTOR[k]*th_g
        print(f"    {k:<9} golge capi = {nstr(cap,7):>10} uas   (+/- {nstr(cap*rel,4)} onculden)")

# --- EHT halka olcumleri ve delta kisiti ---
head("3b) EHT HALKA OLCUMU ile karsilastirma  (halka capi != golge capi; EHT'nin delta'si esas)")
olcum = [
    ("Sgr A*", mpf('51.8'), mpf('2.3'), "Sgr A* (GRAVITY'21 onceli)"),
    ("M87*",   mpf('42.0'), mpf('3.0'), "M87*  (yildiz dinamigi 6.2e9)"),
]
print(f"  {'kaynak':<9}{'halka olculen':>18}{'GR golge':>12}{'USTEL golge':>14}"
      f"{'LIN-P':>10}{'LIN-L':>10}")
for ad, dobs, ddobs, anahtar in olcum:
    _, th_g, rel = tg_kayit[anahtar]
    print(f"  {ad:<9}{nstr(dobs,4)+' +/- '+nstr(ddobs,3):>18}"
          f"{nstr(FAKTOR['GR']*th_g,5):>12}{nstr(FAKTOR['USTEL']*th_g,5):>14}"
          f"{nstr(FAKTOR['LINEER-P']*th_g,5):>10}{nstr(FAKTOR['LINEER-L']*th_g,5):>10}")

print("""
  EHT'nin yayinladigi kesirli sapma:  delta = theta_golge / theta_golge,Schw - 1
    Sgr A* (EHT 2022, VI. makale):  delta = -0.04 (+0.09/-0.10)  [VLTI onceli]
                                    delta = -0.08 (+0.09/-0.09)  [Keck onceli]
    M87*   (EHT 2019, VI. makale):  golge capi Kerr ongorusunun %17'si icinde
                                    (yildiz-dinamigi kutlesiyle kabaca -0.01 < delta < +0.17)
""")
teori_delta = {"GR": mpf(0), "USTEL": 2*mp_e/(3*sqrt(3))-1,
               "LINEER-P": mpf(2)-1, "LINEER-L": (mpf(27)/4)/(3*sqrt(3))-1}
kisit = [("Sgr A* VLTI onceli", mpf('-0.04'), mpf('0.095')),
         ("Sgr A* Keck onceli", mpf('-0.08'), mpf('0.09')),
         ("M87* yildiz-din.",   mpf('0.08'),  mpf('0.09'))]
print(f"  {'aday':<10}{'delta_teori':>14}   " + "".join(f"{k:>26}" for k,_,_ in kisit))
for k in ["GR", "USTEL", "LINEER-L", "LINEER-P"]:
    dt = teori_delta[k]
    sat = f"  {k:<10}{nstr(dt,5):>14}   "
    for ad, dc, sg in kisit:
        z = (dt-dc)/sg
        hk = "UYUMLU" if abs(z) <= 2 else ("SINIRDA" if abs(z) <= 3 else "DISLANIR")
        sat += f"{nstr(z,3)+' sigma '+hk:>26}"
    print(sat)

# =====================================================================
# 4) LYAPUNOV USU / HALKA YAPISI
# =====================================================================
head("4) HALKA YAPISI — kritik yorunge Lyapunov usu ve guclu-sapma katsayilari")
print("""
  Kararsizlik usu k:  delta_r ~ exp(k * phi).  Yariturdan yarituraya sonmelenme = e^{-k*pi}.
  Turetim: (dr/dphi)^2 = (n r)^2 [ 1/b^2 - W^2 ] / ... , W = 1/(n r) ;  kritik noktada
     k = (r_c^2 n_c) * sqrt( -W_c W''(r_c) )        [n_c r_c = b_c , W_c = 1/b_c]
  GR-Schwarzschild icin k = 1  ->  gamma_Lyap = k*pi = pi  (e^{-pi} = 0.0432 sonmelenme).
""")
def lyapunov(bf, rph):
    W  = lambda x: 1/bf(x)
    Wc = W(rph); W2 = diff(W, rph, 2)
    return bf(rph)*rph*sqrt(-Wc*W2)          # = (r_c^2 n_c) sqrt(-Wc W'')
print(f"  {'profil':<32}{'r_ph/mu':>12}{'b_krit/mu':>14}{'k (Lyapunov)':>16}"
      f"{'gamma=k*pi':>14}{'e^-gamma':>13}")
for ad, (bf, x0) in PROFIL.items():
    rph, bc = bkrit[ad]
    k = lyapunov(bf, rph)
    print(f"  {ad:<32}{nstr(rph,8):>12}{nstr(bc,10):>14}{nstr(k,12):>16}"
          f"{nstr(k*pi,10):>14}{nstr(exp(-k*pi),8):>13}")

print("\n  Guclu-sapma limiti:  alpha(b) = -abar*ln(b/b_krit - 1) + bbar ,  abar = 1/k beklenir")
for ad in ["USTEL      (n=e^{2mu/r})", "GR-Schw    (b=r/sqrt(1-2mu/r))"]:
    bf = PROFIL[ad][0]; rph, bc = bkrit[ad]
    pts = []
    for eps in [mpf('1e-4'), mpf('1e-6'), mpf('1e-8')]:
        pts.append((eps, sapma(bf, bc*(1+eps))))
    # iki nokta ile abar, bbar
    (e1,a1),(e2,a2) = pts[0], pts[2]
    abar = (a2-a1)/(log(e1)-log(e2))
    bbar = a1 + abar*log(e1)
    print(f"    {ad:<32} abar = {nstr(abar,10)}   bbar = {nstr(bbar,10)}   "
          f"(alpha at eps=1e-6: {nstr(pts[1][1],10)} rad)")

# =====================================================================
# 5) ISCO ve DISK IC KENARI  (halka parlaklik yapisini etkiler)
# =====================================================================
head("5) ISCO — kutlesel parcacik icin en ic kararli dairesel yorunge")
print("""
  V_eff(r) = Lambda^2 c0^2 + L^2 Lambda^4/r^2  (etkin yapidan; teorinin eyleminden ayni)
  u = mu/r ,  Vt = V/c0^2 = e^{-2u} + l^2 u^2 e^{-4u} ,  l = L/(c0 mu)
  dVt/du = 0 -> l^2 = e^{2u}/(u(1-2u)) ;  d^2Vt/du^2 = 0 ile birlikte:
     4u^2 - 6u + 1 = 0  ->  u = (3-sqrt5)/4  ->  r_ISCO = (3+sqrt5) mu = 5.2360679... mu
  GR: r_ISCO = 6 mu.  Oran r_ISCO/r_ph:  ustel 5.236/2 = 2.618 (= phi^2) ; GR 6/3 = 2.
""")
u = (3-sqrt(5))/4
r_isco = 1/u
l2 = exp(2*u)/(u*(1-2*u))
Vt = exp(-2*u) + l2*u**2*exp(-4*u)
E_isco = sqrt(Vt)
print(f"  USTEL : u_ISCO = {nstr(u,12)}   r_ISCO = {nstr(r_isco,12)} mu  (= 3+sqrt5 = {nstr(3+sqrt(5),12)})")
print(f"          l^2 = {nstr(l2,10)} ,  E/mc0^2 = {nstr(E_isco,12)} ,  "
      f"baglanma verimi = {nstr((1-E_isco)*100,6)} %")
print(f"  GR    : r_ISCO = 6 mu , E/mc0^2 = sqrt(8/9) = {nstr(sqrt(mpf(8)/9),12)} , "
      f"verim = {nstr((1-sqrt(mpf(8)/9))*100,6)} %")
# sayisal dogrulama
def Vfun(uu, ll2): return exp(-2*uu) + ll2*uu**2*exp(-4*uu)
d1 = diff(lambda uu: Vfun(uu, l2), u); d2 = diff(lambda uu: Vfun(uu, l2), u, 2)
print(f"  dogrulama: dV/du = {nstr(d1,6)} , d2V/du2 = {nstr(d2,6)}  (ikisi de ~0 olmali)")
print(f"  -> ustel ISCO GR'dan %{nstr((1-r_isco/6)*100,5)} DAHA IC; disk ic kenari ve QPO"
      f" frekanslari farkli (kutle-dejenere sinav)")

# =====================================================================
# 6) GOLGE GERCEK MI? — cismin yaricapi foton kuresinin icinde mi (UFUK YOK)
# =====================================================================
head("6) UFUKSUZ GOLGE DENETIMI — b<b_krit isinlari cisme carpiyor mu?")
print(f"  rho_n = 4 P0/c0^2 = {nstr(rho_n,8)} kg/m^3   (P0 = {nstr(P0,5)} Pa, M-8)")
for ad, M, dM, D, dD in kaynak[:1] + kaynak[3:4]:
    mu_ = G*M*Msun/c0**2
    Rr = (3*M*Msun/(4*pi*rho_n))**(mpf(1)/3)
    print(f"  {ad:<40} R_rho = {nstr(Rr,6)} m ; r_ph = 2mu = {nstr(2*mu_,6)} m ; "
          f"r_ph/R_rho = {nstr(2*mu_/Rr,6)}")
# b<b_krit isini ic bolgede donum noktasi bulur mu?
print("\n  Ic bolge: r'^2 = E^2/c0^2 - L^2 Lambda^4/r^2 ; Lambda^4/r^2 = e^{-4mu/r}/r^2 -> 0  (r->0)")
print("  yani b < b_krit isini HICBIR ic donum noktasi bulamaz, r=0'a dogru duser ve cisme carpar.")
for xx in [mpf('1.5'), mpf('1.0'), mpf('0.5'), mpf('0.1'), mpf('0.01')]:
    print(f"    r = {nstr(xx,4):>7} mu :  L^2Lambda^4/r^2 olcegi (1/b^2 birimi) = "
          f"{nstr((exp(-2/xx)/xx)**2,6)}   (b_krit^-2 = {nstr(1/(2*mp_e)**2,6)})")
print("  -> GOLGE ufuk gerektirmez: sogurucu KATI/YOGUN cisim + foton kuresi yeterli.")
# M_min
def Mmin():
    f = lambda Mkg: 2*G*Mkg/c0**2 - (3*Mkg/(4*pi*rho_n))**(mpf(1)/3)
    return findroot(f, mpf('1.6e31'))
Mm = Mmin()
print(f"  M_min (r_ph = R_rho) = {nstr(Mm,6)} kg = {nstr(Mm/Msun,6)} Msun  -> GOLGE esigi")

# =====================================================================
# 7) S2 / GRAVITY PRESESYONU
# =====================================================================
head("7) S2 YILDIZI — Schwarzschild presesyonu (GRAVITY 2020)")
mu_sgr = G*mpf('4.297e6')*Msun/c0**2
a_S2 = mpf('125.058e-3')/206264.806*mpf('8246.7')*pc     # 125.058 mas @ 8246.7 pc
e_S2 = mpf('0.884649')
rp_S2 = a_S2*(1-e_S2)
print(f"  mu(Sgr A*) = {nstr(mu_sgr,8)} m = {nstr(mu_sgr/AU,6)} AU")
print(f"  S2: a = {nstr(a_S2/AU,7)} AU , e = {nstr(e_S2,7)} , r_peri = {nstr(rp_S2/AU,6)} AU"
      f" = {nstr(rp_S2/mu_sgr,7)} mu")
print(f"  mu/r_peri = {nstr(mu_sgr/rp_S2,6)}   ->  2PN duzeltmesi ~ (mu/r)^2 = "
      f"{nstr((mu_sgr/rp_S2)**2,5)}")

def presesyon(Lam, a, e, muv):
    x1 = muv/(a*(1+e)); x2 = muv/(a*(1-e))
    L1 = Lam(x1); L2 = Lam(x2)
    B = (x1**2*L1**4 - x2**2*L2**4)/(L2**2 - L1**2)
    A = x1**2*L1**4 + B*L1**2
    def Phi(x):
        L = Lam(x); return (A - B*L**2)/L**4 - x**2
    m_ = (x1+x2)/2; h = (x2-x1)/2
    def integ(t):
        x = m_ + h*sin(t); val = Phi(x); den = (x-x1)*(x2-x)
        if den <= 0 or val <= 0: return mpf(0)
        return sqrt(den/val)
    return 2*quad(integ, [-pi/2, 0, pi/2]) - 2*pi

p_ust = presesyon(lambda x: exp(-x), a_S2, e_S2, mu_sgr)
p_lin = presesyon(lambda x: 1-x,    a_S2, e_S2, mu_sgr)
p_gr  = 6*pi*mu_sgr/(a_S2*(1-e_S2**2))
print(f"\n  {'aday':<12}{'presesyon/yorunge (arcmin)':>30}{'/GR':>16}{'f_SP':>10}")
for ad, p in [("USTEL", p_ust), ("LINEER-L", p_lin), ("GR (1PN)", p_gr)]:
    print(f"  {ad:<12}{nstr(p*arcmin,12):>30}{nstr(p/p_gr,12):>16}{nstr(p/p_gr,5):>10}")
print(f"  GRAVITY 2020 olcumu: f_SP = 1.10 +/- 0.19  (GR: 1) ; 12.1 arcmin/yorunge")
for ad, p in [("USTEL", p_ust), ("LINEER-L", p_lin)]:
    z = (p/p_gr - mpf('1.10'))/mpf('0.19')
    print(f"    {ad:<9} f_SP = {nstr(p/p_gr,8)}  ->  gozlemden {nstr(abs(z),3)} sigma  "
          f"{'UYUMLU' if abs(z)<=2 else 'DISLANIR'}")

# =====================================================================
# 8) AYIRT EDICILIK BUTCESI
# =====================================================================
head("8) AYIRT EDICILIK — hangi hassasiyet %4.63'u gorur?")
d_ust = (2*mp_e/(3*sqrt(3))-1)
print(f"  Ustel imza: delta = +{nstr(d_ust*100,6)} %  (PARAMETRESIZ, ayarlanamaz)")
for ad, M, dM, D, dD in [kaynak[0], kaynak[3]]:
    mu_, th_g, rel = tg_kayit[ad]
    cap = FAKTOR['GR']*th_g
    print(f"\n  {ad}")
    print(f"    GR golge capi {nstr(cap,6)} uas ; ustel-GR farki = {nstr(cap*d_ust,5)} uas")
    print(f"    onculden (M,D) gelen taban gurultu = %{nstr(rel*100,3)} = {nstr(cap*rel,4)} uas")
    print(f"    farki 1 sigma gormek icin gereken toplam capsal hassasiyet <= "
          f"{nstr(cap*d_ust,4)} uas  (%{nstr(d_ust*100,4)})")
for hedef, ad2 in [(mpf('0.10'), "EHT 2022 (bugun)"), (mpf('0.02'), "ngEHT hedefi ~%2"),
                   (mpf('0.01'), "ngEHT/BHEX ideal ~%1"), (mpf('0.005'), "n=1 halka, uzay-VLBI")]:
    print(f"  {ad2:<26} capsal hassasiyet %{nstr(hedef*100,3):>5}  ->  ustel imza "
          f"{nstr(d_ust/hedef,3)} sigma")
print("""
  KRITIK KISIT: Sgr A* kutlesi S-yildizi yorungelerinden BAGIMSIZ ve ~%0.3 hassas
  (GRAVITY 2021: M = 4.297e6 +/- 0.013e6, R0 = 8277 +/- 9 pc -> theta_g ~%0.4).
  Yani sinavin dogruluk tavani, halka<->golge donusumunun (GRMHD kalibrasyonu) sistematigi
  ve halka capi olcum hatasidir; kutle DEGIL. M87*'de ise bagimsiz kutle ~%15 belirsiz
  (yildiz dinamigi 6.2e9 vs gaz dinamigi 3.5e9) -> M87* %5'lik sinav VEREMEZ.
""")
