"""MERKEZ KUTLE UC YOLLA — gercek olculmus degerlerle karsilastirma.

Teoride merkez kutle temel bir buyukluk degildir. 4.2.4'un baglasimi cekim yukunu
nukleon HACMINE baglar (gamma_N = N*V_n) ve kutle ancak rho_n evrensel oldugu icin
ayni sonucu verir:
        M = rho_n * V_deplase ,      rho_n = 2.702e17 kg/m^3  (Ek B.3, [G] rozetli)

Buradan uc olcum yolu dogar:
  YOL 1  KINEMATIK   : M = v^2 r / G  — akı korunumu geregi standart astronomiyle
                       BIREBIR AYNI sayiyi verir; bagimsiz bir el vermez.
  YOL 2  GEOMETRIK   : r_cep = (3M / 4*pi*rho_n)^(1/3) — teorinin TEK ozgun eli.
                       Dogrudan olculebilir ve dogrudan curutulebilir.
  YOL 3  BASINC KUYUSU: P(r) = P0 - alpha*M/r  ->  M = dP*r/alpha, alpha = G*rho_n.
                       Normalizasyon Ek M-42'nin isik bukulmesi kalibrasyonundan.

Bu betik YOL 2'yi gercek olculmus yaricaplarla sinar. Iki sinif kullanilir:
  (a) NOTRON YILDIZLARI — NICER/X-isini ve GW gozlemleri hem M hem R olcer.
      Bu, teorinin sifir serbest parametreli ongorusunun dogrudan sinavidir.
  (b) KARA DELIKLER — EHT golge capi bir boyut olcumu verir.

Literatur degerleri (yaklasik, yayinlanmis merkezi degerler ve belirsizlikler):
  PSR J0030+0451  M=1.44 (+0.15/-0.14) Msun   R=13.02 (+1.24/-1.06) km  [Miller+2019]
  PSR J0740+6620  M=2.072 (+0.067/-0.066)     R=12.39 (+1.30/-0.98) km  [Riley+2021]
  PSR J0437-4715  M=1.418 (+/-0.037)          R=11.36 (+0.95/-0.63) km  [Choudhury+2024]
  4U 1702-429     M=1.9 (+/-0.3)              R=12.4 (+/-0.4) km        [Nattila+2017]
  GW170817 (1.4)  M=1.4 (varsayilan)          R=11.9 (+/-1.4) km        [Abbott+2018]
  Sgr A*          M=4.297e6 Msun [GRAVITY2022]  golge 51.8 (+/-2.3) uas, D=8.277 kpc [EHT2022]
  M87*            M=6.5e9 Msun   [EHT2019]      golge 42 (+/-3) uas,    D=16.8 Mpc  [EHT2019]

UYARI: kara delik "golge" yaricapi bir madde yuzeyi degildir; isinim bolgesinin
gorunur capidir. Teori onu cebin kendisiyle esitlemek zorunda DEGILDIR — ama o
zaman golgenin kaynagini cep disinda (ortamin basinc/optik yapisinda) aciklamak
zorundadir. Grafik bu farki nicel olarak gosterir.
"""

import sys

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
plt.style.use('dark_background')

G_SI = 6.674e-11
C = 2.99792458e8
MSUN = 1.989e30
RHO_N = 2.702e17          # kg/m^3 — Ek B.3, nukleon oz yogunlugu
ALPHA = G_SI * RHO_N
P0 = 6.07e33
PC = 3.0857e16
UAS = np.pi / (180 * 3600 * 1e6)   # mikro yaysaniye -> radyan


def r_cep(M_msun):
    """Teorinin geometrik yolu: deplase hacmin kure yaricapi."""
    V = M_msun * MSUN / RHO_N
    return (3.0 * V / (4.0 * np.pi)) ** (1.0 / 3.0)


def r_s(M_msun):
    return 2.0 * G_SI * M_msun * MSUN / C ** 2


# --- (a) notron yildizlari: gercek M ve R olcumleri ---
NS = [
    ('PSR J0030+0451', 1.44, (0.15, 0.14), 13.02, (1.24, 1.06), 'Miller+2019'),
    ('PSR J0740+6620', 2.072, (0.067, 0.066), 12.39, (1.30, 0.98), 'Riley+2021'),
    ('PSR J0437-4715', 1.418, (0.037, 0.037), 11.36, (0.95, 0.63), 'Choudhury+2024'),
    ('4U 1702-429', 1.90, (0.30, 0.30), 12.40, (0.40, 0.40), 'Nattila+2017'),
    ('GW170817 ($1{,}4M_\\odot$)', 1.40, (0.10, 0.10), 11.90, (1.40, 1.40), 'Abbott+2018'),
]
# --- (b) kara delikler: M ve EHT golge capi ---
BH = [
    ('Sgr A*', 4.297e6, 51.8, 2.3, 8.277e3 * PC, 'GRAVITY2022 / EHT2022'),
    ('M87*', 6.5e9, 42.0, 3.0, 16.8e6 * PC, 'EHT2019'),
]

print("MERKEZ KUTLE — UC YOL, GERCEK OLCUMLERLE")
print("=" * 92)
print("rho_n = %.3e kg/m^3   alpha = G*rho_n = %.4e s^-2" % (RHO_N, ALPHA))
print("-" * 92)
print("YOL 2 SINAVI — NOTRON YILDIZLARI (sifir serbest parametre)")
print("%-26s %8s %10s %10s %8s" % ('cisim', 'M/Msun', 'R olc(km)', 'R teori(km)', 'olc/teori'))
ns_ok = 0
for ad, M, dM, R, dR, kyn in NS:
    rt = r_cep(M) / 1e3
    ora = R / rt
    iyi = abs(R - rt) <= max(dR)
    ns_ok += int(iyi)
    print("%-26s %8.3f %10.2f %10.2f %8.3f  %s" % (ad, M, R, rt, ora, '<- hata icinde' if iyi else ''))
print("  -> %d/%d notron yildizi olcum hatasi icinde" % (ns_ok, len(NS)))
Mns = np.array([n[1] for n in NS]); Rns = np.array([n[3] for n in NS])
EGIM = float(np.polyfit(np.log10(Mns), np.log10(Rns), 1)[0])
print("  olculen M-R egimi = %.3f  (teori 0.333)" % EGIM)
print("  medyan olculen/teori = %.3f ; sacilma = %.1f%%"
      % (np.median(Rns / np.array([r_cep(m) / 1e3 for m in Mns])),
         100 * np.std(Rns / np.array([r_cep(m) / 1e3 for m in Mns]))))
print("-" * 92)
print("YOL 2 SINAVI — KARA DELIKLER (EHT golgesi)")
print("%-10s %11s %12s %13s %13s %10s" % ('cisim', 'M/Msun', 'golge R(m)', 'r_s(m)', 'teori cep(m)', 'golge/cep'))
for ad, M, uas, duas, D, kyn in BH:
    Rg = 0.5 * (uas * UAS) * D
    print("%-10s %11.3e %12.3e %13.3e %13.3e %10.2e"
          % (ad, M, Rg, r_s(M), r_cep(M), Rg / r_cep(M)))
print("-" * 92)
print("YOL 3 — BASINC KUYUSU DERINLIGI dP/P0 = alpha*M/(r*P0)")
for ad, M, r, nt in [('Sgr A*, S2 perisi', 4.297e6, 120 * 1.496e11, '120 AU'),
                     ('Sgr A*, 1000 AU', 4.297e6, 1000 * 1.496e11, ''),
                     ('M87*, 10 r_s', 6.5e9, 10 * r_s(6.5e9), ''),
                     ('Notron y. yuzeyi 1.4', 1.4, 12e3, 'R=12 km')]:
    print("  %-24s r=%.3e m   dP/P0 = %.3e" % (ad + (' (' + nt + ')' if nt else ''), r, ALPHA * M * MSUN / (r * P0)))
print("=" * 92)

# --- GRAFIK ---
fig = plt.figure(figsize=(16.0, 8.8), facecolor='#121212')
gs = GridSpec(2, 3, width_ratios=[1.35, 1, 1], height_ratios=[1, 1],
              hspace=0.36, wspace=0.30, left=0.062, right=0.985, top=0.885, bottom=0.085)
axA = fig.add_subplot(gs[:, 0])
axB = fig.add_subplot(gs[0, 1])
axC = fig.add_subplot(gs[0, 2])
axD = fig.add_subplot(gs[1, 1:])
for a in (axA, axB, axC, axD):
    a.set_facecolor('#121212')
    for sp in ('top', 'right'):
        a.spines[sp].set_visible(False)
    for sp in ('bottom', 'left'):
        a.spines[sp].set_color('#444444')
    a.tick_params(colors='#aaaaaa', labelsize=8.4)
    a.grid(True, alpha=0.14, color='white')

# (A) Yol 2: olculen boyut vs teori — NS ve BH birlikte
xx = np.logspace(3.5, 8.5, 40)
axA.loglog(xx, xx, '--', color='#ffffff', lw=1.7, alpha=0.8, zorder=3,
           label='Yol 2 öngörüsü (1:1, sıfır parametre)')
for ad, M, dM, R, dR, kyn in NS:
    axA.errorbar(r_cep(M), R * 1e3, yerr=[[dR[1] * 1e3], [dR[0] * 1e3]], fmt='o',
                 color='#4ade80', ms=8, capsize=3, elinewidth=1.2, zorder=6)
    pass
for ad, M, uas, duas, D, kyn in BH:
    Rg = 0.5 * (uas * UAS) * D
    dRg = 0.5 * (duas * UAS) * D
    axA.errorbar(r_cep(M), Rg, yerr=dRg, fmt='s', color='#f472b6', ms=9,
                 capsize=3, elinewidth=1.2, zorder=6)
    axA.annotate(ad, (r_cep(M), Rg), textcoords='offset points', xytext=(9, -3),
                 fontsize=7.6, color='#f9a8d4')
axA.scatter([], [], marker='o', s=70, color='#4ade80', label='nötron yıldızı (NICER / GW)')
axA.scatter([], [], marker='s', s=80, color='#f472b6', label='kara delik (EHT gölgesi)')
axA.set_xlabel('Yol 2 öngörüsü:  $r_{cep}=(3M/4\\pi\\rho_n)^{1/3}$  (m)', fontsize=10.2, color='#cccccc')
axA.set_ylabel('ölçülen boyut (m)', fontsize=10.2, color='#cccccc')
axA.set_title('Yol 2 — geometrik yolun sınavı', fontsize=11.4, color='white', pad=9)
axA.set_xlim(3e3, 3e8)
axA.set_ylim(3e3, 3e14)
lg = axA.legend(fontsize=8.4, facecolor='#1a1a1a', edgecolor='#333333', loc='upper left')
for t in lg.get_texts():
    t.set_color('white')
ORAN = float(np.median(Rns / np.array([r_cep(m) / 1e3 for m in Mns])))
axA.annotate('5 nötron yıldızı (NICER + GW170817)\nmertebe doğru, ama %%%.0f sistematik ALTINDA\n'
             've yalnız 1/5\'i ölçüm hatası içinde'
             % (100 * (1 / ORAN - 1)),
             (1.6e4, 1.30e4), textcoords='offset points', xytext=(58, 74),
             fontsize=8.4, color='#4ade80', linespacing=1.5, va='bottom', ha='left',
             arrowprops=dict(arrowstyle='->', color='#4ade80', lw=1.1,
                             connectionstyle='arc3,rad=-0.18'))
axA.text(0.97, 0.90, 'kara delikler\n$10^4$–$10^6$ kat yukarıda', transform=axA.transAxes,
         ha='right', va='top', fontsize=8.6, color='#f472b6', linespacing=1.4)

# (B) M-R diyagrami: nötron yıldızı yakınlaştırması
Ms = np.linspace(0.9, 2.4, 60)
axB.plot(Ms, [r_cep(m) / 1e3 for m in Ms], '-', color='#4ade80', lw=2.4,
         label='teori $R\\propto M^{1/3}$')
for ad, M, dM, R, dR, kyn in NS:
    axB.errorbar(M, R, xerr=[[dM[1]], [dM[0]]], yerr=[[dR[1]], [dR[0]]], fmt='o',
                 color='#ffcc00', ms=6, capsize=2.5, elinewidth=1.0, zorder=6)
axB.set_xlabel('$M$ ($M_\\odot$)', fontsize=9.4, color='#bbbbbb')
axB.set_ylabel('$R$ (km)', fontsize=9.4, color='#bbbbbb')
axB.set_title('Nötron yıldızı $M$–$R$ diyagramı', fontsize=10.4, color='white', pad=6)
axB.set_ylim(9, 17)
lg2 = axB.legend(fontsize=8.0, facecolor='#1a1a1a', edgecolor='#333333', loc='lower right')
for t in lg2.get_texts():
    t.set_color('white')

# (C) r_cep ile r_s'nin kesisimi
Mv = np.logspace(-0.5, 10.5, 200)
axC.loglog(Mv, [r_cep(m) for m in Mv], '-', color='#4ade80', lw=2.2, label='$r_{cep}\\propto M^{1/3}$')
axC.loglog(Mv, [r_s(m) for m in Mv], '-.', color='#c084fc', lw=2.0, label='$r_s\\propto M$')
kes = (3 / (4 * np.pi * RHO_N) * (C ** 2 / (2 * G_SI)) ** 3) ** 0.5 / MSUN
axC.axvline(kes, color='#ffcc00', ls=':', lw=1.4)
axC.text(kes * 1.5, 3e2, 'kesişim\n$\\approx%.0f\\,M_\\odot$' % kes, fontsize=7.6, color='#ffcc00',
         linespacing=1.3)
for ad, M in [('NY', 1.4), ('Sgr A*', 4.297e6), ('M87*', 6.5e9)]:
    axC.plot([M], [r_cep(M)], 'o', color='#ffcc00', ms=5, zorder=6)
    axC.annotate(ad, (M, r_cep(M)), textcoords='offset points', xytext=(5, -9),
                 fontsize=7.0, color='#dddddd')
axC.set_xlabel('$M$ ($M_\\odot$)', fontsize=9.4, color='#bbbbbb')
axC.set_ylabel('yarıçap (m)', fontsize=9.4, color='#bbbbbb')
axC.set_title('$r_{cep}$ ile $r_s$ nerede kesişir?', fontsize=10.4, color='white', pad=6)
lg3 = axC.legend(fontsize=7.8, facecolor='#1a1a1a', edgecolor='#333333', loc='upper left')
for t in lg3.get_texts():
    t.set_color('white')

# (D) uc yolun ozeti
axD.axis('off')
satir = [
    ('Yol 1 — Kinematik', '$M=v^2r/G$',
     'Akı korunumu gereği standart astronomiyle birebir AYNI sayıyı verir.\n'
     'Bağımsız bir el vermez; ölçülen şey yeniden yorumlanır (deplase hacim).', '#888888'),
    ('Yol 2 — Geometrik', '$r_{cep}=(3M/4\\pi\\rho_n)^{1/3}$',
     'Teorinin tek özgün eli, sıfır serbest parametre. Nötron yıldızlarında MERTEBE\n'
     'doğru (%%%.0f fazla tahmin, saçılma yalnız %%%.1f) ama EĞİM sapıyor: teori $M^{1/3}$,\n'
     'ölçüm $M^{%.2f}$ → 1/5 hata içinde. Kara delik gölgesi $10^4$–$10^6$ kat büyük: AÇIK HESAP.'
     % (100 * (1 / ORAN - 1),
        100 * float(np.std(Rns / np.array([r_cep(m) / 1e3 for m in Mns]))), EGIM), '#4ade80'),
    ('Yol 3 — Basınç kuyusu', '$M=\\Delta P\\,r/\\alpha$',
     'Kuyu derinliği kızıla kayma / ışık bükülmesiyle ölçülür; normalizasyon\n'
     'Ek M-42\'de kalibre. Yol 1 ile çapraz denetim sağlar; bağımsız sayı vermez.', '#7dd3fc'),
]
for y, (bas, form, acik, renk) in zip([0.97, 0.63, 0.20], satir):
    axD.text(0.0, y, bas, fontsize=10.6, color=renk, weight='bold', va='top')
    axD.text(0.235, y, form, fontsize=10.6, color='#dddddd', va='top')
    axD.text(0.0, y - 0.105, acik, fontsize=8.6, color='#bbbbbb', va='top', linespacing=1.5)
axD.set_title('Üç yolun statüsü', fontsize=10.4, color='white', pad=6, loc='left')

fig.text(0.5, 0.952, 'Teoride merkez kütle türetilmiş bir büyüklüktür:  '
                     '$M=\\rho_n V_{deplase}$  —  üç ölçüm yolu ve gerçek verilerle sınavı',
         ha='center', fontsize=10.4, color='#aaaaaa')
plt.savefig('merkez_kutle_3yol.png', dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print("Grafik 'merkez_kutle_3yol.png' olarak kaydedildi.")
