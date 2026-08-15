# -*- coding: utf-8 -*-
"""Tripol gercekten kararli mi? Sert sinama + dogrusal kararlilik."""
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

print("="*78); print("  TRIPOL — SERT SINAMA"); print("="*78)

# ---------------------------------------------------------------
# 1. ONCE: bagil denge mi? (analitik kontrol)
# ---------------------------------------------------------------
print("\n[1] Simetrik dogrusal ucluye analitik bakis")
print("    P = [(0,0), (-d,0), (+d,0)],  g = [gc, gs, gs]")
print("    Merkez hizi = 0 (simetri).  Uydu hizi = (0, K(2gc+gs)/(2d)) — TANJANTEL.")
print("    => HER gc, gs icin BAGIL DENGE (kati donus, w = K(2gc+gs)/(2d^2)).")
d=2.0
for gc,gs in [(1,-0.5),(2,-1),(3,-0.2)]:
    P=np.array([[0,0],[-d,0],[d,0]],float); g=np.array([gc,gs,gs],float)
    v0=hiz(P,g,0); v2=hiz(P,g,2)
    w_an=K*(2*gc+gs)/(2*d*d)
    print("      gc=%+.1f gs=%+.1f: |v_merkez|=%.2e  v_uydu=(%.3f,%.3f)  w_say=%.4f w_an=%.4f"
          % (gc,gs,np.linalg.norm(v0),v2[0],v2[1],v2[1]/d,w_an))
    add("gc=%+.1f gs=%+.1f: merkez sabit"%(gc,gs), np.linalg.norm(v0)<1e-12, np.linalg.norm(v0))
    add("gc=%+.1f gs=%+.1f: w = K(2gc+gs)/2d^2"%(gc,gs), abs(v2[1]/d-w_an)<1e-12, abs(v2[1]/d-w_an))

# ---------------------------------------------------------------
# 2. DOGRUSAL KARARLILIK — Jacobian ozdegerleri (donen cercevede)
# ---------------------------------------------------------------
print("\n[2] DOGRUSAL KARARLILIK — donen cercevede Jacobian ozdegerleri")
def maxRe(gc,gs,d=2.0,eps=1e-6):
    P0=np.array([[0,0],[-d,0],[d,0]],float).ravel()
    g=np.array([gc,gs,gs],float)
    Om=K*(2*gc+gs)/(2*d*d)
    def F(q):
        Q=q.reshape(3,2); out=np.zeros_like(Q)
        for i in range(3):
            out[i]=hiz(Q,g,i)-Om*np.array([-Q[i,1],Q[i,0]])
        return out.ravel()
    J=np.zeros((6,6))
    for k in range(6):
        e=np.zeros(6); e[k]=eps
        J[:,k]=(F(P0+e)-F(P0-e))/(2*eps)
    return np.linalg.eigvals(J).real.max()

print("      gc     gs     Gt      maks Re(lambda)   durum")
kararli=[]; kararsiz=[]
for gc in (1.0,2.0,3.0):
    for gs in (-0.1,-0.2,-0.35,-0.5,-0.75,-1.0,-1.5,-2.0):
        m=maxRe(gc,gs)
        dur="KARARLI" if m<1e-6 else "KARARSIZ"
        (kararli if m<1e-6 else kararsiz).append((gc,gs,gc+2*gs))
        print("     %+5.1f  %+5.2f  %+5.2f   %+.4e     %s"%(gc,gs,gc+2*gs,m,dur))
print("\n    kararli sayisi: %d / %d" % (len(kararli), len(kararli)+len(kararsiz)))
add("dogrusal kararlilik AYRISIYOR (hepsi ayni degil)",
    len(kararli)>0 and len(kararsiz)>0, len(kararsiz))

# ---------------------------------------------------------------
# 3. UZUN KOSUM + BUYUK BOZMA
# ---------------------------------------------------------------
print("\n[3] UZUN KOSUM (T=400) + BUYUK BOZMA (eps=0.10)")
def uzun(gc,gs,d=2.0,T=400.0,h=0.002,eps=0.10):
    P0=np.array([[0,0],[-d,0],[d,0]],float); g=np.array([gc,gs,gs],float)
    d0=ikili(P0); olcek=d0.max()
    faz=np.arange(3)*2.399963
    P=P0+eps*np.stack([np.cos(faz),np.sin(faz)],axis=1)
    mx=0.0
    for _ in range(int(T/h)):
        P=rk4(P,g,h); mx=max(mx,np.abs(ikili(P)-d0).max()/olcek)
        if mx>5: break
    return mx
print("      gc     gs     Gt     kayma(T=400)   durum")
for gc,gs in [(1,-0.1),(1,-0.5),(2,-1.0),(3,-0.2),(1,-1.5),(1,-2.0),(2,-2.0)]:
    m=uzun(gc,gs)
    dur="KARARLI" if m<0.12 else ("SINIRDA" if m<0.5 else "DAGILIR")
    print("     %+5.1f  %+5.2f  %+5.2f   %8.4f      %s"%(gc,gs,gc+2*gs,m,dur))

# ---------------------------------------------------------------
# 4. KLASIK TRIPOL: Gamma_top = 0
# ---------------------------------------------------------------
print("\n[4] KLASIK TRIPOL  gc=+2, gs=-1  (Gamma_top = 0)")
m_lin=maxRe(2.0,-1.0); m_uz=uzun(2.0,-1.0)
print("      dogrusal maks Re(lambda) = %+.4e" % m_lin)
print("      uzun kosum kaymasi        = %.4f" % m_uz)
print("      -> %s" % ("KARARLI" if (m_lin<1e-6 and m_uz<0.12) else "KARARSIZ"))
add("klasik tripol (gc=2,gs=-1) kararli", m_lin<1e-6 and m_uz<0.12, max(m_lin,m_uz))

# ---------------------------------------------------------------
# 5. DIPOL uzun kosum
# ---------------------------------------------------------------
print("\n[5] DIPOL uzun kosum (T=400, eps=0.10)")
P0=np.array([[-1.5,0],[1.5,0]],float); g=np.array([1,-1],float)
d0=ikili(P0); P=P0+0.10*np.stack([np.cos(np.arange(2)*2.4),np.sin(np.arange(2)*2.4)],axis=1)
mx=0
for _ in range(200000):
    P=rk4(P,g,0.002); mx=max(mx,abs(ikili(P)[0]-d0[0])/d0[0])
print("      ayrim bagil kaymasi = %.5f  -> %s" % (mx, "KARARLI" if mx<0.12 else "DAGILIR"))
add("dipol uzun kosumda da kararli", mx<0.12, mx)

print("\n"+"="*78)
for n,ok,e in res: print("  %-44s %-9s sapma=%.3e"%(n,"PASS" if ok else "**FAIL**",e))
k=sum(1 for _,ok,_ in res if not ok); print("\n  ---> %d/%d gecti"%(len(res)-k,len(res)))
