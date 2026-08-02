# Geniş çift yıldızlar — düzgün-alan artığının hesabı (G-10'un hesabı; iş 3)

**Soru:** Galaktik diskte yüzen bir geniş çift yıldızın (ayrıklık $s\sim10^3$–$2\times10^4$ AU)
**iç** dinamiği teoride Newton'dan ne kadar sapar? MOND'un bazı sürümleri burada ölçülebilir artış
öngörür ve literatür çekişmelidir (Chae, 2023: $g$'de $\approx\times1{,}4$ artış iddiası ↔ Banik
ve ark., 2024: Newton lehine güçlü sınır). Teorinin kendi cevabı hesapsız bir beklentiydi
(`CALISMA.md` md. 6.5); bu dosya hesabı yapar.

---

## 1. Kurulum ve ölçekler

Girdiler: $\mathcal{G}$'nin yerel ölçülen değeri $6{,}674\times10^{-11}$, $a_0=7{,}39\times10^{-11}$ m/s²
[S], çift kütlesi $M=2M_\odot$, Güneş çevresi $R_0=8$ kpc, $V=233$ km/s.

| $s$ (AU) | $g_{iç}=\mathcal{G}M/s^2$ | $g_{iç}/a_0$ |
|---|---|---|
| 3 000 | $1{,}3\times10^{-9}$ | 17,8 |
| 10 000 | $1{,}19\times10^{-10}$ | 1,6 |
| 20 000 | $3{,}0\times10^{-11}$ | 0,40 |

Geniş çiftler $a_0$ rejimini gerçekten yoklar — ve kritik ölçek örtüşmesi şudur: çiftin kendi
kütlesiyle kurulan vortisite uzunluğu $\ell_\omega(2M_\odot)=\sqrt{\mathcal{G}M/a_0}=1{,}27\times10^4$ AU,
tam geniş-çift ayrıklıkları bandındadır. **Yani nihai denklem çifte *körlemesine* uygulansaydı**
($a_{F4}^{öz}=\sqrt{g_{iç}\,a_0}$) MOND ölçüsünde artış çıkardı:

| $s$ (AU) | karşı-olgusal $a_{F4}^{öz}/g_{iç}$ |
|---|---|
| 3 000 | 0,24 |
| 10 000 | 0,79 |
| 20 000 | 1,58 |

Soru bu yüzden keskindir: teorinin F4 kanalı çifte uygulanır mı, uygulanmaz mı?

## 2. Kaynak denetimi — çiftin öz-F4 kanalı taşıyıcısızdır

F4'ün türetim zincirinin **her halkası koherent disk yapısına bağlıdır**; hiçbir halkası iki
noktasal cisme genellenmiş değildir:

1. **Genlik (6.5.4.3):** F4, *kapsanan baryonik kütlenin dolanım debisinden* beslenir — kaynak,
   diskin vortisitesidir; iki yıldızın yörünge açısal momentumu değil.
2. **Geometri (M-38, Varsayım 3):** $1/R$ yasası silindirik akıdan ($2\pi Rh$, $h=$ sabit disk)
   çıkar ve yalnız $r_0<R<R_{kesim}$ penceresinde geçerlidir. Çiftte disk yoktur; akı yüzeyi
   kurulamaz.
3. **Toplanma (Adım 6, $\sqrt{N}$):** $\ell_\omega^{etkin}=\ell_\omega^{mikro}\sqrt{N}$ köprüsü,
   dolanım korunumunu taşıyan **koherent taşıyıcı yapıda** kurulur; taşıyıcının kaskad karakteri
   ince/soğuk disklerde korunur, izotropik/seyrek yapılarda sönümlenir (85_TUTARLILIK_YASASI,
   $\lambda$ kanalı). İki yıldız arasındaki $10^4$ AU'luk boşlukta dolanım kafesi yoktur —
   $\lambda\to0$ okuması.

Bu, teorinin Güneş Sistemi'ni koruyan mevcut konumunun aynısıdır (G-5: kompakt alt sistem, galaktik
F4'ü *düzgün alan* olarak görür; kendi penceresi yoktur) — geniş çift, Güneş Sistemi'nden bile
seyrek bir yapıdır. **Dolayısıyla teoride çiftin iç dinamiğine giren tek F4, galaktik alanın
çift-ölçeğindeki diferansiyelidir.**

## 3. Kalan artık — galaktik gelgit diferansiyeli

Galaktik alan Güneş çevresinde $g_{gal}=V^2/R_0=2{,}20\times10^{-10}$ m/s²; teorinin ayrışımıyla
$g_{F1}\approx1{,}25\times10^{-10}$, $g_{F4}=\sqrt{g_{F1}a_0}\approx0{,}96\times10^{-10}$ (toplam
denetimi: $2{,}21\times10^{-10}$ ✓). Düzgün bileşen göreli koordinatta tam sadeleşir; kalan,
alanın gradyanının çift boyunca farkıdır: $\Delta a\sim g_{gal}\,s/R_0$.

| $s$ (AU) | $\Delta a_{gelgit}/g_{iç}$ |
|---|---|
| 3 000 | $3{,}0\times10^{-7}$ |
| 10 000 | $1{,}1\times10^{-5}$ |
| 20 000 | $9{,}0\times10^{-5}$ |

### Sonuç

$$\boxed{\;\frac{\Delta a_{Newton'dan}}{g_{iç}}\;\lesssim\;10^{-4}
\qquad(s\leq2\times10^4\ \mathrm{AU};\ \text{baskın terim galaktik gelgit})\;}$$

**Teori geniş çiftlerde Newton öngörür** — sapma üst sınırı $10^{-4}$, gözlemsel tartışmanın
konusu olan ~%20–40'lık artışların üç-dört mertebe altında. Karşı-olgusal öz-F4 (%24–%158) ile
arasındaki boşlukta hiçbir ara değer yoktur: kanal ya taşıyıcılıdır ya değildir. G-10 bu yüzden
temiz bir ikili sınavdır.

## 4. Dürüstlük kayıtları

1. **Öngörü koşulludur.** "F4'ün taşıyıcısı koherent disk dolanımıdır" önermesi teorinin türetim
   zincirinden okunmuştur (md. 2'nin üç halkası) ama *hangi yapıların taşıyıcı olduğunun nicel
   eşiği* türetilmemiştir — bu, $\lambda$ kanalının açık ucuyla aynı kalemdedir. Gözlem MOND-tipi
   artışı kesinleştirirse (Chae 2023 yönü) çürüyen şey teorinin tamamı değil, **M-38'in
   disk-geometrisi kaynağıdır** ve F4'ün taşıyıcısı yeniden türetilmelidir; G-10'un çürütme
   koşulu tam budur.
2. Gelgit hesabı mertebe hesabıdır ($O(1)$ geometri çarpanı — Oort sabitleri — atılmıştır);
   $10^{-4}$ sınırını değiştirmez.
3. Çift *diskin içinde* yüzer; diskin ortamı çiftin iki üyesini **aynı** F4 ile iter — bu ortak
   ivme yörünge merkezine gider, iç dinamiğe girmez (Postülat 7'nin tam kuplaj/düzgün-alan
   sadeleşmesi). Sadeleşmenin bozulduğu tek terim md. 3'ün gradyanıdır.
4. Sayısal doğrulama tek satırdır (bu dosyanın bütün tabloları):
   `python -c "..."` — betikleşecek kadar iş yoktur; girdiler metinde eksiksizdir.
5. Bu hesap Claude Fable 5 tarafından üretilmiştir.

**Kitaba etkisi:** G-10 satırı "beklenti"den "koşullu hesaplı öngörü"ye yükselir (yapıldı);
7.4-12(n2) kapanış notu düşülür (yapıldı). Gaia DR3/DR4 geniş-çift analizlerinin kesinleşmesi
sınavın kendisidir — veri işi değil, literatür izleme kalemidir.
