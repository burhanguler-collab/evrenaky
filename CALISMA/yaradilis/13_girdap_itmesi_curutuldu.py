# -*- coding: utf-8 -*-
"""GIRDAP ITMESI TERIMININ CURUTULMESI  (12 Agu 2026)

§8.8'de modele  F = A/d ,  A = 2*pi*K^2 = 4*pi  bicimde bir "girdap itmesi"
eklenmisti. Gerekcesi: es-yonlu ciftin TOPLAM alaninda arada basinc sirti
(rho=rho0), disarida cukur (rho=0.454) var; bosluk dusuk basinca gider,
oyleyse Kutlar disa itilir.

Bu betik o terimin UC AYRI yerden yanlis oldugunu gosterir:
  1) ISARET  — kuvvet itici degil CEKICI
  2) USTEL   — 1/d degil 1/d^3
  3) BUYUKLUK— d=20'de gercekten ~2520 kat buyuk
ve hatanin kokunu tespit eder: kuvvet TOPLAM alandan hesaplanmisti, oysa bir
Kut'un kendi oz-alani kendini itemez.

Sonuc: terim kaldirildi, arayuz varsayilani KAPALI, §8.8 supersede edildi.
Bkz. 00_CALISMA_Yaradilis_ve_Asimetri.md §8.12
"""
import numpy as np

res = []
add = lambda n, ok, e: res.append((n, ok, e))
K = np.sqrt(2.0)          # |v| = K/r  (kod birimi: r_e=1'de |v| = sqrt2 c)

print("=" * 78)
print("  GIRDAP ITMESI TERIMI DOGRU MU?   F = A/d ,  A = 4*pi")
print("=" * 78)

# ---------------------------------------------------------------------------
print("\n[1] TEK KUT ETRAFINDA BASINC — hangi yone artiyor?")
print("    Modelin kendi yasasi:  rho/rho0 = exp(-(r_e/R)^2)")
print("    Stiff akiskan:         P = c^2 rho   =>  P/P0 = rho/rho0")

P  = lambda R: np.exp(-1.0 / R**2)
dP = lambda R: np.exp(-1.0 / R**2) * (2.0 / R**3)

print("\n      R/r_e      P/P0        dP/dR")
for R in (0.5, 1, 2, 3, 5, 10, 20):
    print("    %7.1f   %10.6f  %+11.3e" % (R, P(R), dP(R)))

add("P her yerde DISA dogru artar", all(dP(R) > 0 for R in (0.5, 1, 2, 5, 20)), 0.0)
print("\n    -> Girdaba YAKLASTIKCA hiz artar, basinc DUSER (Bernoulli).")

# sayisal turev kontrolu — analitik ifade dogru mu
eps, R0 = 1e-6, 3.0
say = (P(R0 + eps) - P(R0 - eps)) / (2 * eps)
add("dP/dR sayisal = analitik", abs(say - dP(R0)) < 1e-6, abs(say - dP(R0)))

# ---------------------------------------------------------------------------
print("\n[2] BOSLUGA ETKIYEN KUVVET — hangi yone?")
print("    Hacim V olan bir BOSLUK icin yuzey basinc kuvveti:  F = -V grad(P)")
print("    Klasik sonuc: bosluk/kabarcik DUSUK basinca gider.")
print("\n      R        dP/dR        F_R = -V dP/dR      yon")
for R in (2, 5, 10, 20):
    f = -dP(R)
    print("    %5.1f   %+11.3e    %+14.3e      %s"
          % (R, dP(R), f, "ICERI = CEKICI" if f < 0 else "DISA = ITICI"))

add("bosluga etkiyen kuvvet CEKICI", all(-dP(R) < 0 for R in (2, 5, 10, 20)), 0.0)
print("\n    *** KIRILMA 1 — ISARET TERS.")
print("        Bu, kabarciklarin girdap cekirdeginde toplanmasidir;")
print("        gercek akiskanlarda evrensel gozlenen olgu.")

# ---------------------------------------------------------------------------
print("\n[3] USTEL — 1/d mi, 1/d^3 mu?")
print("    Buyuk R icin exp(-1/R^2) -> 1, dolayisiyla dP/dR -> 2/R^3.")
print("\n      R      gercek dP/dR     2/R^3        oran      benim 4pi/R")
for R in (5, 10, 20, 40, 80):
    print("    %5.1f   %+12.3e   %+11.3e   %7.4f   %11.4f"
          % (R, dP(R), 2 / R**3, dP(R) / (2 / R**3), 4 * np.pi / R))

add("yasa 1/d^3 (R=40'ta %0.1 icinde)",
    abs(dP(40) / (2 / 40**3) - 1) < 1e-3, abs(dP(40) / (2 / 40**3) - 1))
print("\n    *** KIRILMA 2 — USTEL YANLIS. Gercek 1/d^3, benimki 1/d.")

oran = (4 * np.pi / 20) / dP(20)
print("\n    d=20'de:  gercek %.3e   ·   benim terim %.4f   ·   ORAN %.0f kat"
      % (dP(20), 4 * np.pi / 20, oran))
add("A/d terimi d=20'de >=1000 kat buyuk", oran > 1e3, oran)
print("    *** KIRILMA 3 — BUYUKLUK OLCEKSIZ.")

# ---------------------------------------------------------------------------
print("\n[4] HATANIN KOKU — 'aradaki sirt' argumani nerede coktu?")

def vtot(x, y, ps, gs):
    v = np.zeros(2)
    for (qx, qy), g in zip(ps, gs):
        rx, ry = x - qx, y - qy
        r2 = max(rx * rx + ry * ry, 1e-30)
        v += np.array([-g * K * ry / r2, g * K * rx / r2])
    return v

rho = lambda v: np.exp(-(v[0]**2 + v[1]**2) / 2.0)
d = 3.0
A, B = (-d / 2, 0), (d / 2, 0)

print("    Iki es girdap +-1.5'te. Kiyaslama: TOPLAM alan  vs  YALNIZ A'nin alani")
print("\n      Konum            TOPLAM rho     YALNIZ A")
for x, ad in [(-1.5, "A merkezi"), (-0.75, "arada"), (0.0, "TAM ORTA"),
              (0.75, "arada"), (1.5, "B merkezi"), (3.0, "B disi")]:
    print("    %6.2f (%-9s)   %10.6f   %10.6f"
          % (x, ad, rho(vtot(x, 0, [A, B], [1, 1])), rho(vtot(x, 0, [A], [1]))))

print("\n    TOPLAM alanda orta nokta yuksek (1.000), disi dusuk (0.454)")
print("    -> 'bosluk disa itilir' sonucunu buradan cikarmistim.")
print("\n    HATA: B'ye etkiyen kuvvet, B HARIC alandan hesaplanir.")
print("          Kendi oz-alani kendini itemez. Ortadaki 'sirt' zaten iki alanin")
print("          birbirini goturmesinden dogan bir SUPERPOZISYON eseridir.")

e2 = 1e-4
g1 = rho(vtot(1.5 - e2, 0, [A], [1]))
g2 = rho(vtot(1.5 + e2, 0, [A], [1]))
grad = (g2 - g1) / (2 * e2)
print("\n    A'nin alaninda, B'nin yerinde (x=+1.5):")
print("      dP/dx = %+.6e   =>   F = -dP/dx = %+.6e   (%s)"
      % (grad, -grad, "A'YA DOGRU = CEKICI" if -grad < 0 else "A'DAN UZAGA"))
add("A'nin alani B'yi CEKER", -grad < 0, -grad)

# ---------------------------------------------------------------------------
print("\n[5] SONUC")
print("    Terim UC yerden birden yanlis. Kaldirildi; arayuz varsayilani KAPALI.")
print("    §8.8'in tamami (dis engel, kappa_min=75.4, A d^2 - kappa d + kappa d0 = 0)")
print("    GECERSIZ.")
print()
print("    Yerine gecen yapi zaten vardi ve dogru bicimdeydi:")
print("      kappa (1 - d0/d)/d^2  =  kappa/d^2  -  kappa d0/d^3")
print("      uzakta 1/d^2 CEKIM (Bjerknes) · yakinda 1/d^3 ITME (cepler")
print("      ic ice gecemez) · TEK kararli kok d0 · dis engel YOK.")
print()
print("    Olculen sonuc (simulasyonda): terim kapaliyken 40 Kut'luk toplulukta")
print("    yayilim 0.47x'e buzuluyor ve 7 obege oturuyor; acikken 4.47x saciliyor.")

print("\n" + "=" * 78)
kotu = sum(1 for _, ok, _ in res if not ok)
for n, ok, e in res:
    print("  %-42s %-9s sapma=%.3e" % (n, "PASS" if ok else "**FAIL**", e))
print("\n  ---> %d/%d gecti" % (len(res) - kotu, len(res)))
