# 10.8 Eleme Zinciri — Açığın Anatomisi

*(Hesaplar: `CALISMA/kafes_yogun_sinavi.py`, `CALISMA/acik_ayirma_sinavi.py`, `CALISMA/galaksi_acik_taramasi.py` · kayıtlar: `89_KAFES/` (+`AYIRMA.md`, `GOZLEMSEL.md`), `88_TARAMA/` (+`GURULTU.md`)*)

Nihai denklemin kalan artığı iki bileşene ayrılır: yoğun rejimde tek yönlü bir **mutlak açık** (teori orada fazla itim üretir) ve galaksiden galaksiye bir **saçılma**. Bu bölüm, o iki bileşen için öne sürülebilecek bütün adayları tek tek sınayıp eler — ve elemeler, kalan açığın adresini bulgu düzeyinde daraltır.

## 10.8.1 Kafes yasası yoğun rejimde — iddia ölçülen yönde

Teorinin kendi kanunu, yoğun ortamda kafes yapısı zayıfsa F4'ün küçülmesini gerektirir. Doğrulama programı bu yasayı tutarlılık diliyle ölçmüştür: nihai kurulum rastgele-yürüyüş toplanmasıdır ($\Gamma\propto\sqrt{N}$); kafes zayıflığı, bunun da altına inen bir **bastırma çarpanı** $s$ üretir ve $M_{tut}=m_n s^2$ olarak okunur.

Ölçüm (2728 nokta, 137 galaksi, fit yok): en seyrek yoğunluk kuşağından en yoğununa $s$ medyanı **0,98'den 0,38'e** düşer — 2,6 kat bastırma, ölçülen yönde (Spearman$[\log s,\log\Sigma_*]=-0{,}19$). Üstelik korelasyon ivmeyle değil **yoğunlukla** biraz daha güçlüdür — mekanizmanın bir paketlenme etkisi olduğu yönünde zayıf bir işaret.

![Kafes yasası yoğun rejimde](Gorseller/k10_kafes.png)

Bu tek ölçüm, üç ayrı dosyada üç ayrı açık kalem gibi duran şeyi tek yasanın izdüşümü olarak birleştirmeye adaydır: radyal ivme bağıntısının geçiş artığı (10.6.2), $\mathcal{G}_{yerel}$ eğilimi (10.7.4) ve yüksek-$z$ aşımı (10.9).

## 10.8.2 Ama dejenerasyon vardı — ve kırıldı

Yoğun bölgede ölçülen açık $D=V_{bar}^2+v_{F4}^{teori}-v_{gözl}^2>0$'ı üç ayrı hikâye üretebilir: **kafes** (yalnız F4'ü bastırır), **$\mathcal{G}$/ortam** (bütün $v^2$'yi ölçekler), **$\Upsilon_*$** (yalnız yıldız terimini ölçekler). Üçü aynı sayıyı verir ama **farklı fiziksel sınırlar** taşır — ve bu onları ayırır. Adil ölçüt: her hikâye kaç noktada fiziksel olarak imkânsız bir değer ister?

| $\log g_{bar}$ kuşağı | KAFES imkânsız | $\mathcal{G}$ imkânsız | $\Upsilon_*$ imkânsız |
|---|---|---|---|
| −10,0 … −9,5 | %10,7 | **%0,0** | %34,6 |
| **−9,5 … −9,0 (en yoğun)** | **%24,8** | **%0,0** | %22,2 |
| Tümü (2889 nokta) | %5,5 | **%0,0** | %58,1 |

![Açığın üç hikâyeye ayrıştırılması](Gorseller/k10_ayirma.png)

**Belirleyici satır en yoğun kuşaktır:** orada kafes hikâyesi noktaların dörtte birinde **negatif F4** ister — açık, F4 teriminin tamamından büyüktür; kafes tam bastırma yapsa bile ($s=0$) kapatamaz. Ve bu koşul $a_0$'dan bağımsızdır, cebirsel olarak sadeleşir:

$$D>v_{F4}\iff V_{bar}^2>v_{gözl}^2$$

**Yoğun uçta baryonlar tek başına gözlemi aşmaktadır.** F4 pozitif tanımlı olduğundan eklenen her şey durumu kötüleştirir. Yani yoğun-rejim açığının kaynağı F4'ün genliği değildir; kafes bastırması gerçek ve ölçülen yönde olsa da, en yoğun uçtaki açığı **tek başına** taşıyamaz. $\Upsilon_*$ hikâyesi ise noktaların yarısından fazlasında fotometrik bandın dışına çıkmayı gerektirir ve elenir. Sınırına hiç dayanmayan tek hikâye ortam/$\mathcal{G}$ kanalıdır.

## 10.8.3 Saçılmanın bütçesi — "%68 galaksiler arası"nın gerçek yüzü

Açığın varyansının üçte ikisi galaksiler arasıdır. Bu pay, gözlemsel hata bütçesine karşı ölçülmüştür (`GURULTU.md`): **galaksiler arası varyansın ~%78'i ölçüm bütçesidir** — en büyük kalemi uzaklık belirsizliğidir (%59; $L\propto D^2$). Gerçek, fiziksel galaksiler-arası pay ~%15'e iner.

![Gözlemsel bütçe ayrıştırması](Gorseller/k10_gozlemsel.png)

Aynı ayrıştırma iki aday açıklamayı da eler: **basınç desteği** elenmiştir (öngördüğü radyal imza ters işaretli çıkar) ve **eğiklik** yetersizdir. **Sınıf bandı ise gerçektir:** uzaklık hatası onun yalnız %26'sını açıklar. Yani galaksi başına saçılmanın büyük kısmı ölçüm gürültüsüdür; sınıftan sınıfa sistematik band (0,115 dex) fiziksel bir kalem olarak kalır.

## 10.8.4 On dört değişken taraması — null sonuç

Galaksi başına açığı **öngören** bir değişken var mı? On dört aday (kütle, ışıma, yüzey parlaklığı, disk ölçeği, etkin yarıçap, düz hız, gaz kesri, morfoloji, eğiklik, kalite bayrağı, uzaklık, HI genişliği, kovan kesri…) iki örneklemde tarandı ve **başka-yere-bakma düzeltmesi** uygulandı (4000 permütasyonla boş dağılım; eşik onun %95 dilimi).

![14 değişken taraması](Gorseller/k10_tarama.png)

**Hiçbiri eşiği aşmaz.** En güçlü aday ($\log V_{flat}$, $-0{,}43$) eşiğin (0,455) altında kalır ve tam örneklemde kararsızdır; iki örneklemde de kararlı tek işaret SPARC kalite bayrağıdır ($+0{,}19$) — gözlemsel bileşenin bir izi, ama küçük. Null sonuç, gürültü ayrıştırmasından sonra **güçlenmiştir** (görünürdeki güçlü korelasyonların gürültü seyreltmesinden geldiği gösterildi).

En olası okuma: kalan galaksi-başına saçılma tek bir sebepten değil, birkaç küçük etkinin toplamından gelir — tarama tam olarak bu deseni verir, ve bu, tek bir mekanizma aramanın yanlış strateji olabileceği anlamına gelir.

## 10.8.5 Eleme zincirinin bilançosu

| Aday | Sınav | Hüküm |
|---|---|---|
| $\Upsilon_*$ (yıldız kütle/ışık) | fiziksel sınır sınavı | **elendi** (%58 imkânsız; fotometrik band) |
| Kafes bastırması (tek başına) | en yoğun kuşak | **elendi** ($V_{bar}^2>v_{gözl}^2$; $a_0$'dan bağımsız) |
| Basınç desteği | radyal imza | **elendi** (imza ters işaretli) |
| Eğiklik | bütçe ayrıştırması | yetersiz |
| Uzaklık | bütçe ayrıştırması | saçılmanın ana kalemi (%59) — ama **sınıf bandını açıklamaz** (%26) |
| 14 galaktik değişken | permütasyon eşiği | **null** |
| Ortam/$\mathcal{G}$ kanalı | fiziksel sınır sınavı | **ayakta kalan tek aday** (%0 imkânsız) |

Kalan iki gerçek fizik kalemi — yoğun-rejim davranışı (baryon tarafında, ortam kanalında) ve sınıf bandı — 10.10'un açık kalemleri olarak devralınır.
