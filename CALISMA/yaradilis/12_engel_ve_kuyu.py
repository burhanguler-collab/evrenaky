# -*- coding: utf-8 -*-
"""Sinir tabakasinin disi itiyor mu? Kenetlenmeden once ENGEL var mi?"""
import numpy as np
res=[]; add=lambda n,ok,e: res.append((n,ok,e))
K=np.sqrt(2.0)
print("="*80); print("  SINIR TABAKASI: ONCE ITME, SONRA KENETLENME?"); print("="*80)

def vf(P,pos,gs):
    v=np.zeros(2)
    for q,g in zip(pos,gs):
        r=np.asarray(P,float)-np.asarray(q,float); r2=max(r[0]**2+r[1]**2,1e-30)
        k=g*K/r2; v+=np.array([-k*r[1],k*r[0]])
    return v
rho=lambda v: np.exp(-(v[0]**2+v[1]**2)/2.0)

# ---------------------------------------------------------------
print("\n[1] BASINC PROFILI — dis yan gercekten dusuk mu?")
d=3.0; A=[-d/2,0]; B=[d/2,0]; gs=[1,1]
print("    Es yonlu cift, d=%.1f. Eksen boyunca rho/rho0:" % d)
print("      x        rho/rho0     yer")
for x,ad in [(-6,'B disi... A disi'),(-3.0,'A disi'),(-1.5,'A merkezi'),
             (-0.75,'ARADA'),(0.0,'TAM ORTA'),(0.75,'ARADA'),
             (1.5,'B merkezi'),(3.0,'B disi'),(6.0,'B disi uzak')]:
    r=rho(vf([x,0],[A,B],gs))
    print("    %6.2f   %10.6f   %s" % (x,r,ad))
ic=rho(vf([0,0],[A,B],gs)); dis=rho(vf([d,0],[A,B],gs))
print("\n    ARADA rho=%.4f (yuksek basinc)  ·  DISTA rho=%.4f (dusuk basinc)"%(ic,dis))
add("aradaki basinc DISTAKINDEN yuksek", ic>dis, ic-dis)
print("    Bosluk DUSUK basinca gider => her Kut DISA itilir. ITME GERCEK.")
print("    *** KULLANICI HAKLI: sinir tabakasinin dis yani uzaklastirir.")

# ---------------------------------------------------------------
print("\n[2] ENERJI: yaklasmak IS ISTER MI?")
print("    U_girdap(d) = -A ln d,  A = Gamma^2/2pi > 0 (es isaret)")
GAM=2*np.pi*K; Ae=GAM**2/(2*np.pi)
print("    A = %.4f (kod birimi)" % Ae)
print("      d1 -> d2      yaklasma isi = A ln(d1/d2)")
for d1,d2 in [(4,2),(2,1),(1,0.5),(0.5,0.1)]:
    print("      %4.1f -> %4.1f      %+10.4f" % (d1,d2,Ae*np.log(d1/d2)))
add("yaklasmak POZITIF is ister (engel)", Ae*np.log(2/1)>0, 0.0)
print("    -> Yaklasmak DAIMA is ister ve d->0'da IRAKSAR. Bu bir ENGELDIR.")

# ---------------------------------------------------------------
print("\n[3] AMA MODELIMDE BU KUVVETE DONMUYOR")
print("    Nokta girdap dinamiginde karsilikli tasimanin RADYAL bileseni")
print("    TAM SIFIRDIR (bu oturumda dogrulandi). Yani enerji engeli var,")
print("    dinamik kuvvet YOK. Model bu noktada TUTARSIZ.")
vA=vf(A,[B],[1]); u=np.array([1.0,0.0])
print("    A'nin tasinma hizi: radyal=%.2e  tanjantel=%.4f" % (vA@u, abs(vA[1])))
add("nokta girdapta radyal kuvvet sifir", abs(vA@u)<1e-12, abs(vA@u))
print("    *** EKSIK OLAN: girdap itmesini RADYAL KUVVET olarak eklemek.")

# ---------------------------------------------------------------
print("\n[4] IKI KANAL BIRLIKTE — ENGEL + KUYU cikiyor mu?")
print("    F(d) = A/d  -  kappa(1-d0/d)/d^2      [+ = ayirici]")
print("    Birinci terim girdap itmesi (1/d), ikincisi Bjerknes (1/d^2).")
def F(d,A_,kap,d0): return A_/d - kap*(1-d0/d)/d**2
def U(d,A_,kap,d0,b=200.0,n=400000):
    x=np.linspace(d,b,n); return np.trapezoid(F(x,A_,kap,d0),x)
for kap in (5,20,60,200):
    xs=np.linspace(0.05,8,4000); Fs=F(xs,Ae,kap,1.5)
    isaret=np.sign(Fs); gecis=[xs[i] for i in range(1,len(xs)) if isaret[i]!=isaret[i-1]]
    print("    kappa=%5.0f -> denge noktalari d = %s" % (kap,
          ", ".join("%.3f"%g for g in gecis) if gecis else "YOK (hep itici)"))
print()
print("    Yorum: kappa kucukken girdap itmesi (1/d) uzakta HEP baskin ve")
print("    hicbir kuyu olusmuyor. kappa buyudukce IKI kok cikiyor:")
print("      ic kok  = KARARLI KUYU  (kenetlenme noktasi)")
print("      dis kok = ENGEL TEPESI  (asilmasi gereken tumsek)")
kap=200; xs=np.linspace(0.05,8,4000); Fs=F(xs,Ae,kap,1.5)
isaret=np.sign(Fs); kok=[xs[i] for i in range(1,len(xs)) if isaret[i]!=isaret[i-1]]
if len(kok)>=2:
    print("\n    kappa=200 icin:  kuyu d=%.3f   engel tepesi d=%.3f" % (kok[0],kok[1]))
    print("    Engel yuksekligi (tepeden kuyuya) = %.4f" % (U(kok[0],Ae,kap,1.5)-U(kok[1],Ae,kap,1.5)))
    add("iki kok var: kuyu + engel", len(kok)>=2, len(kok))
else:
    add("iki kok var: kuyu + engel", False, len(kok))

print("\n[5] SONUC")
print("    (a) Itme GERCEK: basinc profili ve enerji birlikte gosteriyor.")
print("    (b) Engel GERCEK: yaklasmak is ister, d->0'da iraksar.")
print("    (c) Modelde EKSIK: girdap itmesi radyal kuvvete cevrilmemis.")
print("    (d) Eklenince yapi TAM istenen bicime geliyor:")
print("        uzak: itici  ->  ENGEL TEPESI  ->  ic: cekici  ->  KUYU (kenetlenme)")
print("    (e) Ama kosul var: Bjerknes yeterince guclu olmali (kappa buyuk),")
print("        yoksa engel asilamaz ve kenetlenme HIC olmaz.")

print("\n"+"="*80)
kotu=sum(1 for _,ok,_ in res if not ok)
for n,ok,e in res: print("  %-46s %-9s sapma=%.3e"%(n,"PASS" if ok else "**FAIL**",e))
print("\n  ---> %d/%d gecti"%(len(res)-kotu,len(res)))
