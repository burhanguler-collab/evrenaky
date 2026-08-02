"""ETKILESIMLI SINIF PANELI.  Kullanim: python kur_etkilesimli.py 01_erken_spiral

Bir sinif klasoru icin tek dosyalik, disa bagimliligi olmayan HTML uretir:
  <sinif>/HESAP/panel.html

Ozellikler
  - 12 galaksinin egrisi tek tek secilebilir (liste + ileri/geri + oto-oynatma)
  - Her cizgi ayri ayri acilip kapatilabilir (olcum, iki ongoru, iki fit, baryon bilesenleri)
  - Secili galaksi icin EVRENAKI GIRDILERI acikca gosterilir: hangi sayi nereden geliyor,
    rozeti ne ([T] turetilmis / [S] gozlemle sabitlenmis / [O] olculmus)
  - Olcut tablosu: RMS, chi2_ind, hata cubugu icindeki nokta orani

Veri HTML'e gomulur (JSON), yani dosya tek basina calisir; internet gerekmez.
Sayilarin hepsi bu betikte yeniden hesaplanir — sinif_ongoru_vs_fit.py ile ayni denklemler.
"""

import os
import sys
import glob
import csv
import json
import warnings

import numpy as np
from scipy.optimize import curve_fit

warnings.filterwarnings('ignore')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

KOK = os.path.dirname(os.path.abspath(__file__))
SINIF = sys.argv[1] if len(sys.argv) > 1 else '01_erken_spiral'
SDIR = os.path.join(KOK, 'SINIF_CALISMASI', SINIF)
HDIR = os.path.join(SDIR, 'HESAP')
os.makedirs(HDIR, exist_ok=True)

G = 4.300917e-6
C_SI = 2.99792458e8
H0_SI = 70e3 / 3.0857e22
ACC = 1e6 / 3.0856776e19
CH0 = (C_SI * H0_SI) / ACC
KATSAYI = 16.1
A0 = CH0 / KATSAYI                    # kitabin eski degeri (tarihsel)
# NIHAI KURULUM (86_NIHAI) + PENCERELI RESMI KALIBRASYON (M-47; 87_ETKIN_YASA/PENCERE_TURETIMI.md)
A0N = 1.75 * 1.038 * A0            # = 7,67e-11 m/s^2
A0_SI = A0N * ACC
RHO_CRIT = 3 * 0.07 ** 2 / (8 * np.pi * G)
H_RED, RB, UPS_PS = 0.7, 1.4, 0.50
YLO, YHI = 0.05, 2.0
TIPAD = {0: 'S0', 1: 'Sa', 2: 'Sab', 3: 'Sb', 4: 'Sbc', 5: 'Sc',
         6: 'Scd', 7: 'Sd', 8: 'Sdm', 9: 'Sm', 10: 'Im', 11: 'BCD'}

_lM1, _N, _be, _ga = 11.59, 0.0351, 1.376, 0.608
_Mh = 10 ** np.linspace(9.0, 15.0, 8000)
_Ms = _Mh * 2 * _N / ((_Mh / 10 ** _lM1) ** -_be + (_Mh / 10 ** _lM1) ** _ga)
Mhalo_am = lambda Ms: float(np.interp(Ms, _Ms, _Mh))
c200_dm14 = lambda M: 10 ** (0.905 - 0.101 * np.log10(M * H_RED / 1e12))


def v_nfw2(R, M200):
    cc = c200_dm14(M200)
    r200 = (3 * M200 / (4 * np.pi * 200 * RHO_CRIT)) ** (1 / 3.0)
    rs = r200 / cc
    mu = lambda x: np.log(1 + x) - x / (1 + x)
    return G * M200 / R * mu(R / rs) / mu(cc)


KAT = {r['Galaksi']: r for r in csv.DictReader(open(os.path.join(SDIR, 'KATALOG.csv'), encoding='utf-8'))}
GAL = []
for f in sorted(glob.glob(os.path.join(SDIR, 'veri', '*_rotmod.dat'))):
    ad = os.path.basename(f)[:-11]
    d = np.loadtxt(f)
    R, Vo, eV, Vg, Vd, Vb, SBd, SBb = [d[:, i] for i in range(8)]
    eV = np.maximum(eV, 1.0)
    Rp = R * 1e3
    L = lambda S: np.concatenate([[0.0], np.cumsum(
        np.pi * (Rp[1:] ** 2 - Rp[:-1] ** 2) * 0.5 * (S[1:] + S[:-1]))])
    k = KAT[ad]
    GAL.append(dict(g=ad, R=R, Vo=Vo, eV=eV, Vg=Vg, Vd=Vd, Vb=Vb, Ld=L(SBd), Lb=L(SBb),
                    N=len(R), L36=float(k['L36_1e9Lsun']) * 1e9, Q=int(k['Q']),
                    inc=float(k['Inc_deg']), einc=float(k['eInc_deg']),
                    D=float(k['D_Mpc']), eD=float(k['eD_Mpc']), Rd=float(k['Rdisk_kpc']),
                    MHI=float(k['MHI_1e9Msun']) * 1e9, Vflat=float(k['Vflat_kms']),
                    tip=TIPAD.get(int(k['T']), k['T']), kaynak=k['Kaynak']))
GAL.sort(key=lambda d: -d['Vo'].max())

Vbar2 = lambda d, Y: np.sign(d['Vg']) * d['Vg'] ** 2 + Y * d['Vd'] ** 2 + RB * Y * d['Vb'] ** 2
Mgas = lambda d: np.maximum(d['R'] * np.sign(d['Vg']) * d['Vg'] ** 2 / G, 0.0)
Mkaps = lambda d, Y: Y * d['Ld'] + RB * Y * d['Lb'] + Mgas(d)
olc = lambda d, mv, k: dict(
    rms=float(np.sqrt(np.mean((mv - d['Vo']) ** 2))),
    ci=float(np.sum(((mv - d['Vo']) / d['eV']) ** 2) / max(d['N'] - k, 1)),
    ic=float(np.mean(np.abs(mv - d['Vo']) <= d['eV'])))


def fitle(d, tur):
    if tur == 'evr':
        # NIHAI bicimin fiti: v^2 = Vbar^2(Y) + (10^lb) sqrt(M_kaps(Y))
        # pencereli bicim (M-47): a0_fit = (10^lb)^2/G, W = min(1, a0_fit R^2 / (G Mkaps))
        f = lambda R, Y, lb, _d=d: np.sqrt(np.maximum(Vbar2(_d, Y), 1e-9)
                                           + (10 ** lb) * np.sqrt(np.maximum(Mkaps(_d, Y), 1e-9))
                                           * np.minimum(1.0, (10 ** lb) ** 2 * R ** 2
                                                        / (G * G * np.maximum(Mkaps(_d, Y), 1e-9))))
        p0, lo, hi = [0.5, -6.4], [YLO, -12], [YHI, -1]
    else:
        f = lambda R, Y, lg, _d=d: np.sqrt(np.maximum(Vbar2(_d, Y), 1e-9) + v_nfw2(R, 10 ** lg))
        p0, lo, hi = [0.5, 11.0], [YLO, 7.0], [YHI, 13.5]
    try:
        p, _ = curve_fit(f, d['R'], d['Vo'], sigma=d['eV'], p0=p0, bounds=(lo, hi), maxfev=600000)
    except Exception:
        return None, None
    mv = f(d['R'], *p)
    return (mv, [float(x) for x in p]) if np.all(np.isfinite(mv)) else (None, None)


VER = []
for d in GAL:
    M = Mkaps(d, UPS_PS)
    Mb = float(max(M[-1], 1e-6))
    lom = float(np.sqrt(G * Mb / A0N))
    gkap = G * np.maximum(M, 1e-9) / d['R'] ** 2
    Wp = np.minimum(1.0, A0N / gkap)                   # M-47 penceresi
    eo = np.sqrt(np.maximum(Vbar2(d, UPS_PS), 1e-9) + np.sqrt(A0N * G * np.maximum(M, 1e-9)) * Wp)
    Ms = UPS_PS * d['L36']
    M200 = Mhalo_am(Ms)
    lo_ = np.sqrt(np.maximum(Vbar2(d, UPS_PS), 1e-9) + v_nfw2(d['R'], M200))
    ef, ep = fitle(d, 'evr')
    lf, lp = fitle(d, 'lcdm')
    bar = np.sqrt(np.maximum(Vbar2(d, UPS_PS), 0))
    # yeni fit parametresi b = sqrt(a0_fit G) -> ima edilen a0 carpani (A0N'e gore)
    lom_fit = float((10 ** ep[1]) ** 2 / (G * A0N)) if ep else None
    Mk_fit = Mkaps(d, ep[0]) if ep else M
    L = lambda a: [round(float(x), 4) for x in a]
    VER.append(dict(
        ad=d['g'], tip=d['tip'], Q=d['Q'], inc=d['inc'], einc=d['einc'], D=d['D'], eD=d['eD'],
        Rd=d['Rd'], MHI=d['MHI'], L36=d['L36'], Vflat=d['Vflat'], kaynak=d['kaynak'], N=d['N'],
        R=L(d['R']), Vo=L(d['Vo']), eV=L(d['eV']),
        Vgas=L(np.sign(d['Vg']) * np.sqrt(np.abs(d['Vg']))**2 * np.sign(d['Vg'])),
        Vg_raw=L(d['Vg']),
        Vdisk=L(np.sqrt(UPS_PS) * d['Vd']), Vbul=L(np.sqrt(RB * UPS_PS) * d['Vb']),
        bar=L(bar), eo=L(eo), lo=L(lo_), ef=L(ef) if ef is not None else None,
        lf=L(lf) if lf is not None else None,
        Mkaps=[float('%.4g' % x) for x in M], Mkaps_fit=[float('%.4g' % x) for x in Mk_fit],
        girdi=dict(Ups=UPS_PS, Mbar=Mb, lom=lom, Mgas=float(Mgas(d)[-1]),
                   Mstar=float(UPS_PS * (d['Ld'][-1] + RB * d['Lb'][-1])),
                   Ups_fit=ep[0] if ep else None, b_fit=float(10 ** ep[1]) if ep else None,
                   lom_fit=lom_fit, Mbar_fit=float(Mk_fit[-1]) if ep else None,
                   M200_ong=M200, c200_ong=float(c200_dm14(M200)),
                   M200_fit=float(10 ** lp[1]) if lp else None,
                   Ups_lcdm_fit=lp[0] if lp else None),
        m=dict(bar=olc(d, bar, 0), eo=olc(d, eo, 0), lo=olc(d, lo_, 0),
               ef=olc(d, ef, 2) if ef is not None else None,
               lf=olc(d, lf, 2) if lf is not None else None)))

SBT = dict(sinif=SINIF, n=len(VER), G=G, CH0_SI=float(CH0 * ACC), KATSAYI=KATSAYI,
           A0_SI=float(A0_SI), A0=float(A0), UPS_PS=UPS_PS, RB=RB, H0=float(H0_SI),
           c=C_SI, rho_n=2.702e17, rho0_rhon=0.25)

HTML = r"""<!doctype html><html lang="tr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>@@SINIF@@ — etkileşimli panel</title><style>
*{box-sizing:border-box}
body{margin:0;background:#0d0d0f;color:#e4e4e7;font:14px/1.5 system-ui,Segoe UI,sans-serif}
h1{font-size:17px;margin:0 0 2px;font-weight:600}
.ust{padding:12px 16px;border-bottom:1px solid #27272a;display:flex;gap:16px;align-items:baseline;flex-wrap:wrap}
.ust .alt{color:#a1a1aa;font-size:12.5px}
.kap{display:grid;grid-template-columns:190px 1fr 320px;gap:14px;padding:14px 16px;align-items:start}
@media(max-width:1100px){.kap{grid-template-columns:1fr}}
.bl{background:#141417;border:1px solid #27272a;border-radius:8px;padding:11px}
.bl h2{font-size:12px;text-transform:uppercase;letter-spacing:.5px;color:#a1a1aa;margin:0 0 8px;font-weight:600}
button{font:inherit;cursor:pointer}
.gl{display:flex;flex-direction:column;gap:3px;max-height:60vh;overflow:auto}
.gl button{background:#1c1c21;border:1px solid #2f2f36;color:#d4d4d8;border-radius:5px;
  padding:5px 8px;text-align:left;font-size:12.5px;display:flex;justify-content:space-between}
.gl button:hover{background:#26262c}
.gl button.on{background:#166534;border-color:#22c55e;color:#fff}
.gl button i{font-style:normal;color:#71717a;font-size:11px}
.gl button.on i{color:#bbf7d0}
.oyn{display:flex;gap:5px;margin-top:8px}
.oyn button{flex:1;background:#1c1c21;border:1px solid #2f2f36;color:#d4d4d8;border-radius:5px;padding:5px}
.oyn button:hover{background:#26262c}
canvas{width:100%;height:auto;display:block;background:#0d0d0f;border-radius:6px}
.cz{display:flex;flex-direction:column;gap:5px}
.cz label{display:flex;align-items:center;gap:7px;font-size:12.5px;cursor:pointer;
  padding:3px 5px;border-radius:4px}
.cz label:hover{background:#1c1c21}
.cz input{accent-color:#22c55e;width:14px;height:14px}
.sw{width:20px;height:3px;border-radius:2px;flex:none}
.sw.d{height:0;border-top:3px dashed currentColor}
.sw.p{height:0;border-top:3px dotted currentColor}
table{width:100%;border-collapse:collapse;font-size:12px}
th,td{text-align:right;padding:3px 5px;border-bottom:1px solid #1f1f24}
th:first-child,td:first-child{text-align:left}
thead th{color:#a1a1aa;font-weight:600;font-size:11px}
.gr{font-size:12px}
.gr div{display:flex;justify-content:space-between;gap:8px;padding:3px 0;border-bottom:1px solid #1f1f24}
.gr span:first-child{color:#a1a1aa}
.gr b{font-weight:600;font-variant-numeric:tabular-nums}
.rz{font-size:9.5px;padding:1px 4px;border-radius:3px;margin-left:5px;vertical-align:middle;font-weight:700}
.rT{background:#166534;color:#bbf7d0}.rS{background:#78350f;color:#fde68a}.rO{background:#1e3a5f;color:#bfdbfe}
.dnk{font-size:12px;background:#0f1419;border:1px solid #1f2937;border-radius:6px;padding:8px;margin-top:8px;
  font-family:ui-monospace,Consolas,monospace;color:#93c5fd;line-height:1.7}
.not{font-size:11.5px;color:#71717a;margin-top:9px;line-height:1.5}
.kz{color:#22c55e}.kk{color:#f87171}
</style></head><body><div style="padding:9px 16px;background:rgba(34,197,94,0.10);border-bottom:1px solid #166534;color:#bbf7d0;font-size:12.5px;line-height:1.45"><strong style="font-size:14px;letter-spacing:.3px">SERBEST PARAMETRE (galaksi ba&#351;&#305;na): <span style="color:#4ade80">EVRENAKI&nbsp;0</span> &nbsp;&#183;&nbsp; &#923;CDM (fit)&nbsp;2</strong> &#8212; fit bu kar&#351;&#305;la&#351;t&#305;rmada teorinin de&#287;il, rakip modelin ihtiyac&#305;d&#305;r. Bu panel <strong>öngörü arenas&#305;d&#305;r</strong>: teorinin fitli e&#287;risi <strong>yoktur — ihtiyac&#305; da yoktur</strong>.<br>&#9889; <strong>Fitsizlik durumu:</strong> Teori hi&#231;bir fit de&#287;erine muhta&#231; de&#287;ildir; tek kalibre say&#305;n&#305;n (a&#8320;) da t&#252;retilmi&#351; kar&#351;&#305;l&#305;&#287;&#305; mevcuttur (M-45) ve yaln&#305;z stat&#252; disiplini gere&#287;i kalibre de&#287;er resm&#238; kullan&#305;mda tutulmaktad&#305;r. Bu paneldeki &#246;ng&#246;r&#252; e&#287;rilerinde galaksi ba&#351;&#305;na fitlenen hi&#231;bir say&#305; yoktur. &#214;ng&#246;r&#252; e&#287;rileri, M-47 penceresini i&#231;eren <strong>pencereli resm&#238; denklemle</strong> hesaplan&#305;r (W = min(1, a&#8320;/g<sub>kaps</sub>) &#8212; Rankine i&#231; kolu, parametresiz).</div>
<div class="ust"><h1>@@SINIF_AD@@ — etkileşimli panel</h1>
<span class="alt">@@N@@ galaksi · SPARC ölçümü + iki parametresiz öngörü (Evrenakı FİT: 0) ·
rakibin fiti çentikle açılır · tek dosya, dış bağımlılık yok</span></div>
<div class="kap">
 <div class="bl"><h2>Galaksi</h2><div class="gl" id="gl"></div>
  <div class="oyn"><button id="geri">◀</button><button id="oyna">▶ Oynat</button><button id="ileri">▶</button></div>
  <div class="not">Oynat: 1,4 s aralıkla sırayla gezer.<br>Klavye: ← → ok tuşları, boşluk oynat/durdur.</div>
 </div>
 <div class="bl"><h2 id="bas">—</h2><canvas id="cv" width="1180" height="660"></canvas>
  <table id="tb"><thead><tr><th>Model</th><th>k</th><th>RMS (km/s)</th><th>χ²/(N−k)</th><th>Hata çubuğu içinde</th></tr></thead><tbody></tbody></table>
  <div class="not" id="dpn"></div>
 </div>
 <div class="bl"><h2>Çizgiler</h2><div class="cz" id="cz"></div>
  <h2 style="margin-top:14px">Evrenakı girdileri</h2><div class="gr" id="grd"></div>
  <div class="dnk" id="dnk"></div>
  <div class="not"><b>Rozetler:</b> <span class="rz rT">T</span> teoriden türetilmiş ·
  <span class="rz rS">S</span> gözlemle sabitlenmiş (kalibre) · <span class="rz rO">Ö</span> bu galaksinin ölçümü
  <br><br>Bu paneldeki hiçbir Evrenakı girdisi galaksi başına serbest değildir; öngörü eğrisi
  yalnız yukarıdaki dört satırdan üretilir.</div>
  <h2 style="margin-top:14px">ΛCDM girdileri</h2><div class="gr" id="grl"></div>
 </div>
</div>
<script>
const V=@@VERI@@, S=@@SBT@@;
const CZ=[
 {k:'Vo', ad:'ÖLÇÜM (hata çubuklu)', c:'#ffcc00', t:'nokta', on:1},
 {k:'eo', ad:'EVRENAKI ÖNGÖRÜSÜ — FİT: 0', c:'#16a34a', t:'kalin', on:1},
 {k:'lo', ad:'ΛCDM zincir öngörüsü — FİT: 0', c:'#7c3aed', t:'kalin', on:1},
 {k:'lf', ad:'ΛCDM FİT — 2 serbest parametre (M₂₀₀, Υ*)', c:'#a78bfa', t:'kesik', on:0},
 {k:'bar',ad:'Baryonlar toplam (Υ*=0,50)', c:'#71717a', t:'nokta_c', on:1},
 {k:'Vdisk',ad:'— bileşen: disk', c:'#38bdf8', t:'ince', on:0},
 {k:'Vbul', ad:'— bileşen: kovan', c:'#fb923c', t:'ince', on:0},
 {k:'Vg_raw',ad:'— bileşen: gaz', c:'#2dd4bf', t:'ince', on:0}];
let i=0, acik={}, oto=null;
CZ.forEach(x=>acik[x.k]=!!x.on);
const q=s=>document.querySelector(s), fx=(x,n)=>Number(x).toFixed(n);
const us=x=>{if(x==null)return'—';const e=Math.floor(Math.log10(Math.abs(x)));
 return (x/Math.pow(10,e)).toFixed(2)+'×10'+String(e).replace(/[0-9-]/g,d=>'⁰¹²³⁴⁵⁶⁷⁸⁹⁻'['0123456789-'.indexOf(d)]);};

/* galaksi listesi */
const gl=q('#gl');
V.forEach((g,n)=>{const b=document.createElement('button');
 b.innerHTML='<span>'+g.ad+'</span><i>'+fx(Math.max(...g.Vo),0)+' km/s</i>';
 b.onclick=()=>{i=n;ciz();};gl.appendChild(b);});

/* cizgi anahtarlari */
const cz=q('#cz');
CZ.forEach(x=>{const l=document.createElement('label');
 const st=x.t==='kesik'?'sw d':(x.t==='nokta_c'?'sw p':'sw');
 l.innerHTML='<input type="checkbox" '+(x.on?'checked':'')+'><span class="'+st+
   '" style="color:'+x.c+';background:'+(x.t==='kesik'||x.t==='nokta_c'?'none':x.c)+'"></span>'+x.ad;
 l.querySelector('input').onchange=e=>{acik[x.k]=e.target.checked;ciz();};cz.appendChild(l);});

function ciz(){
 const g=V[i];
 [...gl.children].forEach((b,n)=>b.className=n===i?'on':'');
 q('#bas').textContent=g.ad+'  ·  '+g.tip+'  ·  Q='+g.Q+'  ·  i='+fx(g.inc,0)+'°±'+fx(g.einc,0)+'°  ·  D='+fx(g.D,2)+'±'+fx(g.eD,2)+' Mpc  ·  N='+g.N;

 const cv=q('#cv'),x=cv.getContext('2d'),W=cv.width,H=cv.height,
  ml=68,mr=14,mt=14,mb=48;
 x.clearRect(0,0,W,H);
 let xm=Math.max(...g.R)*1.04, ym=Math.max(...g.Vo.map((v,j)=>v+g.eV[j]));
 CZ.forEach(c=>{if(acik[c.k]&&g[c.k]&&c.k!=='Vo')ym=Math.max(ym,...g[c.k].map(Math.abs));});
 ym*=1.10;
 const X=v=>ml+v/xm*(W-ml-mr), Y=v=>H-mb-v/ym*(H-mt-mb);
 /* izgara */
 x.strokeStyle='#1f1f24';x.lineWidth=1;x.fillStyle='#71717a';x.font='12px system-ui';
 const adim=(m)=>{const p=Math.pow(10,Math.floor(Math.log10(m)));const n=m/p;
   return p*(n<1.5?.2:n<3?.5:n<7?1:2);};
 for(let v=0,d=adim(ym);v<=ym;v+=d){x.beginPath();x.moveTo(ml,Y(v));x.lineTo(W-mr,Y(v));x.stroke();
   x.textAlign='right';x.fillText(v.toFixed(0),ml-8,Y(v)+4);}
 for(let v=0,d=adim(xm);v<=xm;v+=d){x.beginPath();x.moveTo(X(v),mt);x.lineTo(X(v),H-mb);x.stroke();
   x.textAlign='center';x.fillText(v.toFixed(v<10?1:0),X(v),H-mb+18);}
 x.fillStyle='#a1a1aa';x.font='13px system-ui';
 x.fillText('R  (kpc)',(ml+W-mr)/2,H-12);
 x.save();x.translate(16,(mt+H-mb)/2);x.rotate(-Math.PI/2);x.textAlign='center';
 x.fillText('V  (km/s)',0,0);x.restore();
 /* fit damgasi — grafik uzerinde, her zaman gorunur */
 x.font='600 13px system-ui';x.textAlign='right';
 x.fillStyle='#4ade80';x.fillText('EVRENAKI FİT: 0  (saf öngörü)',W-mr-10,mt+20);
 x.fillStyle='#a78bfa';
 x.fillText(acik['lf']?'ΛCDM FİT: 2 parametre (M₂₀₀, Υ*)':'ΛCDM zincir FİT: 0',W-mr-10,mt+38);
 /* egriler */
 CZ.forEach(c=>{
  if(!acik[c.k]||c.k==='Vo'||!g[c.k])return;
  x.strokeStyle=c.c;x.lineWidth=c.t==='kalin'?2.6:(c.t==='ince'?1.3:1.7);
  x.setLineDash(c.t==='kesik'?[7,5]:(c.t==='nokta_c'?[2,4]:[]));
  x.beginPath();g[c.k].forEach((v,j)=>{const yy=Y(Math.abs(v));j?x.lineTo(X(g.R[j]),yy):x.moveTo(X(g.R[j]),yy);});
  x.stroke();x.setLineDash([]);});
 /* olcum */
 if(acik['Vo']){x.strokeStyle='#ffcc00';x.fillStyle='#ffcc00';x.lineWidth=1.4;
  g.R.forEach((r,j)=>{const cx=X(r);
   x.beginPath();x.moveTo(cx,Y(g.Vo[j]-g.eV[j]));x.lineTo(cx,Y(g.Vo[j]+g.eV[j]));x.stroke();
   x.beginPath();x.moveTo(cx-3,Y(g.Vo[j]-g.eV[j]));x.lineTo(cx+3,Y(g.Vo[j]-g.eV[j]));
   x.moveTo(cx-3,Y(g.Vo[j]+g.eV[j]));x.lineTo(cx+3,Y(g.Vo[j]+g.eV[j]));x.stroke();
   x.beginPath();x.arc(cx,Y(g.Vo[j]),3.4,0,7);x.fill();});}

 /* olcut tablosu */
 const M=[['Yalnız baryonlar','bar',0],['ΛCDM zincir öngörüsü','lo',0],
          ['EVRENAKI ÖNGÖRÜSÜ','eo',0]];  /* yeşil yarış yalnız öngörü satırları arasında */
 let en=1e9,enk=null;M.forEach(([,k])=>{if(g.m[k]&&g.m[k].rms<en){en=g.m[k].rms;enk=k;}});
 if(acik['lf']&&g.m.lf)M.push(['ΛCDM FİT (rakibin fiti — yarış dışı)','lf',2]);
 q('#tb tbody').innerHTML=M.map(([ad,k,kk])=>{const m=g.m[k];if(!m)return'';
  const v=k===enk?' style="color:#22c55e;font-weight:600"':(k==='lf'?' style="color:#a78bfa"':'');
  return '<tr'+v+'><td>'+ad+'</td><td>'+kk+'</td><td>'+fx(m.rms,2)+'</td><td>'+fx(m.ci,2)+
   '</td><td>'+fx(100*m.ic,0)+'%</td></tr>';}).join('');
 const de=g.m.eo.rms,dl=g.m.lo.rms;
 q('#dpn').innerHTML='Öngörü yarışı: <b class="'+(de<dl?'kz':'kk')+'">'+
  (de<dl?'Evrenakı':'ΛCDM')+'</b> daha yakın (RMS '+fx(Math.min(de,dl),1)+
  ' / '+fx(Math.max(de,dl),1)+' km/s). Yeşil satır: en küçük RMS.';

 /* Evrenaki girdileri */
 const gi=g.girdi, sat=(a,b,r)=>'<div><span>'+a+(r?'<span class="rz r'+r+'">'+r+'</span>':'')+
   '</span><b>'+b+'</b></div>';
 q('#grd').innerHTML=
  sat('𝒢 = α/ρ<sub>n</sub>', us(S.G)+' kpc(km/s)²/M☉','T')+
  sat('a₀ (pencereli resmî kalibrasyon — M-47)', us(S.A0_SI)+' m/s²','S')+
  sat('Υ* (popülasyon sentezi)', fx(gi.Ups,2),'S')+
  sat('M<sub>bar</sub> (kapsanan, son nokta)', us(gi.Mbar)+' M☉','O')+
  '<div style="border-bottom:none;padding-top:6px"><span>— yıldız / gaz payı</span><b>'+
   us(gi.Mstar)+' / '+us(gi.Mgas)+'</b></div>'+
  sat('ℓ<sub>ω</sub>(R<sub>dış</sub>) = √(𝒢M<sub>bar</sub>/a₀)', fx(gi.lom,2)+' kpc','T')+
  '<div style="border-bottom:none;padding-top:8px;color:#a1a1aa;font-size:11.5px">'+
   'fit karşılaştırması için: Υ*<sub>fit</sub>='+(gi.Ups_fit==null?'—':fx(gi.Ups_fit,3))+
   ' · a₀<sub>fit</sub>/a₀='+(gi.lom_fit==null?'—':fx(gi.lom_fit,2))+'</div>';
 q('#dnk').innerHTML='v²(R) = V<sub>bar</sub>²(Υ*) + √(𝒢·M<sub>kaps</sub>(R)·a₀)·W, &nbsp;W = min(1, a₀/g<sub>kaps</sub>)'+'<br><span style="color:#71717a">ℓ<sub>ω</sub> YEREL kütleden — pencereli resmî denklem (M-47)</span>';
 q('#grl').innerHTML=
  sat('Υ* (aynı girdi)', fx(S.UPS_PS,2),'S')+
  sat('M<sub>*</sub> = Υ*·L[3,6]', us(S.UPS_PS*g.L36)+' M☉','O')+
  sat('M₂₀₀ ← abundance matching', us(gi.M200_ong)+' M☉','S')+
  sat('c₂₀₀ ← Dutton &amp; Macciò', fx(gi.c200_ong,2),'S')+
  '<div style="border-bottom:none;padding-top:8px;color:#a1a1aa;font-size:11.5px">'+
   'fit karşılaştırması için: M₂₀₀<sub>,fit</sub>='+(gi.M200_fit==null?'—':us(gi.M200_fit))+
   ' M☉ · Υ*<sub>fit</sub>='+(gi.Ups_lcdm_fit==null?'—':fx(gi.Ups_lcdm_fit,3))+'</div>';
}
q('#ileri').onclick=()=>{i=(i+1)%V.length;ciz();};
q('#geri').onclick=()=>{i=(i-1+V.length)%V.length;ciz();};
q('#oyna').onclick=e=>{if(oto){clearInterval(oto);oto=null;e.target.textContent='▶ Oynat';}
 else{oto=setInterval(()=>{i=(i+1)%V.length;ciz();},1400);e.target.textContent='⏸ Durdur';}};
addEventListener('keydown',e=>{
 if(e.key==='ArrowRight'){i=(i+1)%V.length;ciz();}
 else if(e.key==='ArrowLeft'){i=(i-1+V.length)%V.length;ciz();}
 else if(e.key===' '){e.preventDefault();q('#oyna').click();}});
ciz();
</script></body></html>"""

HTML = (HTML.replace('@@VERI@@', json.dumps(VER, ensure_ascii=False))
        .replace('@@SBT@@', json.dumps(SBT))
        .replace('@@SINIF_AD@@', SINIF.replace('_', ' ').title())
        .replace('@@SINIF@@', SINIF)
        .replace('@@N@@', str(len(VER))))
yol = os.path.join(HDIR, 'panel.html')
open(yol, 'w', encoding='utf-8').write(HTML)
print('%s : %d galaksi -> HESAP/panel.html  (%.0f KB)' % (SINIF, len(VER), len(HTML) / 1024))
