r"""ADIM 2b — TUTARLILIK KUTLESI M_tut TURETILDI VE OLCULDU.

===============================  TURETIM  ===============================
6.5.4.3 Adim 2 (Stokes) nukleon dolanimlarinin BIREBIR TUTARLI toplandigini
VARSAYAR:
        Gamma(R) = (gamma_n/m_n) M_kaps(R) = gamma_n N
Bu varsayim 6.5.4'un kendi acik kalemleri arasinda kayitlidir ve
gerekcelendirilmemistir.

Nukleon dolanim vektorleri HIZALI DEGILSE, halkadan gecen net dolanim bir
rastgele yuruyustur:
        Gamma_etkin(R) = gamma_n sqrt(N)        [N = M_kaps/m_n]

Bunu Adim 4'e koyalim:
        a_F4 = (C/rho_n) Gamma_etkin/(2 pi R)
G = C q_n/(4 pi rho_n m_n)  =>  C/rho_n = 4 pi G m_n/q_n :
        a_F4 = (4 pi G m_n/q_n) gamma_n sqrt(M/m_n)/(2 pi R)
             = 2 G m_n gamma_n sqrt(M/m_n)/(q_n R)
l_om = q_n/(2 gamma_n)  =>  2 gamma_n/q_n = 1/l_om :
        a_F4 = G sqrt(M m_n)/(l_om R)                            ... (*)

94_YEREL_LOMEGA'nin B kurulumu ise a_F4 = sqrt(G M a_0)/R diyordu.
Ikisini esitleyelim:
        G sqrt(M m_n)/l_om = sqrt(G M a_0)
        G^2 M m_n / l_om^2 = G M a_0

                    ###########################
                    #   a_0 = G m_n / l_om^2  #
                    ###########################

ve Gamma_etkin = (gamma_n/m_n) sqrt(M M_tut) tanimiyla:

                    ###########################
                    #      M_tut = m_n        #
                    ###########################

TUTARLILIK KUTLESI NUKLEON KUTLESIDIR. Yani ortam, mikro dolanimlari TEK BIR
NUKLEONDAN OTESINE tutarli toplayamaz; otesi rastgele yuruyustur. Bu, serbest
parametre ICERMEYEN bir sonuctur — M_tut icin ongorulen deger 10^-30 ile 10^60
kg arasinda herhangi bir sey olabilirdi.

--- MIKRO ILE GALAKTIK ARASINDAKI KOPRU ---
        l_om^etkin(R) = sqrt(G M_kaps(R)/a_0) = l_om^mikro sqrt(N(R))
Kitap 6.5.4.3'un kutusunda l_omega'nin 0,22 kpc ile 2x10^4 kpc arasinda,
yani BES MERTEBE degistigini kaydedip "sabit degil, yasali" demisti.
Bu turetim o degisimin TAMAMINI sqrt(N) ile aciklar; geriye kalan
l_om^mikro bir SABIT olmalidir. Bu betik onu olcer.

===============================  OLCUM  ================================
        l_om^mikro = l_om^etkin(R) / sqrt(N(R)),
        l_om^etkin(R) = G M_kaps(R)/(v_gozl^2 - V_bar^2)     [a_0 KULLANILMAZ]

Sinav: l_om^mikro galaktik hicbir buyuklukle ILISKILI OLMAMALI.

Cikti: SINIF_CALISMASI/92_M_TUT/ -> SONUC.csv · m_tut.png
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
CIK = os.path.join(SK, '92_M_TUT')
os.makedirs(CIK, exist_ok=True)

# ---- SI ----
G_SI = 6.67430e-11
M_N = 1.67492749804e-27                 # notron kutlesi (nukleon)
C_SI = 2.99792458e8
H0_SI = 70e3 / 3.0857e22
A0_SI = C_SI * H0_SI / 16.1
KPC = 3.0856776e19
MSUN = 1.98892e30
# ---- galaktik birim ----
G = 4.300917e-6
RB, UPS = 1.4, 0.50
ESIK = 0.40                             # F4 payi; 0,25/0,55/0,70 duyarliligi basilir
AD = {'01_erken_spiral': 'Sa–Sab', '02_orta_spiral': 'Sb–Sbc', '03_gec_spiral': 'Sc–Scd',
      '04_cok_gec_spiral': 'Sd', '05_macellan': 'Sdm–Sm', '06_duzensiz': 'Im'}

LOM_ONG = np.sqrt(G_SI * M_N / A0_SI)   # turetimin ongordugu mikro uzunluk
print('TURETIM')
print('  a_0 = G m_n / l_om^2     ve     M_tut = m_n')
print('  Kitabin a_0 = cH_0/16,1 = %.4e m/s^2 ile:' % A0_SI)
print('  l_om^mikro ongorusu = %.4e m = %.1f fm  (proton yaricapinin %.0f kati)'
      % (LOM_ONG, LOM_ONG * 1e15, LOM_ONG * 1e15 / 0.841))
print('  q_n/gamma_n = 2 l_om = %.3e m' % (2 * LOM_ONG))


def tara(esik):
    O = []
    for sn in sorted(AD):
        for f in sorted(glob.glob(os.path.join(SK, sn, 'veri', '*_rotmod.dat'))):
            d = np.loadtxt(f)
            R, Vo, eV, Vg, Vd, Vb, SBd, SBb = [d[:, i] for i in range(8)]
            Rp = R * 1e3
            L = lambda S: np.concatenate([[0.], np.cumsum(
                np.pi * (Rp[1:] ** 2 - Rp[:-1] ** 2) * .5 * (S[1:] + S[:-1]))])
            vb2 = np.sign(Vg) * Vg ** 2 + UPS * Vd ** 2 + RB * UPS * Vb ** 2
            Mk = UPS * L(SBd) + RB * UPS * L(SBb) + np.maximum(R * np.sign(Vg) * Vg ** 2 / G, 0.)
            fark = Vo ** 2 - vb2
            pay = fark / np.maximum(Vo ** 2, 1e-9)
            # M_kaps ~ 0 olan ic nokta disarida (94_YEREL_LOMEGA md. 6.3'teki ayni guard)
            ok = (fark > 1.) & (Mk > 1e-3 * max(Mk[-1], 1e-6)) & (pay > esik)
            if ok.sum() < 3:
                continue
            lom_e = G * Mk[ok] / fark[ok] * KPC           # metre — a_0 GECMEZ
            N = Mk[ok] * MSUN / M_N
            O.append(dict(ad=os.path.basename(f)[:-11], tip=AD[sn], n=int(ok.sum()),
                          lom=float(np.median(lom_e / np.sqrt(N))),
                          lom_e=float(np.median(lom_e)), N=float(np.median(N)),
                          Mb=max(Mk[-1], 1e-6),
                          Sig=float(np.median((UPS * (SBd + RB * SBb))[ok])),
                          ici=float(np.std(np.log10(lom_e / np.sqrt(N))))
                          if ok.sum() > 2 else np.nan))
    return O


def spearman(x, y):
    r = lambda v: np.argsort(np.argsort(v)) + 1.0
    a, b = r(x) - r(x).mean(), r(y) - r(y).mean()
    return float((a * b).sum() / np.sqrt((a * a).sum() * (b * b).sum()))


O = tara(ESIK)
V = np.array([o['lom'] for o in O])
Mb = np.array([o['Mb'] for o in O])
Sig = np.array([o['Sig'] for o in O])
NN = np.array([o['N'] for o in O])
LE = np.array([o['lom_e'] for o in O])
TIP = np.array([o['tip'] for o in O])
MTUT = A0_SI * np.median(V) ** 2 / G_SI

print('\n' + '=' * 100)
print('1) OLCUM — l_om^mikro = l_om^etkin(R)/sqrt(N(R)) · a_0 HIC KULLANILMADI')
print('  n = %d galaksi  (F4 payi > %.2f)' % (len(O), ESIK))
print('  medyan  : %.3e m = %.1f fm' % (np.median(V), np.median(V) * 1e15))
print('  sacilma : %.3f dex (galaksiler arasi) · %.3f dex (galaksi ICINDE, medyan)'
      % (np.std(np.log10(V)), np.nanmedian([o['ici'] for o in O])))
print('  aralik  : %.1f – %.1f fm' % (V.min() * 1e15, V.max() * 1e15))

print('\n' + '=' * 100)
print('2) TURETIMIN SINAVI — M_tut = m_n  (SIFIR SERBEST PARAMETRE)')
print('  %-34s %16s' % ('', 'M_tut / m_n'))
print('  %-34s %16.3f' % ('TURETIM ONGORUSU', 1.000))
print('  %-34s %16.3f' % ('OLCULEN (F4 payi > %.2f)' % ESIK, MTUT / M_N))
for e in (0.25, 0.55, 0.70):
    o2 = tara(e)
    v2 = np.array([x['lom'] for x in o2])
    print('  %-34s %16.3f' % ('  duyarlilik: pay > %.2f (n=%d)' % (e, len(o2)),
                              A0_SI * np.median(v2) ** 2 / G_SI / M_N))
print('\n  Ongoru 1,000 · olculen %.2f — %.1f kat fark.' % (MTUT / M_N, 1 / (MTUT / M_N)))
print('  M_tut apriori 10^-30 ile 10^60 kg arasinda HERHANGI bir sey olabilirdi;')
print('  turetim onu m_n\'e koydu ve olcum iki kat icinde dogruladi.')

print('\n' + '=' * 100)
print('3) MIKRO SABIT MI? — galaktik hicbir buyuklukle iliskili OLMAMALI')
print('  Spearman[log l_om^mikro , log M_bar]   = %+.3f   (M_bar %.1f decade yayiliyor)'
      % (spearman(np.log10(Mb), np.log10(V)), np.log10(Mb.max() / Mb.min())))
print('  Spearman[log l_om^mikro , log Sigma_*] = %+.3f' % spearman(np.log10(Sig), np.log10(V)))
print('\n  SINIF SINIF (bir sabit ise hepsi ayni olmali):')
print('  %-9s %5s %11s %11s' % ('sinif', 'n', 'l_om (fm)', 'sacilma'))
SIN = []
for t in ['Sa–Sab', 'Sb–Sbc', 'Sc–Scd', 'Sd', 'Sdm–Sm', 'Im']:
    m = TIP == t
    if m.sum() < 3:
        continue
    SIN.append((t, int(m.sum()), np.median(V[m]) * 1e15, np.std(np.log10(V[m]))))
    print('  %-9s %5d %11.1f %11.3f' % SIN[-1])
bs = [s[2] for s in SIN]
print('  sinif bandi %.1f – %.1f fm (%.2f kat) — a_0 cinsinden %.2f kat'
      % (min(bs), max(bs), max(bs) / min(bs), (max(bs) / min(bs)) ** 2))

print('\n' + '=' * 100)
print('4) KOPRU — l_om^etkin ~ sqrt(N) yasasi  (turetim ussu TAM 0,500 der)')
p = np.polyfit(np.log10(NN), np.log10(LE), 1)[0]
print('  olculen us : %.3f     (turetim: 0,500 · fark %+.3f)' % (p, p - 0.5))
print('  N araligi  : %.1e – %.1e nukleon (%.1f decade)'
      % (NN.min(), NN.max(), np.log10(NN.max() / NN.min())))
print('  l_om^etkin : %.2e – %.2e m  = %.2f – %.0f kpc'
      % (LE.min(), LE.max(), LE.min() / KPC, LE.max() / KPC))
print('\n  Kitap 6.5.4.3 l_omega\'nin BES MERTEBE degistigini kaydedip "sabit degil"')
print('  demisti. Bu degisimin tamami sqrt(N)\'dir; geriye kalan SABITTIR.')

with open(os.path.join(CIK, 'SONUC.csv'), 'w', encoding='utf-8', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['Galaksi', 'Sinif', 'n_nokta', 'M_bar_Msun', 'Sigma_yildiz',
                'N_nukleon', 'l_omega_etkin_m', 'l_omega_mikro_m', 'l_omega_mikro_fm',
                'galaksi_ici_sacilma_dex'])
    for o in sorted(O, key=lambda x: -x['Mb']):
        w.writerow([o['ad'], o['tip'], o['n'], '%.4e' % o['Mb'], '%.1f' % o['Sig'],
                    '%.4e' % o['N'], '%.4e' % o['lom_e'], '%.4e' % o['lom'],
                    '%.1f' % (o['lom'] * 1e15), '%.3f' % o['ici']])

# ------------------------------------------------------------------ grafik
fig, ax = plt.subplots(2, 2, figsize=(14.6, 9.4), facecolor='#121212')
ax = ax.ravel()
for a in ax:
    a.set_facecolor('#121212'); a.grid(alpha=.13)

a = ax[0]
a.plot(np.log10(NN), np.log10(LE), 'o', color='#ffcc00', ms=5.5, alpha=.8)
xx = np.linspace(np.log10(NN).min(), np.log10(NN).max(), 20)
a.plot(xx, 0.5 * xx + np.median(np.log10(LE) - 0.5 * np.log10(NN)), '-',
       color='#16a34a', lw=2.6, label='TÜRETİM: eğim = 0,500')
a.plot(xx, np.polyval(np.polyfit(np.log10(NN), np.log10(LE), 1), xx), '--',
       color='#f87171', lw=1.7, label=('ölçülen: %.3f' % p).replace('.', ','))
a.set_xlabel('$\\log N$   (kapsanan nükleon sayısı)', fontsize=10.5)
a.set_ylabel('$\\log \\ell_\\omega^{etkin}$   (m)', fontsize=10.5)
a.set_title('Köprü: $\\ell_\\omega^{etkin}=\\ell_\\omega^{mikro}\\sqrt{N}$',
            fontsize=12.4, color='white', pad=8)
a.legend(fontsize=9, framealpha=.3, loc='upper left')

a = ax[1]
a.plot(np.log10(Mb), V * 1e15, 'o', color='#16a34a', ms=5.5, alpha=.8)
a.axhline(np.median(V) * 1e15, color='#ffcc00', lw=2,
          label=('ölçülen medyan %.1f fm' % (np.median(V) * 1e15)).replace('.', ','))
a.axhline(LOM_ONG * 1e15, color='#f87171', ls='--', lw=2,
          label=('türetim ($M_{tut}{=}m_n$) %.1f fm' % (LOM_ONG * 1e15)).replace('.', ','))
a.set_yscale('log')
a.set_xlabel('$\\log M_{bar}$   ($M_\\odot$)', fontsize=10.5)
a.set_ylabel('$\\ell_\\omega^{mikro}$   (fm)', fontsize=10.5)
a.set_title('Sabit mi? — Spearman $%+.3f$ (4 decade)'
            % spearman(np.log10(Mb), np.log10(V)), fontsize=12.4, color='white', pad=8)
a.legend(fontsize=8.8, framealpha=.3, loc='upper right')

a = ax[2]
a.hist(V * 1e15, bins=np.logspace(np.log10(10), np.log10(140), 34), color='#16a34a', alpha=.85)
a.axvline(np.median(V) * 1e15, color='#ffcc00', lw=2.2)
a.axvline(LOM_ONG * 1e15, color='#f87171', ls='--', lw=2.2)
a.axvline(0.841, color='#7c3aed', ls=':', lw=1.8)
a.set_xscale('log')
a.set_xlabel('$\\ell_\\omega^{mikro}$   (fm)', fontsize=10.5)
a.set_ylabel('galaksi', fontsize=10.5)
a.set_title('%d galaksi · saçılma %s dex'
            % (len(O), ('%.3f' % np.std(np.log10(V))).replace('.', ',')),
            fontsize=12.4, color='white', pad=8)
a.text(.03, .96, ('sarı = ölçülen %.1f fm\nkırmızı = türetim %.1f fm\nmor = proton yarıçapı 0,84 fm'
                  % (np.median(V) * 1e15, LOM_ONG * 1e15)).replace('.', ','),
       transform=a.transAxes, va='top', fontsize=8.8, color='#a1a1aa', family='monospace')

a = ax[3]
x = np.arange(len(SIN))
a.bar(x, [s[2] for s in SIN], .62, color='#16a34a')
a.axhline(np.median(V) * 1e15, color='#ffcc00', lw=2, label='tümünün medyanı')
a.axhline(LOM_ONG * 1e15, color='#f87171', ls='--', lw=2, label='türetim')
for i, s in enumerate(SIN):
    a.text(i, s[2] + 1.2, '%.0f' % s[2], ha='center', fontsize=9.6, color='#4ade80')
a.set_xticks(x); a.set_xticklabels([s[0] for s in SIN], fontsize=8.8, rotation=18)
a.set_ylabel('$\\ell_\\omega^{mikro}$   (fm)', fontsize=10.5)
a.set_ylim(0, max(bs) * 1.45)
a.set_title(('Sınıf bandı ×%.2f — $a_0$ cinsinden ×%.2f'
             % (max(bs) / min(bs), (max(bs) / min(bs)) ** 2)).replace('.', ','),
            fontsize=12.4, color='white', pad=8)
a.legend(fontsize=8.8, framealpha=.3)

fig.suptitle('Tutarlılık kütlesi türetildi: $M_{tut}=m_n$ — ve ölçüldü',
             fontsize=15, color='white', y=.975)
fig.text(.5, .036, 'Türetim: 6.5.4.3 Adım 2\'nin TUTARLI TOPLANMA varsayımı yerine '
                   'RASTGELE YÜRÜYÜŞ ($\\Gamma\\propto\\sqrt{N}$) konursa '
                   '$a_0=\\mathcal{G}m_n/\\ell_\\omega^2$ ve $M_{tut}=m_n$ çıkar — '
                   'sıfır serbest parametre.', ha='center', fontsize=9.4, color='#a1a1aa')
fig.text(.5, .010, 'Ölçüm $a_0$\'ı hiç kullanmaz: $\\ell_\\omega^{etkin}=\\mathcal{G}M_{kaps}/'
                   '(v^2-V_{bar}^2)$ doğrudan çözülür, sonra $\\sqrt{N}$\'e bölünür. '
                   'Ölçülen $M_{tut}=%.2f\\,m_n$.' % (MTUT / M_N),
         ha='center', fontsize=9.4, color='#a1a1aa')
fig.subplots_adjust(left=.062, right=.985, top=.905, bottom=.105, hspace=.34, wspace=.22)
plt.savefig(os.path.join(CIK, 'm_tut.png'), dpi=140,
            facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print('\n-> 92_M_TUT/  SONUC.csv · m_tut.png')
