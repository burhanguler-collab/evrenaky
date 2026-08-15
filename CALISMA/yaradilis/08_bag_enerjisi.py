# -*- coding: utf-8 -*-
"""Bagi cozmek enerji ister mi? Uzaktaki Kut cifti ayirabilir mi?"""
import numpy as np
res=[]; add=lambda n,ok,e: res.append((n,ok,e))
K=np.sqrt(2.0); GAM=2*np.pi*K
print("="*78); print("  BAG ENERJISI VAR MI?"); print("="*78)

def hiz(P,g,i):
    d=P[i]-P; r2=(d**2).sum(axis=1); r2[i]=np.inf
    k=g*K/r2
    return np.array([(-k*d[:,1]).sum(),(k*d[:,0]).sum()])
def rk4(P,g,h):
    f=lambda Q: np.array([hiz(Q,g,i) for i in range(len(Q))])
    k1=f(P);k2=f(P+h/2*k1);k3=f(P+h/2*k2);k4=f(P+h*k3)
    return P+h/6*(k1+2*k2+2*k3+k4)
def H(P,g):
    h=0.0
    for i in range(len(P)):
        for j in range(i+1,len(P)):
            h -= g[i]*g[j]*np.log(np.linalg.norm(P[i]-P[j]))
    return h

# ---------------------------------------------------------------
print("\n[1] ETKILESIM ENERJISI — cifti AYIRMAK enerji ister mi?")
print("    Nokta girdap etkilesim enerjisi:  E_int = -(G1*G2/2pi) ln r")
print("    ES isaretli (G1G2>0): r BUYUDUKCE E DUSER  ->  AYRILMAK BEDAVA,")
print("                          hatta enerjiyi DUSURUR (itici etkilesim).")
print("    ZIT isaretli (G1G2<0): r buyudukce E ARTAR ->  ayirmak enerji ISTER.")
print()
print("      r      E_es(+,+)     E_zit(+,-)")
for r in (0.5,1,2,4,8,16):
    print("    %5.1f   %+10.4f   %+10.4f" % (r, -np.log(r), +np.log(r)))
add("es isaretli: ayrilmak enerjiyi DUSURUR", (-np.log(8)) < (-np.log(1)), 0.0)
add("zit isaretli: ayrilmak enerji ISTER",   (+np.log(8)) > (+np.log(1)), 0.0)
print("\n    *** SONUC: ES ISARETLI KUTLARDA BAGLANMA ENERJISI YOKTUR.")
print("        Aksine iticidirler. Bir arada durmalarinin sebebi bir kuyu degil,")
print("        ACISAL IMPULSUN KORUNUMUDUR (yorunge, cukur degil).")

# ---------------------------------------------------------------
print("\n[2] BASINC TABLOSU AYNI SEYI SOYLUYOR MU?")
print("    Es isaretli ciftte: ARADA hizlar goturur -> yuksek basinc (SIRT)")
print("                        DISTA hizlar toplanir -> dusuk basinc")
d=3.0; A=np.array([-d/2,0.]); B=np.array([d/2,0.])
def vfield(P,pos,gs):
    v=np.zeros(2)
    for q,g in zip(pos,gs):
        r=np.asarray(P,float)-q; r2=max(r[0]**2+r[1]**2,1e-30)
        k=g*K/r2; v+=np.array([-k*r[1],k*r[0]])
    return v
ic  = np.hypot(*vfield([0,0],[A,B],[1,1]))          # arada
dis = np.hypot(*vfield([d,0],[A,B],[1,1]))          # disarida (B'nin disi)
tek = np.hypot(*vfield([d,0],[B],[1]))              # yalniz B olsaydi
print("      arada  |v| = %.4f  -> rho/rho0 = %.4f" % (ic, np.exp(-ic**2/2)))
print("      B'nin disinda |v| = %.4f (tek basina %.4f) -> rho/rho0 = %.4f"
      % (dis, tek, np.exp(-dis**2/2)))
add("arada basinc YUKSEK (sirt)", np.exp(-ic**2/2) > np.exp(-dis**2/2), 0.0)
print("    -> Her Kut'un IC yani yuksek, DIS yani dusuk basincta.")
print("       Bosluk dusuk basinca gider => KUTLAR BIRBIRINDEN ITILIR.")
print("       Enerji argumaniyla BIREBIR uyusuyor.")

# ---------------------------------------------------------------
print("\n[3] UZAKTAKI UCUNCU KUT CIFTI NE KADAR BOZAR?")
print("    Cift d=1.5'te, ucuncu Kut D uzakligina konuyor. 300 zaman birimi.")
print("      D      maks |dd|/d      bag (cap=3) kopar mi?")
def dene(D, d0=1.5, T=300.0, h=0.004):
    P=np.array([[-d0/2,0],[d0/2,0],[D,0]],float); g=np.array([1.,1.,1.])
    mx=0.0
    for _ in range(int(T/h)):
        P=rk4(P,g,h)
        dd=np.linalg.norm(P[1]-P[0])
        mx=max(mx,abs(dd-d0)/d0)
    return mx
for D in (4,6,10,20,40,80):
    m=dene(D)
    print("    %5d    %10.5f      %s" % (D, m, "EVET" if 1.5*(1+m)>3 else "hayir"))
add("uzak Kut'un etkisi mesafeyle DUSER", dene(80) < dene(6), dene(80))

# ---------------------------------------------------------------
print("\n[4] YAKIN UCUNCU KUT: bag GERCEKTEN kopuyor mu?")
print("    Cift d=1.5, ucuncu Kut D=3'te (yakalama yaricapi icinde).")
P=np.array([[-0.75,0],[0.75,0],[3.0,0]],float); g=np.array([1.,1.,1.])
d0=1.5; mx=0; mn=9e9; H0=H(P,g)
for _ in range(int(300/0.004)):
    P=rk4(P,g,0.004)
    dd=np.linalg.norm(P[1]-P[0]); mx=max(mx,dd); mn=min(mn,dd)
print("      ayrim araligi: %.4f … %.4f  (baslangic %.2f)" % (mn,mx,d0))
print("      H korunumu: %.2e" % (abs(H(P,g)-H0)/abs(H0)))
print("      cap=3 esigi asiliyor mu? %s" % ("EVET — 'bag' etiketi kopar" if mx>3 else "hayir"))
add("H korunuyor (dinamik saglikli)", abs(H(P,g)-H0)/abs(H0) < 1e-8, abs(H(P,g)-H0)/abs(H0))

# ---------------------------------------------------------------
print("\n[5] PEKI 'BAG' NE? — modelin kendi tanimina bakalim")
print("    Simulasyondaki bag olcutu:  sqrt(dx^2+dy^2+dw^2) <= cap")
print("    Bu bir MESAFE ETIKETIDIR; ne kuvvet ne enerji icerir.")
print("    Es isaretli Kutlarda radyal kuvvet SIFIR (bu oturumda dogrulandi),")
print("    etkilesim enerjisi ITICI. Yani ortada koparilacak bir bag YOK.")
print("    => Kullanicinin bekledigi 'ekstra etki' bu modelde OLMAMASI dogru;")
print("       ama o zaman 'bag' KELIMESI yaniltici.")

# ---------------------------------------------------------------
print("\n[6] ZIT CIFTTE DURUM FARKLI — orada GERCEK bag var")
print("    E_int = +ln r  ->  ayirmak enerji ISTER. Baglanma enerjisi:")
for d0,d1 in [(1,3),(1,10),(0.5,5)]:
    print("      d: %.1f -> %.1f  icin gereken is = %+.4f (Gamma^2/2pi biriminde)"
          % (d0,d1, np.log(d1)-np.log(d0)))
add("zit ciftte ayirma isi POZITIF", (np.log(10)-np.log(1))>0, 0.0)
print("    -> Teorinin ihtiyaci olan BAGLI yapiyi zit cift saglar, es cift DEGIL.")
print("       Ama teori zit yonu yasakliyor. Bu bir GERILIM ve kayda gecmeli.")

print("\n"+"="*78)
for n,ok,e in res: print("  %-46s %-9s sapma=%.3e"%(n,"PASS" if ok else "**FAIL**",e))
k=sum(1 for _,ok,_ in res if not ok); print("\n  ---> %d/%d gecti"%(len(res)-k,len(res)))
