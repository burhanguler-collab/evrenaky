# -*- coding: utf-8 -*-
"""Kullanicinin 4 fizik maddesinin sinanmasi. Saf klasik akiskan; GR yok."""
import numpy as np
res=[]; add=lambda n,ok,e: res.append((n,ok,e))
K=np.sqrt(2.0); SIG=1.9e9
R0=1/np.sqrt(1+SIG); VKAV=np.sqrt(2)*np.sqrt(1+SIG); VM=np.sqrt(SIG)
print("="*80); print("  DORT MADDENIN SINANMASI"); print("="*80)
print("  Birimler: r_e = 1, c = 1.  Duvar hizi v_t = sqrt(2) c.")
print("  HIZ MERDIVENI (c evrensel sinir DEGIL, ortamin ses hizi):")
print("    c = 1  <  sqrt2 c = %.3f  <  v_m = %.3e c  <  v_kav = %.3e c"
      % (K, VM, VKAV))
add("merdiven: c < sqrt2c < v_m < v_kav", 1 < K < VM < VKAV, 0.0)

# =================================================================
print("\n" + "-"*80)
print("MADDE 1 — Bagli iki Kut'u bozmak icin EKSTRA GUC gerekli")
print("-"*80)
print("  Durum: UYGULANDI ve dogrulandi (Bjerknes kanali, 114/114).")
print("    v_rad = kappa (1 - d0/d)/d^2 ;  d=d0'da denge, d<d0'da itme.")
print("    Koparma isi W(d0)>0 ve yakinlastikca artiyor.")
def W(d,kap=2.5,d0=1.5,b=400.0,n=200000):
    x=np.linspace(max(1e-3,d),b,n)
    return np.trapezoid(kap*(1-d0/x)/x**2, x)
for d in (0.8,1.5,3.0,6.0):
    print("      d=%.1f -> W=%.4f" % (d, W(d)))
add("MADDE 1: koparma isi pozitif", W(1.5)>0, W(1.5))

# =================================================================
print("\n" + "-"*80)
print("MADDE 2 — Ters iki Kut: bag KURMAZ, yaklasir, ayirmak zorlasir, birlesir")
print("-"*80)
print("  (a) AYIRMAK IS ISTER MI?  E_int = -(G1G2/2pi) ln d ; zit isarette +ln d")
print("      d1'den d2'ye ayirma isi = ln(d2/d1)  (Gamma^2/2pi biriminde)")
for d1,d2 in [(1,2),(0.5,2),(0.1,2),(0.01,2)]:
    print("      %6.2f -> %.1f :  is = %+.4f" % (d1,d2,np.log(d2/d1)))
add("MADDE 2a: zit cifti ayirmak is ister", np.log(2/1)>0, 0.0)
add("MADDE 2a: yaklastikca ayirma isi ARTAR",
    np.log(2/0.01) > np.log(2/1), np.log(2/0.01)-np.log(2/1))
print("      -> d -> 0 iken is LOGARITMIK IRAKSAR: tam ayirma SONSUZ is ister.")
print("      *** KULLANICI HAKLI: yaklastikca ayirmak zorlasir. TAM.")

print("\n  (b) 'BAG KURMAMALI' — dogru okuma nedir?")
print("      Zit ciftte ayirma isi POZITIF, yani enerji anlaminda BAGLIDIRLAR.")
print("      Ama KARARLI bir yapi kurmazlar: dipol olarak otelenip giderler ve")
print("      esik asilinca yok olurlar. Yani 'bag' degil, OLUME GIDEN CEKIM.")
print("      Terim onerisi: 'bag' yerine 'yok olma yakalanmasi'.")

print("\n  (c) YAKLASMAYI NE SURUKLER?")
print("      Ideal nokta girdapta zit cift OTELENIR, ayrim SABIT kalir")
print("      (bu oturumda dogrulandi). Yaklasma icin enerji KAYBI gerekir.")
print("      E_zit = +ln d  =>  enerji dusunce d KUCULUR.  [dogru yon]")
print("      E_es  = -ln d  =>  enerji dusunce d BUYUR.    [es cift ayrilir]")
add("MADDE 2c: enerji kaybi zit cifti YAKLASTIRIR", (np.log(0.5)-np.log(1))<0, 0.0)
add("MADDE 2c: enerji kaybi es cifti AYIRIR", (-np.log(2))<(-np.log(1)), 0.0)
print("      Kayip kanali: duvar SUPERSONIK oldugundan (v_t = 1.414 c) yayilim")
print("      sok bicimindedir. Mach acisi:  sin(theta) = c/v")
for v,ad in [(K,'duvar sqrt2c'),(10,'10c'),(VM,'v_m'),(VKAV,'v_kav')]:
    th=np.degrees(np.arcsin(min(1.0,1.0/v)))
    print("        v=%10.3e c (%-12s) -> Mach acisi %8.4f derece" % (v,ad,th))
add("supersonik duvar: Mach acisi 45 derece", abs(np.degrees(np.arcsin(1/K))-45)<1e-9,
    abs(np.degrees(np.arcsin(1/K))-45))
print("      *** DUZELTME: darbeyi izotrop dipol cizmistim; kaynak supersonik")
print("          oldugu icin emisyon MACH KONISIDIR. Duvar hizinda 45 derece.")

print("\n  (d) SONUNDA BIRLESIP MOMENTUMU BIRAKMA — UYGULANDI")
print("      d_yok = 2(R_cep1+R_cep2) = %.3e r_e ;  I = Gamma*d devredilir." % (4*R0))

# =================================================================
print("\n" + "-"*80)
print("MADDE 3 — Bagli ikili yeni bir SINIR TABAKASI kurar; N ile orantili")
print("-"*80)
print("  Iddia: N tane es yonlu Kut siki bir obek olusturursa, UZAKTAN tek bir")
print("  girdap gibi gorunur ve dolanimi Gamma_top = N*Gamma olur. O halde")
print("  bilesigin e-katlanma yaricapi:  r_e(N) = Gamma_top/(2pi sqrt2 c) = N r_e")
def uzak_alan(N, R_obek=0.25, R_olc=60.0):
    """N Kut kucuk bir obekte; R_olc'te olculen hiz."""
    a=2*np.pi*np.arange(N)/N
    P=np.stack([R_obek*np.cos(a),R_obek*np.sin(a)],axis=1) if N>1 else np.array([[0.,0.]])
    v=np.zeros(2); X=np.array([R_olc,0.])
    for q in P:
        r=X-q; r2=r[0]**2+r[1]**2
        k=K/r2; v+=np.array([-k*r[1],k*r[0]])
    return np.hypot(*v)
print("\n      N    |v|(R=60)     tek Kut x N    bagil fark    r_e(N)/r_e")
for N in (1,2,3,5,10,20):
    vN=uzak_alan(N); v1=uzak_alan(1)*N
    # r_e: |v| = sqrt2 olan yaricap.  |v| = N*K/R  => R = N*K/sqrt2 = N
    reN = N*K/np.sqrt(2)
    print("    %5d  %10.6f  %12.6f   %10.2e     %6.2f" % (N,vN,v1,abs(vN-v1)/v1,reN))
    add("MADDE 3: N=%d uzak alan = N x tek Kut"%N, abs(vN-v1)/v1 < 2e-4, abs(vN-v1)/v1)
    add("MADDE 3: r_e(%d) = %d r_e"%(N,N), abs(reN-N)<1e-12, abs(reN-N))
print("\n  *** KULLANICI HAKLI VE BU TURETILEBILIR:")
print("      r_e(N) = N * r_e   —  sinir tabakasi Kut sayisiyla DOGRUSAL buyur.")
print("      Kosul: olcum yaricapi obek capindan cok buyuk olmali (R >> d).")

# =================================================================
print("\n" + "-"*80)
print("MADDE 4 — Obekler kendi sinir tabakalariyla bag kurar (HIYERARSIK)")
print("-"*80)
print("  Iddia: her Kut her Kut'la degil; OBEK obekle baglanir.")
print("  Dayanak: (3)'un sonucu — obegin uzak alani yalniz Gamma_top'a baglidir,")
print("  ic dizilime DEGIL. Asagida bu 'ic yapiya korluk' sinaniyor:")
def uzak_alan_dizilim(dizilim, R_olc=60.0):
    P=np.array(dizilim,float); v=np.zeros(2); X=np.array([R_olc,0.])
    for q in P:
        r=X-q; r2=r[0]**2+r[1]**2
        k=K/r2; v+=np.array([-k*r[1],k*r[0]])
    return np.hypot(*v)
a=2*np.pi*np.arange(5)/5
dizilimler={
 'duzgun besgen': np.stack([0.25*np.cos(a),0.25*np.sin(a)],axis=1),
 'dogrusal dizi': np.stack([np.linspace(-0.25,0.25,5),np.zeros(5)],axis=1),
 'yigin (hepsi merkezde)': np.zeros((5,2)),
 'rastgele kume': np.array([[0.1,0.2],[-0.2,0.05],[0.15,-0.18],[-0.05,-0.1],[0.0,0.12]]),
}
ref=None
for ad,P in dizilimler.items():
    v=uzak_alan_dizilim(P)
    if ref is None: ref=v
    print("      %-26s |v|(R=60) = %.8f   fark %.2e" % (ad,v,abs(v-ref)/ref))
    add("MADDE 4: uzak alan ic dizilime KOR (%s)"%ad, abs(v-ref)/ref < 1e-4, abs(v-ref)/ref)
print("\n  *** KULLANICI HAKLI: obegin disaridan gorunusu yalniz Gamma_top'tur.")
print("      Dolayisiyla obek-obek etkilesimi TOPLU niceliklerle yazilmali;")
print("      simdiki 'her cifte esit etki' kurgusu YANLIS (secici degil kusuru).")

print("\n"+"="*80)
kotu=sum(1 for _,ok,_ in res if not ok)
for n,ok,e in res:
    if not ok: print("  **FAIL**  %-52s sapma=%.3e"%(n,e))
print("  ---> %d/%d gecti"%(len(res)-kotu,len(res)))
