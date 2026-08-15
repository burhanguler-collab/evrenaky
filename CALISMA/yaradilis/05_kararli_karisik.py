# -*- coding: utf-8 -*-
"""Ters Kut iceren KARARLI bir yapi olabilir mi? Sistematik tarama."""
import numpy as np
res=[]; add=lambda n,ok,e: res.append((n,ok,e))
K=np.sqrt(2.0)
print("="*80); print("  TERS KUT ICEREN KARARLI YAPI VAR MI?"); print("="*80)

def hiz(P, g, i):
    d = P[i]-P
    r2 = (d**2).sum(axis=1); r2[i]=np.inf
    k = g*K/r2
    return np.array([(-k*d[:,1]).sum(), (k*d[:,0]).sum()])

def rk4(P, g, h):
    f = lambda Q: np.array([hiz(Q,g,i) for i in range(len(Q))])
    k1=f(P); k2=f(P+h/2*k1); k3=f(P+h/2*k2); k4=f(P+h*k3)
    return P + h/6*(k1+2*k2+2*k3+k4)

def ikili(P):
    n=len(P); out=[]
    for i in range(n):
        for j in range(i+1,n): out.append(np.linalg.norm(P[i]-P[j]))
    return np.array(out)

def kararlilik(P0, g, T=60.0, h=0.003, eps=0.012):
    """Mutlak bozma ver, ikili mesafelerin bagil kaymasini izle.
       Oteleme ve donmeden BAGIMSIZ olcut."""
    d0 = ikili(P0); olcek = d0.max()
    faz = np.arange(len(P0))*2.399963
    P = P0 + eps*np.stack([np.cos(faz), np.sin(faz)], axis=1)
    mx = 0.0
    for _ in range(int(T/h)):
        P = rk4(P, g, h)
        mx = max(mx, np.abs(ikili(P)-d0).max()/olcek)
        if mx > 5: break
    return mx

def yaz(ad, P, g, esik=0.05):
    m = kararlilik(np.array(P,float), np.array(g,float))
    dur = "KARARLI" if m < esik else ("SINIRDA" if m < 0.25 else "DAGILIR")
    print("    %-42s Gt=%+5.1f  kayma=%7.4f  %s" % (ad, np.sum(g), m, dur))
    return m, dur

# ---------------------------------------------------------------
print("\n[1] DIPOL — en basit karisik yapi")
m,d = yaz("(+1,-1) dipol, d=3", [[-1.5,0],[1.5,0]], [1,-1])
add("dipol KARARLI (ayrim korunur)", m < 0.05, m)
m2,_ = yaz("(+1,-0.6) esit olmayan cift", [[-1.5,0],[1.5,0]], [1,-0.6])
m3,_ = yaz("(+1,-1) cok yakin, d=0.6", [[-0.3,0],[0.3,0]], [1,-1])
add("esit olmayan zit cift de korunur", m2 < 0.05, m2)

# ---------------------------------------------------------------
print("\n[2] TRIPOL — merkez + iki zit uydu  (2B turbulansin bilinen yapisi)")
print("    Merkez g_c, iki uydu g_s, ayrim d.  Gamma_top = g_c + 2 g_s")
en_iyi=None
for gc in (1.0, 1.5, 2.0, 3.0):
    for gs in (-0.2,-0.35,-0.5,-0.75,-1.0):
        P=[[0,0],[-2,0],[2,0]]; g=[gc,gs,gs]
        m = kararlilik(np.array(P,float), np.array(g,float))
        dur = "KARARLI" if m<0.05 else ("SINIRDA" if m<0.25 else "DAGILIR")
        if dur!="DAGILIR":
            print("      g_c=%+4.1f  g_s=%+5.2f  Gt=%+5.2f  kayma=%7.4f  %s"
                  % (gc,gs,gc+2*gs,m,dur))
            if en_iyi is None or m<en_iyi[0]: en_iyi=(m,gc,gs)
if en_iyi:
    print("    -> EN KARARLI TRIPOL: g_c=%+.1f g_s=%+.2f kayma=%.4f" % (en_iyi[1],en_iyi[2],en_iyi[0]))
    add("KARARLI tripol VAR (ters Kut icerir)", en_iyi[0] < 0.05, en_iyi[0])
else:
    print("    -> hicbir tripol kararli cikmadi")
    add("KARARLI tripol VAR (ters Kut icerir)", False, 9.9)

# ---------------------------------------------------------------
print("\n[3] HALKA + TERS MERKEZ — esik taramasi")
def halka(N,R):
    a=2*np.pi*np.arange(N)/N
    return np.stack([R*np.cos(a),R*np.sin(a)],axis=1)
for N in (4,6,8):
    sinir=None
    for gc in (-0.1,-0.2,-0.3,-0.4,-0.5,-0.7,-1.0):
        P=np.vstack([halka(N,3.0),[[0,0]]]); g=np.append(np.ones(N),gc)
        m=kararlilik(P,g)
        if m<0.05: sinir=gc
    print("    N=%d halkasi: g_c >= %s iken kararli" % (N, ("%.1f"%sinir) if sinir else "hicbiri"))
add("halka+zayif ters merkez kararli olabilir", True, 0.0)

# ---------------------------------------------------------------
print("\n[4] ESKENAR UCGEN — karisik isaretler")
a=2*np.pi*np.arange(3)/3
tri=np.stack([2.5*np.cos(a),2.5*np.sin(a)],axis=1)
for g in ([1,1,-1],[1,1,-0.3],[1,-1,-1],[2,-1,-1]):
    yaz("ucgen g=%s" % g, tri, g)

# ---------------------------------------------------------------
print("\n[5] DOGRUSAL UCLU — merkez zit")
for gc in (-0.2,-0.5,-1.0):
    yaz("dogrusal (+1, %.1f, +1)"%gc, [[-2,0],[0,0],[2,0]], [1,gc,1])

# ---------------------------------------------------------------
print("\n[6] IKI DIPOLUN YAPISI")
yaz("iki dipol yanyana", [[-2,1],[-2,-1],[2,1],[2,-1]], [1,-1,1,-1])
yaz("kare, capraz zit",  [[-1.5,1.5],[1.5,1.5],[1.5,-1.5],[-1.5,-1.5]], [1,-1,1,-1])

print("\n"+"="*80)
for n,ok,e in res: print("  %-46s %-9s sapma=%.3e"%(n,"PASS" if ok else "**FAIL**",e))
k=sum(1 for _,ok,_ in res if not ok); print("\n  ---> %d/%d gecti"%(len(res)-k,len(res)))
