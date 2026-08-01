r"""DORDUNCU ADAY — BASINC DESTEGI ve EGIKLIK.  89_KAFES/AYIRMA.md'nin acik kalemi.

===============================  OLGU  =================================
Yogun rejimde (log g_bar >= -10) baryonlar TEK BASINA gozlemi asiyor:
        V_bar^2 > v_gozl^2   -> noktalarin %31,5'inde (2 sigma otesinde %11,8)
Bu, F4'e dokunan hicbir hikayeyle (kafes dahil) kapatilamaz, cunku F4 pozitif.
AYIRMA.md ucunu eledi/birakti:  Y* ELENDI · KAFES ELENDI · G AYAKTA
ve dorduncu adayi ele almadi: v_gozl'un KENDISI eksik olabilir.

=========================  DORDUNCU ADAY IKI SEY  ======================
(4a) BASINC DESTEGI (asimetrik surukleme)
     Hiz dagilimi varsa gozlenen donme, gercek dairesel hizdan KUCUKTUR:
        v_c^2 = v_donme^2 + 3,36 sigma^2 (R/R_1/2)      [n=1 disk, Burkert+2010]
     R_1/2 = 1,678 R_disk  =>  v_c^2 - v_donme^2 = 2,00 sigma^2 (R/R_disk)
     YONU DOGRU: gercek v_c daha buyukse acik kucculur.
     AMA BIR IMZASI VAR: duzeltme R ile BUYUR (dogrusal). Acik ise ice dogru
     buyur. Radyal imza TERS ise 4a elenir.

(4b) EGIKLIK HATASI
     v_gozl ~ 1/sin(i). i fazla tahmin edilmisse v_gozl kucuk cikar.
     Kapatmak icin gereken i kaymasi hesaplanir ve SPARC'in kendi e_i'siyle
     karsilastirilir. Gereken kayma e_i'yi cok asiyorsa 4b elenir.
     AYRICA: egiklik GALAKSI BASINA tek sayidir. Eger acik esas olarak
     galaksiden galaksiye degisiyorsa (galaksi ICINDE degil) 4b lehinedir;
     tersi ise aleyhinedir. Bunu varyans ayristirmasi olcer.

Cikti: SINIF_CALISMASI/89_KAFES/ -> GOZLEMSEL.csv · gozlemsel.png
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
CIK = os.path.join(SK, '89_KAFES')
os.makedirs(CIK, exist_ok=True)

G = 4.300917e-6
ACC = 1e6 / 3.0856776e19
A0 = (2.99792458e8 * (70e3 / 3.0857e22)) / ACC / 16.1 * 2.08
RB, UPS = 1.4, 0.50
YOGUN = -10.0                 # log g_bar esigi — acigin oldugu rejim
AD = {'01_erken_spiral': 'Sa–Sab', '02_orta_spiral': 'Sb–Sbc', '03_gec_spiral': 'Sc–Scd',
      '04_cok_gec_spiral': 'Sd', '05_macellan': 'Sdm–Sm', '06_duzensiz': 'Im'}

P = []
for sn in sorted(AD):
    KAT = {r['Galaksi']: r for r in csv.DictReader(
        open(os.path.join(SK, sn, 'KATALOG.csv'), encoding='utf-8'))}
    for f in sorted(glob.glob(os.path.join(SK, sn, 'veri', '*_rotmod.dat'))):
        ad = os.path.basename(f)[:-11]
        k = KAT[ad]
        Rd = float(k['Rdisk_kpc']); inc = float(k['Inc_deg']); einc = float(k['eInc_deg'])
        if Rd <= 0:
            continue
        d = np.loadtxt(f)
        R, Vo, eV, Vg, Vd, Vb, SBd, SBb = [d[:, i] for i in range(8)]
        Rp = R * 1e3
        L = lambda S: np.concatenate([[0.], np.cumsum(
            np.pi * (Rp[1:] ** 2 - Rp[:-1] ** 2) * .5 * (S[1:] + S[:-1]))])
        vg2 = np.maximum(np.sign(Vg) * Vg ** 2, 0.)
        vb2 = vg2 + UPS * Vd ** 2 + RB * UPS * Vb ** 2
        Mk = UPS * L(SBd) + RB * UPS * L(SBb) + np.maximum(R * np.sign(Vg) * Vg ** 2 / G, 0.)
        vF4 = np.sqrt(A0 * G * np.maximum(Mk, 1e-9))
        for j in range(len(R)):
            if vb2[j] <= 0 or Mk[j] <= 1e-3 * max(Mk[-1], 1e-6) or Vo[j] <= 0:
                continue
            P.append(dict(ad=ad, tip=AD[sn], R=R[j], Rd=Rd, inc=inc, einc=einc,
                          Vo=Vo[j], eV=max(eV[j], 1.), VB=vb2[j], F4=vF4[j],
                          D=vb2[j] + vF4[j] - Vo[j] ** 2,
                          gb=vb2[j] / R[j] * ACC, Q=int(k['Q']),
                          fbul=RB * UPS * Vb[j] ** 2 / vb2[j],
                          fD=int(k['fD']), Dm=float(k['D_Mpc']), eD=float(k['eD_Mpc'])))

GB = np.array([p['gb'] for p in P])
YM = np.log10(GB) >= YOGUN
Y = [p for p, m in zip(P, YM) if m]
print('n = %d nokta · yogun rejim (log g_bar >= %.1f): %d nokta, %d galaksi'
      % (len(P), YOGUN, len(Y), len(set(p['ad'] for p in Y))))
D = np.array([p['D'] for p in Y])
VB = np.array([p['VB'] for p in Y]); F4 = np.array([p['F4'] for p in Y])
VP = VB + F4
R = np.array([p['R'] for p in Y]); RD = np.array([p['Rd'] for p in Y])
VO = np.array([p['Vo'] for p in Y]); EV = np.array([p['eV'] for p in Y])
INC = np.array([p['inc'] for p in Y]); EINC = np.array([p['einc'] for p in Y])
ASAN = VB > VO ** 2            # baryonlar tek basina asan noktalar


def spearman(x, y):
    r = lambda v: np.argsort(np.argsort(v)) + 1.0
    a, b = r(x) - r(x).mean(), r(y) - r(y).mean()
    return float((a * b).sum() / np.sqrt((a * a).sum() * (b * b).sum()))


print('\n' + '=' * 100)
print('4a) BASINC DESTEGI — gereken sigma ne kadar?')
print('    v_c^2 - v_donme^2 = 2,00 sigma^2 (R/R_disk)  =>  sigma = sqrt(D R_disk/(2 R))')
sg = np.sqrt(np.maximum(D, 0) * RD / (2.0 * R))
print('    gereken sigma: medyan %.1f km/s · ceyreklikler %.1f – %.1f · %%90 %.1f'
      % (np.median(sg), np.percentile(sg, 25), np.percentile(sg, 75), np.percentile(sg, 90)))
print('    yerel disklerde gozlenen: gaz 8–12 · yildiz diski 20–40 · kovan 100–200 km/s')
print('    -> %s' % ('MAKUL: gereken sigma gozlenen aralikta'
                     if np.median(sg) < 60 else 'AGIR: gereken sigma disk degerlerinin ustunde'))
print('\n    RADYAL IMZA — 4a\'nin ayirt edici izi (duzeltme R ile BUYUMELI)')
print('    %-20s %6s %12s %12s' % ('R/R_disk kuşağı', 'n', 'D medyan', 'D/v_ong^2'))
xr = R / RD
for lo, hi in [(0, 0.5), (0.5, 1), (1, 1.5), (1.5, 2.5), (2.5, 6)]:
    m = (xr >= lo) & (xr < hi)
    if m.sum() < 20:
        continue
    print('    %6.1f … %-11.1f %6d %12.0f %12.3f'
          % (lo, hi, m.sum(), np.median(D[m]), np.median(D[m] / VP[m])))
eg = spearman(np.log10(np.maximum(xr, 1e-3)), D / VP)
print('    Spearman[D/v_ong^2 , R/R_disk] = %+.3f' % eg)
print('    4a POZITIF bekler (duzeltme disa dogru buyur) -> %s'
      % ('LEHTE' if eg > 0.1 else ('ALEYHTE — imza ters' if eg < -0.1 else 'AYIRT EDILEMIYOR')))

print('\n' + '=' * 100)
print('4b) EGIKLIK — gereken kayma SPARC\'in hata payi icinde mi?')
# v_gozl ~ 1/sin i ; kapatmak icin v_gozl -> sqrt(v_ong^2) olmali
f = np.sqrt(np.maximum(VP, 1e-9)) / VO                    # gereken buyutme carpani
sn_ = np.clip(np.sin(np.radians(INC)) / np.maximum(f, 1e-6), -1, 1)
i_ger = np.degrees(np.arcsin(sn_))
di = INC - i_ger
print('    gereken egiklik kaymasi |di| : medyan %.1f° · %%90 %.1f°'
      % (np.median(np.abs(di)), np.percentile(np.abs(di), 90)))
print('    SPARC\'in bildirdigi e_i      : medyan %.1f°' % np.median(EINC))
print('    kayma e_i\'nin 2 katini asan  : %%%.1f'
      % (100 * np.mean(np.abs(di) > 2 * EINC)))
print('    -> %s' % ('MAKUL: kayma hata payi icinde' if np.median(np.abs(di)) < np.median(EINC)
                     else 'AGIR: gereken kayma bildirilen hatayi asiyor'))
print('\n    Egiklikle iliski (4b dogruysa dusuk i\'de acik BUYUK olmali —')
print('    cunku sin i belirsizligi yuz-uste dogru buyur):')
print('    Spearman[D/v_ong^2 , egiklik] = %+.3f' % spearman(INC, D / VP))
print('    %-16s %6s %12s' % ('egiklik', 'n', 'D/v_ong^2'))
for lo, hi in [(30, 50), (50, 65), (65, 80), (80, 91)]:
    m = (INC >= lo) & (INC < hi)
    if m.sum() < 20:
        continue
    print('    %4d … %-9d %6d %12.3f' % (lo, hi, m.sum(), np.median(D[m] / VP[m])))

print('\n' + '=' * 100)
print('4a EK — KOVAN BASINCI  (disk asimetrik suruklemesi elendi; kovan ayri)')
FB = np.array([p.get('fbul', 0.) for p in Y])
print('  Spearman[D/v_ong^2 , kovan kesri] = %+.3f' % spearman(FB, D / VP))
print('  %-20s %6s %12s' % ('kovan kesri', 'n', 'D/v_ong^2'))
for lo, hi in [(0, .01), (.01, .15), (.15, .35), (.35, 1.01)]:
    m = (FB >= lo) & (FB < hi)
    if m.sum() < 20:
        continue
    print('  %6.2f … %-11.2f %6d %12.3f' % (lo, hi, m.sum(), np.median((D / VP)[m])))
_kb = (FB < 0.01)
print('  KOVANSIZ noktalarda (n=%d) acik hala %.3f -> kovan basinci TEK BASINA YETMEZ'
      % (_kb.sum(), np.median((D / VP)[_kb])))

print('\n' + '=' * 100)
print('4c — MESAFE HATASI  (V_bar^2 ~ D, v_gozl mesafeden BAGIMSIZ)')
GALX = {}
for p, xx in zip(Y, D / VP):
    GALX.setdefault(p['ad'], []).append(xx)
_ger, _bil, _fd, _ed = [], [], [], []
INFO = {p['ad']: p for p in Y}
for a, v in GALX.items():
    if len(v) < 3:
        continue
    xm = float(np.median(v))
    _ger.append(100 * xm); _fd.append(INFO[a]['fD'])
    _ed.append(100 * INFO[a]['eD'] / INFO[a]['Dm'])
_ger, _ed, _fd = np.array(_ger), np.array(_ed), np.array(_fd)
print('  gereken |dD/D| medyan %.1f%%  ·  SPARC\'in bildirdigi e_D/D medyan %.1f%%'
      % (np.median(_ger), np.median(_ed)))
print('\n  BELIRLEYICI — mesafe YONTEMINE gore (fD: 1=Hubble · 2=TRGB · 3=Cepheid · 4=UMa · 5=SN)')
print('  Mesafe hatasi sebepse IYI mesafeli galakside acik KUCUK olmali')
print('  %-6s %8s %12s %14s' % ('fD', 'n_gal', 'D/v_ong^2', 'e_D/D medyan'))
for fd in sorted(set(_fd.tolist())):
    m = _fd == fd
    if m.sum() < 3:
        continue
    print('  %-6d %8d %12.3f %13.1f%%' % (fd, m.sum(), np.median(_ger[m]) / 100, np.median(_ed[m])))
print('\n  Spearman[acik , e_D/D] = %+.3f  (n=%d galaksi)' % (spearman(_ed, _ger), len(_ger)))
print('  -> mesafe sebepse POZITIF olmali. %s'
      % ('ELENDI: en iyi mesafeli galakside acik en buyuk, korelasyon yok'
         if spearman(_ed, _ger) < 0.15 else 'lehte'))

print('\n' + '=' * 100)
print('VARYANS AYRISTIRMASI — acik galaksi BASINA mi, galaksi ICINDE mi?')
print('  Egiklik ve mesafe GALAKSI BASINA tek sayidir -> galaksiler ARASI varyans')
print('  G ve basinc destegi yaricapla degisir        -> galaksi ICI varyans')
x = D / VP
gal = {}
for p, v in zip(Y, x):
    gal.setdefault(p['ad'], []).append(v)
ic = [np.var(v) for v in gal.values() if len(v) > 2]
ort = [np.mean(v) for v in gal.values() if len(v) > 2]
va, vi = float(np.var(ort)), float(np.mean(ic))
print('  galaksiler ARASI varyans : %.4f  (%%%.0f)' % (va, 100 * va / (va + vi)))
print('  galaksi ICI varyans      : %.4f  (%%%.0f)' % (vi, 100 * vi / (va + vi)))
print('  -> %s' % ('galaksiler arasi baskin: EGIKLIK/MESAFE lehine'
                   if va > vi else 'galaksi ici baskin: G ve BASINC lehine, egiklik aleyhine'))

with open(os.path.join(CIK, 'GOZLEMSEL.csv'), 'w', encoding='utf-8', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['Galaksi', 'Sinif', 'Q', 'R_kpc', 'R_bolu_Rdisk', 'egiklik_deg',
                'e_egiklik_deg', 'g_bar_ms2', 'acik_D', 'v_ong2', 'D_bolu_vong2',
                'gereken_sigma_kms', 'gereken_egiklik_kaymasi_deg',
                'baryon_tek_basina_asiyor'])
    for p, xx, s2, dd, aa in zip(Y, x, sg, di, ASAN):
        w.writerow([p['ad'], p['tip'], p['Q'], '%.2f' % p['R'],
                    '%.2f' % (p['R'] / p['Rd']), '%.0f' % p['inc'], '%.0f' % p['einc'],
                    '%.3e' % p['gb'], '%+.0f' % p['D'], '%.0f' % (p['VB'] + p['F4']),
                    '%+.3f' % xx, '%.1f' % s2, '%+.1f' % dd,
                    'evet' if aa else 'hayir'])

# ------------------------------------------------------------------ grafik
fig, ax = plt.subplots(1, 3, figsize=(16.4, 5.6), facecolor='#121212')
for a in ax:
    a.set_facecolor('#121212'); a.grid(alpha=.13)

a = ax[0]
a.hist(sg, bins=np.linspace(0, 120, 40), color='#16a34a', alpha=.85)
for v, c, t in [(12, '#7c3aed', 'gaz 8–12'), (40, '#ffcc00', 'yıldız diski 20–40'),
                (150, '#f87171', 'kovan 100–200')]:
    a.axvline(v, color=c, ls='--', lw=1.8, label=t)
a.axvline(np.median(sg), color='white', lw=2.2,
          label=('gereken medyan %.0f' % np.median(sg)))
a.set_xlim(0, 120)
a.set_xlabel('gereken $\\sigma$   (km/s)', fontsize=10.5)
a.set_ylabel('ölçüm noktası', fontsize=10.5)
a.set_title('4a — basınç desteği ne kadar $\\sigma$ ister?', fontsize=12, color='white', pad=8)
a.legend(fontsize=8.6, framealpha=.3)

a = ax[1]
kk = []
for lo, hi in [(0, 0.5), (0.5, 1), (1, 1.5), (1.5, 2.5), (2.5, 6)]:
    m = (xr >= lo) & (xr < hi)
    if m.sum() >= 20:
        kk.append(((lo + hi) / 2, float(np.median(D[m] / VP[m])), int(m.sum())))
a.plot(np.log10(np.maximum(xr, 1e-3)), x, '.', color='#52525b', ms=2.6, alpha=.35)
a.plot(np.log10([k[0] for k in kk]), [k[1] for k in kk], 'o-', color='#ffcc00',
       ms=10, lw=2.6, label='kuşak medyanı')
a.axhline(0, color='#71717a', lw=1.2)
a.set_ylim(-0.6, 0.8)
a.set_xlabel('$\\log (R/R_{disk})$', fontsize=10.5)
a.set_ylabel('$D/v_{öng}^2$', fontsize=10.5)
a.set_title('4a\'nın imzası — açık dışa doğru büyüyor mu?', fontsize=12, color='white', pad=8)
a.legend(fontsize=8.8, framealpha=.3)
a.text(.97, .95, ('Spearman %+.3f\n4a POZİTİF bekler' % eg).replace('.', ','),
       transform=a.transAxes, ha='right', va='top', fontsize=9.2,
       color='#f87171' if eg < 0 else '#4ade80', family='monospace')

a = ax[2]
a.plot(np.abs(di), EINC, '.', color='#52525b', ms=3, alpha=.45)
lim = [0, 40]
a.plot(lim, lim, '--', color='#f87171', lw=1.8, label='gereken = bildirilen hata')
a.plot(lim, [2 * v for v in lim], ':', color='#fbbf24', lw=1.6, label='2× hata')
a.set_xlim(0, 40); a.set_ylim(0, 20)
a.set_xlabel('gereken eğiklik kayması $|\\Delta i|$   (°)', fontsize=10.5)
a.set_ylabel('SPARC\'ın bildirdiği $e_i$   (°)', fontsize=10.5)
a.set_title('4b — eğiklik hatası yeter mi?', fontsize=12, color='white', pad=8)
a.legend(fontsize=8.8, framealpha=.3)
a.text(.97, .95, ('gereken medyan %.1f°\nbildirilen medyan %.1f°\n2×\'i aşan %%%.0f'
                  % (np.median(np.abs(di)), np.median(EINC),
                     100 * np.mean(np.abs(di) > 2 * EINC))).replace('.', ','),
       transform=a.transAxes, ha='right', va='top', fontsize=9.2, color='#fbbf24',
       family='monospace')

fig.suptitle('Dördüncü aday sınandı — basınç desteği ve eğiklik  ·  yoğun rejim, %d nokta'
             % len(Y), fontsize=14.4, color='white', y=.975)
fig.text(.5, .035, 'Olgu: yoğun rejimde baryonlar tek başına gözlemi aşıyor '
                   '($V_{bar}^2>v_{gözl}^2$). $F4$ pozitif olduğu için ona dokunan hiçbir '
                   'hikâye bunu kapatamaz — kafes dahil.',
         ha='center', fontsize=9.4, color='#a1a1aa')
fig.text(.5, .008, 'Varyans ayrıştırması: galaksiler arası %%%.0f · galaksi içi %%%.0f  →  %s'
                   % (100 * va / (va + vi), 100 * vi / (va + vi),
                      'eğiklik/mesafe lehine' if va > vi else '$\\mathcal{G}$ ve basınç lehine'),
         ha='center', fontsize=9.4, color='#fbbf24')
fig.subplots_adjust(left=.055, right=.986, top=.855, bottom=.185, wspace=.28)
plt.savefig(os.path.join(CIK, 'gozlemsel.png'), dpi=140,
            facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print('\n-> 89_KAFES/  GOZLEMSEL.csv · gozlemsel.png')
