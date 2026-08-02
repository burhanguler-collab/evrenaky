# Toplanma türetimi — bir kazanç, iki çürüyen aday, daralan uzay (iş 6)

**Hedef:** 95_RAR iş 1 / 7.4-12(h): *"şu an $a_{tam}=a_{F1}+a_{F4}$ basitçe toplanıyor ve M-37
bunu gerektiriyor mu, gösterilmemiştir"* borcunun türetimi; üç ölçülmüş hedef ve bir yasakla
(`VORTISITE_KARARI.md`). Hesaplar: `../../toplanma_turetimi.py` + oturum içi baryon-kayma denemesi.

---

## 1. KAZANÇ — basit toplam türetildi (koşullu)

Ortamın hâl yapısı iki kanalda da **lineerdir**: dalga kanalı $P=c^2\rho$ (M-44), deplasman
kanalı $(\partial P/\partial\chi)_\rho=-C$ ile $\nabla^2\chi=-q_nn_m$ (M-46). Lineer alan
denklemlerinde iki kaynağın basınç bozulumları süperpoze olur; test cismi toplam gradyanı duyar:

$$a=-\tfrac{1}{\rho}\nabla(\delta P_{F1}+\delta P_{F4})=a_{F1}+a_{F4}
\qquad\Big(+\,O(\delta P/P_0)\sim10^{-9}\ \text{çapraz terim}\Big)$$

Arka plan pürüzleri $10^{-9}$ mertebesinde olduğundan (Ek B; Dünya için $\Delta P/P_0\sim10^{-9}$)
düzeltme umutsuzca küçüktür. **Basit toplam artık varsayım değil, lineerliğin sonucudur.**

*Koşul (dürüstlük):* F1'in kanalı eylemde yazılıdır (M-46); **F4'ün dolanım kolunun eylem terimi
hâlâ açıktır** (Blok I Açık Uçlar: "F4/dolanım kolunun eyleme bağlanması"). Süperpozisyon
argümanı o kanalın da lineer rejimde olduğunu varsayar — zayıf bozulum rejiminde doğal, ama
eylem terimi yazılana dek toplama **[T-koşullu]** statüsündedir. Sonuç: 95_RAR iş 1'in yükü yer
değiştirdi — sorun *toplanmada değil*, F4'ün **genlik/pencere yasasında** ve eylem teriminde.

## 2. ÇÜRÜYEN ADAY — kayma-ağırlıklı koherens (iki biçimde de reddedildi)

Hipotez güzeldi: kaskadı diferansiyel dönmenin kayması besler; katı-cisim bölgede kayma sıfır →
koherent kolon beslenmez → $a_{F4}=\sqrt{w}\,\sqrt{\mathcal{G}M_{kaps}a_0}/R$,
$w=1-d\ln v/d\ln R$. İki uygulaması da adil kalibrasyonla sınandı:

| Model | $k_{kal}$ | medyan RMS | RAR eğimi | sınıf bandı |
|---|---|---|---|---|
| B (resmî, $w{=}1$) | 1,011 | **12,76** | **−0,043** | **16,1 %** |
| S (öz-uyumlu $w(v_{öng})$) | 2,775 | 30,79 | −0,131 | 25,6 % |
| S$_b$ ($w(V_{bar})$, baryon-kayma) | 0,985 | 15,62 | −0,080 | 17,6 % |
| S$_b$, $w_{max}{=}1$ | 1,171 | 14,69 | −0,080 | 19,1 % |

**Neden çöktü:** verinin istediği düzeltme deseni (derin uçta *daha çok*, Newton yakasında
*daha az* F4) kayma yapısıyla ters düşüyor — cücelerin yükselen eğrileri $w<1$ verir ve tam da
daha çok F4 isteyen derin uç **bastırılır**; öz-uyumlu biçimde bu kendini pekiştirir
(az F4 → daha da yükselen öngörü → daha küçük $w$). Kuşak artıkları her varyantta kötüleşti.
**Karar: kayma ağırlığı reddedildi** (ışıma-artığı emsalindeki gibi, kayıt silinmez).

## 3. Daralan aday uzayı — borcun güncel tarifi

Bugüne kadar dışlananlar: besleme seçimi ($M_{kaps}\!\leftrightarrow\!g_{bar}$, fark sığ),
geometri üssü ($f_{geo}^{\alpha}$, $\alpha>1$ verice dışlanır), **öz-tutarlı besleme** (taban,
×22), **kayma ağırlığı** (bu sınav, iki biçim). Kalan desen tek cümledir:

> Artık, $\log g_{bar}$'da tekdüze bir sürüklenmedir: teori $y=g_{bar}/a_0\gtrsim3$'te *fazla*,
> $y\lesssim0{,}3$'te *eksik* öngörür; hiçbir yerel geometrik/kinematik ağırlık bunu üretmiyor.

Ayakta kalan iki mekanik aday (türetilmeden **fit edilmeyecekler** — MOND'un $\nu$'süne
düşmemenin tek yolu):

1. ~~**Kanal-arası bastırma**~~ — **BİÇİMİ TÜRETİLDİ** ([PENCERE_TURETIMI.md](PENCERE_TURETIMI.md)):
   aranan bastırma, M-30'un Rankine iç kolunun galaktik denkleme uygulanmasıyla parametresizce
   çıktı — $W=\min(1,a_0/g_{kaps})$; küresel sürüklenme $\approx0$'a indi, galaksi-içi yarılandı
   ($-0{,}033$ kaldı), RMS iyileşti, band ve derin limit dokunulmadı. Statü [T-aday]; resmî
   denkleme alınması onay bekliyor.
2. ~~**Derin ucun λ payı**~~ — **ÇÜRÜDÜ** ([SINIF_ICI_SURUKLENME.md](SINIF_ICI_SURUKLENME.md)):
   ayrıştırma sınavı koşuldu; sınıflar-arası bileşen $+0{,}0006\approx0$, galaksi-İÇİ eğim
   $-0{,}074$ (küreselden büyük). Sürüklenme sınıf kanalının izi değil, galaksi-içi radyal
   pencere imzasıdır; λ yalnız bandı (ofsetleri) taşır. **Tek hedef aday (i) kaldı** ve sayısal
   ölçüsü keskinleşti: türetilen pencere galaksi-içi eğimi $-0{,}07\to\approx0$ çekmelidir.

## 4. Dürüstlük kayıtları

1. Kayma sınavlarında $d\ln v/d\ln R$ ayrık gradyanla alındı (gürültülü); ama çöküş gürültü
   ölçeğinin çok üstünde (RMS +%22…+%141) — hüküm gradyan tekniğine duyarlı değil.
2. $w_{max}$ (1 ve 1,5) iki değerle tarandı; ikisi de kötü.
3. md. 1'in süperpozisyon argümanı **yeni denklem üretmez** — mevcut denklemin toplama adımını
   gerekçelendirir; RAR sürüklenmesine dokunmaz (o, genlik yasasının işidir).
4. md. 3'ün iki adayı bugün **türetilmemiştir**; bu dosya onları aday olarak kaydeder, hiçbir
   biçim fit edilmemiştir.
5. Bu türetim/sınav Claude Fable 5 tarafından yapılmıştır; kayma hipotezi bu oturumda kurulup
   aynı oturumda verice reddedilmiştir — reddin kaydı kazancın kendisidir.
