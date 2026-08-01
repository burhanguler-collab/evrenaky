# -*- coding: utf-8 -*-
"""GAZ, F4'UN KAYNAGI OLABILIR MI?  —  'kafes yapisi yok' iddiasinin sinavi.

IDDIA (yazar): Gazda kafes yapisi olmadigi icin F4'e katkisi cok azdir;
dolayisiyla gaz, F4'un kaynagi olan toplam kutle verisi olarak kullanilamaz.

Bu iddia F4'e IKI AYRI YERDEN girer ve yonleri TERSTIR — o yuzden "lehte mi
aleyhte mi" sorusu tahminle cevaplanamaz:

  (A) PAY:    F4 = G * M_kaynak / l_omega      -> gaz cikarsa F4 KUCULUR (aleyhte)
  (B) BOLEN:  l_omega = q_n/(2*gamma_n)        -> gamma_n dolanim debisi; kafes
              gerektiriyorsa gaz gamma_n'e girmez, l_omega BUYUR
              -> F4 = G*M/l_omega yine KUCULUR (aleyhte)

Yani iddianin her iki kanadi da ayni yone bakiyor. Buna karsin iddianin
LEHTE olabilecegi bir yer var ve asil sinav orada:

  (C) EGIM ve SINIF SACILMASI: gaz orani kutleyle guclu bicimde ters iliskilidir
      (cuceler gaz baskin, buyuk sarmallar yildiz baskin). Gazi bastirmak bu
      yuzden KUTLEYE BAGLI bir duzeltme getirir. Sinif calismasinin en buyuk
      cozulmemis sorunu, gereken a_0 carpaninin siniftan sinifa 1,47-3,76 arasi
      degismesiydi. Eger o sacilma gaz oraniyla olcekleniyorsa, bu iddia o
      sorunu ACIKLAR — normalizasyonu daha da bozma bedeliyle.

Uc olceklendirme kurulur (f = M_kafes / M_bar, gaz agirligi w ile):
  K1  yalniz pay      : F4 -> f  * F4_cal        (l_omega kalibre halinde)
  K2  yalniz bolen    : F4 -> f  * F4_cal        (l_omega 1/f kadar buyur)
  K3  ikisi birden    : F4 -> f^2 * F4_cal       (mekanizmaya en sadik hal)
F1 (V_bar) HER ZAMAN gazi icerir: pulsasyon kutle deplasmanidir, kafes gerektirmez.

Cikti: SINIF_CALISMASI/97_BTFR/GAZ_KAFES.md  ·  gaz_kafes.png
"""

import os
import sys
import glob
import warnings

import numpy as np
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
plt.style.use('dark_background')

KOK = os.path.dirname(os.path.abspath(__file__))
VERI = os.path.join(KOK, 'veri')
CIK = os.path.join(KOK, 'SINIF_CALISMASI', '97_BTFR')

G = 4.300917e-6
C_SI, H0_SI = 2.99792458e8, 70e3 / 3.0857e22
ACC = 1e6 / 3.0856776e19
A0 = (C_SI * H0_SI / ACC) / 16.1
RB, UPS, XGAZ = 1.4, 0.50, 1.33          # XGAZ: M_gaz = 1,33 * M_HI (helyum)
TIPAD = {0: 'S0', 1: 'Sa', 2: 'Sab', 3: 'Sb', 4: 'Sbc', 5: 'Sc',
         6: 'Scd', 7: 'Sd', 8: 'Sdm', 9: 'Sm', 10: 'Im', 11: 'BCD'}


def mrt(yol, alan):
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
    R, Vo, eV, Vg, Vd, Vb = [d[:, i] for i in range(6)]
    if np.any(R <= 0):
        continue
    ROT[ad] = dict(R=R, Vb2=np.sign(Vg) * Vg ** 2 + UPS * Vd ** 2 + RB * UPS * Vb ** 2)

AD = [n for n in sorted(B) if B[n]['Vf'] > 0 and n in ROT and n in K
      and K[n]['L36'] > 0 and K[n]['MHI'] > 0]
Mb = np.array([10 ** B[n]['lMb'] for n in AD])
lMb = np.log10(Mb)
Vf = np.array([B[n]['Vf'] for n in AD])
Mst = np.array([UPS * K[n]['L36'] * 1e9 for n in AD])
Mgz = np.array([XGAZ * K[n]['MHI'] * 1e9 for n in AD])
Vb2 = np.array([max(ROT[n]['Vb2'][-1], 0.0) for n in AD])
tip = [TIPAD.get(int(K[n]['T']), '?') for n in AD]
lv = np.log10(Vf)

# ---- 1) ayristirmanin dogrulugu: M_* + 1,33 M_HI ?= yayinlanmis M_b ----
d0 = np.log10((Mst + Mgz) / Mb)
print('=' * 96)
print('AYRISTIRMA DENETIMI  (%d galaksi)' % len(AD))
print('  log[(M_* + 1,33 M_HI) / M_b(yayin)] : medyan %+.3f dex · sacilma %.3f dex'
      % (np.median(d0), np.std(d0)))
print('  -> ayristirma yayinlanmis M_b ile %s' %
      ('TUTARLI' if abs(np.median(d0)) < .05 and np.std(d0) < .10 else 'TUTARSIZ — dikkat'))
fgaz = Mgz / (Mst + Mgz)
print('  gaz orani M_gaz/M_bar : medyan %.2f · aralik %.2f-%.2f' %
      (np.median(fgaz), fgaz.min(), fgaz.max()))
print('  gaz BASKIN (f>0,5) galaksi sayisi : %d/%d' % ((fgaz > .5).sum(), len(AD)))


def sp(a, b):
    ra = np.argsort(np.argsort(a)).astype(float)
    rb = np.argsort(np.argsort(b)).astype(float)
    return float(np.corrcoef(ra, rb)[0, 1])


print('  gaz orani <-> log M_b (Spearman) : %+.2f' % sp(lMb, fgaz))

# ---- 2) uc olceklendirme ----
F4c = np.sqrt(G * Mb * A0)                 # kalibre F4 (gaz dahil, iki yerde de)


def f_kafes(w):
    """M_kafes / M_bar — gaz agirligi w ile."""
    return (Mst + w * Mgz) / (Mst + Mgz)


KUR = [('K1  yalniz pay      (F4 -> f F4)', lambda f: f),
       ('K2  yalniz bolen    (F4 -> f F4)', lambda f: f),
       ('K3  ikisi birden    (F4 -> f² F4)', lambda f: f ** 2)]


def a0_carpani(vb2, f4, vgoz):
    """Medyan sapmayi kapatan a_0 carpani — SAYISAL cozulur.

    a_0 -> k a_0 olunca F4 sqrt(k) ile olceklenir, V_bar^2 hic olceklenmez.
    """
    fk = lambda k: np.median(np.log10(np.sqrt(vb2 + np.sqrt(k) * f4) / vgoz))
    a, b = 1e-4, 1e6
    if fk(a) > 0 or fk(b) < 0:
        return np.nan
    for _ in range(200):
        m = np.sqrt(a * b)
        if fk(m) < 0:
            a = m
        else:
            b = m
    return np.sqrt(a * b)


print('\n' + '=' * 96)
print('IDDIANIN ETKISI  (w = gazin F4 kaynagindaki agirligi; w=1 mevcut hal)')
print('  %-34s %5s %11s %8s %12s' % ('kurulum', 'w', 'v_ong/v_olc', 'egim', 'gereken a_0'))
SON = {}
for ad, olc in KUR:
    for w in (1.0, 0.5, 0.25, 0.0):
        f4 = olc(f_kafes(w)) * F4c
        v = np.sqrt(Vb2 + f4)
        dd = np.log10(v / Vf)
        eg = np.polyfit(np.log10(v), lMb, 1)[0]
        kk = a0_carpani(Vb2, f4, Vf)
        SON[(ad, w)] = (10 ** np.median(dd), eg, kk)
        print('  %-34s %5.2f %11.3f %8.3f %11.2fx' % (ad, w, 10 ** np.median(dd), eg, kk))
    print()
eg_a = np.polyfit(lv, lMb, 1)[0]
wg = 1 / np.maximum(np.array([B[n]['elMb'] for n in AD]), .02) ** 2
A = np.vstack([lv, np.ones_like(lv)]).T
eg_ag = np.linalg.solve(A.T @ np.diag(wg) @ A, A.T @ np.diag(wg) @ lMb)[0]
print('  %-34s %5s %11.3f %8s %12s'
      % ('GOZLENEN', '—', 1.0, '%.3f-%.3f' % (min(eg_a, eg_ag), max(eg_a, eg_ag)), '—'))

# ---- 3) ASIL SINAV: artik gaz oraniyla olcekleniyor mu? ----
v1 = np.sqrt(Vb2 + F4c)
art = np.log10(v1 / Vf)                    # mevcut kurulumun artigi (hiz dex)
print('\n' + '=' * 96)
print('ASIL SINAV — mevcut kurulumun artigi gaz oraniyla olcekleniyor mu?')
print('  Iddia dogruysa: gazi BASTIRMAK gerekiyorsa, gaz zengini galaksiler')
print('  simdi FAZLA ongoruluyor olmali -> artik(hiz) gaz oraniyla ARTMALI (+).')
r_f = sp(fgaz, art)
print('  Spearman[artik , gaz orani]      : %+.2f' % r_f)
print('  Spearman[artik , log M_b]        : %+.2f' % sp(lMb, art))
ic = fgaz > np.median(fgaz)
print('  gaz zengin yari  (f>%.2f, n=%d) : medyan artik %+.3f dex  (v_ong/v_olc %.3f)'
      % (np.median(fgaz), ic.sum(), np.median(art[ic]), 10 ** np.median(art[ic])))
print('  gaz yoksul yari  (f<%.2f, n=%d) : medyan artik %+.3f dex  (v_ong/v_olc %.3f)'
      % (np.median(fgaz), (~ic).sum(), np.median(art[~ic]), 10 ** np.median(art[~ic])))
fark = np.median(art[ic]) - np.median(art[~ic])
print('  FARK (zengin - yoksul)           : %+.3f dex' % fark)
print('  -> iddianin ongordugu YON: POZITIF fark. Olculen: %s'
      % ('POZITIF — iddia bu testi GECIYOR' if fark > 0.01 else
         ('NEGATIF — iddia bu testi GECMIYOR' if fark < -0.01 else 'SIFIR — ayirt edilemiyor')))

# her galaksi icin gereken carpan, gaz oraniyla iliskisi
kg = np.array([a0_carpani(np.array([Vb2[j]]), np.array([F4c[j]]), np.array([Vf[j]]))
               for j in range(len(AD))])
iy = np.isfinite(kg)
print('\n  galaksi basina gereken a_0 carpani: medyan x%.2f · aralik x%.2f-x%.2f'
      % (np.median(kg[iy]), kg[iy].min(), kg[iy].max()))
print('  Spearman[gereken carpan , gaz orani] : %+.2f' % sp(fgaz[iy], kg[iy]))
print('  -> sinif calismasinin x1,47-3,76 sacilmasi gaz oraniyla aciklaniyor mu?  %s'
      % ('EVET yonunde (|r|>0,4)' if abs(sp(fgaz[iy], kg[iy])) > .4 else 'HAYIR (|r|<0,4)'))

# ---- grafik ----
fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(16.6, 5.5), facecolor='#121212')
for a in (a1, a2, a3):
    a.set_facecolor('#121212')
    a.grid(alpha=.13)

a1.scatter(fgaz, art, c=lMb, cmap='viridis', s=34, zorder=4)
zz = np.polyfit(fgaz, art, 1)
a1.plot([0, 1], np.polyval(zz, [0, 1]), '-', color='#f87171', lw=2.2,
        label='eğim %+.3f · Spearman %+.2f' % (zz[0], r_f))
a1.axhline(0, color='#71717a', lw=1, ls=':')
a1.set_xlabel('gaz oranı  $M_{gaz}/M_{bar}$', fontsize=11)
a1.set_ylabel('artık  $\\log(v_{öng}/v_{ölç})$', fontsize=11)
a1.set_title('ASIL SINAV: artık gaz oranıyla ölçekleniyor mu?', fontsize=12, color='white', pad=8)
a1.legend(fontsize=9, framealpha=.2, loc='lower right')
a1.text(.03, .04, 'İddia doğruysa bu eğim\nPOZİTİF olmalıydı', transform=a1.transAxes,
        fontsize=9.6, color='#fbbf24', family='monospace', va='bottom')

ws = np.linspace(0, 1, 41)
for ad, olc, cc in [(KUR[0][0], KUR[0][1], '#38bdf8'), (KUR[2][0], KUR[2][1], '#f472b6')]:
    kk = [a0_carpani(Vb2, olc(f_kafes(w)) * F4c, Vf) for w in ws]
    a2.plot(ws, kk, '-', color=cc, lw=2.4, label=ad.split('(')[0].strip())
a2.axhline(2.02, color='#4ade80', lw=1.8, ls='--', label='mevcut hâl ×2,02')
a2.axhspan(1.29, 2.83, color='#4ade80', alpha=.10, zorder=1)
a2.text(.5, 2.05, 'sınıf çalışmasının bandı ×1,47–3,76', fontsize=9, color='#4ade80')
a2.set_xlabel('gazın F4 kaynağındaki ağırlığı $w$   (1 = mevcut, 0 = gaz hiç saymaz)', fontsize=10.4)
a2.set_ylabel('gereken $a_0$ çarpanı', fontsize=11)
a2.set_yscale('log')
a2.set_title('Gazı bastırmanın bedeli', fontsize=12, color='white', pad=8)
a2.legend(fontsize=9, framealpha=.2)
a2.invert_xaxis()

for ad, olc, cc in [(KUR[0][0], KUR[0][1], '#38bdf8'), (KUR[2][0], KUR[2][1], '#f472b6')]:
    eg = [np.polyfit(np.log10(np.sqrt(Vb2 + olc(f_kafes(w)) * F4c)), lMb, 1)[0] for w in ws]
    a3.plot(ws, eg, '-', color=cc, lw=2.4, label=ad.split('(')[0].strip())
a3.axhspan(min(eg_a, eg_ag), max(eg_a, eg_ag), color='#ffcc00', alpha=.16, zorder=1)
a3.text(.5, (eg_a + eg_ag) / 2, 'gözlenen bant', fontsize=9.4, color='#fbbf24', ha='center')
a3.axhline(3.632, color='#4ade80', lw=1.8, ls='--', label='mevcut hâl 3,632')
a3.set_xlabel('gazın F4 kaynağındaki ağırlığı $w$', fontsize=10.4)
a3.set_ylabel('BTFR eğimi', fontsize=11)
a3.set_title('Eğim ne oluyor?', fontsize=12, color='white', pad=8)
a3.legend(fontsize=9, framealpha=.2)
a3.invert_xaxis()

fig.suptitle('«Gazda kafes yok, F4\'e katkısı az» iddiasının sınavı — %d galaksi, fit yok'
             % len(AD), fontsize=13.6, color='white', y=.98)
fig.text(.5, .015, 'Gaz oranı medyanı %.2f ve kütleyle Spearman %+.2f — yani bu iddia '
                   'KÜTLEYE BAĞLI bir düzeltmedir, sabit bir kayma değil.'
         % (np.median(fgaz), sp(lMb, fgaz)), ha='center', fontsize=9.4, color='#a1a1aa')
plt.tight_layout(rect=[0, .045, 1, .935])
plt.savefig(os.path.join(CIK, 'gaz_kafes.png'), dpi=125, facecolor='#121212')
print('\n-> 97_BTFR/gaz_kafes.png')
