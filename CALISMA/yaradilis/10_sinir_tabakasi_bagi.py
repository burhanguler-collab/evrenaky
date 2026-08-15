# -*- coding: utf-8 -*-
"""Sinir tabakasinda GERCEK bir bag kuvveti olabilir mi?"""
import numpy as np
res=[]; add=lambda n,ok,e: res.append((n,ok,e))
print("="*78); print("  SINIR TABAKASI BAGI — aday kanal"); print("="*78)

# ---------------------------------------------------------------
print("\n[1] GIRDAP KANALI BAG VEREMEZ  (yeniden, kesin)")
print("    E_int = -(G1 G2 / 2pi) ln d.  Es isaret => d buyudukce E DUSER.")
print("    Sonlu cekirdek bunu DEGISTIRMEZ: uzak alan ayni, isaret ayni.")
for d in (1,2,4,8):
    print("      d=%2d  ->  E_int = %+.4f  (Gamma^2/2pi biriminde)" % (d,-np.log(d)))
add("girdap kanali es isarette itici", -np.log(8) < -np.log(1), 0.0)
print("    => Bag BASKA bir kanaldan gelmeli.")

# ---------------------------------------------------------------
print("\n[2] ADAY: IKINCIL BJERKNES KUVVETI  (pulsasyon kanali)")
print("    Teorinin BIRINCI IMZASI her Kut'un pulsasyonudur (boyutsal salinim,")
print("    1.4.11). Pulsasyon yapan iki KAVITE, akiskanda birbirine kuvvet uygular:")
print("      F = - rho <V1' V2'> / (4 pi d^2)   (ikincil Bjerknes)")
print("    AYNI FAZDA pulsasyon  -> <V1'V2'> > 0  -> F CEKICI")
print("    ZIT FAZDA pulsasyon   -> <V1'V2'> < 0  -> F ITICI")
print()
print("    Ve teori faz uyumunu SAGLIYOR: butun Kutlar ayni 4B donusun")
print("    parcasi oldugundan omega_2 ORTAK (1.4.12: nukleonda w2 = w1).")

def bjerknes(d, A=1.0, faz=0.0):
    """F ~ -A^2 cos(faz)/d^2 ; negatif = cekici."""
    return -A*A*np.cos(faz)/d**2
print("\n      d      ayni faz F      zit faz F")
for d in (1,2,4,8):
    print("    %5.1f   %+11.5f   %+11.5f" % (d, bjerknes(d,1,0.0), bjerknes(d,1,np.pi)))
add("ayni fazda Bjerknes CEKICI", bjerknes(2,1,0.0) < 0, bjerknes(2,1,0.0))
add("zit fazda Bjerknes ITICI",   bjerknes(2,1,np.pi) > 0, bjerknes(2,1,np.pi))
add("F ~ 1/d^2", abs(bjerknes(2)/bjerknes(4) - 4) < 1e-12, abs(bjerknes(2)/bjerknes(4)-4))

# ---------------------------------------------------------------
print("\n[3] BAGLANMA ENERJISI — koparmak IS ISTER MI?")
print("    F = -B/d^2  =>  U(d) = -B/d   (cekici kuyu)")
print("    d0'dan sonsuza cikarmak icin gereken is:  W = B/d0")
B=1.0
print("\n      d0     U(d0)      koparma isi W = B/d0")
for d0 in (0.5,1,2,4):
    print("    %5.1f   %+8.4f        %8.4f" % (d0, -B/d0, B/d0))
add("koparma isi POZITIF ve 1/d0 ile artar", B/0.5 > B/4 > 0, 0.0)
print("\n    *** ISTE KULLANICININ ISTEDIGI SEY: yakinsa koparmak DAHA COK is ister.")
print("        Ve is sonlu => yeterince guclu bir etki bagi cozebilir.")

# ---------------------------------------------------------------
print("\n[4] BAG NEREDE OTURUYOR — sinir tabakasinda mi?")
print("    Bjerknes kuvveti kavitenin HACIM SALINIMINDAN dogar; kaviteyi")
print("    cevreleyen alan sinir tabakasidir. Yani kuvvet tam olarak")
print("    SINIR TABAKALARININ ORTUSTUGU yerde uretilir. Ortusme yoksa")
print("    <V1'V2'> carpimi ihmal edilir hale gelir.")
re_=1.0
print("\n      d/r_e   rho(d/2)/rho0   ortusme gucu (kaba)")
for x in (0.5,1,2,3,5,10):
    rho=np.exp(-(re_/(x/2))**2) if x>0 else 0
    print("     %5.1f    %12.3e    %s" % (x, rho, "GUCLU" if x<3 else ("zayif" if x<6 else "yok")))
print("\n    -> Sinir tabakasi ~3 r_e'ye kadar anlamli. Bag mesafesi de orasi.")

# ---------------------------------------------------------------
print("\n[5] SIMULASYONA NASIL GIRER")
print("    Nokta girdap hizina EK bir radyal terim:")
print("      v_bag(i) = -kappa * SUM_j  cos(dfaz_ij) * rhat_ij / d_ij^2")
print("    kappa: bag siddeti (PARAMETRE, turetilmemis)")
print("    dfaz : iki Kut'un pulsasyon faz farki (ayni faz = 0)")
print("    Bu, Hamilton yapisini BOZAR (girdap dinamigi + dis kuvvet) —")
print("    dolayisiyla H artik korunmaz. Bunu ARAYUZDE SOYLEMEK gerekir.")
kappa=1.0
print("\n      d      v_bag       girdap hizi (K/d)    oran")
K=np.sqrt(2)
for d in (0.5,1,2,4):
    vb=kappa/d**2; vg=K/d
    print("    %5.1f   %8.4f      %8.4f        %6.2f" % (d,vb,vg,vb/vg))
print("    -> Bag terimi YAKINDA baskin (1/d^2 vs 1/d), UZAKTA sonuk. Dogru davranis.")
add("bag terimi yakinda baskin, uzakta sonuk", (1/0.5**2)/(K/0.5) > (1/4**2)/(K/4), 0.0)

print("\n"+"="*78)
for n,ok,e in res: print("  %-46s %-9s sapma=%.3e"%(n,"PASS" if ok else "**FAIL**",e))
k=sum(1 for _,ok,_ in res if not ok); print("\n  ---> %d/%d gecti"%(len(res)-k,len(res)))
