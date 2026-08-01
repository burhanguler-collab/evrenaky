"""NGC 3198 — GERCEK SPARC VERISIYLE SINAV.

Veri: SPARC (Lelli, McGaugh & Schombert 2016), Rotmod_LTG/NGC3198_rotmod.dat
      43 nokta, 0.32-44.08 kpc, gercek hata cubuklari, D = 13.8 Mpc.
      Sutunlar: Rad, Vobs, errV, Vgas, Vdisk, Vbul, SBdisk, SBbul
      V_disk, M/L = 1 icin verilir; olcekleme Y* (=M/L) ile sqrt(Y*) uzerinden.
      SPARC Bulges.mrt: NGC 3198 icin L_bul = 0.0  ->  KOVANSIZ galaksi.
      Negatif V_gas, merkezi gaz cukurunun ice dogru katkisidir; isaretli kare alinir.

ONEMLI DUZELTME KAYDI:
  Bu betikten onceki analizler NGC 3198 icin TEMSILI (uydurma) bir donus egrisi
  kullaniyordu ve o veri ic bolgeyi 47-65 km/s FAZLA gosteriyordu. Gercek veride
  ic bolgede V_disk > V_obs, yani baryonlar eksik degil FAZLADIR. Dolayisiyla
  "ic kol acigi" diye arastirilan sorun var olmayan bir sorundu; onun icin
  onerilen mekanizmalar (kovan zorlamasi, deplasman fazlasi, degisken alpha,
  ivmeye bagli F1) gereksizdir ve geri alinmistir.

MODELLER (hepsi ayni baryonik girdiyi kullanir, Y* serbest):
  1) Yalniz baryonlar          : v^2 = sgn(Vg)Vg^2 + Y* Vd^2
  2) LCDM NFW                  : + NFW halo, c200 simulasyon iliskisinden
                                 (Dutton & Maccio 2014) -> tek serbest: M200
  3) Evrenaki F1+F4            : + b*M_kaps(R)   (M-38 silindirik aki, kaynak =
                                 kapsanan nukleon motorlari, Bolum 3.1)
  4) Evrenaki + M-38 yayilmasi : + b*M_kaps(R)/(1+R/Rf)
                                 M-38'in kendi yanlislanabilir sonucu: diskler
                                 disa dogru kalinlasir (h artar), akı yogunlugu
                                 1/R'den hizli duser, egri duzlukten sapar.
  5) MOND (kiyas)              : a = a_N*nu(a_N/a0), a0 = c*H0/(2pi)

M_kaps: yildiz kismi SBdisk profilinin integralinden (L/pc^2 -> Msun, x Y*),
gaz kismi kuresel esdeger R*Vg^2/G ile. Hatalar gercek errV; ki-kare bunlarla.

UYARI: R_f burada FITLENIR, gozlenen h(R) profilinden alinmaz. Dolayisiyla
M-38'in yayilma ongorusu burada dogrulanmis degil, yalnizca basarili bir fit
vermistir. Gercek sinav 21 cm kalinlik profilini girdi olarak kullanmaktir.
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
C_SI = 2.99792458e8
KPC_M = 3.0856776e19
ACC = 1e6 / KPC_M
H0_SI = 70e3 / 3.0857e22
A0 = (C_SI * H0_SI / (2 * np.pi)) / ACC          # (km/s)^2/kpc
RHO_CRIT = 3 * 0.07 ** 2 / (8 * np.pi * G)
H_RED = 0.7

VERI = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'veri', 'NGC3198_rotmod.dat')
d = np.loadtxt(VERI)
R, Vo, eV, Vg, Vd, Vb, SBd = d[:, 0], d[:, 1], d[:, 2], d[:, 3], d[:, 4], d[:, 5], d[:, 6]
N = len(R)

# Eski (uydurma) temsili veri — duzeltme kaydi paneli icin
r_eski = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 12.0, 14.0,
                   16.0, 18.0, 20.0, 22.0, 24.0, 26.0, 28.0, 30.0])
v_eski = np.array([110, 134, 145, 147, 148, 152, 156, 153, 155, 156,
                   157, 153, 154, 151, 149, 148, 146, 147], dtype=float)


def Vbar2(Y):
    """Baryonik katki. Negatif V_gas = merkezi gaz cukuru -> isaretli kare."""
    return np.sign(Vg) * Vg ** 2 + Y * Vd ** 2


# Kapsanan baryonik kutle (F4'un kaynagi)
Rpc = R * 1e3
Lenc = np.concatenate([[0.0], np.cumsum(
    np.pi * (Rpc[1:] ** 2 - Rpc[:-1] ** 2) * 0.5 * (SBd[1:] + SBd[:-1]))])


def Mkaps(Y):
    return Y * Lenc + np.maximum(R * np.sign(Vg) * Vg ** 2 / G, 0.0)


def nu_mond(x):
    return 0.5 + np.sqrt(0.25 + 1.0 / x)


# --- Modeller ---
def m_baryon(R_, Y):
    return np.sqrt(np.maximum(Vbar2(Y), 1e-9))


def m_lcdm(R_, Y, M200):
    c200 = 10 ** (0.905 - 0.101 * np.log10(M200 * H_RED / 1e12))
    r200 = (3.0 * M200 / (4.0 * np.pi * 200.0 * RHO_CRIT)) ** (1.0 / 3.0)
    rs = r200 / c200
    mu = lambda x: np.log(1.0 + x) - x / (1.0 + x)
    return np.sqrt(np.maximum(Vbar2(Y), 0) + G * M200 / R_ * mu(R_ / rs) / mu(c200))


def m_evr(R_, Y, b):
    return np.sqrt(np.maximum(Vbar2(Y), 0) + b * Mkaps(Y))


def m_evr_flare(R_, Y, b, Rf):
    return np.sqrt(np.maximum(Vbar2(Y), 0) + b * Mkaps(Y) / (1.0 + R_ / Rf))


def m_mond(R_, Y):
    aN = np.maximum(Vbar2(Y), 1e-9) / R_
    return np.sqrt(R_ * aN * nu_mond(aN / A0))


modeller = [
    dict(ad='Yalnız baryonlar (F1, karanlık madde yok)', kisa='baryonlar',
         fn=m_baryon, p0=[0.5], lo=[0.05], hi=[2.0],
         renk='#888888', bicem=':', lw=1.9, zorder=3),
    dict(ad='MOND (kıyas)', kisa='MOND',
         fn=m_mond, p0=[0.5], lo=[0.05], hi=[2.0],
         renk='#f472b6', bicem=(0, (1, 1.4)), lw=1.9, zorder=4),
    dict(ad='ΛCDM NFW — $c_{200}$ simülasyon ilişkisinden', kisa='ΛCDM NFW',
         fn=m_lcdm, p0=[0.5, 1e11], lo=[0.05, 1e8], hi=[2.0, 1e13],
         renk='#c084fc', bicem='-.', lw=2.4, zorder=6),
    dict(ad='Evrenakı F1+F4 — $b\\,M_{kaps}(R)$', kisa='Evrenakı (yayılmasız)',
         fn=m_evr, p0=[0.5, 4e-7], lo=[0.05, 0], hi=[2.0, 1e-4],
         renk='#ffa040', bicem='--', lw=2.2, zorder=5),
    dict(ad='Evrenakı + M-38 yayılması — $b\\,M_{kaps}/(1{+}R/R_f)$',
         kisa='Evrenakı + yayılma',
         fn=m_evr_flare, p0=[0.5, 6e-7, 30.0], lo=[0.05, 0, 1.0], hi=[2.0, 1e-4, 1e5],
         renk='#4ade80', bicem='-', lw=3.0, zorder=8),
]

for m in modeller:
    popt, _ = curve_fit(m['fn'], R, Vo, sigma=eV, p0=m['p0'],
                        bounds=(m['lo'], m['hi']), maxfev=900000)
    m['popt'] = popt
    m['npar'] = len(popt)
    m['mv'] = m['fn'](R, *popt)
    m['artik'] = m['mv'] - Vo
    m['sigma_artik'] = m['artik'] / eV
    m['rms'] = np.sqrt(np.mean(m['artik'] ** 2))
    m['chi2'] = np.sum((m['artik'] / eV) ** 2)
    m['chi2_ind'] = m['chi2'] / (N - m['npar'])
    m['aic'] = m['chi2'] + 2 * m['npar']

d_ = {m['kisa']: m for m in modeller}
aic_min = min(m['aic'] for m in modeller)

# --- Rapor ---
print("NGC 3198 — GERCEK SPARC VERISIYLE SINAV  (43 nokta, gercek hatalar)")
print("=" * 100)
print(f"{'model':<48}{'k':>3}{'RMS':>8}{'chi2_ind':>10}{'AIC':>9}{'dAIC':>8}")
for m in modeller:
    print(f"{m['ad'][:47]:<48}{m['npar']:3d}{m['rms']:8.2f}{m['chi2_ind']:10.2f}"
          f"{m['aic']:9.1f}{m['aic'] - aic_min:+8.1f}")
print("-" * 100)
for m in modeller:
    print(f"  {m['kisa']:<24} parametreler: "
          + ", ".join(f"{x:.4g}" for x in m['popt']))
print("-" * 100)
en_iyi = min(modeller, key=lambda m: m['aic'])
print(f"EN IYI: {en_iyi['ad']}  ->  chi2_ind = {en_iyi['chi2_ind']:.2f}, AIC = {en_iyi['aic']:.1f}")
print(f"  LCDM'e gore dAIC = {d_['ΛCDM NFW']['aic'] - en_iyi['aic']:+.1f} (Evrenaki lehine)")
print(f"  yayilma R_f = {d_['Evrenakı + yayılma']['popt'][2]:.1f} kpc  "
      f"(disk olcek uzunlugunun ~{d_['Evrenakı + yayılma']['popt'][2] / 3.14:.1f} kati)")
ic = R < 3
print(f"  ic bolge (R<3 kpc) V_disk > V_obs olan nokta sayisi: "
      f"{np.sum((Vd > Vo) & ic)}/{np.sum(ic)}  -> baryonlar FAZLA")
print("=" * 100)

# --- GRAFIK ---
fig = plt.figure(figsize=(15.5, 9.0), facecolor='#121212')
gsL = GridSpec(2, 1, height_ratios=[3, 1.5], hspace=0.09,
               left=0.055, right=0.605, top=0.925, bottom=0.078)
gsR = GridSpec(2, 1, height_ratios=[1, 1], hspace=0.42,
               left=0.685, right=0.985, top=0.925, bottom=0.078)
ax = fig.add_subplot(gsL[0])
axr = fig.add_subplot(gsL[1], sharex=ax)
axa = fig.add_subplot(gsR[0])
axd = fig.add_subplot(gsR[1])
for a_ in (ax, axr, axa, axd):
    a_.set_facecolor('#121212')
    a_.spines['top'].set_visible(False)
    a_.spines['right'].set_visible(False)
    a_.spines['bottom'].set_color('#444444')
    a_.spines['left'].set_color('#444444')
    a_.tick_params(colors='#aaaaaa')
    a_.grid(True, alpha=0.15, color='white')

# (1) donus egrisi
Rs = np.linspace(R.min(), R.max(), 400)
ax.errorbar(R, Vo, yerr=eV, fmt='o', color='#ffcc00', capsize=3, markersize=5,
            elinewidth=1.2, zorder=10, label='SPARC ölçüm (43 nokta, gerçek hatalar)')
for m in modeller:
    ax.plot(R, m['mv'], color=m['renk'], ls=m['bicem'], lw=m['lw'], zorder=m['zorder'],
            label=f"{m['ad']}  ({m['npar']} par., $\\chi^2_{{ind}}$ {m['chi2_ind']:.2f})")
ax.set_title('NGC 3198 — Gerçek SPARC Verisiyle Sınav (kovansız galaksi, $L_{bul}=0$)',
             fontsize=12.6, pad=13, color='white')
ax.set_ylabel('Yörünge Hızı — $v$ (km/s)', fontsize=11.5, color='#cccccc')
ax.set_ylim(0, 185)
ax.set_xlim(0, 46)
lg = ax.legend(fontsize=9.0, facecolor='#1a1a1a', edgecolor='#333333', loc='lower right')
for t in lg.get_texts():
    t.set_color('white')

# (2) sigma cinsinden artiklar (hatalar cok degistigi icin normalize)
axr.axhline(0, color='#ffcc00', lw=1.2, alpha=0.85)
axr.fill_between([0, 46], -1, 1, color='#ffcc00', alpha=0.14, label='$\\pm1\\sigma$')
for m in modeller:
    if m['kisa'] in ('baryonlar', 'MOND'):
        continue
    axr.plot(R, m['sigma_artik'], 'o', ls=m['bicem'], color=m['renk'],
             ms=4.2, lw=1.7, zorder=m['zorder'], label=m['kisa'])
axr.set_xlabel('Merkezden Uzaklık — $R$ (kpc)', fontsize=11.5, color='#cccccc')
axr.set_ylabel('(Hesap − Ölçüm) / $\\sigma$', fontsize=10, color='#cccccc')
axr.set_ylim(-6, 6)
lg2 = axr.legend(fontsize=8.0, facecolor='#1a1a1a', edgecolor='#333333',
                 loc='lower right', ncol=4)
for t in lg2.get_texts():
    t.set_color('white')

# (3) AIC
sirali = sorted(modeller, key=lambda m: m['aic'])
ypos = np.arange(len(sirali))
axa.barh(ypos, [m['aic'] for m in sirali], color=[m['renk'] for m in sirali],
         alpha=0.88, height=0.6)
for yy, m in zip(ypos, sirali):
    axa.text(m['aic'] * 1.06 + 20, yy, f"{m['aic']:.0f}", va='center',
             color='#dddddd', fontsize=8.6)
axa.set_yticks(ypos)
axa.set_yticklabels([f"{m['kisa']}\n(k={m['npar']})" for m in sirali],
                    fontsize=8.0, color='#cccccc')
axa.invert_yaxis()
axa.set_xscale('log')
axa.set_xlabel('AIC  (küçük = iyi, log ölçek)', fontsize=9.5, color='#bbbbbb')
axa.set_title('Model seçimi — gerçek veriyle', fontsize=10.2, color='white', pad=7)

# (4) DUZELTME KAYDI: uydurma veri vs gercek veri
axd.errorbar(R, Vo, yerr=eV, fmt='o', color='#ffcc00', capsize=2.5, markersize=4,
             elinewidth=1.0, zorder=5, label='SPARC (gerçek)')
axd.plot(r_eski, v_eski, 's--', color='#ff5555', ms=5, lw=1.8, zorder=6,
         label='önceki "temsilî" veri (hatalı)')
axd.plot(R, Vd, '-', color='#7dd3fc', lw=1.6, zorder=4,
         label='$V_{disk}$ ($M/L{=}1$, Spitzer)')
axd.axvspan(0, 3, color='#ff5555', alpha=0.10, zorder=0)
axd.annotate('iç bölgede 47–65 km/s\nfazla gösteriyordu', xy=(2.0, 90), xytext=(9, 42),
             color='#ff8888', fontsize=8.4,
             arrowprops=dict(arrowstyle='->', color='#ff8888', lw=1.2))
axd.set_title('Düzeltme kaydı: veri hatası', fontsize=10.2, color='white', pad=7)
axd.set_xlabel('$R$ (kpc)', fontsize=9.5, color='#bbbbbb')
axd.set_ylabel('$v$ (km/s)', fontsize=9.5, color='#bbbbbb')
axd.set_xlim(0, 32)
axd.set_ylim(0, 180)
lg4 = axd.legend(fontsize=7.6, facecolor='#1a1a1a', edgecolor='#333333', loc='lower right')
for t in lg4.get_texts():
    t.set_color('white')

plt.savefig('sparc_ngc3198.png', dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print("Grafik 'sparc_ngc3198.png' olarak kaydedildi.")
