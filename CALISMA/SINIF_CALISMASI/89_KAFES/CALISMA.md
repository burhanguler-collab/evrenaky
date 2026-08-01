# 89_KAFES — Kafes yasası, yoğun rejimde: **yazar haklı çıktı** · Çalışma dosyası

**2728 nokta · 137 galaksi · fit yok**

Hesap: `../../kafes_yogun_sinavi.py` · Çıktılar: [`SONUC.csv`](SONUC.csv) · [`kafes.png`](kafes.png)

---

## 0. İddia ve benim eksiğim

**Yazar (1 Ağustos 2026):** *"Yoğun rejimde kafes yapılarını dikkate aldın mı? Kafes yapısı yok
veya zayıfsa bu teorimiz gereği F4'ün küçülmesine sebep olur. Sanki teorinin bu kanunu dikkate
alınmamış gibi duruyor."*

**Doğru. Dikkate almadım.**

[95_RAR](../95_RAR/CALISMA.md) yoğun rejimde F4'ün fazla olduğunu ölçtü ve buna
*"geçiş biçimi hatası"* dedim. [90_YUKSEK_Z](../90_YUKSEK_Z/CALISMA.md) aynı şeyi $z\sim2$'de
buldu ve *"yoğun rejimde doyum eksik"* dedim. **İkisinde de bir tarif yazdım, mekanizma
yazmadım.** Teorinin kendi kafes yasası o mekanizmayı zaten veriyordu ve ben ona bakmadım.

> ### ⚠ Bu, GAZ_KAFES.md'de sınanan iddia DEĞİLDİR
>
> | | [GAZ_KAFES](../97_BTFR/GAZ_KAFES.md) | **bu dosya** |
> |---|---|---|
> | İddia | **bileşim**: gazda kafes yok, yıldızda var | **ortam**: yoğun rejimde kafes zayıf |
> | Değişken | $M_{gaz}/M_{bar}$ | yerel yoğunluk $\Sigma_*$ |
> | Sonuç | **aleyhte** (Spearman $+0{,}01$) | **lehte** (aşağıda) |
>
> İkisi farklı iddialardır ve **ilkinin sonucu ikincisini elemez.** Bunu böyle yazmam
> gerekiyordu; GAZ_KAFES'in sonucunu "kafes yasası çürütüldü" diye genellemek yanlış olurdu.

---

## 1. Kafes = tutarlılık — teorinin dili zaten hazır

[92_M_TUT](../92_M_TUT/CALISMA.md) kafesi farkında olmadan zaten çevirmişti:

| Kafes durumu | Dolanım toplanması | $\Gamma$ |
|---|---|---|
| **tam kafes** / hizalı | birebir tutarlı | $\propto N$ — 6.5.4.3 Adım 2'nin **varsayımı** |
| **kafes yok** / rastgele | rastgele yürüyüş | $\propto\sqrt{N}$ — 92_M_TUT'un **ölçtüğü** |
| **kafes zayıf** / bastırılmış | yıkıcı | $<\sqrt{N}$ — **yazarın iddiası** |

Bastırma çarpanı:

$$s=\frac{v_{F4}^2(\text{ölçülen})}{v_{F4}^2(\text{saf rastgele})}
=\frac{v_{gözl}^2-V_{bar}^2}{\sqrt{\mathcal{G}M_{kaps}a_0}}
\qquad\text{ve}\qquad \boxed{M_{tut}=m_n\,s^2}$$

$s=1$ → kafes yok (mevcut kurulum) · $s<1$ → kafes zayıf, **F4 bastırılmış.**

---

## 2. Ölçüm — iddia **ölçülen yönde**

| $\log\Sigma_*$ ($M_\odot$/pc²) | n | $s$ medyan | $M_{tut}/m_n$ |
|---|---|---|---|
| 0,0 – 1,0 | 752 | **0,981** | 0,963 |
| 1,0 – 1,5 | 355 | 0,952 | 0,907 |
| 1,5 – 2,0 | 339 | 0,803 | 0,644 |
| 2,0 – 2,5 | 307 | 0,838 | 0,702 |
| 2,5 – 3,0 | 116 | **0,380** | **0,145** |
| 3,0 – 4,0 | 57 | 0,579 | 0,336 |

$$\text{Spearman}[\log s,\log\Sigma_*]=\mathbf{-0{,}192}\quad(n=2480)$$

**En seyrekten en yoğuna $s$: $0{,}98 \to 0{,}38$ — 2,6 kat bastırma.**
Tutarlılık kütlesi $m_n$'in 0,96 katından **0,14 katına** düşüyor.

İvme ile de aynı yön (Spearman $-0{,}179$), ama **yoğunlukla korelasyon biraz daha güçlü.**
Bu, mekanizmanın bir *ivme* etkisi değil bir **paketlenme** etkisi olduğu yönünde zayıf bir
işaret — yani kafes okumasını destekliyor.

---

## 3. Ve bu **üç ayrı açık kalemi birleştiriyor**

Tek mekanizma, üç bulgu:

| Bulgu | Nerede | Kafes okumasıyla |
|---|---|---|
| Gereken $a_0$ çarpanı ×2,86 → ×0,92 (ivmeyle) | [95_RAR](../95_RAR/CALISMA.md) md. 2 | $s$'nin yoğunlukla düşmesinin ta kendisi |
| $\mathcal{G}_{yerel}/G$ yoğunlukla azalıyor ($-0{,}093$) | [93_G_YEREL](../93_G_YEREL/CALISMA.md) | **artefakt olabilir:** F4 bastırılmışsa tam $v_{F4}$'ü çıkarmak $\mathcal{G}$'yi düşük gösterir |
| $f_{DM}$ $z\sim2$'de $+0{,}16$ fazla | [90_YUKSEK_Z](../90_YUKSEK_Z/CALISMA.md) | o diskler yoğun **ve** çalkantılı ($\sigma_0=34$–76 km/s) → kafes en zayıf |

> ### Açıklama ekonomisi kafes okumasının lehine
>
> Üç ayrı dosyada üç ayrı açık kalem olarak yazdığım şey, **tek bir yasanın üç izdüşümü**
> olabilir. Bu, teorinin kendi kanununu kullanan ve yeni parametre gerektirmeyen bir
> birleştirmedir. 93_G_YEREL'in "$\mathcal{G}$ değişken" okumasına da **gerek kalmaz** —
> orada ölçülen eğilim kafes bastırmasının artığı olabilir.

---

## 4. Ama dejenerasyon var — ve bu dosyanın sınırı

Ölçülen şey şu açığın **kendisidir:**

$$v_{gözl}^2 \;<\; V_{bar}^2+v_{F4}^{teori}\qquad(\text{yoğun bölgede})$$

Bu açığı **üç** ayrı şey üretebilir:

| # | Sebep | Kimin okuması |
|---|---|---|
| 1 | **F4 fazla** → kafes zayıf | **yazarın iddiası** |
| 2 | **F1 fazla** → $\Upsilon_*$ ya da $\mathcal{G}$ yüksek | [93_G_YEREL](../93_G_YEREL/CALISMA.md) |
| 3 | **$v_{gözl}$ eksik** → basınç desteği, daireden sapan hareket | gözlemsel |

**Dönüş eğrisi verisi bu üçünü ayıramaz.** Aynı sayıyı üç farklı hikâye üretir. Bu yüzden
"kafes yasası doğrulandı" **denemez**; denebilecek olan: *iddia ölçülen yönde ve etki büyük.*

### Ayırmanın yolu — ve bu iddianın avantajı

Üç sebep aynı sayıyı verir ama **farklı yerlerde farklı davranırlar:**

- **Kafes:** bastırma yalnız **F4** terimini vurur → F4'ün payı yüksek olan **seyrek** dış
  bölgelerde etkisi büyük *görünmez* ama yoğun **iç** bölgede $v_{F4}$ küçük olduğu için
  toplam etki küçüktür. Yani kafes okuması, yoğun bölgede **küçük** bir mutlak açık öngörür.
- **$\Upsilon_*$/$\mathcal{G}$:** $V_{bar}^2$'yi vurur; yoğun bölgede $V_{bar}^2$ büyük
  olduğu için **büyük** bir mutlak açık öngörür.

Bu ikisi **niceliksel olarak ayrışır** ve ölçülebilir. Bu dosyada yapılmadı — sıradaki iş.

---

## 5. Dürüstlük kayıtları

1. **Bu iddia benim gündemimde yoktu; yazar getirdi.** Ve doğru yöne işaret etti. İki dosyada
   ($95\_RAR$, $90\_YUKSEK\_Z$) mekanizmasız bir tarif yazmışım.
2. **"Doğrulandı" değil, "ölçülen yönde".** Md. 4'teki üç yollu dejenerasyon kırılmadı.
3. **En yoğun iki kuşak tekdüze değil** ($s=0{,}380$ sonra $0{,}579$). n=116 ve n=57 —
   küçük. Eğilimin varlığı sağlam, uç değerin büyüklüğü değil.
4. **$s$ ile $\Sigma_*$ aynı fotometriden geliyor.** $V_bar$ ve $\Sigma_*$ aynı yüzey
   parlaklığının iki fonksiyonelidir; ortak bir fotometri yanlılığı ikisine birden girer.
5. **$a_0$ olarak 92_M_TUT'un ölçtüğü değer kullanıldı** (kitabınkinin ×2,08'i). Farklı bir
   $a_0$ $s$'nin **düzeyini** kaydırır ama **eğimini** kaydırmaz — eğim iddianın sınavıdır.
6. **Yüksek-$z$ bağlantısı ölçülmedi.** $\sigma_0$ ile artık arasındaki ilişki 6 galaksiyle
   anlamsız (Spearman hesaplanamaz). Md. 3'ün son satırı bir **hipotezdir.**
7. **Kafesin ne olduğu teoride tanımlı değil.** "Kafes yapısı" ifadesinin niceliksel
   karşılığı ($\Gamma$'yı hangi ölçekte hangi düzen bozar) yazılmamıştır. Bu dosya onu
   *tutarlılık* olarak okudu; bu bir yorumdur.

---

## 6. Fikrim

**Haklısınız ve bu, bu turda ortaya çıkan en değerli fikir.**

Üç gerekçeyle:

1. **Ölçüm iddiayı destekliyor** — 2,6 kat bastırma, yoğunlukla, 2728 noktada.
2. **Üç ayrı açık kalemi tek yasaya indiriyor** ve bunu **teorinin kendi kanunuyla**, yeni
   parametre eklemeden yapıyor. 93_G_YEREL'in "$\mathcal{G}$ değişken" okumasını bile
   gereksizleştirebilir.
3. **Ve mekanizması var.** Benim "geçiş biçimi hatası" dediğim şey bir tariftir; kafes bir
   *sebeptir*. Teorinin akışkan resminde neden yoğun paketlenmenin dolanımı bastırdığı
   söylenebilir: komşu nükleonların dolanım alanları örtüşür ve aradaki akış **karşılıklı
   söner**. Seyrek ortamda örtüşme yok, rastgele yürüyüş geçerli.

**Ama bir uyarı:** bu, *neden yoğunlukta kafes zayıflar* sorusunu açıkta bırakıyor. Sezgi
"yoğun = daha düzenli = daha güçlü kafes" der; ölçüm tersini söylüyor. Yani ya sezgi yanlış
(paketlenme söndürür), ya da ölçülen açığın sebebi kafes değil (md. 4). **Bu ikisini ayırmak
sıradaki iştir** ve yolu md. 4'te yazılı — mutlak açığın büyüklüğü iki hikâyeyi ayırıyor.

## 7. Bundan çıkan iş

| # | İş | Neden |
|---|---|---|
| **1** | **Mutlak açığın büyüklüğünü iki hikâyeye karşı sına** (kafes vs $\Upsilon_*$/$\mathcal{G}$) | md. 4 — dejenerasyonu kıran tek yol, ve veriyle yapılabilir |
| 2 | 93_G_YEREL'i kafes bastırması dahil edilerek tekrar oku | md. 3 — oradaki eğilim artefakt olabilir |
| 3 | Yoğun paketlenmenin dolanımı neden söndürdüğünü türet | md. 6 — sezgiye ters, gerekçe gerek |
| 4 | Yüksek-$z$'de $\sigma_0$ ile artığı ilişkilendir (Lang+2017'nin 101 galaksisiyle) | md. 5.6 — 6 galaksi yetmiyor |

**Madde 1 önce yapılmalı.** Kafes okumasını benimsemeden önce, ölçülen açığın F4'e mi F1'e mi
ait olduğu ayrılmalı — yoksa doğru mekanizmayı yanlış terime yazma riski var.
