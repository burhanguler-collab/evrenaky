# -*- coding: utf-8 -*-
"""
USTEL OLCEK YAPISI — BAGIMSIZ BES YOLUN SAYISAL DENETIMI
=========================================================
Ana oturumun yolu (stiff K=P -> dP/dchi = -C P/P0) KULLANILMAZ.
Bes bagimsiz yol ayri ayri kurulur ve sonuc profilleri karsilastirilir:

  YOL 1  Stiff entalpi  (M-3', M-50: h = U'(rho) = c0^2 (1+ln(rho/rho0)))
  YOL 2  Siklostrofik denge / sikistirilabilir Euler (M-9'un kendi denklemi)
  YOL 3  Eylem ilkesi   (M-44/M-46: U(rho,chi) = g(chi) c0^2 rho ln(rho/rho0))
  YOL 4  Olcek kapanmasi (Postulat 4: mutlak basinc olcegi YOK)
  YOL 5  Kabuk/Arsimet muhasebesi (dislanan hacim; M-46'nin kendi kaydi)

Sembol/kalibrasyon zinciri kitaptan:
  rho_n = 2.7e17,  P0 = (1/4) rho_n c0^2,  rho0 = rho_n/4
  Phi = kuyu derinligi (POZITIF),  mu = GM/c0^2,  u = 4 Phi/c0^2 = 4 mu/r
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
from mpmath import mp, mpf, exp, log, sqrt, pi, quad, sin, cos, diff, mpmathify

mp.dps = 50

c0     = mpf('2.99792458e8')
G      = mpf('6.67430e-11')
rho_n  = mpf('2.7e17')
P0     = rho_n*c0**2/4
rho0   = rho_n/4
GMsun  = mpf('1.32712440018e20')
GMearth= mpf('3.986004418e14')
Rearth = mpf('6.371e6')
AU     = mpf('1.495978707e11')
mu_s   = GMsun/c0**2
arcsec = 180*3600/pi

def sep(t): print("\n" + "="*78 + "\n" + t + "\n" + "="*78)

print("Kalibrasyon zinciri denetimi")
print("  P0            = %.5e Pa   (kitap: 6.07e33)" % P0)
print("  rho0          = %.5e kg/m3 (kitap: 6.8e16)" % rho0)
print("  P0/rho0       = c0^2 ? oran = %.16f" % (P0/rho0/c0**2))
print("  mu_gunes      = %.6f m ... %.4f km" % (mu_s, mu_s/1000))

# =====================================================================
sep("YOL 1 — STIFF ENTALPI (M-3', M-50)")
# =====================================================================
# M-50: U(rho) = c0^2 rho ln(rho/rho0)  =>  P = rho U' - U = c0^2 rho   (stiff)
#       h = U'(rho) = c0^2 (1 + ln(rho/rho0))
# Denetim: P = rho U' - U gercekten c0^2 rho mi?
def U_stiff(r_):  return c0**2*r_*log(r_/rho0)
for rt in ['0.3','1.0','3.7']:
    r_ = mpf(rt)*rho0
    P_ = r_*diff(U_stiff, r_) - U_stiff(r_)
    print("  rho/rho0=%4s :  rho*U'-U = %.10e ,  c0^2 rho = %.10e ,  oran=%.16f"
          % (rt, P_, c0**2*r_, P_/(c0**2*r_)))

# Entalpi HAL DENKLEMI kanalinda kurulur (M-44 'Kritik Ayrim': deplasman
# bagintisi bir hal denklemi DEGILDIR, dolayisiyla termodinamik potansiyel
# kurmak icin kullanilamaz).  Stiff kanalda P = c0^2 rho oldugundan:
#     h(P) - h(P0) = c0^2 ln(P/P0)
# Deplasman alani ortamin DOGAL enerji degiskenine lineer baglanir:
#     C chi = -P0 ln(P/P0)   =>   P = P0 exp(-C chi/P0)
# Kalibrasyon (M-46 zincir denetimi): C chi/P0 = 4 Phi/c0^2
def P_yol1(Phi):  return P0*exp(-4*Phi/c0**2)
# Rakip okuma (deplasman kanali entalpisi H = P/rho0, rho sabit):
def P_lineer(Phi): return P0 - rho_n*Phi

print("\n  Iki entalpi okumasi ve BIRINCI MERTEBE ORTUSMESI:")
print("  %-14s %-24s %-24s %-12s" % ("Phi/c0^2", "ustel P/P0", "lineer P/P0", "fark"))
for e in ['1e-12','7e-10','1e-6','1e-3']:
    Phi = mpf(e)*c0**2
    a = P_yol1(Phi)/P0; b = P_lineer(Phi)/P0
    print("  %-14s %-24s %-24s %.3e" % (e, mp.nstr(a,16), mp.nstr(b,16), a-b))
print("  -> fark = 8(Phi/c0^2)^2 mertebesinde (ikinci mertebe) ✓ zincir korunur")

# Kalibrasyon zinciri: DeltaP_yuzey = rho_n Phi (M-8) ustelde de saglaniyor mu?
Phi_e = GMearth/Rearth
dP_ustel  = P0 - P_yol1(Phi_e)
dP_kitap  = rho_n*Phi_e
print("\n  M-8 denetimi (Dunya yuzeyi, Phi=%.4e m2/s2):" % Phi_e)
print("    DeltaP(ustel) = %.10e Pa" % dP_ustel)
print("    rho_n*Phi     = %.10e Pa" % dP_kitap)
print("    oran          = %.14f  -> M-8 kalibrasyonu KORUNUR" % (dP_ustel/dP_kitap))

# delta_c/c0 = -2 Phi/c0^2 (M-42) denetimi
c_loc = lambda Phi: c0*exp(-2*Phi/c0**2)
print("    delta_c/c0(ustel) = %.10e ;  -2Phi/c0^2 = %.10e ; oran=%.14f"
      % (c_loc(Phi_e)/c0-1, -2*Phi_e/c0**2, (c_loc(Phi_e)/c0-1)/(-2*Phi_e/c0**2)))

# =====================================================================
sep("YOL 2 — SIKLOSTROFIK DENGE / SIKISTIRILABILIR EULER (M-9)")
# =====================================================================
# M-9 Gecerlilik Siniri, kitabin kendi denklemi:   grad P / rho0 = v_theta^2 / r
# (a) ORTAMIN DOLASIM HIZI, maddenin yorunge hizina KILITLI (tureti1miş sonuc)
#     madde:  v_orb^2/r = (1/rho_n) dP/dr        (M-2 + dairesel yorunge)
#     ortam:  v_theta^2/r = (1/rho0) dP/dr       (M-9)
#     ORAN:   v_theta^2/v_orb^2 = rho_n/rho0 = 4   (TAM, her r'de, zayif alan gerekmez)
print("  (a) v_theta/v_orb = sqrt(rho_n/rho0) = %.14f  (beklenen 2)" % sqrt(rho_n/rho0))
print("      -> ortam, maddenin dairesel yorunge hizinin TAM 2 KATINDA dolasir")
print("      -> v_theta = sqrt(2)*v_kacis  (ortam kuyuya bagli degil; M-9 agirliksizlik ile tutarli)")
for nm,GM,r in [("Dunya yuzeyi",GMearth,Rearth),("Gunes @1AU",GMsun,AU),
                ("Gunes @1 R_gunes",GMsun,mpf('6.957e8'))]:
    vk = sqrt(GM/r)
    print("      %-18s v_orb=%9.3f km/s  ->  v_theta=%9.3f km/s   M_theta=v_th/c0=%.4e"
          % (nm, vk/1000, 2*vk/1000, 2*vk/c0))

# (b) KAPANMA: siklostrofik denklem LOKAL ses hizina bolunerek yazilir.
#     P/rho0 = c_loc^2 (Kavrama Yasasi'nin ORAN bicimi, YEREL — M-1 + k=0)
#     (1/rho0) dP/dr = v_th^2/r   |  ÷ c_loc^2 = P/rho0
#     =>  d ln P / dr = (v_th/c_loc)^2 / r = M_th^2 / r
#     Dolayisiyla profil, dolasimin YEREL MACH sayisi tarafindan belirlenir.
#     Iki rakip kapanma:
#        (L) v_th^2/c0^2    = 4 mu/r   (arka plana gore normalize)  -> LINEER
#        (U) v_th^2/c_loc^2 = 4 mu/r   (YERELE gore normalize)      -> USTEL
def profil_kapanma(mode, r_, mu_, N=400000):
    """ln(P/P0) = -int_r^inf (M_th^2/r') dr' , M_th^2 = 4 mu/r' * (c0/c_loc)^{0 veya 2}"""
    if mode == 'U':
        # d lnP/dr = 4 mu / r^2  (M_th yerel)  -> analitik
        return -4*mu_/r_
    else:
        # (1/rho0) dP/dr = v_th^2/r , v_th^2 = 4 mu c0^2 / r  -> dP/dr = 4 mu P0 /r^2
        return None  # lineer: P = P0 (1 - 4mu/r), asagida ayri

print("\n  (b) Kapanma denetimi (Gunes, r = 1 R_gunes):")
rr = mpf('6.957e8')
lnP_U = profil_kapanma('U', rr, mu_s)
print("      (U) yerel Mach kapanmasi : ln(P/P0) = %.14e   -> P/P0 = %s"
      % (lnP_U, mp.nstr(exp(lnP_U),16)))
print("      (L) arka plan kapanmasi  : P/P0 = 1 - 4mu/r = %s"
      % mp.nstr(1-4*mu_s/rr,16))
print("      -> (U) TAM OLARAK P = P0 exp(-4mu/r) verir. (L) lineer profili verir.")
print("      -> ayrim: dolasim Mach'i YEREL c_loc'a mi, arka plan c0'a mi gore? ")
print("         Postulat 4 (her sey yerel; c0 evrensel sabit degil) -> YEREL -> USTEL")

# (b2) Dogrudan ODE entegrasyonu ile denetim (analitik yerine sayisal)
#      d lnP/dr = M_th^2 / r ,  M_th^2 = 4 mu / r   (yerel kapanma)
def lnP_ode(r_, mu_):
    f = lambda s: 4*mu_/s**2
    return -quad(f, [r_, mp.inf])
print("\n      Sayisal entegrasyon denetimi (quad, r->inf):")
for rt in ['1e9','1e10','1e11']:
    r_ = mpf(rt)
    a = lnP_ode(r_, mu_s); b = -4*mu_s/r_
    print("        r=%-6s  quad=%.20e   -4mu/r=%.20e   oran=%.16f" % (rt,a,b,a/b))

# (c) DONUSUZ (irrotational) ALT KOL DISLANIR
#     Bernoulli 1/2 v^2 + h = sbt  +  siklostrofik  =>  v dv/dr = -v^2/r => v ~ 1/r
#     (potansiyel girdap) => (1/rho0)dP/dr ~ 1/r^3 => P = P0 - A/r^2  (YANLIS PROFIL)
print("\n  (c) Donusuz alt kol: Bernoulli + siklostrofik -> v ~ 1/r (potansiyel girdap)")
print("      => (1/rho0) dP/dr propto 1/r^3 => P = P0 - A/r^2")
print("      log-log egim denetimi (dP/dr ~ r^p):")
A = mpf('1e30')
f = lambda s: A/s**2
for rt in ['1e9','1e10']:
    r_=mpf(rt)
    p = (log(abs(diff(f,r_*mpf('1.001')))) - log(abs(diff(f,r_))))/(log(r_*mpf('1.001'))-log(r_))
    print("        r=%-6s  d(P)/dr egimi = %.6f  (beklenen -3)" % (rt,p))
print("      -> 1/r^2 profili kutle-itimi 1/r^3 yapar; M-46/M-35 ile CELISIR.")
print("      -> HUKUM: ortamin kutle cevresindeki dolasimi DONUSUZ OLAMAZ")
print("         (chi kaynak terimi vortisite kaynagidir; M-44 md.3'un donusuzluk")
print("          kisiti kutle-itim kuyusunda gecerli degildir).")

# =====================================================================
sep("YOL 3 — EYLEM ILKESI (M-44 + M-46)")
# =====================================================================
# Onerilen ic enerji:  U(rho,chi) = g(chi) * c0^2 * rho * ln(rho/rho0)
# 1) Basinc:      P = rho U_rho - U = g(chi) c0^2 rho
# 2) Ses hizi:    (dP/drho)_chi = g c0^2 = P/rho = c_loc^2  -> stiff, YEREL bicimde
# 3) chi kaynagi: dU/dchi = g'(chi) c0^2 rho ln(rho/rho0) -> rho=rho0'da SIFIR
#                 => nabla^2 chi = -q_n n_m AYNEN KALIR
def U_g(rho_, g_):  return g_*c0**2*rho_*log(rho_/rho0)
print("  1) P = rho*U_rho - U  denetimi (cesitli g ve rho):")
for gv in ['1.0','0.7','1.4']:
    for rt in ['0.5','1.0','2.0']:
        g_=mpf(gv); r_=mpf(rt)*rho0
        Uf = lambda x: U_g(x,g_)
        P_ = r_*diff(Uf,r_) - Uf(r_)
        print("     g=%-4s rho/rho0=%-4s : P=%.8e ,  g*c0^2*rho=%.8e , oran=%.16f"
              % (gv,rt,P_,g_*c0**2*r_,P_/(g_*c0**2*r_)))
print("\n  2) (dP/drho)_chi = g c0^2 = c_loc^2  (YEREL stiff kosul):")
for gv in ['1.0','0.7']:
    g_=mpf(gv); Uf=lambda x:U_g(x,g_)
    Pf = lambda x: x*diff(Uf,x)-Uf(x)
    r_=rho0*mpf('1.0')
    dPdrho = diff(Pf, r_)
    print("     g=%-4s : dP/drho=%.10e ,  g*c0^2=%.10e , oran=%.16f ; c_loc/c0=%.10f"
          % (gv,dPdrho,g_*c0**2,dPdrho/(g_*c0**2),sqrt(g_)))
print("     -> GW170817: dalga hizi = c_loc, YEREL olarak tam ‘isik hizi’ ✓ (M-44 korunur)")
print("\n  3) chi kaynak terimi rho=rho0'da:  g'(chi) c0^2 rho0 ln(1) = 0  -> Poisson DEGISMEZ ✓")

# g(chi)'nin bicimi: chi'nin SIFIR NOKTASI kaymasi altinda ortusme (Postulat 4)
# chi(x) = int q_n n_m/(4pi|x-x'|) d3x'  : evrendeki TUM maddenin fonksiyoneli
# => chi -> chi + chi_inf kaymasi fiziksel olamaz; yalnizca YEREL birimleri
#    (P0,rho0,c0) yeniden olcekleyebilir  =>  g(chi+chi') = g(chi) g(chi')
#    tek surekli cozum: g = exp(-a chi)
print("\n  4) chi sifir-noktasi kaymasi altinda ortusme testi:")
def g_ustel(x): return exp(-x)
def g_lineer(x): return 1-x
for nm,gf in [("ustel  g=exp(-x)",g_ustel),("lineer g=1-x",g_lineer)]:
    ihl = mpf(0)
    for a_,b_ in [('6.96e-10','9.87e-9'),('1e-6','3e-6'),('1e-3','2e-3')]:
        x1=mpf(a_); x2=mpf(b_)
        ihl = max(ihl, abs(gf(x1)*gf(x2)-gf(x1+x2)))
    print("     %-20s max |g(x1)g(x2)-g(x1+x2)| = %.4e" % (nm,ihl))
print("     -> yalnizca ustel, toplamsal chi ile carpimsal g'yi bagdastirir")

# =====================================================================
sep("YOL 4 — OLCEK KAPANMASI (Postulat 4: mutlak basinc olcegi YOK)")
# =====================================================================
# Genel tepki yasasi:  dP/dchi = -(C/P0^n) P^n   (n: tepki ussu)
# n != 1 ise yasa, MUTLAK bir basinc olcegi (P0) tasimak zorundadir.
# Postulat 4: P0 yereldir, evrensel sabit degildir -> yasada gorunemez.
# Boyut analizi: [dP/dchi] = Pa/(m2/s) . Yalnizca n=1 icin katsayi
#   C/P0 = boyutu 1/(m2/s) olan ve BASINC OLCEGI ICERMEYEN bir sayidir.
print("  Genel aile:  P(u) = P0 [1-(1-n) u]^{1/(1-n)},  u = 4Phi/c0^2 ; n=1 -> exp(-u)")
def P_family(u,n):
    n=mpf(n); u=mpf(u)
    if abs(n-1) < mpf('1e-30'): return exp(-u)
    return (1-(1-n)*u)**(1/(1-n))
print("  %-6s %-26s %-16s %-14s" % ("n","P/P0 (u=1e-3)","kappa=4n-3","beta=2n-1"))
for n in ['0','0.5','0.9','1','1.1','1.5']:
    print("  %-6s %-26s %-16s %-14s" % (n, mp.nstr(P_family('1e-3',n),18),
          mp.nstr(4*mpf(n)-3,6), mp.nstr(2*mpf(n)-1,6)))
print("\n  Olcek-serbestlik testi: yasayi P -> s*P , P0 -> s*P0 altinda yaz.")
print("  dP/dchi = -(C/P0^n) P^n  ->  s dP/dchi = -(C/(s^n P0^n)) s^n P^n = -(C/P0^n)P^n")
print("  ... her n icin ORTUSUR ama n!=1'de yasa P0'i ACIKCA tasir.")
print("  Postulat 4 kesin testi: YEREL gozlemci kendi P0_loc = P0*Lambda^4 ile ayni")
print("  yasayi yazabilmeli (form-degismezlik). Denetim:")
for n in ['0','0.5','1']:
    n_=mpf(n)
    # yerel gozlemci: P = P0L * f(u_loc). Arka plan gozlemcisiyle ortusme sarti
    L4 = exp(-mpf('1e-3'))   # ornek derinlik
    u1 = mpf('2e-4')         # ek derinlik
    # arka plan: P = P0 * F(u0+u1) ; yerel: P = (P0 F(u0)) * F(u1) ?
    u0 = mpf('1e-3')
    F = lambda u: P_family(u,n_)
    lhs = F(u0+u1); rhs = F(u0)*F(u1)
    print("     n=%-5s  F(u0+u1)=%-22s F(u0)F(u1)=%-22s ihlal=%.4e"
          % (n, mp.nstr(lhs,16), mp.nstr(rhs,16), abs(lhs-rhs)))
print("  -> yalnizca n=1 (ustel) form-degismezdir: yerel gozlemci ayni yasayi yazar.")

# =====================================================================
sep("YOL 5 — KABUK / ARSIMET MUHASEBESI (dislanan hacim)")
# =====================================================================
# M-46'nin kendi kaydi: dislanan-hacim modeli P = P(rho/(1-f)) , f = n_m V_cep
# stiff:  P = c0^2 rho/(1-f)  =>  dP/df = c0^2 rho/(1-f)^2 = P/(1-f)
# yani tepki MEVCUT BASINCA oranli (mutlak bir miktara degil) -> carpimsal
print("  Dislanan hacim (M-46'nin kendi kaydi, stiff):  P = c0^2 rho/(1-f)")
Pf = lambda f_: c0**2*rho0/(1-f_)
for ft in ['0','1e-6','1e-3','0.1']:
    f_=mpf(ft)
    d = diff(Pf,f_)
    print("     f=%-8s  dP/df = %.10e ,  P/(1-f) = %.10e , oran=%.16f"
          % (ft,d,Pf(f_)/(1-f_),d/(Pf(f_)/(1-f_))))
print("     -> (dP/df)_rho = rho0 c0^2 = %.4e Pa   (M-46: 6.07e33 ✓ 'dogru mertebe')" % (rho0*c0**2))
print("     -> KRITIK: tepki katsayisi SABIT DEGIL, P ile olcekleniyor.")

# Kabuk carpimsal birikimi: N kabuk, her biri mevcut basinci (1-a) kati yapiyor
print("\n  N kabuk, her biri mevcut basinci (1 - u/N) kati yapiyor (u toplam etki):")
print("  %-10s %-26s %-26s" % ("N","(1-u/N)^N","hata vs exp(-u)"))
u_tot = mpf('1e-3')
for N in [1,2,10,100,10000,10**8]:
    v = (1-u_tot/N)**N
    print("  %-10s %-26s %.4e" % (N, mp.nstr(v,20), abs(v-exp(-u_tot))))
print("  -> N->inf limitinde TAM olarak exp(-u). Kabuklarin sirasindan bagimsiz (carpim degismeli).")
print("\n  Karsit muhasebe (her kabuk SABIT miktar dusuruyor): P = P0(1 - u) — N'den bagimsiz")
print("  Ayrim: 'sabit oran' mi 'sabit miktar' mi? Stiff ortamda K = rho c^2 = P")
print("  oldugundan geri-itme gucu mevcut basinctir -> SABIT ORAN.")
print("  K = P denetimi: K = rho (dP/drho) = rho c_loc^2 = P")
for gv in ['1.0','0.6']:
    g_=mpf(gv); Uf=lambda x:U_g(x,g_); Pfn=lambda x:x*diff(Uf,x)-Uf(x)
    r_=rho0
    K = r_*diff(Pfn,r_)
    print("     g=%-4s : K=%.8e , P=%.8e , K/P=%.16f" % (gv,K,Pfn(r_),K/Pfn(r_)))

# =====================================================================
sep("BAGIMSIZ GOZLEM DENETIMI — MERKUR (yollarin ortak sonucu)")
# =====================================================================
# Teorinin kendi eyleminden: S = -m c0^2 int Lambda sqrt(1-V^2/c_loc^2) dt
# (dx/dphi)^2 = (A - B Lambda^2)/Lambda^4 - x^2 , x = mu/r , c_loc = c0 Lambda^2
def presesyon(Lam, a, e, mu_):
    x1 = mu_/(a*(1+e)); x2 = mu_/(a*(1-e))
    L1 = Lam(x1); L2 = Lam(x2)
    B = (x1**2*L1**4 - x2**2*L2**4)/(L2**2 - L1**2)
    A_ = x1**2*L1**4 + B*L1**2
    def Phi_(x):
        L = Lam(x); return (A_ - B*L**2)/L**4 - x**2
    m_=(x1+x2)/2; h_=(x2-x1)/2
    def integ(t):
        x = m_ + h_*sin(t); den=(x-x1)*(x2-x); val=Phi_(x)
        if den<=0 or val<=0: return mpf(0)
        return sqrt(den/val)
    return 2*quad(integ,[-pi/2,pi/2]) - 2*pi

a_m = mpf('5.790905e10'); e_m = mpf('0.20563'); T_m = mpf('87.9691')
turlar = mpf('36525')/T_m
for nm, Lam in [("USTEL  Lambda=exp(-x)", lambda x: exp(-x)),
                ("LINEER Lambda=1-x",     lambda x: 1-x)]:
    dpo = presesyon(Lam, a_m, e_m, mu_s)
    print("  %-24s  %.6f as/yy" % (nm, dpo*turlar*arcsec))
GR = 6*pi*mu_s/(a_m*(1-e_m**2))
print("  %-24s  %.6f as/yy   (6 pi mu / a(1-e^2))" % ("GR referansi", GR*turlar*arcsec))
print("  %-24s  42.9799 +/- 0.0009 as/yy" % "OLCUM")

# =====================================================================
sep("YOL 2'nin KAPANMA CATALI — ham hiz mi, YEREL MACH mi?")
# =====================================================================
# chi-sektorunun tek frekansi: omega_C = C/rho0  ([C]=kg m^-3 s^-1 -> [C/rho0]=s^-1)
# Boyut zorunlulugu: v^2 (m2/s2) = omega_C (1/s) * chi (m2/s) — TEK kombinasyon.
# chi = K/r (M-46 Poisson) => v_theta^2 propto 1/r  (Kepler-benzeri) — ek varsayim YOK.
# CATAL: chi'ye lineer baglanan sey ham v_theta^2 mi, yoksa (v_theta/c_loc)^2 mi?
K_ = 4*mu_s*c0**2/mpf(1)      # omega_C*K = 4 mu c0^2  (kalibrasyon)
def ode_caseA(r_):   # ham hiz: (1/rho0)dP/dr = omega_C chi / r
    return 1 - 4*mu_s/r_                      # -> LINEER (analitik)
def ode_caseB(r_):   # yerel Mach: (v/c_loc)^2 = omega_C chi/c0^2
    return exp(-4*mu_s/r_)                    # -> USTEL (analitik)
# Sayisal ODE denetimi: cozumu ONCEDEN VARSAYMADAN, coklu sistemi cozelim.
# Degisken: s = 1/r (boylece r->inf sinir kosulu s=0'a gelir).
# Case A:  dP/dr = rho0 omega_C chi / r  = 4 mu P0 / r^2   ->  dy/ds = -4 mu   (y=P/P0)
# Case B:  dP/dr = (P/c0^2) omega_C chi / r = P*4mu/r^2    ->  dy/ds = -4 mu y
# Ikisi de s=0'da y=1. mpmath odefun ile (adaptif Taylor) cozulur.
def ode_coz(mode, r_hedef):
    if mode=='A': F = lambda s, y: [-4*mu_s]
    else:         F = lambda s, y: [-4*mu_s*y[0]]
    f = mp.odefun(F, mpf(0), [mpf(1)], tol=mpf('1e-40'))
    return f(1/r_hedef)[0]
rt = mpf('6.957e8')
print("  Gunes yuzeyi (r=R_gunes):")
print("    Case A (ham v^2 ~ chi)      : analitik 1-4mu/r  = %s" % mp.nstr(ode_caseA(rt),20))
print("    Case A (ODE cozumu)         :                     %s" % mp.nstr(ode_coz('A',rt),20))
print("    Case B (Mach^2 ~ chi, yerel): analitik exp(-4mu/r)= %s" % mp.nstr(ode_caseB(rt),20))
print("    Case B (ODE cozumu)         :                     %s" % mp.nstr(ode_coz('B',rt),20))
print("    Case B ODE/analitik farki   : %.3e" % abs(ode_coz('B',rt)-ode_caseB(rt)))
print("    A ile B'nin farki           : %.3e  (= 8(mu/r)^2 mertebesi)"
      % abs(ode_caseA(rt)-ode_caseB(rt)))
print("\n  Catalin hukmu: sikistirilabilir akiskanda tepki daima MACH sayisinin")
print("  fonksiyonudur (Prandtl-Glauert). Kitap bunu kinematik kolda ZATEN kullaniyor")
print("  (11.4.8.1, Lambda_kin) -> ayni kural potansiyel koluna uygulanir -> Case B.")

# Lambda = Lambda_grav * Lambda_kin carpimsalligi: ustel bunu TAM saglar
print("\n  11.4.8.1 carpimsalligi (Lambda = Lambda_grav * Lambda_kin) denetimi:")
for U_,V_ in [('9.87e-9','1e-4'),('1e-6','1e-3')]:
    Ug=mpf(U_); Vk=mpf(V_)         # Vk = v/c_loc
    Lg_u = exp(-Ug); Lk = sqrt(1-Vk**2)
    Lg_l = 1-Ug
    # ortak kuyu+hareket: ustelde exp(-U) * Lk ; toplam potansiyelde exp(-(U1+U2)) ozdes
    print("    U=%-9s v/c=%-7s  ustel Lg*Lk=%-24s  lineer Lg*Lk=%-24s"
          % (U_,V_,mp.nstr(Lg_u*Lk,16),mp.nstr(Lg_l*Lk,16)))
print("    (fark yalnizca Lambda_grav kolunda; carpimsal bileşim ustelde her")
print("     mertebede kapanir, lineerde 2. mertebede kirilir)")

# Isik bukulmesi (1. mertebe) ustelde korunuyor mu?
print("\n  Isik bukulmesi (Gunes kenari, n_eff = 1/Lambda^2):")
b = mpf('6.957e8')
delta_lin = 4*mu_s/b
print("    zayif alan: delta = 4 mu/b = %.6f as   (olculen 1.7510)" % (delta_lin*arcsec))
# ustel: n = exp(4mu/r) -> delta = 2 int dPhi/dr ... 1. mertebede ayni
print("    ustel n_eff = exp(+4Phi/c0^2): 1. mertebede ozdes, fark O((mu/b)^2)=%.3e"
      % ((mu_s/b)**2))

# v_theta = 2 v_K ongorusunun buyuklugu — ayrisabilir imza
print("\n  ONGORU: ortamin dolasim hizi v_theta = 2 v_K * Lambda^2")
print("  %-22s %-14s %-14s %-14s" % ("konum","v_K (km/s)","v_theta (km/s)","M_theta"))
for nm,GM,r in [("Dunya yuzeyi",GMearth,Rearth),("Ay yorungesi",GMearth,mpf('3.844e8')),
                ("Gunes @1AU",GMsun,AU),("Gunes @R_gunes",GMsun,mpf('6.957e8')),
                ("Gunes @10 mu",GMsun,10*mu_s)]:
    vk=sqrt(GM/r); L2=exp(-GM/(c0**2*r))
    print("  %-22s %-14.4f %-14.4f %-14.5e" % (nm,vk/1000,2*vk*L2/1000,2*vk*L2/(c0*L2**2)))

# =====================================================================
sep("YOL 3'un AYIRT EDICI SINAVI — iki ic-enerji adayi, ayni eylem")
# =====================================================================
# Her iki hal denklemini de VEREN en genel U (rho U_rho - U = P):
#   (I)  CARPIMSAL :  U = g(chi) c0^2 rho ln(rho/rho0)        -> P = g(chi) c0^2 rho
#   (II) TOPLAMSAL :  U = c0^2 rho ln(rho/rho0) + C chi (1 - rho/rho0)
#                                                              -> P = c0^2 rho - C chi
# Ikisi de rho=rho0'da chi-kaynagini bozmuyor (dU/dchi = 0). Ayrim BASKA yerde:
#   dalga kanalinin hizi (dP/drho)_chi, YEREL yayilma hizina esit mi?
Cc = mpf('1e10')   # olcek onemsiz, oran testi
def U_I(rho_, chi_):   # carpimsal
    return exp(-Cc*chi_/P0)*c0**2*rho_*log(rho_/rho0)
def U_II(rho_, chi_):  # toplamsal
    return c0**2*rho_*log(rho_/rho0) + Cc*chi_*(1-rho_/rho0)
def P_of(Ufn, rho_, chi_):
    f = lambda x: Ufn(x, chi_)
    return rho_*diff(f, rho_) - f(rho_)
def dPdrho(Ufn, rho_, chi_):
    return diff(lambda x: P_of(Ufn, x, chi_), rho_)
def dUdchi(Ufn, rho_, chi_):
    return diff(lambda y: Ufn(rho_, y), chi_)

print("  %-12s %-24s %-24s %-24s" % ("aday","P (rho0,chi)","(dP/drho)_chi","P/rho0 = c_loc^2"))
for nm,Ufn in [("CARPIMSAL",U_I),("TOPLAMSAL",U_II)]:
    for cht in ['0','1e21','1e22']:
        ch=mpf(cht)
        Pv=P_of(Ufn,rho0,ch); dP=dPdrho(Ufn,rho0,ch)
        print("  %-12s chi=%-7s P=%.8e  dP/drho=%.8e  P/rho0=%.8e  ORAN=%.14f"
              % (nm,cht,Pv,dP,Pv/rho0,dP/(Pv/rho0)))
print("\n  -> CARPIMSAL: (dP/drho)_chi = P/rho = c_loc^2  ORAN=1 her chi'de.")
print("     Kavrama Yasasi'nin ORAN ve DIFERANSIYEL bicimleri her noktada ORTUSUR.")
print("  -> TOPLAMSAL: (dP/drho)_chi = c0^2 SABIT kalir, ama P/rho = c_loc^2 duser.")
print("     Iki bicim kuyunun icinde AYRISIR.")

print("\n  chi-kaynagi denetimi (dU/dchi, rho=rho0'da sifir olmali):")
for nm,Ufn in [("CARPIMSAL",U_I),("TOPLAMSAL",U_II)]:
    v0 = dUdchi(Ufn,rho0,mpf('1e21'))
    v1 = dUdchi(Ufn,rho0*mpf('1.01'),mpf('1e21'))
    print("    %-12s rho=rho0 : %.4e   |  rho=1.01rho0 : %.4e" % (nm,v0,v1))
print("    -> ikisi de rho=rho0'da Poisson'u bozmaz; ayrim dalga hizindadir.")

# GW170817 sonucu: TOPLAMSAL okumada GW hizi c0, isik hizi c0*Lambda^2 -> AYRISIR
print("\n  GW170817 SONUCU (|Delta v|/v < 4.2e-16):")
print("  %-26s %-18s %-18s %-14s" % ("ortam","Phi/c0^2","toplamsal ihlal","carpimsal"))
for nm,U_ in [("Dunya yuzeyi",'6.96e-10'),("Gunes yuzeyi",'2.12e-6'),
              ("Samanyolu (200 km/s)",'4.45e-7'),("notron yildizi",'0.2')]:
    U__=mpf(U_)
    ihl_top = abs(1 - exp(-2*U__))     # c0 (GW) vs c0*Lambda^2 (isik)
    print("  %-26s %-18s %-18.4e %-14s" % (nm,U_,ihl_top,"0 (ozdes)"))
print("  -> TOPLAMSAL (lineer) okuma GW170817'yi Samanyolu potansiyelinde bile")
print("     ~9 mertebe ihlal eder (8.9e-7 vs 4.2e-16).")
print("  -> CARPIMSAL (ustel) okumada GW ve isik AYNI c_loc'ta gider: ihlal ozdes SIFIR.")
print("  -> Bu, M-44'un 'GW170817 otomatik' iddiasini gercekten otomatik yapan tek biçimdir.")

sep("BITTI")
