r"""TOPLU DEFTER — butun duzeltmeler uygulaninca NE DEGISIR?

=============================  UC KURULUM  =============================
A  MEVCUT (kitabin hali)
     l_omega = sqrt(G M_bar / a_0)        [TOPLAM kutle]
     a_0     = c H_0 / 16,1 = 4,224e-11   [kalibre]

B  YALNIZ YEREL KUTLE  (94_YEREL_LOMEGA)
     l_omega = sqrt(G M_kaps(R) / a_0)    [YEREL kutle]  ->  v_F4^2 = sqrt(G M_kaps a_0)
     a_0     = ayni (4,224e-11)

C  HEPSI  (94_YEREL_LOMEGA + 92_M_TUT)
     l_omega = yerel
     a_0     = G m_n / l_om_mikro^2 = 8,78e-11  (x2,08)   [olculen l_om = 35,7 fm]

A->B: yeni parametre YOK, bir tutarsizligin giderilmesi.
B->C: a_0 kalibre bir ivme olmaktan cikip mikro sabitlerden turetiliyor.

============================  SINANAN HER SEY  =========================
 1) Donus egrisi RMS ve dis yari sapmasi — 141 galaksi, sinif sinif
 2) BTFR egimi ve normalizasyonu — 121 galaksi
 3) RAR medyan artik ve BICIM egimi — 2888 nokta (kendi egrilerimizden)
 4) ETG dis nokta — 16 galaksi
 5) S0+BCD — 8 galaksi
 6) YUKSEK-z f_DM — 6 galaksi (Genzel+2017)
 7) LCDM karsilastirmasi — nerede varsa

Cikti: SINIF_CALISMASI/_HESAPLAR/toplu_defter.csv · toplu_defter.png
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
CIK = os.path.join(SK, '_HESAPLAR')
os.makedirs(CIK, exist_ok=True)

G = 4.300917e-6
ACC = 1e6 / 3.0856776e19
A0_K = (2.99792458e8 * (70e3 / 3.0857e22)) / ACC / 16.1     # kitap
KAT_C = 2.08                                                 # 92_M_TUT'un olctugu
RB, UPS = 1.4, 0.50
KPC = 3.0856776e19
AD = {'01_erken_spiral': 'Sa–Sab', '02_orta_spiral': 'Sb–Sbc', '03_gec_spiral': 'Sc–Scd',
      '04_cok_gec_spiral': 'Sd', '05_macellan': 'Sdm–Sm', '06_duzensiz': 'Im'}
KUR = [('A', 'MEVCUT', 'toplam', 1.0), ('B', 'yerel kütle', 'yerel', 1.0),
       ('C', 'yerel+×2,08', 'yerel', KAT_C), ('F', 'NİHAİ ×1,75', 'yerel', 1.75),
       ('P', 'PENCERELİ resmî (M-47)', 'pencere', 1.75 * 1.038)]

RHO = 3 * 0.07 ** 2 / (8 * np.pi * G)
mu = lambda x: np.log(1 + x) - x / (1 + x)
_lM1, _N, _be, _ga = 11.59, 0.0351, 1.376, 0.608
_Mh = 10 ** np.linspace(9.0, 15.0, 8000)
_Ms = _Mh * 2 * _N / ((_Mh / 10 ** _lM1) ** -_be + (_Mh / 10 ** _lM1) ** _ga)


def F4(Mk, Mb, tur, k, R=None):
    if tur == 'toplam':
        return G * Mk / np.sqrt(G * Mb / (k * A0_K))
    taban = np.sqrt(k * A0_K * G * np.maximum(Mk, 1e-9))
    if tur == 'pencere':                      # M-47: W = min(1, a0/g_kaps)
        gk = G * np.maximum(Mk, 1e-9) / R ** 2
        return taban * np.minimum(1.0, k * A0_K / gk)
    return taban


def yukle(kls):
    out = []
    for sn in kls:
        KA = {r['Galaksi']: r for r in csv.DictReader(
            open(os.path.join(SK, sn, 'KATALOG.csv'), encoding='utf-8'))}
        for f in sorted(glob.glob(os.path.join(SK, sn, 'veri', '*_rotmod.dat'))):
            ad = os.path.basename(f)[:-11]
            d = np.loadtxt(f)
            R, Vo, eV, Vg, Vd, Vb, SBd, SBb = [d[:, i] for i in range(8)]
            Rp = R * 1e3
            L = lambda S: np.concatenate([[0.], np.cumsum(
                np.pi * (Rp[1:] ** 2 - Rp[:-1] ** 2) * .5 * (S[1:] + S[:-1]))])
            vb2 = np.maximum(np.sign(Vg) * Vg ** 2, 0.) + UPS * Vd ** 2 + RB * UPS * Vb ** 2
            Mk = np.maximum(UPS * L(SBd) + RB * UPS * L(SBb)
                            + np.maximum(R * np.sign(Vg) * Vg ** 2 / G, 0.), 1e-6)
            L36 = float(KA[ad]['L36_1e9Lsun']) * 1e9
            M200 = float(np.interp(UPS * L36, _Ms, _Mh)) if L36 > 0 else np.nan
            out.append(dict(ad=ad, tip=AD.get(sn, sn), R=R, Vo=Vo, eV=np.maximum(eV, 1.),
                            vb2=vb2, Mk=Mk, Mb=max(Mk[-1], 1e-6), M200=M200))
    return out


DISK = yukle(sorted(AD))
print('%d disk galaksisi · %d olcum noktasi'
      % (len(DISK), sum(len(g['R']) for g in DISK)))
SAT = []          # defter satirlari


def ekle(ad, birim, deg, yon, lcdm=None):
    SAT.append(dict(ad=ad, birim=birim, A=deg[0], B=deg[1], C=deg[2], F=deg[3], P=deg[4],
                    yon=yon, lcdm=lcdm))


# ----------------------------------------------------- 1) donus egrisi
rms = {}; sap = {}
for kod, _, tur, k in KUR:
    r, s = [], []
    for g in DISK:
        v = np.sqrt(np.maximum(g['vb2'] + F4(g['Mk'], g['Mb'], tur, k, g['R']), 1e-9))
        r.append(np.sqrt(np.mean((v - g['Vo']) ** 2)))
        m = g['R'] > np.median(g['R'])
        s.append(100 * np.mean((v[m] - g['Vo'][m]) / g['Vo'][m]))
    rms[kod] = np.median(r); sap[kod] = np.median(s)
# LCDM ayni olcut
rl = []
for g in DISK:
    if not np.isfinite(g['M200']):
        continue
    c = 10 ** (0.905 - 0.101 * np.log10(g['M200'] * 0.7 / 1e12))
    r200 = (3 * g['M200'] / (4 * np.pi * 200 * RHO)) ** (1 / 3.)
    v = np.sqrt(np.maximum(g['vb2'] + G * g['M200'] / g['R'] * mu(g['R'] * c / r200) / mu(c), 1e-9))
    rl.append(np.sqrt(np.mean((v - g['Vo']) ** 2)))
ekle('Dönüş eğrisi RMS (141 gal.)', 'km/s', [rms['A'], rms['B'], rms['C'], rms['F'], rms['P']], 'kucuk',
     np.median(rl))
ekle('Dış yarı sapması', '%', [sap['A'], sap['B'], sap['C'], sap['F'], sap['P']], 'sifir')

# ----------------------------------------------------- 2) BTFR
def mrt(y, al):
    h = open(y, encoding='utf-8', errors='replace').read().split('\n')
    a = [i for i, x in enumerate(h) if x.startswith('----')][-1]
    D = {}
    for Lx in h[a + 1:]:
        p = Lx.split()
        if len(p) < len(al):
            continue
        try:
            D[p[0]] = {kk: float(v) for kk, v in zip(al[1:], p[1:len(al)])}
        except ValueError:
            pass
    return D


B19 = mrt(os.path.join(KOK, 'veri', '_BTFR_Lelli2019.mrt'),
          ['Name', 'lMb', 'elMb', 'Inc', 'eInc', 'Vf', 'eVf', 'V2exp', 'eV2exp', 'V2eff',
           'eV2eff', 'Vmax', 'eVmax', 'Wp20', 'eWp20', 'Wm50', 'eWm50', 'Wm50c', 'eWm50c'])
IX = {g['ad']: g for g in DISK}
N = [n for n in B19 if B19[n]['Vf'] > 0 and n in IX]
lMb = np.array([B19[n]['lMb'] for n in N]); Vf = np.array([B19[n]['Vf'] for n in N])
eg, nor = {}, {}
for kod, _, tur, k in KUR:
    v = np.array([np.sqrt(max(IX[n]['vb2'][-1]
                  + F4(IX[n]['Mk'], IX[n]['Mb'], tur, k, IX[n]['R'])[-1], 1e-9)) for n in N])
    eg[kod] = np.polyfit(np.log10(v), lMb, 1)[0]
    nor[kod] = 10 ** np.median(np.log10(v / Vf))
ekle('BTFR eğimi (%d gal.)' % len(N), '', [eg['A'], eg['B'], eg['C'], eg['F'], eg['P']], 'band', 2.716)
ekle('BTFR normalizasyonu', 'v_öng/v_ölç', [nor['A'], nor['B'], nor['C'], nor['F'], nor['P']], 'bir', 1.027)

# ----------------------------------------------------- 3) RAR
gb = np.concatenate([g['vb2'] / g['R'] * ACC for g in DISK])
go = np.concatenate([g['Vo'] ** 2 / g['R'] * ACC for g in DISK])
KEN = np.arange(-12.0, -8.5 + 1e-9, 0.25)
med, bic = {}, {}
for kod, _, tur, k in KUR:
    gp = np.concatenate([(g['vb2'] + F4(g['Mk'], g['Mb'], tur, k, g['R'])) / g['R'] * ACC
                         for g in DISK])
    m0 = (gb > 0) & (go > 0)
    med[kod] = np.median(np.log10(gp[m0] / go[m0]))
    xo, ao = [], []
    for lo, hi in zip(KEN[:-1], KEN[1:]):
        mm = m0 & (np.log10(gb) >= lo) & (np.log10(gb) < hi)
        if mm.sum() < 25:
            continue
        xo.append((lo + hi) / 2); ao.append(np.median(np.log10(gp[mm] / go[mm])))
    bic[kod] = np.polyfit(xo, ao, 1)[0]
ekle('RAR medyan artık', 'dex', [med['A'], med['B'], med['C'], med['F'], med['P']], 'sifir')
ekle('RAR BİÇİM eğimi', 'dex/dex', [bic['A'], bic['B'], bic['C'], bic['F'], bic['P']], 'sifir')

# ----------------------------------------------------- 4) ETG
E = []
for Lx in open(os.path.join(KOK, 'veri', '_etg.mrt'), encoding='utf-8', errors='replace'):
    p = Lx.split()
    if not p or p[0].startswith('#') or len(p) < 20:
        continue
    try:
        E.append([float(v) for v in p[12:20]])
    except ValueError:
        pass
E = np.array(E)
gb2, go2 = 10 ** E[:, 6], 10 ** E[:, 2]          # Ab2, Ao2 (dis nokta)
etg = {}
for kod, _, tur, k in KUR:
    # ETG'de yalniz RAR bicimi kullanilabilir (yaricap yok) -> yerel kurulum
    gp = gb2 + np.sqrt(k * A0_K * ACC * gb2) * (
        np.minimum(1.0, k * A0_K * ACC / gb2) if tur == 'pencere' else 1.0)
    etg[kod] = np.median(np.log10(gp / go2))
ekle('ETG dış nokta (16 gal.)', 'dex', [etg['A'], etg['B'], etg['C'], etg['F'], etg['P']], 'sifir', 0.045)

# ----------------------------------------------------- 5) S0+BCD
SB = yukle(['99_KARMASIK'])
GER = {x['Galaksi']: x for x in csv.DictReader(
    open(os.path.join(SK, '99_KARMASIK', 'GEREKCE.csv'), encoding='utf-8'))}
SB = [g for g in SB if GER.get(g['ad'], {}).get('Tip') in ('S0', 'BCD')]
sb = {}
for kod, _, tur, k in KUR:
    sb[kod] = np.median([np.sqrt(np.mean((np.sqrt(np.maximum(
        g['vb2'] + F4(g['Mk'], g['Mb'], tur, k, g['R']), 1e-9)) - g['Vo']) ** 2)) for g in SB])
ekle('S0+BCD RMS (%d gal.)' % len(SB), 'km/s', [sb['A'], sb['B'], sb['C'], sb['F'], sb['P']], 'kucuk')

# ----------------------------------------------------- 6) YUKSEK-z
GZ = list(csv.DictReader(
    (l for l in open(os.path.join(KOK, 'veri', '_genzel2017_tablo1.csv'), encoding='utf-8')
     if not l.startswith('#'))))
hz = {}
for kod, _, tur, k in KUR:
    a0 = k * A0_K * ACC
    f = []
    for g in GZ:
        Rh = float(g['R_half_kpc']); vc = float(g['vc_kms'])
        if tur == 'pencere':                  # M-47: oz-uyumlu s cozumu
            a0u = k * A0_K
            ss = 0.9
            for _ in range(40):
                vbar2 = (ss * vc) ** 2
                Wp = min(1., a0u / max(vbar2 / Rh, 1e-12))
                vF42 = np.sqrt(max(vbar2, 1e-9) * a0u * Rh) * Wp
                ss = np.sqrt(max(vc ** 2 - vF42, 1e-9)) / vc
            f.append(1 - ss ** 2 - float(g['fDM']))
        else:
            b = np.sqrt(a0 * Rh * KPC) / (vc * 1e3)
            ss = (-b + np.sqrt(b ** 2 + 4)) / 2
            f.append(1 - ss ** 2 - float(g['fDM']))
    hz[kod] = np.median(f)
ekle('Yüksek-z f_DM artığı (6 gal.)', '', [hz['A'], hz['B'], hz['C'], hz['F'], hz['P']], 'sifir')

# ------------------------------------------------------------------ tablo
print('\n' + '=' * 104)
print('TOPLU DEFTER — A: mevcut · B: yerel · C: x2,08 · F: x1,75 · P: PENCERELI RESMI (M-47)')
print('=' * 104)
print('  %-30s %10s | %8s %8s %8s %8s %8s | %8s %s'
      % ('ölçüt', 'birim', 'A', 'B', 'C', 'F', 'P', 'A→P', 'ΛCDM'))
IY = 0; KO = 0
for s in SAT:
    if s['yon'] == 'kucuk':
        iyi = s['P'] < s['A']; oran = '%+.0f%%' % (100 * (s['P'] / s['A'] - 1))
    elif s['yon'] == 'sifir':
        iyi = abs(s['P']) < abs(s['A'])
        oran = '%+.0f%%' % (100 * (abs(s['P']) / max(abs(s['A']), 1e-9) - 1))
    elif s['yon'] == 'bir':
        iyi = abs(s['P'] - 1) < abs(s['A'] - 1)
        oran = '%+.3f' % (abs(s['P'] - 1) - abs(s['A'] - 1))
    else:                                    # band: 3,530-3,738
        d = lambda v: 0 if 3.530 <= v <= 3.738 else min(abs(v - 3.530), abs(v - 3.738))
        iyi = d(s['P']) <= d(s['A']); oran = 'band' if d(s['P']) == 0 else '%+.3f' % d(s['P'])
    IY += iyi; KO += (not iyi)
    print('  %-30s %10s | %8.3f %8.3f %8.3f %8.3f %8.3f | %8s %s%s'
          % (s['ad'], s['birim'], s['A'], s['B'], s['C'], s['F'], s['P'], oran,
             '' if s['lcdm'] is None else '%.3f' % s['lcdm'],
             '   <-- KOTULESTI' if not iyi else ''))
print('\n  A -> P (PENCERELI RESMI):  %d olcut IYILESTI · %d olcut KOTULESTI  (toplam %d)' % (IY, KO, len(SAT)))

print('\nSINIF SINIF DONUS EGRISI RMS (km/s)')
print('  %-9s %5s | %7s %7s %7s %7s %7s | %8s' % ('sınıf', 'n', 'A', 'B', 'C', 'F', 'P', 'A→P'))
for sn in sorted(AD):
    Lg = [g for g in DISK if g['tip'] == AD[sn]]
    v = []
    for kod, _, tur, k in KUR:
        v.append(np.median([np.sqrt(np.mean((np.sqrt(np.maximum(
            g['vb2'] + F4(g['Mk'], g['Mb'], tur, k, g['R']), 1e-9)) - g['Vo']) ** 2)) for g in Lg]))
    print('  %-9s %5d | %7.2f %7.2f %7.2f %7.2f %7.2f | %7.0f%%'
          % (AD[sn], len(Lg), v[0], v[1], v[2], v[3], v[4], 100 * (v[4] / v[0] - 1)))

with open(os.path.join(CIK, 'toplu_defter.csv'), 'w', encoding='utf-8', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['olcut', 'birim', 'A_mevcut', 'B_yerel', 'C_yerel_x2_08',
                'F_x1_75', 'P_PENCERELI_RESMI', 'iyi_yon', 'LCDM'])
    for s in SAT:
        w.writerow([s['ad'], s['birim'], '%.4f' % s['A'], '%.4f' % s['B'],
                    '%.4f' % s['C'], '%.4f' % s['F'], '%.4f' % s['P'], s['yon'],
                    '' if s['lcdm'] is None else '%.4f' % s['lcdm']])

# ------------------------------------------------------------------ grafik
fig, ax = plt.subplots(2, 5, figsize=(20.4, 8.4), facecolor='#121212')
ax = ax.ravel()
for a in ax:
    a.set_facecolor('#121212'); a.grid(alpha=.13)
for a in ax[len(SAT):]:
    a.axis('off')
for i, s in enumerate(SAT[:10]):
    a = ax[i]
    vv = [s['A'], s['B'], s['C'], s['F'], s['P']]
    cl = ['#7c3aed', '#a1a1aa', '#4ade80', '#86efac', '#16a34a']
    a.bar(range(5), vv, .62, color=cl)
    if s['lcdm'] is not None:
        a.axhline(s['lcdm'], color='#f87171', ls='--', lw=1.8, label='ΛCDM')
        a.legend(fontsize=8, framealpha=.3)
    if s['yon'] == 'sifir':
        a.axhline(0, color='#ffcc00', lw=1.4)
    elif s['yon'] == 'bir':
        a.axhline(1, color='#ffcc00', lw=1.4)
    elif s['yon'] == 'band':
        a.axhspan(3.530, 3.738, color='#ffcc00', alpha=.2)
    for j, v in enumerate(vv):
        a.text(j, v + (max(vv) - min(min(vv), 0)) * .04, ('%.3f' % v).replace('.', ','),
               ha='center', fontsize=9, color=cl[j], fontweight='bold')
    a.set_xticks(range(5)); a.set_xticklabels(['A', 'B', 'C', 'F', 'P'], fontsize=10)
    a.set_title('%s\n(%s)' % (s['ad'], s['birim'] or '—'), fontsize=10, color='white', pad=6)
fig.suptitle('TOPLU DEFTER — A: mevcut · B: yerel · C: ×2,08 · F: ×1,75 · P: PENCERELİ RESMİ (M-47)  ·  '
             'A→P: %d iyileşti, %d kötüleşti' % (IY, KO), fontsize=14.6, color='white', y=.975)
fig.text(.5, .015, 'P (RESMİ, M-47): yerel $\\ell_\\omega$ + $a_0=7{,}67\\times10^{-11}$ m/s$^2$ '
                   '+ Rankine penceresi $W=\\min(1,\\,a_0/g_{kaps})$ — parametresiz. '
                   'Sarı = hedef · kırmızı kesik = ΛCDM.',
         ha='center', fontsize=9.4, color='#a1a1aa')
fig.subplots_adjust(left=.045, right=.988, top=.885, bottom=.075, hspace=.42, wspace=.26)
plt.savefig(os.path.join(CIK, 'toplu_defter.png'), dpi=140,
            facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print('\n-> _HESAPLAR/  toplu_defter.csv · toplu_defter.png')
