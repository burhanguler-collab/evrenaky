"""KARA DELIKLERDE MERKEZ KUTLE — uc yol, gercek olculmus degerlerle.

Teoride merkez kutle temel bir buyukluk degildir: M = rho_n * V_deplase.
Uc olcum yolu dogar. Bu betik uculden SADECE kara deliklere uygulanabilir
olanlari sinar.

  YOL 1  KINEMATIK   : M = v^2 r / G. Aki korunumu geregi (6.5.2.1) alpha sabit
                       oldugundan standart astronomiyle BIREBIR AYNI sayiyi verir.
                       Bagimsiz bir el vermez — ama Yol 3 ile capraz denetlenebilir.

  YOL 2  GEOMETRIK   : r_cep = (3M / 4*pi*rho_n)^(1/3). Kara deliklerde
                       KESIN OLARAK BASARISIZ: 10^4-10^6 kat kucuk cikar.

  YOL 3  BASINC KUYUSU: P(r) = P0 - alpha*M/r.  P(r)=0 olan yarıcap:
                            r_kilit = alpha*M / P0
                       Simdi kritik nokta — alpha ve P0 bagimsiz sabitlenmistir:
                            alpha = G*rho_n                      (4.2.4)
                            P0    = ((1-k)/4) * rho_n * c^2      (Ek B.3, k=0)
                       Bunlari yerine koyunca rho_n TAMAMEN SADELESIR:
                            r_kilit = G*rho_n*M / (rho_n c^2/4) = 4GM/c^2 = 2 r_s
                       SIFIR serbest parametre, SIFIR yeni varsayim. Ustelik P0
                       zayif alan isik bukulmesinden (delta_c/c = 2Phi/c^2)
                       sabitlenmisti — yani ~10^-6 mertebesinde bir etkiden
                       kalibre edilen normalizasyon, hicbir ayar yapilmadan
                       guclu alanda 2 r_s veriyor. Bu bir EKSTRAPOLASYONDUR.

  GR karsilastirmasi:  olay ufku      r_s      = 2GM/c^2
                       foton kuresi   1.5 r_s  = 3GM/c^2
                       TEORI KILIDI   2.0 r_s  = 4GM/c^2   <-- bu betigin konusu
                       golge yaricapi 2.598 r_s = 3*sqrt(3) GM/c^2
                       golge / kilit  = 3*sqrt(3)/4 = 1.2990   (saf sayi)

Olculmus boyut verisi — dunyada yalnizca IKI kara delik icin vardir:
  Sgr A*  M=4.297e6 +/-0.042e6 Msun [GRAVITY Collab. 2022]
          halka capi 51.8 +/- 2.3 uas, golge capi 48.7 +/- 7 uas [EHT 2022]
          D = 8.277 +/- 0.033 kpc [GRAVITY 2021]
  M87*    M=6.5e9 +/- 0.7e9 Msun, halka capi 42 +/- 3 uas,
          D = 16.8 +/- 0.8 Mpc [EHT Collab. 2019]

Yalnizca dinamik kutlesi olculmus kara delikler (merdiven paneli icin):
  Cyg X-1        21.2 +/- 2.2   [Miller-Jones+2021]
  GW150914 kal.  62   +/- 4     [Abbott+2016]
  GW190521 kal.  142  +/- 30    [Abbott+2020]
  NGC 4258       4.00e7 +/-0.09e7 [Humphreys+2013, maser — en kesin olcum]
  M31*           1.4e8          [Bender+2005]
  NGC 1332       1.47e9         [Barth+2016]
  NGC 4889       2.1e10         [McConnell+2011]
  TON 618        6.6e10         [Shemmer+2004]
"""

import sys

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
plt.style.use('dark_background')

G = 6.674e-11
C = 2.99792458e8
MSUN = 1.989e30
RHO_N = 2.702e17                  # Ek B.3
K_PAR = 0.0                       # Ek M-44: deplasman basinci degistirir, yogunlugu degil
P0 = (1.0 - K_PAR) / 4.0 * RHO_N * C ** 2
ALPHA = G * RHO_N
PC = 3.0857e16
UAS = np.pi / (180.0 * 3600.0 * 1e6)
GOLGE_KAT = 3.0 * np.sqrt(3.0) / 4.0      # GR golgesi / teori kilidi = 1.2990


def r_s(M):
    return 2.0 * G * M * MSUN / C ** 2


def r_kilit(M):
    """Yol 3: P(r)=0 olan yaricap. Cebirsel olarak 4GM/c^2 = 2 r_s."""
    return ALPHA * M * MSUN / P0


def r_cep(M):
    """Yol 2: deplase hacmin kure yaricapi."""
    return (3.0 * M * MSUN / (4.0 * np.pi * RHO_N)) ** (1.0 / 3.0)


# --- olculmus boyutu olan iki kara delik ---
# ad, M, dM, halka capi (uas), d(uas), D (m), dD/D
OLCUM = [
    ('Sgr A*', 4.297e6, 0.042e6, 51.8, 2.3, 8.277e3 * PC, 0.0040, 'GRAVITY22 / EHT22'),
    ('M87*', 6.5e9, 0.7e9, 42.0, 3.0, 16.8e6 * PC, 0.0476, 'EHT 2019'),
]
# yalnizca dinamik kutle
DINAMIK = [('Cyg X-1', 21.2), ('GW150914', 62.0), ('GW190521', 142.0),
           ('NGC 4258', 4.00e7), ('M31*', 1.4e8), ('NGC 1332', 1.47e9),
           ('NGC 4889', 2.1e10), ('TON 618', 6.6e10)]

print("KARA DELIKLERDE MERKEZ KUTLE — UC YOL")
print("=" * 96)
print("rho_n = %.4e kg/m^3    k = %.0f" % (RHO_N, K_PAR))
print("alpha = G*rho_n        = %.5e s^-2" % ALPHA)
print("P0    = (1-k)/4 rho_n c^2 = %.5e Pa" % P0)
print("-" * 96)
print("YOL 3'UN KIMLIGI — rho_n sadelesiyor:")
print("  r_kilit = alpha*M/P0 = 4GM/c^2 ;  r_kilit/r_s = %.6f  (tam olarak 2 olmali)"
      % (r_kilit(1.0) / r_s(1.0)))
print("  GR golge yaricapi / r_kilit = 3*sqrt(3)/4 = %.4f" % GOLGE_KAT)
print("=" * 96)
print("YOL 3 SINAVI — olculmus halka yaricapi vs 4GM/c^2 (sifir serbest parametre)")
print("%-9s %11s %13s %13s %9s %9s" % ('cisim', 'M/Msun', 'halka R (m)', 'r_kilit (m)',
                                       'oran', 'sapma'))
oranlar, hatalar = [], []
for ad, M, dM, uas, duas, D, dD, kyn in OLCUM:
    Rh = 0.5 * uas * UAS * D
    dRh = Rh * np.sqrt((duas / uas) ** 2 + dD ** 2)
    rk = r_kilit(M)
    o = Rh / rk
    do = o * np.sqrt((duas / uas) ** 2 + dD ** 2 + (dM / M) ** 2)
    oranlar.append(o); hatalar.append(do)
    print("%-9s %11.4g %13.4e %13.4e %9.3f %8.2fσ"
          % (ad, M, Rh, rk, o, abs(o - GOLGE_KAT) / do))
w = 1.0 / np.array(hatalar) ** 2
om = float(np.sum(w * np.array(oranlar)) / np.sum(w))
osd = float(1.0 / np.sqrt(np.sum(w)))
print("-" * 96)
print("  agirlikli ortalama oran = %.4f +/- %.4f   (GR beklentisi 3sqrt(3)/4 = %.4f)"
      % (om, osd, GOLGE_KAT))
print("  sapma = %.2f sigma  -> %s" % (abs(om - GOLGE_KAT) / osd,
                                       'UYUMLU' if abs(om - GOLGE_KAT) / osd < 2 else 'UYUMSUZ'))
print("=" * 96)
print("YOL 2 SINAVI — ayni iki cisimde geometrik yol")
for ad, M, dM, uas, duas, D, dD, kyn in OLCUM:
    Rh = 0.5 * uas * UAS * D
    print("  %-9s r_cep = %.4e m   halka/r_cep = %.3e   <- %s"
          % (ad, r_cep(M), Rh / r_cep(M), 'BASARISIZ'))
print("=" * 96)
print("YOL 1 — kinematik: standart degerlerle birebir ayni (bagimsiz el yok)")
print("  Sgr A* S2 yorungesi:  M = 4.297e6 Msun  (teoride ayni sayi, farkli yorum)")
print("  M87* yildiz dinamigi: M = 6.5e9 Msun    (gaz dinamigi 3.5e9 ile gerilimli)")
print("=" * 96)

# ============================== GRAFIK ==============================
fig = plt.figure(figsize=(17.6, 9.0), facecolor='#121212')
gs = GridSpec(2, 3, hspace=0.34, wspace=0.235, height_ratios=[1.30, 1.0],
              left=0.050, right=0.986, top=0.872, bottom=0.055)
axA = fig.add_subplot(gs[0, 0])
axB = fig.add_subplot(gs[0, 1])
axC = fig.add_subplot(gs[0, 2])
axD = fig.add_subplot(gs[1, :])
for a in (axA, axB, axC, axD):
    a.set_facecolor('#121212')
    for sp in ('top', 'right'):
        a.spines[sp].set_visible(False)
    for sp in ('bottom', 'left'):
        a.spines[sp].set_color('#444444')
    a.tick_params(colors='#aaaaaa', labelsize=8.6)
    a.grid(True, alpha=0.13, color='white')

# --- (A) Yol 3 sinavi: olculen halka vs 4GM/c^2 ---
xx = np.logspace(9.6, 14.2, 50)
axA.loglog(xx, xx, ':', color='#888888', lw=1.4, label='1:1 (kilit = halka)')
axA.loglog(xx, GOLGE_KAT * xx, '-', color='#4ade80', lw=2.2,
           label='öngörü: halka $=\\frac{3\\sqrt{3}}{4}r_{kilit}$ (%.3f)' % GOLGE_KAT)
for ad, M, dM, uas, duas, D, dD, kyn in OLCUM:
    Rh = 0.5 * uas * UAS * D
    dRh = Rh * np.sqrt((duas / uas) ** 2 + dD ** 2)
    rk = r_kilit(M)
    axA.errorbar(rk, Rh, yerr=dRh, xerr=rk * dM / M, fmt='o', color='#ffcc00',
                 ms=10, capsize=3.5, elinewidth=1.3, zorder=7)
    axA.annotate('%s\noran %.3f' % (ad, Rh / rk), (rk, Rh), textcoords='offset points',
                 xytext=(13, -16), fontsize=8.4, color='#ffe89a', linespacing=1.4)
axA.set_xlabel('Yol 3 öngörüsü:  $r_{kilit}=\\alpha M/P_0=4GM/c^2$  (m)',
               fontsize=10.0, color='#cccccc')
axA.set_ylabel('ölçülen EHT halka yarıçapı (m)', fontsize=10.0, color='#cccccc')
axA.set_title('(A)  Yol 3 — basınç kuyusu yolunun sınavı', fontsize=11.2, color='white', pad=8)
axA.set_xlim(2e9, 2e14)
axA.set_ylim(2e9, 4e14)
lgA = axA.legend(fontsize=8.4, facecolor='#1a1a1a', edgecolor='#333333', loc='upper left')
for t in lgA.get_texts():
    t.set_color('white')
axA.text(0.97, 0.06, 'ağırlıklı oran %.3f ± %.3f\nöngörü %.4f  →  %.1f$\\sigma$'
         % (om, osd, GOLGE_KAT, abs(om - GOLGE_KAT) / osd),
         transform=axA.transAxes, ha='right', va='bottom', fontsize=9.0,
         color='#4ade80', linespacing=1.5)

# --- (B) basinc profili: kilit yaricapi nerede ---
rr = np.linspace(1.0, 6.0, 500)
axB.plot(rr, 1.0 - 2.0 / rr, '-', color='#7dd3fc', lw=2.6,
         label='$P(r)/P_0=1-2r_s/r$')
axB.axhline(0, color='#666666', lw=1.0)
axB.fill_between([1.0, 2.0], -0.35, 1.0, color='#7f1d1d', alpha=0.30, zorder=0)
axB.text(1.5, -0.24, '$P<0$\nyasak bölge', ha='center', fontsize=8.6,
         color='#fca5a5', linespacing=1.4)
for x, ad, rk2, st, ty in [(1.0, 'olay ufku $r_s$', '#c084fc', '-', 0.98),
                           (1.5, 'foton küresi $1{,}5r_s$', '#c084fc', ':', 0.83),
                           (2.0, 'TEORİ KİLİDİ\n$2r_s=4GM/c^2$', '#4ade80', '-', 0.98),
                           (2.598, 'GR gölgesi $2{,}60r_s$', '#c084fc', '--', 0.60)]:
    axB.axvline(x, color=rk2, ls=st, lw=2.4 if x == 2.0 else 1.2,
                alpha=0.95 if x == 2.0 else 0.55)
    axB.text(x + 0.05, ty, ad, ha='left', va='top', fontsize=7.8, color=rk2,
             linespacing=1.35, weight='bold' if x == 2.0 else 'normal')
for ad, M, dM, uas, duas, D, dD, kyn in OLCUM:
    Rh = 0.5 * uas * UAS * D
    x = Rh / r_s(M)
    axB.plot([x], [1.0 - 2.0 / x], 'o', color='#ffcc00', ms=9, zorder=8)
    sgr = 'Sgr' in ad
    axB.annotate('%s ölçümü\n$%.2f\\,r_s$' % (ad, x), (x, 1.0 - 2.0 / x),
                 textcoords='offset points', xytext=(13, -36) if sgr else (13, 15),
                 ha='left', fontsize=7.8, color='#ffe89a', linespacing=1.35,
                 arrowprops=dict(arrowstyle='-', color='#8a7a3a', lw=0.7))
axB.set_xlabel('$r/r_s$', fontsize=10.0, color='#cccccc')
axB.set_ylabel('$P(r)/P_0$  (evrenakı basıncı)', fontsize=10.0, color='#cccccc')
axB.set_title('(B)  Evrenakı kilidi — basınç kuyusu nerede dibe vuruyor?',
              fontsize=11.2, color='white', pad=8)
axB.set_xlim(1.0, 6.0)
axB.set_ylim(-0.35, 1.0)
lgB = axB.legend(fontsize=8.4, facecolor='#1a1a1a', edgecolor='#333333', loc='lower right')
for t in lgB.get_texts():
    t.set_color('white')

# --- (C) karakteristik yaricap merdiveni, 10 dekat ---
Mv = np.logspace(0.6, 11.2, 300)
axC.loglog(Mv, [r_kilit(m) for m in Mv], '-', color='#4ade80', lw=2.6,
           label='Yol 3: $r_{kilit}=4GM/c^2=2r_s$')
axC.loglog(Mv, GOLGE_KAT * np.array([r_kilit(m) for m in Mv]), '--', color='#c084fc',
           lw=1.6, label='GR gölgesi $=3\\sqrt{3}\\,GM/c^2$')
axC.loglog(Mv, [r_s(m) for m in Mv], ':', color='#c084fc', lw=1.4, label='$r_s$')
axC.loglog(Mv, [r_cep(m) for m in Mv], '-', color='#f472b6', lw=2.2,
           label='Yol 2: $r_{cep}\\propto M^{1/3}$')
for ad, M in DINAMIK:
    axC.plot([M], [r_kilit(M)], 'o', color='#555555', ms=4.5, zorder=5)
for ad, M, dM, uas, duas, D, dD, kyn in OLCUM:
    Rh = 0.5 * uas * UAS * D
    axC.plot([M], [Rh], '*', color='#ffcc00', ms=17, zorder=8)
    axC.annotate(ad, (M, Rh), textcoords='offset points', xytext=(-6, 13),
                 fontsize=8.2, color='#ffe89a', ha='right')
axC.annotate('Yol 2 burada\n$10^4$–$10^6$ kat ıskalıyor', (2e6, r_cep(2e6)),
             xytext=(3e4, 8e3), textcoords='data', fontsize=8.2, color='#f9a8d4',
             linespacing=1.4, va='bottom', ha='left',
             arrowprops=dict(arrowstyle='->', color='#f472b6', lw=1.1,
                             connectionstyle='arc3,rad=-0.25'))
axC.set_xlabel('$M$ ($M_\\odot$)', fontsize=10.0, color='#cccccc')
axC.set_ylabel('yarıçap (m)', fontsize=10.0, color='#cccccc')
axC.set_title('(C)  Karakteristik yarıçaplar — 10 dekat kütle aralığında',
              fontsize=11.2, color='white', pad=8)
axC.set_ylim(1e2, 1e16)
lgC = axC.legend(fontsize=8.0, facecolor='#1a1a1a', edgecolor='#333333', loc='upper left')
for t in lgC.get_texts():
    t.set_color('white')
axC.text(0.985, 0.022, 'gri noktalar: yalnız dinamik kütlesi ölçülmüş 8 kara delik  ·  '
                       'yıldızlar: boyutu da ölçülmüş iki cisim',
         transform=axC.transAxes, ha='right', va='bottom', fontsize=7.2,
         color='#777777')

# --- (D) bilanco ---
axD.axis('off')
BLK = [
    ('#4ade80', 'Yol 3 — basınç kuyusu:  KAZANIYOR',
     '$P(r)=P_0-\\alpha M/r=0 \\Rightarrow r_{kilit}=\\alpha M/P_0$\n'
     '$\\alpha=G\\rho_n$ (4.2.4) ve $P_0=\\frac{1}{4}\\rho_n c^2$ (Ek B.3) konunca\n'
     '$\\rho_n$ sadeleşir:  $r_{kilit}=4GM/c^2=2r_s$ — sıfır serbest parametre.\n'
     'Ölçülen halka / öngörü = %.3f ± %.3f, beklenen $3\\sqrt{3}/4$ = %.3f → %.1f$\\sigma$.'
     % (om, osd, GOLGE_KAT, abs(om - GOLGE_KAT) / osd)),
    ('#f472b6', 'Yol 2 — geometrik:  ÇÖKÜYOR',
     '$r_{cep}=(3M/4\\pi\\rho_n)^{1/3}$ kara delikte $10^4$–$10^6$ kat küçük.\n'
     'Nedeni yapısal: $M^{1/3}$ ölçekleniyor, gözlenen boyut ise $M^1$.\n'
     'Kara delikte nükleon paketi kalmamıştır — yol tanım gereği geçersiz.'),
    ('#888888', 'Yol 1 — kinematik:  SESSİZ',
     'Akı korunumu $\\alpha$’yı sabitlediği için standart astronomiyle\n'
     'birebir aynı sayı. Bağımsız el vermez; ama Yol 3 ile çapraz denetlenir.'),
    ('#fbbf24', 'ÖDENMEMİŞ HESAP — yanlışlanabilir öngörü',
     '$3\\sqrt{3}/4$ çarpanı GR’ın güçlü alan jeodeziklerinden gelir; teori onu\n'
     'kendi ışık yayılımından (Ek M-42) türetmek zorundadır — henüz türetmedi.\n'
     'Ayrıca teori ışımanın $2r_s$’de KESKİN kesilmesini öngörür; GR ufka kadar\n'
     'ışıma verir. Bu fark ngEHT çözünürlüğünde ayrıştırılabilir.'),
]
# iki kolon: (Yol 3, Yol 2) solda, (Yol 1, odenmemis hesap) sagda.
# konumlar puan cinsinden hesaplanir; boylece satir sayisi degisse de cakisma olmaz.
H_PT = axD.get_position().height * fig.get_figheight() * 72.0
TIT, BDY, LS, ARA = 10.6, 8.8, 1.5, 15.0
for x, blok in [(0.0, BLK[:2]), (0.515, BLK[2:])]:
    y = 1.0
    for renk, bas, gvd in blok:
        axD.text(x, y, bas, fontsize=TIT, color=renk, weight='bold', va='top')
        y -= TIT * 2.0 / H_PT
        axD.text(x, y, gvd, fontsize=BDY, color='#bbbbbb', va='top', linespacing=LS)
        y -= ((gvd.count('\n') + 1) * BDY * LS + ARA) / H_PT
axD.set_title('(D)  Kara delik bilançosu — üç yolun karşılaştırmalı sonucu',
              fontsize=11.2, color='white', pad=8, loc='left')

fig.text(0.5, 0.958, 'Kara Deliklerde Merkez Kütle — Evrenakı’nın Üç Yolu, Gerçek Ölçümlerle',
         ha='center', fontsize=13.6, color='white')
fig.text(0.5, 0.921,
         'Veri: GRAVITY Collab. 2022 (Sgr A* kütlesi) · EHT Collab. 2019, 2022 (halka çapları) · '
         '8 ek kara delik dinamik kütlesi  ·  teoride serbest parametre yok',
         ha='center', fontsize=9.0, color='#999999')
plt.savefig('karadelik_3yol.png', dpi=185, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print("Grafik 'karadelik_3yol.png' olarak kaydedildi.")
