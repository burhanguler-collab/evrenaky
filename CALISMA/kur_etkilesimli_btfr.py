# -*- coding: utf-8 -*-
"""BTFR icin etkilesimli panel (tek dosya, dis bagimlilik yok).

Sinif panellerinden FARKLI: orada galaksi basina bir egri vardi, burada tek
grafikte 121 galaksi var. O yuzden etkilesim SECIMLERI OYNATMAK uzerine kurulu —
bu dosyanin butun durustluk kayitlari birer dugmeye baglanmistir:

  1) V_bar okuma yaricapi: son nokta / bir iceri / dis yarinin ortasi   (md. 6.6)
  2) Hiz tanimi          : yedi tanim                                   (md. 5)
  3) W/2 duzeltmesi      : acik/kapali — cizgi genisligi tuzagi         (md. 5)
  4) a_0 carpani kaydiraci: x0,5 - x4 arasi, canli                      (md. 3)
  5) Gereken a_0          : SAYISAL cozulur (ikiye bolme)

Yani panel, secim degistikce hukmun nasil oynadigini gosterir. Kullanici
teorinin lehine de aleyhine de kiraz toplayabilir; ikisi de gorunur.

KALDIRILAN: v1'in 'yalniz F4 asimptot' kurulumu (v^4 = G M a_0) panelde YOKTUR.
O kurulum F1'i atiyordu; yanlis bir HESAPTI, teorinin bir ongorusu degildi ve
bir calisma aracinda tutulmasinin savunmasi yok. Hatanin kaydi silinmemistir:
SINIF_CALISMASI/97_BTFR/CALISMA.md'nin basindaki duzeltme kaydinda durur.
Ayni gerekcyle naif 10^(-4*fark) carpani da panelde gosterilmez; gereken a_0
her zaman sayisal cozulur. Bunlar yanlis hesaplar oldugu icin kaldirildi —
teorinin ALEYHINE olan DOGRU sonuclar (hiz acigi, gereken a_0, W/2 tuzagi,
normalizasyonda LCDM'in onde olusu) panelde AYNEN durur.

Cikti: SINIF_CALISMASI/97_BTFR/panel.html
"""

import os
import sys
import glob
import json
import warnings

import numpy as np

warnings.filterwarnings('ignore')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

KOK = os.path.dirname(os.path.abspath(__file__))
VERI = os.path.join(KOK, 'veri')
CIK = os.path.join(KOK, 'SINIF_CALISMASI', '97_BTFR')
os.makedirs(CIK, exist_ok=True)

G = 4.300917e-6
C_SI = 2.99792458e8
H0_SI = 70e3 / 3.0857e22
ACC = 1e6 / 3.0856776e19
CH0 = (C_SI * H0_SI) / ACC
KATSAYI = 16.1
A0_ESKI = CH0 / KATSAYI               # kitabin eski degeri (tarihsel)
# NIHAI KURULUM (karar: 86_NIHAI/CALISMA.md): a_0 = 1,75 x cH_0/16,1
A0 = 1.75 * 1.038 * A0_ESKI        # pencereli resmi kalibrasyon (M-47) = 7,67e-11 m/s^2
A0_SI = A0 * ACC
RHO_CRIT = 3 * 0.07 ** 2 / (8 * np.pi * G)
H_RED, RB, UPS = 0.7, 1.4, 0.50
TIPAD = {0: 'S0', 1: 'Sa', 2: 'Sab', 3: 'Sb', 4: 'Sbc', 5: 'Sc',
         6: 'Scd', 7: 'Sd', 8: 'Sdm', 9: 'Sm', 10: 'Im', 11: 'BCD'}


def mrt(yol, alan):
    """Son '----' ayiracindan sonrasini BELIRTEC tabanli okur.

    Sabit genislik KULLANILMAZ: SPARC .mrt dosyalarinda baslik bir bayt
    kayabiliyor ve sabit genislikli okuma sessizce yanlis sonuc veriyor.
    """
    ham = open(yol, encoding='utf-8', errors='replace').read().split('\n')
    a = [i for i, x in enumerate(ham) if x.startswith('----')][-1]
    D = {}
    for L in ham[a + 1:]:
        p = L.split()
        if len(p) < len(alan):
            continue
        try:
            D[p[0]] = {k: float(v) for k, v in zip(alan[1:], p[1:len(alan)])}
        except ValueError:
            continue
    return D


B = mrt(os.path.join(VERI, '_BTFR_Lelli2019.mrt'),
        ['Name', 'lMb', 'elMb', 'Inc', 'eInc', 'Vf', 'eVf', 'V2exp', 'eV2exp', 'V2eff',
         'eV2eff', 'Vmax', 'eVmax', 'Wp20', 'eWp20', 'Wm50', 'eWm50', 'Wm50c', 'eWm50c'])
K = mrt(os.path.join(VERI, '_sparc.mrt'),
        ['Name', 'T', 'D', 'eD', 'fD', 'Inc', 'eInc', 'L36', 'eL36', 'Reff', 'SBeff',
         'Rdisk', 'SBdisk', 'MHI', 'RHI', 'Vflat', 'eVflat', 'Q'])

ROT = {}
for f in sorted(glob.glob(os.path.join(VERI, '*_rotmod.dat'))):
    ad = os.path.basename(f)[:-11]
    d = np.loadtxt(f)
    if d.ndim < 2 or len(d) < 6:
        continue
    R, Vo, eV, Vg, Vd, Vb, SBd, SBb = [d[:, i] for i in range(8)]
    if np.any(R <= 0):
        continue
    ROT[ad] = dict(R=R, Vb2=np.sign(Vg) * Vg ** 2 + UPS * Vd ** 2 + RB * UPS * Vb ** 2)

_lM1, _N, _be, _ga = 11.59, 0.0351, 1.376, 0.608
_Mh = 10 ** np.linspace(9.0, 15.0, 8000)
_Ms = _Mh * 2 * _N / ((_Mh / 10 ** _lM1) ** -_be + (_Mh / 10 ** _lM1) ** _ga)
mu = lambda x: np.log(1 + x) - x / (1 + x)


KIRPILAN = []


def v_max_nfw(Ms, ad=''):
    """Ms (M_gunes) -> M_200 (abundance matching) -> c_200 -> NFW V_max.

    DIKKAT: np.interp tablo disindaki degeri SESSIZCE kirpar. Bu bir kez
    hataya yol acti (L[3.6] birimi 10^9 L_gunes'tir; 1e9 carpani atlanmisti,
    butun galaksiler tablonun alt sinirina kirpilip ayni V_max'i aldi).
    Artik kirpilan her galaksi kaydedilir ve ekrana basilir.
    """
    if Ms < _Ms[0] or Ms > _Ms[-1]:
        KIRPILAN.append((ad, Ms))
    M200 = float(np.interp(Ms, _Ms, _Mh))
    c = 10 ** (0.905 - 0.101 * np.log10(M200 * H_RED / 1e12))
    R200 = (3 * M200 / (4 * np.pi * 200 * RHO_CRIT)) ** (1 / 3.)
    return np.sqrt(G * M200 / R200) * np.sqrt(0.2162 * c / mu(c)), M200, c


# ---- veri paketi: her galaksi icin UC yaricapta V_bar ----
HIZ = ['Vf', 'V2exp', 'V2eff', 'Vmax', 'Wp20', 'Wm50', 'Wm50c']
VER = []
for n in sorted(B):
    if n not in ROT:
        continue
    r = ROT[n]
    idx = [-1, -2, len(r['R']) - max(1, len(r['R']) // 4) - 1]
    Mb = 10 ** B[n]['lMb']
    ka = K.get(n, {})
    L36 = ka.get('L36', 0.0) * 1e9      # SPARC birimi 10^9 L_gunes — 1e9 ZORUNLU
    Mstar = UPS * L36
    vm, M200, c200 = v_max_nfw(Mstar, n) if L36 > 0 else (None, None, None)
    VER.append(dict(
        ad=n, tip=TIPAD.get(int(ka.get('T', -1)), '?'), Q=int(ka.get('Q', 0)),
        D=ka.get('D', 0.0), inc=B[n]['Inc'], einc=B[n]['eInc'],
        lMb=B[n]['lMb'], elMb=B[n]['elMb'], Mb=Mb,
        v={k: B[n][k] for k in HIZ}, ev={k: B[n]['e' + k] for k in HIZ},
        R=[float(r['R'][j]) for j in idx],
        vb2=[float(max(r['Vb2'][j], 0.0)) for j in idx],
        Rout=float(r['R'][-1]), N=len(r['R']),
        lom=float(np.sqrt(G * Mb / A0)), F4=float(np.sqrt(G * Mb * A0)),
        L36=L36, Mstar=Mstar, Vmax_l=vm, M200_l=M200, c200_l=c200))

SBT = dict(n=len(VER), G=G, A0=float(A0), A0_SI=float(A0_SI), KATSAYI=KATSAYI,
           CH0_SI=float(CH0 * ACC), UPS=UPS, RB=RB, H0=float(H0_SI), c=C_SI,
           rho_n=2.702e17, hiz=HIZ)
print('panel verisi: %d galaksi (BTFR tablosu %d, rotmod eslesen)' % (len(VER), len(B)))
_vm = [g['Vmax_l'] for g in VER if g['Vmax_l']]
print('LCDM zinciri: %d galaksi · V_max %.0f-%.0f km/s · farkli deger sayisi %d'
      % (len(_vm), min(_vm), max(_vm), len(set(np.round(_vm, 3)))))
if KIRPILAN:
    print('UYARI: abundance matching tablosu disinda kalan %d galaksi KIRPILDI -> %s'
          % (len(KIRPILAN), ', '.join('%s(%.2e)' % k for k in KIRPILAN[:5])))
elif len(set(np.round(_vm, 3))) < len(_vm) * 0.9:
    print('UYARI: V_max degerleri beklenenden az cesitli — birim hatasi olabilir.')

HTML = r"""<!doctype html><html lang="tr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>BTFR sınavı — etkileşimli panel</title><style>
*{box-sizing:border-box}
body{margin:0;background:#0d0d0f;color:#e4e4e7;font:14px/1.5 system-ui,Segoe UI,sans-serif}
h1{font-size:17px;margin:0 0 2px;font-weight:600}
.ust{padding:12px 16px;border-bottom:1px solid #27272a;display:flex;gap:16px;align-items:baseline;flex-wrap:wrap}
.ust .alt{color:#a1a1aa;font-size:12.5px}
.kap{display:grid;grid-template-columns:236px 1fr 330px;gap:14px;padding:14px 16px;align-items:start}
@media(max-width:1180px){.kap{grid-template-columns:1fr}}
.bl{background:#141417;border:1px solid #27272a;border-radius:8px;padding:11px}
.bl h2{font-size:12px;text-transform:uppercase;letter-spacing:.5px;color:#a1a1aa;margin:0 0 8px;font-weight:600}
button{font:inherit;cursor:pointer}
.gl{display:flex;flex-direction:column;gap:3px;max-height:34vh;overflow:auto}
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
.rT{background:#166534;color:#bbf7d0}.rS{background:#78350f;color:#fde68a}.rO{background:#1e3a5f;color:#bfdbfe}
.dnk{font-size:12px;background:#0f1419;border:1px solid #1f2937;border-radius:6px;padding:8px;margin-top:8px;
  font-family:ui-monospace,Consolas,monospace;color:#93c5fd;line-height:1.7}
.not{font-size:11.5px;color:#71717a;margin-top:9px;line-height:1.5}
.uyari{font-size:11.5px;background:#2a1215;border:1px solid #7f1d1d;color:#fca5a5;border-radius:6px;
  padding:7px 9px;margin-top:8px;line-height:1.5}
input[type=range]{width:100%;accent-color:#22c55e}
.kz{color:#22c55e}.kk{color:#f87171}.ks{color:#fbbf24}
</style></head><body><div style="padding:9px 16px;background:rgba(34,197,94,0.10);border-bottom:1px solid #166534;color:#bbf7d0;font-size:12.5px;line-height:1.45"><strong style="font-size:14px;letter-spacing:.3px">SERBEST PARAMETRE (galaksi ba&#351;&#305;na): <span style="color:#4ade80">EVRENAKI&nbsp;0</span> &nbsp;&#183;&nbsp; &#923;CDM (fit)&nbsp;2</strong> &#8212; fit bu kar&#351;&#305;la&#351;t&#305;rmada teorinin de&#287;il, rakip modelin ihtiyac&#305;d&#305;r.<br>&#9889; <strong>Fitsizlik durumu:</strong> Teori hi&#231;bir fit de&#287;erine muhta&#231; de&#287;ildir; tek kalibre say&#305;n&#305;n (a&#8320;) da t&#252;retilmi&#351; kar&#351;&#305;l&#305;&#287;&#305; mevcuttur (M-45) ve yaln&#305;z stat&#252; disiplini gere&#287;i kalibre de&#287;er resm&#238; kullan&#305;mda tutulmaktad&#305;r. Bu paneldeki &#246;ng&#246;r&#252; e&#287;rilerinde galaksi ba&#351;&#305;na fitlenen hi&#231;bir say&#305; yoktur. &#214;ng&#246;r&#252; e&#287;rileri, M-47 penceresini i&#231;eren <strong>pencereli resm&#238; denklemle</strong> hesaplan&#305;r (W = min(1, a&#8320;/g<sub>kaps</sub>) &#8212; Rankine i&#231; kolu, parametresiz).</div>
<div class="ust"><h1>BTFR sınavı — etkileşimli panel</h1>
<span class="alt">@@N@@ galaksi · fit yok, iki taraf da sıfır serbest parametre ·
her seçim bir düğmeye bağlı · tek dosya, dış bağımlılık yok</span></div>
<div class="kap">
 <div class="bl"><h2>Kuvvet kurulumu</h2>
  <div class="dnk" style="margin-top:0">v² = V<sub>bar</sub>²(Υ*) + 𝒢·M<sub>bar</sub>/ℓ<sub>ω</sub></div>
  <p class="et" style="margin-top:6px">M-37 merkezcil dengesi <b>F1 (pulsasyon)</b> ve
  <b>F4 (eksenel)</b> terimlerini birden alır. Seçenek yok: teorinin radyal ivmesi budur.</p>
  <h2 style="margin-top:12px">V<sub>bar</sub> okuma yarıçapı</h2>
  <p class="et">F1 hangi noktadan okunuyor?</p>
  <div class="seg" id="sg_yar"></div>
  <h2 style="margin-top:12px">Hız tanımı</h2>
  <div class="seg" id="sg_hiz"></div>
  <div class="seg" id="sg_w"></div>
  <h2 style="margin-top:12px">a₀ çarpanı</h2>
  <input type="range" id="sl" min="-0.30" max="0.62" step="0.005" value="0">
  <div style="display:flex;justify-content:space-between;font-size:11.5px;color:#a1a1aa">
   <span>×0,5</span><b id="sl_v" style="color:#e4e4e7">×1,00</b><span>×4,2</span></div>
  <div class="oyn"><button id="sl_1">a₀ = nihai değer</button><button id="sl_c">gereken çarpana git</button></div>
 </div>
 <div class="bl"><h2 id="bas">—</h2><canvas id="cv" width="1180" height="700"></canvas>
  <table id="tb"><thead><tr><th>Kurulum</th><th>v<sub>öng</sub>/v<sub>ölç</sub></th>
   <th>saçılma</th><th>eğim</th><th>gereken a₀</th></tr></thead><tbody></tbody></table>
  <div class="not" id="dpn"></div>
  <div class="uyari" id="uy" style="display:none"></div>
 </div>
 <div class="bl"><h2>Çizgiler</h2><div class="cz" id="cz"></div>
  <h2 style="margin-top:14px">Galaksi</h2><div class="gl" id="gl"></div>
  <div class="oyn"><button id="geri">◀</button><button id="oyna">▶ Oynat</button><button id="ileri">▶</button></div>
  <h2 style="margin-top:14px">Seçili galaksinin girdileri</h2><div class="gr" id="grd"></div>
  <div class="dnk" id="dnk"></div>
  <div class="not"><b>Rozetler:</b> <span class="rz rT">T</span> teoriden türetilmiş ·
  <span class="rz rS">S</span> gözlemle sabitlenmiş (kalibre) · <span class="rz rO">Ö</span> yayınlanmış ölçüm
  <br><br>Bu panelde <b>hiçbir parametre fitlenmiyor.</b> Υ*=0,50 iki tarafta da aynıdır ve
  yayınlanmış M<sub>b</sub>'nin kendi değeridir (Lelli+2019, Not 1).
  <br><br>Klavye: ← → galaksi, boşluk oynat/durdur.</div>
  <h2 style="margin-top:14px">ΛCDM girdileri</h2><div class="gr" id="grl"></div>
 </div>
</div>
<script>
const V=@@VERI@@, S=@@SBT@@;
const CZ=[
 {k:'olc', ad:'ÖLÇÜM (hata çubuklu)',            c:'#ffcc00', t:'nokta', on:1},
 {k:'tam', ad:'EVRENAKI öngörüsü — galaksi başına', c:'#16a34a', t:'halka', on:1},
 {k:'tre', ad:'└ öngörünün eğilimi',              c:'#16a34a', t:'kalin', on:1},
  {k:'gfa', ad:'gözlenen fit (ağırlıklı)',         c:'#f87171', t:'kesik', on:1},
 {k:'gfz', ad:'gözlenen fit (ağırlıksız)',        c:'#fca5a5', t:'kesik', on:0},
 {k:'lcd', ad:'ΛCDM zinciri (NFW V_max)',         c:'#7c3aed', t:'nokta', on:1},
 {k:'bag', ad:'seçili galaksinin ölçüm↔öngörü bağı', c:'#f472b6', t:'ince', on:1}];
const YAR=[{k:0,ad:'son nokta'},{k:1,ad:'bir içerisi'},{k:2,ad:'dış yarının ortası'}];
const HAD={Vf:'V_f (düz)',V2exp:'V_2,2Rd',V2eff:'V_2Reff',Vmax:'V_max',
           Wp20:'HI W_p20',Wm50:'HI W_m50',Wm50c:'HI W_m50^c'};
let i=0, acik={}, oto=null, yar=0, hiz='Vf', w2=1, mult=1;
CZ.forEach(x=>acik[x.k]=!!x.on);
const q=s=>document.querySelector(s), fx=(x,n)=>Number(x).toFixed(n).replace('.',',');
const us=x=>{if(x==null)return'—';const e=Math.floor(Math.log10(Math.abs(x)));
 return (x/Math.pow(10,e)).toFixed(2).replace('.',',')+'×10'+String(e).replace(/[0-9-]/g,
 d=>'⁰¹²³⁴⁵⁶⁷⁸⁹⁻'['0123456789-'.indexOf(d)]);};
const med=a=>{const b=[...a].sort((p,r)=>p-r),n=b.length;
 return n%2?b[(n-1)/2]:(b[n/2-1]+b[n/2])/2;};
const sd=a=>{const m=a.reduce((p,r)=>p+r,0)/a.length;
 return Math.sqrt(a.reduce((p,r)=>p+(r-m)*(r-m),0)/a.length);};

/* ---- gecerli ornekleme: secili hiz tanimi olculmus VE hatasi var ---- */
function orn(){return V.filter(g=>g.v[hiz]>0&&g.ev[hiz]>0);}
/* olculen hiz: W tanimlarinda istege bagli W/2 duzeltmesi */
const vobs=g=>(hiz[0]==='W'&&w2)?g.v[hiz]/2:g.v[hiz];
/* Teorinin ongordugu hiz — M-37 merkezcil dengesi F1 ve F4'u BIRDEN alir.
    Tek kurulum vardir; secenek yok. (Yalniz-F4 asimptotik kurulum panelden
    KALDIRILDI: yanlis hesapti. Kayit: CALISMA.md duzeltme kaydi.) */
function vong(g,m){const gk=Math.max(g.vb2[yar],1e-9)/g.R[yar];      /* g_bar vekili, (km/s)^2/kpc */
 const Wp=Math.min(1, m*S.A0/gk);                                     /* M-47 penceresi */
 return Math.sqrt(g.vb2[yar]+Math.sqrt(m)*g.F4*Wp);}

/* dogrusal fit: y = a x + b  (w verilirse agirlikli) */
function fit(x,y,w){let sw=0,sx=0,sy=0,sxx=0,sxy=0;
 for(let j=0;j<x.length;j++){const q=w?w[j]:1;
  sw+=q;sx+=q*x[j];sy+=q*y[j];sxx+=q*x[j]*x[j];sxy+=q*x[j]*y[j];}
 const d=sw*sxx-sx*sx; return [(sw*sxy-sx*sy)/d,(sxx*sy-sx*sxy)/d];}

/* GEREKEN a_0 CARPANI — sayisal cozulur, formulle bulunmaz.
   a_0 -> k a_0 olunca F4 = sqrt(GM a_0) terimi sqrt(k) ile olceklenir ama
   V_bar^2 HIC olceklenmez. Naif 10^(-4*fark) formulu yalniz saf-F4
   asimptotunda dogrudur; TAM formulde ikiye bolme ile cozuyoruz. */
function gereken(gs){
 const f=m=>med(gs.map(g=>Math.log10(vong(g,m)/vobs(g))));
 let a=1e-3,b=1e3; if(f(a)>0||f(b)<0)return NaN;
 for(let t=0;t<80;t++){const m=Math.sqrt(a*b); if(f(m)<0)a=m; else b=m;}
 return Math.sqrt(a*b);}

/* ---- dugmeler ---- */
function seg(el,liste,secili,tik){el.innerHTML='';liste.forEach(o=>{
 const b=document.createElement('button');b.textContent=o.ad;
 b.className=(o.uy?'uy ':'')+(secili(o)?'on':'');
 b.onclick=()=>{tik(o);kur();ciz();};el.appendChild(b);});}
function kur(){
 seg(q('#sg_yar'),YAR,o=>o.k===yar,o=>yar=o.k);
 seg(q('#sg_hiz'),S.hiz.map(k=>({k:k,ad:HAD[k]})),o=>o.k===hiz,o=>hiz=o.k);
 q('#sg_w').innerHTML='';
 if(hiz[0]==='W'){const b=document.createElement('button');
  b.textContent=w2?'W/2 düzeltmesi AÇIK':'W/2 düzeltmesi KAPALI';
  b.className=w2?'on':'uy on';b.onclick=()=>{w2=1-w2;kur();ciz();};q('#sg_w').appendChild(b);}
 /* yaricap secimi asimptot kurulumunda anlamsiz — F1 yok */
}
const cz=q('#cz');
CZ.forEach(x=>{const l=document.createElement('label');
 const st=x.t==='kesik'?'sw d':(x.t==='nokta_c'?'sw p':(x.t==='halka'?'sw n':'sw'));
 l.innerHTML='<input type="checkbox" '+(x.on?'checked':'')+'><span class="'+st+
  '" style="color:'+x.c+';background:'+(['kesik','nokta_c','halka'].includes(x.t)?'none':x.c)+
  '"></span>'+x.ad;
 l.querySelector('input').onchange=e=>{acik[x.k]=e.target.checked;ciz();};cz.appendChild(l);});

const gl=q('#gl');
function liste(gs){gl.innerHTML='';gs.forEach((g,n)=>{const b=document.createElement('button');
 b.innerHTML='<span>'+g.ad+'</span><i>'+fx(vobs(g),0)+' km/s</i>';
 b.onclick=()=>{i=n;ciz();};gl.appendChild(b);});}

q('#sl').oninput=e=>{mult=Math.pow(10,+e.target.value);ciz();};
q('#sl_1').onclick=()=>{mult=1;q('#sl').value=0;ciz();};
q('#sl_c').onclick=()=>{const k=gereken(orn());
 if(!isNaN(k)){mult=k;q('#sl').value=Math.max(-0.30,Math.min(0.62,Math.log10(k)));ciz();}};

function ciz(){
 const gs=orn(); if(i>=gs.length)i=0;
 liste(gs);
 const g=gs[i];
 [...gl.children].forEach((b,n)=>b.className=n===i?'on':'');
 q('#sl_v').textContent='×'+fx(mult,2);

 const lv=gs.map(g=>Math.log10(vobs(g))), lm=gs.map(g=>g.lMb),
  wgt=gs.map(g=>1/Math.pow(Math.max(g.elMb,.02),2)),
  vt=gs.map(g=>vong(g,mult)), lt=vt.map(Math.log10),
  lcd=gs.filter(g=>g.Vmax_l), llc=lcd.map(g=>Math.log10(g.Vmax_l));
 const [ega,kga]=fit(lv,lm,wgt), [egz,kgz]=fit(lv,lm), [etr,ktr]=fit(lt,lm),
  [elc,klc]=lcd.length>2?fit(llc,lcd.map(g=>g.lMb)):[0,0];

 q('#bas').textContent=g.ad+' · '+g.tip+' · Q='+g.Q+' · N='+g.N+
  '  |  örneklem: '+gs.length+' galaksi ('+HAD[hiz]+
  (hiz[0]==='W'?(w2?', W/2':', HAM W'):'')+')';

 const cv=q('#cv'),x=cv.getContext('2d'),W=cv.width,H=cv.height,ml=70,mr=14,mt=14,mb=48;
 x.clearRect(0,0,W,H);
 /* eksen sinirlari CIZILEN her seriyi kapsar. Once yalniz ust sinir llc'yi
    iceriyordu; LCDM noktalari sol kenarin disina dusup GORUNMEZ olmustu. */
 const hep=[...lv,...lt].concat(acik['lcd']?llc:[]);
 let x0=Math.min(...hep)-.06, x1=Math.max(...hep)+.06,
     y0=Math.min(...lm)-.16, y1=Math.max(...lm)+.16;
 const X=v=>ml+(v-x0)/(x1-x0)*(W-ml-mr), Y=v=>H-mb-(v-y0)/(y1-y0)*(H-mt-mb);
 x.strokeStyle='#1f1f24';x.lineWidth=1;x.fillStyle='#71717a';x.font='12px system-ui';
 for(let v=Math.ceil(y0*5)/5;v<=y1;v+=.5){x.beginPath();x.moveTo(ml,Y(v));x.lineTo(W-mr,Y(v));
  x.stroke();x.textAlign='right';x.fillText(fx(v,1),ml-8,Y(v)+4);}
 for(let v=Math.ceil(x0*10)/10;v<=x1;v+=.2){x.beginPath();x.moveTo(X(v),mt);x.lineTo(X(v),H-mb);
  x.stroke();x.textAlign='center';x.fillText(fx(v,1),X(v),H-mb+18);}
 x.fillStyle='#a1a1aa';x.font='13px system-ui';
 x.fillText('log '+HAD[hiz]+'   (km/s)',(ml+W-mr)/2,H-12);
 x.save();x.translate(17,(mt+H-mb)/2);x.rotate(-Math.PI/2);x.textAlign='center';
 x.fillText('log M_bar   (M☉, Υ*=0,50)',0,0);x.restore();
 /* fit damgasi — grafik uzerinde, her zaman gorunur */
 x.font='600 13px system-ui';x.textAlign='left';
 x.fillStyle='#4ade80';x.fillText('EVRENAKI FİT: 0 — model fiti yok, iki taraf da öngörü',ml+10,mt+20);

 const dogru=(a,b,c,dash,lw)=>{x.strokeStyle=c;x.lineWidth=lw||1.9;x.setLineDash(dash||[]);
  x.beginPath();x.moveTo(X(x0),Y(a*x0+b));x.lineTo(X(x1),Y(a*x1+b));x.stroke();x.setLineDash([]);};
  if(acik['gfz'])dogru(egz,kgz,'#fca5a5',[7,5]);
 if(acik['gfa'])dogru(ega,kga,'#f87171',[7,5]);
 if(acik['tre'])dogru(etr,ktr,'#16a34a',[],2.3);
 if(acik['lcd']){x.fillStyle='#7c3aed';lcd.forEach((h,j)=>{x.beginPath();
  x.arc(X(llc[j]),Y(h.lMb),3.2,0,7);x.fill();});}
 if(acik['olc']){x.strokeStyle='#ffcc00';x.fillStyle='#ffcc00';x.lineWidth=1;
  gs.forEach((h,j)=>{const cx=X(lv[j]);
   x.beginPath();x.moveTo(cx,Y(h.lMb-h.elMb));x.lineTo(cx,Y(h.lMb+h.elMb));x.stroke();
   x.beginPath();x.arc(cx,Y(h.lMb),3.1,0,7);x.fill();});}
 if(acik['tam']){x.strokeStyle='#16a34a';x.lineWidth=1.4;
  gs.forEach((h,j)=>{const cx=X(lt[j]),cy=Y(h.lMb),r=3.6;
   x.beginPath();x.moveTo(cx,cy-r);x.lineTo(cx+r,cy);x.lineTo(cx,cy+r);x.lineTo(cx-r,cy);
   x.closePath();x.stroke();});}
 /* secili galaksi: olcum <-> ongoru bagi */
 if(acik['bag']){const cy=Y(g.lMb),a=X(Math.log10(vobs(g))),b=X(lt[i]);
  x.strokeStyle='#f472b6';x.lineWidth=1.6;x.setLineDash([3,3]);
  x.beginPath();x.moveTo(a,cy);x.lineTo(b,cy);x.stroke();x.setLineDash([]);
  x.beginPath();x.arc(a,cy,7,0,7);x.stroke();
  x.fillStyle='#f472b6';x.font='11.5px system-ui';x.textAlign=b<a?'right':'left';
  x.fillText(g.ad+'  '+(lt[i]<Math.log10(vobs(g))?'':'+')+
   fx(100*(vt[i]/vobs(g)-1),1)+'%',b+(b<a?-10:10),cy-8);}

 /* ---- olcut tablosu: iki kurulum yan yana, hangisi secili olursa olsun ---- */
 const sat=[];
 {const vv=gs.map(h=>vong(h,mult)), d=vv.map((v,j)=>Math.log10(v/vobs(gs[j]))),
   e=fit(vv.map(Math.log10),lm)[0], ge=gereken(gs);
  sat.push(['EVRENAKI  V_bar(F1) + F4',fx(Math.pow(10,med(d)),3),fx(sd(d),3),fx(e,3),
   isNaN(ge)?'—':'×'+fx(ge,2),true]);}
 sat.push(['GÖZLENEN (ağırlıklı)','1,000','—',fx(ega,3),'—',false]);
 sat.push(['GÖZLENEN (ağırlıksız)','1,000','—',fx(egz,3),'—',false]);
 if(lcd.length>2)sat.push(['ΛCDM zinciri','—','—',fx(elc,3),'—',false]);
 q('#tb tbody').innerHTML=sat.map(r=>'<tr'+(r[5]?' style="color:#22c55e;font-weight:600"':'')+
  '>'+r.slice(0,5).map((c,j)=>'<td>'+c+'</td>').join('')+'</tr>').join('');

 const dt=gs.map(h=>Math.log10(vong(h,mult)/vobs(h))), M=med(dt), coz=gereken(gs);
 q('#dpn').innerHTML='Teorinin hız açığı: <b class="'+(Math.abs(M)<.01?'kz':'kk')+'">'+
  (M<0?'':'+')+fx(100*(Math.pow(10,M)-1),1)+'%</b>. Eğim: teori <b>'+fx(fit(dt.map((d,j)=>lt[j]),lm)[0],3)+
  '</b>, gözlenen bandı <b>'+fx(Math.min(ega,egz),3)+'–'+fx(Math.max(ega,egz),3)+'</b>'+
  (fit(lt,lm)[0]>=Math.min(ega,egz)&&fit(lt,lm)[0]<=Math.max(ega,egz)?
   ' → <b class="kz">bandın içinde</b>':' → <b class="kk">bandın dışında</b>')+
  '.<br>Gereken a₀: <b>nihai değerin ×'+(isNaN(coz)?'—':fx(coz,2))+' katı</b> '+
  '<span style="color:#71717a">(sayısal çözüm; mutlak değer, kaydıraçtan bağımsız)</span>'+
  (Math.abs(mult-1)>=.01
   ? ' · kaydıraç ×'+fx(mult,2)+'\'de, <b>kalan</b> düzeltme ×'+fx(coz/mult,2)
   : '')+'.';

 /* ---- kurulum uyarilari ---- */
 const u=[];
 if(hiz[0]==='W'&&!w2)u.push('<b>W/2 düzeltmesi kapalı.</b> HI çizgi genişliği W≈2V'+
  '<sub>rot</sub>\'tur; ham W ile karşılaştırma kesimi 4log2=1,204 dex kaydırır. '+
  'Bu satırdaki çarpan <b>fizik değil tanım farkıdır</b> ve hiçbir yerde alıntılanmamalıdır.');
 if(hiz!=='Vf'&&hiz[0]!=='W')u.push('ℓ<sub>ω</sub> yasası kütlenin <b>tamamına</b> bağlıdır, '+
  'dolayısıyla fiziksel karşılığı dönüş eğrisinin <b>düz kısmıdır</b> (V<sub>f</sub>). '+
  'Bu tanım iç yarıçapları ölçer; sonuç teorinin lehine ya da aleyhine kayabilir.');
 if(yar!==0)u.push('V<sub>bar</sub> son ölçüm noktasından değil, <b>'+
  YAR[yar].ad+'nden</b> okunuyor. Raporlanan sonuç <b>son nokta</b> (teori için en kötü, '+
  'en muhafazakâr) seçimidir.');
 if(Math.abs(mult-1)>.01)u.push('a₀ nihai değerin (1,75·cH₀/16,1) <b>×'+fx(mult,2)+
  '</b> katına alınmıştır. Bu bir <b>fit değil</b>, ne kadar düzeltme gerektiğini '+
  'göstermek içindir; nihai değer ×1,00\'dir.');
 q('#uy').style.display=u.length?'block':'none';
 q('#uy').innerHTML=u.map(t=>'• '+t).join('<br><br>');

 /* ---- secili galaksinin girdileri ---- */
 const st=(a,b,r)=>'<div><span>'+a+(r?'<span class="rz r'+r+'">'+r+'</span>':'')+
  '</span><b>'+b+'</b></div>';
 const f4m=Math.sqrt(mult)*g.F4, pay=f4m/(g.vb2[yar]+f4m);
 q('#grd').innerHTML=
  st('𝒢 = α/ρ<sub>n</sub>', us(S.G)+' kpc(km/s)²/M☉','T')+
  st('a₀ = 1,75·cH₀/'+S.KATSAYI+(mult!==1?' × '+fx(mult,2):''), us(S.A0_SI*mult)+' m/s²','S')+
  st('Υ* (3,6 μm)', fx(S.UPS,2),'O')+
  st('M<sub>bar</sub> (Lelli+2019)', us(g.Mb)+' M☉','O')+
  st('V<sub>bar</sub> ('+YAR[yar].ad+', R='+fx(g.R[yar],2)+' kpc)',
     fx(Math.sqrt(g.vb2[yar]),1)+' km/s','O')+
  st('ℓ<sub>ω</sub> = √(𝒢M<sub>bar</sub>/a₀)', fx(g.lom/Math.sqrt(mult),2)+' kpc','T')+
  st('ℓ<sub>ω</sub>/R<sub>dış</sub>', fx(g.lom/Math.sqrt(mult)/g.Rout,2)+
     (g.lom/Math.sqrt(mult)>g.Rout?' ⚠':''),'T')+
  st('F4\'ün v² içindeki payı', fx(100*pay,0)+'%','T')+
  '<div style="border-bottom:none;padding-top:6px"><span>öngörü / ölçüm</span><b>'+
   fx(vt[i],1)+' / '+fx(vobs(g),1)+' km/s  ('+(vt[i]<vobs(g)?'':'+')+
   fx(100*(vt[i]/vobs(g)-1),1)+'%)</b></div>';
 q('#dnk').innerHTML='v² = V<sub>bar</sub>²(Υ*) + 𝒢·M<sub>bar</sub>/ℓ<sub>ω</sub>'+
  ' = V<sub>bar</sub>² + √(𝒢M<sub>bar</sub>a₀)·W, &nbsp;W = min(1, a₀/g<sub>bar</sub>) — M-47 penceresi (g<sub>kaps</sub> yerine g<sub>bar</sub> vekili)';
 q('#grl').innerHTML=g.Vmax_l
  ? st('Υ* (aynı girdi)', fx(S.UPS,2),'O')+
    st('M<sub>*</sub> = Υ*·L[3,6]', us(g.Mstar)+' M☉','O')+
    st('M₂₀₀ ← Moster+2013', us(g.M200_l)+' M☉','S')+
    st('c₂₀₀ ← Dutton &amp; Macciò', fx(g.c200_l,2),'S')+
    st('V<sub>max</sub><sup>NFW</sup>', fx(g.Vmax_l,1)+' km/s','T')+
    '<div style="border-bottom:none;padding-top:6px;color:#a1a1aa;font-size:11.5px">'+
    'ΛCDM BTFR\'yi analitik vermez; bu zincir en yakın karşılıktır, resmî bir öngörü değildir.</div>'
  : '<div style="border-bottom:none;color:#71717a">Bu galaksi için L[3,6] yok — zincir kurulamıyor.</div>';
}
q('#ileri').onclick=()=>{i=(i+1)%orn().length;ciz();};
q('#geri').onclick=()=>{const n=orn().length;i=(i-1+n)%n;ciz();};
q('#oyna').onclick=e=>{if(oto){clearInterval(oto);oto=null;e.target.textContent='▶ Oynat';}
 else{oto=setInterval(()=>{i=(i+1)%orn().length;ciz();},1100);e.target.textContent='⏸ Durdur';}};
addEventListener('keydown',e=>{
 if(e.key==='ArrowRight'){i=(i+1)%orn().length;ciz();}
 else if(e.key==='ArrowLeft'){const n=orn().length;i=(i-1+n)%n;ciz();}
 else if(e.key===' '){e.preventDefault();q('#oyna').click();}});
kur();ciz();
</script></body></html>"""

HTML = (HTML.replace('@@VERI@@', json.dumps(VER, ensure_ascii=False))
        .replace('@@SBT@@', json.dumps(SBT, ensure_ascii=False))
        .replace('@@N@@', str(len(VER))))
yol = os.path.join(CIK, 'panel.html')
open(yol, 'w', encoding='utf-8').write(HTML)
print('-> 97_BTFR/panel.html  (%.0f KB)' % (len(HTML) / 1024))
