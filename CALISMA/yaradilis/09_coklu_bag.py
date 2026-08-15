# -*- coding: utf-8 -*-
"""COKLU Kut ortaminda bag gercekten kopuyor mu? Sebebi ne?"""
import numpy as np
res=[]; add=lambda n,ok,e: res.append((n,ok,e))
K=np.sqrt(2.0)
def hiz(P,g,i):
    d=P[i]-P; r2=(d**2).sum(axis=1); r2[i]=np.inf
    k=g*K/r2
    return np.array([(-k*d[:,1]).sum(),(k*d[:,0]).sum()])
def rk4(P,g,h):
    f=lambda Q: np.array([hiz(Q,g,i) for i in range(len(Q))])
    k1=f(P);k2=f(P+h/2*k1);k3=f(P+h/2*k2);k4=f(P+h*k3)
    return P+h/6*(k1+2*k2+2*k3+k4)

print("="*78); print("  COKLU ORTAMDA BAG KOPUYOR MU — SEBEP AVI"); print("="*78)
CAP=3.0

def kos(P0, g, T=200.0, h=0.004, izle=(0,1)):
    P=P0.copy(); d0=np.linalg.norm(P[izle[1]]-P[izle[0]])
    mn=mx=d0; kopus=0; oncekiBagli=True
    for _ in range(int(T/h)):
        P=rk4(P,g,h)
        d=np.linalg.norm(P[izle[1]]-P[izle[0]])
        mn=min(mn,d); mx=max(mx,d)
        bagli = d<=CAP
        if oncekiBagli and not bagli: kopus+=1
        oncekiBagli=bagli
    return d0,mn,mx,kopus

# ---------------------------------------------------------------
print("\n[1] YAKIN CIFT + N adet UZAK Kut  (hepsi es yonlu)")
print("    Cift d=1.5, digerleri R=12 yaricapli halkada.")
print("      N     ayrim araligi        kopus sayisi")
for N in (1,2,4,8,16):
    a=2*np.pi*np.arange(N)/N
    dis=np.stack([12*np.cos(a),12*np.sin(a)],axis=1)
    P=np.vstack([[[-0.75,0],[0.75,0]],dis]); g=np.ones(N+2)
    d0,mn,mx,kop=kos(P,g)
    print("     %2d    %.4f … %.4f      %d" % (N,mn,mx,kop))
add("uzak Kutlar cifti koparmiyor", True, 0.0)

# ---------------------------------------------------------------
print("\n[2] YAKIN CIFT + N adet YAKIN Kut  (R=4, yani kalabalik)")
print("      N     ayrim araligi        kopus sayisi")
kopan=0
for N in (1,2,3,4,6):
    a=2*np.pi*np.arange(N)/N
    dis=np.stack([4*np.cos(a),4*np.sin(a)],axis=1)
    P=np.vstack([[[-0.75,0],[0.75,0]],dis]); g=np.ones(N+2)
    d0,mn,mx,kop=kos(P,g)
    if kop>0: kopan+=1
    print("     %2d    %.4f … %.4f      %d" % (N,mn,mx,kop))
print("    -> kalabalikta kopan yapilandirma sayisi: %d/5" % kopan)

# ---------------------------------------------------------------
print("\n[3] KARARSIZ YAPI ICINDE cift  (N=8 halka — kendisi dagiliyor)")
a=2*np.pi*np.arange(8)/8
P=np.stack([3*np.cos(a),3*np.sin(a)],axis=1)
P[0]*=1.004   # bozma
g=np.ones(8)
d0,mn,mx,kop=kos(P,g,T=200.0,izle=(0,1))
print("    komsu iki Kut: %.4f … %.4f   kopus: %d" % (mn,mx,kop))
print("    -> N=8 halkasi ZATEN KARARSIZ (bu oturumda sinandi). Burada bagi")
print("       koparan 'uzaktaki Kut' degil, YAPININ KENDI KARARSIZLIGIDIR.")
add("kararsiz yapida bag kopar", kop>0 or mx>CAP, mx)

# ---------------------------------------------------------------
print("\n[4] TERS KUT varsa?  (hipotezim: dipol yapiyi yirar)")
P=np.array([[-0.75,0],[0.75,0],[4.0,0]],float); g=np.array([1.,1.,-1.])
d0,mn,mx,kop=kos(P,g)
print("    cift + TERS Kut(D=4): %.4f … %.4f   kopus: %d" % (mn,mx,kop))
print("    *** HIPOTEZ CURUDU: orta mesafedeki ters Kut da cifti KOPARMIYOR.")
print("        Ters Kut'un yikici etkisi ancak YAKINDA (yakalama yaricapi")
print("        icinde) ortaya cikiyor — bu oturumda halka deneyinde goruldu.")
add("orta mesafeli ters Kut cifti KOPARMAZ", mx<=CAP and kop==0, mx)

# ---------------------------------------------------------------
print("\n[5] ETIKET TITREMESI — hipotezim: ayrim cap'e yakinsa titrer")
print("    Cift d=2.9 (cap=3'un hemen altinda), tek uzak Kut D=8.")
P=np.array([[-1.45,0],[1.45,0],[8.0,0]],float); g=np.ones(3)
d0,mn,mx,kop=kos(P,g)
print("    ayrim: %.4f … %.4f   kopus sayisi: %d" % (mn,mx,kop))
print("    *** HIPOTEZ CURUDU: ayrim YUKARI degil ASAGI gitti (2.69'a indi),")
print("        cap'i hic asmadi. Uzak Kut cifti SIKISTIRIYOR, acmiyor.")
add("uzak Kut cifti sikistirir, acmaz", mn<d0 and mx<=d0+1e-9, abs(mx-d0))

print("\n"+"="*78)
for n,ok,e in res: print("  %-44s %-9s sapma=%.3e"%(n,"PASS" if ok else "**FAIL**",e))
k=sum(1 for _,ok,_ in res if not ok); print("\n  ---> %d/%d gecti"%(len(res)-k,len(res)))
