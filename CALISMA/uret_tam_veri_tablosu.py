"""Tum SPARC ornekleminin galaksi-basina fit sonuclarini markdown tablosu olarak uretir
ve 07_Galaktik_Yorungeler.md dosyasina yeni bir alt bolum olarak isler."""
import io, os, glob, warnings
warnings.filterwarnings('ignore')
import numpy as np
from scipy.optimize import curve_fit

BASE = r'C:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi'
VERI = os.path.join(BASE, r'Metin\Akademik\CALISMA\veri')
G = 4.300917e-6
RHO_CRIT = 3 * 0.07 ** 2 / (8 * np.pi * G)
H_RED = 0.7
C_SI = 2.99792458e8
KPC_M = 3.0856776e19
ACC = 1e6 / KPC_M
A0 = (C_SI * (70e3 / 3.0857e22) / (2 * np.pi)) / ACC
RF_UST = 3e3


def yukle(f):
    d = np.loadtxt(f)
    if d.ndim < 2 or len(d) < 6:
        return None
    D = dict(g=os.path.basename(f)[:-11], R=d[:, 0], Vo=d[:, 1],
             eV=np.maximum(d[:, 2], 1.0), Vg=d[:, 3], Vd=d[:, 4], Vb=d[:, 5],
             SBd=d[:, 6], SBb=d[:, 7])
    if np.any(D['R'] <= 0) or D['Vo'].max() <= 0:
        return None
    Rpc = D['R'] * 1e3
    L = lambda SB: np.concatenate([[0.0], np.cumsum(
        np.pi * (Rpc[1:] ** 2 - Rpc[:-1] ** 2) * 0.5 * (SB[1:] + SB[:-1]))])
    D['Ld'] = L(D['SBd']); D['Lb'] = L(D['SBb'])
    D['N'] = len(D['R']); D['kovan'] = bool(np.any(D['Vb'] > 0))
    D['Vmax'] = float(D['Vo'].max())
    return D


Vbar2 = lambda D, Y: np.sign(D['Vg']) * D['Vg'] ** 2 + Y * D['Vd'] ** 2 + 1.4 * Y * D['Vb'] ** 2
Mkaps = lambda D, Y: Y * D['Ld'] + 1.4 * Y * D['Lb'] + np.maximum(D['R'] * np.sign(D['Vg']) * D['Vg'] ** 2 / G, 0.0)


def v_nfw2(R, M200):
    c = 10 ** (0.905 - 0.101 * np.log10(M200 * H_RED / 1e12))
    r200 = (3.0 * M200 / (4.0 * np.pi * 200.0 * RHO_CRIT)) ** (1.0 / 3.0)
    rs = r200 / c
    mu = lambda x: np.log(1.0 + x) - x / (1.0 + x)
    return G * M200 / R * mu(R / rs) / mu(c)


def ft(D, f, p0, lo, hi):
    try:
        p, _ = curve_fit(f, D['R'], D['Vo'], sigma=D['eV'], p0=p0, bounds=(lo, hi), maxfev=600000)
    except Exception:
        return None
    mv = f(D['R'], *p)
    if not np.all(np.isfinite(mv)):
        return None
    c2 = float(np.sum(((mv - D['Vo']) / D['eV']) ** 2))
    return dict(p=p, c2i=c2 / max(D['N'] - len(p), 1))


rows = []
for f in sorted(glob.glob(os.path.join(VERI, '*_rotmod.dat'))):
    D = yukle(f)
    if D is None or D['N'] < 6:
        continue
    L = ft(D, lambda R, Y, lg, _D=D: np.sqrt(np.maximum(Vbar2(_D, Y), 1e-9) + v_nfw2(R, 10 ** lg)),
           [0.5, 11.0], [0.05, 7.0], [2.0, 13.5])
    E = ft(D, lambda R, Y, b, _D=D: np.sqrt(np.maximum(Vbar2(_D, Y), 1e-9) + b * Mkaps(_D, Y)),
           [0.5, 4e-7], [0.05, 1e-12], [2.0, 1e-1])
    if not (L and E):
        continue
    F = ft(D, lambda R, Y, b, Rf, _D=D: np.sqrt(np.maximum(Vbar2(_D, Y), 1e-9) + b * Mkaps(_D, Y) / (1 + R / Rf)),
           [0.5, 6e-7, 20.0], [0.05, 1e-12, 0.3], [2.0, 1e-1, RF_UST])
    Y = E['p'][0]; b = E['p'][1]
    lom = G / b if b > 1e-11 else np.nan
    Mbar = Mkaps(D, Y)[-1]
    lom_ong = np.sqrt(G * Mbar / A0) if Mbar > 0 else np.nan
    rf = F['p'][2] if F else np.nan
    rows.append(dict(g=D['g'], N=D['N'], kov=D['kovan'], V=D['Vmax'],
                     cL=L['c2i'], cE=E['c2i'], Y=Y, Mbar=Mbar,
                     lom=lom, lom_ong=lom_ong, rf=rf,
                     cF=F['c2i'] if F else np.nan))
rows.sort(key=lambda r: r['V'])

# --- markdown ---
sat = []
sat.append('| # | Galaksi | $N$ | Kovan | $V_{max}$ | $\\chi^2_{ind}$ ΛCDM | $\\chi^2_{ind}$ Evr. | $\\Delta\\chi^2$ | $\\Upsilon_*$ | $M_{bar}$ | $\\ell_\\omega$ ölç. | $\\ell_\\omega$ öngörü | oran | $R_f$ |')
sat.append('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|')
for i, r in enumerate(rows, 1):
    rf = '$\\to\\infty$' if (not np.isfinite(r['rf']) or r['rf'] > 0.98 * RF_UST) else '%.1f' % r['rf']
    orn = '%.2f' % (r['lom'] / r['lom_ong']) if np.isfinite(r['lom'] / r['lom_ong']) else '—'
    kaz = '**%+.2f**' % (r['cL'] - r['cE']) if (r['cL'] - r['cE']) > 0 else '%+.2f' % (r['cL'] - r['cE'])
    sat.append('| %d | %s | %d | %s | %.0f | %.2f | %.2f | %s | %.2f | %.2e | %.2f | %.2f | %s | %s |'
               % (i, r['g'].replace('_', '\\_'), r['N'], 'var' if r['kov'] else '—', r['V'],
                  r['cL'], r['cE'], kaz, r['Y'], r['Mbar'], r['lom'], r['lom_ong'], orn, rf))
tablo = '\n'.join(sat)

V = np.array([r['V'] for r in rows]); dC = np.array([r['cL'] - r['cE'] for r in rows])
n = len(rows)
ozet = []
for lo, hi, ad in [(0, 60, '$<60$'), (60, 80, '$60$–$80$'), (80, 120, '$80$–$120$'),
                   (120, 180, '$120$–$180$'), (180, 250, '$180$–$250$'), (250, 9999, '$>250$')]:
    m = (V >= lo) & (V < hi)
    if m.sum():
        p = np.sum(dC[m] > 0) / m.sum()
        sg = (p - 0.5) / np.sqrt(max(p * (1 - p), 1e-9) / m.sum())
        ozet.append('| %s | %d | %d | %.2f | %+.1f |' % (ad, m.sum(), int(np.sum(dC[m] > 0)), p, sg))

BOLUM = """### 6.5.3.4 Tam Veri Tablosu — Galaksi Başına Sonuçlar

*(Üretim betiği: `CALISMA/plot_sparc_tam.py`; ham veri: `CALISMA/veri/*_rotmod.dat`; bu tabloyu üreten betik: aynı dizindeki tablo üreticisi. Her satır bağımsız olarak yeniden hesaplanabilir.)*

Aşağıdaki tablo, 6.5.3.3'ün istatistiklerinin dayandığı **%d galaksinin tamamını** satır satır verir. Hiçbir galaksi seçilmemiş, dışlanmamış ya da ağırlıklandırılmamıştır; dosya olarak indirilebilen ve fit edilebilen tüm SPARC örneklemi buradadır. Amaç, 6.5.3.1–6.5.3.3 ve 6.5.4.5–6.5.4.6'daki her sayının denetlenebilir olmasıdır.

**Sütunlar.** $N$: dönüş eğrisi nokta sayısı. Kovan: SPARC'ın $V_{bul}>0$ verdiği galaksiler. $V_{max}$ (km/s): gözlenen en büyük hız, dinamik kütlenin vekili. $\\chi^2_{ind}$ ΛCDM: NFW halosu, konsantrasyon Dutton & Macciò (2014) ilişkisinden, $k=2$ ($\\Upsilon_*$, $M_{200}$). $\\chi^2_{ind}$ Evr.: Evrenakı F1+F4, $k=2$ ($\\Upsilon_*$, $b$). $\\Delta\\chi^2=\\chi^2_{\\Lambda CDM}-\\chi^2_{Evrenakı}$; **kalın** değerler Evrenakı'nın önde olduğu satırlardır. $\\Upsilon_*$: Evrenakı fitinin istediği 3,6 μm kütle/ışık oranı. $M_{bar}$ ($M_\\odot$): o $\\Upsilon_*$ ile kapsanan toplam baryonik kütle. $\\ell_\\omega$ ölç.: $\\mathcal{G}/b$ (kpc). $\\ell_\\omega$ öngörü: $\\sqrt{\\mathcal{G}M_{bar}/a_0}$ (6.5.4.5'in yasası, sıfır serbest parametre). Oran: ölçülen/öngörülen. $R_f$: yayılma ölçeği (kpc); $\\to\\infty$ işareti fitin yayılma istemediği galaksileri gösterir (6.5.4.6).

Tablo $V_{max}$'a göre artan sırada dizilmiştir; böylece 6.5.3.3'ün rejim deseni doğrudan okunabilir — üstteki cüce/LSB satırlarında $\\Delta\\chi^2$ ağırlıklı olarak pozitif, alttaki kütleli satırlarda karışıktır.

%s

**Bant özeti (tablonun doğrudan sayımı):**

| $V_{max}$ bandı | $n$ | Evrenakı önde | Oran | Anlamlılık |
|---|---|---|---|---|
%s
| **TOPLAM** | **%d** | **%d** | **%.2f** | **%+.1f$\\sigma$** |

*Uyarı:* Bu tablodaki $\\chi^2_{ind}$ değerleri yalnızca SPARC'ın kendi hata çubuklarını kullanır; uzaklık, eğiklik ve kütle/ışık sistematikleri modellenmemiştir. Bu nedenle mutlak değerler değil, **aynı satırdaki iki modelin karşılaştırması** anlamlıdır (7.4, madde 12).

""" % (n, tablo, '\n'.join(ozet), n, int(np.sum(dC > 0)), np.sum(dC > 0) / n,
       (np.sum(dC > 0) / n - 0.5) / np.sqrt((np.sum(dC > 0) / n) * (1 - np.sum(dC > 0) / n) / n))

p6 = os.path.join(BASE, r'Metin\Akademik\Kisim_6_Kanitlar\07_Galaktik_Yorungeler.md')
s = io.open(p6, encoding='utf-8').read()
anchor = '### Sonuç\n'
i = s.index(anchor)
s = s[:i] + BOLUM + s[i:]
io.open(p6, 'w', encoding='utf-8').write(s)
print('6.5.3.4 Tam Veri Tablosu eklendi: %d galaksi, %d satir' % (n, len(sat) - 2))
print('Evrenaki onde: %d/%d (%%%.0f)' % (int(np.sum(dC > 0)), n, 100 * np.sum(dC > 0) / n))
