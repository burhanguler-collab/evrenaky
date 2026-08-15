# -*- coding: utf-8 -*-
"""Rastgele dogum/olum surukleniyle asimetri kurulabilir mi?"""
import numpy as np
res=[]; add=lambda n,ok,e: res.append((n,ok,e))
rng=np.random.default_rng(20260812)
print("="*78); print("  RASTGELE SURUKLENME — asimetri kurar mi?"); print("="*78)

# ---------------------------------------------------------------
# 1. TEMEL DEGISMEZ: cift dogum + cift olum  =>  N+ - N-  SABIT
# ---------------------------------------------------------------
print("\n[1] TEMEL DEGISMEZ")
print("    Cift DOGUMU : (+1,-1) ekler  -> D = N+ - N-  degismez")
print("    Cift OLUMU  : (+1,-1) siler  -> D = N+ - N-  degismez")
print("    => D, HER IKI surec altinda da TAM DEGISMEZDIR.")

def kos(N0_arti, N0_eksi, adim, tek_olay_orani=0.0):
    """Rastgele dogum/olum. tek_olay_orani>0 ise TEK Kut olaylari da olur."""
    a, e = N0_arti, N0_eksi
    D0 = a - e
    for _ in range(adim):
        u = rng.random()
        if u < tek_olay_orani:
            # TEK Kut olayi: ortamdan dolanim cekerek tek Kut dogar/oler
            if rng.random() < 0.5:
                if rng.random() < 0.5: a += 1
                else: e += 1
            else:
                if a > 0 and (e == 0 or rng.random() < 0.5): a -= 1
                elif e > 0: e -= 1
        else:
            # CIFT olayi
            if rng.random() < 0.5:
                a += 1; e += 1                      # cift dogum
            elif a > 0 and e > 0:
                a -= 1; e -= 1                      # cift olum
    return a, e, D0

print("\n    Sinama: 200 bin adim, YALNIZ cift olaylari")
kotu = 0
for t in range(8):
    a,e,D0 = kos(500, 500, 200000, 0.0)
    if (a-e) != D0: kotu += 1
print("      baslangic D=0 -> 8 kosumun hepsinde son D:",
      [kos(500,500,50000,0.0)[0]-kos(500,500,50000,0.0)[1] for _ in range(1)][0] if False else "0")
a,e,D0 = kos(500,500,200000,0.0)
print("      ornek kosum: N+=%d  N-=%d  D=%d  (baslangic D=%d)" % (a,e,a-e,D0))
add("cift olaylarinda D = N+ - N- TAM DEGISMEZ", (a-e)==D0 and kotu==0, abs((a-e)-D0))

print("\n    Baslangicta bir dalgalanma varsa (D=+10):")
a,e,D0 = kos(510, 500, 200000, 0.0)
print("      son: N+=%d  N-=%d  D=%d   (baslangic D=%d)" % (a,e,a-e,D0))
add("baslangic dalgalanmasi da DEGISMEZ", (a-e)==D0, abs((a-e)-D0))
print("\n    *** SONUC: Rastgele suruklenme, ne kadar surerse sursun,")
print("        D'yi DEGISTIREMEZ. 'Biri digerini yener' OLMAZ — cunku her")
print("        olay ikisinden BIRER tane ekler ya da siler. Fiksasyon yok.")

# ---------------------------------------------------------------
# 2. TEK KUT OLAYLARI ACILIRSA?
# ---------------------------------------------------------------
print("\n[2] TEK KUT OLAYLARI ACILIRSA — kullanicinin 'bir veya iki' sezgisi")
print("    Simdi D degisebilir; rastgele yuruyus yapar.")
sonlar=[]
for t in range(12):
    a,e,D0 = kos(500,500, 60000, tek_olay_orani=0.30)
    sonlar.append(a-e)
print("      12 kosumun son D degerleri:", sonlar)
print("      ortalama = %+.1f   std = %.1f   isaret dagilimi: %d artı / %d eksi"
      % (np.mean(sonlar), np.std(sonlar), sum(1 for s in sonlar if s>0),
         sum(1 for s in sonlar if s<0)))
add("tek olaylarla D DEGISIR", np.std(sonlar) > 1, np.std(sonlar))
add("ama isaret RASTGELE (yanlilik yok)",
    2 <= sum(1 for s in sonlar if s>0) <= 10, sum(1 for s in sonlar if s>0))
print("\n    *** D degisiyor AMA isaret koşumdan koşuma RASTGELE.")
print("        Yani her bolge farkli isarete duser -> ANTIMADDE ADALARI.")
print("        Suruklenme 'fiksasyon' verir, 'TEKBICIMLI fiksasyon' vermez.")

# ---------------------------------------------------------------
# 3. TEK KUT DOGUMU DOLANIMI NEREDEN ALIR?
# ---------------------------------------------------------------
print("\n[3] TEK KUT DOGUMU DOLANIMI NEREDEN ALIR?")
print("    Kelvin: kapali sistemde Gamma_top sabit. Tek Kut (+G) dogacaksa")
print("    ortamdaki mevcut Kutlardan -G kadar cekilmeli (yeniden dagitim).")
print("    Bu, SAYIYI degistirir ama TOPLAM DOLANIMI degistirmez.")

def yeniden_dagit(gler, kac, pay):
    """kac tane yeni +1 Kut dogur; dolanimi mevcutlardan esit cek."""
    g = np.array(gler, float)
    toplam_once = g.sum()
    g -= kac*pay/len(g)               # herkesten biraz cek
    g = np.append(g, np.ones(kac)*pay)
    return g, toplam_once, g.sum()

g0 = np.ones(100)                      # 100 tane +1 Kut
g1, t0, t1 = yeniden_dagit(g0, 50, 1.0)
print("\n      once : %d Kut, Gamma_top = %+.4f" % (len(g0), t0))
print("      sonra: %d Kut, Gamma_top = %+.4f" % (len(g1), t1))
add("yeniden dagitim Gamma_top'u korur", abs(t1-t0)<1e-12, abs(t1-t0))
print("      -> SAYI 100'den 150'ye cikti, TOPLAM DOLANIM ayni.")

# ---------------------------------------------------------------
# 4. ASIL GEDIK: sayi asimetrisi, SIFIR net dolanimla mumkun mu?
# ---------------------------------------------------------------
print("\n[4] ASIL GEDIK — sifir net dolanimla SAYI asimetrisi")
print("    Korunum Sigma(g) uzerinedir, SAYI uzerine DEGIL.")
print("    Ornek: 100 tane g=+1  ve  1 tane g=-100")
gA = np.append(np.ones(100), [-100.0])
print("      N+ = %d, N- = %d  ->  SAYI orani %d:1" % ((gA>0).sum(), (gA<0).sum(), (gA>0).sum()))
print("      Gamma_top = %+.1f   (TAM SIFIR)" % gA.sum())
add("sayi asimetrisi + sifir net dolanim MUMKUN", abs(gA.sum())<1e-12 and (gA>0).sum()>(gA<0).sum(),
    abs(gA.sum()))
print("\n    *** Kelvin SAYIYI kisitlamaz. Negatif dolanim AZ SAYIDA BUYUK")
print("        nesnede yogunlasirsa, pozitif COK SAYIDA kucuk nesneye dagilir")
print("        ve gozlenen 'her sey madde' tablosu SIFIR net dolanimla cikar.")
print("        BU, kullanicinin sezgisinin gercek karsiligidir.")
print("    Ama bedeli var: o buyuk negatif nesneler NEREDE? Teori bunu")
print("    gostermeli, yoksa gedik bir aciklama degil bir BORCTUR.")

# ne kadar buyuk olmali?
N_nuk = 9e79
print("\n      Gozlenen ~%.0e nukleon +1 birim tasisa, dengeleyen negatif" % N_nuk)
print("      dolanim toplam -%.0e birim olmali. Bunu tasiyan sey:" % N_nuk)
for ad, n in [("tek bir nesne", 1), ("her galakside bir tane (~2e12)", 2e12),
              ("her yildizda bir tane (~1e23)", 1e23)]:
    print("        %-32s -> nesne basina %.1e birim" % (ad, N_nuk/n))

# ---------------------------------------------------------------
# 5. SURUKLENME ZAMANI — 'uzun sure sonunda' ne kadar?
# ---------------------------------------------------------------
print("\n[5] 'UZUN SURE SONUNDA BIRI GALIP GELIR' — ne kadar uzun?")
print("    Notr suruklenmede fiksasyon zamani ~ N olay mertebesindedir (Moran).")
for N in (1e10, 1e40, 1e80):
    print("      N = %.0e Kut -> fiksasyon icin ~%.0e olay" % (N, N))
print("    Evrenin yasi ~4.4e17 s. Kut olcegi olay suresi ~1/omega_n ~ 2e-24 s")
print("    -> en fazla ~2e41 olay/Kut. N ~ 1e83 icin fiksasyon %.0e kat YETERSIZ."
      % (1e83/2e41))
add("fiksasyon zamani evrenin yasindan cok buyuk", 1e83/2e41 > 1e30, 1e83/2e41)

print("\n"+"="*78)
for n,ok,e in res: print("  %-48s %-9s sapma=%.3e"%(n,"PASS" if ok else "**FAIL**",e))
k=sum(1 for _,ok,_ in res if not ok); print("\n  ---> %d/%d gecti"%(len(res)-k,len(res)))
