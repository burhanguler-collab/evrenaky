# dSph sınavı — M-48+a₀ örneklem-dışı GEÇTİ; M-49 büyük uydularda ilk işaret (iş 13)

**Veri:** McConnachie 2012 (AJ 144, 4; VizieR `J/AJ/144/4`, CfA aynası) —
`veri/_mcconnachie2012.tsv`, değiştirilmemiş. **SPARC'tan tamamen bağımsız ilk veri ailesi.**
Hesap: `../../dsph_sinavi.py` (okuma kuralları betik başlığında, veriye bakılmadan yazıldı).
Çıktı: [`SONUC_DSPH.csv`](SONUC_DSPH.csv).

Örnek: σ* ölçülü 43 cüce (Sgr hariç — bilinen gelgit bozulması, önceden dışlandı); ana örnek
$M_*\geq10^5\,M_\odot$: **28 sistem** (9 MW + 14 M31 uydusu + 5 izole). Öngörü: M-48 köprüsü
($\alpha=2$, $r_h$'ta) ± M-49 EFE terimi; $a_0$ ve bütün sabitler **SPARC değerlerinde
dondurulmuş — sıfır yeniden-kalibrasyon.**

## 1. BÜYÜK SONUÇ — köprü + $a_0$, bağımsız ailede bire oturdu

$$\text{TÜM ANA (28 sistem): medyan }\log(\sigma_{öng}/\sigma_{ölç})=+0{,}009\ \text{dex},\quad
\text{saçılma }0{,}172\ \text{dex}$$

Gruplar (EFE'siz): MW $-0{,}051$ · M31 $+0{,}018$ · izole $-0{,}047$. Bu, kitabın bağımsızlık
arenasındaki tek eksiğinin ("$a_0$ sınandığı veriden okundu"; 6.5.3.6 karnesi) **ilk fiilî
kapanış adımıdır**: $a_0$ + M-47 penceresi + M-48 köprüsü, Yerel Grup'un basınç-destekli
cücelerinde, hiçbir şey ayarlanmadan, medyanda %2 isabetle çalıştı. (Konvansiyon bandı:
$\Upsilon_V=1$ — kataloğun kendi kuralı; $\times2$ duyarlılığı medyanı $+0{,}094$'e taşır —
$O(1)$ konvansiyonlar hükmü değiştirmez.)

## 2. M-49 (EFE) — kütle-bağımlı iki yüz

| Altküme | n | EFE'siz | EFE'li | Okuma |
|---|---|---|---|---|
| $M_*>10^6$ (büyük uydular) | 14 | $+0{,}109$ (fazla) | **$+0{,}042$** | **imza VAR: öngörülen yönde ve mertebede düzeltme** (And II: öngörü 7,3 = ölçüm 7,3; Fornax 17,0→15,1, ölçüm 11,7; And VII 13,5→10,4, ölçüm 9,7) |
| $M_*<10^6$ (küçük klasikler) | 14 | $-0{,}089$ (zaten eksik) | $-0{,}430$ | **aşırı bastırma** — ama bu altküme gelgit-karıştırıcılıdır (aşağıda) |

**Küçük-klasik ucunun dürüst okuması:** Draco, UMi, Carina, Sextans, CVn ve soluk And uyduları
EFE'siz kurulumda bile eksik-öngörülüdür (standart resimde de "en karanlık-madde-baskın"
denilen, MOND'un da en zorlandığı sistemler). En derin dış alandakiler aynı zamanda **gelgit
ısınmasının en güçlü olduğu** sistemlerdir; gelgit σ'yu şişirir — tam EFE'nin bastırdığı yerde.
İki etki bu veriyle ayrıştırılamaz: bu uçta **hüküm verilmez** (gelgit modeli türetilmeden).
G-13'ün korelasyon imzası da bu yüzden bulanık: EFE'siz artık $\sim\log g_{ext}$ Spearman
$-0{,}11\approx0$, EFE'li $-0{,}31$.

## 3. Hüküm

1. **M-48 [T-aday] ilk bağımsız-veri sınavını GEÇTİ** (28 sistem, medyan $+0{,}009$).
   [T]'ye tam geçiş için ikinci aile (eliptik dış-$\sigma$, G-12) beklenir.
2. **M-49 [T-aday] kalır — iki kayıtla:** büyük-uydu rejiminde **ilk lehte işaret**
   (+0,109→+0,042, tam öngörülen düzeltme); küçük-klasik rejimde aleyhte görünüm
   **gelgit karıştırıcısıyla çakışık** — ayrıştırma, gelgit-ısınması hesabını ya da
   gelgit-korunaklı bir örneklemi (uzak/dairesel yörüngeli uydular) bekler.
3. İzole beklenen-üstü iki sistem (Cetus 17,0'a karşı 9,5; Tucana 15,8'e karşı 6,5)
   literatürde σ'ları tartışmalı sistemlerdir (küçük örneklem, çiftlik şişmesi); kayda geçirildi,
   hükme sokulmadı.

## 4. Dürüstlük kayıtları

1. Bu bir **mertebe/işaret sınavıdır**: $\alpha=2$, izotropi, $r_h$'ta tam-$M$ konvansiyonu,
   $\Upsilon_V=1$ — hepsi $O(1)$ serbestliği taşır ve **hiçbiri sonuca göre seçilmedi**
   (kurallar betik başlığında, koşumdan önce).
2. $g_{ext}$ düz $V^2/D$ ile alındı (MW 220, M31 230); uydu yörünge fazı bilinmiyor —
   anlık $D$ kullanıldı.
3. Ana-örnek eşiği ($M_*\geq10^5$) önceden kondu; ultra-soluklar rapor dışıdır (CSV'de
   işaretli dururlar).
4. Sgr önceden dışlandı; başka dışlama yapılmadı.
5. Bu sınav Claude Fable 5 tarafından koşulmuştur; McConnachie derlemesi değiştirilmeden
   kullanılmıştır.
