# -*- coding: utf-8 -*-
"""
MIGHTEE ORNEKLEM-DISI SINAVI (87_ETKIN_YASA is 14) — a0'in ikinci bagimsiz-aile dogrulamasi.

Veri: Ponomareva+2021 (MNRAS 508,1195; VizieR J/MNRAS/508/1195, CfA aynasi)
      -> veri/_mightee_btfr.tsv (degistirilmemis). SPARC ortusmesi SIFIR.

ONCEDEN YAZILAN KURALLAR:
  kesim: I3DB>=40, Nbeams>=3;  M_bar = 1.33*10^logMHI + 10^logM*  (yayinin kutleleri)
  SIFIR YENIDEN-KALIBRASYON: a0 = 7.67e-11 (pencereli resmi) donmus.
  Olcu: Delta = log v_olc - 0.25 log(G M_bar a0)
  Teori bandi: [0, +0.053]   (saf-F4 asimptotu .. +F1 payi, SPARC medyani l_om/R=0.27)
  Iki yanli hiz tanimi gercegi sarar: v_W = W50/(2 sin i)  (+yanli, turbulans)
                                      V_out                (-yanli, duzluk-alti)
  MOND kiyasi: ayni Delta, g_dagger=1.2e-10 ile.
Sonuclar: MIGHTEE_SINAVI.md (medyan v_W +0.083 / V_out -0.026; braket bandi icine alir -> GECTI)
"""
import io, os, math, sys
import numpy as np

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
KOK = os.path.dirname(os.path.abspath(__file__))
G = 4.300917e-6
ACC = 1e6 / 3.0856776e19
A0 = 1.75 * 1.038 * (2.99792458e8 * (70e3 / 3.0857e22)) / ACC / 16.1
GD = 1.2e-10 / ACC

h = io.open(os.path.join(KOK, 'veri', '_mightee_btfr.tsv'), encoding='utf-8', errors='replace').read().split('\n')
i0 = [i for i, l in enumerate(h) if l.startswith('recno\tID')][0]
cols = h[i0].split('\t'); ix = {c: j for j, c in enumerate(cols)}
dw, do, dm, LM, LV = [], [], [], [], []
for l in h[i0 + 2:]:
    p = l.split('\t')
    if len(p) < len(cols):
        break
    try:
        mhi = float(p[ix['logMHI']]); ms = float(p[ix['logM*']])
        inc = float(p[ix['I3DB']]); vo = float(p[ix['Vout']])
        w = float(p[ix['W50']]); nb = float(p[ix['Nbeams']])
    except ValueError:
        continue
    if inc < 40 or nb < 3:
        continue
    Mb = 1.33 * 10 ** mhi + 10 ** ms
    vw = w / (2 * math.sin(math.radians(inc)))
    vp = (G * Mb * A0) ** 0.25
    dw.append(math.log10(vw / vp)); do.append(math.log10(vo / vp))
    dm.append(math.log10(vw / (G * Mb * GD) ** 0.25))
    LM.append(math.log10(Mb)); LV.append(math.log10(vw))
dw, do, dm = map(np.array, (dw, do, dm))
print('MIGHTEE-HI: n=%d' % len(dw))
print('Delta [teori bandi 0..+0.053]:')
print('  v_W   medyan %+0.4f  sacilma %.3f' % (np.median(dw), np.std(dw)))
print('  V_out medyan %+0.4f  sacilma %.3f' % (np.median(do), np.std(do)))
print('  MOND (g_dagger), v_W: %+0.4f' % np.median(dm))
print('  naif egim (dar aralik, asagi-yanli — hukumsuz): %.2f' % np.polyfit(LV, LM, 1)[0])
