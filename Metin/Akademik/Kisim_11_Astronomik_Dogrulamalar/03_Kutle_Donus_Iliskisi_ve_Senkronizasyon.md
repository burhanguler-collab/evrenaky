# 11.3 Kütle-Dönüş İlişkisi ve Yörünge Senkronizasyonu (Kilitlenme)

Standart gök mekaniği, Ay gibi uyduların neden gezegenlerine kilitlendiğini veya gezegenlerin eksenel dönüş hızlarının neden uzayla yavaşladığını "Gelgit Sönümlemesi" veya "Dinamik Sürtünme" ile modeller. Evrenakı teorisinde bu kilitlenme (senkronizasyon) ve uydu göçü, Zerre sürtünmesinin yarattığı **artık kuplaj** ve vorteks profil dengesinin kaçınılmaz matematiksel çıktısıdır (Bkz. Ek M-37).

## 11.3.1 İki Denge, İki Yoğunluk: "Madde Düşer, Ortam Dolaşır"

Kütle çevresindeki tek fiziksel alan basınçtır. Fakat aynı $\nabla P$ alanı **iki ayrı nesneye iki ayrı yoğunluk üzerinden** etki eder ve bu ayrım karıştırılmamalıdır (Ek M-9, Geçerlilik Sınırı):

| | Denge denklemi | Bölen yoğunluk | Sonuç |
|---|---|---|---|
| **Madde** (nükleon: katı deplasman cebi) | $\vec a=-\dfrac{1}{\rho_n}\nabla P$ | $\rho_n$ — nükleon öz yoğunluğu | akıp dengelenemez, **bütün hâlde itilir → düşer** |
| **Ortam** (Zerre akışkanı) | $\dfrac{1}{\rho_0}\dfrac{dP}{dR}=\dfrac{v_\theta^2}{R}$ | $\rho_0$ — arka plan yoğunluğu | gradyana düşerek değil **dolaşarak** cevap verir |

### Maddenin yörüngesi: serbest düşme

Yörüngedeki cismi taşıyan bir mekanizmaya gerek yoktur — cisim basınç gradyanında **düşer.** Dairesel yörünge şartı maddenin kendi ivmesiyle yazılır:

$$\frac{v_{madde}^2}{R}=\bigl|a_{madde}\bigr|=\frac{1}{\rho_n}\frac{dP}{dR}=\frac{\mathcal{G}M}{R^2} \;\Longrightarrow\; \boxed{\;v_{madde}(R)=\sqrt{\frac{\mathcal{G}M}{R}}\;}$$

Klasik yörünge hız profili, kütleçekiminden bağımsız bir basınç dengesi olarak böylece yeniden türetilir.

### Ortamın dolaşımı: aynı alan, farklı yoğunluk

Aynı $dP/dR$ ortamın kendi merkezcil ihtiyacını da karşılamak zorundadır (M-22'nin siklostrofik dengesi). Fakat ortam $\rho_0$ ile bölünür:

$$v_\theta^2=\frac{R}{\rho_0}\frac{dP}{dR}=\frac{\rho_n}{\rho_0}\cdot\frac{\mathcal{G}M}{R} \;\Longrightarrow\; \boxed{\;v_\theta(R)=\sqrt{\frac{\rho_n}{\rho_0}}\;v_{madde}(R)=2\,v_{madde}(R)\;}$$

$\rho_0=\frac{1-k}{4}\rho_n$ ve $k=0$ olduğundan (Ek M-8) oran **tam 2'dir** — serbest parametre içermez.

> **Kritik ayrım — kapılış yörüngeyi sağlamaz.** Sürüklenme zarfı (Postülat 7) bir **taşıma mekanizması değil, yerel sürükleme bastırıcısıdır.** Zarfın içinde bağıl hız sıfıra iner ve klasik $F_d\propto\rho v^2$ sürüklemesi kaybolur; Michelson–Morley'in null sonucu bundandır. Ama gövdenin yörüngesi zarftan gelmez — basınç gradyanında serbest düşmeden gelir. Cisim ortamın hızına **kilitli olsaydı** $2v_{Kepler}$ ile dolanırdı; gözlem bunu kesin biçimde dışlar.
>
> *(Kayıt: bu bölümün önceki sürümü "sürüklenme zarfı nedeniyle uydu bu akışkana hapsolur, $v_{yör}=v_\theta$" yazıyor ve maddenin yörüngesini ortamın dengesinden çıkarıyordu — iki yoğunluk karışmıştı. Sonuç doğru, gerekçe yanlıştı. Aynı karışıklık Ek M-37'nin sıfırıncı mertebe tanımında da vardır ["sürüklenme... yörünge hareketinin kendisini sağlar"] ve Ek M-9 ile çelişir; düzeltmesi izin kalemi olarak kayıtlıdır.)*

### Doğrudan bir öngörü: ortam–madde kayması

İki hız arasındaki fark serbest bir sayı değildir; **her yarıçapta yörünge hızının kendisine eşittir:**

$$\Delta v = v_\theta - v_{madde} = \left(\sqrt{\tfrac{\rho_n}{\rho_0}}-1\right)v_{madde} = v_{madde}$$

| Sistem | $v_{madde}$ | $v_{ortam}$ | Kayma |
|---|---|---|---|
| Merkür | 47,9 | 95,8 | **47,9 km/s** |
| Dünya yörüngesi | 29,8 | 59,6 | **29,8 km/s** |
| Jüpiter | 13,1 | 26,1 | **13,1 km/s** |
| Ay yörüngesi (Dünya çevresi) | 1,02 | 2,04 | **1,02 km/s** |
| Güneş, galaktik yarıçap | 220 | 440 | **220 km/s** |

Bu, $\rho_n/\rho_0=4$ oranının doğrudan sınavıdır ve hiçbir serbest kalem içermez. Ortam görünmez olduğu için kayma bugüne dek ölçülmemiştir; **açık kalem:** zarf gövdeyle birlikte giderken çevre ortam iki kat hızlı aktığından zarf sınırında bir **kayma tabakası** doğar. Bu tabakanın yitimi ve torku hesaplanmamıştır (Ek M-43'ün altkritik bastırması adaydır).

### Galaktik zincire etkisi: yok

Kısım 10'un ve 6.5.4'ün tüm galaktik zinciri **madde seviyesindedir** — $a_{F4}$ Ek M-38'de $C/\rho_n$ ile yazılır, dönüş eğrisi yasası $v^2=R\,a_{madde}$ biçimindedir. Dolayısıyla $a_0$, $\ell_\omega$ ve M-45'in mikro–makro kapanışı bu ayrımdan **etkilenmez.** Yukarıdaki 2 çarpanı yalnız ortamın kendi dolaşımına aittir ve gözlenen dönüş eğrilerine girmez.

## 11.3.2 Gevşeme Zamanı ($\tau_{ret}$) ve Sürüklenme Rejimi

Uydu ile Evrenakı girdabı arasında bağıl bir hız ($\Delta v$) oluşursa, akışkan Stokes biçimli bir artık kuplaj (sürtünme kuvveti) uygular:
$$F_{s\ddot{u}r} = 6\pi\,\eta_E\,a_b\,\Delta v \;\Longrightarrow\; \frac{d(\Delta v)}{dt} = -\gamma_{s\ddot{u}r}\Delta v$$

Burada $a_b$ uydu yarıçapı, $\eta_E$ Evrenakı viskozitesi (sönüm katsayısı) ve $\gamma_{s\ddot{u}r} = \frac{6\pi\eta_E a_b}{m}$ ivmelenme çarpanıdır. Uydu kütlesi $m=\tfrac43\pi a_b^3\rho_c$ kullanılarak, yörüngenin denge düzlemine (ekvatora) gevşeme zaman ölçeği ($\tau_{ret}$) türetilir:

$$\boxed{\;\tau_{ret} = \frac{1}{\gamma_{s\ddot{u}r}} = \frac{2\,\rho_c\,a_b^{2}}{9\,\eta_E}\;}$$

Bu tek denklem, Güneş Sistemi mimarisinin neden bugünkü "gevşemiş" hâlinde olduğunu izah eder:
1. **Eş Düzlemlilik:** Yörünge eğikliği ($i \ne 0$) olan uydular, $\tau_{ret}$ süresi içinde sistemin ana ekvator düzlemine oturur.
2. **Dairesellik:** Eksantrik yörüngeler daireselliğe sönümlenir.
3. **Kilitlenme:** Cisimler sürüklenme zarfı içinde akıntıyla eş-dönüşe zorlanarak kilitlenir (Tidal Locking).

## 11.3.3 Senkron Yarıçap ve Uydu Göçü (Phobos/Triton)

Yörüngedeki kütle, yerel bir basınç çukuru (gradyan lobu) taşır. Yörünge kilitlenmesi sonrasında, uydunun kaderi (içeri düşmesi veya dışarı açılması) ana gövdenin (gezegenin) dönüş açısal hızı ($\omega_{g\ddot{o}vde}$) ile uydunun açısal hızı ($\omega_{uydu}$) arasındaki yarışa bağlıdır. Sınır çizgisi, **senkron yarıçaptır**.

- **Senkron Üstü Rejim (Ay, Deimos):** Eğer $\omega_{g\ddot{o}vde} > \omega_{uydu}$ ise, gezegenin yüzey hızı uydudan fazladır. Gelgit şişkinliği ve gradyan lobu uydunun **önüne** geçer. Lob, uyduya ileri yönde kinetik enerji aktarır. Uydu dışarı sarmal çizer (Örn. Ay yılda ~3.8 cm uzaklaşır).
- **Senkron Altı Rejim (Phobos, WASP-12b):** Eğer $\omega_{g\ddot{o}vde} < \omega_{uydu}$ ise, uydu gezegenden hızlı dolanmaktadır. Lob geride kalır ve uyduyu frenler. Yörünge bozunur, uydu içe göçer (Örn. Phobos Mars'a yaklaşır).
- **Retrograd Yörünge (Triton):** Lob daima karşı yönde kalır ve sönüm çok agresiftir. Triton sistemdeki en belirgin içe göç vakasıdır.

*(Not: Retrograd uyduların bugüne dek hayatta kalması, $\eta_E$ sönüm katsayısının inanılmaz derecede küçük olduğunu kanıtlar. Phoebe verisi $\eta_E$'nin suyun viskozitesinin otuzda biri kadar küçük olması gerektiğini gösterir.)*
