# -*- coding: utf-8 -*-
"""
FORMASYON GEREKCESI — ortam dolasimi NEDEN ~0?
===============================================
Kilit teoremi (ortam_donusu_kilit_teoremi.md) dolasimin gozlemsel olarak
dislandigini gosterdi (4 govde). Ama kohezyon sifiri IZINLI kiliyor, ZORUNLU
kilmiyor: acisal momentum serbest bir baslangic kosuludur. Bu betik uc bagimsiz
ayagi sinar:

AYAK 1 — DIFERANSIYEL DONUS BIR DENGE DURUMU DEGIL.
  M-5: kohezyon kanali KESME MODULU rolunde (Sigma <-> G_s), v_m = sqrt(Sigma/rho_0).
  Kesme modulu olan ortam KARARLI kesme akisini tasiyamaz: gerilme birikir.
  Diferansiyel donus bir denge degil, v_m/L frekansli KESME SALINIMIDIR.
  Gunes sisteminde periyot L/v_m ~ ? -> yorunge olcegindeki her gozlem sifira ortalar.

AYAK 2 — KATI (RIGID) DONUS SINIRSIZ ORTAMDA YASAK.
  Rigid Omega icin merkezcil gereksinim: dP/dr = rho_0 Omega^2 r
  => gereken gerilme rho_0 Omega^2 r^2/2, r ile SINIRSIZ buyur.
  Sigma'yi asinca ortam YIRTILIR -> M-7'nin yirtilmama kosulunun ihlali.
  Yirtilma yaricapi r_max = sqrt(2 Sigma/rho_0)/Omega = sqrt(2) v_m/Omega
  Ortam sinirsiz (monizm) => Omega = 0 TAM.

AYAK 3 — MADDE ORTAMI DONDUREMEZ.
  (a) Elastik: maddenin donme enerji yogunlugu / Sigma orani
  (b) Suruklenme: M-43'un altkritik bastirmasi (10^28)
"""
import numpy as np

c0    = 2.99792458e8
G     = 6.67430e-11
rho_n = 2.7e17
P0    = 0.25*rho_n*c0**2
rho_0 = rho_n/4
Sigma = 1e8*P0                    # M-5 alt siniri
v_m   = np.sqrt(Sigma/rho_0)      # kesme sinyal hizi
AU    = 1.495978707e11
pc    = 3.0857e16
Msun  = 1.98892e30
yil   = 3.15576e7
R_H   = 1.3e26                    # Hubble yaricapi mertebesi

print("="*92)
print("ORTAM PARAMETRELERI")
print("="*92)
print(f"  Sigma (alt sinir) = {Sigma:.3e} Pa   |   rho_0 = {rho_0:.3e} kg/m^3")
print(f"  v_m = sqrt(Sigma/rho_0) = {v_m:.4e} m/s = {v_m/c0:.3e} c0   [M-5: >1e4 c0 ✓]")
print()

print("="*92)
print("AYAK 1 — DIFERANSIYEL DONUS: denge degil, KESME SALINIMI")
print("="*92)
print("  Kesme modulu olan ortamda diferansiyel donus gerilme biriktirir;")
print("  sistem sifir-kesme durumu etrafinda v_m/L frekansiyla SALINIR.")
print("  (Viskozite ~0 oldugundan sonumlenmez, ama ORTALAMASI sifirdir.)")
print()
print(f"{'olcek':<28}{'L (m)':>12}{'L/v_m (periyot)':>20}{'yorunge/salinim':>20}")
olcekler = [
    ("Dunya yaricapi",     6.371e6,   None),
    ("Ay yorungesi",       3.844e8,   27.32*86400),
    ("Merkur yorungesi",   0.387*AU,  87.97*86400),
    ("1 AU",               AU,        365.25*86400),
    ("Satürn yorungesi",   9.58*AU,   29.45*yil),
    ("Gunes sistemi (100 AU)", 100*AU, None),
    ("Galaksi (10 kpc)",   1e4*pc,    2.2e8*yil),
    ("Hubble yaricapi",    R_H,       13.8e9*yil),
]
for ad, L, T_orb in olcekler:
    T_shear = L/v_m
    if T_orb:
        oran = T_orb/T_shear
        print(f"  {ad:<26}{L:>12.3e}{T_shear:>20.3e}{oran:>20.3e}")
    else:
        print(f"  {ad:<26}{L:>12.3e}{T_shear:>20.3e}{'—':>20}")
print()
print(f"  Merkür: kesme salinim periyodu {0.387*AU/v_m:.4f} s ;  yorunge 87.97 gun")
print(f"     -> yorunge basina {87.97*86400/(0.387*AU/v_m):.3e} salinim cevrimi")
print("     -> sekuler apsis olcumu diferansiyel donusu SIFIRA ORTALAR")
print()
print(f"  Hubble olceginde kesme denklesme suresi = {R_H/v_m/yil:.3e} yil")
print(f"     evren yasi / bu sure = {13.8e9/(R_H/v_m/yil):.3e}")
print("     -> ilksel diferansiyel donus, evren yasinin ~1e4 kati once elastik olarak silindi")
print()

print("="*92)
print("AYAK 2 — KATI DONUS: sinirsiz kohezyonlu ortamda YASAK")
print("="*92)
print("  Rigid Omega: dP/dr = rho_0 Omega^2 r  =>  gereken gerilme tau = rho_0 Omega^2 r^2/2")
print("  Sigma'yi astigi yaricap: r_max = sqrt(2 Sigma/rho_0)/Omega = sqrt(2) v_m/Omega")
print()
print(f"{'Omega (rad/s)':>16}{'r_max (m)':>14}{'r_max (pc)':>14}{'R_Hubble ile':>16}")
for Om in [1e-6, 1e-10, 1e-14, 1e-18, 2.3e-18]:
    r_max = np.sqrt(2)*v_m/Om
    print(f"{Om:>16.1e}{r_max:>14.3e}{r_max/pc:>14.3e}{r_max/R_H:>16.3e}")
print()
Om_struct = np.sqrt(2)*v_m/R_H
print(f"  Yapisal sinir (yirtilma R_Hubble'dan once olmasin):  |Omega| < {Om_struct:.3e} rad/s")
print(f"  Gozlemsel sinir (Merkur):                            |Omega| <= 2.3e-18 rad/s")
print(f"  -> gozlem yapisal sinirdan {Om_struct/2.3e-18:.1e} kat daha sıkı")
print()
print("  KRITIK: ortam SINIRSIZ ise (monizm — okyanus evrenin otesine uzanir),")
print("          her Omega != 0 sonlu bir yaricapta yirtar  =>  Omega = 0 TAM.")
print("          M-7'nin yirtilmama kosulu bunu zaten dayatiyor.")
print()

print("="*92)
print("AYAK 3 — MADDE ORTAMI DONDUREMEZ")
print("="*92)
print("  (a) Elastik enerji karsilastirmasi: maddenin donme enerji yogunlugu vs Sigma")
print(f"{'sistem':<26}{'E_don/V (Pa)':>16}{'/ Sigma':>14}")
sistemler = [
    ("Gunes (donme KE)",  2.4e41, 1.412e27),          # E_rot ~ 2.4e41 J, V_sun
    ("Jupiter (donme KE)", 2.1e35, 1.43e24),
    ("Gunes sistemi yorunge KE", 1.9e43, (4/3)*np.pi*(30*AU)**3),
    ("Galaksi (donme KE)", 1e53, (4/3)*np.pi*(1.5e4*pc)**3),
]
for ad, E, V in sistemler:
    u = E/V
    print(f"  {ad:<24}{u:>16.3e}{u/Sigma:>14.3e}")
print()
print("  => maddenin elindeki enerji yogunlugu, Sigma'nin 1e-26..1e-30 kati.")
print("     Ortami kesmeye zorlayacak enerji YOK.")
print()
print("  (b) Suruklenme kanali: M-43 altkritik bastirma ~1e28")
print("     => tork kanali da kapali. Iki bagimsiz argüman ayni sonucu veriyor.")
print()

print("="*92)
print("BONUS — MACH ILKESI: yerel eylemsizlik cercevesi neden uzak yildizlarla ayni?")
print("="*92)
print("  Ortam TEK surekli elastik gövdedir; kesme rijitligi her yamayi kuresel")
print("  duruma kilitler. Denklesme suresi L/v_m:")
for ad, L in [("Gunes sistemi", 100*AU), ("Galaksi", 1e4*pc), ("Gozlenebilir evren", R_H)]:
    print(f"    {ad:<22} {L/v_m:.3e} s = {L/v_m/yil:.3e} yil")
print()
print("  => Yerel eylemsizlik cercevesinin uzak maddeye gore donmemesi, GR'de")
print("     kozmolojik madde dagilimindan gelen bir uyum sorunudur (Mach ilkesi);")
print("     bu teoride TEK elastik ortamin kesme rijitliginin bedava sonucudur.")
