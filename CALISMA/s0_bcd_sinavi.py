r"""S0 + BCD SINAVI — disklerin iki ucu, 8 galaksi.

--- BU DOSYA YENI FIT YAPMAZ ---
Sekiz galaksinin hesabi 99_KARMASIK'ta ZATEN yapilmisti; oraya "kendi Hubble
tipinde N<5, istatistik tasimaz" kuraliyla dusmuslerdi. Burada yalniz
AYRISTIRILIP okunuyorlar. Tek yeni hesap, gereken a_0 carpaninin SAYISAL
cozumu ve tipik ivme (ikisi de sinif_carpan_duzeltme.py ile ayni yontem).

--- NEDEN AYRI OKUMAYA DEGER ---
Bu iki tip orneklemın IKI UCUNDA oturur:
  S0  (mercek)      -> kadran baskin, YUKSEK ivme, F4 payi dusuk
  BCD (mavi tikiz cuce) -> gaz baskin, DUSUK ivme, F4 payi yuksek
Yani acik duran "carpan siniftan sinifa x1,47-3,76 degisiyor" sorusunun uc
noktalarini verirler. Ayrica S0'lar 96_ETG'nin erken tip sonucuyla dogrudan
karsilastirilabilir: ayni morfoloji, biri donus egrisiyle, oteki iki ivme
noktasiyla olculmus.

--- ORNEKLEM KALITESI ESIT DEGIL — RAPORUN OMURGASI BU ---
S0 (3): ucu de YALNIZ tip kuralindan dustu. Ikisi Q=1 (en yuksek kalite),
        N = 7, 17, 45. Temiz.
BCD (5): yalnizca NGC2915 temiz (N=30, Q=2). Ucu Q=3 (dusuk kalite),
        biri N=4 (egri sinanamaz). Yani BCD sonucu S0 sonucuyla AYNI
        agirlikta okunamaz ve oyle raporlanir.

Cikti: SINIF_CALISMASI/07_S0_BCD/ -> SONUC.csv · s0_bcd.png
"""

import os
import sys
import csv
import glob
import warnings

import numpy as np
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
plt.style.use('dark_background')

KOK = os.path.dirname(os.path.abspath(__file__))
SK = os.path.join(KOK, 'SINIF_CALISMASI')
KRM = os.path.join(SK, '99_KARMASIK')
CIK = os.path.join(SK, '07_S0_BCD')
os.makedirs(CIK, exist_ok=True)

# ---- sabitler: sinif_ongoru_vs_fit.py ile BIREBIR ayni ----
G = 4.300917e-6
C_SI = 2.99792458e8
ACC = 1e6 / 3.0856776e19
A0_ESKI = (C_SI * (70e3 / 3.0857e22)) / ACC / 16.1
# NIHAI KURULUM (86_NIHAI): yerel l_omega + a_0 x1,75 — SONUC.csv de nihai
A0 = 1.75 * A0_ESKI
RB, UPS = 1.4, 0.50
PAY_ESIK = 0.25
mu = lambda x: np.log(1 + x) - x / (1 + x)
RHO_CRIT = 3 * 0.07 ** 2 / (8 * np.pi * G)


def v_nfw2(R, M200, c200):
    r200 = (3 * M200 / (4 * np.pi * 200 * RHO_CRIT)) ** (1 / 3.0)
    return G * M200 / R * mu(R * c200 / r200) / mu(c200)


def carpan(vb2, f4, vo):
    """mean((v_ong - v_olc)/v_olc) = 0 kokunu ikiye bolmeyle cozer.
    sinif_carpan_duzeltme.py ile AYNI tanim (oranlarin ortalamasi)."""
    fk = lambda k: float(np.mean((np.sqrt(np.maximum(vb2 + np.sqrt(k) * f4, 1e-9))
                                  - vo) / vo))
    a, b = 1e-4, 1e4
    if fk(a) > 0 or fk(b) < 0:
        return np.nan
    for _ in range(200):
        m = np.sqrt(a * b)
        if fk(m) < 0:
            a = m
        else:
            b = m
    return np.sqrt(a * b)


# ---------------------------------------------------------------- veri
GER = {x['Galaksi']: x for x in csv.DictReader(open(os.path.join(KRM, 'GEREKCE.csv'),
                                                    encoding='utf-8'))}
SON = {x['Galaksi']: x for x in csv.DictReader(open(os.path.join(KRM, 'HESAP', 'SONUC.csv'),
                                                    encoding='utf-8'))}
KAT = {x['Galaksi']: x for x in csv.DictReader(open(os.path.join(KRM, 'KATALOG.csv'),
                                                    encoding='utf-8'))}
SEC = sorted([a for a, g in GER.items() if g['Tip'] in ('S0', 'BCD')],
             key=lambda a: (GER[a]['Tip'] != 'S0', a))
print('S0+BCD: %d galaksi (99_KARMASIK icinden ayristirildi)' % len(SEC))

f = lambda x, k: float(x[k]) if x.get(k) else np.nan
GAL, EN_KOTU = [], 0.0
for ad in SEC:
    yol = os.path.join(KRM, 'veri', ad + '_rotmod.dat')
    d = np.loadtxt(yol)
    R, Vo, eV, Vg, Vd, Vb, SBd, SBb = [d[:, i] for i in range(8)]
    eV = np.maximum(eV, 1.0)
    Rp = R * 1e3
    L = lambda S: np.concatenate([[0.0], np.cumsum(
        np.pi * (Rp[1:] ** 2 - Rp[:-1] ** 2) * 0.5 * (S[1:] + S[:-1]))])
    Vbar2 = np.sign(Vg) * Vg ** 2 + UPS * Vd ** 2 + RB * UPS * Vb ** 2
    Mgas = np.maximum(R * np.sign(Vg) * Vg ** 2 / G, 0.0)
    Mkaps = UPS * L(SBd) + RB * UPS * L(SBb) + Mgas
    lom = np.sqrt(G * max(Mkaps[-1], 1e-6) / A0)          # rapor kolonu
    F4 = np.sqrt(A0 * G * np.maximum(Mkaps, 1e-9))        # NIHAI: yerel
    v_evr = np.sqrt(np.maximum(Vbar2, 1e-9) + F4)
    s = SON[ad]
    v_lcd = np.sqrt(np.maximum(Vbar2, 1e-9) +
                    v_nfw2(R, f(s, 'ONG_lcdm_M200_Msun'), f(s, 'ONG_lcdm_c200')))
    m = R > np.median(R)                                   # dis yari — kayitla ayni
    sap = 100 * float(np.mean((v_evr[m] - Vo[m]) / Vo[m]))
    ref = f(s, 'DIS_evr_sapma_yuzde')
    EN_KOTU = max(EN_KOTU, abs(sap - ref))
    GAL.append(dict(
        ad=ad, tip=GER[ad]['Tip'], N=len(R), Q=int(GER[ad]['Q']),
        gerekce=GER[ad]['Gerekce'], R=R, Vo=Vo, eV=eV,
        vbar=np.sqrt(np.maximum(Vbar2, 0)), v_evr=v_evr, v_lcd=v_lcd,
        k=carpan(Vbar2[m], F4[m], Vo[m]),
        pay=float(np.median(F4[m] / np.maximum(Vbar2[m] + F4[m], 1e-9))),
        gb_dis=Vbar2[-1] / R[-1] * ACC,
        gb_med=float(np.median(Vbar2 / R)) * ACC,
        sap=ref, lom=lom, L36=float(KAT[ad]['L36_1e9Lsun']),
        rms_e=f(s, 'ONG_evr_rms'), rms_l=f(s, 'ONG_lcdm_rms'),
        ci_e=f(s, 'ONG_evr_chi2ind'), ci_l=f(s, 'ONG_lcdm_chi2ind'),
        ic_e=f(s, 'ONG_evr_hataici'), ic_l=f(s, 'ONG_lcdm_hataici'),
        ye=f(s, 'FIT_evr_Ystar'), yl=f(s, 'FIT_lcdm_Ystar'),
        temiz=('Q=3' not in GER[ad]['Gerekce'] and 'nokta' not in GER[ad]['Gerekce'])))
print('OZ DENETIM — kayitli DIS_evr_sapma_yuzde: en buyuk fark %.3f puan -> %s'
      % (EN_KOTU, 'GECTI' if EN_KOTU < 0.06 else 'KALDI'))
if EN_KOTU >= 0.06:
    raise SystemExit('oz denetim basarisiz.')

def KG(k):
    """Carpani yazdirir. Dip sinira dayanan deger SAYI gibi gosterilmez."""
    if not np.isfinite(k):
        return 'çözülemedi'
    return '<0,01' if k < 0.01 else ('×%.2f' % k).replace('.', ',')


S0 = [g for g in GAL if g['tip'] == 'S0']
BC = [g for g in GAL if g['tip'] == 'BCD']

print('\n' + '=' * 100)
print('GALAKSI GALAKSI  (fit yok; carpan sayisal cozum)')
print('  %-10s %-4s %3s %2s %8s %8s %8s %8s %9s %7s'
      % ('galaksi', 'tip', 'N', 'Q', 'RMS_E', 'RMS_L', 'sapma%', 'F4 payi',
         'carpan', 'temiz'))
for g in GAL:
    print('  %-10s %-4s %3d %2d %8.1f %8.1f %+8.1f %8.2f %8.2fx %7s'
          % (g['ad'], g['tip'], g['N'], g['Q'], g['rms_e'], g['rms_l'],
             g['sap'], g['pay'], g['k'], 'evet' if g['temiz'] else 'HAYIR'))

print('\n' + '=' * 100)
print('TIP OZETI')
print('  %-16s %3s %9s %9s %9s %10s %14s'
      % ('tip', 'n', 'RMS_E', 'RMS_L', 'F4 payi', 'carpan', 'log g_bar dis'))
OZ = []
for ad, L in [('S0 (mercek)', S0), ('BCD (tikiz cuce)', BC),
              ('BCD — yalniz temiz', [g for g in BC if g['temiz']])]:
    if not L:
        continue
    d = dict(ad=ad, n=len(L), rms_e=np.median([g['rms_e'] for g in L]),
             rms_l=np.median([g['rms_l'] for g in L]),
             pay=np.median([g['pay'] for g in L]),
             k=np.median([g['k'] for g in L]),
             gbd=np.median([g['gb_dis'] for g in L]),
             gbm=np.median([g['gb_med'] for g in L]))
    OZ.append(d)
    print('  %-16s %3d %9.1f %9.1f %9.2f %9.2fx %14.2f'
          % (ad, d['n'], d['rms_e'], d['rms_l'], d['pay'], d['k'], np.log10(d['gbd'])))

# ---- alti sinifla karsilastirma ----
DYOL = os.path.join(SK, '_HESAPLAR', 'sinif_carpan_duzeltme.csv')
SINIF = []
if os.path.exists(DYOL):
    D = list(csv.DictReader(open(DYOL, encoding='utf-8')))
    ads = []
    for x in D:
        if x['Sinif'] not in ads:
            ads.append(x['Sinif'])
    for a in ads:
        v = [x for x in D if x['Sinif'] == a and x['carpan_DOGRU_sayisal']]
        SINIF.append(dict(ad=a, n=len(v),
                          k=float(np.median([float(x['carpan_DOGRU_sayisal']) for x in v])),
                          gbd=float(np.median([float(x['g_bar_dis_nokta_ms2']) for x in v]))))
    print('\n' + '=' * 100)
    print('ALTI SINIFLA BIRLIKTE — acik duran carpan sacilmasinin UC NOKTALARI')
    print('  %-18s %4s %10s %14s' % ('sinif/tip', 'n', 'carpan', 'log g_bar dis'))
    for s in SINIF:
        print('  %-18s %4d %9.2fx %14.2f' % (s['ad'], s['n'], s['k'], np.log10(s['gbd'])))
    for d in OZ[:2]:
        print('  %-18s %4d %9.2fx %14.2f  <- BU SINAV'
              % (d['ad'], d['n'], d['k'], np.log10(d['gbd'])))
    tk = [s['k'] for s in SINIF] + [d['k'] for d in OZ[:2]]
    print('\n  Band alti sinifta x%.2f-%.2f idi; S0+BCD eklenince x%.2f-%.2f (%.1f kat).'
          % (min(s['k'] for s in SINIF), max(s['k'] for s in SINIF),
             min(tk), max(tk), max(tk) / min(tk)))

# ------------------------------------------------------------ SONUC.csv
with open(os.path.join(CIK, 'SONUC.csv'), 'w', encoding='utf-8', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['Galaksi', 'Tip', 'N', 'Q', 'temiz_ornek', '99_KARMASIK_gerekcesi',
                'L36_1e9Lsun', 'ONG_evr_rms', 'ONG_lcdm_rms', 'ONG_evr_chi2ind',
                'ONG_lcdm_chi2ind', 'ONG_evr_hataici', 'ONG_lcdm_hataici',
                'FIT_evr_Ystar', 'FIT_lcdm_Ystar', 'DIS_evr_sapma_yuzde',
                'F4_payi', 'carpan_DOGRU_sayisal', 'l_omega_kpc',
                'g_bar_dis_nokta_ms2', 'g_bar_medyan_ms2'])
    for g in GAL:
        w.writerow([g['ad'], g['tip'], g['N'], g['Q'],
                    'evet' if g['temiz'] else 'HAYIR', g['gerekce'],
                    '%.3f' % g['L36'], '%.2f' % g['rms_e'], '%.2f' % g['rms_l'],
                    '%.3f' % g['ci_e'], '%.3f' % g['ci_l'],
                    '%.2f' % g['ic_e'], '%.2f' % g['ic_l'],
                    '' if np.isnan(g['ye']) else '%.3f' % g['ye'],
                    '' if np.isnan(g['yl']) else '%.3f' % g['yl'],
                    '%+.1f' % g['sap'], '%.3f' % g['pay'], '%.4f' % g['k'],
                    '%.2f' % g['lom'], '%.3e' % g['gb_dis'], '%.3e' % g['gb_med']])

# ---------------------------------------------------------------- grafik
fig = plt.figure(figsize=(16.6, 9.8), facecolor='#121212')
gs = fig.add_gridspec(3, 4, height_ratios=[1, 1, 1.35], hspace=.42, wspace=.24)
for i, g in enumerate(GAL):
    a = fig.add_subplot(gs[i // 4, i % 4])
    a.set_facecolor('#121212'); a.grid(alpha=.12)
    a.errorbar(g['R'], g['Vo'], yerr=g['eV'], fmt='o', color='#ffcc00', ms=3.2,
               elinewidth=.8, capsize=0, zorder=5)
    a.plot(g['R'], g['vbar'], ':', color='#71717a', lw=1.3, zorder=2)
    a.plot(g['R'], g['v_lcd'], '--', color='#7c3aed', lw=1.5, zorder=3)
    a.plot(g['R'], g['v_evr'], '-', color='#16a34a', lw=2.0, zorder=4)
    ren = '#22c55e' if g['tip'] == 'S0' else '#fb923c'
    a.set_title('%s · %s%s' % (g['ad'], g['tip'], '' if g['temiz'] else '  (!)'),
                fontsize=9.6, color=ren, pad=4)
    a.text(.04, .95, 'N=%d Q=%d\n%s' % (g['N'], g['Q'], KG(g['k'])),
           transform=a.transAxes, va='top', fontsize=7.8, color='#a1a1aa',
           family='monospace')
    a.tick_params(labelsize=7.5)
    if i % 4 == 0:
        a.set_ylabel('V (km/s)', fontsize=8.5)
    a.set_xlabel('R (kpc)', fontsize=8.3, labelpad=1)

a3 = fig.add_subplot(gs[2, :2]); a4 = fig.add_subplot(gs[2, 2:])
for a in (a3, a4):
    a.set_facecolor('#121212'); a.grid(alpha=.13)

# --- carpan vs ivme.  Eksen 1-32 ile SINIRLI: PGC51017 (x0,00) disarida kalir
#     ve ok ile isaretlenir. Onu eksene sokmak dort decade acar, hicbir sey
#     okunmaz; silmek de dogru degil — o yuzden gorunur bicimde DISARIDA.
YLO, YHI = 0.9, 34.0
if SINIF:
    a3.plot([np.log10(s['gbd']) for s in SINIF], [s['k'] for s in SINIF], 'o',
            color='#a1a1aa', ms=10, zorder=4, label='altı morfolojik sınıf (141 gal.)')
    for s in SINIF:
        a3.annotate(s['ad'], (np.log10(s['gbd']), s['k']), fontsize=7.6,
                    color='#d4d4d8', xytext=(0, 9), textcoords='offset points',
                    ha='center')
for g in GAL:
    y = g['k']
    ren = '#22c55e' if g['tip'] == 'S0' else '#fb923c'
    if not np.isfinite(y) or y < YLO:
        a3.annotate('', (np.log10(g['gb_dis']), YLO * 1.35),
                    xytext=(np.log10(g['gb_dis']), YLO * 3.0),
                    arrowprops=dict(arrowstyle='-|>', color=ren, lw=1.5))
        a3.text(np.log10(g['gb_dis']), YLO * 3.4, '%s\n%s' % (g['ad'], KG(y)),
                fontsize=7.2, color=ren, ha='center', va='bottom')
        continue
    a3.plot(np.log10(g['gb_dis']), min(y, YHI * .97), '.', ms=8, color=ren,
            alpha=.7, zorder=5)
for d, ren, mk in [(OZ[0], '#22c55e', 's'), (OZ[1], '#fb923c', 'D')]:
    a3.plot(np.log10(d['gbd']), d['k'], mk, color=ren, ms=14, zorder=6,
            mec='white', mew=1.2,
            label='%s medyanı (n=%d) ← bu sınav' % (d['ad'], d['n']))
a3.axhline(2.21, color='#4ade80', ls='--', lw=1.4, zorder=2,
           label='141 galaksinin medyanı ×2,21')
a3.axhspan(1.47, 3.76, color='#a1a1aa', alpha=.12, zorder=1)
a3.set_yscale('log'); a3.set_ylim(YLO, YHI)
a3.set_yticks([1, 2, 3, 5, 10, 20, 30])
a3.set_yticklabels(['1', '2', '3', '5', '10', '20', '30'])
a3.set_xlabel('$\log g_{bar}$ (dış nokta, m/s²)', fontsize=10)
a3.set_ylabel('gereken $a_0$ çarpanı', fontsize=10)
a3.set_title('Açık duran çarpan saçılmasının uç noktaları', fontsize=11.8,
             color='white', pad=8)
a3.legend(fontsize=8.0, framealpha=.35, loc='upper center', ncol=2)
a3.text(.015, .04, 'gri bant = altı sınıfın bandı ×1,47–3,76',
        transform=a3.transAxes, fontsize=8.4, color='#a1a1aa')

x = np.arange(len(GAL))
a4.bar(x - .2, [g['rms_e'] for g in GAL], .38, color='#16a34a', zorder=4,
       label='Evrenakı öngörüsü')
a4.bar(x + .2, [g['rms_l'] for g in GAL], .38, color='#7c3aed', zorder=4,
       label='ΛCDM öngörüsü')
a4.set_xticks(x)
a4.set_xticklabels(['%s\n%s%s' % (g['ad'], g['tip'], '' if g['temiz'] else ' (!)')
                    for g in GAL], fontsize=7.2)
a4.set_ylabel('öngörü RMS (km/s)', fontsize=10)
a4.set_title('Öngörü yarışı — fit yok, iki tarafta da sıfır parametre',
             fontsize=11.8, color='white', pad=8)
a4.legend(fontsize=8.6, framealpha=.3, loc='upper center')
oe = sum(1 for g in GAL if g['rms_e'] < g['rms_l'])
a4.text(.985, .95, 'Evrenakı %d/%d galakside önde' % (oe, len(GAL)),
        transform=a4.transAxes, ha='right', va='top', fontsize=9.6,
        color='#f87171' if oe < len(GAL) / 2 else '#4ade80', family='monospace')

fig.suptitle('S0 + BCD — disklerin iki ucu · 8 galaksi, yeni fit yok',
             fontsize=14.5, color='white', y=.978)
fig.text(.5, .048, "Bu sekiz galaksi 99_KARMASIK'ta «kendi Hubble tipinde $N<5$» kuralıyla "
                   'bekliyordu; hesapları orada yapılmıştı, burada yalnız ayrıştırıldı. '
                   'Yeşil düz = Evrenakı · mor kesik = ΛCDM · gri nokta = yalnız baryonlar · '
                   'sarı = ölçüm.', ha='center', fontsize=9.2, color='#a1a1aa')
fig.text(.5, .015, "(!) = örneklem temiz değil (SPARC $Q=3$ ya da $N<6$). S0'ların üçü de temiz "
                   "ve ikisi $Q=1$; BCD'lerin yalnız biri temiz — iki sonuç AYNI ağırlıkta "
                   'okunamaz.', ha='center', fontsize=9.2, color='#fbbf24')
fig.subplots_adjust(left=.052, right=.988, top=.918, bottom=.112)
plt.savefig(os.path.join(CIK, 's0_bcd.png'), dpi=140,
            facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print('\n-> 07_S0_BCD/  SONUC.csv · s0_bcd.png')
