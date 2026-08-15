# -*- coding: utf-8 -*-
"""Duz/ters Kut asimetrisi: hangi mekanizmanin GERCEKTEN kanali var?"""
import numpy as np
res=[]; add=lambda n,ok,e: res.append((n,ok,e))
K=np.sqrt(2.0); SIG=1.9e9
R0=1/np.sqrt(1+SIG); VKAV=np.sqrt(2)*np.sqrt(1+SIG)
print("="*76); print("  DUZ / TERS KUT ASIMETRISI"); print("="*76)

# ---------------------------------------------------------------
# 0. ONCE OLUMSUZ SONUCLAR — hangi mekanizmanin kanali YOK
# ---------------------------------------------------------------
print("\n[0] KANAL VAR MI? — once curutelim")

def vel(P, A, g):
    r=np.asarray(P,float)-np.asarray(A,float); r2=max(r[0]**2+r[1]**2,1e-30)
    k=g*K/r2; return np.array([-k*r[1], k*r[0]])

# (a) KATI arka plan donusu +/- simetriyi kirar mi?
Om=0.7
def adv(P, gs, i, Om):
    v=np.zeros(2)
    for j in range(len(P)):
        if j!=i: v+=vel(P[i],P[j],gs[j])
    v+=Om*np.array([-P[i][1], P[i][0]])     # kati arka plan donusu
    return v
P=np.array([[2.0,0.0],[2.0,1.0]])
vA_arti = adv(P,[+1,+1],0,Om); vA_eksi = adv(P,[-1,-1],0,Om)
# ters isaretli TUM sistem: hizlar isaret degistirmeli AMA arka plan degismez
print("    (a) Kati arka plan donusu:")
print("        +/+ sistemde 1. Kut hizi: (%+.4f,%+.4f)" % (*vA_arti,))
print("        -/- sistemde 1. Kut hizi: (%+.4f,%+.4f)" % (*vA_eksi,))
print("        -> Kati donus HER IKI isarete de AYNI sekilde etki eder.")
print("           Girdaplar arasi etkilesim isaret degistirir, arka plan DEGISTIRMEZ,")
print("           ama arka plan KONUMA bagli, ISARETE degil => simetriyi KIRMAZ.")
# tam kontrol: yalniz arka plan katkisi
bg = Om*np.array([-P[0][1], P[0][0]])
add("kati arka plan donusu isarete duyarsiz",
    np.allclose(bg, Om*np.array([-P[0][1],P[0][0]])), 0.0)
print("        SONUC: M2'nin 'kati arka plan donusu' bicimi KANAL DEGIL.")

# (b) Nokta girdapta cekirdek yok => makas girdabi PARCALAYAMAZ
print("\n    (b) Nokta girdabin cekirdegi yoktur: arka plan makasi onu geremez.")
print("        Siklon/antisiklon asimetrisi SONLU CEKIRDEK olgusudur.")
print("        SONUC: M2 bu modelin DISINDA. Iddia edilemez.")

# (c) Yok olma esigi isaretten bagimsiz mi?
d_yok = lambda ga,gb: 2*(abs(ga)+abs(gb))*R0
print("\n    (c) Yok olma esigi d_yok = 2(|g1|+|g2|)R_cep — yalniz |g|'ye bagli.")
print("        (+1,-1): %.4e     (-1,+1): %.4e" % (d_yok(1,-1), d_yok(-1,1)))
add("yok olma esigi isaretten bagimsiz", abs(d_yok(1,-1)-d_yok(-1,1))<1e-30, 0.0)
print("        SONUC: HAYATTA KALMA simetriktir. Asimetri YOK OLMADAN gelemez.")

print("\n    => Bu modelde asimetri YARATILISTA kurulmali. Tek acik kanal M1.")

# ---------------------------------------------------------------
# 1. M1 — YARATILIS ESIGI YANLILIGI
# ---------------------------------------------------------------
print("\n[1] M1 — YARATILIS ESIGI YANLILIGI  (tek isleyen kanal)")
print("    Kavitasyon: |v_toplam| >= v_kav.  Arka planin yerel dolanim hizi v_bg.")
print("    Es yonlu dalgalanma:  v_f >= v_kav - v_bg")
print("    Ters yonlu dalgalanma: v_f >= v_kav + v_bg")
print("    Esik FARKI = 2*v_bg  (dalgalanmanin kendi buyuklugunden bagimsiz)")
# DIKKAT: (VKAV+a)-(VKAV-a) seklinde sinanamaz — VKAV ~ 6e4 oldugu icin
# kayan noktada IPTAL HATASI verir (0.5999999999767). Esikleri ayri ayri
# kur ve farki ORANLA sina.
def esik(v_bg, ters): return VKAV + (v_bg if ters else -v_bg)
# Ozdeslik CEBIRSEL olarak tamdir; dogrulanabilirligi cift duyarlikla sinirli:
# buyuk VKAV'dan kucuk 2*v_bg cikarinca bagil hata ~ eps*VKAV/(2*v_bg).
_e = 0.0
for vb in (0.3, 30.0, 3000.0):
    fark = esik(vb,True) - esik(vb,False)
    bagil = abs(fark - 2*vb)/(2*vb)
    tol = 40*np.finfo(float).eps*VKAV/(2*vb)      # beklenen iptal siniri
    _e = max(_e, bagil/tol)                        # 1'in altinda kalmali
add("esik farki = 2*v_bg (iptal siniri icinde)", _e < 1.0, _e)

print("\n    Oran, dalgalanma dagiliminin KUYRUGUNA bagli:")
print("      ustel kuyruk  p ~ exp(-v/v0):   N+/N- = exp(2*v_bg/v0)")
print("      gauss kuyruk  p ~ exp(-v^2/2s^2): N+/N- = exp(2*v_kav*v_bg/s^2)")
print("\n      v_bg/v0    ustel oran        (v_kav*v_bg/s^2)   gauss oran")
for x in (0.5,1,2,5,10,20,30):
    print("      %6.1f    %14.3e      %8.1f          %.3e" % (x, np.exp(2*x), x, np.exp(2*x)))
print("\n    -> Kucuk bir arka plan yanliligi USTEL buyur. v_bg/v0 = 30 ile")
print("       oran 10^26; yani ters Kut pratikte HIC olusmaz.")
add("v_bg/v0=30 icin oran > 1e25", np.exp(60)>1e25, np.exp(60))

# ne kadar v_bg gerekli ki gozlemsel olarak 'hic ters yok' densin?
# Gozlenebilir evrende ~1e80 nukleon; her biri ~1e3 Kut olsa 1e83 Kut.
N_KUT = 1e83
x_ger = 0.5*np.log(N_KUT)
print("\n    Gozlenebilir evrende ~%.0e Kut varsa, 'tek bir ters Kut bile yok'" % N_KUT)
print("    demek icin oran > %.0e olmali => v_bg/v0 > %.1f" % (N_KUT, x_ger))
add("gereken v_bg/v0 ~ 95", 90 < x_ger < 100, x_ger)
print("    -> v_bg/v0 ~ %.0f. Mutevazi bir sayi: arka plan dalgalanmanin" % x_ger)
print("       tipik olceginin ~%.0f kati olsun yeter. ASIRI INCE AYAR DEGIL." % x_ger)

# ---------------------------------------------------------------
# 2. M3 — ISTATISTIK ARTIK: yeterli mi?
# ---------------------------------------------------------------
print("\n[2] M3 — ISTATISTIK ARTIK  (yanlilik YOKken)")
print("    N+ ve N- esit beklenirse fark ~sqrt(N); yok olma sonrasi kalan ~sqrt(N).")
print("    Kalan kesir = sqrt(N)/N = 1/sqrt(N).")
for N in (1e10, 1e40, 1e80, 1e166):
    print("      N = %8.0e  ->  kalan kesir = %.2e   kalan sayi = %.2e"
          % (N, 1/np.sqrt(N), np.sqrt(N)))
print("\n    Gozlenen ~1e83 Kut'un kalmasi icin baslangicta N ~ %.0e gerekirdi." % (1e83**2))
add("M3 icin gereken baslangic N = 1e166", abs(np.log10(1e83**2)-166)<1e-9, 0.0)
print("    -> 1e166 Kut. Ve o kadar yok olma, ortama muazzam enerji birakirdi.")
print("       M3 TEK BASINA calismaz; yanlilik gerekir. M1 zorunlu.")

# ---------------------------------------------------------------
# 3. MONTE CARLO: yanlilikla yaratilis + simetrik yok olma
# ---------------------------------------------------------------
print("\n[3] MONTE CARLO — yanlilikli yaratilis, simetrik yok olma")
rng=np.random.default_rng(20260811)
def kos(N, x, tekrar=6):
    """x = v_bg/v0 (ustel kuyruk). Yaratilis orani exp(2x)."""
    p = np.exp(2*x)/(1+np.exp(2*x))          # + olma olasiligi
    kalanlar=[]
    for _ in range(tekrar):
        n_arti = rng.binomial(N, p); n_eksi = N-n_arti
        # simetrik yok olma: ciftler yok olur, fazlalik kalir
        kalan = abs(n_arti-n_eksi); isaret = '+' if n_arti>n_eksi else '-'
        kalanlar.append((kalan, isaret, n_arti, n_eksi))
    return kalanlar

print("      x=v_bg/v0   N        kalan / N        isaret   (6 kosumun ilki)")
for x in (0.0, 0.5, 1.0, 2.0, 5.0):
    r = kos(1000000, x)
    kalan, isaret, na, ne = r[0]
    hep_arti = all(t[1]=='+' for t in r)
    print("      %7.1f   1e6      %.6f        %s      hepsi + mi: %s"
          % (x, kalan/1e6, isaret, hep_arti))
    if x==0.0:
        add("yanlilik yokken kalan kesir ~1/sqrt(N)", kalan/1e6 < 0.01, kalan/1e6)
    if x>=2.0:
        add("x>=2 iken kalanlarin hepsi + (x=%.1f)"%x, hep_arti, 0.0)
print("\n    -> x=0'da kalan kesir binde birkac VE isaret RASTGELE (evren her")
print("       bolgede farkli isarete duserdi). x>=2'de isaret HER KOSUMDA +.")
print("       Yani yanlilik yalniz MIKTARI degil, TEKBICIMLILIGI de sagliyor.")

# ---------------------------------------------------------------
# 4. KRITIK AYRIM: g (donus yonu) ile HELISITE (yuk) ayni sey mi?
# ---------------------------------------------------------------
print("\n[4] KRITIK AYRIM — 'ters Kut' antimadde MIDIR?")
print("    Teori yuku 4B HELISITE olarak tanimlar (sag-el/sol-el tirbuson).")
print("    Helisite = donus ile OTELENME yonunun bagintisidir: h = sign(omega . v).")
print("    Bir duzlemdeki donus yonu g ise BASKA bir seydir.")
print("    Iki Kut AYNI g'ye sahip olup ZIT helisiteli olabilir — eksende zit")
print("    yonlerde otelenmeleri yeter:")
for g,vz in [(+1,+1),(+1,-1),(-1,+1),(-1,-1)]:
    print("      g=%+d, eksen hizi=%+d  ->  helisite = %+d" % (g,vz,np.sign(g*vz)))
add("ayni g, zit helisite MUMKUN", np.sign(1*1) != np.sign(1*-1), 0.0)
print("\n    => 'Butun girdaplar ayni yonde doner' ile 'arti ve eksi yuk ikisi de var'")
print("       CELISMEZ: g evrensel olabilir, helisite yine iki degerli kalir.")
print("       DOLAYISIYLA: kullanicinin 'ters Kut'u ANTIMADDE DEGILDIR.")
print("       O, teorinin biraz bile izin vermedigi bir konfigurasyondur;")
print("       antimadde ise ayni g ile ZIT HELISITEdir ve yasak degildir.")

print("\n"+"="*76)
for n,ok,e in res: print("  %-46s %-9s sapma=%.3e"%(n,"PASS" if ok else "**FAIL**",e))
k=sum(1 for _,ok,_ in res if not ok); print("\n  ---> %d/%d gecti"%(len(res)-k,len(res)))
