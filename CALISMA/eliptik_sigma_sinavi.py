# -*- coding: utf-8 -*-
"""
ELIPTIK DIS-SIGMA SINAVI (G-12) — M-48 koprusunun ikinci bagimsiz-veri ailesi
(87_ETKIN_YASA is 16; [T-aday] -> [T] gecisinin son sinavi)

VERI: Forbes+ 2017 (AJ 153, 114; CDS J/AJ/153/114) — SLUGGS: 27 erken-tip galakside
      3573 kuresel-kume (GC) radyal hizi. SPARC'tan bagimsiz UCUNCU veri ailesi
      (dSph ve MIGHTEE'den sonra). Dosyalar: veri/_sluggs_gal.dat (table1),
      veri/_sluggs_gc.dat (table5, erratum-duzeltmeli) — degistirilmemis.

ONCEDEN YAZILAN KURALLAR (veriye bakilmadan):
 1) Ornek: table1'deki 27 galaksi; GC'ler table5'ten ad onekiyle eslestirilir,
    HRV=99 (olcumsuz) atilir. DIS bolge: R_gal > 2 R_eff (derin-rejim sinavi).
    ANA ornek: dis bolgede n_GC >= 15 olan galaksiler; 10<=n<15 olanlar rapor
    edilir, hukme girmez; n<10 sigma guvenilmez, yalniz CSV'de durur.
 2) Olculen sigma: dis bolgedeki GC'lerin V_sys (table1) etrafindaki rms'i
    (donme ayristirilmaz — toplam kinetik destek; alpha=2 konvansiyonuyla tutarli).
    3-sigma'lik tek gecisli ayiklama (aykiri/etkilesen komsu kacaklari icin);
    ayiklanan sayisi CSV'ye yazilir. Hata: sigma/sqrt(2n).
 3) M_bar = M* (logM*, table1 — katalogun kendi kurali, Forbes+2016 3.6um);
    ETG'de gaz ihmal (kayit). Ic-kutle profili: Hernquist, a = R_eff/1,8153;
    M(r) = M* r^2/(r+a)^2. r = dis GC'lerin medyan yaricapi (arcmin->kpc, Dist ile).
 4) Ongoru (M-48 Jeans, alpha=2 — dsph_sinavi.py ile BIREBIR ayni bicim):
       sigma_pred^2 = r*[g_bar + g_F4*W]/2
       g_bar = G M(r)/r^2;  g_F4 = sqrt(G M(r) a0)/r;  W = min(1, a0/g_bar)   [M-47]
    a0 ve butun sabitler SPARC degerlerinde DONMUS — sifir yeniden-kalibrasyon.
    EFE uygulanmaz: bunlar grup merkezlileri/alan galaksileri, g_ext << g_bar (kayit).
 5) OLCUTLER: (i) ana ornekte medyan log(sig_pred/sig_obs) ve sacilma;
    (ii) derin-limit FJ egimi: log sigma_obs ~ log M* dogrusal egim, beklenen 1/4'e karsi;
    (iii) yaricap-cozumlu ek tablo: n>=10'luk R/Reff kusaklarinda ayni oran.
 6) Duyarlilik (sonuca gore SECILMEZ, ikisi de rapor edilir): (a) Ups carpani x0,7
    (bizim kovan konvansiyonumuz, katalog Ups~1'e karsi); (b) dis esik 3 R_eff.
 7) Bu bir MERTEBE/ISARET sinavidir (alpha=2, izotropi, Hernquist, donme-dahil rms
    hepsi O(1)); [T] gecisi medyanin ~0,1 dex icinde olmasina ve sistematik egim
    olmamasina bakar.

Cikti: SINIF_CALISMASI/87_ETKIN_YASA/SONUC_ELIPTIK_SIGMA.csv
"""
import os, sys, io, csv, math, warnings
import numpy as np

warnings.filterwarnings('ignore')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

KOK = os.path.dirname(os.path.abspath(__file__))
G = 4.300917e-6
ACC = 1e6 / 3.0856776e19
A0 = 1.75 * 1.038 * (2.99792458e8 * (70e3 / 3.0857e22)) / ACC / 16.1   # pencereli resmi
ARCMIN_RAD = math.pi / 180.0 / 60.0

# ---- table1: galaksi ozellikleri (sabit-genislik, ReadMe bayt araliklari) ----
GALX = {}
for L in io.open(os.path.join(KOK, 'veri', '_sluggs_gal.dat'), encoding='utf-8'):
    if len(L) < 44:
        continue
    ngc = int(L[0:4]); dist = float(L[9:13]); lM = float(L[14:19])
    reff_as = float(L[20:25]); mtip = L[26:33].strip(); env = L[34:35]
    vsys = float(L[36:40]); sig1 = float(L[41:44])
    reff_kpc = dist * 1e3 * reff_as / 60.0 * ARCMIN_RAD
    GALX['NGC%d' % ngc] = dict(dist=dist, lM=lM, reff=reff_kpc, tip=mtip,
                               env=env, vsys=vsys, sig1=sig1)

# ---- table5: GC hizlari ----
GC = {k: [] for k in GALX}
for L in io.open(os.path.join(KOK, 'veri', '_sluggs_gc.dat'), encoding='utf-8'):
    if len(L) < 56:
        continue
    ad = L[0:14].strip().split('_')[0]
    try:
        hrv = float(L[37:41]); rg = float(L[55:61])
    except ValueError:
        continue
    if hrv == 99 or ad not in GALX:
        continue
    GC[ad].append((rg, hrv))

def hernquist_M(Mtot, r, reff):
    a = reff / 1.8153
    return Mtot * r * r / (r + a) ** 2

def sigma_pred(Mtot, reff, r, ups=1.0):
    M = ups * hernquist_M(Mtot, r, reff)
    gbar = G * M / r ** 2
    gF4 = math.sqrt(G * M * A0) / r
    W = min(1.0, A0 / gbar)
    return math.sqrt(r * (gbar + gF4 * W) / 2.0)

def dis_sigma(ad, esik):
    g = GALX[ad]
    reff_am = g['reff'] / (g['dist'] * 1e3 * ARCMIN_RAD)   # kpc -> arcmin
    dis = [(rg, v) for rg, v in GC[ad] if rg > esik * reff_am]
    n0 = len(dis)
    if n0 < 3:
        return None
    v = np.array([x[1] for x in dis]); rg = np.array([x[0] for x in dis])
    d = v - g['vsys']
    s = float(np.sqrt(np.mean(d ** 2)))
    kes = np.abs(d) <= 3 * s                              # tek gecisli 3-sigma
    v, rg = v[kes], rg[kes]
    n = len(v)
    sig = float(np.sqrt(np.mean((v - g['vsys']) ** 2)))
    rmed = float(np.median(rg)) * g['dist'] * 1e3 * ARCMIN_RAD
    return dict(n=n, atilan=n0 - n, sig=sig, esig=sig / math.sqrt(2 * n), rmed=rmed)

SAT, ANA = [], []
for ad in sorted(GALX, key=lambda k: -GALX[k]['lM']):
    g = GALX[ad]
    o = dis_sigma(ad, 2.0)
    if o is None:
        SAT.append([ad, g['tip'], '%.2f' % g['lM'], len(GC[ad]), 0, '', '', '', '', '', ''])
        continue
    Mtot = 10 ** g['lM']
    sp = sigma_pred(Mtot, g['reff'], o['rmed'])
    sp07 = sigma_pred(Mtot, g['reff'], o['rmed'], ups=0.7)
    d = math.log10(sp / o['sig'])
    gbar = G * hernquist_M(Mtot, o['rmed'], g['reff']) / o['rmed'] ** 2
    SAT.append([ad, g['tip'], '%.2f' % g['lM'], len(GC[ad]), o['n'],
                '%.1f' % o['rmed'], '%.1f' % (o['rmed'] / g['reff']),
                '%.1f±%.1f' % (o['sig'], o['esig']), '%.1f' % sp,
                '%+.3f' % d, '%.2f' % (gbar / A0)])
    if o['n'] >= 15:
        ANA.append(dict(ad=ad, lM=g['lM'], n=o['n'], sig=o['sig'], sp=sp, sp07=sp07,
                        d=d, d07=math.log10(sp07 / o['sig']), gb=gbar / A0,
                        rmed=o['rmed'], reff=g['reff']))

yol = os.path.join(KOK, 'SINIF_CALISMASI', '87_ETKIN_YASA', 'SONUC_ELIPTIK_SIGMA.csv')
with io.open(yol, 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(['galaksi', 'tip', 'logM*', 'nGC_top', 'nGC_dis(>2Reff,ayik)', 'r_med_kpc',
                'r/Reff', 'sigma_obs', 'sigma_pred', 'dex(pred/obs)', 'g_bar/a0'])
    for s in SAT:
        w.writerow(s)

D = np.array([a['d'] for a in ANA]); D07 = np.array([a['d07'] for a in ANA])
print('ANA ORNEK (dis n>=15): %d galaksi' % len(ANA))
print('  medyan log(pred/obs) = %+.3f dex · sacilma %.3f dex' % (np.median(D), np.std(D)))
print('  Ups x0,7 duyarliligi : %+.3f dex' % np.median(D07))
lm = np.array([a['lM'] for a in ANA]); ls = np.array([math.log10(a['sig']) for a in ANA])
eg = np.polyfit(lm, ls, 1)[0]
print('  FJ egimi (log sig_obs ~ log M*): %.3f  (derin-limit beklenti 0,25)' % eg)
art_eg = np.polyfit(lm, D, 1)[0]
print('  artik ~ logM* egimi: %+.3f (sistematik kontrol)' % art_eg)
gb = np.array([a['gb'] for a in ANA])
print('  g_bar/a0 araligi: %.2f - %.2f (derinlik kontrolu)' % (gb.min(), gb.max()))
print()
print('  %-8s %5s %3s %8s %8s %7s %6s' % ('galaksi', 'logM*', 'n', 'sig_obs', 'sig_pred', 'dex', 'gb/a0'))
for a in sorted(ANA, key=lambda x: -x['lM']):
    print('  %-8s %5.2f %3d %8.1f %8.1f %+7.3f %6.2f'
          % (a['ad'], a['lM'], a['n'], a['sig'], a['sp'], a['d'], a['gb']))

# duyarlilik: dis esik 3 Reff
D3 = []
for ad in GALX:
    o = dis_sigma(ad, 3.0)
    if o is None or o['n'] < 15:
        continue
    g = GALX[ad]
    D3.append(math.log10(sigma_pred(10 ** g['lM'], g['reff'], o['rmed']) / o['sig']))
print('\nDUYARLILIK esik 3Reff: n=%d · medyan %+.3f dex' % (len(D3), np.median(D3)))

# yaricap-cozumlu: ana-ornek galaksilerinde R/Reff kusaklari (kusak basina n>=10)
print('\nYARICAP-COZUMLU (ana ornek; kusak n>=10):')
KUS = [(2, 3), (3, 4), (4, 6), (6, 10)]
for k0, k1 in KUS:
    dd = []
    for a in ANA:
        g = GALX[a['ad']]
        reff_am = g['reff'] / (g['dist'] * 1e3 * ARCMIN_RAD)
        sec = [(rg, v) for rg, v in GC[a['ad']] if k0 * reff_am < rg <= k1 * reff_am]
        if len(sec) < 10:
            continue
        v = np.array([x[1] for x in sec]); rg = np.array([x[0] for x in sec])
        d0 = v - g['vsys']; s = float(np.sqrt(np.mean(d0 ** 2)))
        kes = np.abs(d0) <= 3 * s; v, rg = v[kes], rg[kes]
        sig = float(np.sqrt(np.mean((v - g['vsys']) ** 2)))
        rmed = float(np.median(rg)) * g['dist'] * 1e3 * ARCMIN_RAD
        dd.append(math.log10(sigma_pred(10 ** g['lM'], g['reff'], rmed) / sig))
    if dd:
        print('  %d-%d Reff : n_gal=%2d · medyan %+.3f dex' % (k0, k1, len(dd), np.median(dd)))
