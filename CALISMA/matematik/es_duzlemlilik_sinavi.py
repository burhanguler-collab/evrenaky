# -*- coding: utf-8 -*-
"""
ES-DUZLEMLILIK ve ORTAM DONUSU — bagimli sonuclarin envanteri
==============================================================
SORU: Ortam dolasmiyorsa (ortam_hiz_alani_cozumu.md), kitabin es-duzlemlilik ve
prograd tercih anlatilari ile ortam-dolasimina bagli sonuclari ne olur?

KITABIN KENDI KAYITLARI (okundu):
 * 18_5:313  "Es duzlemliligin gercek adresi F5'in duzlem secimidir (M-39);
              DAIRESELLIK ve PROGRAD TERCIHIN kanitlanmis mekanizmasi YOKTUR
              - acik kalem (7.4)"
 * 11.4:1172 "Ayakta duran sey F5'in duzlem secimidir - KORUNUMLUDUR, sonum
              gerektirmez... prograd tercih ve dairesellik ayri hesap kalemi (11.4-viii)"
 * KARNE s.35 "ES-DUZLEMLILIK ICIN MEKANIZMA BORCU YOKTUR. Egiklik korunumludur;
              donmus niceligi tutmak icin kuvvet gerekmez, gereken tek sey
              dagitacak kanalin olmamasidir."
 => ES-DUZLEMLILIK ORTAM DOLASIMINA DAYANMIYOR. (F5 = govdenin kendi donusu)

AMA dolasima BAGLI olan bir kume var:
 * 05_Oturma:136-138  retrograd/prograd suruklenme orani 3^4 = 81  (DY-2: ortam 2v)
 * 11.4:782,786       "ortamin siklostrofik dolasimi, her yaricapta prograd ve
                       maddeden hizli" -> prograd tork
 * 11.4:811           AU kararliligindan eta_E siniri (prograd tork uzerinden)
 * KARNE:765          Delta_v = v_yor*sqrt(5-4cos i)  (prograd v, retrograd 3v)
 * 18_5:565           M-39'un R2 rejimi "M-22 (R2'de hiz kaynagi)"

Bu betik: (a) 81 carpaninin dolasima bagimliligini gosterir, (b) ortam donusunu
BAGIMSIZ olarak sinayan gozlemleri hesaplar (Ay'in gunberi, Saturn uydulari).
"""
import numpy as np

G = 6.67430e-11
AU = 1.495978707e11
Msun = 1.98892e30
Mearth = 5.9722e24
Msat = 5.6834e26
yil = 3.15576e7
arcsec = 180*3600/np.pi

print("="*86)
print("1) 81 CARPANI — dolasima bagimliligi")
print("="*86)
print("  DY-2: ortam prograd yonde w = 2 v_yor ;  Delta_v = |v_cisim - w|")
print(f"{'kurulum':<34}{'prograd Dv':>14}{'retro Dv':>12}{'oran Dv^4':>14}")
for ad, w_kat in [("dolasan ortam (w = 2 v_yor)", 2.0), ("statik ortam (w = 0)", 0.0)]:
    dv_p = abs(1.0 - w_kat)      # v birimlerinde
    dv_r = abs(-1.0 - w_kat)
    oran = (dv_r/dv_p)**4 if dv_p > 0 else float('inf')
    print(f"  {ad:<32}{dv_p:>14.2f}{dv_r:>12.2f}{oran:>14.4g}")
print()
print("  => 81 carpani TAM OLARAK w = 2v varsayimindan gelir (3^4).")
print("     Statik ortamda prograd/retrograd ASIMETRI YOK: oran 1.")
print("     Kitabin 7.4 md.15'i bunu zaten SINAV olarak kaydetmis:")
print("     'Aynı geometrili prograd/retrograd uydu ciftlerinde ... fark sifir cikarsa")
print("      girdap kesme katsayisinin siniri bir kademe daha duser'")
print("     -> Statik cozum 'fark sifir' ongoruyor. Iki dislayici ongoru, tanimli sinav.")
print()

print("="*86)
print("2) ORTAM DONUSUNUN BAGIMSIZ SINAVLARI — apsis suruklenmesi")
print("="*86)
print("  Fizik (ortam_dolasimi_mp.py): apsis suruklenme hizi = Omega_ortam")
print("  Dolasan ortam varsayiminda Omega_m = 2 v_yor / r")
print()
print(f"{'sistem':<30}{'r (m)':>11}{'v_yor km/s':>12}{'Omega_m (rad/s)':>17}{'suruklenme periyodu':>21}")
sistemler = [
    ("Merkur (Gunes)",      G*Msun,   0.38709893*AU),
    ("Dunya (Gunes)",       G*Msun,   AU),
    ("AY (Dunya)",          G*Mearth, 3.844e8),
    ("GPS (Dunya)",         G*Mearth, 2.656e7),
    ("Titan (Saturn)",      G*Msat,   1.2219e9),
    ("Phoebe (Saturn)",     G*Msat,   1.2952e10),
]
for ad, GM_, r_ in sistemler:
    v = np.sqrt(GM_/r_)
    Om = 2*v/r_
    T = 2*np.pi/Om
    if T < 3*yil:
        Ts = f"{T/86400:.2f} gun"
    else:
        Ts = f"{T/yil:.2f} yil"
    print(f"  {ad:<28}{r_:>11.3e}{v/1e3:>12.3f}{Om:>17.3e}{Ts:>21}")
print()
print("  GOZLENEN apsis presesyonlari (karsilastirma):")
print("    Ay'in gunberi (perigee) presesyonu:  8.85 YIL periyot  (LLR ile mm hassasiyette)")
print("    Merkur gunberi: 42.98 as/yy  (dolasan ortam 1.15e9 as/yy verirdi)")
print()
Om_ay = 2*np.sqrt(G*Mearth/3.844e8)/3.844e8
T_ay = 2*np.pi/Om_ay
print(f"  AY KRITIK: dolasan ortam Ay'in apsisini {T_ay/86400:.2f} gunde bir tur dondururdu;")
print(f"             gozlenen periyot 8.85 yil = {8.85*yil/86400:.0f} gun")
print(f"             -> asim carpani {8.85*yil/T_ay:.0f}x  ->  KESIN DISLANIR")
print("             (Ay, Dunya'nin zarfi icinde: 60 R_earth < 235 R_earth  ✓")
print("              yani bu sinav DUNYA'nin ortamini bagimsiz olarak sinar)")
print()

print("="*86)
print("3) HANGI ORTAM HANGI GOZLEMLE KILITLENDI")
print("="*86)
print(f"{'ortam':<26}{'sinayan gozlem':<30}{'sonuc'}")
print(f"  {'Gunes cevresi':<24}{'Merkur gunberi 42.98 as/yy':<30}{'Omega <= 1.4e-18 rad/s'}")
print(f"  {'Dunya cevresi':<24}{'Ay perigee 8.85 yil (LLR)':<30}{'dolasim dislanir'}")
print(f"  {'Dunya cevresi':<24}{'GPS -7 mus/gun (kinematik)':<30}{'V = yorunge hizi ✓'}")
print(f"  {'Saturn cevresi':<24}{'uydu apsisleri (hesaplanmadi)':<30}{'ACIK — yapilacak'}")
print()
print("  => Iki bagimsiz gozlem (Merkur + Ay) iki ayri ortami statik ilan ediyor.")
print("     Kohezyonla tutulan statik denge, ikisini birden aciklayan tek resim.")
print()

print("="*86)
print("4) F5'IN DUZLEM SECIMI — dolasimsiz calisiyor mu?")
print("="*86)
print("  F5 yanal itim: f_yanal = -(kappa_5 rho v_e^2 / r) sin(2theta)")
print("  Kaynak: GOVDENIN KENDI donusu (v_e = ekvator hizi), ortam dolasimi DEGIL.")
print("  Kararlilik: theta>0 -> kuvvet -theta yonu (ekvatora); theta<0 -> +theta (ekvatora)")
print("  => Ekvator kararli denge; kutup kararsiz.  ORTAM DOLASIMI GEREKMEZ.  ✓")
print()
print("  Kitabin kendi kaydi (KARNE s.35): 'Es-duzlemlilik icin mekanizma borcu")
print("  yoktur. Egiklik korunumludur; donmus niceligi tutmak icin kuvvet gerekmez,")
print("  gereken tek sey dagitacak kanalin olmamasidir.'")
print("  => ES-DUZLEMLILIK STATIK ORTAMLA TAM UYUMLU. Hicbir sey kaybedilmiyor.")
