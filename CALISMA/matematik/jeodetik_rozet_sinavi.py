# -*- coding: utf-8 -*-
"""
JEODETIK ROZET SINAVI (v3) — cift zit-dolasan sinyal paketi, torksuz merkez bagi
==================================================================================
Kucuk-dongu lemmasinin mikro-mekanik sinamasi. Onceki iki tasarimin dersleri:
  v1: duzgun gradyanda duz tasima -> simetri geregi sifir (dogru sifir; gozlenen
      buyukluk KAPALI YORUNGE HOLONOMISIDIR).
  v2: bagi her sekmede pusulaya kilitlemek yon HAFIZASINI siler; bag v'ye
      kilitlenip yorungeyle birlikte doner (tam 2pi/yorunge olctuk) — jiroskop
      modeli koleles(tir)ilemez.
v3 tasarimi: yon hafizasini SINYALIN KENDISI tasir —
  * Iki paket, ayni ic yaricapta ZIT yonlerde dolasir (sinyal hizi = yerel c).
  * Baglama: merkeze (C) yonelik MERKEZI ivme alani (+hafif radyal sonum).
    Merkezi kuvvet C etrafinda TORK uygulayamaz -> yonelim hafizasi serbest.
  * Rozet isaretcisi: m = (phi1 + phi2)/2 — zit dolasimda faz toplami sabit
    kalir; m'nin sekuler kaymasi = tasinan yon hafizasinin donmesi.
  * Kodda SR/GR formulu YOK. Ortam: c(x) = c0(1 - 2mu/|x|)  (M-1 + M-42).
Beklenti (calisma dosyasi, Kalem A — Fermat holonomisi):
  [mu acik] - [mu kapali] farki = +4*pi*mu/R per yorunge   (agirlik +2).
Not: Bu sinav SINYAL kanalinin agirligini olcer. Madde tarafinin tur acigi
(Thomas, -1/2) ayri mekanizmadir ve jeodetik_pusula_sinavi.py SINAV 2'de
bilesim cebiriyle dogrulanmistir; toplam = 2 - 1/2 = 3/2.
"""
import numpy as np

c0 = 1.0

def cval(x, mu):
    if mu == 0.0: return c0
    return c0 * (1.0 - 2.0*mu/np.hypot(x[0], x[1]))

def gradc(x, mu):
    if mu == 0.0: return np.zeros(2)
    r2 = x[0]*x[0] + x[1]*x[1]; r = np.sqrt(r2)
    return (2.0*mu*c0/(r2*r)) * x

def rhs(state, t, mu, C, vC, a_in, om_b, gam_d):
    """state = (x1,y1,th1, x2,y2,th2); paketler yerel c ile gider, yonleri
    (i) kirilma  dth = -kperp.gradc
    (ii) merkezi bag ivmesi a_b = -om_b^2 (x-C) - gam_d*(radyal hiz) r_hat
         dth += kperp.a_b / c
    ile evrilir."""
    Ct = C(t); out = np.empty(6)
    for p in range(2):
        x = state[3*p:3*p+2]; th = state[3*p+2]
        k = np.array([np.cos(th), np.sin(th)]); kp = np.array([-k[1], k[0]])
        c = cval(x, mu); gc = gradc(x, mu)
        d = x - Ct; r = np.hypot(d[0], d[1]); rh = d/r
        vrad = c*(k @ rh)                      # radyal hiz bileseni
        ab = -om_b*om_b*d - gam_d*vrad*rh      # merkezi + radyal sonum (torksuz)
        dth = -(kp @ gc) + (kp @ ab)/c
        out[3*p:3*p+2] = c*k
        out[3*p+2] = dth
    return out

def rk4_run(mu, R, v, a_in, n_orbit, h):
    om_b = c0/a_in                              # dairesel ic dolasim kosulu
    gam_d = 0.08*om_b
    if v > 0:
        w = v/R
        C  = lambda t: R*np.array([np.cos(w*t), np.sin(w*t)])
    else:
        C  = lambda t: R*np.array([1.0, 0.0])
    vC = None
    T_orbit = (2*np.pi*R/v) if v > 0 else (2*np.pi*a_in/c0)*2000
    # baslangic: iki paket ayni noktada, zit teget yonlerde
    C0 = C(0.0); x0 = C0 + a_in*np.array([1.0, 0.0])
    st = np.array([x0[0], x0[1], np.pi/2, x0[0], x0[1], -np.pi/2])
    nstep = int(n_orbit*T_orbit/h)
    t = 0.0
    ph1 = 0.0; ph2 = 0.0                        # unwrap edilmis fazlar
    prev1 = 0.0; prev2 = 0.0
    ts, ms = [], []
    kayit = max(1, nstep//20000)
    for i in range(nstep):
        k1 = rhs(st, t, mu, C, vC, a_in, om_b, gam_d)
        k2 = rhs(st+0.5*h*k1, t+0.5*h, mu, C, vC, a_in, om_b, gam_d)
        k3 = rhs(st+0.5*h*k2, t+0.5*h, mu, C, vC, a_in, om_b, gam_d)
        k4 = rhs(st+h*k3, t+h, mu, C, vC, a_in, om_b, gam_d)
        st = st + h/6*(k1+2*k2+2*k3+k4)
        t += h
        Ct = C(t)
        a1 = np.arctan2(st[1]-Ct[1], st[0]-Ct[0])
        a2 = np.arctan2(st[4]-Ct[1], st[3]-Ct[0])
        d1 = (a1 - prev1 + np.pi) % (2*np.pi) - np.pi
        d2 = (a2 - prev2 + np.pi) % (2*np.pi) - np.pi
        ph1 += d1; ph2 += d2; prev1 = a1; prev2 = a2
        if i % kayit == 0:
            ts.append(t); ms.append(0.5*(ph1+ph2))
    ts = np.array(ts); ms = np.array(ms)
    msk = ts > 0.3*n_orbit*T_orbit/1.0          # gecici rejim disari
    slope = np.polyfit(ts[msk], ms[msk], 1)[0]
    return slope*T_orbit if v > 0 else slope    # rad/yorunge (v>0)

def main():
    R, a_in = 1.0, 0.02
    v = 0.03
    mu = 2.0e-4
    h = 2*np.pi*a_in/c0/240                     # ic dongu basina 240 adim
    print("="*76)
    print("ROZET SINAVI — isaretci m=(phi1+phi2)/2'nin sekuler kaymasi [rad/yorunge]")
    print(f"  R={R}, a_ic={a_in}, v={v}, mu={mu}, h={h:.2e}")
    print("="*76)
    print("kosuluyor: (i) mu=0 kontrol ...")
    D0 = rk4_run(0.0, R, v, a_in, n_orbit=1.5, h=h)
    print(f"  D0 (mu=0)      = {D0:+.6e} rad/yorunge   [isaretcinin kinematik payi]")
    print("kosuluyor: (ii) mu=2e-4 ...")
    D1 = rk4_run(mu, R, v, a_in, n_orbit=1.5, h=h)
    print(f"  D1 (mu=2e-4)   = {D1:+.6e} rad/yorunge")
    fark = D1 - D0
    pred = 4*np.pi*mu/R
    print(f"  FARK D1-D0     = {fark:+.6e}")
    print(f"  BEKLENEN 4*pi*mu/R = {pred:+.6e}   ->  oran = {fark/pred:.4f}")
    print()
    print("kosuluyor: (iii) statik kontrol (v=0, mu=2e-4) ...")
    Ds = rk4_run(mu, R, 0.0, a_in, n_orbit=1.0, h=h)
    print(f"  statik kayma hizi = {Ds:+.3e} rad/zaman  (beklenen ~0; simetri)")

if __name__ == "__main__":
    main()
