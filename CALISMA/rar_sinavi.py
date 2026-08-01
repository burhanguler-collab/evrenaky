r"""RADYAL IVME BAGINTISI (RAR) SINAVI — 2693 nokta, FIT YOK.

Teorinin EN GENIS ORNEKLEMLI fit-siz sinavi. 96_ETG'de yan urun olarak cikti,
burada kendi sinavi olarak kuruluyor.

--- SINANAN SEY: SEKIL, SADECE OLCEK DEGIL ---
Onceki sinavlar (97_BTFR, 96_ETG) tek bir sayi olcuyordu: medyan sapma ve
gereken a_0 carpani. Bu sinav BASKA bir sey soruyor:

    Teorinin ONGORDUGU BICIM dogru mu — yoksa yalniz olcegi mi tutuyor?

    g_ong = g_bar + sqrt(g_bar a_0)

Bu formulun sekli sabittir. Eger sekil dogruysa, artik (log g_ong - log g_obs)
ivmeden BAGIMSIZ olmalidir: a_0 yanlis kalibre ise butun noktalar ayni miktarda
kayar, ama EGILIM olusmaz. Artikta ivmeye bagli bir yapi varsa, sorun a_0'da
degil FORMULUN KENDISINDEDIR.

Dort decadelik ivme araligi ve 2693 nokta, bunu ayirt edecek guctedir. 16
ETG'yle yapilamayan sinav (96_ETG md. 6) burada yapilabilir.

--- OLCULENLER ---
 1) Kusakli artik: 0,25 dex'lik ivme kusaklarinda medyan sapma ve gereken a_0.
    a_0 EVRENSELSE her kusak ayni carpani istemelidir.
 2) Dusuk ivme asimptot egimi: teori TAM 0,500 der (g_obs -> sqrt(g_bar a_0)).
 3) Sacilma butcesi: gozlenen sacilma, bildirilen olcum hatasiyla aciklanabilir
    mi? Yani "tek yasa" iddiasinin gercek payi ne?
 4) Kiyas: ampirik RAR uyum fonksiyonu (Lelli+2017) — bir parametresi FITLENMIS
    olan bu egri, teorinin FITSIZ egrisiyle karsilastirilir. Adil degildir ve
    oyle isaretlenmistir: teorinin ustunlugu varsa dezavantajlidir.

--- BU SINAVDA LCDM YOK ---
_RAR.mrt yalniz (g_bar, g_obs) ciftlerini verir; galaksi kimligi, kutle ve
yaricap YOKTUR. LCDM zinciri kurulamaz. 97_BTFR ve 96_ETG'de kuruldu, orada
bakilmalidir. Buraya sahte bir karsi taraf uydurulmadi.

Cikti: SINIF_CALISMASI/95_RAR/ -> SONUC.csv · rar.png
Kaynak: Lelli F., McGaugh S.S., Schombert J.M., Pawlowski M.S., 2017,
        ApJ 836, 152 — Sekil 2'nin arkasindaki veri.
"""

import os
import sys
import csv
import warnings

import numpy as np
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
plt.style.use('dark_background')

KOK = os.path.dirname(os.path.abspath(__file__))
VERI = os.path.join(KOK, 'veri')
CIK = os.path.join(KOK, 'SINIF_CALISMASI', '95_RAR')
os.makedirs(CIK, exist_ok=True)

# ---- sabitler: btfr_sinavi.py / etg_sinavi.py ile BIREBIR ayni ----
C_SI = 2.99792458e8
H0_SI = 70e3 / 3.0857e22
ACC = 1e6 / 3.0856776e19
A0 = (C_SI * H0_SI) / ACC / 16.1 * ACC        # m/s^2 = 4,224e-11
G_DAGGER = 1.20e-10                            # ampirik olcek — FITLENMIS
PAY_ESIK = 0.25      # F4'un ongoruye katkisi bunun altindaysa carpan OKUNMAZ
                     # (96_ETG md. 3'un kurali; oradan buraya tasindi)


def oku_rar(yol):
    lg, elg, lo, elo = [], [], [], []
    for L in open(yol, encoding='utf-8', errors='replace'):
        p = L.split()
        if len(p) != 4:
            continue
        try:
            v = [float(x) for x in p]
        except ValueError:
            continue
        if -14 < v[0] < -7 and -14 < v[2] < -7:
            lg.append(v[0]); elg.append(v[1]); lo.append(v[2]); elo.append(v[3])
    return map(np.array, (lg, elg, lo, elo))


LGB, ELGB, LGO, ELGO = oku_rar(os.path.join(VERI, '_RAR.mrt'))
GB, GO = 10 ** LGB, 10 ** LGO
print('RAR: %d nokta · log g_bar %.2f … %.2f  (%.1f decade)'
      % (len(GB), LGB.min(), LGB.max(), LGB.max() - LGB.min()))


def ongoru(gbar, k=1.0):
    return gbar + np.sqrt(k * A0 * gbar)


def ampirik(gbar):
    """Lelli+2017 uyum fonksiyonu. g_dagger FITLENMISTIR — teorinin degil."""
    return gbar / (1 - np.exp(-np.sqrt(gbar / G_DAGGER)))


def pay(gbar):
    """F4'un ongoruye katkisi = gereken a_0'in kaldiraci."""
    return np.sqrt(A0 * gbar) / ongoru(gbar)


def a0_carpani(gbar, gobs):
    fk = lambda k: np.median(np.log10(ongoru(gbar, k) / gobs))
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


ART = np.log10(ongoru(GB) / GO)          # teorinin artigi
ART_A = np.log10(ampirik(GB) / GO)       # ampirik uyumun artigi (1 parametre fitli)
K_HEP = a0_carpani(GB, GO)

print('\n' + '=' * 100)
print('BUTUN ORNEKLEM')
print('  %-42s %11s %9s %12s' % ('kurulum', 'medyan dex', 'sacilma', 'gereken a_0'))
print('  %-42s %+11.3f %9.3f %11.2fx'
      % ('EVRENAKI  g_bar+sqrt(g_bar a_0)   FIT YOK', np.median(ART), np.std(ART), K_HEP))
print('  %-42s %+11.3f %9.3f %12s'
      % ('ampirik uyum (g_dagger FITLENMIS)', np.median(ART_A), np.std(ART_A), '—'))

# ---------------------------------------------------- 1) kusakli cozumleme
print('\n' + '=' * 100)
print('KUSAKLI COZUMLEME — a_0 EVRENSEL MI?  (her kusak ayni carpani istemeli)')
print('  %-16s %6s %9s %10s %11s %11s'
      % ('log g_bar kusagi', 'n', 'F4 payi', 'artik dex', 'gereken a_0', 'durum'))
KEN = np.arange(-12.5, -8.0 + 1e-9, 0.25)
KUS, ATILAN = [], []
for lo_, hi_ in zip(KEN[:-1], KEN[1:]):
    m = (LGB >= lo_) & (LGB < hi_)
    if m.sum() < 15:
        continue
    p = np.median(pay(GB[m]))
    k = a0_carpani(GB[m], GO[m])
    ok = p >= PAY_ESIK
    KUS.append(dict(lo=lo_, hi=hi_, orta=(lo_ + hi_) / 2, n=int(m.sum()), pay=p,
                    art=np.median(ART[m]), sac=np.std(ART[m]), k=k, ok=ok,
                    aart=np.median(ART_A[m])))
    if not ok:
        ATILAN.append((lo_, hi_, int(m.sum()), p, k))
    print('  %6.2f … %-6.2f %6d %9.2f %+10.3f %10.2fx %11s'
          % (lo_, hi_, m.sum(), p, np.median(ART[m]), k,
             'okunur' if ok else 'KOTU KOSULLU'))

KG = [b for b in KUS if b['ok']]
kk = np.array([b['k'] for b in KG])
print('\n  Esik: F4 payi >= %.2f. Okunabilir kusak %d/%d; %d kusak elendi'
      % (PAY_ESIK, len(KG), len(KUS), len(ATILAN)))
print('  (elenenler yuksek ivme tarafindadir: orada ongorunun neredeyse tamami Newton')
print('   terimidir, a_0\'in kaldiraci yoktur. 96_ETG md. 3\'te ayni sey olculmustu.)')
print('\n  OKUNABILIR KUSAKLARDA GEREKEN a_0:')
print('    medyan x%.2f · aralik x%.2f - x%.2f · sacilma %.3f dex'
      % (np.median(kk), kk.min(), kk.max(), np.std(np.log10(kk))))
print('    -> %s'
      % ('TEK BIR a_0 dort decade boyunca yetiyor'
         if np.std(np.log10(kk)) < 0.10 else
         'carpan ivmeyle DEGISIYOR — tek a_0 yetmiyor'))

# artigin ivmeye bagimliligi: egim sifir mi?
xo = np.array([b['orta'] for b in KG])
ao = np.array([b['art'] for b in KG])
eg_art = np.polyfit(xo, ao, 1)[0]
eg_amp = np.polyfit(xo, [b['aart'] for b in KG], 1)[0]
print('\n  ARTIGIN IVMEYE BAGIMLILIGI  (sekil sinavi — 0 olmali)')
print('    teori  : d(artik)/d(log g_bar) = %+.4f dex/dex' % eg_art)
print('    ampirik: %+.4f dex/dex  (bir parametresi fitli)' % eg_amp)

# ------------------------------------------- 2) dusuk ivme asimptot egimi
print('\n' + '=' * 100)
print('DUSUK IVME ASIMPTOTU — teori TAM 0,500 der')
print('  %-24s %6s %10s %10s' % ('esik', 'n', 'egim', 'fark'))
ASI = []
for esik in (-10.5, -11.0, -11.5):
    m = LGB < esik
    if m.sum() < 30:
        continue
    e = np.polyfit(LGB[m], LGO[m], 1)[0]
    ASI.append((esik, int(m.sum()), e))
    print('  log g_bar < %-13.1f %6d %10.3f %+10.3f' % (esik, m.sum(), e, e - 0.5))
print('  %-24s %6s %10s' % ('TEORI', '—', '0,500'))
_e = [a[2] for a in ASI]
print('\n  DIKKAT: bu sayi ESIK SECIMINE cok duyarlidir (%.3f - %.3f).' % (min(_e), max(_e)))
print('  Ikili bir hukum VERILEMEZ. Uc ayri sebep:')
print('   (a) kesilmis ornekte dogrusal regresyon yanlidir;')
print('   (b) en dusuk esik (-11,5) yalniz %d nokta birakiyor ve ornegin KENARINDA;'
      % ASI[-1][1])
print('   (c) noktalar bagimsiz degil — ayni galaksinin komsu yaricaplari.')
print('  Soylenebilecek olan: egim 0,5 civarindadir ve 1,0\'den (Newton) acikca uzaktir;')
print('  0,500\'un kendisi bu veriyle DOGRULANMIS SAYILAMAZ.')

# --------------------------------------------------- 3) sacilma butcesi
print('\n' + '=' * 100)
print('SACILMA BUTCESI — "tek yasa" iddiasinin gercek payi')
# artik = log g_ong - log g_obs. Hata butcesi: g_obs'un hatasi + g_bar'in
# hatasinin ongoruye tasinmasi (zincir kurali).
dgdb = (1 + 0.5 * np.sqrt(A0 / GB)) * GB / ongoru(GB)     # dlog g_ong / dlog g_bar
BEK = np.sqrt(ELGO ** 2 + (dgdb * ELGB) ** 2)
print('  bildirilen hata: e(log g_obs) medyan %.3f · e(log g_bar) medyan %.3f dex'
      % (np.median(ELGO), np.median(ELGB)))
print('  beklenen sacilma (hata butcesi)     : %.3f dex' % np.median(BEK))
print('  gozlenen sacilma (teori artigi)     : %.3f dex' % np.std(ART))
ic_ = np.std(ART) ** 2 - np.median(BEK) ** 2
print('  ic sacilma (kok fark)               : %s dex'
      % ('%.3f' % np.sqrt(ic_) if ic_ > 0 else '0 (hata butcesi gozleneni ASIYOR)'))
print('  ampirik uyumun artigi               : %.3f dex' % np.std(ART_A))
print('  -> Gozlenen sacilmanin %.0f%%\'i bildirilen olcum hatasiyla aciklaniyor.'
      % (100 * min(1.0, np.median(BEK) ** 2 / np.std(ART) ** 2)))

# ------------------------------------------------------------ SONUC.csv
with open(os.path.join(CIK, 'SONUC.csv'), 'w', encoding='utf-8', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['kusak_alt_log_gbar', 'kusak_ust', 'n', 'F4_payi',
                'TEORI_artik_medyan_dex', 'TEORI_sacilma_dex',
                'TEORI_gereken_a0_carpani', 'carpan_okunabilir',
                'AMPIRIK_artik_medyan_dex'])
    for b in KUS:
        w.writerow(['%.2f' % b['lo'], '%.2f' % b['hi'], b['n'], '%.3f' % b['pay'],
                    '%+.3f' % b['art'], '%.3f' % b['sac'], '%.2f' % b['k'],
                    'evet' if b['ok'] else 'HAYIR', '%+.3f' % b['aart']])

# ---------------------------------------------------------------- grafik
fig = plt.figure(figsize=(16.4, 9.2), facecolor='#121212')
gs = fig.add_gridspec(2, 2, height_ratios=[1.45, 1], width_ratios=[1.5, 1],
                      hspace=.30, wspace=.22)
a1 = fig.add_subplot(gs[0, 0]); a2 = fig.add_subplot(gs[0, 1])
a3 = fig.add_subplot(gs[1, 0]); a4 = fig.add_subplot(gs[1, 1])
for a in (a1, a2, a3, a4):
    a.set_facecolor('#121212')
    a.grid(alpha=.13)

xx = np.linspace(-12.6, -8.3, 300)
gx = 10 ** xx
a1.plot(LGB, LGO, '.', color='#52525b', ms=1.8, alpha=.42, zorder=1,
        label='%d nokta (Lelli+2017)' % len(GB))
a1.plot(xx, xx, ':', color='#71717a', lw=1.3, zorder=2, label='Newton  $g_{obs}=g_{bar}$')
a1.plot(xx, np.log10(ampirik(gx)), '--', color='#f87171', lw=1.7, zorder=4,
        label='ampirik uyum — $g_\\dagger$ FİTLENMİŞ')
a1.plot(xx, np.log10(ongoru(gx)), '-', color='#16a34a', lw=2.7, zorder=6,
        label='EVRENAKI  $g_{bar}+\\sqrt{g_{bar}a_0}$ — FİT YOK')
a1.plot(xx, np.log10(ongoru(gx, K_HEP)), '-.', color='#4ade80', lw=1.7, zorder=5,
        label='  └ $a_0\\times%.2f$' % K_HEP)
kx = np.array([b['orta'] for b in KUS])
a1.plot(kx, [np.median(LGO[(LGB >= b['lo']) & (LGB < b['hi'])]) for b in KUS], 'o',
        color='#ffcc00', ms=6, zorder=7, label='kuşak medyanı (0,25 dex)')
a1.set_xlim(-12.6, -8.3); a1.set_ylim(-12.0, -8.3)
a1.set_xlabel('$\\log g_{bar}$   (m/s²)', fontsize=10.5)
a1.set_ylabel('$\\log g_{obs}$   (m/s²)', fontsize=10.5)
a1.set_title('Radyal İvme Bağıntısı — dört decade, 2693 nokta', fontsize=12.5,
             color='white', pad=8)
a1.legend(fontsize=8.4, framealpha=.3, loc='upper left')

# --- artik: SEKIL sinavi ---
a3.axhline(0, color='#71717a', lw=1.2, zorder=2)
a3.plot(LGB, ART, '.', color='#3f3f46', ms=1.5, alpha=.35, zorder=1)
a3.plot(kx, [b['art'] for b in KUS], 'o-', color='#16a34a', ms=6, lw=1.9, zorder=6,
        label='teori (fit yok)')
a3.plot(kx, [b['aart'] for b in KUS], 's--', color='#f87171', ms=4.6, lw=1.4, zorder=5,
        label='ampirik uyum (fitli)')
a3.axhline(np.median(ART), color='#4ade80', lw=1.2, ls=':', zorder=3,
           label=('medyan %+.3f dex' % np.median(ART)).replace('.', ','))
a3.set_xlim(-12.6, -8.3)
a3.set_xlabel('$\\log g_{bar}$   (m/s²)', fontsize=10.5)
a3.set_ylabel('artık $\\log(g_{öng}/g_{gözl})$', fontsize=10.5)
a3.set_title('Şekil sınavı: artık ivmeyle değişiyor mu?', fontsize=12.5, color='white', pad=8)
a3.legend(fontsize=8.6, framealpha=.3, loc='lower left')
a3.text(.985, .95, ('eğim = %+.4f dex/dex\n(sıfır = biçim doğru)'
                    % eg_art).replace('.', ','), transform=a3.transAxes, ha='right',
        va='top', fontsize=9.4, color='#4ade80', family='monospace')

# --- kusak basina gereken a_0 ---
ko = [b for b in KUS if b['ok']]
kh = [b for b in KUS if not b['ok']]
a2.plot([b['orta'] for b in ko], [b['k'] for b in ko], 'o-', color='#16a34a',
        ms=6.5, lw=2.0, zorder=6, label='F4 payı ≥ %.2f — okunur' % PAY_ESIK)
if kh:
    a2.plot([b['orta'] for b in kh], [b['k'] for b in kh], 'x', color='#71717a',
            ms=7, mew=1.6, zorder=4,
            label='F4 payı < %.2f — kötü koşullu' % PAY_ESIK)
a2.axhspan(kk.min(), kk.max(), color='#16a34a', alpha=.13, zorder=1)
a2.axhline(np.median(kk), color='#4ade80', lw=1.5, ls='--', zorder=3,
           label=('okunabilir kuşakların medyanı ×%.2f' % np.median(kk)).replace('.', ','))
a2.axhline(1.0, color='#f87171', lw=1.2, ls=':', zorder=2, label='çarpan gerekmezdi')
a2.set_yscale('log')
a2.set_xlim(-12.6, -8.3)
a2.set_xlabel('$\\log g_{bar}$   (m/s²)', fontsize=10.5)
a2.set_ylabel('kuşağın istediği $a_0$ çarpanı', fontsize=10.5)
a2.set_title('$a_0$ evrensel mi? — 2693 noktayla', fontsize=12.5, color='white', pad=8)
a2.legend(fontsize=8.2, framealpha=.3, loc='lower left')
a2.text(.985, .965, ('okunabilir bant ×%.2f – ×%.2f\nsaçılma %.3f dex'
                    % (kk.min(), kk.max(), np.std(np.log10(kk)))).replace('.', ','),
        transform=a2.transAxes, ha='right', va='top', fontsize=9.4,
        color='#4ade80', family='monospace')

# --- sacilma butcesi ---
et = ['gözlenen\nsaçılma\n(teori)', 'bildirilen\nölçüm hatası', 'iç saçılma\n(kök fark)',
      'ampirik\nuyumun artığı']
vv = [np.std(ART), np.median(BEK), np.sqrt(ic_) if ic_ > 0 else 0.0, np.std(ART_A)]
cl = ['#16a34a', '#fbbf24', '#a1a1aa', '#f87171']
a4.bar(range(4), vv, .62, color=cl, zorder=4)
for i, v in enumerate(vv):
    a4.text(i, v + .004, ('%.3f' % v).replace('.', ','), ha='center', fontsize=10,
            color=cl[i], fontweight='bold')
a4.set_xticks(range(4)); a4.set_xticklabels(et, fontsize=8.6)
a4.set_ylabel('dex', fontsize=10.5)
a4.set_ylim(0, max(vv) * 1.28)
a4.set_title('Saçılmanın ne kadarı ölçüm hatası?', fontsize=12.5, color='white', pad=8)

fig.suptitle('Radyal İvme Bağıntısı Sınavı — teorinin en geniş örneklemli fit-siz sınavı',
             fontsize=14.5, color='white', y=.975)
vg = lambda x: ('%.2f' % x).replace('.', ',')
fig.text(.5, .038, 'Bu sınav ölçeği değil BİÇİMİ sınar: $a_0$ yanlış kalibreyse bütün noktalar '
                   'aynı miktarda kayar ama artıkta EĞİLİM oluşmaz. Ölçülen eğim %s dex/dex.'
                   % ('%+.4f' % eg_art).replace('.', ','),
         ha='center', fontsize=9.4, color='#a1a1aa')
fig.text(.5, .012, 'Yüksek ivme kuşakları elendi (F4 payı < %s): orada öngörünün neredeyse tamamı '
                   'Newton terimidir, $a_0$\'ın kaldıracı yoktur. Bu sınavda ΛCDM YOKTUR — '
                   'veri yalnız ($g_{bar}$, $g_{obs}$) çiftleridir, zincir kurulamaz.'
                   % vg(PAY_ESIK), ha='center', fontsize=9.4, color='#a1a1aa')
fig.subplots_adjust(left=.058, right=.986, top=.905, bottom=.105)
plt.savefig(os.path.join(CIK, 'rar.png'), dpi=140,
            facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print('\n-> 95_RAR/  SONUC.csv · rar.png')
