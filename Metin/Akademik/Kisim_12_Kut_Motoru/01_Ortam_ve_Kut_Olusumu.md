# 12.1 Ortam ve Kut Oluşumu: Kavitasyon Eşiği ve Cep Yarıçapı

Evrenakı Teorisi'nin varlık tabanı **Kut**'tur. Bu kısma kadar Kut, çoğunlukla bir *ad* olarak kullanıldı: dolanımı taşıyan, Zerre'yi kuran, hesaba girmeyen temel yapı taşı. Burada o adın **nasıl var olduğunu** soruyoruz.

Cevap yeni bir mekanizma icat etmiyor. Sıkıştırılabilir bir akışkanda yeterince hızlı dönen bir bölge, merkezinde bir **boşluk** açar. Bu, laboratuvarda her gün görülen **kavitasyondur**: pervane ucunda, pompada, kırılan bir dalganın altında. Evrenakı'nda olan tam olarak budur — yalnız ölçek ve basınç, hiçbir laboratuvarın ulaşamayacağı düzeydedir.

Bu bölümün iddiası mütevazıdır ve tam da bu yüzden güçlüdür: **Kut'un oluşumu için Evrenakı'na yabancı bir yasa gerekmez.** Gereken tek şey, ortamın sıkıştırılabilir olması ve bir yerde dönmenin başlamış olmasıdır.

> **Kaynak sorusu açıkça beyan edilir.** Dönmenin *nasıl* başladığını bilmiyoruz. Teori bunu bir bilinmeyen olarak ilan eder ve öyle bırakır. Bilinen şudur: dönme vardır, ve bir kez varsa gerisi akışkan mekaniğidir. Bu kısım "gerisi"ni yazar.

---

## 12.1.1 Ortam: Sert (Zel'dovich) Akışkan

Evrenakı'nın hâl denklemi teorinin kendi postülatlarından gelir:

$$P = c_0^2\rho$$

Bu, sıkıştırılabilir akışkanların en sert hâlidir — **Zel'dovich sınırı**. İki doğrudan sonucu vardır ve ikisi de bu kısımda sürekli kullanılacaktır:

| Sonuç | İfade | Anlamı |
|---|---|---|
| Ses hızı | $v_{\text{ses}} = \sqrt{dP/d\rho} = c_0$ **tam** | $c_0$ evrensel bir sınır değil, **ortamın ses hızıdır** |
| Yoğunluk profili | $\rho/\rho_0 = e^{-(r_e/R)^2}$ | Kut'un çevresindeki **sınır tabakası** |

Taban büyüklükler:

| Sembol | Değer | Kaynak |
|---|---|---|
| $\rho_0$ | $6{,}8\times10^{16}$ kg/m³ | Evrenakı taban yoğunluğu |
| $P_0$ | $\tfrac14\rho_n c_0^2 = 6{,}07\times10^{33}$ Pa | Taban basınç |
| $c_0$ | $\sqrt{P_0/\rho_0}$ | Ortamın ses hızı |
| $r_e$ | Kut'un e-katlanma yarıçapı | $\rho = \rho_0/e$ olan yer |
| $\Sigma/P_0$ | $\gtrsim 1{,}9\times10^{9}$ | Kavitasyon eşiği oranı |

**$c_0$ bir tavan değildir.** Bu, Kısım 12'nin en sık yanlış okunmaya açık noktasıdır. $c_0$ yalnızca Evrenakı'nın ses hızıdır; ortamda ondan çok daha hızlı olaylar vardır ve Kut'un oluşumu bunlardan biridir. Hız merdiveni:

$$c_0 \;<\; \sqrt2\,c_0 \;<\; v_m \;<\; v_{\text{kav}}$$

| Hız | Değer | Ne? |
|---|---|---|
| $c_0$ | $2{,}998\times10^{8}$ m/s | Ortamın ses hızı |
| $v_t = \sqrt2\,c_0$ | $4{,}2397\times10^{8}$ m/s | **Duvar hızı** — $r_e$'de akışın hızı |
| $v_m$ | $\approx 4{,}36\times10^{4}\,c_0$ | Ara eşik |
| $v_{\text{kav}}$ | $\approx 6{,}16\times10^{4}\,c_0$ | **Kavitasyon hızı** |

Yani Kut'un sınır tabakasındaki akış zaten **süpersoniktir** ($M = \sqrt2 = 1{,}414$), oluşum anındaki hızlar ise $c_0$'nin **on binlerce katıdır**. Bu kısımda anlatılan hiçbir olay $c_0$ ile sınırlı değildir.

### Kut'un içindeki hız profili

Buradaki $1{,}414$ değeri yalnızca **sınır tabakasının** ($r_e$) hızıdır; Kut'un bütününü
temsil etmez. Dolanım sabit olduğu için
$\lvert v\rvert = \sqrt2\,c_0\,(r_e/R)$ ve merkeze inildikçe hız hızla büyür:

| Yer | $\lvert v\rvert$ | $M$ |
|---|---|---|
| $3\,r_e$ | $0{,}471\,c_0$ | 0,47 (subsonik) |
| $d_{\text{denge}} = 1{,}41\,r_e$ (bağ) | $\approx c_0$ | ≈1 |
| $r_e$ (sınır tabakası) | $1{,}414\,c_0$ | 1,41 |
| **$R_{\text{cep}}$ (cep duvarı)** | $\mathbf{6{,}164\times10^{4}\,c_0}$ | $\mathbf{6{,}16\times10^{4}}$ |

**Cep duvarındaki hız, standart fiziğin $c$ değeriyle kıyaslanamayacak ölçüde yüksektir.**
Ve bu sayı bağımsız olarak doğrulanır: $\sqrt2\,c_0\,(r_e/R_{\text{cep}}) = \sqrt2\,c_0\sqrt{1+\Sigma/P_0} = v_{\text{kav}}$ — yani cep duvarı, tanım gereği **kavitasyon
hızında** döner. İki ayrı yoldan aynı sayı çıkar.

**Compton kıyası.** Zitterbewegung resminde Compton dönüş hızı **tam olarak $c$**'dir
($\omega_C \cdot \hbar/m_ec = c$). Kut'un cep duvarı ise:

$$\frac{v(R_{\text{cep}})}{v_{\text{Compton}}} = 6{,}16\times10^{4}$$

> **Kut, Compton dönüş hızının yaklaşık 62 bin katında döner.** Zerre ölçeğindeki
> "hızlı" saydığımız her şey, Kut ölçeğinde yavaştır.

---

## 12.1.2 Kavitasyon Eşiği ve Cep Yarıçapı

Dönme başladığında merkeze doğru hız artar, basınç düşer. Basınç yeterince düştüğünde ortam **köprülenemez** ve bir boşluk açılır. Açılan boşluğun yarıçapı doğrudan türetilir:

$$\boxed{\;R_{\text{cep}} = \frac{r_e}{\sqrt{1+\Sigma/P_0}}\;}$$

$\Sigma/P_0 \gtrsim 1{,}9\times10^{9}$ değeriyle:

$$R_{\text{cep}} = 2{,}294\times10^{-5}\,r_e$$

Bu sayı Kısım 12 boyunca defalarca karşımıza çıkacaktır, çünkü **Kut'un gerçek boşluğu budur.** $r_e$ ise boşluğun kendisi değil, çevresindeki yoğunluk profilinin e-katlanma yarıçapıdır — yani **sınır tabakasının ölçeğidir.**

> **İkisini karıştırmak, bu kısımda yapılabilecek en pahalı hatadır.** $r_e$ ile $R_{\text{cep}}$ arasında **65 000 kat** vardır. 12.3'te gösterileceği gibi, Kutların birleşip birleşemeyeceği sorusunun cevabı tam olarak bu orandan çıkar.

Kavitasyon hızı da aynı orandan gelir:

$$v_{\text{kav}} = \sqrt2\,c_0\,\sqrt{1+\Sigma/P_0}$$

---

## 12.1.3 Yoğunluk Profili: Sınır Tabakası

Kut'un çevresi boş değildir. Yoğunluk merkeze doğru üstel olarak düşer:

$$\frac{\rho(R)}{\rho_0} = \exp\!\left[-\left(\frac{r_e}{R}\right)^{\!2}\right]$$

| $R/r_e$ | $\rho/\rho_0$ | Yorum |
|---|---|---|
| 0,5 | 0,0183 | Neredeyse boş |
| 1,0 | **0,3679** | Tanım gereği $1/e$ |
| 2,0 | 0,7788 | Tabakanın dışı |
| 3,0 | 0,8948 | Arka planın %89'u |
| 10,0 | 0,9901 | %99 |

Bu profil **sert bir duvar değildir.** Kut'un "yüzeyi" yoktur; yoğunluk sürekli olarak arka plana yaklaşır. Bu, 12.3'te iki Kut'un ne zaman "değdiğini" tanımlarken kritik olacaktır: değme, keskin bir temas değil, **tabakaların örtüşmesidir.**

> **Neden üstel — keskin duvarlı okuma neden yanlıştır.** Sıkıştırılamaz bir ortam
> varsayılırsa profil $p = 1 - (r_e/R)^2$ çıkar ve Kut'a **keskin bir duvar** atfeder.
> Sert akışkanda bu biçim geçersizdir; doğru biçim üsteldir. Fark önemsiz değildir:
> keskin duvar, tabakaların örtüşmesini — dolayısıyla 12.3'te kurulan **bağ
> mekanizmasının tamamını** — imkânsız kılardı. Kut'un bir yüzeyi olsaydı, Kutlar
> birbirine tutunamazdı.

---

## 12.1.4 Oluşumun Aşamaları

Simülasyon oluşumu dört evrede gösterir. Evreler keyfi değildir; her biri farklı bir fiziksel eşiğe karşılık gelir.

| Evre | Ne olur | Eşik |
|---|---|---|
| **1 — W'de dönme** | Dördüncü uzay boyutunda merkezî dönme başlar | (kaynak bilinmiyor, beyan edilmiştir) |
| **2 — Kavitasyon** | Basınç düşer, ortam köprülenemez, boşluk açılır | $v \to v_{\text{kav}}$ |
| **3 — Kut oluşur** | Boşluk $R_{\text{cep}}$'te kararlı hâle gelir | $R_{\text{cep}} = r_e/\sqrt{1+\Sigma/P_0}$ |
| **4 — Sınır tabakası** | Çevrede üstel yoğunluk profili yerleşir | $\rho = \rho_0 e^{-(r_e/R)^2}$ |

Dördüncü evre, Kut'u yalnız bir delik olmaktan çıkarıp **etkileşebilen** bir nesne yapan şeydir. 12.3'te kurulan bütün bağ mekanizması bu tabaka üzerinden işler.

<p style="margin:20px 0;padding:16px;border:1px solid #22c55e;border-radius:10px;background:rgba(34,197,94,0.07)"><a href="Simulasyon/kisim12/kut_kavitasyon_dogusu.html" target="_blank" rel="noopener" style="display:inline-block;padding:12px 22px;background:#166534;color:#ffffff;border-radius:8px;font-weight:700;text-decoration:none;font-size:1.05em">&#9654;&#65039; SİMÜLASYONU AÇ — Kavitasyonla Kut oluşumu</a><br><span style="color:#a1a1aa;font-size:0.9em;display:inline-block;margin-top:8px">Yan yana iki ekran: solda <b>4B</b> dönüş ve kavitasyon, sağda aynı olayın <b>3B kesitimizde</b> nasıl göründüğü. Dört evre tek tek izlenebilir, durdurulup ileri sarılabilir. Yoğunluk profili, cep yarıçapı ve kavitasyon hızı canlı okunur. <b>21 öz-sınama</b> sayfa açılırken koşar ve sonucu üstte gösterir — hâl denklemi, profil yasası, $R_{\text{cep}}$ formülü ve hız merdiveni dahil. Tek dosya, dış bağımlılık yok.</span></p>

---

## 12.1.5 Bu Bölümün Sınırı

Burada gösterilen şey **Kut'un var olabileceğidir** — sıkıştırılabilir bir ortamda dönme varsa, kavitasyon kaçınılmazdır ve açılan boşluğun yarıçapı hesaplanabilir.

Gösterilmeyen şey, dönmenin **neden** başladığıdır. Teori bunu bilmediğini açıkça yazar. Bu bir eksiklik değil, bir **sınır beyanıdır**: Evrenakı Teorisi, ilk dönmenin kaynağını açıklama iddiasında değildir.

Bir sonraki bölüm, o dönmenin bir kez var olduktan sonra **ne ürettiğini** ele alır — ve orada teorinin asıl motoru ortaya çıkar.
