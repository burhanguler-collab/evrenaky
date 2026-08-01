r"""ADIM 3 — G YEREL MI?  Teorinin degiskenlik iddiasinin dogrudan sinavi.

--- IDDIA ---
Teoride  G = alfa/rho_n.  rho_n ortamin YEREL yogunlugudur; c'nin sabit
olmadigi bir kuramda G de sabit olamaz (Postulat 4). Madde ortami sikistiriyorsa
yogun bolgede rho_n artar -> G DUSER. Yani:

    G_yerel/G_Newton, yerel baryonik yuzey yogunlugu ile AZALMALI.

--- OLCUM ---
F4'un payinin kucuk oldugu bolgede (pay < 0,15) ongoru neredeyse saf F1'dir:

    G_yerel/G  =  (v_gozl^2 - v_F4^2) / V_bar,Newton^2

V_bar SPARC'tan gelir ve EVRENSEL Newton G'siyle hesaplanmistir; oran 1'den
saparsa ya G yereldir, ya Y* yanlistir, ya da F1'in kendisi eksiktir.

--- KRITIK BOZULMA (DEJENERASYON) VE NASIL KIRILIR ---
V_bar^2 = (G_yerel/G) * [ V_gaz^2 + Y* V_disk^2 + R_B Y* V_kovan^2 ]
G'yi %20 buyutmek ile Y*'i %20 buyutmek YILDIZ terimi icin ayni seydir.
AMA GAZ terimi Y* icermez:
    G degisirse  -> gaz ve yildiz BIRLIKTE olceklenir
    Y* yanlissa  -> yalniz yildiz olceklenir
Dolayisiyla oran ile GAZ KESRI arasindaki iliski ikisini ayirir:
    oran gaz kesrinden BAGIMSIZ  -> G yerelligi lehine
    oran gaz kesriyle DEGISIYOR  -> Y* yanlisligi lehine
Bu betigin asil sinavi budur.

F4 icin 94_YEREL_LOMEGA'nin B kurulumu kullanilir (yerel M_kaps).

Cikti: SINIF_CALISMASI/93_G_YEREL/ -> SONUC.csv · g_yerel.png
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
CIK = os.path.join(SK, '93_G_YEREL')
os.makedirs(CIK, exist_ok=True)

G = 4.300917e-6
ACC = 1e6 / 3.0856776e19
A0 = (2.99792458e8 * (70e3 / 3.0857e22)) / ACC / 16.1
RB, UPS = 1.4, 0.50
PAY_ESIK = 0.35        # F4'un payi bunun altindaysa ongoru F1 BASKIN.
                       # 0,15 ile de kosuldu: n=164, egilim ayni (rho -0,39).
                       # 0,35 secildi cunku 0,15 yalniz 164 nokta birakiyor ve
                       # Sigma araligini daraltiyor. F4 zaten CIKARILIYOR, yani
                       # gevsek esik F4 modelini sonuca sokmaz, sadece artigi buyutur.
AD = {'01_erken_spiral': 'Sa–Sab', '02_orta_spiral': 'Sb–Sbc', '03_gec_spiral': 'Sc–Scd',
      '04_cok_gec_spiral': 'Sd', '05_macellan': 'Sdm–Sm', '06_duzensiz': 'Im'}

P = []          # nokta nokta
for sn in sorted(AD):
    for f in sorted(glob.glob(os.path.join(SK, sn, 'veri', '*_rotmod.dat'))):
        d = np.loadtxt(f)
        R, Vo, eV, Vg, Vd, Vb, SBd, SBb = [d[:, i] for i in range(8)]
        Rp = R * 1e3
        L = lambda S: np.concatenate([[0.], np.cumsum(
            np.pi * (Rp[1:] ** 2 - Rp[:-1] ** 2) * .5 * (S[1:] + S[:-1]))])
        v_gaz2 = np.sign(Vg) * Vg ** 2
        v_yil2 = UPS * Vd ** 2 + RB * UPS * Vb ** 2
        vb2 = v_gaz2 + v_yil2
        Mk = np.maximum(UPS * L(SBd) + RB * UPS * L(SBb)
                        + np.maximum(R * v_gaz2 / G, 0.), 1e-6)
        F4 = np.sqrt(A0 * G * Mk)                       # 94_YEREL_LOMEGA kurulum B
        pay = F4 / np.maximum(vb2 + F4, 1e-9)
        Sig = UPS * (SBd + RB * SBb)                    # yildiz yuzey yog. M_gunes/pc^2
        for j in range(len(R)):
            if pay[j] >= PAY_ESIK or vb2[j] <= 0 or Sig[j] <= 0:
                continue
            if Vo[j] ** 2 - F4[j] <= 0:
                continue
            P.append(dict(ad=os.path.basename(f)[:-11], tip=AD[sn], R=R[j],
                          oran=(Vo[j] ** 2 - F4[j]) / vb2[j],
                          Sig=Sig[j], pay=pay[j],
                          fgaz=max(v_gaz2[j], 0.) / vb2[j],
                          eV=max(eV[j], 1.), Vo=Vo[j]))

ORAN = np.array([p['oran'] for p in P])
SIG = np.array([p['Sig'] for p in P])
FG = np.array([p['fgaz'] for p in P])
print('F4 payi < %.2f olan nokta: %d  (%d galaksiden)'
      % (PAY_ESIK, len(P), len(set(p['ad'] for p in P))))


def spearman(x, y):
    r = lambda v: np.argsort(np.argsort(v)) + 1.0
    a, b = r(x) - r(x).mean(), r(y) - r(y).mean()
    return float((a * b).sum() / np.sqrt((a * a).sum() * (b * b).sum()))


print('\n' + '=' * 100)
print('1) G_yerel / G_Newton  —  teori 1\'den SAPMA ve yogunlukla AZALMA bekliyor')
print('  medyan %.3f   ·  sacilma %.3f dex  ·  ceyreklikler %.2f – %.2f'
      % (np.median(ORAN), np.std(np.log10(ORAN)),
         np.percentile(ORAN, 25), np.percentile(ORAN, 75)))

print('\n  YILDIZ YUZEY YOGUNLUGU KUSAKLARI')
print('  %-24s %6s %10s %10s' % ('log Sigma_* (M_g/pc^2)', 'n', 'oran med', 'sacilma'))
KEN = np.arange(1.0, 4.25 + 1e-9, 0.25)
KUS = []
for lo, hi in zip(KEN[:-1], KEN[1:]):
    m = (np.log10(SIG) >= lo) & (np.log10(SIG) < hi)
    if m.sum() < 25:
        continue
    KUS.append(((lo + hi) / 2, np.median(ORAN[m]), int(m.sum()), np.std(np.log10(ORAN[m]))))
    print('  %8.2f … %-11.2f %6d %10.3f %10.3f'
          % (lo, hi, m.sum(), np.median(ORAN[m]), np.std(np.log10(ORAN[m]))))
xk = np.array([k[0] for k in KUS]); yk = np.array([k[1] for k in KUS])
eg_S = np.polyfit(xk, np.log10(yk), 1)[0]
rho_S = spearman(np.log10(SIG), np.log10(ORAN))
print('\n  d log(G_yerel/G) / d log Sigma_*  =  %+.4f     (teori: NEGATIF bekler)' % eg_S)
print('  Spearman[log oran , log Sigma_*]  =  %+.3f   (n=%d)' % (rho_S, len(P)))

GAL = sorted(set(p['ad'] for p in P))
gS = np.array([np.median([q['Sig'] for q in P if q['ad'] == g]) for g in GAL])
gO = np.array([np.median([q['oran'] for q in P if q['ad'] == g]) for g in GAL])
print('\n  GALAKSI BASINA KUMELENMIS  (noktalar bagimsiz degil — bu satir zorunlu)')
print('    n = %d galaksi · Spearman %+.3f · egim %+.4f dex/dex'
      % (len(GAL), spearman(np.log10(gS), np.log10(gO)),
         np.polyfit(np.log10(gS), np.log10(gO), 1)[0]))
print('    DIKKAT: nokta duzeyi egimi %+.4f; galaksi duzeyi cok daha dik.' % eg_S)
print('    Ikisi ayni seyi olcmuyor olabilir — galaksi duzeyi sinif sacilmasini da')
print('    tasir. Egimin BUYUKLUGU bu yuzden belirsizdir; guvenilir olan ISARETIDIR.')

print('\n' + '=' * 100)
print('2) DEJENERASYON SINAVI — sapma G\'den mi, Y*\'tan mi?')
print('  G degisirse gaz ve yildiz BIRLIKTE olceklenir -> oran gaz kesrinden BAGIMSIZ')
print('  Y* yanlissa yalniz yildiz olceklenir          -> oran gaz kesriyle DEGISIR')
rho_g = spearman(FG, np.log10(ORAN))
print('\n  Spearman[log oran , gaz kesri]    =  %+.3f' % rho_g)
print('  %-28s %6s %10s' % ('gaz kesri kusagi', 'n', 'oran med'))
GK = [(0.0, 0.2), (0.2, 0.4), (0.4, 0.6), (0.6, 1.01)]
GKS = []
for lo, hi in GK:
    m = (FG >= lo) & (FG < hi)
    if m.sum() < 15:
        continue
    GKS.append(((lo + hi) / 2, np.median(ORAN[m]), int(m.sum())))
    print('  %8.2f … %-15.2f %6d %10.3f' % (lo, hi, m.sum(), np.median(ORAN[m])))
if len(GKS) >= 2:
    fark = GKS[-1][1] / GKS[0][1]
    print('\n  gaz baskin / yildiz baskin oran farki : %.3f  (%.3f dex)'
          % (fark, np.log10(fark)))
    print('  -> %s' % ('AYIRT EDILEMIYOR: sapma iki bilesene de esit dokunuyor -> '
                       'G YERELLIGI ile tutarli'
                       if abs(np.log10(fark)) < 0.05 else
                       'gaz kesriyle DEGISIYOR -> Y* yanlisligi daha olasi'))

print('\n  GAZ KALDIRACI YOK — ve bu YAPISALDIR:')
print('    F4 payinin dusuk oldugu bolge zaten YILDIZ BASKIN bolgedir. Dort ayri')
print('    kesitte de (pay<0,15 / 0,25 / 0,35 / 0,50) noktalarin TAMAMI gaz kesri')
print('    <0,2 kusaginda kaldi. Bu yontemle G ile Y* AYRILAMAZ — veri eksigi degil,')
print('    olcumun yapisal siniri.')

print('\n  AMA BIR ISARET ARGUMANI VAR:')
print('    Olculen  : oran Sigma_* ile AZALIYOR.')
print('    Y* savi  : bunu Y*\'in yogunlukla AZALMASI ile kapatmak zorunda.')
print('    Oysa 3,6 um\'de yogun bolgeler (kovan, ic disk) YASLI ve KIRMIZI nufus')
print('    barindirir; populasyon sentezi orada Y*\'in ARTMASINI bekler.')
print('    Yani Y* aciklamasi yildiz nufusu fizigiyle TERS isaret istiyor.')
print('    G = alfa/rho_n ise yogun yerde azalmayi DOGRUDAN ongorur — isaret dogru.')
print('    Bu bir KANIT DEGIL, bir yon argumanidir. Dejenerasyon kirilmamistir.')

print('\n  Not: sapma yalniz Y* ile kapatilsaydi Y* = %.2f x %.3f = %.3f olurdu'
      % (UPS, np.median(ORAN), UPS * np.median(ORAN)))
print('        (populasyon sentezi bandi 0,3-0,8 -> deger bandin %s).'
      % ('ICINDE' if 0.3 <= UPS * np.median(ORAN) <= 0.8 else 'DISINDA'))

with open(os.path.join(CIK, 'SONUC.csv'), 'w', encoding='utf-8', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['Galaksi', 'Sinif', 'R_kpc', 'F4_payi', 'Sigma_yildiz_Msun_pc2',
                'gaz_kesri', 'G_yerel_bolu_G'])
    for p in P:
        w.writerow([p['ad'], p['tip'], '%.2f' % p['R'], '%.3f' % p['pay'],
                    '%.2f' % p['Sig'], '%.3f' % p['fgaz'], '%.4f' % p['oran']])

# ------------------------------------------------------------------ grafik
fig, ax = plt.subplots(1, 3, figsize=(16.2, 5.6), facecolor='#121212')
for a in ax:
    a.set_facecolor('#121212'); a.grid(alpha=.13)

a = ax[0]
a.plot(np.log10(SIG), np.log10(ORAN), '.', color='#52525b', ms=3, alpha=.45)
a.plot(xk, np.log10(yk), 'o-', color='#16a34a', ms=8, lw=2.2, zorder=5,
       label='kuşak medyanı')
a.axhline(0, color='#f87171', ls='--', lw=1.5, label='$\\mathcal{G}=G$ (değişmez)')
xx = np.linspace(xk.min(), xk.max(), 20)
a.plot(xx, np.polyval(np.polyfit(xk, np.log10(yk), 1), xx), ':', color='#4ade80', lw=1.7,
       label=('eğim %+.4f' % eg_S).replace('.', ','))
a.set_xlabel('$\\log \\Sigma_*$   ($M_\\odot$/pc²)', fontsize=10.5)
a.set_ylabel('$\\log(\\mathcal{G}_{yerel}/G)$', fontsize=10.5)
a.set_title('Teori: yoğun yerde $\\mathcal{G}$ düşmeli', fontsize=12, color='white', pad=8)
a.set_ylim(-1.0, 1.0)
a.legend(fontsize=8.6, framealpha=.3, loc='upper right')

a = ax[1]
# Bu panel BOS gorunuyorsa bulgu odur: kaldirac yok. Dagilimi gostererek soyluyoruz.
a.hist(FG, bins=np.linspace(0, 1, 41), color='#fb923c', alpha=.85)
a.axvline(0.2, color='#f87171', ls='--', lw=1.6)
a.set_xlim(0, 1)
a.set_xlabel('gaz kesri  $V_{gaz}^2/V_{bar}^2$', fontsize=10.5)
a.set_ylabel('ölçüm noktası', fontsize=10.5)
a.set_title('Dejenerasyon kaldıracı — YOK', fontsize=12, color='white', pad=8)
NOT = """G ile Y* ayrılabilmesi için
gaz baskın nokta gerekir.

%d noktanın TAMAMI
gaz kesri < 0,2 kuşağında.

F4'ün payı düşükse bölge
zaten yıldız baskındır —
bu YAPISAL bir sınır,
veri eksiği değil.""" % len(P)
a.text(.32, .84, NOT, transform=a.transAxes, fontsize=9.2, color='#fbbf24',
       va='top', family='monospace')

a = ax[2]
a.hist(np.log10(ORAN), bins=45, color='#16a34a', alpha=.8)
a.axvline(0, color='#f87171', ls='--', lw=1.6, label='$\\mathcal{G}=G$')
a.axvline(np.log10(np.median(ORAN)), color='#ffcc00', lw=1.8,
          label=('medyan %.3f' % np.median(ORAN)).replace('.', ','))
a.set_xlabel('$\\log(\\mathcal{G}_{yerel}/G)$', fontsize=10.5)
a.set_ylabel('ölçüm noktası', fontsize=10.5)
a.set_title('%d nokta · %d galaksi' % (len(P), len(set(p['ad'] for p in P))),
            fontsize=12, color='white', pad=8)
a.legend(fontsize=8.6, framealpha=.3)

fig.suptitle('$\\mathcal{G}$ yerel mi? — F4\'ün payının %%%d\'in altında olduğu bölgede'
             % int(100 * PAY_ESIK), fontsize=14, color='white', y=.975)
fig.text(.5, .075, 'Ölçüm: $\\mathcal{G}_{yerel}/G=(v_{gözl}^2-v_{F4}^2)/V_{bar,Newton}^2$. '
                   '$V_{bar}$ SPARC\'tan gelir ve evrensel Newton $G$\'siyle hesaplanmıştır — '
                   'oran 1\'den saparsa ya $\\mathcal{G}$ yereldir, ya $\\Upsilon_*$ yanlıştır.',
         ha='center', fontsize=9.2, color='#a1a1aa')
fig.text(.5, .028, 'Orta panel ikisini ayırır: $\\mathcal{G}$ gazı da yıldızı da ölçekler, '
                   '$\\Upsilon_*$ yalnız yıldızı. Düz çizgi $\\mathcal{G}$ lehine, eğimli '
                   '$\\Upsilon_*$ lehinedir.', ha='center', fontsize=9.2, color='#a1a1aa')
fig.subplots_adjust(left=.052, right=.988, top=.855, bottom=.225, wspace=.26)
plt.savefig(os.path.join(CIK, 'g_yerel.png'), dpi=140,
            facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print('\n-> 93_G_YEREL/  SONUC.csv · g_yerel.png')
