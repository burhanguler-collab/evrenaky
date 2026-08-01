r"""%68 GALAKSILER ARASI — NE KADARI GURULTU?  88_TARAMA md.7 madde 1.

===============================  SORU  =================================
89_KAFES/GOZLEMSEL.md acigin varyansinin %68'inin GALAKSILER ARASI oldugunu
olctu ve son uc dosya bunun uzerine kuruldu. Ama o oran HAM varyanstir:
icinde olcum gurultusu de var. Gurultu ayrilmadan "adi olmayan sistematik"
denemez.

============================  HATA BUTCESI  ===========================
Hedef:  x = 1 - v_gozl^2 / v_ong^2        (v_ong^2 = V_bar^2 + v_F4)
Uc hata kaynagi, ikisi GALAKSI BASINA:

 (1) v_gozl olcum hatasi  e_V   — NOKTA basina
        dx/dv_gozl = -2 v_gozl/v_ong^2
        -> hem galaksi ICI hem galaksiler ARASI varyansa katkida bulunur
           (galaksi basina medyan aliniyor, n nokta ile azalir)

 (2) MESAFE hatasi  e_D        — GALAKSI basina
        M ~ D^2, R ~ D  =>  V_bar^2 ~ D  ve  v_F4 = sqrt(G M a_0) ~ D
        yani v_ong^2 ~ D butunuyle:
        dx/dlnD = + v_gozl^2/v_ong^2 = (1-x)
        -> YALNIZ galaksiler arasi varyans

 (3) EGIKLIK hatasi  e_i       — GALAKSI basina
        v_gozl ~ 1/sin i  =>  dln v_gozl/di = -cot(i)
        dx/di = +2 (v_gozl^2/v_ong^2) cot(i) = 2(1-x) cot(i)   [i radyan]
        -> YALNIZ galaksiler arasi varyans

Gurultu payi cikarilinca kalan varyans GERCEK galaksi-basina degisimdir.
Kalan sifira yakinsa "adsiz sistematik" YOKTUR — hepsi hata butcesidir.

Cikti: SINIF_CALISMASI/88_TARAMA/ -> GURULTU.csv · gurultu.png
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
CIK = os.path.join(SK, '88_TARAMA')
os.makedirs(CIK, exist_ok=True)

G = 4.300917e-6
ACC = 1e6 / 3.0856776e19
A0 = (2.99792458e8 * (70e3 / 3.0857e22)) / ACC / 16.1 * 2.08
RB, UPS = 1.4, 0.50
AD = {'01_erken_spiral': 'Sa–Sab', '02_orta_spiral': 'Sb–Sbc', '03_gec_spiral': 'Sc–Scd',
      '04_cok_gec_spiral': 'Sd', '05_macellan': 'Sdm–Sm', '06_duzensiz': 'Im'}
rng = np.random.default_rng(20260801)

GAL = {}
for sn in sorted(AD):
    KAT = {r['Galaksi']: r for r in csv.DictReader(
        open(os.path.join(SK, sn, 'KATALOG.csv'), encoding='utf-8'))}
    for f in sorted(glob.glob(os.path.join(SK, sn, 'veri', '*_rotmod.dat'))):
        ad = os.path.basename(f)[:-11]
        k = KAT[ad]
        d = np.loadtxt(f)
        R, Vo, eV, Vg, Vd, Vb, SBd, SBb = [d[:, i] for i in range(8)]
        eV = np.maximum(eV, 1.0)
        Rp = R * 1e3
        L = lambda S: np.concatenate([[0.], np.cumsum(
            np.pi * (Rp[1:] ** 2 - Rp[:-1] ** 2) * .5 * (S[1:] + S[:-1]))])
        vb2 = np.maximum(np.sign(Vg) * Vg ** 2, 0.) + UPS * Vd ** 2 + RB * UPS * Vb ** 2
        Mk = UPS * L(SBd) + RB * UPS * L(SBb) + np.maximum(R * np.sign(Vg) * Vg ** 2 / G, 0.)
        F4 = np.sqrt(A0 * G * np.maximum(Mk, 1e-9))
        vp = vb2 + F4
        gb = np.log10(np.maximum(vb2 / np.maximum(R, 1e-9) * ACC, 1e-30))
        ok = (vb2 > 0) & (Mk > 1e-3 * max(Mk[-1], 1e-6)) & (Vo > 0)
        for etk, m in [('tum', ok), ('yog', ok & (gb >= -10))]:
            if m.sum() < 3:
                continue
            x = 1 - Vo[m] ** 2 / vp[m]
            # (1) v_gozl hatasindan gelen NOKTA basina sigma_x
            sx = 2 * Vo[m] * eV[m] / vp[m]
            # galaksi basina medyanin gurultu varyansi — bootstrap
            B = 600
            sim = np.median(1 - (Vo[m] + rng.normal(0, eV[m], (B, m.sum()))) ** 2 / vp[m],
                            axis=1)
            v1 = float(np.var(sim))
            xm = float(np.median(x))
            # (2) mesafe
            eD = float(k['eD_Mpc']) / float(k['D_Mpc'])
            v2 = ((1 - xm) * eD) ** 2
            # (3) egiklik
            ir = np.radians(float(k['Inc_deg'])); ei = np.radians(float(k['eInc_deg']))
            v3 = (2 * (1 - xm) / np.tan(ir) * ei) ** 2 if np.tan(ir) != 0 else 0.0
            GAL.setdefault(etk, {})[ad] = dict(
                tip=AD[sn], n=int(m.sum()), x=xm, v_vgozl=v1, v_mesafe=v2,
                v_egiklik=v3, sx=float(np.median(sx)), eD=eD,
                inc=float(k['Inc_deg']), ei=float(k['eInc_deg']))

SON = {}
for etk, ad2 in [('yog', 'YOGUN REJIM (log g_bar >= -10)'), ('tum', 'BUTUN EGRI')]:
    Gd = GAL[etk]
    x = np.array([g['x'] for g in Gd.values()])
    n1 = np.array([g['v_vgozl'] for g in Gd.values()])
    n2 = np.array([g['v_mesafe'] for g in Gd.values()])
    n3 = np.array([g['v_egiklik'] for g in Gd.values()])
    V_ham = float(np.var(x))                      # gozlenen galaksiler ARASI varyans
    N1, N2, N3 = float(np.mean(n1)), float(np.mean(n2)), float(np.mean(n3))
    N = N1 + N2 + N3
    kalan = V_ham - N
    SON[etk] = (V_ham, N1, N2, N3, kalan, len(x))
    print('\n' + '=' * 100)
    print('%s  ·  n = %d galaksi' % (ad2, len(x)))
    print('  GOZLENEN galaksiler arasi varyans   : %.5f   (sacilma %.3f)'
          % (V_ham, np.sqrt(V_ham)))
    print('  --- hata butcesi ---')
    print('  (1) v_gozl olcum hatasi             : %.5f   (%%%.0f)' % (N1, 100 * N1 / V_ham))
    print('  (2) MESAFE hatasi (galaksi basina)  : %.5f   (%%%.0f)' % (N2, 100 * N2 / V_ham))
    print('  (3) EGIKLIK hatasi (galaksi basina) : %.5f   (%%%.0f)' % (N3, 100 * N3 / V_ham))
    print('      TOPLAM GURULTU                  : %.5f   (%%%.0f)' % (N, 100 * N / V_ham))
    print('  KALAN (gercek galaksi-basina degisim): %.5f  (%%%.0f · sacilma %s)'
          % (kalan, 100 * kalan / V_ham,
             '%.3f' % np.sqrt(kalan) if kalan > 0 else 'TANIMSIZ'))
    print('  -> %s' % ('KALAN NEGATIF/SIFIR: adsiz sistematik YOK, hepsi hata butcesi'
                       if kalan <= 0.1 * V_ham else
                       ('kalan %%%.0f: gercek bir galaksi-basina degisim VAR'
                        % (100 * kalan / V_ham))))

# ---- GOZLEMSEL.md'nin %68'i yeniden hesaplaniyor (gurultu duzeltmeli) ----
print('\n' + '=' * 100)
print('GOZLEMSEL.md md.4\'UN %68\'I — GURULTU DUZELTMELI HALI')
Gd = GAL['yog']
ic = []
for sn in sorted(AD):
    pass
# galaksi ici varyansi da gurultuden arindir
for etk, ad2 in [('yog', 'YOGUN'), ('tum', 'TUM')]:
    Gd = GAL[etk]
    V_ham, N1, N2, N3, kalan, n = SON[etk]
    # galaksi ICI ham varyans: her galaksinin nokta sacilmasi
    print('  %-8s : ham arasi %.5f · gurultu %.5f · GERCEK arasi %s'
          % (ad2, V_ham, N1 + N2 + N3,
             '%.5f' % kalan if kalan > 0 else '<= 0'))

with open(os.path.join(CIK, 'GURULTU.csv'), 'w', encoding='utf-8', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['Galaksi', 'Sinif', 'kesit', 'n_nokta', 'acik_x', 'sigma_x_nokta',
                'var_vgozl', 'var_mesafe', 'var_egiklik', 'eD_bolu_D',
                'egiklik_deg', 'e_egiklik_deg'])
    for etk in ('yog', 'tum'):
        for a, g in sorted(GAL[etk].items()):
            w.writerow([a, g['tip'], etk, g['n'], '%+.4f' % g['x'], '%.4f' % g['sx'],
                        '%.6f' % g['v_vgozl'], '%.6f' % g['v_mesafe'],
                        '%.6f' % g['v_egiklik'], '%.3f' % g['eD'],
                        '%.0f' % g['inc'], '%.0f' % g['ei']])

# ------------------------------------------------------------------ grafik
fig, ax = plt.subplots(1, 3, figsize=(16.4, 5.6), facecolor='#121212')
for a in ax:
    a.set_facecolor('#121212'); a.grid(alpha=.13)

for a, etk, ad2 in [(ax[0], 'yog', 'YOĞUN REJİM'), (ax[1], 'tum', 'BÜTÜN EĞRİ')]:
    V_ham, N1, N2, N3, kalan, n = SON[etk]
    et = ['gözlenen\ntoplam', '$v_{gözl}$\nhatası', 'MESAFE\nhatası',
          'EĞİKLİK\nhatası', 'KALAN\ngerçek']
    vv = [V_ham, N1, N2, N3, max(kalan, 0)]
    cl = ['#a1a1aa', '#7c3aed', '#f87171', '#fbbf24', '#16a34a']
    a.bar(range(5), vv, .62, color=cl)
    for i, v in enumerate(vv):
        a.text(i, v + V_ham * .02, ('%.4f' % v).replace('.', ','), ha='center',
               fontsize=9.4, color=cl[i], fontweight='bold')
        if i > 0:
            a.text(i, v / 2 if v > V_ham * .12 else v + V_ham * .075,
                   '%%%.0f' % (100 * v / V_ham), ha='center', fontsize=9,
                   color='#0a0a0a' if v > V_ham * .12 else '#d4d4d8')
    a.set_xticks(range(5)); a.set_xticklabels(et, fontsize=8.4)
    a.set_ylabel('galaksiler arası varyans', fontsize=10.5)
    a.set_ylim(0, V_ham * 1.22)
    a.set_title('%s · n=%d galaksi' % (ad2, n), fontsize=12, color='white', pad=8)

a = ax[2]
Gd = GAL['yog']
xx = np.array([g['x'] for g in Gd.values()])
ss = np.sqrt(np.array([g['v_vgozl'] + g['v_mesafe'] + g['v_egiklik'] for g in Gd.values()]))
srt = np.argsort(xx)
a.errorbar(np.arange(len(xx)), xx[srt], yerr=ss[srt], fmt='o', color='#16a34a',
           ms=4.6, elinewidth=1.2, capsize=0)
a.axhline(np.median(xx), color='#ffcc00', lw=2,
          label=('medyan %+.3f' % np.median(xx)).replace('.', ','))
a.axhline(0, color='#71717a', lw=1.2)
a.set_xlabel('galaksi (açığa göre sıralı)', fontsize=10.5)
a.set_ylabel('açık $D/v_{öng}^2$', fontsize=10.5)
a.set_title('Galaksi başına açık ve hata bütçesi', fontsize=12, color='white', pad=8)
a.legend(fontsize=9, framealpha=.3)

fig.suptitle('«%68 galaksiler arası» — ne kadarı gürültü?', fontsize=14.4,
             color='white', y=.975)
fig.text(.5, .035, 'Üç hata kaynağı: $v_{gözl}$ ölçüm hatası (nokta başına, bootstrap) · '
                   'MESAFE ($v_{öng}^2\\propto D$, galaksi başına) · '
                   'EĞİKLİK ($v_{gözl}\\propto1/\\sin i$, galaksi başına).',
         ha='center', fontsize=9.4, color='#a1a1aa')
fig.text(.5, .008, 'Mesafe ve eğiklik SEBEP olarak elenmişti (GOZLEMSEL.md) — ama '
                   'SAÇILMA katkıları ayrı bir şeydir ve burada ilk kez hesaplandı.',
         ha='center', fontsize=9.4, color='#fbbf24')
fig.subplots_adjust(left=.055, right=.986, top=.855, bottom=.185, wspace=.28)
plt.savefig(os.path.join(CIK, 'gurultu.png'), dpi=140,
            facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print('\n-> 88_TARAMA/  GURULTU.csv · gurultu.png')
