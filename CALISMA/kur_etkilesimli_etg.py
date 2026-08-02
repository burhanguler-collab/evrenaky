# -*- coding: utf-8 -*-
"""ETG (erken tip galaksi) icin etkilesimli panel — tek dosya, dis bagimlilik yok.

97_BTFR panelinden FARKI: orada eksen hiz-kutle idi, burada RADYAL IVME
DUZLEMI var ve arka planda 2693 disk noktasi duruyor. Yani panel her an
"ETG'ler disklerin ustune dusuyor mu" sorusunu gorsel olarak yanitliyor.

Her durustluk kaydi bir dugmeye baglidir:

  1) Nokta kumesi     : ic / dis / ikisi        -> md. 3 (ic nokta kotu kosullu)
  2) a_0 carpani       : x0,5 - x4 canli         -> md. 2
  3) Y* kaydiraci      : 0,40 - 1,00             -> md. 4, md. 5
     BU DUGME PANELIN ASIL FIKRIDIR: Y* oynatilinca LCDM'in ongorusu kayar,
     TEORININ ongorusu KILINI KIPIRDATMAZ. Cunku teori g_bar'i OLCUM olarak
     alir; LCDM ise yaricapi Y*'dan geri kurmak zorundadir.
  4) F4 payi gostergesi: gereken a_0'in nerede okunabilecegini soyler
  5) Disk RAR bulutu   : ayni olcut, 2693 nokta  -> md. 2

Panelde gosterilen ve TEORININ ALEYHINE olan sonuclar (dis noktada LCDM'in
medyan ve sacilmada onde olusu, ic noktadaki 0,12 dex acik) AYNEN durur.

Cikti: SINIF_CALISMASI/96_ETG/panel.html
"""

import os
import sys
import json
import warnings

import numpy as np

warnings.filterwarnings('ignore')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

KOK = os.path.dirname(os.path.abspath(__file__))
VERI = os.path.join(KOK, 'veri')
CIK = os.path.join(KOK, 'SINIF_CALISMASI', '96_ETG')
os.makedirs(CIK, exist_ok=True)

# ---- sabitler: etg_sinavi.py ve btfr_sinavi.py ile BIREBIR ayni ----
G = 4.300917e-6
C_SI = 2.99792458e8
H0_SI = 70e3 / 3.0857e22
ACC = 1e6 / 3.0856776e19
KATSAYI = 16.1
A0_ESKI = (C_SI * H0_SI) / ACC / KATSAYI   # kitabin eski degeri (tarihsel)
# NIHAI KURULUM (86_NIHAI): a_0 = 1,75 x cH_0/16,1
A0 = 1.75 * 1.038 * A0_ESKI        # pencereli resmi kalibrasyon (M-47) = 7,67e-11 m/s^2
A0_SI = A0 * ACC                          # m/s^2
RHO_CRIT = 3 * 0.07 ** 2 / (8 * np.pi * G)
H_RED = 0.7
G_DAGGER = 1.20e-10
UPS_LST = [0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00]   # Y* kaydiracinin duraklari


def oku_etg(yol):
    ALAN = ['Ad', 'D', 'eD', 'fD', 'Inc', 'eInc', 'L36', 'eL36', 'Reff', 'SBeff',
            'Rexp', 'SBexp', 'Ao1', 'eAo1', 'Ao2', 'eAo2', 'Ab1', 'eAb1', 'Ab2', 'eAb2']
    D = []
    for L in open(yol, encoding='utf-8', errors='replace'):
        p = L.split()
        if not p or p[0].startswith('#') or len(p) < len(ALAN):
            continue
        try:
            g = {k: float(v) for k, v in zip(ALAN[1:], p[1:len(ALAN)])}
        except ValueError:
            continue
        g['Ad'] = p[0]
        D.append(g)
    return D


def oku_rar(yol):
    P = []
    for L in open(yol, encoding='utf-8', errors='replace'):
        p = L.split()
        if len(p) != 4:
            continue
        try:
            v = [float(x) for x in p]
        except ValueError:
            continue
        if -14 < v[0] < -7 and -14 < v[2] < -7:
            P.append([round(v[0], 2), round(v[2], 2)])
    return P


E = oku_etg(os.path.join(VERI, '_etg.mrt'))
RAR = oku_rar(os.path.join(VERI, '_RAR.mrt'))

_lM1, _N, _be, _ga = 11.59, 0.0351, 1.376, 0.608
_Mh = 10 ** np.linspace(9.0, 15.0, 8000)
_Ms = _Mh * 2 * _N / ((_Mh / 10 ** _lM1) ** -_be + (_Mh / 10 ** _lM1) ** _ga)
mu = lambda x: np.log(1 + x) - x / (1 + x)
KIRPILAN = []


def lcdm(Mst, gbar_si, ad=''):
    """Yaricabi g_bar'dan geri kur, NFW kapsanan kutlesinin ivmesini dondur.

    DIKKAT: np.interp tablo disini SESSIZCE kirpar (97_BTFR panelinde bir kez
    hataya yol acti). Kirpilan her galaksi kaydedilir ve ekrana basilir.
    """
    if Mst < _Ms[0] or Mst > _Ms[-1]:
        KIRPILAN.append((ad, Mst))
    R = float(np.sqrt(G * Mst / (gbar_si / ACC)))          # kpc
    M200 = float(np.interp(Mst, _Ms, _Mh))
    c = 10 ** (0.905 - 0.101 * np.log10(M200 * H_RED / 1e12))
    R200 = (3 * M200 / (4 * np.pi * 200 * RHO_CRIT)) ** (1 / 3.)
    aDM = G * (M200 * mu(c * R / R200) / mu(c)) / R ** 2 * ACC
    return R, float(aDM), M200, float(c)


VER = []
for g in sorted(E, key=lambda z: -z['L36']):
    L36 = g['L36'] * 1e9                 # SPARC birimi 10^9 L_gunes — 1e9 ZORUNLU
    gb = [10 ** g['Ab1'], 10 ** g['Ab2']]
    go = [10 ** g['Ao1'], 10 ** g['Ao2']]
    Rk, aD, M2, c2 = {}, {}, {}, {}
    for u in UPS_LST:
        ak = '%.2f' % u
        Rk[ak], aD[ak], M2[ak], c2[ak] = [], [], [], []
        for j in (0, 1):
            R, a, M, c = lcdm(u * L36, gb[j], g['Ad'])
            Rk[ak].append(round(R, 3)); aD[ak].append(a)
            M2[ak].append(M); c2[ak].append(round(c, 3))
    VER.append(dict(ad=g['Ad'], D=g['D'], eD=g['eD'], inc=g['Inc'], einc=g['eInc'],
                    L36=L36, Reff=g['Reff'], SBeff=g['SBeff'],
                    gb=gb, go=go, ego=[g['eAo1'], g['eAo2']],
                    lgb=[g['Ab1'], g['Ab2']], lgo=[g['Ao1'], g['Ao2']],
                    R=Rk, aDM=aD, M200=M2, c200=c2))

SBT = dict(n=len(VER), A0=float(A0_SI), KATSAYI=KATSAYI, G=G,
           CH0=float(C_SI * H0_SI), GD=G_DAGGER, ups=UPS_LST, UPS0=0.70,
           H0=float(H0_SI), c=C_SI, rho_n=2.702e17, nrar=len(RAR))
print('panel verisi: %d ETG (%d nokta) · disk RAR bulutu %d nokta'
      % (len(VER), 2 * len(VER), len(RAR)))
_r = [v['R']['0.70'][1] for v in VER]
print('yeniden kurulan dis yaricap (Y*=0,70): %.1f-%.1f kpc · farkli deger %d'
      % (min(_r), max(_r), len(set(np.round(_r, 3)))))
if KIRPILAN:
    print('UYARI: abundance matching tablosu disinda %d kayit KIRPILDI -> %s'
          % (len(KIRPILAN), ', '.join('%s(%.2e)' % k for k in KIRPILAN[:5])))

HTML = r"""<!doctype html><html lang="tr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Erken tip galaksi sınavı — etkileşimli panel</title><style>
*{box-sizing:border-box}
body{margin:0;background:#0d0d0f;color:#e4e4e7;font:14px/1.5 system-ui,Segoe UI,sans-serif}
h1{font-size:17px;margin:0 0 2px;font-weight:600}
.ust{padding:12px 16px;border-bottom:1px solid #27272a;display:flex;gap:16px;align-items:baseline;flex-wrap:wrap}
.ust .alt{color:#a1a1aa;font-size:12.5px}
.kap{display:grid;grid-template-columns:246px 1fr 330px;gap:14px;padding:14px 16px;align-items:start}
@media(max-width:1180px){.kap{grid-template-columns:1fr}}
.bl{background:#141417;border:1px solid #27272a;border-radius:8px;padding:11px}
.bl h2{font-size:12px;text-transform:uppercase;letter-spacing:.5px;color:#a1a1aa;margin:0 0 8px;font-weight:600}
button{font:inherit;cursor:pointer}
.gl{display:flex;flex-direction:column;gap:3px;max-height:32vh;overflow:auto}
.gl button{background:#1c1c21;border:1px solid #2f2f36;color:#d4d4d8;border-radius:5px;
  padding:4px 8px;text-align:left;font-size:12px;display:flex;justify-content:space-between;gap:6px}
.gl button:hover{background:#26262c}
.gl button.on{background:#166534;border-color:#22c55e;color:#fff}
.gl button i{font-style:normal;color:#71717a;font-size:11px;flex:none}
.gl button.on i{color:#bbf7d0}
.oyn{display:flex;gap:5px;margin-top:8px}
.oyn button{flex:1;background:#1c1c21;border:1px solid #2f2f36;color:#d4d4d8;border-radius:5px;padding:5px}
.oyn button:hover{background:#26262c}
canvas{width:100%;height:auto;display:block;background:#0d0d0f;border-radius:6px}
.cz{display:flex;flex-direction:column;gap:4px}
.cz label{display:flex;align-items:center;gap:7px;font-size:12.5px;cursor:pointer;padding:3px 5px;border-radius:4px}
.cz label:hover{background:#1c1c21}
.cz input{accent-color:#22c55e;width:14px;height:14px}
.sw{width:20px;height:3px;border-radius:2px;flex:none}
.sw.d{height:0;border-top:3px dashed currentColor}
.sw.p{height:0;border-top:3px dotted currentColor}
.sw.n{height:9px;width:9px;border-radius:50%;border:2px solid currentColor;background:none!important}
.sw.k{height:9px;width:9px;border-radius:2px;border:2px solid currentColor;background:none!important}
.seg{display:flex;flex-wrap:wrap;gap:4px;margin-bottom:9px}
.seg button{background:#1c1c21;border:1px solid #2f2f36;color:#a1a1aa;border-radius:5px;
  padding:4px 8px;font-size:12px}
.seg button.on{background:#1e3a5f;border-color:#3b82f6;color:#dbeafe;font-weight:600}
.seg button.uy.on{background:#7f1d1d;border-color:#ef4444;color:#fecaca}
.et{font-size:11px;color:#71717a;margin:0 0 4px}
table{width:100%;border-collapse:collapse;font-size:12px}
th,td{text-align:right;padding:3px 5px;border-bottom:1px solid #1f1f24}
th:first-child,td:first-child{text-align:left}
thead th{color:#a1a1aa;font-weight:600;font-size:11px}
.gr{font-size:12px}
.gr div{display:flex;justify-content:space-between;gap:8px;padding:3px 0;border-bottom:1px solid #1f1f24}
.gr span:first-child{color:#a1a1aa}
.gr b{font-weight:600;font-variant-numeric:tabular-nums}
.rz{font-size:9.5px;padding:1px 4px;border-radius:3px;margin-left:5px;vertical-align:middle;font-weight:700}
.rT{background:#166534;color:#bbf7d0}.rS{background:#78350f;color:#fde68a}
.rO{background:#1e3a5f;color:#bfdbfe}.rK{background:#4c1d95;color:#ddd6fe}
.dnk{font-size:12px;background:#0f1419;border:1px solid #1f2937;border-radius:6px;padding:8px;margin-top:8px;
  font-family:ui-monospace,Consolas,monospace;color:#93c5fd;line-height:1.7}
.not{font-size:11.5px;color:#71717a;margin-top:9px;line-height:1.5}
.uyari{font-size:11.5px;background:#2a1215;border:1px solid #7f1d1d;color:#fca5a5;border-radius:6px;
  padding:7px 9px;margin-top:8px;line-height:1.5}
.iyi{font-size:11.5px;background:#0f1f14;border:1px solid #166534;color:#86efac;border-radius:6px;
  padding:7px 9px;margin-top:8px;line-height:1.5}
input[type=range]{width:100%;accent-color:#22c55e}
.kz{color:#22c55e}.kk{color:#f87171}.ks{color:#fbbf24}
</style></head><body><div style="padding:9px 16px;background:rgba(34,197,94,0.10);border-bottom:1px solid #166534;color:#bbf7d0;font-size:12.5px;line-height:1.45"><strong style="font-size:14px;letter-spacing:.3px">SERBEST PARAMETRE (galaksi ba&#351;&#305;na): <span style="color:#4ade80">EVRENAKI&nbsp;0</span> &nbsp;&#183;&nbsp; &#923;CDM (fit)&nbsp;2</strong> &#8212; fit bu kar&#351;&#305;la&#351;t&#305;rmada teorinin de&#287;il, rakip modelin ihtiyac&#305;d&#305;r.<br>&#9889; <strong>Fitsizlik durumu:</strong> Teori hi&#231;bir fit de&#287;erine muhta&#231; de&#287;ildir; tek kalibre say&#305;n&#305;n (a&#8320;) da t&#252;retilmi&#351; kar&#351;&#305;l&#305;&#287;&#305; mevcuttur (M-45) ve yaln&#305;z stat&#252; disiplini gere&#287;i kalibre de&#287;er resm&#238; kullan&#305;mda tutulmaktad&#305;r. Bu paneldeki &#246;ng&#246;r&#252; e&#287;rilerinde galaksi ba&#351;&#305;na fitlenen hi&#231;bir say&#305; yoktur. &#214;ng&#246;r&#252; e&#287;rileri, M-47 penceresini i&#231;eren <strong>pencereli resm&#238; denklemle</strong> hesaplan&#305;r (W = min(1, a&#8320;/g<sub>kaps</sub>) &#8212; Rankine i&#231; kolu, parametresiz).</div>
<div class="ust"><h1>Erken tip galaksi sınavı — etkileşimli panel</h1>
<span class="alt">@@N@@ galaksi · 32 ivme noktası · <b>fit YAPILAMAZ</b> (2 nokta/galaksi) ·
arka planda @@NR@@ disk noktası · tek dosya, dış bağımlılık yok</span></div>
<div class="kap">
 <div class="bl"><h2>Teorinin öngörüsü</h2>
  <div class="dnk" style="margin-top:0">g<sub>öng</sub> = g<sub>bar</sub> + √(g<sub>bar</sub>·a₀)·W, &nbsp;W = min(1, a₀/g<sub>bar</sub>) — M-47</div>
  <p class="et" style="margin-top:6px">M-37 merkezcil dengesinde 𝒢M = g<sub>bar</sub>R²
  konunca <b>R sadeleşir</b>. Formülde ne yarıçap, ne Υ*, ne kütle var.
  g<sub>bar</sub> <b>ölçülen</b> büyüklüktür.</p>
  <h2 style="margin-top:12px">Nokta kümesi</h2>
  <div class="seg" id="sg_kume"></div>
  <h2 style="margin-top:12px">a₀ çarpanı</h2>
  <input type="range" id="sl" min="-0.30" max="0.62" step="0.005" value="0">
  <div style="display:flex;justify-content:space-between;font-size:11.5px;color:#a1a1aa">
   <span>×0,5</span><b id="sl_v" style="color:#e4e4e7">×1,00</b><span>×4,2</span></div>
  <div class="oyn"><button id="sl_1">a₀ = nihai değer</button><button id="sl_c">gereken çarpana git</button></div>
  <h2 style="margin-top:14px">Υ* (yalnız ΛCDM'i etkiler)</h2>
  <p class="et">ΛCDM yarıçabı Υ*'dan geri kurmak zorunda. Teori kurmuyor.
  Kaydırın: <b>mor</b> nokta bulutu oynar, <b>yeşil</b> eğri kıpırdamaz.</p>
  <div class="seg" id="sg_ups"></div>
  <div class="iyi" id="ups_not"></div>
 </div>
 <div class="bl"><h2 id="bas">—</h2><canvas id="cv" width="1180" height="720"></canvas>
  <table id="tb"><thead><tr><th>Kurulum</th><th>n</th><th>medyan dex</th>
   <th>saçılma</th><th>gereken a₀</th></tr></thead><tbody></tbody></table>
  <div class="not" id="dpn"></div>
  <div class="uyari" id="uy" style="display:none"></div>
 </div>
 <div class="bl"><h2>Çizgiler</h2><div class="cz" id="cz"></div>
  <h2 style="margin-top:14px">Galaksi</h2><div class="gl" id="gl"></div>
  <div class="oyn"><button id="geri">◀</button><button id="oyna">▶ Oynat</button><button id="ileri">▶</button></div>
  <h2 style="margin-top:14px">Seçili galaksinin girdileri</h2><div class="gr" id="grd"></div>
  <div class="dnk" id="dnk"></div>
  <h2 style="margin-top:14px">ΛCDM girdileri</h2><div class="gr" id="grl"></div>
  <div class="not"><b>Rozetler:</b> <span class="rz rT">T</span> teoriden türetilmiş ·
  <span class="rz rS">S</span> gözlemle sabitlenmiş · <span class="rz rO">Ö</span> yayınlanmış ölçüm ·
  <span class="rz rK">K</span> <b>yeniden kurulmuş</b> (ölçüm değil)
  <br><br>Bu panelde <b>hiçbir parametre fitlenemez</b> — galaksi başına 2 nokta, 0 serbestlik.
  <br><br>Klavye: ← → galaksi, boşluk oynat/durdur.</div>
 </div>
</div>
<script>
const V=@@VERI@@, S=@@SBT@@, RAR=@@RAR@@;
const CZ=[
 {k:'rar', ad:'disk RAR bulutu ('+S.nrar+' nokta)', c:'#52525b', t:'nokta', on:1},
 {k:'new', ad:'g_öng = g_bar (Newton)',             c:'#71717a', t:'nokta_c', on:1},
 {k:'amp', ad:'ampirik RAR — FİTLİ, 1 parametre (g†; rakip taraf)', c:'#f87171', t:'kesik', on:0},
 {k:'evr', ad:'EVRENAKI  g_bar+√(g_bar a₀)·W (M-47)',  c:'#16a34a', t:'kalin', on:1},
 {k:'evk', ad:'└ a₀ × (gereken çarpan — duyarlılık)',   c:'#4ade80', t:'kesik', on:0},
 {k:'dis', ad:'ETG dış nokta (HI halkası dışı)',    c:'#ffcc00', t:'', on:1},
 {k:'ic',  ad:'ETG iç nokta (HI halkası içi)',      c:'#fb923c', t:'k', on:1},
 {k:'lcd', ad:'ΛCDM zinciri (NFW, yarıçap kurulmuş)', c:'#a78bfa', t:'halka', on:1},
 {k:'bag', ad:'seçili galaksinin ölçüm↔öngörü bağı', c:'#f472b6', t:'ince', on:1}];
const KUME=[{k:2,ad:'ikisi (32)'},{k:1,ad:'yalnız dış (16)'},{k:0,ad:'yalnız iç (16)',uy:1}];

let i=0, acik={}, oto=null, kume=1, mult=1, ups='0.70';
CZ.forEach(x=>acik[x.k]=!!x.on);
const q=s=>document.querySelector(s), fx=(x,n)=>Number(x).toFixed(n).replace('.',',');
const us=x=>{if(x==null)return'—';const e=Math.floor(Math.log10(Math.abs(x)));
 return (x/Math.pow(10,e)).toFixed(2).replace('.',',')+'×10'+String(e).replace(/[0-9-]/g,
 d=>'⁰¹²³⁴⁵⁶⁷⁸⁹⁻'['0123456789-'.indexOf(d)]);};
const med=a=>{const b=[...a].sort((p,r)=>p-r),n=b.length;
 return n%2?b[(n-1)/2]:(b[n/2-1]+b[n/2])/2;};
const sd=a=>{const m=a.reduce((p,r)=>p+r,0)/a.length;
 return Math.sqrt(a.reduce((p,r)=>p+(r-m)*(r-m),0)/a.length);};

/* TEORI: F1 olceklenmez, yalniz F4 sqrt(k) ile olceklenir. */
const ongoru=(gb,k)=>gb+Math.sqrt(k*S.A0*gb)*Math.min(1,k*S.A0/gb);  /* M-47 penceresi */
/* F4'un ongoruye katkisi = gereken a_0'in KALDIRACI. Dusukse carpan okunmaz. */
const pay=gb=>Math.sqrt(S.A0*gb)*Math.min(1,S.A0/gb)/ongoru(gb,1);
/* ampirik RAR uyumu — Lelli+2017, g_dagger FITLENMISTIR (teorinin degil) */
const ampirik=gb=>gb/(1-Math.exp(-Math.sqrt(gb/S.GD)));

/* secili kumedeki (galaksi, nokta) ciftleri */
function noktalar(){const o=[];V.forEach((g,n)=>{
 if(kume!==0)o.push({g:g,j:1,n:n}); if(kume!==1)o.push({g:g,j:0,n:n});});return o;}

/* GEREKEN a_0 — kapali formul YOK, ikiye bolmeyle cozulur (btfr paneliyle ayni). */
function gereken(P){
 const f=k=>med(P.map(p=>Math.log10(ongoru(p.g.gb[p.j],k)/p.g.go[p.j])));
 let a=1e-3,b=1e3; if(f(a)>0||f(b)<0)return NaN;
 for(let t=0;t<80;t++){const m=Math.sqrt(a*b); if(f(m)<0)a=m; else b=m;}
 return Math.sqrt(a*b);}

/* disk RAR'i AYNI ivme araliginda olc — yoksa iki farkli rejim kiyaslanir */
function diskKesit(){
 const L=noktalar().map(p=>p.g.lgb[p.j]), lo=Math.min(...L), hi=Math.max(...L);
 return RAR.filter(r=>r[0]>=lo&&r[0]<=hi);}
function diskOlc(){const D=diskKesit();
 if(D.length<20)return null;
 const d=D.map(r=>Math.log10(ongoru(Math.pow(10,r[0]),mult)/Math.pow(10,r[1])));
 const f=k=>med(D.map(r=>Math.log10(ongoru(Math.pow(10,r[0]),k)/Math.pow(10,r[1]))));
 let a=1e-3,b=1e3,ge=NaN;
 if(f(a)<=0&&f(b)>=0){for(let t=0;t<80;t++){const m=Math.sqrt(a*b);if(f(m)<0)a=m;else b=m;}
  ge=Math.sqrt(a*b);}
 return {n:D.length, med:med(d), sd:sd(d), ge:ge};}

function seg(el,liste,secili,tik){el.innerHTML='';liste.forEach(o=>{
 const b=document.createElement('button');b.textContent=o.ad;
 b.className=(o.uy?'uy ':'')+(secili(o)?'on':'');
 b.onclick=()=>{tik(o);kur();ciz();};el.appendChild(b);});}
function kur(){
 seg(q('#sg_kume'),KUME,o=>o.k===kume,o=>kume=o.k);
 seg(q('#sg_ups'),S.ups.map(u=>({k:u.toFixed(2),ad:'Υ*='+u.toFixed(2).replace('.',',')})),
     o=>o.k===ups,o=>ups=o.k);
}
const cz=q('#cz');
CZ.forEach(x=>{const l=document.createElement('label');
 const st=x.t==='kesik'?'sw d':(x.t==='nokta_c'?'sw p':(x.t==='halka'?'sw n':
   (x.t==='k'?'sw k':'sw')));
 l.innerHTML='<input type="checkbox" '+(x.on?'checked':'')+'><span class="'+st+
  '" style="color:'+x.c+';background:'+(['kesik','nokta_c','halka','k'].includes(x.t)?'none':x.c)+
  '"></span>'+x.ad;
 l.querySelector('input').onchange=e=>{acik[x.k]=e.target.checked;ciz();};cz.appendChild(l);});

const gl=q('#gl');
function liste(){gl.innerHTML='';V.forEach((g,n)=>{const b=document.createElement('button');
 b.innerHTML='<span>'+g.ad+'</span><i>'+fx(g.L36/1e9,0)+'×10⁹ L☉</i>';
 b.onclick=()=>{i=n;ciz();};gl.appendChild(b);});}

q('#sl').oninput=e=>{mult=Math.pow(10,+e.target.value);ciz();};
q('#sl_1').onclick=()=>{mult=1;q('#sl').value=0;ciz();};
q('#sl_c').onclick=()=>{const k=gereken(noktalar());
 if(!isNaN(k)){mult=k;q('#sl').value=Math.max(-0.30,Math.min(0.62,Math.log10(k)));ciz();}};

function ciz(){
 liste();
 const g=V[i]; [...gl.children].forEach((b,n)=>b.className=n===i?'on':'');
 q('#sl_v').textContent='×'+fx(mult,2);
 const P=noktalar(), gerek=gereken(P), dk=diskOlc();
 const dtx=P.map(p=>Math.log10(ongoru(p.g.gb[p.j],mult)/p.g.go[p.j]));
 const dlc=P.map(p=>Math.log10((p.g.gb[p.j]+p.g.aDM[ups][p.j])/p.g.go[p.j]));

 q('#bas').textContent=g.ad+' · L=' +fx(g.L36/1e9,1)+'×10⁹ L☉ · R_eff='+fx(g.Reff,2)+
  ' kpc · D='+fx(g.D,1)+' Mpc  |  küme: '+KUME.find(k=>k.k===kume).ad;

 const cv=q('#cv'),x=cv.getContext('2d'),W=cv.width,H=cv.height,ml=72,mr=14,mt=14,mb=48;
 x.clearRect(0,0,W,H);
 let x0=-12.7,x1=-8.2,y0=-12.1,y1=-8.2;
 const X=v=>ml+(v-x0)/(x1-x0)*(W-ml-mr), Y=v=>H-mb-(v-y0)/(y1-y0)*(H-mt-mb);
 x.strokeStyle='#1f1f24';x.lineWidth=1;x.fillStyle='#71717a';x.font='12px system-ui';
 for(let v=-12.5;v<=y1;v+=.5){x.beginPath();x.moveTo(ml,Y(v));x.lineTo(W-mr,Y(v));
  x.stroke();x.textAlign='right';x.fillText(fx(v,1),ml-8,Y(v)+4);}
 for(let v=-12.5;v<=x1;v+=.5){x.beginPath();x.moveTo(X(v),mt);x.lineTo(X(v),H-mb);
  x.stroke();x.textAlign='center';x.fillText(fx(v,1),X(v),H-mb+18);}
 x.fillStyle='#a1a1aa';x.font='13px system-ui';
 x.fillText('log g_bar   (m/s²) — ölçülen baryonik ivme',(ml+W-mr)/2,H-12);
 x.save();x.translate(19,(mt+H-mb)/2);x.rotate(-Math.PI/2);x.textAlign='center';
 x.fillText('log g_obs   (m/s²)',0,0);x.restore();
 /* fit damgasi — grafik uzerinde, her zaman gorunur */
 x.font='600 13px system-ui';x.textAlign='left';
 x.fillStyle='#4ade80';x.fillText('EVRENAKI FİT: 0  (saf öngörü)',ml+10,mt+20);
 if(acik['amp']){x.fillStyle='#f87171';x.fillText('ampirik RAR: 1 fit parametresi (g†)',ml+10,mt+38);}

 /* disk bulutu — once, en altta */
 if(acik['rar']){x.fillStyle='rgba(120,120,130,.42)';
  RAR.forEach(r=>{x.fillRect(X(r[0])-.9,Y(r[1])-.9,1.8,1.8);});}
 /* secili kumenin ivme araligi — disk kesiti nerede olculuyor */
 if(acik['rar']&&dk){const L=P.map(p=>p.g.lgb[p.j]);
  x.fillStyle='rgba(255,204,0,.05)';
  x.fillRect(X(Math.min(...L)),mt,X(Math.max(...L))-X(Math.min(...L)),H-mt-mb);}

 const egri=(fn,c,dash,lw)=>{x.strokeStyle=c;x.lineWidth=lw||2.4;x.setLineDash(dash||[]);
  x.beginPath();for(let t=0;t<=240;t++){const lg=x0+(x1-x0)*t/240,v=Math.log10(fn(Math.pow(10,lg)));
   t?x.lineTo(X(lg),Y(v)):x.moveTo(X(lg),Y(v));}x.stroke();x.setLineDash([]);};
 if(acik['new'])egri(gb=>gb,'#71717a',[2,4],1.4);
 if(acik['amp'])egri(ampirik,'#f87171',[8,5],1.8);
 if(acik['evr'])egri(gb=>ongoru(gb,1),'#16a34a',[],2.6);
 if(acik['evk']&&!isNaN(gerek))egri(gb=>ongoru(gb,gerek),'#4ade80',[7,4],1.8);

 if(acik['lcd']){x.strokeStyle='#a78bfa';x.lineWidth=1.5;
  P.forEach(p=>{x.beginPath();
   x.arc(X(p.g.lgb[p.j]),Y(Math.log10(p.g.gb[p.j]+p.g.aDM[ups][p.j])),4,0,7);x.stroke();});}
 P.forEach(p=>{const dis=p.j===1; if(!acik[dis?'dis':'ic'])return;
  const cx=X(p.g.lgb[p.j]),cy=Y(p.g.lgo[p.j]),e=p.g.ego[p.j];
  x.strokeStyle=dis?'#ffcc00':'#fb923c';x.lineWidth=1.1;
  x.beginPath();x.moveTo(cx,Y(p.g.lgo[p.j]-e));x.lineTo(cx,Y(p.g.lgo[p.j]+e));x.stroke();
  if(dis){x.fillStyle='#ffcc00';x.beginPath();x.arc(cx,cy,4.4,0,7);x.fill();}
  else{x.lineWidth=1.7;x.strokeRect(cx-3.9,cy-3.9,7.8,7.8);}});

 if(acik['bag']){x.strokeStyle='#f472b6';x.lineWidth=1.6;
  [0,1].forEach(j=>{if(kume===1&&j===0)return; if(kume===0&&j===1)return;
   const cx=X(g.lgb[j]),a=Y(g.lgo[j]),b=Y(Math.log10(ongoru(g.gb[j],mult)));
   x.setLineDash([3,3]);x.beginPath();x.moveTo(cx,a);x.lineTo(cx,b);x.stroke();x.setLineDash([]);
   x.beginPath();x.arc(cx,a,8,0,7);x.stroke();
   x.fillStyle='#f472b6';x.font='11.5px system-ui';x.textAlign='left';
   x.fillText(g.ad+(j?' dış ':' iç ')+
    (b>a?'':'+')+fx(100*(ongoru(g.gb[j],mult)/g.go[j]-1),1)+'%',cx+11,(a+b)/2);});}

 /* ---- olcut tablosu ---- */
 const sat=[['EVRENAKI  g_bar+√(g_bar a₀)·W (M-47)',P.length,
   (med(dtx)<0?'':'+')+fx(med(dtx),3),fx(sd(dtx),3),
   isNaN(gerek)?'—':'×'+fx(gerek,2),1]];
 sat.push(['ΛCDM (Υ*='+ups.replace('.',',')+', yarıçap kurulmuş)',P.length,
   (med(dlc)<0?'':'+')+fx(med(dlc),3),fx(sd(dlc),3),'—',0]);
 if(dk)sat.push(['disk RAR — AYNI ivme aralığı',dk.n,
   (dk.med<0?'':'+')+fx(dk.med,3),fx(dk.sd,3),isNaN(dk.ge)?'—':'×'+fx(dk.ge,2),0]);
 q('#tb tbody').innerHTML=sat.map(r=>'<tr'+(r[5]?' style="color:#22c55e;font-weight:600"':'')+
  '>'+r.slice(0,5).map(c=>'<td>'+c+'</td>').join('')+'</tr>').join('');

 const mp=med(P.map(p=>pay(p.g.gb[p.j])));
 q('#dpn').innerHTML='Teorinin ivme açığı: <b class="'+(Math.abs(med(dtx))<.02?'kz':'kk')+'">'+
  (med(dtx)<0?'':'+')+fx(100*(Math.pow(10,med(dtx))-1),1)+'%</b>'+
  (dk?' · aynı ivme aralığındaki <b>'+dk.n+'</b> disk noktası <b>'+
   (dk.med<0?'':'+')+fx(100*(Math.pow(10,dk.med)-1),1)+'%</b> → fark <b class="'+
   (Math.abs(med(dtx)-dk.med)<.05?'kz':'ks')+'">'+fx(Math.abs(med(dtx)-dk.med),3)+' dex</b>':'')+
  '.<br>F4\'ün öngörüye katkısı (medyan): <b>'+fx(mp,2)+'</b> — '+
  (mp<0.25?'<b class="kk">düşük: gereken a₀ kötü koşullanmış, sayı olarak okunmamalı</b>':
   '<b class="kz">yeterli: gereken a₀ okunabilir</b>')+'.';

 const u=[];
 if(kume===0)u.push('<b>Yalnız iç nokta seçili.</b> Bu rejimde F4\'ün öngörüye katkısı '+
  'yaklaşık <b>%'+fx(100*mp,0)+'</b>\'dur; öngörünün neredeyse tamamı Newton terimidir. '+
  'a₀\'ın kaldıracı yoktur, <b>«gereken a₀» burada anlamlı bir sayı değildir</b> '+
  '(aynı sebeple disk RAR da bu aralıkta ×0,07 «istiyor»).');
 if(kume===2)u.push('İç ve dış noktalar <b>bağımsız değildir</b>: aynı galaksinin iki '+
  'noktası ortak mesafe, eğiklik ve fotometri hatası taşır. «32 nokta» 32 bağımsız '+
  'ölçüm <b>değildir</b>; asıl tablo iç/dış ayrımıdır.');
 if(Math.abs(mult-1)>.01)u.push('a₀ nihai değerin <b>×'+fx(mult,2)+
  '</b> katına alınmıştır. Bu bir <b>fit değil</b>; nihai değer ×1,00\'dir.');
 if(ups!=='0.70')u.push('Υ* varsayılan 0,70\'ten <b>'+ups.replace('.',',')+
  '</b>\'e alındı. Bu <b>yalnız ΛCDM\'i</b> etkiler (yarıçap ondan geri kurulur); '+
  'teorinin öngörüsü değişmedi çünkü g<sub>bar</sub> ölçülmüş bir büyüklüktür.');
 if(med(dlc)!==null&&Math.abs(med(dlc))<Math.abs(med(dtx))&&kume!==0)
  u.push('<b>Bu ayarda ΛCDM medyanda teoriden daha yakın</b> ('+
   fx(med(dlc),3)+' vs '+fx(med(dtx),3)+' dex). Sonuç silinmedi: teorinin tek '+
   'üstünlüğü burada <b>doğruluk değil sağlamlıktır</b> — Υ* kaydıracını oynatın, '+
   'ΛCDM oynar, teori oynamaz.');
 q('#uy').style.display=u.length?'block':'none';
 q('#uy').innerHTML=u.map(t=>'• '+t).join('<br><br>');

 const d0=V.map(v=>Math.log10((v.gb[1]+v.aDM['0.70'][1])/v.go[1])),
       dn=V.map(v=>Math.log10((v.gb[1]+v.aDM[ups][1])/v.go[1]));
 q('#ups_not').innerHTML='ΛCDM dış nokta medyanı: <b>'+(med(dn)<0?'':'+')+fx(med(dn),3)+
  ' dex</b> (Υ*=0,70\'te '+(med(d0)<0?'':'+')+fx(med(d0),3)+
  ') · TEORİ: <b>'+fx(med(V.map(v=>Math.log10(ongoru(v.gb[1],mult)/v.go[1]))),3)+
  ' dex — Υ*\'tan bağımsız</b>';

 /* ---- secili galaksinin girdileri ---- */
 const st=(a,b,r)=>'<div><span>'+a+(r?'<span class="rz r'+r+'">'+r+'</span>':'')+
  '</span><b>'+b+'</b></div>';
 const j=kume===0?0:1, etk=kume===0?'iç':'dış';
 q('#grd').innerHTML=
  st('𝒢 = α/ρ<sub>n</sub>', us(S.G)+' kpc(km/s)²/M☉','T')+
  st('a₀ = 1,75·cH₀/'+S.KATSAYI+(mult!==1?' × '+fx(mult,2):''), us(S.A0*mult)+' m/s²','S')+
  st('L[3,6]', us(g.L36)+' L☉','O')+
  st('R<sub>eff</sub>', fx(g.Reff,2)+' kpc','O')+
  st('eğiklik i', fx(g.inc,0)+'° ± '+fx(g.einc,0),'O')+
  st('g<sub>bar</sub> ('+etk+')', us(g.gb[j])+' m/s²','O')+
  st('g<sub>obs</sub> ('+etk+')', us(g.go[j])+' m/s² ± '+fx(g.ego[j],2)+' dex','O')+
  st('F4 = √(g<sub>bar</sub>·a₀)·W', us(Math.sqrt(mult*S.A0*g.gb[j])*Math.min(1,mult*S.A0/g.gb[j]))+' m/s²','T')+
  st('F4\'ün payı', fx(100*pay(g.gb[j]),0)+'%'+(pay(g.gb[j])<.25?' ⚠':''),'T')+
  '<div style="border-bottom:none;padding-top:6px"><span>öngörü / ölçüm</span><b>'+
   fx(Math.log10(ongoru(g.gb[j],mult)),2)+' / '+fx(g.lgo[j],2)+'  ('+
   (ongoru(g.gb[j],mult)<g.go[j]?'':'+')+
   fx(100*(ongoru(g.gb[j],mult)/g.go[j]-1),1)+'%)</b></div>';
 q('#dnk').innerHTML='g<sub>öng</sub> = g<sub>bar</sub> + √(g<sub>bar</sub>·a₀)·W'+
  '<br><span style="color:#71717a">R sadeleşti — yarıçap, Υ*, kütle YOK</span>';
 q('#grl').innerHTML=
  st('Υ* (seçili)', fx(+ups,2),'S')+
  st('M<sub>*</sub> = Υ*·L[3,6]', us(+ups*g.L36)+' M☉','K')+
  st('R = √(𝒢M<sub>*</sub>/g<sub>bar</sub>)', fx(g.R[ups][j],1)+' kpc = '+
     fx(g.R[ups][j]/g.Reff,1)+' R<sub>eff</sub>','K')+
  st('M₂₀₀ ← Moster+2013', us(g.M200[ups][j])+' M☉','S')+
  st('c₂₀₀ ← Dutton &amp; Macciò', fx(g.c200[ups][j],2),'S')+
  st('a<sub>DM</sub>(R)', us(g.aDM[ups][j])+' m/s²','K')+
  '<div style="border-bottom:none;padding-top:6px;color:#a1a1aa;font-size:11.5px">'+
  'Yarıçap <b>ölçülmedi, geri kuruldu</b> — küresel simetri varsayar ve gaz kütlesini '+
  'içermez. Teori bu adımı hiç kullanmaz.</div>';
}
q('#ileri').onclick=()=>{i=(i+1)%V.length;ciz();};
q('#geri').onclick=()=>{i=(i-1+V.length)%V.length;ciz();};
q('#oyna').onclick=e=>{if(oto){clearInterval(oto);oto=null;e.target.textContent='▶ Oynat';}
 else{oto=setInterval(()=>{i=(i+1)%V.length;ciz();},1100);e.target.textContent='⏸ Durdur';}};
addEventListener('keydown',e=>{
 if(e.key==='ArrowRight'){i=(i+1)%V.length;ciz();}
 else if(e.key==='ArrowLeft'){i=(i-1+V.length)%V.length;ciz();}
 else if(e.key===' '){e.preventDefault();q('#oyna').click();}});
kur();ciz();
</script></body></html>"""

HTML = (HTML.replace('@@VERI@@', json.dumps(VER, ensure_ascii=False))
        .replace('@@SBT@@', json.dumps(SBT, ensure_ascii=False))
        .replace('@@RAR@@', json.dumps(RAR))
        .replace('@@NR@@', str(len(RAR)))
        .replace('@@N@@', str(len(VER))))
yol = os.path.join(CIK, 'panel.html')
open(yol, 'w', encoding='utf-8').write(HTML)
print('-> 96_ETG/panel.html  (%.0f KB)' % (len(HTML) / 1024))
