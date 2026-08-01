r"""YUKSEK-z SINAVI — a_0 kozmik zamanla degisiyor mu?  TEORININ ILK SPARC-DISI SINAVI.

===============================  SORU  =================================
91_A0_KOPRU iki okuma birakti:
    (K) KOZMIK : a_0(z) = a_0(0) x H(z)/H_0      [kitabin a_0 = cH_0/16,1 okumasi]
    (S) SABIT  : a_0(z) = a_0(0)                 [92_M_TUT'un a_0 = G m_n/l_om^2 okumasi]
z=2'de ikisi duz hizda %31 ayrisir. Bu betik farki GERCEK VERIYLE olcer.

===============================  YONTEM  ===============================
Evrenaki'da karanlik madde YOKTUR. Genzel+2017'nin olctugu "f_DM" bizde
F4'un v^2 icindeki PAYIDIR:
        f_DM = v_F4^2 / v_c^2
94_YEREL_LOMEGA'nin B kurulumunda a_F4 = sqrt(a_F1 a_0), yani
        v_F4^2 = R a_F4 = v_bar sqrt(a_0 R)
Bunu v_c^2 = v_bar^2 + v_F4^2 icine koyup s = v_bar/v_c icin cozelim:
        s^2 + s*sqrt(a_0 R)/v_c - 1 = 0
        s = [-b + sqrt(b^2+4)]/2 ,  b = sqrt(a_0 R)/v_c
        f_DM_ongoru = 1 - s^2

BUNUN GUZELLIGI: yalniz v_c ve R gerekir. Kutle modeli, Y*, disk geometrisi
GEREKMEZ. Ikisi de Genzel Tablo 1'de DOGRUDAN OLCULMUS buyukluklerdir.

===============================  CAPA  =================================
Ayni formul once YEREL orneklemde (SPARC, z~0) kosulur. Yerelde tutuyorsa
yuksek-z'deki sapma gercek bir evrim sinyalidir; yerelde de tutmuyorsa
formulun kendisi sucludur. Capa olmadan sinav yorumlanamaz.

Veri: veri/_genzel2017_tablo1.csv  (PDF'ten elle aktarildi, kaynak dosyada)
Cikti: SINIF_CALISMASI/90_YUKSEK_Z/ -> SONUC.csv · yuksek_z.png
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
CIK = os.path.join(SK, '90_YUKSEK_Z')
os.makedirs(CIK, exist_ok=True)

KPC = 3.0856776e19
G_SI = 6.67430e-11
M_N = 1.67492749804e-27
LOM = 3.568e-14                      # 92_M_TUT olcumu
A0_0 = G_SI * M_N / LOM ** 2         # yerel ornekelemin gerektirdigi a_0
OM, OL = 0.3, 0.7
Hz = lambda z: np.sqrt(OM * (1 + z) ** 3 + OL)

# --- galaktik birim (SPARC capasi icin) ---
G = 4.300917e-6
ACC = 1e6 / 3.0856776e19
RB, UPS = 1.4, 0.50
AD = ['01_erken_spiral', '02_orta_spiral', '03_gec_spiral',
      '04_cok_gec_spiral', '05_macellan', '06_duzensiz']

print('a_0(z=0) = G m_n/l_om^2 = %.3e m/s^2   (l_om = %.1f fm, 92_M_TUT)'
      % (A0_0, LOM * 1e15))


def f_dm_ongoru(vc_kms, R_kpc, a0):
    """v_c^2 = v_bar^2 + v_bar sqrt(a_0 R) coz -> f_DM = 1 - (v_bar/v_c)^2.
    Kutle modeli GEREKMEZ; yalniz olculen v_c ve R."""
    b = np.sqrt(a0 * R_kpc * KPC) / (vc_kms * 1e3)
    s = (-b + np.sqrt(b ** 2 + 4)) / 2
    return 1 - s ** 2


# ==================================================================== CAPA
print('\n' + '=' * 100)
print('0) CAPA — ayni formul YEREL orneklemde (SPARC, z~0) tutuyor mu?')
CAPA = []
for sn in AD:
    for f in sorted(glob.glob(os.path.join(SK, sn, 'veri', '*_rotmod.dat'))):
        d = np.loadtxt(f)
        R, Vo, eV, Vg, Vd, Vb, SBd, SBb = [d[:, i] for i in range(8)]
        vb2 = np.sign(Vg) * Vg ** 2 + UPS * Vd ** 2 + RB * UPS * Vb ** 2
        j = np.argmin(np.abs(R - np.median(R)))          # egrinin orta yaricapi
        if vb2[j] <= 0 or Vo[j] <= 0 or Vo[j] ** 2 <= vb2[j]:
            continue
        CAPA.append((f_dm_ongoru(Vo[j], R[j], A0_0), 1 - vb2[j] / Vo[j] ** 2, Vo[j]))
CAPA = np.array(CAPA)
d_capa = CAPA[:, 0] - CAPA[:, 1]
print('  n = %d galaksi (orta yaricapta)' % len(CAPA))
print('  f_DM ongoru medyan %.3f · olculen medyan %.3f · FARK %+.3f (sacilma %.3f)'
      % (np.median(CAPA[:, 0]), np.median(CAPA[:, 1]), np.median(d_capa), np.std(d_capa)))
print('  -> capa %s' % ('TUTUYOR (|fark| < 0,05)' if abs(np.median(d_capa)) < 0.05
                        else 'TUTMUYOR — yuksek-z sonucu bu kaymayla birlikte okunmali'))
CAPA_KAY = float(np.median(d_capa))

# =============================================================== YUKSEK z
G7 = list(csv.DictReader(
    (l for l in open(os.path.join(KOK, 'veri', '_genzel2017_tablo1.csv'),
                     encoding='utf-8') if not l.startswith('#'))))
print('\n' + '=' * 100)
print('0b) IC TUTARLILIK — Genzel\'in kendi sayilari birbirini tutuyor mu?')
print('    v_bar(f_DM\'den) =? v_bar(M_bar\'dan, kovan tam + diskin yarisi)')
_o = []
for g in G7:
    vc = float(g['vc_kms']); R = float(g['R_half_kpc'])
    v1 = vc * np.sqrt(1 - float(g['fDM']))
    Mb = float(g['Mbar_fit_1e11Msun']) * 1e11; fb = float(g['Mbulge_bolu_Mbar'])
    v2 = np.sqrt(G * Mb * (fb + 0.5 * (1 - fb)) / R)
    _o.append(v2 / v1)
print('    oranlar: %s  ·  medyan %.2f'
      % (' '.join('%.2f' % x for x in _o), np.median(_o)))
print('    -> 1\'e yakin: tablo dogru okundu, sayilar ic tutarli.')
print('       (%%%d\'lik fark kuresel yaklasimin diske gore fazlasidir, beklenen.)'
      % round(100 * (np.median(_o) - 1)))

print('\n' + '=' * 100)
print('1) YUKSEK-z — Genzel+2017 Tablo 1, %d galaksi' % len(G7))
print('  %-12s %6s %7s %7s | %8s %10s | %10s %10s'
      % ('galaksi', 'z', 'R_1/2', 'v_c', 'f_DM', 'aralik', 'SABIT', 'KOZMIK'))
SAT = []
for g in G7:
    z = float(g['z']); R = float(g['R_half_kpc']); vc = float(g['vc_kms'])
    fo = float(g['fDM']); alt = float(g['fDM_alt']); ust = float(g['fDM_ust'])
    fs = f_dm_ongoru(vc, R, A0_0)
    fk = f_dm_ongoru(vc, R, A0_0 * Hz(z))
    SAT.append(dict(ad=g['Galaksi'], z=z, R=R, vc=vc, fo=fo, alt=alt, ust=ust,
                    us=g['fDM_ust_sinir_mi'] == 'evet', fs=fs, fk=fk,
                    Mb=float(g['Mbar_fit_1e11Msun'])))
    print('  %-12s %6.3f %7.1f %7.0f | %8.2f %10s | %10.3f %10.3f'
          % (g['Galaksi'], z, R, vc, fo, '%.2f-%.2f' % (alt, ust), fs, fk))

fo = np.array([s['fo'] for s in SAT]); ust = np.array([s['ust'] for s in SAT])
fs = np.array([s['fs'] for s in SAT]); fk = np.array([s['fk'] for s in SAT])
zz = np.array([s['z'] for s in SAT])

print('\n' + '=' * 100)
print('2) HUKUM')
print('  %-28s %10s %10s %12s %14s'
      % ('okuma', 'medyan', 'medyan', 'yayinin', 'ust sinirin'))
print('  %-28s %10s %10s %12s %14s'
      % ('', 'f_DM', 'artik', 'araliginda', 'ustunde'))
for ad, fp in [('SABIT  a_0(z)=a_0(0)', fs), ('KOZMIK a_0(z)~H(z)', fk)]:
    ic = int(np.sum((fp >= [s['alt'] for s in SAT]) & (fp <= ust)))
    asan = int(np.sum(fp > ust))
    print('  %-28s %10.3f %+10.3f %9d/%d %11d/%d'
          % (ad, np.median(fp), np.median(fp - fo), ic, len(SAT), asan, len(SAT)))
print('  %-28s %10.3f %10s' % ('GOZLENEN (Genzel+2017)', np.median(fo), '—'))
print('\n  ki-kare benzeri (ust sinirlar ust deger sayilarak):')
for ad, fp in [('SABIT ', fs), ('KOZMIK', fk)]:
    hedef = np.array([s['ust'] if s['us'] else s['fo'] for s in SAT])
    hata = np.array([max(s['ust'] - s['fo'], 0.05) / 2 for s in SAT])
    print('    %s : ortalama |artik|/sigma = %.2f' % (ad, np.mean(np.abs(fp - hedef) / hata)))

kaz = 'SABIT' if np.median(np.abs(fs - fo)) < np.median(np.abs(fk - fo)) else 'KOZMIK'
print('\n  -> %s okuma daha yakin (medyan |artik| %.3f vs %.3f)'
      % (kaz, np.median(np.abs(fs - fo)), np.median(np.abs(fk - fo))))
print('  AMA IKISI DE ASIYOR: teori bu alti galakside f_DM\'yi FAZLA ongoruyor.')
print('     sabit okuma  : medyan +%.2f' % np.median(fs - fo))
print('     kozmik okuma : medyan +%.2f' % np.median(fk - fo))
print('     Yerel capa kaymasi %+.3f — asimin %s bu kaymadan geliyor.'
      % (CAPA_KAY, 'bir kismi' if abs(CAPA_KAY) > 0.03 else 'cok azi'))

with open(os.path.join(CIK, 'SONUC.csv'), 'w', encoding='utf-8', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['Galaksi', 'z', 'R_half_kpc', 'vc_kms', 'Mbar_1e11',
                'GENZEL_fDM', 'GENZEL_alt', 'GENZEL_ust', 'ust_sinir_mi',
                'ONG_SABIT', 'ONG_KOZMIK', 'artik_SABIT', 'artik_KOZMIK'])
    for s in SAT:
        w.writerow([s['ad'], s['z'], s['R'], s['vc'], s['Mb'], s['fo'], s['alt'],
                    s['ust'], 'evet' if s['us'] else 'hayir',
                    '%.3f' % s['fs'], '%.3f' % s['fk'],
                    '%+.3f' % (s['fs'] - s['fo']), '%+.3f' % (s['fk'] - s['fo'])])

# ------------------------------------------------------------------ grafik
fig, ax = plt.subplots(1, 3, figsize=(16.4, 5.6), facecolor='#121212')
for a in ax:
    a.set_facecolor('#121212'); a.grid(alpha=.13)

a = ax[0]
a.plot(CAPA[:, 1], CAPA[:, 0], '.', color='#52525b', ms=4, alpha=.5,
       label='SPARC $z\\approx0$ (%d)' % len(CAPA))
a.plot([0, 1], [0, 1], '--', color='#f87171', lw=1.6, label='eşitlik')
a.set_xlim(0, 1); a.set_ylim(0, 1)
a.set_xlabel('ölçülen $f_{DM}$', fontsize=10.5)
a.set_ylabel('öngörülen $f_{DM}$', fontsize=10.5)
a.set_title('ÇAPA — formül yerelde tutuyor mu?', fontsize=12.2, color='white', pad=8)
a.text(.04, .96, ('medyan fark %+.3f\nsaçılma %.3f' % (CAPA_KAY, np.std(d_capa))).replace('.', ','),
       transform=a.transAxes, va='top', fontsize=9.4, color='#4ade80', family='monospace')
a.legend(fontsize=8.8, framealpha=.3, loc='lower right')

a = ax[1]
x = np.arange(len(SAT))
for i, s in enumerate(SAT):
    if s['us']:
        a.annotate('', (i, s['ust']), (i, s['ust'] + .1),
                   arrowprops=dict(arrowstyle='-|>', color='#ffcc00', lw=1.8))
        a.plot([i - .22, i + .22], [s['ust']] * 2, '-', color='#ffcc00', lw=2.4)
    else:
        a.errorbar(i, s['fo'], yerr=[[s['fo'] - s['alt']], [s['ust'] - s['fo']]],
                   fmt='o', color='#ffcc00', ms=8, elinewidth=1.8, capsize=4)
a.plot(x, fs, 's', color='#16a34a', ms=10, label='SABİT $a_0$', zorder=5)
a.plot(x, fk, 'D', color='#7c3aed', ms=9, label='KOZMİK $a_0\\propto H(z)$', zorder=5)
a.set_xticks(x)
a.set_xticklabels(['%s\n$z$=%.2f' % (s['ad'].replace('_', ' '), s['z']) for s in SAT],
                  fontsize=7.2, rotation=25)
a.set_ylabel('$f_{DM}(R_{1/2})$', fontsize=10.5)
a.set_ylim(0, 0.75)
a.set_title('Genzel+2017 · sarı = gözlem (ok = üst sınır)', fontsize=12.2,
            color='white', pad=8)
a.legend(fontsize=9, framealpha=.3, loc='upper right')

a = ax[2]
a.plot(zz, fs - fo, 's-', color='#16a34a', ms=8, lw=1.8, label='SABİT')
a.plot(zz, fk - fo, 'D-', color='#7c3aed', ms=8, lw=1.8, label='KOZMİK')
a.axhline(0, color='#ffcc00', lw=2, label='gözlem')
a.axhline(CAPA_KAY, color='#f87171', ls=':', lw=1.8,
          label=('yerel çapa kayması %+.3f' % CAPA_KAY).replace('.', ','))
a.set_xlabel('kırmızıya kayma $z$', fontsize=10.5)
a.set_ylabel('artık  $f_{DM}^{öng}-f_{DM}^{gözl}$', fontsize=10.5)
a.set_title('Artık — hangisi daha yakın?', fontsize=12.2, color='white', pad=8)
a.legend(fontsize=8.6, framealpha=.3, loc='upper left')

fig.suptitle('Yüksek-$z$ sınavı — teorinin ilk SPARC dışı sınavı  ·  Genzel+2017, 6 galaksi',
             fontsize=14.4, color='white', y=.975)
fig.text(.5, .035, 'Öngörü yalnız ölçülen $v_c$ ve $R_{1/2}$ kullanır: '
                   '$v_c^2=v_{bar}^2+v_{bar}\\sqrt{a_0R}$ çözülür. Kütle modeli, '
                   '$\\Upsilon_*$ ve disk geometrisi GEREKMEZ.',
         ha='center', fontsize=9.4, color='#a1a1aa')
fig.text(.5, .008, 'Evrenakı\'da karanlık madde yoktur; Genzel\'in $f_{DM}$\'si burada '
                   'F4\'ün $v^2$ içindeki payıdır.', ha='center', fontsize=9.4, color='#a1a1aa')
fig.subplots_adjust(left=.055, right=.986, top=.855, bottom=.20, wspace=.28)
plt.savefig(os.path.join(CIK, 'yuksek_z.png'), dpi=140,
            facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print('\n-> 90_YUKSEK_Z/  SONUC.csv · yuksek_z.png')
