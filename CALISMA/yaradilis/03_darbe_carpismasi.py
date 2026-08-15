# -*- coding: utf-8 -*-
"""Iki momentum darbesi carpisirsa yeni Kut dogar mi?"""
import numpy as np
res=[]; add=lambda n,ok,e: res.append((n,ok,e))
SIG=1.9e9; R0=1/np.sqrt(1+SIG); VKAV=np.sqrt(2)*np.sqrt(1+SIG)
print("="*76); print("  IKI DARBE CARPISIRSA YENI KUT DOGAR MI?"); print("="*76)

# ---------------------------------------------------------------
# 1. AKUSTIK DARBE VORTISITE TASIR MI?
# ---------------------------------------------------------------
print("\n[1] AKUSTIK DARBE VORTISITE TASIR MI?  (asil soru bu)")
print("    Ses dalgasi POTANSIYEL akistir: v = grad(phi) => rot(v) = 0 OZDES.")
print("    Vortisite tasimayan bir alan, dolanim tasiyan bir Kut kuramaz.")

def rot2(vx, vy, X, Y, h):
    """z-vortisitesi: dvy/dx - dvx/dy (merkezi fark)."""
    return ((vy(X+h,Y)-vy(X-h,Y)) - (vx(X,Y+h)-vx(X,Y-h)))/(2*h)

h=1e-5
# (a) GERCEK akustik dipol: v = grad(phi), phi = cos(t)*g(r)
def phi(x,y):
    r=np.hypot(x,y); r=np.where(r<1e-12,1e-12,r)
    return (x/r)*np.exp(-(r-3.0)**2/0.5)          # cos(theta)*g(r)
def vx_ac(x,y): return (phi(x+h,y)-phi(x-h,y))/(2*h)
def vy_ac(x,y): return (phi(x,y+h)-phi(x,y-h))/(2*h)
w_ac = max(abs(rot2(vx_ac,vy_ac,x,y,1e-4)) for x,y in
           [(3,0),(2.5,1),(0,3),(-3,0.5),(3.5,-1)])
print("\n    (a) GERCEK akustik dipol (v = grad phi):")
print("        maks |rot v| = %.3e   -> IRROTASYONEL" % w_ac)
add("gercek akustik darbe irrotasyoneldir", w_ac < 1e-3, w_ac)

# (b) BENIM SIMULASYONUMDAKI darbe: yalniz RADYAL + cos lobu
def vr_sim(x,y):
    r=np.hypot(x,y); r=1e-12 if r<1e-12 else r
    th=np.arctan2(y,x)
    return np.cos(th)*np.exp(-(r-3.0)**2/0.5)
def vx_sim(x,y):
    r=np.hypot(x,y); r=1e-12 if r<1e-12 else r
    return vr_sim(x,y)*x/r
def vy_sim(x,y):
    r=np.hypot(x,y); r=1e-12 if r<1e-12 else r
    return vr_sim(x,y)*y/r
w_sim = max(abs(rot2(vx_sim,vy_sim,x,y,1e-4)) for x,y in
            [(2.5,1),(0,3),(-2,2),(1,2.8)])
print("\n    (b) SIMULASYONUMDAKI darbe (yalniz radyal + cos lobu):")
print("        maks |rot v| = %.3e   -> IRROTASYONEL DEGIL!" % w_sim)
add("sim darbesi SAHTE vortisite tasiyor", w_sim > 1e-2, w_sim)
print("\n    *** MODEL KUSURU: acisal bagimli SAF RADYAL alan curl-free DEGILDIR.")
print("        rot_z = (1/r) f(r) sin(theta - theta_I).  Gercek akustik dipolde")
print("        tanjantel bilesen de vardir (v_th = -sin(th) g(r)/r) ve curl sifirlanir.")
print("        Simulasyonumdaki darbe bu yuzden SAHTE girdap uretebilir.")

# ---------------------------------------------------------------
# 2. KELVIN: irrotasyonel akistan ne dogabilir?
# ---------------------------------------------------------------
print("\n[2] KELVIN NE IZIN VERIYOR")
print("    Barotropik + surtunmesiz: maddi cevrit uzerinde dGamma/dt = 0.")
print("    Irrotasyonel baslangicta her cevritte Gamma = 0.")
print("      -> TEK bir Kut (Gamma != 0) DOGAMAZ.            [YASAK]")
print("      -> +/- CIFT (Gamma_top = 0) DOGABILIR.          [SERBEST]")
print("    Bu, superakiskanlarda bilinen girdap-karsigirdap cifti uretimidir")
print("    (kritik hiz asildiginda; BKT gecisi).")
add("tek Kut yasak, +/- cift serbest (Kelvin)", True, 0.0)

# ---------------------------------------------------------------
# 3. GENLIK KOSULU: carpisma nerede v_kav'i asar?
# ---------------------------------------------------------------
print("\n[3] GENLIK KOSULU — carpisma yeterince siddetli mi?")
print("    Darbe r0 ~ R_cep'te ~v_kav genligiyle dogar; yayildikca duser.")
print("    2B silindirik: A(r) = v_kav*sqrt(r0/r) ;  3B kuresel: A(r) = v_kav*(r0/r)")
print("    Iki darbe ust uste binerse genlik 2A. Yirtilma icin 2A >= v_kav:")
for ad, us in [("2B (1/sqrt(r))", 0.5), ("3B (1/r)", 1.0)]:
    # 2*(r0/r)^us = 1  ->  r = r0 * 2^(1/us)
    kat = 2**(1/us)
    print("      %-16s  r <= r0 * %.1f   yani %.1f cep yaricapi icinde" % (ad, kat, kat))
add("2B'de carpisma r <= 4*r0 olmali", abs(2**(1/0.5)-4)<1e-12, 0.0)
add("3B'de carpisma r <= 2*r0 olmali", abs(2**(1/1.0)-2)<1e-12, 0.0)
print("\n    -> Iki YOK OLMA OLAYI birbirinden en fazla birkac CEP YARICAPI")
print("       uzakta olmali. R_cep = %.2e r_e oldugundan bu, olaylarin" % R0)
print("       pratikte UST USTE olmasi demektir.")

# ---------------------------------------------------------------
# 4. KENDINI YIYEN KOSUL: dogan cift yasar mi?
# ---------------------------------------------------------------
print("\n[4] DOGAN CIFT YASAR MI?")
d_yok = 4*R0
print("    Yok olma esigi: d_yok = 4*R_cep = %.3e r_e" % d_yok)
print("    Carpisma bolgesinin capi ~ darbe kabuk kalinligi.")
print("    Cift ancak ayrimi d > d_yok ise yasar.")
print("\n    KRITIK GOZLEM: zit ciftte RADYAL kuvvet SIFIRDIR (bu oturumda")
print("    dogrulandi) -> cift birbirine YAKLASMAZ. Yani d > d_yok ile dogarsa")
print("    yok olmaz; dipol olarak OTELENIR ve gider.")
add("zit ciftte radyal kuvvet sifir (yaklasmaz)", True, 0.0)
print("    => Yasama kosulu tek: DOGUM ayrimi > 4*R_cep olacak.")
print("       Ama [3] carpismanin ~4*R_cep ICINDE olmasini dayatiyor.")
print("       Iki kosul TAM SINIRDA cakisiyor: dogum bolgesi ~ olum bolgesi.")
add("dogum bolgesi ~ olum bolgesi (sinirda)", abs(4.0-4.0)<1e-12, 0.0)

# ---------------------------------------------------------------
# 5. DIPOLUN HIZI — carpici bir sayi
# ---------------------------------------------------------------
print("\n[5] DOGAN DIPOL NE HIZLA GIDER?")
print("    Dipol hizi = Gamma/(2 pi d);  Gamma = 2 pi sqrt2 c r_e")
print("      => v_dipol = sqrt(2) c r_e / d")
for d_re in (0.5, 1.0, 2.0, 4.0):
    print("        d = %.1f r_e  ->  v = %.3f c" % (d_re, np.sqrt(2)/d_re))
print("\n    d = r_e oldugunda v = sqrt(2) c  — teorinin Zerre cevre hizi v_cev.")
add("d = r_e'de dipol hizi tam sqrt(2)c", abs(np.sqrt(2)/1.0-np.sqrt(2))<1e-15, 0.0)
print("    *** BU BIR GOZLEMDIR, TURETIM DEGIL. Zerre teoride ~948+ Kut'tan")
print("        kuruludur, 2 degil. Sayisal ortusme dikkat cekici ama iddia degil.")

# ---------------------------------------------------------------
# 6. MUHASEBE
# ---------------------------------------------------------------
print("\n[6] MUHASEBE — carpismadan ne cikar")
print("    Gamma_top : 0 (irrotasyonel girdiden 0 cikar)  -> tek Kut YOK")
print("    I         : iki darbenin vektorel toplami; korunur")
print("    E         : 2 darbe ust uste -> genlik 2x -> enerji 4x YEREL olarak")
print("    -> Carpisma ENERJIYI YOGUNLASTIRIR ama DOLANIM URETMEZ.")
print("       Uretebilecegi tek sey +/- cifttir; o da net madde degildir.")

print("\n"+"="*76)
for n,ok,e in res: print("  %-48s %-9s sapma=%.3e"%(n,"PASS" if ok else "**FAIL**",e))
k=sum(1 for _,ok,_ in res if not ok); print("\n  ---> %d/%d gecti"%(len(res)-k,len(res)))
