# -*- coding: utf-8 -*-
"""
SATURN ORTAMININ KILITLENMESI — ve genel teorem
================================================
GENEL TEOREM (bu betikte turetiliyor): Siklostrofik ortam dolasimi
    w(r) = 2 v_yor(r) = 2 sqrt(GM/r)
apsis suruklenme hizini
    Omega_m = w/r = 2 sqrt(GM/r^3) = 2n      (n = yorunge ortalama hareketi)
verir. Yani ORTAM DOLASIYORSA, HER yorungenin apsisi yorunge periyodunda TAM
IKI TUR atar. Bu, r'den ve M'den bagimsiz, evrensel bir imzadir.

Gozlenen apsis presesyonlari ise n'nin 1e-3 ... 1e-8 katidir. Dislama carpani
dogrudan  2n / omega_dot_gozlenen  olur — hassasiyet tartismasina gerek yok.

Bu betik: Saturn uydulari (+ karsilastirma icin Merkur, Ay, Jupiter uydusu)
icin dislama carpanlarini ve ortam donusu ust sinirlarini hesaplar.
"""
import numpy as np

arcsec = 180*3600/np.pi
gun = 86400.0
yil = 3.15576e7

# --- govde parametreleri ---
GM_sat   = 3.7931208e16     # m^3/s^2
R_sat    = 60268e3
J2_sat   = 1.629071e-2
GM_jup   = 1.26686534e17
R_jup    = 71492e3
J2_jup   = 1.4696e-2
GM_earth = 3.986004418e14
R_earth  = 6.371e6
J2_earth = 1.08263e-3
GM_sun   = 1.32712440018e20

def n_of(GM, a): return np.sqrt(GM/a**3)

def omega_J2(GM, a, R, J2, e=0.0, i=0.0):
    """J2 kaynakli apsidal presesyon (kucuk e,i): 1.5 n J2 (R/a)^2 * (1-e^2)^-2"""
    return 1.5*n_of(GM, a)*J2*(R/a)**2/(1-e**2)**2

print("="*94)
print("GENEL TEOREM: siklostrofik ortam => apsis suruklenmesi = 2n (yorunge basina TAM 2 TUR)")
print("="*94)
print("  w = 2 v_yor = 2 sqrt(GM/r)  =>  Omega_m = w/r = 2 sqrt(GM/r^3) = 2n")
print("  Sayisal denetim (Omega_m/n oranı her sistemde 2 cikmali):")
for ad, GM, a in [("Merkur", GM_sun, 0.38709893*1.495978707e11),
                  ("Ay", GM_earth, 3.844e8),
                  ("Titan", GM_sat, 1.22187e9),
                  ("Mimas", GM_sat, 1.8554e8)]:
    v = np.sqrt(GM/a); Om = 2*v/a; n = n_of(GM, a)
    print(f"    {ad:<8} Omega_m/n = {Om/n:.10f}")
print()

print("="*94)
print("SATURN SISTEMI — dislama carpanlari")
print("="*94)
uydular = [
    # ad, a (km), e, gozlenen apsidal presesyon periyodu (yil) [J2 hakim]
    ("Mimas",     185539, 0.0196),
    ("Enceladus", 237948, 0.0047),
    ("Tethys",    294619, 0.0001),
    ("Dione",     377396, 0.0022),
    ("Rhea",      527108, 0.0013),
    ("Titan",    1221870, 0.0288),
    ("Iapetus",  3560820, 0.0283),
]
print(f"{'uydu':<11}{'a (km)':>10}{'P_yor (gun)':>13}{'w_J2 (rad/s)':>15}"
      f"{'apsis per. (yil)':>18}{'Omega_m (rad/s)':>17}{'dislama':>11}")
sonuc = []
for ad, a_km, e in uydular:
    a = a_km*1e3
    n = n_of(GM_sat, a)
    P = 2*np.pi/n/gun
    wJ2 = omega_J2(GM_sat, a, R_sat, J2_sat, e)
    Tap = 2*np.pi/wJ2/yil
    Om_m = 2*n
    dis = Om_m/wJ2
    sonuc.append((ad, wJ2, Om_m, dis))
    print(f"  {ad:<9}{a_km:>10}{P:>13.3f}{wJ2:>15.4e}{Tap:>18.1f}{Om_m:>17.4e}{dis:>11.3e}")
print()
print("  Phoebe (retrograd, a=12,947,780 km, i=175.3 deg):")
a_ph = 12947780e3; n_ph = n_of(GM_sat, a_ph)
print(f"    n = {n_ph:.4e} rad/s (P = {2*np.pi/n_ph/gun:.1f} gun) ; Omega_m = 2n = {2*n_ph:.4e} rad/s")
print(f"    -> apsis 4 Gyr'de {2*n_ph*4e9*yil/(2*np.pi):.3e} tur atardi")
print()

print("="*94)
print("KARSILASTIRMA — diger sistemler (ayni yontem)")
print("="*94)
digerler = [
    ("Merkur (Gunes)",  GM_sun,   0.38709893*1.495978707e11, 575.3100/arcsec/(100*yil), "Park+2017 toplam presesyon"),
    ("Ay (Dunya)",      GM_earth, 3.844e8,   2*np.pi/(8.85*yil), "perigee 8.85 yil (LLR)"),
    ("LAGEOS-2 (Dunya)",GM_earth, 12163e3,   None, "J2 hakim"),
    ("Io (Jupiter)",    GM_jup,   421800e3,  None, "J2 hakim"),
]
print(f"{'sistem':<20}{'omega_dot goz. (rad/s)':>24}{'Omega_m=2n (rad/s)':>21}{'dislama':>12}")
for ad, GM, a, wobs, not_ in digerler:
    n = n_of(GM, a)
    if wobs is None:
        if "LAGEOS" in ad:  wobs = omega_J2(GM, a, R_earth, J2_earth)
        else:               wobs = omega_J2(GM, a, R_jup, J2_jup)
    print(f"  {ad:<18}{wobs:>24.4e}{2*n:>21.4e}{2*n/wobs:>12.3e}   ({not_})")
print()

print("="*94)
print("ORTAM DONUSU UST SINIRLARI (olcum hassasiyetinden)")
print("="*94)
print("  Yontem: |Omega_ortam| <= (apsidal hizin olcum belirsizligi)")
print()
print(f"{'sistem':<22}{'referans belirsizlik':<30}{'|Omega| ust sinir (rad/s)':>26}")
# Merkur: Park+2017 575.3100 +/- 0.0015 as/yy
dOm_merc = 0.0015/arcsec/(100*yil)
print(f"  {'Gunes ortami':<20}{'Merkur: +/-0.0015 as/yy':<30}{dOm_merc:>26.3e}")
# Ay: LLR apsidal rate ~1e-8 rel.
w_ay = 2*np.pi/(8.85*yil)
print(f"  {'Dunya ortami (Ay)':<20}{'LLR: ~1e-8 bagil':<30}{w_ay*1e-8:>26.3e}")
# Saturn: Cassini efemerid, muhafazakar 1e-5 bagil (Titan ve Mimas)
for ad, wJ2, Om_m, dis in sonuc:
    if ad in ("Mimas", "Titan", "Iapetus"):
        print(f"  {'Saturn ortami ('+ad+')':<20}{'Cassini efemerid: ~1e-5 bagil':<30}{wJ2*1e-5:>26.3e}")
print()
print("  NOT: dislama carpanlari 1e2-1e6 mertebesinde oldugundan, siklostrofik")
print("       hipotezin dislanmasi olcum hassasiyetine HIC bagli degil — model")
print("       tamamen coker. Hassasiyet yalnız KALAN donusun ust sinirini belirler.")
print()

print("="*94)
print("SONUC: kac bagimsiz ortam kilitlendi?")
print("="*94)
print("  1. Gunes ortami   — Merkur gunberi        |Omega| <= 2.3e-18 rad/s")
print("  2. Dunya ortami   — Ay perigee (LLR)      dislama 237x ; |Omega| <= ~2e-16")
print("  3. SATURN ortami  — Titan/Mimas apsisleri dislama 1e3-3e4x ; |Omega| <= ~1e-12..1e-15")
print("  (+ Jupiter ve Dunya-yapay uydu kanallari da ayni yontemle acik)")
print()
print("  Uc ayri govdenin ortami, uc bagimsiz gozlem ailesiyle STATIK ilan ediliyor.")
print("  Kohezyonla tutulan statik denge (tau_rr = rho_n*Phi/2 << Sigma) ucunu birden aciklar.")
