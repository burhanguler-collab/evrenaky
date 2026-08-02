# -*- coding: utf-8 -*-
"""
dSph SINAVI — M-48 (kopru) + M-49 (EFE) ilk bagimsiz-veri sinavi (87_ETKIN_YASA is 13; G-13)

VERI: McConnachie 2012 (AJ 144, 4; VizieR J/AJ/144/4 CfA aynasi) — SPARC'tan tamamen bagimsiz.
      veri/_mcconnachie2012.tsv (degistirilmemis).

ONCEDEN YAZILAN KURALLAR (veriye bakilmadan):
 1) Ornek: sigma* olculmus (ust-limit degil), R2>0, Mass>0. Sagittarius HARIC (bilinen
    gelgit bozulmasi). ANA ornek: Mass >= 0.1 (1e5 Msun; ultra-soluklarin sistematigi ayri
    rapor edilir, hukme girmez).
 2) Girdiler: M_bar=(Mass+1.33*M.HI)*1e6 Msun (McConnachie kurali Ups_V=1; x2 duyarliligi
    rapor edilir); r_h=R2 (pc->kpc); g_ext: MW uydusu 220^2/D(MW), M31 uydusu 230^2/D(M31),
    izole: max(MW,M31) alani (kucuk).
 3) Ongoru (M-48 Jeans, alpha=2, r_h'ta; EFE_TURETIMI konvansiyonu):
       sigma_pred^2 = r_h*[g_bar + g_F4*W_ic*W_dis]/2
       g_bar=G M/r_h^2;  g_F4=sqrt(G M a0)/r_h;  W_ic=min(1,a0/g_bar);
       W_dis=min(1,sqrt(g_bar/g_ext))    [M-49]
 4) OLCUTLER: (i) grup medyan log(sig_pred/sig_obs) EFE'siz ve EFE'li;
    (ii) G-13 imzasi: EFE'siz artik ~ log g_ext pozitif korele olmali (guclu alanda fazla-
    ongoru), EFE'li artikta korelasyon kucullmeli; (iii) izole<->uydu farki.
 5) Bu bir MERTEBE/ISARET sinavidir: alpha, anizotropi, Ups_V, M_kaps konvansiyonu O(1);
    p-degeri uretilir ama [T] gecisi tek basina buna baglanmaz.

Cikti: SINIF_CALISMASI/87_ETKIN_YASA/SONUC_DSPH.csv
"""
import os, sys, io, csv, math, warnings
import numpy as np

warnings.filterwarnings('ignore')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

KOK = os.path.dirname(os.path.abspath(__file__))
G = 4.300917e-6
ACC = 1e6 / 3.0856776e19
A0 = 1.75 * 1.038 * (2.99792458e8 * (70e3 / 3.0857e22)) / ACC / 16.1   # pencereli resmi
VMW, VM31 = 220.0, 230.0

h = io.open(os.path.join(KOK, 'veri', '_mcconnachie2012.tsv'), encoding='utf-8', errors='replace').read().split('\n')
i0 = [i for i, l in enumerate(h) if l.startswith('recno\tSubG')][0]
cols = h[i0].split('\t')
ix = {c: j for j, c in enumerate(cols)}

CUC = []
for l in h[i0 + 2:]:
    p = l.split('\t')
    if len(p) < len(cols) - 2:
        break
    gv = lambda c: (p[ix[c]].strip() if ix[c] < len(p) else '')
    if not gv('sigma*') or gv('l_sigma*'):
        continue
    try:
        sig = float(gv('sigma*')); R2 = float(gv('R2')); Ms = float(gv('Mass'))
    except ValueError:
        continue
    if R2 <= 0 or Ms <= 0:
        continue
    ad = gv('Name')
    if ad.startswith('Sagittarius dSph'):
        continue
    MHI = float(gv('M.HI')) if gv('M.HI') else 0.0
    dmw = float(gv('D(MW)')) if gv('D(MW)') else 1e9
    dm31 = float(gv('D(M31)')) if gv('D(M31)') else 1e9
    sub = gv('SubG')
    if sub == 'MW':
        gext = VMW ** 2 / dmw
    elif sub == 'M31':
        gext = VM31 ** 2 / dm31
    else:
        gext = max(VMW ** 2 / dmw, VM31 ** 2 / dm31)
    CUC.append(dict(ad=ad, sub=sub, sig=sig, rh=R2 / 1e3,
                    M=(Ms + 1.33 * MHI) * 1e6, gext=gext, Ms=Ms))
print('%d cuce (sigma olculu, Sgr haric) · ana ornek (M*>=1e5): %d' %
      (len(CUC), sum(1 for c in CUC if c['Ms'] >= 0.1)))

def ongoru(c, efe):
    gbar = G * c['M'] / c['rh'] ** 2
    gf4 = math.sqrt(G * c['M'] * A0) / c['rh']
    W = min(1.0, A0 / gbar)
    if efe:
        W *= min(1.0, math.sqrt(gbar / c['gext']))
    return math.sqrt(c['rh'] * (gbar + gf4 * W) / 2.0)

def spearman(a, b):
    def rk(x):
        s = sorted(range(len(x)), key=lambda i: x[i]); r = [0] * len(x)
        for i, j in enumerate(s):
            r[j] = i + 1
        return r
    ra, rb = rk(a), rk(b); n = len(a)
    ma = sum(ra) / n; mb = sum(rb) / n
    pay = sum((x - ma) * (y - mb) for x, y in zip(ra, rb))
    pd = math.sqrt(sum((x - ma) ** 2 for x in ra) * sum((y - mb) ** 2 for y in rb))
    return pay / pd if pd else 0.0

ANA = [c for c in CUC if c['Ms'] >= 0.1]
print('\n1) GRUP MEDYANLARI — log10(sigma_pred/sigma_obs)')
print('%-12s %4s | %10s %10s' % ('grup', 'n', 'EFEsiz', 'EFEli'))
for sub, et in [('MW', 'MW uydu'), ('M31', 'M31 uydu'), ('Rest', 'IZOLE')]:
    gg = [c for c in ANA if c['sub'] == sub]
    if not gg:
        continue
    d0 = [math.log10(ongoru(c, False) / c['sig']) for c in gg]
    d1 = [math.log10(ongoru(c, True) / c['sig']) for c in gg]
    print('%-12s %4d | %+10.3f %+10.3f' % (et, len(gg), np.median(d0), np.median(d1)))
d0 = [math.log10(ongoru(c, False) / c['sig']) for c in ANA]
d1 = [math.log10(ongoru(c, True) / c['sig']) for c in ANA]
lg = [math.log10(c['gext']) for c in ANA]
print('%-12s %4d | %+10.3f %+10.3f' % ('TUM ANA', len(ANA), np.median(d0), np.median(d1)))

print('\n2) G-13 IMZASI — artik ~ log g_ext (Spearman):')
print('   EFEsiz: %+0.3f   EFEli: %+0.3f   (beklenen: pozitiften sifira dogru)' %
      (spearman(d0, lg), spearman(d1, lg)))

print('\n3) DUYARLILIK — Ups_V x2 (M -> 2M):')
for c in ANA:
    c['M'] *= 2
d0b = [math.log10(ongoru(c, False) / c['sig']) for c in ANA]
d1b = [math.log10(ongoru(c, True) / c['sig']) for c in ANA]
print('   medyan EFEsiz %+0.3f  EFEli %+0.3f' % (np.median(d0b), np.median(d1b)))
for c in ANA:
    c['M'] /= 2

print('\n4) GALAKSI TABLOSU (ana ornek):')
print('%-24s %-4s %7s %6s %7s | %6s %8s %8s' % ('ad', 'grup', 'M*/1e6', 'r_h', 'g_ext', 'sig_o', 'pred_0', 'pred_EFE'))
for c in sorted(ANA, key=lambda c: -c['Ms']):
    print('%-24s %-4s %7.1f %6.2f %7.0f | %6.1f %8.1f %8.1f' %
          (c['ad'][:24], c['sub'], c['Ms'], c['rh'], c['gext'], c['sig'],
           ongoru(c, False), ongoru(c, True)))

yol = os.path.join(KOK, 'SINIF_CALISMASI', '87_ETKIN_YASA', 'SONUC_DSPH.csv')
with io.open(yol, 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Ad', 'Grup', 'Mstar_1e6', 'MHIdahil_Mbar_1e6', 'rh_kpc', 'gext_kms2kpc',
                'sigma_obs', 'sigma_pred_EFEsiz', 'sigma_pred_EFEli', 'ana_ornek'])
    for c in CUC:
        w.writerow([c['ad'], c['sub'], '%.3f' % c['Ms'], '%.3f' % (c['M'] / 1e6),
                    '%.3f' % c['rh'], '%.1f' % c['gext'], '%.1f' % c['sig'],
                    '%.2f' % ongoru(c, False), '%.2f' % ongoru(c, True),
                    1 if c['Ms'] >= 0.1 else 0])
print('\nyazildi: %s' % yol)
