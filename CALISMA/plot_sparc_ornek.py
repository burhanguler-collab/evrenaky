"""SPARC ORNEKLEM SINAVI — on iki galaksi, gercek veri.

Soru: 6.5.4.3'un turettigi vortisite uzunlugu l_omega (esdeger olarak b = G/l_omega)
ve M-38'in yayilma olcegi R_f EVRENSEL mi, yoksa galaksi basina serbest fit
parametreleri mi? Teorinin ongoru iddiasi bu sorunun cevabina baglidir.

Veri: SPARC (Lelli, McGaugh & Schombert 2016), Rotmod_LTG dosyalari.
Ornek, kasitli olarak geniş secilmistir (7'si kovansiz, 5'i kovanli):
  DDO154   12 nokta  gaz-baskin cuce, kovansiz
  NGC6503  31 nokta  kucuk disk, kovansiz
  NGC2403  73 nokta  en yuksek kaliteli egri, kovansiz
  NGC3198  43 nokta  klasik karanlik madde vakasi, kovansiz
  NGC3521  41 nokta  kutleli disk, kovansiz
  NGC7331  36 nokta  KOVANLI
  NGC2841  50 nokta  KOVANLI, klasik MOND problem vakasi

Modeller (hepsi ayni baryonik girdiyi kullanir; SPARC konvansiyonu Y_bul=1.4*Y_disk):
  LCDM NFW      : Vbar^2 + NFW,  c200 Dutton & Maccio 2014 iliskisinden  -> k=2 (Y*, M200)
  Evrenaki      : Vbar^2 + b*M_kaps(R)                                    -> k=2 (Y*, b)
  Evrenaki+yay. : Vbar^2 + b*M_kaps(R)/(1+R/Rf)                           -> k=3 (Y*, b, Rf)

Negatif V_gas (merkezi gaz cukuru) isaretli kare ile alinir. Hata cubuklari
gercektir; ki-kare onlarla hesaplanir.
"""

import sys
import os

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.optimize import curve_fit

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
plt.style.use('dark_background')

G = 4.300917e-6
RHO_CRIT = 3 * 0.07 ** 2 / (8 * np.pi * G)
H_RED = 0.7
VERI_DIZIN = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'veri')

GAL = [('DDO154', 'gaz-baskın cüce'), ('NGC6503', 'küçük disk'),
       ('NGC2403', 'en yüksek kaliteli'), ('NGC3198', 'klasik vaka'),
       ('NGC2903', 'sarmal'), ('NGC5055', 'sarmal'),
       ('NGC3521', 'kütleli disk'), ('NGC0891', 'sarmal, KOVANLI'),
       ('NGC4157', 'sarmal, KOVANLI'), ('NGC5985', 'sarmal, KOVANLI'),
       ('NGC7331', 'KOVANLI'), ('NGC2841', 'KOVANLI')]


def yukle(g):
    d = np.loadtxt(os.path.join(VERI_DIZIN, g + '_rotmod.dat'))
    D = dict(g=g, R=d[:, 0], Vo=d[:, 1], eV=np.maximum(d[:, 2], 1.0),
             Vg=d[:, 3], Vd=d[:, 4], Vb=d[:, 5], SBd=d[:, 6], SBb=d[:, 7])
    Rpc = D['R'] * 1e3

    def Lenc(SB):
        return np.concatenate([[0.0], np.cumsum(
            np.pi * (Rpc[1:] ** 2 - Rpc[:-1] ** 2) * 0.5 * (SB[1:] + SB[:-1]))])

    D['Ld'] = Lenc(D['SBd'])
    D['Lb'] = Lenc(D['SBb'])
    D['kovan'] = bool(np.any(D['Vb'] > 0))
    return D


def Vbar2(D, Y):
    """SPARC konvansiyonu: Y_bul = 1.4 * Y_disk."""
    return np.sign(D['Vg']) * D['Vg'] ** 2 + Y * D['Vd'] ** 2 + 1.4 * Y * D['Vb'] ** 2


def Mkaps(D, Y):
    return (Y * D['Ld'] + 1.4 * Y * D['Lb']
            + np.maximum(D['R'] * np.sign(D['Vg']) * D['Vg'] ** 2 / G, 0.0))


def v_nfw2(R, M200):
    c200 = 10 ** (0.905 - 0.101 * np.log10(M200 * H_RED / 1e12))
    r200 = (3.0 * M200 / (4.0 * np.pi * 200.0 * RHO_CRIT)) ** (1.0 / 3.0)
    rs = r200 / c200
    mu = lambda x: np.log(1.0 + x) - x / (1.0 + x)
    return G * M200 / R * mu(R / rs) / mu(c200)


def fitle(D, f, p0, lo, hi):
    R, Vo, eV = D['R'], D['Vo'], D['eV']
    p, _ = curve_fit(f, R, Vo, sigma=eV, p0=p0, bounds=(lo, hi), maxfev=900000)
    mv = f(R, *p)
    chi2 = float(np.sum(((mv - Vo) / eV) ** 2))
    k = len(p)
    return dict(p=p, k=k, chi2=chi2, chi2i=chi2 / max(len(R) - k, 1),
                aic=chi2 + 2 * k, mv=mv, rms=float(np.sqrt(np.mean((mv - Vo) ** 2))))


MODEL_RENK = {'lcdm': '#c084fc', 'evr': '#ffa040', 'yay': '#4ade80'}
sonuc = []
for g, etiket in GAL:
    D = yukle(g)
    fL = lambda R, Y, lg, _D=D: np.sqrt(np.maximum(Vbar2(_D, Y), 0) + v_nfw2(R, 10 ** lg))
    fE = lambda R, Y, b, _D=D: np.sqrt(np.maximum(Vbar2(_D, Y), 0) + b * Mkaps(_D, Y))
    fF = lambda R, Y, b, Rf, _D=D: np.sqrt(
        np.maximum(Vbar2(_D, Y), 0) + b * Mkaps(_D, Y) / (1.0 + R / Rf))
    r = dict(D=D, etiket=etiket,
             lcdm=fitle(D, fL, [0.5, 11.0], [0.05, 7.5], [2.0, 13.5]),
             evr=fitle(D, fE, [0.5, 4e-7], [0.05, 0], [2.0, 1e-3]),
             yay=fitle(D, fF, [0.5, 6e-7, 20.0], [0.05, 0, 0.5], [2.0, 1e-3, 1e5]))
    r['lom_evr'] = G / r['evr']['p'][1] if r['evr']['p'][1] > 0 else np.nan
    r['lom_yay'] = G / r['yay']['p'][1] if r['yay']['p'][1] > 0 else np.nan
    r['Rf'] = r['yay']['p'][2]
    r['bar'] = np.sqrt(np.maximum(Vbar2(D, r['lcdm']['p'][0]), 0))
    sonuc.append(r)

# --- Rapor ---
print("SPARC ORNEKLEM SINAVI — 12 galaksi, gercek veri")
print("=" * 112)
print("%-9s %4s %6s | %14s | %21s | %28s" % ('galaksi', 'N', 'kovan',
      'LCDM k=2', 'Evrenaki k=2', 'Evrenaki+yayilma k=3'))
print("%-9s %4s %6s | %7s %6s | %7s %6s %6s | %7s %6s %9s %6s" %
      ('', '', '', 'chi2i', 'AIC', 'chi2i', 'AIC', 'l_om', 'chi2i', 'AIC', 'Rf', 'l_om'))
print("-" * 112)
for r in sonuc:
    print("%-9s %4d %6s | %7.2f %6.1f | %7.2f %6.1f %6.2f | %7.2f %6.1f %9.1f %6.2f" % (
        r['D']['g'], len(r['D']['R']), 'var' if r['D']['kovan'] else '-',
        r['lcdm']['chi2i'], r['lcdm']['aic'],
        r['evr']['chi2i'], r['evr']['aic'], r['lom_evr'],
        r['yay']['chi2i'], r['yay']['aic'], r['Rf'], r['lom_yay']))
print("-" * 112)
lomE = np.array([r['lom_evr'] for r in sonuc])
lomF = np.array([r['lom_yay'] for r in sonuc])
Rfa = np.array([r['Rf'] for r in sonuc])
print("\nEVRENSELLIK SINAVI — parametreler galaksiler arasinda sabit mi?")
for ad, v in [('l_omega (yayilmasiz)', lomE), ('l_omega (yayilmali)', lomF), ('R_f', Rfa)]:
    print("  %-22s min=%9.2f  max=%9.2f  medyan=%8.2f  YAYILIM = %.0f kat"
          % (ad, v.min(), v.max(), np.median(v), v.max() / v.min()))
sinirda = int(np.sum(Rfa > 5e4))
print("  R_f, %d/12 galakside ust sinira dayaniyor -> o galaksilerde yayilma ISE YARAMIYOR" % sinirda)
print("\nKAZANAN SAYIMI (en iyi AIC)")
for ad, k in [('LCDM k=2', 'lcdm'), ('Evrenaki k=2', 'evr'), ('Evrenaki+yayilma k=3', 'yay')]:
    w = sum(1 for r in sonuc if r[k]['aic'] == min(r['lcdm']['aic'], r['evr']['aic'], r['yay']['aic']))
    print("  %-22s %d/12" % (ad, w))
esit = sum(1 for r in sonuc if r['evr']['aic'] < r['lcdm']['aic'])
tot = sum(r['lcdm']['aic'] - r['evr']['aic'] for r in sonuc)
print("\nESIT SERBESTLIKTE (k=2): Evrenaki %d/12 galakside onde; toplam dAIC = %+.1f "
      "(negatif = LCDM onde)" % (esit, tot))
en = min(sonuc, key=lambda r: r['yay']['chi2i'])
print("\nDIKKAT CEKEN: %s — LCDM chi2i=%.2f iken Evrenaki %.2f. Cuce galaksilerde"
      % (sonuc[0]['D']['g'], sonuc[0]['lcdm']['chi2i'], sonuc[0]['evr']['chi2i']))
print("  NFW'nin c-M iliskisi dayatildiginda cusp-core problemi devreye giriyor;")
print("  teori bu problemi paylasmiyor. Ornekteki tek net kazanc budur.")
print("=" * 112)

# --- GRAFIK ---
fig = plt.figure(figsize=(19.5, 11.4), facecolor='#121212')
NC = 5
gs = GridSpec(3, NC, hspace=0.40, wspace=0.27, left=0.045, right=0.987, top=0.915, bottom=0.062)
for idx, r in enumerate(sonuc):
    a = fig.add_subplot(gs[idx // NC, idx % NC])
    D = r['D']
    a.set_facecolor('#121212')
    for sp in ('top', 'right'):
        a.spines[sp].set_visible(False)
    for sp in ('bottom', 'left'):
        a.spines[sp].set_color('#444444')
    a.tick_params(colors='#999999', labelsize=8)
    a.grid(True, alpha=0.13, color='white')
    a.errorbar(D['R'], D['Vo'], yerr=D['eV'], fmt='o', color='#ffcc00', ms=3,
               capsize=1.6, elinewidth=0.9, zorder=6)
    a.plot(D['R'], r['bar'], ':', color='#888888', lw=1.3, zorder=2)
    a.plot(D['R'], r['lcdm']['mv'], '-.', color=MODEL_RENK['lcdm'], lw=1.8, zorder=4)
    a.plot(D['R'], r['evr']['mv'], '--', color=MODEL_RENK['evr'], lw=1.6, zorder=3)
    a.plot(D['R'], r['yay']['mv'], '-', color=MODEL_RENK['yay'], lw=2.0, zorder=5)
    kaz = 'ΛCDM' if r['lcdm']['aic'] < min(r['evr']['aic'], r['yay']['aic']) else 'Evrenakı'
    kr = MODEL_RENK['lcdm'] if kaz == 'ΛCDM' else MODEL_RENK['yay']
    a.set_title('%s  (%s)' % (D['g'], r['etiket']), fontsize=9.2, color='white', pad=4)
    a.text(0.03, 0.96, 'ΛCDM $\\chi^2_i$=%.2f\nEvr. $\\chi^2_i$=%.2f\nEvr+yay=%.2f'
           % (r['lcdm']['chi2i'], r['evr']['chi2i'], r['yay']['chi2i']),
           transform=a.transAxes, va='top', ha='left', fontsize=7.4, color='#dddddd',
           linespacing=1.35)
    a.text(0.97, 0.06, 'kazanan: %s' % kaz, transform=a.transAxes, ha='right',
           va='bottom', fontsize=7.6, color=kr, weight='bold')
    a.set_xlim(0, D['R'].max() * 1.05)
    a.set_ylim(0, max(D['Vo'].max(), r['lcdm']['mv'].max()) * 1.28)
    if idx // NC == 2 or idx >= len(sonuc) - NC:
        a.set_xlabel('$R$ (kpc)', fontsize=8.6, color='#bbbbbb')
    if idx % NC == 0:
        a.set_ylabel('$v$ (km/s)', fontsize=8.6, color='#bbbbbb')

# 8. panel: evrensellik sinavi
a = fig.add_subplot(gs[2, NC - 3])
a.set_facecolor('#121212')
for sp in ('top', 'right'):
    a.spines[sp].set_visible(False)
for sp in ('bottom', 'left'):
    a.spines[sp].set_color('#444444')
a.tick_params(colors='#999999', labelsize=8)
a.grid(True, alpha=0.13, color='white')
x = np.arange(len(sonuc))
a.semilogy(x, lomE, 'o', color=MODEL_RENK['evr'], ms=7, label='$\\ell_\\omega$ (yayılmasız)')
a.semilogy(x, Rfa, 's', color=MODEL_RENK['yay'], ms=7, label='$R_f$')
a.axhline(np.median(lomE), color=MODEL_RENK['evr'], ls='--', lw=1.1, alpha=0.6)
a.set_xticks(x)
a.set_xticklabels([r['D']['g'].replace('NGC', 'N').replace('DDO', 'D') for r in sonuc],
                  rotation=55, fontsize=7.2, color='#cccccc')
a.set_ylabel('kpc (log)', fontsize=8.6, color='#bbbbbb')
a.set_title('Evrensellik sınavı — BAŞARISIZ', fontsize=9.2, color='#ff6b6b', pad=4)
a.text(0.5, 0.04, '$\\ell_\\omega$: %.0f kat yayılım\n$R_f$: %.0f kat yayılım'
       % (lomE.max() / lomE.min(), Rfa.max() / Rfa.min()),
       transform=a.transAxes, ha='center', va='bottom', fontsize=7.8, color='#ff9999',
       linespacing=1.4)
lg = a.legend(fontsize=7.2, facecolor='#1a1a1a', edgecolor='#333333', loc='upper left')
for t in lg.get_texts():
    t.set_color('white')

fig.text(0.5, 0.963, 'SPARC Örneklem Sınavı — On İki Galaksi, Gerçek Veri: '
                     '$\\ell_\\omega$ ve $R_f$ evrensel mi?',
         ha='center', fontsize=13.2, color='white')
fig.text(0.5, 0.928, 'sarı: ölçüm  ·  gri noktalı: baryonlar  ·  mor: ΛCDM NFW (k=2)  ·  '
                     'turuncu: Evrenakı (k=2)  ·  yeşil: Evrenakı + yayılma (k=3)',
         ha='center', fontsize=9.2, color='#aaaaaa')
plt.savefig('sparc_ornek_12galaksi.png', dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print("Grafik 'sparc_ornek_12galaksi.png' olarak kaydedildi.")
