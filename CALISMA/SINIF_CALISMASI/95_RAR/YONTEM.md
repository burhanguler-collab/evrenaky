# 95_RAR — Yöntem

Üreten betik: `../../rar_sinavi.py` · Sonuçlar: [`CALISMA.md`](CALISMA.md)

## 1. Veri

`veri/_RAR.mrt` — Lelli, McGaugh, Schombert & Pawlowski 2016 (ApJ 836, 152), Şekil 2'nin
arkasındaki veri. Dört sütun: `gbar e_gbar gobs e_gobs`, hepsi $\log_{10}$ m/s².

| | |
|---|---|
| Ham satır | 2706 |
| Geçerli nokta | **2693** |
| $\log g_{bar}$ aralığı | $-12{,}08$ … $-8{,}18$ (**3,9 decade**) |

Süzgeç: dört belirteç olmayan satırlar (başlık) ve $-14 < \log g < -7$ dışına düşen değerler
atılır. Bu, yalnız başlık satırlarını eler; **hiçbir veri noktası atılmadı** (2706 − 13 başlık
satırı = 2693).

**Bu dosyada olmayanlar:** galaksi kimliği, kütle, yarıçap, morfoloji. Bu yüzden
(a) ΛCDM zinciri kurulamaz, (b) galaksi başına kümeleme yapılamaz (bkz. CALISMA.md md. 7.1).

## 2. Teorinin öngörüsü

$$g_{öng} = g_{bar} + \sqrt{g_{bar}\,a_0}$$

Türetimi [96_ETG/YONTEM.md](../96_ETG/YONTEM.md) md. 2'dedir ($R$ sadeleşir).
$a_0 = cH_0/16{,}1 = 4{,}224\times10^{-11}$ m/s², **[S] kalibre**, bu sınavda oynatılmadı.
Sabitler `btfr_sinavi.py` ve `etg_sinavi.py` ile birebir aynıdır.

$g_{bar}$ **ölçülen** büyüklüktür → $\Upsilon_*$ öngörüye girmez, fitlenecek hiçbir şey yoktur.

## 3. Kıyas eğrisi — ampirik uyum

$$g_{obs} = \frac{g_{bar}}{1-e^{-\sqrt{g_{bar}/g_\dagger}}}, \qquad
g_\dagger = 1{,}20\times10^{-10}\ \text{m/s}^2$$

Lelli+2017'nin kendi uyum fonksiyonu. $g_\dagger$ **bu veriye fitlenmiştir** — teorinin
hiçbir parametresi fitlenmemiştir. Karşılaştırma bu yüzden **teorinin aleyhinedir** ve grafikte,
tabloda, metinde öyle işaretlenmiştir. Kaldırılmadı çünkü "biçim doğru mu" sorusu ancak düz
artıklı bir referansla yanıtlanabilir.

$g_\dagger/a_0 = 2{,}84$ — bu oran CALISMA.md md. 3'te kullanılır.

## 4. Kuşaklı çözümleme

Kuşak genişliği **0,25 dex**, kenarlar $-12{,}50$ … $-8{,}00$. En az 15 nokta içeren kuşaklar
raporlanır (14 kuşak kaldı). Her kuşakta:

- medyan artık $\log(g_{öng}/g_{gözl})$
- standart sapma
- gereken $a_0$ çarpanı — **sayısal çözülür** (ikiye bölme, 200 iterasyon, $k\in[10^{-4},10^4]$)
- F4 payı: $\sqrt{a_0 g_{bar}}/g_{öng}$

### Okunabilirlik eşiği

$$\frac{\partial \log g_{öng}}{\partial \log k} = \frac{1}{2}\cdot\frac{F4}{g_{bar}+F4}$$

F4 payı $< 0{,}25$ olan kuşakların çarpanı **kötü koşullanmıştır** ve tabloya "okunmaz" olarak
girer. Eşik [96_ETG](../96_ETG/CALISMA.md) md. 3'ten alındı, burada değiştirilmedi.
Elenen kuşaklar CSV'de `carpan_okunabilir = HAYIR` ile durur — **silinmez.**

### Biçim ölçütü

Okunabilir kuşakların medyan artıkları, kuşak merkezine karşı doğrusal fitlenir:
$d(\text{artık})/d(\log g_{bar})$. **Sıfır = biçim doğru.** Aynı ölçüt ampirik uyum için de
hesaplanır (referans düzlüğü).

## 5. Düşük ivme asimptot eğimi

$\log g_{obs}$ üzerinde $\log g_{bar}$'a doğrusal regresyon, üç ayrı eşikle
($-10{,}5$ / $-11{,}0$ / $-11{,}5$). **Tek bir eşik seçilip hüküm verilmez** — üçü de basılır
ve duyarlılık ekrana yazılır. Gerekçe CALISMA.md md. 5.

## 6. Saçılma bütçesi

Artık $= \log g_{öng} - \log g_{obs}$. İki hata kaynağı vardır ve $g_{bar}$'ınki öngörüye
zincir kuralıyla taşınır:

$$\frac{\partial \log g_{öng}}{\partial \log g_{bar}}
= \left(1+\tfrac{1}{2}\sqrt{a_0/g_{bar}}\right)\frac{g_{bar}}{g_{öng}}$$

$$\sigma_{bek} = \sqrt{e(\log g_{obs})^2 + \left(\tfrac{\partial \log g_{öng}}{\partial \log g_{bar}}\right)^2 e(\log g_{bar})^2}$$

İç saçılma $=\sqrt{\sigma_{göz}^2-\sigma_{bek}^2}$ (negatifse 0 yazılır).

**Varsayımlar:** hatalar bağımsız ve Gauss. İkisi de kesin doğru değildir — mesafe hatası
$g_{bar}$ ve $g_{obs}$'a **birlikte** girer, yani gerçek bütçe biraz farklıdır. İç saçılma bu
yüzden bir **üst sınır** sayılmalıdır.

## 7. İstatistik

- Merkezî eğilim: **medyan** (aykırı değere dayanıklı). Ortalama hiç kullanılmadı.
- Yayılım: standart sapma (dex).
- Gereken $a_0$: **kapalı formül yok**, ikiye bölmeyle çözülür. Naif $10^{-4\Delta}$ formülü
  yalnız saf-F4 asimptotunda geçerlidir (97_BTFR'nin düzeltme kaydı).
- **Hata çubuğu / güven aralığı verilmedi.** Noktalar bağımsız olmadığı için (md. 1) hesaplanan
  herhangi bir standart hata yanıltıcı olurdu. Bu bilinçli bir eksikliktir.

## 8. Çıktı — `SONUC.csv`

Kuşak başına bir satır (14 satır):

| Sütun | Anlamı |
|---|---|
| `kusak_alt_log_gbar`, `kusak_ust` | kuşak sınırları |
| `n` | kuşaktaki nokta sayısı |
| `F4_payi` | medyan F4 katkısı — okunabilirliği belirler |
| `TEORI_artik_medyan_dex`, `TEORI_sacilma_dex` | teorinin artığı |
| `TEORI_gereken_a0_carpani` | sayısal çözüm |
| `carpan_okunabilir` | `evet` / `HAYIR` — eşik kararı |
| `AMPIRIK_artik_medyan_dex` | fitli referansın artığı |

## 9. Tekrarlanabilirlik

```bash
python rar_sinavi.py
```

`SINIF_CALISMASI/95_RAR/` altına `SONUC.csv` ve `rar.png` yazar. Bağımlılık: `numpy`,
`matplotlib`. Rastgelelik yok, fit yok; iterasyon yalnız çarpan çözümündedir (deterministik).
