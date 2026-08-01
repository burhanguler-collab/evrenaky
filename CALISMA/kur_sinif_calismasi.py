"""SINIF CALISMASI KLASOR YAPISINI KURAR.

Ilke. Her galaksi morfolojik sinifina gore ayri klasore konur. Her klasorde:
  veri/        : olculen donus egrisi dosyalari (SPARC Rotmod_LTG, degistirilmemis)
  KATALOG.csv  : o sinifin galaksileri icin YAYINLANMIS katalog buyuklukleri
  OKUBENI.md   : sinif tanimi, sayilar, her sutunun kaynagi ve nasil olculdugu

Onemli kural: KATALOG.csv'deki hicbir sayi BU CALISMADA hesaplanmamistir. Hepsi
Lelli, McGaugh & Schombert (2016) Tablo 1'den birebir alinmistir ve o tablonun
kendi olcum yontemi yayinda belgelidir. Bizim fit sonuclarimiz bu klasorlere
KONULMAZ; onlar ayri tutulur (bkz. _HESAPLAR/OKUBENI.md).

Siniflama (SPARC Hubble tipi T, ana katalog sutun 2):
  01_erken_spiral    Sa, Sab        T=1,2
  02_orta_spiral     Sb, Sbc        T=3,4
  03_gec_spiral      Sc, Scd        T=5,6
  04_cok_gec_spiral  Sd             T=7
  05_macellan        Sdm, Sm        T=8,9
  06_duzensiz        Im             T=10
  99_KARMASIK        ayrim yapilamayanlar

KARMASIK olcutu (herhangi biri saglanirsa):
  (a) donus egrisinde N<6 nokta            -> egri sinanamaz
  (b) SPARC kalite bayragi Q=3 (dusuk)     -> olcum guvenilir degil
  (c) egiklik i<30 derece (yuz-ustu)       -> donme hizi kotu belirlenmis
  (d) tipi kendi sinifinda N<5 kaliyor     -> istatistik tasimaz (S0, BCD)
Her karmasik galaksi icin GEREKCE.csv'ye hangi olcutten dustugu yazilir.
"""

import os
import shutil
import sys

import numpy as np

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

KOK = os.path.dirname(os.path.abspath(__file__))
VERI = os.path.join(KOK, 'veri')
CIK = os.path.join(KOK, 'SINIF_CALISMASI')

TIP = {0: 'S0', 1: 'Sa', 2: 'Sab', 3: 'Sb', 4: 'Sbc', 5: 'Sc',
       6: 'Scd', 7: 'Sd', 8: 'Sdm', 9: 'Sm', 10: 'Im', 11: 'BCD'}
UZAK = {1: 'Hubble akisi (H0=73, Virgo duzeltmeli)', 2: 'TRGB (kirmizi dev ucu)',
        3: 'Cepheid donem-parlaklik', 4: 'Ursa Major kumesi uyeligi', 5: 'Supernova isik egrisi'}
KAL = {1: 'yuksek', 2: 'orta', 3: 'dusuk'}

SINIF = [('01_erken_spiral', 'Sa – Sab', [1, 2]),
         ('02_orta_spiral', 'Sb – Sbc', [3, 4]),
         ('03_gec_spiral', 'Sc – Scd', [5, 6]),
         ('04_cok_gec_spiral', 'Sd', [7]),
         ('05_macellan', 'Sdm – Sm', [8, 9]),
         ('06_duzensiz', 'Im', [10])]
AYRIK = [0, 11]          # S0 ve BCD: kendi siniflarinda N<5 -> KARMASIK

# ---- ana katalogu oku (sabit genislik DEGIL: baslik bir bayt kaymis, belirtec kullan) ----
SUT = ['Galaksi', 'T', 'D_Mpc', 'eD_Mpc', 'fD', 'Inc_deg', 'eInc_deg', 'L36_1e9Lsun',
       'eL36_1e9Lsun', 'Reff_kpc', 'SBeff', 'Rdisk_kpc', 'SBdisk', 'MHI_1e9Msun',
       'RHI_kpc', 'Vflat_kms', 'eVflat_kms', 'Q', 'Kaynak']
ham = open(os.path.join(VERI, '_sparc.mrt'), encoding='utf-8', errors='replace').read().split('\n')
ayr = [i for i, x in enumerate(ham) if x.startswith('----')][-1]
KAT = {}
for L in ham[ayr + 1:]:
    p = L.split()
    if len(p) < 19:
        continue
    try:
        KAT[p[0]] = dict(zip(SUT, [p[0], int(p[1])] + [float(x) for x in p[2:4]] + [int(p[4])]
                             + [float(x) for x in p[5:17]] + [int(p[17]), p[18]]))
    except (ValueError, IndexError):
        continue
print('ana katalog: %d kayit' % len(KAT))

# ---- donus egrisi dosyalarini tara ----
G = {}
for f in sorted(os.listdir(VERI)):
    if not f.endswith('_rotmod.dat'):
        continue
    ad = f[:-11]
    try:
        d = np.loadtxt(os.path.join(VERI, f))
    except Exception:
        continue
    N = 0 if d.ndim < 2 else len(d)
    G[ad] = dict(dosya=f, N=N, kat=KAT.get(ad))
print('rotmod dosyasi: %d' % len(G))

# ---- siniflandir ----
atama, karmasik = {}, {}
for ad, g in G.items():
    k = g['kat']
    ger = []
    if k is None:
        ger.append('ana katalogda kaydi yok')
    if g['N'] < 6:
        ger.append('N=%d < 6 nokta (egri sinanamaz)' % g['N'])
    if k:
        if k['Q'] == 3:
            ger.append('SPARC kalite bayragi Q=3 (dusuk)')
        if k['Inc_deg'] < 30:
            ger.append('egiklik i=%.0f < 30 derece (yuz-ustu)' % k['Inc_deg'])
        if k['T'] in AYRIK:
            ger.append('tip %s: kendi sinifinda N<5, istatistik tasimaz' % TIP[k['T']])
    if ger:
        karmasik[ad] = ger
        continue
    for kls, _, ts in SINIF:
        if k['T'] in ts:
            atama.setdefault(kls, []).append(ad)
            break
    else:
        karmasik[ad] = ['tip T=%d hicbir sinifa girmiyor' % k['T']]

# ---- klasorleri yaz ----
def temizle(kok):
    """Icerigi siler ama KOK KLASORU SILMEZ — Windows'ta acik bir gezgin penceresi
    ust klasoru kilitleyebiliyor. Silinemeyen dosya varsa uyarir, durmaz."""
    if not os.path.isdir(kok):
        os.makedirs(kok)
        return
    kalan = []
    for ad in os.listdir(kok):
        y = os.path.join(kok, ad)
        try:
            shutil.rmtree(y) if os.path.isdir(y) else os.remove(y)
        except OSError as e:
            kalan.append('%s (%s)' % (ad, e.__class__.__name__))
    if kalan:
        print('  UYARI: silinemedi -> %s' % ', '.join(kalan))


temizle(CIK)
os.makedirs(CIK, exist_ok=True)


def _alan(v):
    """Virgul iceren alanlari (ornegin Kaynak='Tr09,dB01') tirnaklar."""
    s = str(v)
    return '"%s"' % s.replace('"', '""') if (',' in s or '"' in s) else s


def katalog_csv(yol, adlar):
    with open(yol, 'w', encoding='utf-8') as fh:
        fh.write(','.join(SUT + ['N_nokta']) + '\n')
        for ad in sorted(adlar):
            k = G[ad]['kat']
            if k is None:
                fh.write(ad + ',' * (len(SUT)) + str(G[ad]['N']) + '\n')
                continue
            fh.write(','.join(_alan(k[s]) for s in SUT) + ',%d\n' % G[ad]['N'])


def okubeni(yol, baslik, tanim, adlar, ek=''):
    n = len(adlar)
    ts = sorted({G[a]['kat']['T'] for a in adlar if G[a]['kat']}) if n else []
    Ns = [G[a]['N'] for a in adlar]
    with open(yol, 'w', encoding='utf-8') as fh:
        fh.write('# %s\n\n%s\n\n' % (baslik, tanim))
        fh.write('## Sayılar\n\n')
        fh.write('| | |\n|---|---|\n')
        fh.write('| Galaksi sayısı | **%d** |\n' % n)
        fh.write('| Toplam ölçüm noktası | %d |\n' % sum(Ns))
        fh.write('| Nokta / galaksi | %d – %d (medyan %d) |\n'
                 % (min(Ns), max(Ns), int(np.median(Ns))) if n else '')
        if ts:
            fh.write('| İçerdiği Hubble tipleri | %s |\n'
                     % ', '.join('%s (T=%d, n=%d)' % (TIP[t], t,
                       sum(1 for a in adlar if G[a]['kat'] and G[a]['kat']['T'] == t)) for t in ts))
        if n:
            kk = [G[a]['kat']['Q'] for a in adlar if G[a]['kat']]
            fh.write('| Kalite | %s |\n' % ' · '.join(
                'Q=%d %s: %d' % (q, KAL[q], kk.count(q)) for q in sorted(set(kk))))
            ii = np.array([G[a]['kat']['Inc_deg'] for a in adlar if G[a]['kat']])
            fh.write('| Eğiklik | %.0f° – %.0f° (medyan %.0f°) |\n' % (ii.min(), ii.max(), np.median(ii)))
        fh.write('\n' + ek)
        fh.write("""
## Bu klasördeki dosyalar

- `veri/*_rotmod.dat` — **ölçülen** dönüş eğrileri. SPARC `Rotmod_LTG` dosyaları, **değiştirilmemiş kopyalar.**
  Sütunlar: `Rad(kpc)  Vobs(km/s)  errV(km/s)  Vgas  Vdisk  Vbul  SBdisk  SBbul`
  `Vdisk` ve `Vbul`, $\\Upsilon_*=1$ için verilir; ölçekleme kullanıcıya bırakılmıştır.
- `KATALOG.csv` — bu sınıfın galaksileri için **yayınlanmış** katalog büyüklükleri.

## Kaynak ve provenans

Bütün sayılar **Lelli, McGaugh & Schombert (2016), AJ 152, 157**, Tablo 1'den birebir alınmıştır.
Bu çalışmada **hiçbiri yeniden hesaplanmamıştır.** Ölçüm yöntemleri o yayında belgelidir:

| Sütun | Ne | Nasıl ölçüldü |
|---|---|---|
| `T` | Hubble tipi | 0=S0, 1=Sa … 7=Sd, 8=Sdm, 9=Sm, 10=Im, 11=BCD |
| `D_Mpc`, `eD_Mpc`, `fD` | uzaklık ve yöntemi | 1=Hubble akışı · 2=TRGB · 3=Cepheid · 4=UMa üyeliği · 5=Süpernova |
| `Inc_deg`, `eInc_deg` | eğiklik | HI hız alanı ve/veya optik eksen oranından |
| `L36_1e9Lsun` | 3,6 μm toplam ışıma | *Spitzer* IRAC fotometrisi |
| `Reff_kpc`, `SBeff` | etkin yarıçap / yüzey parlaklığı | 3,6 μm profilinden |
| `Rdisk_kpc`, `SBdisk` | disk ölçek uzunluğu / merkezî yüzey parlaklığı | 3,6 μm diske eksponansiyel uydurma |
| `MHI_1e9Msun`, `RHI_kpc` | HI kütlesi / yarıçapı | 21 cm; $R_{HI}$ = 1 M☉/pc² konturu |
| `Vflat_kms`, `eVflat_kms` | asimptotik düz hız | dönüş eğrisinin dış düz kısmına uydurma |
| `Q` | kalite bayrağı | 1=yüksek, 2=orta, 3=düşük |
| `Kaynak` | HI/Hα verisinin kaynağı | yayın kısaltması (ana katalogun Not 4'ü) |
| `N_nokta` | eğri noktası sayısı | `veri/` dosyasının satır sayısı (tek türetilmiş alan) |

### Okuma uyarıları

- **`Vflat_kms = 0.0` "hız sıfır" demek değildir.** SPARC'ın kuralı: dönüş eğrisinde ölçülebilir
  bir düz (asimptotik) kısım yoksa alan sıfır bırakılır. Bu galaksilerde $V_{flat}$ **tanımsızdır**;
  sıfır olarak hesaba katılmamalıdır. Aynı şey `RHI_kpc = 0.0` için de geçerlidir.
- **`Vdisk`, `Vbul` sütunları $\\Upsilon_*=1$ içindir.** Gerçek katkı $\\sqrt{\\Upsilon_*}\\,V_{disk}$'tir.
- **`Kaynak` alanı virgül içerebilir** (birden çok yayın); CSV'de tırnaklanmıştır.
- Uzaklık hatası tüm eğriyi birlikte ölçekler, eğiklik hatası tüm hızları birlikte ölçekler —
  bunlar **korelasyonlu sistematiklerdir**, nokta başına bağımsız hata değil.

**Atıf zorunludur:** Lelli F., McGaugh S. S., Schombert J. M., 2016, AJ, 152, 157 (SPARC).
""")


TANIM_EK = """## Neden bu sınıf ayrı tutuluyor

Morfolojik tip, dönüş eğrisi biçimini belirleyen fiziksel özelliklerle (kovan oranı, yüzey
parlaklığı, gaz kesri, disk kalınlığı) güçlü biçimde ilişkilidir. Sınıfları karıştırmak, blok
ortalamasının içinde ters yönlü davranışları görünmez kılar. Bu nedenle her sınıf ayrı
çalışılır ve **sonuçlar sınıf sınıf raporlanır, blok ortalaması yalnız yanında verilir.**
"""

toplam = 0
for kls, tanim_tip, ts in SINIF:
    adlar = atama.get(kls, [])
    if not adlar:
        continue
    d = os.path.join(CIK, kls)
    os.makedirs(os.path.join(d, 'veri'))
    for ad in adlar:
        shutil.copy2(os.path.join(VERI, G[ad]['dosya']), os.path.join(d, 'veri', G[ad]['dosya']))
    katalog_csv(os.path.join(d, 'KATALOG.csv'), adlar)
    okubeni(os.path.join(d, 'OKUBENI.md'), 'Sınıf: %s' % tanim_tip,
            'SPARC Hubble tipi **T = %s**. Kalite ve eğiklik süzgeçlerini geçen galaksiler.'
            % ', '.join(str(t) for t in ts), adlar, TANIM_EK)
    toplam += len(adlar)
    print('  %-20s %3d galaksi' % (kls, len(adlar)))

# ---- KARMASIK ----
d = os.path.join(CIK, '99_KARMASIK')
os.makedirs(os.path.join(d, 'veri'))
for ad in karmasik:
    shutil.copy2(os.path.join(VERI, G[ad]['dosya']), os.path.join(d, 'veri', G[ad]['dosya']))
katalog_csv(os.path.join(d, 'KATALOG.csv'), list(karmasik))
with open(os.path.join(d, 'GEREKCE.csv'), 'w', encoding='utf-8') as fh:
    fh.write('Galaksi,Tip,N_nokta,Q,Inc_deg,Gerekce\n')
    for ad in sorted(karmasik):
        k = G[ad]['kat']
        fh.write('%s,%s,%d,%s,%s,"%s"\n' % (ad, TIP[k['T']] if k else '?', G[ad]['N'],
                 k['Q'] if k else '?', k['Inc_deg'] if k else '?', ' ; '.join(karmasik[ad])))
okubeni(os.path.join(d, 'OKUBENI.md'), 'KARMAŞIK — ayrım yapılamayanlar',
        'Bu galaksiler **sınıflandırılmadı.** Morfolojik tipleri bilinse bile, aşağıdaki '
        'ölçütlerden en az biri nedeniyle sınıf çalışmasına alınmamışlardır. Her galaksinin '
        'hangi ölçütten düştüğü `GEREKCE.csv`\'de yazılıdır.', list(karmasik),
        """## Karmaşık ilan etme ölçütleri

| Ölçüt | Neden |
|---|---|
| $N<6$ nokta | Eğri, iki parametreli bir modelle bile anlamlı sınanamaz |
| SPARC $Q=3$ (düşük kalite) | Ölçümün kendisi güvenilir değil |
| Eğiklik $i<30°$ | Yüz-üstü galakside dönme hızı $V_{obs}=V_{gerçek}\\sin i$ ile kötü belirlenir |
| Kendi tipinde $N<5$ | S0 ($n=3$) ve BCD ($n=4$): istatistik taşımaz |

**Bu klasör çöp kutusu değildir.** Buradaki galaksiler ileride kullanılabilir: kalite veya
eğiklik ölçütü gevşetilirse, ya da S0/BCD için bağımsız bir örneklem eklenirse. Ölçütler
`GEREKCE.csv`'de galaksi başına kayıtlı olduğu için geri alınabilir bir karardır.

**Uyarı:** karmaşık galaksileri sonradan sınıflara eklemek, seçim etkisi doğurur. Eklenirse
sonuç *hem* eklenmiş *hem* eklenmemiş hâliyle raporlanmalıdır.
""")
print('  %-20s %3d galaksi' % ('99_KARMASIK', len(karmasik)))
print('toplam: %d siniflandirilmis + %d karmasik = %d' % (toplam, len(karmasik), toplam + len(karmasik)))

# ---- kok OKUBENI + siniflama tablosu ----
with open(os.path.join(CIK, '00_SINIFLAMA.csv'), 'w', encoding='utf-8') as fh:
    fh.write('Galaksi,Tip_T,Tip_ad,Sinif,N_nokta,Q,Inc_deg,D_Mpc,Vflat_kms\n')
    for kls, _, _ in SINIF:
        for ad in sorted(atama.get(kls, [])):
            k = G[ad]['kat']
            fh.write('%s,%d,%s,%s,%d,%d,%.1f,%.2f,%.1f\n'
                     % (ad, k['T'], TIP[k['T']], kls, G[ad]['N'], k['Q'],
                        k['Inc_deg'], k['D_Mpc'], k['Vflat_kms']))
    for ad in sorted(karmasik):
        k = G[ad]['kat']
        fh.write('%s,%s,%s,99_KARMASIK,%d,%s,%s,%s,%s\n'
                 % (ad, k['T'] if k else '', TIP[k['T']] if k else '?', G[ad]['N'],
                    k['Q'] if k else '', k['Inc_deg'] if k else '',
                    k['D_Mpc'] if k else '', k['Vflat_kms'] if k else ''))

sat = []
for kls, tad, ts in SINIF:
    a = atama.get(kls, [])
    if a:
        sat.append('| `%s` | %s | T=%s | **%d** | %d |' % (kls, tad, ','.join(map(str, ts)),
                   len(a), sum(G[x]['N'] for x in a)))
sat.append('| `99_KARMASIK` | ayrım yapılamayanlar | — | **%d** | %d |'
           % (len(karmasik), sum(G[x]['N'] for x in karmasik)))

with open(os.path.join(CIK, '00_OKUBENI.md'), 'w', encoding='utf-8') as fh:
    fh.write(("""# Sınıf Çalışması — kuruluş ve kurallar

Bu klasör, galaktik dönüş eğrisi çalışmasını **morfolojik sınıf sınıf** yürütmek için kurulmuştur.
Yapıyı üreten betik: `kur_sinif_calismasi.py` (bu klasörün bir üstünde). Betik yeniden koşulduğunda
yapı sıfırdan kurulur, yani **kuruluş tekrarlanabilirdir.**

## Neden sınıf sınıf

Örneklem bloğu hâlinde bakıldığında ters yönlü davranışlar birbirini götürüyor. Ölçüldü: aynı
büyüklük (fitlenen $\\Upsilon_*$'ın fotometrik bandın dışında kalma oranı) spiral sınıfında %44,
Macellan sınıfında %91 çıkıyor. Blok ortalaması ikisini de gizler. Bu nedenle **hiçbir sonuç blok
hâlinde verilmez;** sınıf sınıf verilir, blok ortalaması yalnız yanında özet olarak durur.

## Sınıflar

| Klasör | Tip | SPARC T | Galaksi | Ölçüm noktası |
|---|---|---|---|---|
@@TABLO@@

## Ölçütler

Bir galaksi, aşağıdakilerden **en az biri** geçerliyse `99_KARMASIK`'a konur:

1. Dönüş eğrisinde $N<6$ nokta
2. SPARC kalite bayrağı $Q=3$ (düşük)
3. Eğiklik $i<30°$ (yüz-üstü — $V_{obs}=V\\sin i$ kötü belirlenir)
4. Kendi Hubble tipi sınıfında $N<5$ galaksi kalıyor (S0, BCD)

Her karmaşık galaksinin hangi ölçütten düştüğü `99_KARMASIK/GEREKCE.csv`'de yazılıdır.

## Veri türü ayrımı — bu klasörün en önemli kuralı

| Klasörde ne VAR | Klasörde ne YOK |
|---|---|
| **Ölçülen** dönüş eğrileri (SPARC Rotmod_LTG, değiştirilmemiş) | Bu çalışmanın fit sonuçları |
| **Yayınlanmış** katalog büyüklükleri (Lelli+2016 Tablo 1) | Türetilmiş model parametreleri ($\\Upsilon_*$, $M_{200}$, $b$, $R_f$ …) |
| Her sütunun nasıl ölçüldüğü (`OKUBENI.md`) | $\\chi^2$, AIC, BIC gibi uyum ölçütleri |

**Gerekçe:** sınıf klasörleri **girdi** klasörleridir. Buradaki her sayının kaynağı bir yayındır ve
ölçüm yöntemi o yayında belgelidir. Bizim hesapladığımız hiçbir şey buraya karışmaz — karışırsa
girdi ile çıktı ayrımı kaybolur ve sonuçlar denetlenemez hâle gelir.

Bu çalışmanın kendi hesapları `_HESAPLAR/` altında, her biri kendi klasöründe ve üreten betiğin
adıyla birlikte tutulur.

## Tek dosyada tüm sınıflama

`00_SINIFLAMA.csv` — 163 galaksinin tamamı, hangi sınıfa girdiği ve neden. Sütunlar:
`Galaksi, Tip_T, Tip_ad, Sinif, N_nokta, Q, Inc_deg, D_Mpc, Vflat_kms`

## Kaynak

Lelli F., McGaugh S. S., Schombert J. M., 2016, **AJ 152, 157** — *SPARC: Mass Models for 175 Disk
Galaxies with Spitzer Photometry and Accurate Rotation Curves.* Ana katalog: `veri/_sparc.mrt`.
Dönüş eğrileri: `Rotmod_LTG`.
""").replace('@@TABLO@@', '\n'.join(sat)))

# ---- _HESAPLAR iskeleti ----
h = os.path.join(CIK, '_HESAPLAR')
os.makedirs(h)
with open(os.path.join(h, 'OKUBENI.md'), 'w', encoding='utf-8') as fh:
    fh.write("""# Hesaplar — bu çalışmanın kendi çıktıları

Sınıf klasörleri **girdi**dir: yalnız ölçülen eğriler ve yayınlanmış katalog büyüklükleri.
Bu klasör **çıktı**dır: bu çalışmada hesaplanan her şey.

## Kural

Her hesap kendi alt klasörüne konur ve şu üçü birlikte bulunur:

1. `SONUC.csv` — galaksi başına sayısal çıktı
2. `YONTEM.md` — hangi denklem, hangi parametreler serbest, hangi sınırlar, hangi ölçüt
3. `betik` — üreten betiğin adı ve sürüm tarihi

Bir hesap bu üçü olmadan buraya girmez. Gerekçe: bu çalışmanın bütün geçmişinde en pahalı
hatalar, bir sayının nasıl üretildiğinin kaydının tutulmamasından çıktı.

## Dışarıdan alınan ilişkiler — ve statüleri

Aşağıdaki büyüklükler bu çalışmada hesaplanmamış, literatürden alınmıştır. Kullanıldıkları her
yerde atıf zorunludur:

| İlişki | Kaynak | Ne veriyor | Statü |
|---|---|---|---|
| NFW yoğunluk profili | Navarro, Frenk & White 1996 | halo profil biçimi | N-cisim çıktısına **uydurulmuş formül** (analitik türetim değil) |
| $c_{200}$–$M_{200}$ | Dutton & Macciò 2014 | konsantrasyon–kütle, 0,11 dex saçılma | N-cisim simülasyonlarına **fitlenmiş** iki katsayı |
| Abundance matching | Moster ve ark. 2013 | $M_* \\leftrightarrow M_{halo}$ | gözlemsel kütle fonksiyonuna **fitlenmiş** |
| Popülasyon sentezi $\\Upsilon_*$ | 3,6 μm literatürü | $\\Upsilon_*\\approx0{,}3$–$0{,}8$ | IMF varsayımına bağlı **bant**, tek sayı değil |

**Uyarı:** bu dördü de "türetilmiş" değil, "kalibre edilmiş"tir. Karşılaştırmalarda bu böyle
sunulmalıdır.
""")
print("\n'SINIF_CALISMASI/' kuruldu.")
