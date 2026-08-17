# -*- coding: utf-8 -*-
"""
JEODETIK ROZET TARAMASI — olcek ayristirmasi
=============================================
Rozet sinavinin (v3) farki beklenenin ~2.25 kati cikti. Hipotez: fark =
HOLONOMI (a ve v'den bagimsiz, 4*pi*mu/R) + BULASMA (ic yaricap a ve/veya
hiz v ile olceklenen zorlanmis-polarizasyon capraz terimleri).
Bu tarama a ve v degistirerek ikisini ayirir: a->0 limitinde oran -> 1
bekleniyorsa lemma dogrulanmis olur.
Model ve kurallar v3 ile ayni (teori-yerli; SR/GR formulu yok).
"""
import math
import numpy as np

c0 = 1.0

def kosu(mu, R, v, a_in, n_orbit, adim_per_cyc=200, skip=0.5):
    om_b = c0/a_in; gam = 0.08*om_b
    om2 = om_b*om_b
    w = v/R if v > 0 else 0.0
    T_orbit = 2*math.pi*R/v if v > 0 else 2*math.pi*a_in/c0*3000
    h = 2*math.pi*a_in/c0/adim_per_cyc
    n = int(n_orbit*T_orbit/h)
    # durum: x1,y1,t1, x2,y2,t2  (skaler; hiz icin saf python)
    Cx0 = R; Cy0 = 0.0
    x1 = Cx0 + a_in; y1 = 0.0; th1 = math.pi/2
    x2 = Cx0 + a_in; y2 = 0.0; th2 = -math.pi/2
    t = 0.0
    ph1 = ph2 = 0.0; pr1 = pr2 = 0.0
    ts = []; ms = []
    kayit = max(1, n//12000)
    mu2 = 2.0*mu*c0
    def deriv(x1,y1,th1,x2,y2,th2,t):
        if v > 0:
            Cx = R*math.cos(w*t); Cy = R*math.sin(w*t)
        else:
            Cx, Cy = Cx0, Cy0
        out = []
        for (x,y,th) in ((x1,y1,th1),(x2,y2,th2)):
            ck = math.cos(th); sk = math.sin(th)
            if mu != 0.0:
                r2 = x*x+y*y; r = math.sqrt(r2)
                c = c0*(1.0-2.0*mu/r)
                gfac = mu2/(r2*r)
                gx = gfac*x; gy = gfac*y
            else:
                c = c0; gx = gy = 0.0
            dx = x-Cx; dy = y-Cy
            rr = math.sqrt(dx*dx+dy*dy)
            rhx = dx/rr; rhy = dy/rr
            vrad = c*(ck*rhx+sk*rhy)
            abx = -om2*dx - gam*vrad*rhx
            aby = -om2*dy - gam*vrad*rhy
            # kperp = (-sk, ck)
            dth = -(-sk*gx+ck*gy) + (-sk*abx+ck*aby)/c
            out.extend((c*ck, c*sk, dth))
        return out
    for i in range(n):
        d1 = deriv(x1,y1,th1,x2,y2,th2,t)
        d2 = deriv(x1+0.5*h*d1[0], y1+0.5*h*d1[1], th1+0.5*h*d1[2],
                   x2+0.5*h*d1[3], y2+0.5*h*d1[4], th2+0.5*h*d1[5], t+0.5*h)
        d3 = deriv(x1+0.5*h*d2[0], y1+0.5*h*d2[1], th1+0.5*h*d2[2],
                   x2+0.5*h*d2[3], y2+0.5*h*d2[4], th2+0.5*h*d2[5], t+0.5*h)
        d4 = deriv(x1+h*d3[0], y1+h*d3[1], th1+h*d3[2],
                   x2+h*d3[3], y2+h*d3[4], th2+h*d3[5], t+h)
        x1 += h/6*(d1[0]+2*d2[0]+2*d3[0]+d4[0]); y1 += h/6*(d1[1]+2*d2[1]+2*d3[1]+d4[1])
        th1 += h/6*(d1[2]+2*d2[2]+2*d3[2]+d4[2])
        x2 += h/6*(d1[3]+2*d2[3]+2*d3[3]+d4[3]); y2 += h/6*(d1[4]+2*d2[4]+2*d3[4]+d4[4])
        th2 += h/6*(d1[5]+2*d2[5]+2*d3[5]+d4[5])
        t += h
        if v > 0:
            Cx = R*math.cos(w*t); Cy = R*math.sin(w*t)
        else:
            Cx, Cy = Cx0, Cy0
        a1 = math.atan2(y1-Cy, x1-Cx); a2 = math.atan2(y2-Cy, x2-Cx)
        dd1 = (a1-pr1+math.pi) % (2*math.pi) - math.pi
        dd2 = (a2-pr2+math.pi) % (2*math.pi) - math.pi
        ph1 += dd1; ph2 += dd2; pr1 = a1; pr2 = a2
        if i % kayit == 0:
            ts.append(t); ms.append(0.5*(ph1+ph2))
    ts = np.array(ts); ms = np.array(ms)
    msk = ts > skip*T_orbit
    slope = np.polyfit(ts[msk], ms[msk], 1)[0]
    return slope*T_orbit

def main():
    R = 1.0; mu = 2.0e-4
    pred = 4*math.pi*mu/R
    print("="*76)
    print(f"ROZET TARAMASI — beklenen holonomi 4*pi*mu/R = {pred:.6e} (a ve v'den bagimsiz)")
    print("="*76)
    print(f"{'a_ic':>7}{'v':>7}{'D(mu=0)':>15}{'D(mu)':>15}{'FARK':>13}{'oran':>8}")
    for a_in, v in [(0.04,0.03),(0.02,0.03),(0.01,0.03),(0.02,0.02),(0.01,0.02)]:
        D0 = kosu(0.0, R, v, a_in, n_orbit=2.0)
        D1 = kosu(mu, R, v, a_in, n_orbit=2.0)
        fark = D1-D0
        print(f"{a_in:>7}{v:>7}{D0:>15.6e}{D1:>15.6e}{fark:>13.4e}{fark/pred:>8.4f}")

if __name__ == "__main__":
    main()
