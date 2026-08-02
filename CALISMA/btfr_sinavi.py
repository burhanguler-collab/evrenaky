r"""BTFR SINAVI — teorinin turetim iddiasi, FIT YAPMADAN.  (v2: F1 eklenmis)

--- SURUM NOTU ---
Bu betigin ILK surumu teoriyi yalniz F4'un asimptotik limitiyle sinadi:
    v^4 = G M_bar a_0            (yalniz F4, R >> l_omega varsayimi)
Bu YANLISTI. Teorinin tam radyal ivmesi iki terimlidir ve M-37 merkezcil dengesi
ikisini birden alir:
    v^2 = V_bar^2(Y*)  +  G M_bar / l_omega
          |- F1: pulsasyon, kuresel aki, Newton benzeri (SPARC ayristirmasindan)
                             |- F4: silindirik aki
l_omega = sqrt(G M_bar/a_0) konulunca ikinci terim sqrt(G M_bar a_0) olur, yani
ilk surumun tamami; F1 ise ona EKLENIR.

Asimptot varsayimi neden gecersiz: l_omega/R_dis olculdu -> 0,13 ile 1,6 arasi,
medyan 0,36. Alti galakside l_omega > R_dis, yani asimptot HIC ulasilmamis.
F1'i atmak hizi sqrt(1+l_om/R) kadar KUCUK gosterir (medyan carpan 1,166).

Duzeltmenin etkisi (121 galaksi, V_bar son olcum noktasinda):
    kurulum                          v_ong/v_olc   egim   gereken a_0
    yalniz F4 asimptot (ilk surum)      0.723      4.000     x3.65
    V_bar(F1) + F4  (BU SURUM)          0.885      3.632     x2.02
    gozlenen                            1.000      3.530       —
Onemli: duzeltme, kitabin BTFR gerilimi (x2,26) ile SAYISAL OLARAK ORTUSUYOR.
Ilk surumun x3,65'i ile sinif calismasinin (o zamanki) x1,70'i arasindaki
"cozulemez celiski"
tamamen F1'in atilmasindan dogmustu.

IKINCI DUZELTME — 'gereken a_0' nasil hesaplanir:
    Naif formul  k = 10^(-4 * medyan log(v_ong/v_olc))  YALNIZ saf-F4 asimptotunda
    gecerlidir (orada v ~ a_0^(1/4)). TAM formulde a_0 -> k a_0 yapilinca
        v^2 = V_bar^2 + sqrt(k) * sqrt(G M_b a_0)
    olur; V_bar^2 hic olceklenmez. Yani k, sayisal olarak COZULMELIDIR.
    Naif deger x1.63 verirdi; dogru cozum x2.02. Fark, F4'un v^2 icindeki
    payindan gelir (medyan 0,70; 0,36-0,87 arasi).
    Bu betik dogru (cozulmus) degeri raporlar; naif degeri de karsilastirma
    icin yazdirir ki formulun nerede kirildigi gorulsun.

DIKKAT — bu surum de bir SECIM icerir: V_bar hangi yaricapta okunuyor?
    son nokta (kullanilan)      0.885   egim 3.632   -> k = x2.02
    son noktanin bir icerisi    0.890   egim 3.596   -> k = x1.98
    dis yarinin ortasi          0.918   egim 3.387   -> k = x1.73
Yani x1.73-x2.02 bandi yaricap secimiyle oynatilabilir. En muhafazakar
(teori icin en kotu) secim olan son nokta raporlanmistir.

--- KURULUM ---
Referans veri: Lelli, McGaugh, Schombert, Desmond & Katz — BTFR_Lelli2019.mrt (153 galaksi).
  Yayinin Not 1'i: "These values assume a stellar mass-to-light ratio of 0.5 at
  3.6 um" -> yayinlanmis M_b, bizim ongorumuzdeki Y*=0,50 ile ayni. Y* SECIMI YOK.
V_bar: SPARC Rotmod_LTG'nin V_gas, V_disk, V_bul sutunlarindan (Y*=0,50 ile).
  Bunlar bilesenlerin NEWTON donus hizlaridir; G = alfa/rho_n oldugu icin F1'in
  ta kendisidir ve kuresel yaklasimdan (sqrt(GM/R)) daha dogrudur cunku disk
  geometrisini icerir.

Yedi hiz tanimi da ayri ayri raporlanir. HI cizgi genisligi satirlarinda W ~ 2V
oldugu icin kesim 4log2 = 1,204 dex kayar; ham degerler karsilastirilamaz.

Karsi taraf: M_* -> M_200 (Moster+2013) -> c_200 (Dutton&Maccio 2014) -> NFW V_max.
Sifir serbest parametre. LCDM BTFR'yi analitik vermez; bu en yakin karsiligidir.

Cikti: SINIF_CALISMASI/97_BTFR/ -> SONUC.csv · YONTEM.md · btfr.png
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
VERI = os.path.join(KOK, 'veri')
CIK = os.path.join(KOK, 'SINIF_CALISMASI', '97_BTFR')
os.makedirs(CIK, exist_ok=True)

G = 4.300917e-6
C_SI = 2.99792458e8
H0_SI = 70e3 / 3.0857e22
ACC = 1e6 / 3.0856776e19
CH0 = (C_SI * H0_SI) / ACC
KATSAYI = 16.1
A0_TARIHSEL = CH0 / KATSAYI                  # kurulum A (ilk surum)
A0 = 1.75 * 1.038 * A0_TARIHSEL              # v3: PENCERELI RESMI (M-47) = 7,67e-11 m/s^2
RHO_CRIT = 3 * 0.07 ** 2 / (8 * np.pi * G)
H_RED, RB, UPS = 0.7, 1.4, 0.50
KESIM_T = -np.log10(G * A0)
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
print('BTFR tablosu %d · ana katalog %d galaksi' % (len(B), len(K)))
print('TEORI: log M_b = 4,000 log v + %.3f   (yalniz F4 asimptotu)' % KESIM_T)
print('       v^2 = V_bar^2 + sqrt(G M_b a_0)  (TAM: F1 + F4)')

# ---- rotmod'dan V_bar ----
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
Mhalo_am = lambda Ms: float(np.interp(Ms, _Ms, _Mh))
mu = lambda x: np.log(1 + x) - x / (1 + x)


def v_max_nfw(M200):
    c = 10 ** (0.905 - 0.101 * np.log10(M200 * H_RED / 1e12))
    R200 = (3 * M200 / (4 * np.pi * 200 * RHO_CRIT)) ** (1 / 3.)
    return np.sqrt(G * M200 / R200) * np.sqrt(0.2162 * c / mu(c))


HIZ = [('Vf', 'eVf', 'düz dönme hızı $V_f$'), ('V2exp', 'eV2exp', '$V_{2{,}2R_d}$'),
       ('V2eff', 'eV2eff', '$V_{2R_{eff}}$'), ('Vmax', 'eVmax', '$V_{max}$'),
       ('Wp20', 'eWp20', 'HI $W_{p20}$'), ('Wm50', 'eWm50', 'HI $W_{m50}$'),
       ('Wm50c', 'eWm50c', 'HI $W_{m50}^{c}$')]

# ---- galaksi listesi (Vf olculmus VE rotmod var) ----
AD = [n for n in B if B[n]['Vf'] > 0 and n in ROT]
Mb = np.array([10 ** B[n]['lMb'] for n in AD])
lMb = np.log10(Mb)
Vf = np.array([B[n]['Vf'] for n in AD])
eVf = np.array([B[n]['eVf'] for n in AD])
elMb = np.array([B[n]['elMb'] for n in AD])
Rout = np.array([ROT[n]['R'][-1] for n in AD])
Vbar2out = np.array([max(ROT[n]['Vb2'][-1], 0.0) for n in AD])
lom = np.sqrt(G * Mb / A0)
F4 = np.sqrt(G * Mb * A0)                 # = G M_b / l_omega
gkout = G * Mb / Rout ** 2                # g_kaps (M_bar yaklasimi; md. 6.8)
Wout = np.minimum(1.0, A0 / gkout)        # M-47 Rankine penceresi
v_f4 = F4 ** 0.5                          # yalniz F4 (asimptot)
v_tam = np.sqrt(Vbar2out + F4 * Wout)     # PENCERELI RESMI: F1 + F4*W (M-47)
print('eslesen: %d galaksi · l_omega/R_dis medyan %.2f · asimptot ulasilmayan %d'
      % (len(AD), np.median(lom / Rout), int((lom > Rout).sum())))

def a0_carpani(vb2, f4, vgoz, gk=None, asimptot=False):
    """Medyan sapmayi kapatan a_0 carpani k.

    a_0 -> k a_0 olunca F4 = sqrt(G M a_0) terimi sqrt(k) ile olceklenir,
    V_bar^2 hic olceklenmez. Bu yuzden k KAPALI FORMULLE bulunamaz; sayisal
    cozulur. Naif 10^(-4*fark) formulu yalniz saf-F4 asimptotunda dogrudur.
    """
    if asimptot:
        return 10 ** (-4 * np.median(np.log10(np.sqrt(f4) / vgoz)))
    if gk is None:
        fk = lambda k: np.median(np.log10(np.sqrt(vb2 + np.sqrt(k) * f4) / vgoz))
    else:                                     # M-47: W carpanla birlikte olceklenir
        fk = lambda k: np.median(np.log10(np.sqrt(
            vb2 + np.sqrt(k) * f4 * np.minimum(1.0, k * A0 / gk)) / vgoz))
    a, b = 1e-3, 1e3
    if fk(a) > 0 or fk(b) < 0:
        return np.nan
    for _ in range(200):                      # ikiye bolme — scipy'ye gerek yok
        m = np.sqrt(a * b)
        if fk(m) < 0:
            a = m
        else:
            b = m
    return np.sqrt(a * b)


egim = lambda lv, lm, w=None: (np.polyfit(lv, lm, 1) if w is None else
                               np.linalg.solve((np.vstack([lv, np.ones_like(lv)]).T.T * w)
                                               @ np.vstack([lv, np.ones_like(lv)]).T,
                                               (np.vstack([lv, np.ones_like(lv)]).T.T * w) @ lm))

print('\n' + '=' * 96)
print('SURUM KARSILASTIRMASI  (%d galaksi, R = son olcum noktasi)' % len(AD))
print('  %-38s %11s %9s %8s %12s %11s'
      % ('kurulum', 'v_ong/v_olc', 'sacilma', 'egim', 'gereken a_0', '(naif form.)'))
K_ASI = a0_carpani(Vbar2out, F4, Vf, asimptot=True)
K_TAM = a0_carpani(Vbar2out, F4, Vf, gk=gkout)
for nm, v, kk, na in [('yalniz F4 asimptot (ILK SURUM)', v_f4, K_ASI, ''),
                      ('V_bar(F1) + F4*W  (PENCERELI RESMI, M-47)', v_tam, K_TAM,
                       '%.2fx' % 10 ** (-4 * np.median(np.log10(v_tam / Vf))))]:
    d = np.log10(v / Vf)
    e = np.polyfit(np.log10(v), lMb, 1)[0]
    print('  %-38s %11.3f %9.3f %8.3f %11.2fx %11s'
          % (nm, 10 ** np.median(d), np.std(d), e, kk, na))
print('  NOT: naif formul 10^(-4*fark) yalniz saf-F4 asimptotunda gecerlidir;')
print('       TAM formulde k sayisal cozulur (F4 payi medyan %.2f).'
      % np.median(F4 * Wout / (Vbar2out + F4 * Wout)))
eg_g, ke_g = np.polyfit(np.log10(Vf), lMb, 1)
w = 1 / np.maximum(elMb, .02) ** 2
A = np.vstack([np.log10(Vf), np.ones_like(Vf)]).T
eg_ga, ke_ga = np.linalg.solve(A.T @ np.diag(w) @ A, A.T @ np.diag(w) @ lMb)
print('  %-38s %11.3f %9s %8.3f %12s' % ('GOZLENEN (agirliksiz)', 1.0, '—', eg_g, '—'))
print('  %-38s %11s %9s %8.3f %12s' % ('GOZLENEN (agirlikli)', '—', '—', eg_ga, '—'))

# ---- yaricap secimine duyarlilik ----
print('\n' + '=' * 96)
print('YARICAP SECIMINE DUYARLILIK  (V_bar hangi yaricapta okunuyor?)')
print('  %-26s %11s %8s %12s' % ('V_bar okuma yeri', 'v_ong/v_olc', 'egim', 'gereken a_0'))
for nm, fn in [('son nokta (kullanilan)', lambda r: -1),
               ('son noktanin bir icerisi', lambda r: -2),
               ('dis yarinin ortasi', lambda r: len(r) - max(1, len(r) // 4) - 1)]:
    vb = np.array([max(ROT[n]['Vb2'][fn(ROT[n]['R'])], 0.0) for n in AD])
    Ri = np.array([ROT[n]['R'][fn(ROT[n]['R'])] for n in AD])
    gki = G * Mb / Ri ** 2
    v = np.sqrt(vb + F4 * np.minimum(1.0, A0 / gki))
    d = np.log10(v / Vf)
    print('  %-26s %11.3f %8.3f %11.2fx' % (nm, 10 ** np.median(d),
          np.polyfit(np.log10(v), lMb, 1)[0], a0_carpani(vb, F4, Vf, gk=gki)))

# ---- yedi hiz tanimi ----
print('\n' + '=' * 96)
print('YEDI HIZ TANIMI  (TAM formulle; W satirlari icin W/2 duzeltmesi ayrica)')
print('  %-8s %5s | %8s %9s | %11s %11s %10s'
      % ('hiz', 'n', 'gozl.egim', 'sacilma', 'fark(dex)', 'gereken a_0', '(naif)'))
sonuc = {}
for k, ek, ad in HIZ:
    g = [n for n in B if B[n][k] > 0 and B[n][ek] > 0 and n in ROT]
    if len(g) < 10:
        continue
    v = np.array([B[n][k] for n in g])
    lm = np.array([B[n]['lMb'] for n in g])
    el = np.array([B[n]['elMb'] for n in g])
    m = np.array([10 ** B[n]['lMb'] for n in g])
    vb = np.array([max(ROT[n]['Vb2'][-1], 0.0) for n in g])
    Rg = np.array([ROT[n]['R'][-1] for n in g])
    gkg = G * m / Rg ** 2
    vt = np.sqrt(vb + np.sqrt(G * m * A0) * np.minimum(1.0, A0 / gkg))
    vk = v / 2 if k.startswith('W') else v
    d = np.log10(vt / vk)
    Aa = np.vstack([np.log10(v), np.ones_like(v)]).T
    ww = 1 / np.maximum(el, .02) ** 2
    eg = np.linalg.solve(Aa.T @ np.diag(ww) @ Aa, Aa.T @ np.diag(ww) @ lm)[0]
    art = lm - np.polyval(np.polyfit(np.log10(v), lm, 1), np.log10(v))
    kk = a0_carpani(vb, np.sqrt(G * m * A0), vk, gk=gkg)
    sonuc[k] = dict(ad=ad, n=len(g), eg=eg, sac=np.std(art), med=np.median(d),
                    carp=kk, naif=10 ** (-4 * np.median(d)), W=k.startswith('W'))
    print('  %-8s %5d | %8.3f %9.3f | %+11.3f %10.2fx %9.2fx%s'
          % (k, len(g), eg, np.std(art), np.median(d), kk,
             10 ** (-4 * np.median(d)), '  (W/2)' if k.startswith('W') else ''))

# ---- LCDM ----
ort = [n for n in AD if n in K and K[n]['L36'] > 0]
vL = np.array([v_max_nfw(Mhalo_am(UPS * K[n]['L36'] * 1e9)) for n in ort])
lmL = np.array([B[n]['lMb'] for n in ort])
vOb = np.array([B[n]['Vf'] for n in ort])
egL = np.polyfit(np.log10(vL), lmL, 1)[0]
print('\n' + '=' * 96)
print('LCDM ZINCIRI (%d galaksi, sifir serbest parametre)' % len(vL))
print('  ima ettigi egim : %.3f   ·  V_max/V_f : medyan %.3f, sacilma %.3f dex'
      % (egL, 10 ** np.median(np.log10(vL / vOb)), np.std(np.log10(vL / vOb))))
print('  V_f araligi %.0f-%.0f km/s · V_max araligi %.0f-%.0f km/s -> aralik %.2f kat genis'
      % (vOb.min(), vOb.max(), vL.min(), vL.max(),
         (np.log10(vL.max()) - np.log10(vL.min())) / (np.log10(vOb.max()) - np.log10(vOb.min()))))
print('\n  EGIM SIRALAMASI:  teori(tam) %.3f  |  gozlenen %.3f-%.3f  |  LCDM %.3f'
      % (np.polyfit(np.log10(v_tam), lMb, 1)[0], eg_g, eg_ga, egL))

# ---- SONUC.csv ----
with open(os.path.join(CIK, 'SONUC.csv'), 'w', encoding='utf-8', newline='') as fh:
    w2 = csv.writer(fh)
    w2.writerow(['Galaksi', 'Tip', 'YAY_logMb', 'YAY_elogMb'] +
                sum([['YAY_' + k, 'YAY_e' + k] for k, _, _ in HIZ], []) +
                ['R_dis_kpc', 'Vbar_dis_kms', 'l_omega_kpc', 'l_om_bolu_R',
                 'TEORI_v_yalnizF4', 'TEORI_v_TAM', 'FARK_dex_TAM', 'W_pencere', 'LCDM_Vmax_kms'])
    for n in sorted(B, key=lambda x: -B[x]['lMb']):
        b = B[n]
        t = TIPAD.get(int(K[n]['T']), '') if n in K else ''
        row = [n, t, '%.2f' % b['lMb'], '%.2f' % b['elMb']]
        for k, ek, _ in HIZ:
            row += ['%.1f' % b[k], '%.1f' % b[ek]]
        if n in ROT:
            m = 10 ** b['lMb']
            lo = np.sqrt(G * m / A0)
            vb = max(ROT[n]['Vb2'][-1], 0.0)
            f4 = np.sqrt(G * m * A0)
            wr = min(1.0, A0 * ROT[n]['R'][-1] ** 2 / (G * m))     # M-47
            vt = np.sqrt(vb + f4 * wr)
            row += ['%.2f' % ROT[n]['R'][-1], '%.1f' % np.sqrt(vb), '%.2f' % lo,
                    '%.3f' % (lo / ROT[n]['R'][-1]), '%.1f' % f4 ** .5, '%.1f' % vt,
                    '%+.3f' % (np.log10(vt / b['Vf'])) if b['Vf'] > 0 else '',
                    '%.3f' % wr]
        else:
            row += [''] * 8
        row += ['%.1f' % v_max_nfw(Mhalo_am(UPS * K[n]['L36'] * 1e9))
                if (n in K and K[n]['L36'] > 0) else '']
        w2.writerow(row)

# ---- grafik ----
fig, (a1, a2) = plt.subplots(1, 2, figsize=(15.4, 6.6), facecolor='#121212')
a1.set_facecolor('#121212')
lv = np.log10(Vf)
a1.errorbar(lv, lMb, yerr=elMb, xerr=eVf / (Vf * np.log(10)), fmt='o', color='#ffcc00',
            ms=4.2, elinewidth=.8, capsize=0, zorder=5, label='ölçüm (%d galaksi)' % len(AD))
xx = np.linspace(lv.min() - .08, lv.max() + .08, 50)
# TAM ongoru NOKTA olarak cizilir: galaksi basina bir deger, duz bir yasa DEGIL
# (V_bar her galaksinin kendi ayristirmasindan gelir). Cizgi yalniz egilimi gosterir.
et_ = np.polyfit(np.log10(v_tam), lMb, 1)
a1.scatter(np.log10(v_tam), lMb, s=40, marker='D', facecolors='none',
           edgecolors='#16a34a', linewidths=1.4, zorder=7,
           label='EVRENAKI RESMİ (M-47): $V_{bar}^2+\\sqrt{\\mathcal{G}Ma_0}\\cdot W$  (galaksi başına)')
a1.plot(xx, np.polyval(et_, xx), '-', color='#16a34a', lw=2.2, alpha=.6, zorder=6,
        label='  └ eğilimi (eğim %.2f)' % et_[0])
a1.plot(xx, 4 * xx + KESIM_T, ':', color='#4ade80', lw=1.8, zorder=6,
        label='yalnız F4 asimptot (ilk sürüm, eğim 4)')
a1.plot(xx, eg_g * xx + ke_g, '--', color='#f87171', lw=1.8, zorder=4,
        label='gözlenen fit (eğim %.2f)' % eg_g)
a1.plot(np.log10(vL), lmL, '.', color='#7c3aed', ms=7, zorder=3, alpha=.85,
        label='ΛCDM zinciri (eğim %.2f)' % egL)
a1.set_xlabel('$\\log V_f$   (km/s)', fontsize=11)
a1.set_ylabel('$\\log M_{bar}$   ($M_\\odot$, $\\Upsilon_*{=}0{,}5$)', fontsize=11)
a1.set_title('Baryonik Tully-Fisher — pencereli resmî denklem (M-47)', fontsize=12.5,
             color='white', pad=9)
a1.legend(fontsize=8.4, framealpha=.2, loc='upper left')
a1.grid(alpha=.13)
dt = np.log10(v_tam / Vf)
a1.text(.97, .05, ('TAM formül:\n  $v_{öng}/v_{ölç}$ = %.3f\n  gereken $a_0$: ×%.2f\n'
                   '  (naif formül ×%.2f)\nilk sürüm: ×%.2f'
                   % (10 ** np.median(dt), K_TAM,
                      10 ** (-4 * np.median(dt)), K_ASI)).replace('.', ','),
        transform=a1.transAxes, ha='right', fontsize=9.4, color='#4ade80',
        family='monospace')

a2.set_facecolor('#121212')
et = ['ilk sürüm\nyalnız F4', 'RESMİ (M-47)\n$V_{bar}$+F4·W', 'gözlenen\n(ağırlıksız)',
      'gözlenen\n(ağırlıklı)', 'ΛCDM\nzinciri']
vv = [np.polyfit(np.log10(v_f4), lMb, 1)[0], np.polyfit(np.log10(v_tam), lMb, 1)[0],
      eg_g, eg_ga, egL]
cl = ['#4ade80', '#16a34a', '#ffcc00', '#fbbf24', '#7c3aed']
a2.bar(range(5), vv, .6, color=cl, zorder=4)
for i, v in enumerate(vv):
    a2.text(i, v + .06, '%.3f' % v, ha='center', fontsize=10.4, color=cl[i], fontweight='bold')
a2.axhspan(min(eg_g, eg_ga), max(eg_g, eg_ga), color='#ffcc00', alpha=.14, zorder=1)
a2.set_xticks(range(5))
a2.set_xticklabels(et, fontsize=9)
a2.set_ylabel('BTFR eğimi', fontsize=11)
a2.set_ylim(0, 4.5)
a2.set_title('Eğim: F1 eklenince teori gözlenene yaklaşıyor', fontsize=12.5, color='white', pad=9)
a2.grid(alpha=.13, axis='y')
a2.text(.98, .955, 'sarı bant = gözlenen aralık', transform=a2.transAxes, ha='right',
        fontsize=9, color='#fbbf24')

fig.suptitle('BTFR Sınavı (v3): Pencereli Resmî Denklem (M-47)', fontsize=14, color='white', y=.985)
fig.text(.5, .042, 'v3: Rankine penceresi (M-47) ve pencereli resmî $a_0=7{,}67\\times10^{-11}$ m/s$^2$ ile. '
                   '$\ell_\omega/R_{dış}$ medyan %.2f; $R_{dış}$'"'"'ta çoğu galakside $W=1$ — pencere BTFR yapısını değiştirmez. '
                   'F1 (SPARC ayrıştırmasından $V_{bar}$) dahildir.' % np.median(lom / Rout), ha='center',
         fontsize=9.2, color='#a1a1aa')
vg = lambda x: ('%.2f' % x).replace('.', ',')
fig.text(.5, .012, 'Gereken $a_0$ çarpanı ×%s (yarıçap duyarlılığı ×1,00–×1,11) — pencereli resmî kalibrasyonla '
                   'kurulum-A döneminin ×2,02 gerilimi kapanmıştır. Çarpan sayısal çözülmüştür; fit yoktur.'
                   % vg(K_TAM),
         ha='center', fontsize=9.2, color='#a1a1aa')
plt.tight_layout(rect=[0, .072, 1, .955])
plt.savefig(os.path.join(CIK, 'btfr.png'), dpi=150, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print('\n-> 97_BTFR/  SONUC.csv · btfr.png')
