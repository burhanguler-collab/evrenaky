# -*- coding: utf-8 -*-
"""
JEODETIK PUSULA SINAVI (v2) — yorunge holonomisi, sinyal-kilitli cerceve
=========================================================================
Model tamamen teori-yerli kurallarla kurulur; kodda SR/GR formulu YOKTUR
(ne metrik, ne 3/2, ne Thomas formulu — onlar yalniz BEKLENTI satirlarinda):

  * Sinyal ORTAMA gore yerel c(x) ile gider (M-1):  c(x) = c0*(1 - 2*mu/|x|)
    (kutle-itim kuyusunun yayilim kanali; ln n_eff = +2mu/r, M-42).
  * Isin denklemi (Fermat):  dx/dt = c k ,  dk/dt = -(I - kk^T) grad c.
  * Yapi: A yorungede (dairesel kilavuz; kutle-itim orbiti), B = A + bag.
    Bagin LAB uzunlugu P-G ezilmesiyle kisalir (11.4.8.1, [T]):
    boyuna bilesen 1/gamma — model girdisi, SR aksiyomu degil.
  * SINYAL KILIDI: her gidis-donusten sonra bag yonu, A'nin ic pusulasina
    (B'den gelen sinyalin varis dogrultusunun tersine) yeniden oturur.
    "Eksen malzeme dogrultusu degildir" (11.7.1) — yon bilgisini sinyal tasir.
  * Olculen: bag yonunun LAB acisindaki sekuler kayma (rad/yorunge).

BEKLENTILER (jeodetik_turetim_calismasi.md):
  (a) mu=0, dairesel tasima:            -2*pi*(gamma-1)          [tur acigi]
  (b) mu>0, ayni v:                     +4*pi*mu/R - 2*pi*(gamma-1)
  (c) Kepler bagi (v^2 = mu*c0^2/R):    +3*pi*mu/R               [de Sitter/GP-B]
  (a0) ezilme KAPALI (tani kosusu):     tur acigi bozulmali — ezilme yuk tasiyor mu?

ONCEKI v1 DERSI (kayit): duzgun gradyanda DUZ tasinan pusula donmez (y-oteleme
simetrisi) — dogru sifir. Fiziksel gozlenen, kapali yorunge HOLONOMISIDIR:
gradyan yonu yorunge boyunca dondugu icin birikim olur.

SINAV 2 (bagimsiz cebir denetimi): turetilmis cetvel-saat-yerelzaman
haritalarinin dairesel hiz yolunda adim adim bilesiminden Wigner artigi;
beklenen tur basina -2*pi*(gamma-1).
"""
import numpy as np

c0 = 1.0

# ------------------------------------------------------------------ ortam
def cval(x, mu):
    return c0 * (1.0 - 2.0*mu/np.linalg.norm(x))

def gradc(x, mu):
    r = np.linalg.norm(x)
    return (2.0*mu*c0/r**3) * x            # grad[-2mu/r] = +2mu x/r^3

# ------------------------------------------------------------------ isin
def ray_rhs(x, k, mu):
    gc = gradc(x, mu)
    return cval(x, mu)*k, -(gc - k*(k @ gc))

def integrate_ray(x0, k0, T, mu, nstep):
    x = x0.copy(); k = k0.copy(); h = T/nstep
    for _ in range(nstep):
        k1x,k1k = ray_rhs(x,k,mu)
        k2x,k2k = ray_rhs(x+0.5*h*k1x, k+0.5*h*k1k, mu)
        k3x,k3k = ray_rhs(x+0.5*h*k2x, k+0.5*h*k2k, mu)
        k4x,k4k = ray_rhs(x+h*k3x, k+h*k3k, mu)
        x = x + h/6*(k1x+2*k2x+2*k3x+k4x)
        k = k + h/6*(k1k+2*k2k+2*k3k+k4k)
        k /= np.linalg.norm(k)
    return x, k

# ------------------------------------------------------------------ yorunge
def make_orbit(R, v):
    w = v/R
    A  = lambda t: R*np.array([np.cos(w*t), np.sin(w*t)])
    vA = lambda t: v*np.array([-np.sin(w*t), np.cos(w*t)])
    return A, vA

def lab_bond(s_hat, vdir, L0, beta2, contract):
    """P-G ezilmesi: bagin lab vektoru. Oz uzunluk L0; boyuna bilesen 1/gamma."""
    if not contract:
        return L0 * s_hat
    g = 1.0/np.sqrt(1.0-beta2)
    par = (s_hat @ vdir) * vdir
    perp = s_hat - par
    d = par/g + perp                      # boyuna kisalmis lab vektoru
    return L0 * d/np.linalg.norm(d) * np.linalg.norm(d)   # = L0*d (oz-normalize etmiyoruz)

def shoot(P0, t0, target_pos, target_vel, mu, Tguess, kguess, nstep):
    """P0'dan t0'da cikip hareketli hedefe varan isin: (k0, T, varis_k)."""
    th = np.arctan2(kguess[1], kguess[0]); T = Tguess
    for it in range(50):
        k0 = np.array([np.cos(th), np.sin(th)])
        xT, kT = integrate_ray(P0, k0, T, mu, nstep)
        tgt = target_pos(t0+T)
        Rres = xT - tgt
        if abs(Rres[0])+abs(Rres[1]) < 1e-13:
            break
        cend = cval(xT, mu)
        # yaklasik analitik Jacobian
        kperp = np.array([-k0[1], k0[0]])
        J = np.column_stack([cend*T*kperp, cend*kT - target_vel(t0+T)])
        d = np.linalg.solve(J, -Rres)
        th += d[0]; T += d[1]
        if T <= 0: T = Tguess
    return np.array([np.cos(th), np.sin(th)]), T, kT

def yorunge_kosusu(mu, R, v, L0, n_orbit=2.0, contract=True, nstep=24):
    A, vA = make_orbit(R, v)
    beta2 = (v/c0)**2
    t = 0.0
    s_hat = np.array([1.0, 0.0])          # baglangic bag yonu (radyal)
    Tleg = L0/c0
    kAB_guess = s_hat.copy(); kBA_guess = -s_hat.copy()
    T1g = Tleg; T2g = Tleg
    times, angles = [], []
    T_orbit = 2*np.pi*R/v
    while t < n_orbit*T_orbit:
        vdir = vA(t)/v
        bond = lab_bond(s_hat, vdir, L0, beta2, contract)
        Bpos = lambda tt, t_ref=t, b=bond: A(tt) + b        # bag, gidis-donus boyunca rijit
        Bvel = lambda tt: vA(tt)
        # A -> B
        k1, T1, kB = shoot(A(t), t, Bpos, Bvel, mu, T1g, kAB_guess, nstep)
        t1 = t + T1
        # B -> A
        Apos = lambda tt: A(tt)
        k2, T2, kA = shoot(A(t)+bond, t1, Apos, vA, mu, T2g, kBA_guess, nstep)
        t = t1 + T2
        comp = -kA                          # A'nin pusulasi: B'nin gorunen yonu
        s_hat = comp/np.linalg.norm(comp)   # sinyal kilidi: bag pusulaya oturur
        kAB_guess, kBA_guess, T1g, T2g = k1, k2, T1, T2
        times.append(t); angles.append(np.arctan2(s_hat[1], s_hat[0]))
    times = np.array(times); angles = np.unwrap(np.array(angles))
    # gecici rejimi at: ilk yarim yorunge disari
    m = times > 0.5*T_orbit
    slope = np.polyfit(times[m], angles[m], 1)[0]
    return slope * T_orbit                  # rad / yorunge

def sinav1():
    print("="*78)
    print("SINAV 1 (v2) — Yorunge holonomisi: bag yonunun sekuler kaymasi [rad/yorunge]")
    print("="*78)
    R, L0 = 1.0, 0.04
    rows = []
    # (a) bos uzay — tur acigi tek basina
    v = 0.03; g = 1/np.sqrt(1-(v/c0)**2)
    pred_a = -2*np.pi*(g-1)
    num_a = yorunge_kosusu(0.0, R, v, L0)
    rows.append(("(a)  mu=0, v=0.03, ezilme ACIK", num_a, pred_a))
    # (a0) tani: ezilme kapali
    num_a0 = yorunge_kosusu(0.0, R, v, L0, contract=False)
    rows.append(("(a0) mu=0, v=0.03, ezilme KAPALI", num_a0, float('nan')))
    # (b) alan acik, ayni v
    mu = 2.0e-4
    pred_b = 4*np.pi*mu/R - 2*np.pi*(g-1)
    num_b = yorunge_kosusu(mu, R, v, L0)
    rows.append(("(b)  mu=2e-4, v=0.03", num_b, pred_b))
    # (c) Kepler bagi: v^2 = mu c0^2 / R  ->  3*pi*mu/R
    vk = np.sqrt(mu/R)*c0; gk = 1/np.sqrt(1-(vk/c0)**2)
    pred_c = 4*np.pi*mu/R - 2*np.pi*(gk-1)   # = 3*pi*mu/R + O(mu^2)
    num_c = yorunge_kosusu(mu, R, vk, L0, n_orbit=2.0)
    rows.append(("(c)  KEPLER: mu=2e-4, v=0.014142", num_c, pred_c))
    print(f"{'kosum':<36}{'olculen':>14}{'beklenen':>14}{'oran':>9}")
    for ad, num, pred in rows:
        oran = num/pred if pred==pred and pred!=0 else float('nan')
        print(f"{ad:<36}{num:>14.6e}{pred:>14.6e}{oran:>9.4f}")
    print(f"\n  Kontrol: 3*pi*mu/R = {3*np.pi*2e-4:.6e}  (de Sitter/GP-B katsayisi 3/2'nin yorunge bicimi)")
    print()

# ------------------------------------------------------------------ SINAV 2
def harita(v):
    """Turetilmis kinematik harita (P-G ezilme + saat + yerel-zaman), (t,x,y)."""
    vx, vy = v; b2 = (vx*vx+vy*vy)/c0**2
    if b2 < 1e-30: return np.eye(3)
    g = 1.0/np.sqrt(1.0-b2)
    n = np.array([vx, vy])/np.sqrt(vx*vx+vy*vy)
    M = np.eye(3)
    M[0,0] = g; M[0,1:] = -g*np.array([vx,vy])/c0**2
    M[1:,0] = -g*np.array([vx,vy]); M[1:,1:] = np.eye(2) + (g-1.0)*np.outer(n,n)
    return M

def sinav2(u, N=20000):
    top = 0.0
    for i in range(N):
        f0 = 2*np.pi*i/N; f1 = 2*np.pi*(i+1)/N
        C = harita(u*np.array([np.cos(f1), np.sin(f1)])) @ \
            np.linalg.inv(harita(u*np.array([np.cos(f0), np.sin(f0)])))
        Rs = C[1:,1:]
        top += 0.5*(Rs[1,0]-Rs[0,1])       # adimin Wigner (donme) artigi
    g = 1/np.sqrt(1-u*u)
    print(f"  u/c0={u}:  net Wigner = {top:+.6e} rad/tur ; -2*pi*(gamma-1) = {-2*np.pi*(g-1):+.6e} ; oran = {top/(-2*np.pi*(g-1)):.5f}")

if __name__ == "__main__":
    sinav1()
    print("="*78)
    print("SINAV 2 — Turetilmis haritalarin bilesimi: adim basina Wigner artigi toplami")
    print("="*78)
    sinav2(0.3); sinav2(0.05); sinav2(0.03)
