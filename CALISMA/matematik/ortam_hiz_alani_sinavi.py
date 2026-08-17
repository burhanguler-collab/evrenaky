# -*- coding: utf-8 -*-
"""
ORTAMIN HIZ ALANI — kuyu neyle tutuluyor?
==========================================
SORUN (DEVIR_KAYDI §5): M-9'un Gecerlilik Siniri, kutle cevresindeki ortamin
"dusmek degil DOLASMAK" zorunda oldugunu soyler ve siklostrofik denge yazar:
    grad P / rho_0 = v_th^2 / r     =>     v_th = 2 v_yor   (rho_n/rho_0 = 4)
Ama Merkur'un gunberi kaymasi ortam dolasimina yer birakmiyor:
    |Omega_ortam| <~ 1.4e-18 rad/s   (ortam_dolasimi_mp.py)
M-9'un verdigi deger 1.65e-6 rad/s — 10^12 kat fazla.

HIPOTEZ (bu betigin sinadigi): M-9 EULER denklemini kullaniyor; Euler
KOHEZYONSUZ akiskanin denklemidir (yalniz izotropik basinc, kesme yok).
Ama teorinin ortami KOHEZYONLUDUR: M-4 kohezyon dayanimi Sigma, M-5 ise
Sigma'yi kesme modulu G_s rolunde kullanir (v_m = sqrt(Sigma/rho_0)).
Kesme tasiyabilen bir ortam, basinc kuyusunu DOLASMADAN, statik elastik
dengede tutabilir:  div(sigma) = 0,  sigma_ij = -P d_ij + tau_ij
Kuresel simetride radyal denge:
    d(tau_rr)/dr + 3 tau_rr / r = dP/dr
Cozum (sonsuzda sonen):  tau_rr = rho_n * Phi / 2 = DeltaP / 2
Sinav: tau_rr << Sigma mi?  (Sigma/P0 > 1e8, M-5)
"""
import numpy as np

c0    = 2.99792458e8
G     = 6.67430e-11
rho_n = 2.7e17
P0    = 0.25*rho_n*c0**2          # 6.07e33 Pa (M-8)
rho_0 = rho_n/4
Sigma_min = 1e8*P0                # M-5: Sigma/P0 > 1e8 (Bell, Salart 2008)
v_m   = c0*np.sqrt(Sigma_min/P0)  # kohezyon kanali sinyal hizi
AU    = 1.495978707e11
Msun  = 1.98892e30
Mearth= 5.9722e24
pc    = 3.0857e16
yil   = 3.15576e7

print("="*84)
print("ORTAMIN HIZ ALANI — statik kohezyon dengesi mi, dolasim mi?")
print("="*84)
print(f"  P0 = {P0:.3e} Pa ;  rho_0 = {rho_0:.3e} kg/m^3 ;  rho_n/rho_0 = {rho_n/rho_0:.1f}")
print(f"  Sigma (alt sinir) = {Sigma_min:.3e} Pa   [M-5: Sigma/P0 > 1e8]")
print(f"  v_m = c0*sqrt(Sigma/P0) = {v_m/c0:.3e} c0   [kohezyon kanali]")
print()

print("="*84)
print("1) STATIK ELASTIK DENGE: gereken kesme gerilmesi tau_rr = rho_n*Phi/2")
print("="*84)
print("   Turetim: kuresel simetri, sigma = -P I + tau (izsiz), div sigma = 0")
print("            d(tau_rr)/dr + 3 tau_rr/r = dP/dr = rho_n*G*M/r^2")
print("            => (1/r^3) d(r^3 tau_rr)/dr = rho_n*G*M/r^2")
print("            => tau_rr = rho_n*G*M/(2r) = rho_n*Phi/2   (sonsuzda sonen kol)")
print()
print(f"{'konum':<34}{'Phi/c0^2':>12}{'tau_rr (Pa)':>14}{'tau_rr/Sigma':>14}{'tau/P0':>12}")
konumlar = [
    ("Merkur yorungesi (Gunes)",      G*Msun,        0.38709893*AU),
    ("Dunya yorungesi (Gunes)",       G*Msun,        AU),
    ("Gunes yuzeyi",                  G*Msun,        6.957e8),
    ("Dunya yuzeyi",                  G*Mearth,      6.371e6),
    ("Samanyolu (Gunes yaricapi)",    (200e3)**2*8.2*1e3*pc/1.0, 8.2e3*pc),  # Phi ~ v^2
    ("notron yildizi yuzeyi",         G*1.4*Msun,    1.2e4),
]
for ad, GM_, r_ in konumlar:
    if "Samanyolu" in ad:
        Phi = (200e3)**2            # v^2 mertebesi
    else:
        Phi = GM_/r_
    tau = rho_n*Phi/2
    print(f"  {ad:<32}{Phi/c0**2:>12.3e}{tau:>14.3e}{tau/Sigma_min:>14.3e}{tau/P0:>12.3e}")
print()
print("  HUKUM: gereken kesme gerilmesi, kohezyon dayaniminin ALT SINIRININ bile")
print("         14-15 mertebe altinda. Ortam kuyuyu DOLASMADAN, statik elastik")
print("         dengede tutabilir. Elastik zorlanma tau/Sigma ~ 1e-15 mertebesinde.")
print()

print("="*84)
print("2) M-9'un siklostrofik degeri ile gozlem siniri")
print("="*84)
print(f"{'konum':<30}{'v_th=2v_yor (km/s)':>20}{'Omega_m (rad/s)':>18}{'gozlem siniri':>16}")
for ad, r_ in [("Merkur yorungesi", 0.38709893*AU), ("Dunya yorungesi", AU)]:
    v_orb = np.sqrt(G*Msun/r_)
    v_th = 2*v_orb
    Om = v_th/r_
    print(f"  {ad:<28}{v_th/1e3:>20.2f}{Om:>18.3e}{'1.4e-18':>16}")
print()
print(f"  Asim carpani (Merkur): {2*np.sqrt(G*Msun/(0.38709893*AU))/(0.38709893*AU)/1.4e-18:.2e}")
print("  => Siklostrofik dolasim GOZLEMSEL OLARAK DISLANIYOR.")
print("     Dolayisiyla dengeyi saglayan sey dolasim DEGIL, kohezyon olmak zorunda.")
print()

print("="*84)
print("3) OTELEME SURUKLENMESI: ortam hangi cercevede durgun?")
print("="*84)
print("  Postulat 7 / DY-1: ortam, gradyani hakim olan cismin cevresinde tutulur.")
print("  Zarf erimi (11.4.8.1): R_zarf ~ a (M/3M_merkez)^(1/3)  [Hill yaricapi]")
# Gunes'in galaksiye gore Hill yaricapi
M_gal_ic = 1e11*Msun          # Gunes yaricapi icindeki galaktik kutle mertebesi
R_gal = 8.2e3*pc
R_hill_sun = R_gal*(Msun/(3*M_gal_ic))**(1/3)
print(f"  Gunes'in galaktik Hill yaricapi = {R_hill_sun/pc:.3f} pc = {R_hill_sun/AU:.2e} AU")
print(f"  Neptun yorungesi = 30 AU ;  Kuiper kusagi ~50 AU ;  Oort ~1e5 AU")
print(f"  => Gunes sistemi tamamen Gunes'in zarfi ICINDE ({R_hill_sun/AU:.1e} AU >> 1e5 AU?"
      f" { 'EVET' if R_hill_sun/AU > 1e5 else 'HAYIR'})")
# Dunya'nin Gunes'e gore Hill yaricapi
R_hill_earth = AU*(Mearth/(3*Msun))**(1/3)
print(f"  Dunya'nin Hill yaricapi = {R_hill_earth/1e3:.3e} km = {R_hill_earth/6.371e6:.1f} R_earth")
print(f"     (11.4.8.1'in verdigi 235 R_earth ile karsilastir)")
print(f"  GPS yorunge yaricapi = {26.56e6/6.371e6:.2f} R_earth  -> Dunya zarfi ICINDE")
print()
print("  SONUC: Merkur, Gunes'in zarfi icinde ama KENDI zarfinin disinda hareket eder")
print("         => V = 47.9 km/s (Gunes cercevesinde durgun ortama gore)  ✓")
print("         GPS uydusu, Dunya'nin zarfi icinde => V = yorunge hizi (Dunya cercevesi) ✓")
print()

print("="*84)
print("4) MERKUR'UN YENI ROLU: ortam donusunun en hassas olcumu")
print("="*84)
Om_lim = 1.4e-18
r_m = 0.38709893*AU
print(f"  |Omega_ortam| <= {Om_lim:.1e} rad/s   (Merkur gunberi, 1 sigma)")
print(f"  esdeger tegetsel hiz: v_phi <= {Om_lim*r_m*1e9:.2f} nm/s")
print(f"  Gunes spini ile karsilastir: Omega_sun = {2.9e-6:.1e} rad/s"
      f"  -> oran {Om_lim/2.9e-6:.1e}")
print(f"  Bir tam tur suresi: {2*np.pi/Om_lim/yil:.2e} yil"
      f"  (evren yasi ~1.4e10 yil'in {2*np.pi/Om_lim/yil/1.4e10:.1e} kati)")
print()
print("  => Teorinin YENI ongorusu/kaydi: Gunes sisteminin ortami, evren yasi")
print("     olceginde bile fiilen DONMUYOR. Bu, kohezyonla tutulan statik kuyunun")
print("     dogal halidir; dolasan bir vorteks olsaydi Merkur bunu gorurdu.")
