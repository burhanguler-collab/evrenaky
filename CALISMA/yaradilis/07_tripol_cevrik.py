# -*- coding: utf-8 -*-
"""Isaret-cevrik tripol: merkez NEGATIF, uydular POZITIF. 8.3 gedigine aday."""
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
def ikili(P):
    n=len(P);o=[]
    for i in range(n):
        for j in range(i+1,n): o.append(np.linalg.norm(P[i]-P[j]))
    return np.array(o)
def maxRe(gc,gs,d=2.0,eps=1e-6):
    P0=np.array([[0,0],[-d,0],[d,0]],float).ravel(); g=np.array([gc,gs,gs],float)
    Om=K*(2*gc+gs)/(2*d*d)
    def F(q):
        Q=q.reshape(3,2); out=np.zeros_like(Q)
        for i in range(3): out[i]=hiz(Q,g,i)-Om*np.array([-Q[i,1],Q[i,0]])
        return out.ravel()
    J=np.zeros((6,6))
    for k in range(6):
        e=np.zeros(6); e[k]=eps
        J[:,k]=(F(P0+e)-F(P0-e))/(2*eps)
    return np.linalg.eigvals(J).real.max()
def uzun(gc,gs,d=2.0,T=400.0,h=0.002,eps=0.10):
    P0=np.array([[0,0],[-d,0],[d,0]],float); g=np.array([gc,gs,gs],float)
    d0=ikili(P0); olcek=d0.max(); faz=np.arange(3)*2.399963
    P=P0+eps*np.stack([np.cos(faz),np.sin(faz)],axis=1); mx=0.0
    for _ in range(int(T/h)):
        P=rk4(P,g,h); mx=max(mx,np.abs(ikili(P)-d0).max()/olcek)
        if mx>5: break
    return mx

print("="*74)
print("  ISARET-CEVRIK TRIPOL — merkez NEGATIF, uydular POZITIF")
print("="*74)
print("  8.3 gedigi: az sayida BUYUK negatif + cok sayida kucuk pozitif,")
print("  toplam dolanim SIFIR. Boyle bir yapi KARARLI olabilir mi?")
print()
print("    gc     gs    N+:N-   Gt      maks Re(l)      uzun     durum")
for gc,gs in [(-2,1),(-1,0.5),(-3,1.5),(-4,2),(-1,1),(-2,2),(-0.4,1)]:
    m=maxRe(gc,gs); u=uzun(gc,gs)
    npos=sum(1 for x in [gc,gs,gs] if x>0); nneg=3-npos
    dur="KARARLI" if (m<1e-6 and u<0.12) else "KARARSIZ"
    print("  %+5.1f  %+5.2f   %d:%d   %+5.2f   %+.3e   %7.4f   %s"
          % (gc,gs,npos,nneg,gc+2*gs,m,u,dur))
    if (gc,gs)==(-2,1):
        add("cevrik klasik tripol (gc=-2,gs=+1) KARARLI", m<1e-6 and u<0.12, max(m,u))
        add("  ve Gamma_top = 0", abs(gc+2*gs)<1e-12, abs(gc+2*gs))
        add("  ve N+ > N- (2:1 sayi asimetrisi)", npos>nneg, 0.0)

# isaret cevirme kararliligi korur mu? (Hamilton sistemi, zaman tersinmesi)
print("\n  ISARET CEVIRME SINAMASI: (g) ile (-g) ayni kararliligi vermeli")
e=0.0
for gc,gs in [(2,-1),(1,-0.5),(3,-1.5),(1,-2)]:
    a=maxRe(gc,gs); b=maxRe(-gc,-gs)
    print("    (%+.1f,%+.2f): %+.3e   (%+.1f,%+.2f): %+.3e   fark %.2e"
          % (gc,gs,a,-gc,-gs,b,abs(a-b)))
    e=max(e,abs(a-b))
add("isaret cevirme kararliligi korur", e<1e-9, e)

# daha buyuk N: merkez -N, cevrede N tane +1
print("\n  BUYUK SAYI: merkez g=-N, cevrede N tane +1 (halka)")
def halka_merkez(N,gc,R=3.0,T=200.0,h=0.003,eps=0.05):
    a=2*np.pi*np.arange(N)/N
    P0=np.vstack([np.stack([R*np.cos(a),R*np.sin(a)],axis=1),[[0,0]]])
    g=np.append(np.ones(N),gc)
    d0=ikili(P0); olcek=d0.max(); faz=np.arange(N+1)*2.399963
    P=P0+eps*np.stack([np.cos(faz),np.sin(faz)],axis=1); mx=0.0
    for _ in range(int(T/h)):
        P=rk4(P,g,h); mx=max(mx,np.abs(ikili(P)-d0).max()/olcek)
        if mx>3: break
    return mx
print("      N   gc     Gt    kayma    durum")
for N in (2,3,4,6):
    m=halka_merkez(N,-float(N))
    print("     %2d  %+5.1f  %+5.1f  %7.4f  %s" % (N,-N,0.0,m,"KARARLI" if m<0.12 else "DAGILIR"))

print("\n"+"="*74)
for n,ok,e in res: print("  %-44s %-9s sapma=%.3e"%(n,"PASS" if ok else "**FAIL**",e))
k=sum(1 for _,ok,_ in res if not ok); print("\n  ---> %d/%d gecti"%(len(res)-k,len(res)))
