# ÇALIŞMA DOSYASI — Eksen Devinimi ve Oblikite

> **Statü:** Çalışma dosyası. Yayın bölümü **değil**, site menüsüne kayıtlı **değil**.
> **Yöntem:** Bütün türetim ve denetim burada. Hedef dosyaya yalnız yazar *"sonuçlandı"*
> dediğinde, **tek partide**. Terk edilen rotalar silinmez.
>
> **Hedef dosya:** `Kisim_11_.../07_Eksen_Devinimi_ve_Oblikite.md` (**11.7**, iskelet hazır)
> **Karne:** `websitesi/Metin/Akademik/00_KARNE_Dogrulama_Durumu.md`
>
> **Açılış:** 6 Ağustos 2026

---

## 0. NEDEN BU DOSYA

Kısım 11'in kapsam taramasında çıktı: 11.2.8'de *"Merkür ve Venüs: Figür Ekseninin Devri"*
var, ama **Dünya'nın kendi eksen devinimi kitapta hiçbir yerde geçmiyor.** Gökbilimin en eski
hassas ölçülmüş olgusu (Hipparkhos, MÖ ~130) ve Kısım 11'in tam konusu.

**Neden şimdi mümkün:** gereken bütün parçalar artık Kısım 11'de var.

| Parça | Nerede | Statü |
|---|---|---|
| $J_2$'nin türetimi | 11.2.6, sekiz gövdede sınanmış | **[T]** |
| Düğüm/eksen presesyonu formalizmi | 11.4.3 | **[T]** |
| F5'in dikey geri-çağırması | 11.4.9, Ek M-22 | **[T]** |

Eksen devinimi bunların **kardeşidir**: yörüngeye değil **figüre** uygulanan torkun cevabı.

---

## 1. GÖZLEM TABANI

| Nicelik | Değer |
|---|---|
| Boylamda genel devinim | $\approx50{,}29''$/yıl |
| Dönem | $\mathbf{25.772}$ yıl |
| Dünya oblikitesi | $\varepsilon=23{,}44°$ |
| Dinamik elipsiklik (gözlenen) | $H=3{,}2737\times10^{-3}$ |
| Atalet çarpanı | $C/MR^2=0{,}3307$ |
| Ay/Güneş tork payı | kabaca $2{,}2:1$ (Ay baskın) |

---

## 2. ÖN DENETİM — zincirin ilk halkası tutuyor

Devinim hızı dinamik elipsiklik üzerinden gider:

$$H\equiv\frac{C-A}{C}=\frac{J_2\,MR^2}{C}=\frac{J_2}{C/MR^2}$$

Dünya için, kitabın türettiği $J_2$ ile:

$$H=\frac{1{,}0826\times10^{-3}}{0{,}3307}=\mathbf{3{,}2735\times10^{-3}}
\qquad\text{↔}\qquad \text{gözlenen } 3{,}2737\times10^{-3}$$

**Dört hanede tutuyor.** Yani zincirin ilk halkası ($J_2\to H$) sorunsuz; sıra torka ve
spin açısal momentumuna geliyor.

---

## 3. AÇIK KALEMLER

### K-1 · DEVİNİM HIZININ TÜRETİMİ *(ana iş)*

**Yapılacak:** Güneş + Ay torkunun türetilmiş $J_2$ üzerine etkisi, spin açısal momentumuna
bölünerek $25.772$ yıl **serbest parametre eklenmeden** çıkarılacak. Girdiler: $J_2$ (11.2),
$C/MR^2$ (bkz. K-2 — dikkat), $\varepsilon$, $n_\odot$, $n_{Ay}$, $M_{Ay}/M_\oplus$.

**Beklenti dürüst biçimde şu:** $J_2$ doğru olduğu için sayı da çıkacak. Bu bir **tutarlılık
kazancıdır**, yeni bir sınav değil — ve öyle sunulacak.

---

### K-2 · DÖNGÜSELLİK RİSKİ — $C/MR^2$ nereden geliyor? *(kritik, K-1'den önce)*

$H=J_2/(C/MR^2)$ bağıntısı $C/MR^2$'yi girdi olarak istiyor. Ve $0{,}3307$ değeri geleneksel
olarak **Darwin–Radau** bağıntısıyla $J_2$'den okunur. Eğer teori de onu oradan alırsa:

$$J_2 \longrightarrow C/MR^2 \longrightarrow H \longrightarrow \dot\psi$$

zincirinin girdisi ile çıktısı **aynı nicelik** olur ⟹ sınav $J_2$'yi kendisiyle sınar.

**Ve kitabın bu konuda bir kaydı var:** 11.2.6 §*"Darwin–Radau neden ana yöntem değildir"*.
O bölüm okunacak ve şu tespit edilecek: teori $C/MR^2$'yi **bağımsız** bir yerden alıyor mu
(iç yoğunluk profili? 11.4.1-(4)'ün $\phi(\rho)$ profili buna girdi verebilir), yoksa
Darwin–Radau'dan mı?

> **Bu kalem kapanmazsa K-1 bir sınav olarak sunulamaz** — yalnız "iç tutarlılık denetimi"
> olarak yazılır. Dürüstlük kaydı zorunlu.

> [!IMPORTANT]
> **KAPANDI (7 Ağustos 2026) — ve korkulan çember iki yönden birden kırıldı.**
>
> **İlk kapanış (ters yön, 11.7.4'e yazıldı):** zincir tersine çevrildi —
> $\lambda=J_2^{teori}/H^{gözlenen}=0{,}3303$, denetim bağımsız alandan (PREM, $-\%0{,}11$).
> Devinim girdi, $\lambda$ çıktı ⟹ döngüsellik yok.
>
> **İkinci kapanış (düz yön, 11.7.6'ya yazıldı):** $\lambda$ **devinime hiç dokunmadan** da
> üretilebiliyor. K-2'nin *"iç yoğunluk profili buna girdi verebilir mi"* sorusunun cevabı
> **hayır ama gerek de yok**: aranan şey $\rho(r)$ değil, izobar koşulunun **içeriye
> uzatılmasıdır.** Yüzey ölçülen alanın izobarıysa her iç seviye yüzeyi de izobardır; gereken
> ikinci malzeme gövde içi alan denklemidir ve teori onu kendisi üretir (Ek M-35, kapanmış açık
> uç: $\mathrm{tr}\,\mathsf{T}\vert_{iç}=-4\pi\mathcal{G}\rho_{madde}$). Sonuç:
> $$\lambda=\tfrac23\Bigl[1-\tfrac25\sqrt{\tfrac{5q}{2f}-1}\Bigr]\qquad\text{girdi: yalnız } f,q$$
> Dünya: $\lambda=0{,}33137$ (PREM $0{,}3307$, $+\%0{,}20$) ⟹ $\varepsilon=3{,}2662\times10^{-3}$
> ($-\%0{,}23$) ⟹ Chandler $433{,}7$ ↔ $433{,}0$ gün.
>
> ⟹ **K-1 artık "iç tutarlılık denetimi" değil, sınav olarak sunulabilir.** Ama dürüstlük kaydı
> yine zorunlu ve iki kalemdir: **(i)** üretilen bağıntı Darwin–Radau'nun kendisidir ⟹ ayrışma
> değil **ekonomi** kazanılır; **(ii)** kapanış $\lambda\lesssim0{,}2$'de çöker (Güneş $+\%105$).
> İkisi de 11.7.6'nın uyarı kutusuna yazıldı.

---

### K-3 · F5'İN PAYI VE DEJENERASYON *(kısa)*

**Ön beklenti: F5 burada ayrışan imza bırakmaz.** Gerekçe: F5'in potansiyeli **saf $P_2$**'dir
(Sınav 1, 6.6.2) ve eksen devinimi de $P_2$ torkuyla çalışır ⟹ F5'in katkısı $J_2$'ye
**dejenere** olur. 11.4.4'ün tek-parite $(R_e/r)^3$ kanalı gibi bir kurtarıcı burada yok.

**Yapılacak:** dejenerasyon açıkça gösterilecek ve $r_g$ kaydının ikizi düşülecek
(11.4.9-(a)'nın `[!IMPORTANT]` kutusu): *türetilir, ama F5 sınavı değildir.*

---

### K-4 · OBLİKİTENİN KARARLILIĞI *(ikincil, ilginç)*

Standart okumada Dünya'nın $23{,}44°$'si Ay'ın varlığıyla kararlı tutulur; Ay'sız Mars'ın
oblikitesi kaotik salınır. Teorinin 11.4.9-(e) muhasebesi bu konuda ne söylüyor?

Bağlantı noktası: **Ay $r_{geçiş}$'in dışındadır** ($6{,}25\,r_g$, 11.4.9-(a)) — yani Ay'ın
düzlemini gezegen değil kolektif kuruyor. Ay'ın oblikite üzerindeki dengeleyici rolü bu
çerçevede nasıl okunur?

> **Uyarı:** bu kalem kolayca *"her şeyi açıklıyoruz"* diline kayar. Sayı çıkmazsa
> **kapsam dışı** yazılacak, nitel anlatı eklenmeyecek.

---

## 4. ÇALIŞMA KURALLARI

- **HEDEF DOSYAYA YAZMA YASAĞI.** İş sonuçlanmadan iskelete hiçbir şey yazılmaz.
- **Menü kaydı taşımayla birlikte** — iskelet `app.js`'e eklenmemiştir.
- **Betik yok**; hesap elle ve açık.
- **Sınır alıntılama kuralı:** bir gözlemsel sınır kullanılırken hangi toleransla okunduğu
  yazılır *(yorungeler dosyasının dersi)*.
- **Dejenerasyon dürüstlüğü:** bir kanal $J_2$'ye dejenereyse "kazanılmış sınav" diye
  sunulmaz — $r_g$ kaydı emsaldir.
- Terk edilen rota silinmez.

---

## 5. SIRA

| Sıra | Kalem | Gerekçe |
|---|---|---|
| **1** | **K-2** | Döngüsellik riski; K-1'in statüsünü o belirliyor. 11.2.6 okunacak |
| 2 | **K-1** | Ana türetim |
| 3 | **K-3** | Kısa; dejenerasyon kaydı |
| 4 | **K-4** | İkincil; sayı çıkmazsa kapsam dışı |

---

## 5-B. K-2 · K-1 · K-3 YÜRÜTÜLDÜ *(6 Ağustos 2026, ikinci tur)*

### 5-B.1 K-2 — döngüsellik gerçek, ama hesabı TERS çevirmek onu kaldırıyor

11.2.6'nın kendi tablosu Dünya için $\lambda=C/MR^2=0{,}3307$'nin kaynağını *"uydu ölçümü —
**bağımsız**"* diye kaydediyor, ve gaz devlerinin aksine **model çıktısı değil.** Bu doğru bir
ayrım — ama yeterli değil, çünkü Dünya için $\lambda$'nın klasik yüksek-hassasiyetli anconu
$J_2$ **ile devinimin kendisidir** ($\lambda=J_2/H$).

⟹ **Düz kullanım döngüsel:** $\lambda$'dan devinim öngörmek, devinimden okunmuş bir sayıyı
devinimi öngörmek için kullanmaktır.

**Çözüm: zinciri ters çevirmek.** Teorinin katkısı $J_2$'yi **türetmesidir**; devinim ise
gözlemdir. O hâlde:

$$\underbrace{J_2^{\text{teori}}}_{\text{türetilmiş}}\;\Big/\;\underbrace{H^{\text{gözlenen}}}_{\text{devinimden}}\;=\;\lambda
\qquad\longrightarrow\qquad \text{sismolojiyle karşılaştır}$$

Bu **döngüsel değildir**: devinim **girdi**, çıktı Dünya'nın atalet çarpanı, ve denetim **bağımsız
bir alandan** (sismik yoğunluk profilleri) gelir. Teori, 26.000 yıllık bir kinematik gözlemi
Dünya'nın **iç yapısının ölçümüne** çeviriyor.

### 5-B.2 K-1 — zincir ve sayılar

Teorinin izobar okuması **basıklığı** verir (11.2.6, Dünya'da $+\%0{,}014$). $J_2$ ondan ve
dönme parametresinden çıkar, **yeni girdi yok:**

$$q=\frac{\omega^2R_e^3}{\mathcal{G}M}=3{,}461\times10^{-3},\qquad
J_2\simeq\tfrac23\left(f-\tfrac q2\right)=1{,}0814\times10^{-3}
\quad(\text{gözlenen }1{,}0826\times10^{-3},\ \%0{,}1)$$

**Düz yön** (denetim olarak, döngüsellik kaydıyla): $H=J_2/\lambda=3{,}2701\times10^{-3}$
(gözlenen $3{,}2737\times10^{-3}$, $-\%0{,}11$) ile

$$\dot\psi=\tfrac32\,\frac{H\cos\varepsilon}{\omega}\left[\frac{\mathcal{G}M_\odot}{a_\odot^3}
+\frac{\mathcal{G}M_{Ay}}{a_{Ay}^3}\Big(1-\tfrac32\sin^2 i_{Ay}\Big)\right]$$

| Nicelik | Hesap | Gözlenen | Sapma |
|---|---|---|---|
| Ay/Güneş tork oranı | $2{,}18$ | $\sim2{,}2$ | ✓ |
| Devinim hızı | $50{,}18''$/yıl | $50{,}39''$/yıl (luni-solar) | $-\%0{,}4$ |
| Dönem | $25.827$ yıl | $25.772$ yıl | $+\%0{,}2$ |

**Ters yön** (asıl sunulacak olan): $\lambda=J_2^{teori}/H^{gözlenen}=\mathbf{0{,}3303}$ ↔
sismik $0{,}3307$ ⟹ $\mathbf{-\%0{,}11}$

*(Birinci mertebe muamelesi: gezegen devinimi, yüksek mertebe terimler ve $e$ düzeltmeleri
alınmadı. Sapmalar bu düzeyde beklenen mertebede.)*

### 5-B.3 K-3 — F5 tam dejenere, beklendiği gibi

Eksen devinimi **$P_2$ figür terimiyle** çalışır; F5'in potansiyeli ise **saf $P_2$**'dir
(Sınav 1, 6.6.2 — $J_4$'e hiç katkı vermez). ⟹ F5'in katkısı $J_2$'ye **eklenir ve ondan
ayrılamaz.** 11.4.4'ün tek-parite $(R_e/r)^3$ kanalı gibi bir kurtarıcı burada **yok.**

$$\boxed{\;\text{Eksen devinimi bir F5 sınavı DEĞİLDİR — kanal } J_2\text{'ye tam dejenere.}\;}$$

**K-3 kapandı.** Bu, $r_g$ (11.4.9-(a)) ve şekillendirme kuralının **üçüncü örneğidir**:
türetilir, tutar, ama ayrışan imza yok.

### 5-B.4 K-4 — kapsam dışı

Oblikitenin uzun dönemli **kararlılığı** (Ay'lı Dünya ↔ Ay'sız Mars kaosu) bir kaotik dinamik
sorusudur; teorinin statik figür/düzlem makinesi ona söz söylemiyor. **Kapsam dışı yazılacak**,
nitel anlatı eklenmeyecek. *(11.4.9-(a)'nın Ay $6{,}25\,r_g$ dışarıda kaydı yerinde duruyor ve
yeterlidir.)*

---

## 5-C. ⚠ ÇERÇEVE DÜZELTMESİ — teorinin kendi devinim kaynağı var *(yazar uyarısı, üçüncü tur)*

Yazar: *"Standart bilimi unut. Bizde 4B'den 3B'ye geçen dönüş kaynaklı precession var."*
**Uyarı yerinde: §5-B'nin tamamı standart rijit-cisim muamelesiydi** — Güneş+Ay torkunun $J_2$
şişkinliğine etkisi. Teorinin kendi kaynağı başka yerdedir ve **Kısım 1'de kurulu.**

### 5-C.1 Teorinin ifadesi (birebir)

**1.4.7** — çift dönüşün 3B sonucu: *"XY bileşeni bize normal bir dönüş olarak görünür; ZW
bileşeni ise görünür dönüşün eksenini … periyodik olarak modüle eder."* Ve devinim hızı
**$\omega_2$'nin büyüklüğüne bağlıdır** (*"$\omega_2$ büyüdükçe koninin taranma hızı artar"*).

**1.4.10** — *"Evrenakı teorisine göre devinimli dönme, **dış bir kuvvetin veya eksen
kaçıklığının eseri değil**, dördüncü boyutu (W eksenini) içeren dönüş bileşeninin doğal
sonucudur."* Ve: *"Gök cisimlerinde ve nükleonlarda gözlemlediğimiz … yalpalamaların
(precession) sırrı buradadır."*

**1.4.11** — üçüncü izdüşüm imzası: *"bir bileşeni W'ye taşmışsa görünür dönme ekseni sabit
kalamaz."*

**1.4.9** — ve teorinin klasik mekanizmaya itirazı: aşağı yönlü bir kuvvetin *"nedensellik
gösterilmeden 90 derece yana sapıp"* koni çizdirmesi.

⟹ **Teoride devinim içkindir; dış tork gerektirmez.** Gözlenen hızdan doğrudan W-bileşeni
okunur:

| Gövde | $\omega_{spin}$ (s⁻¹) | $\omega_{devinim}$ (s⁻¹) | $\omega_2/\omega_1$ |
|---|---|---|---|
| Dünya | $7{,}292\times10^{-5}$ | $7{,}726\times10^{-12}$ | $\mathbf{1{,}06\times10^{-7}}$ |
| Mars | $7{,}088\times10^{-5}$ | $1{,}164\times10^{-12}$ | $\mathbf{1{,}64\times10^{-8}}$ |

### 5-C.2 Ve buradan **teorinin kendi iddiasına ilk nicel sınır** çıkıyor

İki gövdenin **tork ortamı çok farklıdır** — Dünya'da Ay baskındır (Güneş'in $2{,}18$ katı),
Mars'ın büyük uydusu **yoktur** ve Güneş'ten uzaktır. İçkin bir $\omega_2$'nin bu farkı
bilmesi için hiçbir sebep yok. Tork kanalı ise tam olarak bunu öngörür:

$$\dot\psi=\tfrac32\,\frac{H\cos\varepsilon}{\omega}\left[\frac{\mathcal{G}M_\odot}{a_\odot^3}
+\frac{\mathcal{G}M_{Ay}}{a_{Ay}^3}\Big(1-\tfrac32\sin^2 i\Big)\right],\qquad H=\frac{J_2}{\lambda}$$

| | Tork hesabı | Gözlenen | Sapma |
|---|---|---|---|
| Dünya dönemi | $25.798$ yıl | $25.772$ yıl | $+\%0{,}1$ |
| Mars dönemi | $172.461$ yıl | $\sim171.000$ yıl | $+\%0{,}9$ |
| **Dünya/Mars oranı** | $\mathbf{6{,}68}$ | $\mathbf{6{,}64}$ | $\mathbf{+\%0{,}8}$ |

**Tork kanalı, tork ortamı çok farklı iki gövdede ve oranlarında yüzde-altı tutuyor.**

$$\boxed{\;\Longrightarrow\ \text{İçkin (W-bileşeni) kanalı Güneş Sistemi'nde ALT BASKINDIR: } \lesssim\%1\ \text{(bu hassasiyette).}\;}$$

### 5-C.3 Ama iddia çürütülmüyor — ve nedeni teorinin kendi sınavında

**1.4.10 ayırt edici sınavı zaten tanımlamış:** kütle-itim, manyetik alan ve **bütün dış
etkilerden yalıtılmış**, serbest dönen bir nesne. O düzenekte **tork kanalı sıfırdır** ⟹ içkin
kanal **tek sinyaldir.**

⟹ İki kanal **çelişmiyor, ayrı rejimlerde okunuyor:**

| Rejim | Baskın kanal |
|---|---|
| Güneş Sistemi gövdeleri (tork ortamı var) | **tork** — içkin pay $\lesssim\%1$ |
| Yalıtılmış serbest dönen cisim | **içkin** — tek kanal, ve sınav budur |

*(Sınav deney fazına aittir — **T-9**, yazarın planlı fazı. Burada yalnız kaydı düşülür;
sıradaki iş olarak önerilmez.)*

### 5-C.4 Ve teorinin tork kanalına katkısı ayrıca var

Tork hesabının girdisi $J_2$'dir ve **teori onu türetir** (izobar okuması, 11.2.6, Dünya'da
$+\%0{,}014$): $J_2=\tfrac23(f-\tfrac q2)=1{,}0814\times10^{-3}$, gözlenen $1{,}0826\times10^{-3}$.
Yani teori tork kanalını gözlemden **ödünç almıyor**, kendi figüründen besliyor.

$\lambda$ ise dış girdidir ve Dünya'daki anconu devinimin kendisini içerir ⟹ **düz kullanım
döngüsel** (§5-B.1). Döngüsel olmayan kullanım **ters yöndedir:**
$\lambda=J_2^{teori}/H^{gözlenen}=0{,}3303$ ↔ sismik $0{,}3307$ ($-\%0{,}11$).

### 5-C.5 Bölümün yeni şekli

Bölüm artık **iki kanallı** yazılacak, ve çekirdeği §5-C.2'nin sınırıdır — bu, **teorinin kendi
iddiasına konulmuş ilk nicel sınırdır** ve kitapta yok.

---

## 6. İZİN BEKLEYEN KALEMLER

| # | İçerik | Kayıt |
|---|---|---|
| **İ-0** | **Teorinin kendi devinim kaynağı:** içkin, W-bileşeninin 3B izdüşümü; dış tork gerektirmez (1.4.7/1.4.9/1.4.10/1.4.11) | ⚠ **ÇEKİRDEK — bölüm bununla açılacak.** Kısım 1 kurulu ama Kısım 11'e hiç bağlanmamış |
| **İ-1** | **İçkin kanala ilk nicel sınır: $\lesssim\%1$** (§5-C.2) — Dünya ve Mars, tork ortamları çok farklı, tork kanalı ikisinde ve oranlarında yüzde-altı tutuyor | ⚠ **Asıl kazanç.** Teorinin **kendi iddiasına** konulmuş ilk sınır; kitapta yok |
| **İ-2** | **İki rejim ayrımı:** tork ortamında tork baskın · **yalıtılmış cisimde içkin tek kanal** ⟹ 1.4.10'un sınavı ayrıştırıcıdır | Sınav **T-9**'a ait; yalnız kaydı düşülür |
| **İ-3** | Gözlenen hızdan okunan $\omega_2/\omega_1$: Dünya $1{,}06\times10^{-7}$ · Mars $1{,}64\times10^{-8}$ | Üst sınır okuması ($\lesssim\%1$ ile ölçeklenir) |
| **İ-4** | Tork kanalının girdisi **teoriden**: $J_2=\tfrac23(f-\tfrac q2)=1{,}0814\times10^{-3}$ | Teori kanalı gözlemden ödünç almıyor |
| **İ-5** | **Ters zincir:** $J_2^{teori}/H^{gözlenen}=0{,}3303$ ↔ sismik $0{,}3307$ | Döngüsel **değil**; devinim girdi, çıktı iç yapı |
| **İ-6** | Düz yön denetimi: Dünya $25.798$ yıl · Mars $172.461$ yıl · Ay/Güneş $2{,}18$ | ⚠ **$\lambda$ döngüsellik kaydıyla** — denetim, öngörü değil |
| **İ-7** | **F5 tam dejenere** — eksen devinimi F5 sınavı değildir (saf $P_2$) | ⚠ zorunlu kutu; $r_g$ emsali |
| **İ-8** | Oblikite kararlılığı **kapsam dışı** | kısa kayıt |

---

## 6-B. ✅ TAŞINDI — 11.7 yazıldı ve yayında *(6 Ağustos, dördüncü tur)*

Dosya adı içeriğe göre daraltıldı: `07_Eksen_Devinimi_ve_Oblikite.md` →
**`07_Eksen_Devinimi.md`** (oblikite kapsam dışı kaldı). Başlık:
**"Eksen Devinimi: İçkin Kanal ve Tork Kanalı."**

| Alt bölüm | İçerik | Kalem |
|---|---|---|
| 11.7.0 | Gözlem; ve boşluğun bir **bağlanmama** sorunu olduğu kaydı | — |
| **11.7.1** | **Teorinin nasıl işlediği** — 4B'de dönüş düzlemdedir; $XY$ görünür dönüş, $ZW$ ekseni modüle eder; bileşke **devinim**. Kuvvet gerekmez, **kinematik**. Klasik jiroskop anlatısıyla yapısal fark (1.4.9) | **İ-0** |
| 11.7.2 | Gözlenen hızdan $\omega_2/\omega_1$: Dünya $1{,}06\times10^{-7}$ · Mars $1{,}64\times10^{-8}$ | İ-3 |
| **11.7.3** | **Çekirdek:** tork ortamı bir mertebe farklı iki gövde; tork kanalı ikisinde ve **oranlarında** yüzde-altı ⟹ **içkin pay $\lesssim\%1$**. "Tesadüf" okumasının neden tutmadığı da yazıldı | **İ-1** |
| 11.7.4 | Tork kanalının girdisi **teoriden** ($J_2=\tfrac23(f-\tfrac q2)$); $\lambda$ döngüsellik uyarısı; **ters zincir** $0{,}3303$ ↔ sismik $0{,}3307$ | İ-4, İ-5, İ-6 |
| 11.7.5 | **F5 tam dejenere** — saf $P_2$; $r_g$ emsali | İ-7 |
| 11.7.6 | Bilanço + **iki rejim tablosu** + kapsam dışı + üç açık kalem | İ-2, İ-8 |

**Sınırın $\lambda$ döngüselliğinden etkilenmediği ayrıca yazıldı:** sınır iki gövde arasındaki
**orana** dayanıyor, $\lambda$'ların mutlak değerine değil.

**`app.js`:** 11.7 kaydedildi; Özet → **11.8**, Kaynakça → **11.9**.
**Kaynakçaya üç kalem** (50–52): IAU 2000 devinim nicelikleri · PREM (sismik $\lambda$ —
ters zincirin bağımsız denetimi) · Konopliv ve ark. 2011 (Mars, ayırt edici ikinci gövde).
Teorinin devinim kaynağı **kaynakça dışı** olarak işaretlendi (Kısım 1 §1.4.3/7/9/10/11).

### 6-B.1 Dosyanın statüsü

**İşi bitti.** Dört kalem kapandı (K-1…K-4), dokuz kalem taşındı. Kitaba devredilen açık
kalemler: **11.7-i** (sınırın sıkılaştırılması) · **11.7-ii** ($\omega_2/\omega_1$ bir yasaya
bağlanabilir mi — 11.3.7-(b)'nin biriktirme sorusuyla akraba) · **11.7-iii** (gövde
topluluğuna genişletme). Ayırt edici sınav **Kısım V'in deney programına** ait olarak kaydedildi.

---

## 6-C. 🔓 DOSYA YENİDEN AÇILDI — GALAKTİK WARP HATTI *(yazar hipotezi, 6 Ağustos beşinci tur)*

**Yazar hipotezi:** *"Samanyolu warpının presesyondan kaynaklandığını düşünüyorum. Warp dönemi
ile karadelik presesyonunu kıyasla. Bizim teorimiz bağlamında precession yapabilmelidir.
Ek bilgi: kütle-spin dönüşünde zarf faktörümüz vardı, precessionda aynı zarf yapısından
etkileniyor olmalı."*

Hipotez **iki parçaya ayrıldı** ve biri öldü, biri yaşadı. Yazar ikinci okumayı onayladı:
*"warpın galaktik düzeyde olmasını onaylıyorum."*

### 6-C.1 ÖLÜ PARÇA — warp ← Sgr A*'ın presesyonu · iki bağımsız eleme

**(i) Hız $3{,}9\times10^{6}$ kat uyuşmuyor.**

| Nicelik | Değer |
|---|---|
| Warp presesyonu ($13$ km/s/kpc, 11.4.9) | $\omega=4{,}21\times10^{-16}$ s⁻¹ ⟹ **473 Myr** |
| *(Gaia, Poggio ve ark. 2020: $10{,}9$ km/s/kpc)* | *566 Myr* |
| Sgr A* ufuk dönüşü ($M=4{,}15\times10^6M_\odot$, $a^*=0{,}9$; $\mathcal{G}M/c^3=20{,}4$ s) | $\Omega_H=1{,}53\times10^{-2}$ s⁻¹ ⟹ $410$ **s** |
| $\omega_2/\omega_1$ **evrensel** olsaydı (Dünya'nın $1{,}06\times10^{-7}$'si) | BH devinimi $\approx\mathbf{123}$ **yıl** |

Warp dönemini tutması için gereken: $\omega_2/\omega_1|_{SgrA^*}=2{,}75\times10^{-14}$ —
Dünya'nın $2{,}6\times10^{-7}$'si.

**(ii) Ve asıl eleyen: kuplaj yok — $2\times10^{-19}$.** Bu $\omega_2$'den **tamamen bağımsızdır**
ve doğrudan hâli tek başına bitirir. BH spininin uzaktaki diske çerçeve-sürüklenme torku
$\propto J/r^3$:

$$J_{SgrA^*}=a^*\frac{\mathcal{G}M^2}{c}=1{,}36\times10^{55}\ \mathrm{kg\,m^2/s}
\quad\Longrightarrow\quad
\Omega_{LT}(20\,\mathrm{kpc})=\frac{2\mathcal{G}J}{c^2r^3}=8{,}6\times10^{-35}\ \mathrm{s^{-1}}$$

$$\frac{\Omega_{LT}}{\omega_{warp}}=2\times10^{-19}$$

Kütle tarafı da aynı yönde: 20 kpc'de kapsanan kütle $\approx2{,}3\times10^{11}M_\odot$,
Sgr A* onun $1{,}8\times10^{-5}$'i. ⟹ **Karadelik doğru hızda dönse bile dış diski eğemez.**

### 6-C.2 ✅ YAŞAYAN PARÇA — warp = **galaksinin kendi** W-imzası *(yazar onayladı)*

Warp, BH'nin sürüklemesi değil; aynı 4B yapının **kardeş izdüşümü.** BH bir *neden* değil, bir
*akraba*. Böylece kuplaj sorunu **tamamen kalkıyor** — sürükleyen bir şey yok.

$$\frac{\omega_2}{\omega_1}\bigg|_{galaksi}=\frac{\omega_{warp}}{\Omega(20\,\mathrm{kpc})}
=\frac{4{,}21\times10^{-16}}{3{,}57\times10^{-16}}=\mathbf{1{,}18}$$

**Mertebe bir — ayarlanmış küçük bir sayı değil.** Teorinin dilinde: **izokliniğe yakın çift
dönüş**, yani en doğal hâl. Karşılaştırma için Dünya $1{,}06\times10^{-7}$, Mars $1{,}64\times10^{-8}$.

**Ve üçüncü bir destek var, ve bu güçlü: warp YAYGINDIR.** Kenarı görünen sarmalların büyük
çoğunluğu warp taşır. Dış-tork açıklamaları her galaksi için ayrı bir tork kaynağı gerektirir;
**içkin bir W-bileşeni yaygınlığı kendiliğinden verir.**

> **Bu hesap standart çerçevede yapılamaz** (yazar kaydı): $\omega_2$ diye bir nicelik orada
> yoktur, dolayısıyla "warp presesyonu / dönüş hızı" oranı bir **anlam** taşımaz. Oran
> teoriye özgüdür.

### 6-C.3 ⚠ YAŞAYAN PARÇANIN KENDİ SORUNU — $\omega_1$ tanımsız

**Galaksi rijit cisim değil.** "Galaksinin $\omega_1$'i" tanımlı değil:

| Yarıçap | $\Omega$ | $\omega_{warp}/\Omega$ |
|---|---|---|
| $8{,}2$ kpc | $26{,}8$ km/s/kpc | $0{,}48$ |
| $20$ kpc | $11{,}0$ km/s/kpc | $\mathbf{1{,}18}$ |

⟹ $1{,}18$ **yarıçapa bağlı**, dolayısıyla o kadar temiz değil. Rijit cisimlerde (Dünya, Mars)
soru yok; galakside var ve **teorinin cevaplaması gerekiyor: diferansiyel dönen bir yapıda W
hangi $\omega_1$ ile eşleşir?**

### 6-C.4 Zarf/doygunluk ipucu — yönü doğru, kapatamıyor

Yazarın zarf ipucunu teorinin kendi kayıtları **destekliyor**:

| Kayıt | Ne diyor |
|---|---|
| 11.3.6 | Karadelikler **tavan doğrusuna yaslanır**; *"tavanı dolduran tek sınıf"* |
| M-40 | Ufukta $\xi\to1$ — ortam **neredeyse tam eş-dönüşte** |
| 11.3.7 | $\phi\to1$, kafes **kilitli** |

⟹ 3B dönüşü **doygun** bir cisimde W'ye taşacak pay doğal olarak kısılır. Gereken sıralama tam bu:

$$\text{galaksi } O(1)\ \gg\ \text{gezegen } 10^{-7}\ \gg\ \text{karadelik } 10^{-14}$$

**Ama kapatılamadı — ve uydurulmayacak.** Gereken yayılım **14 mertebe**, elde **iki nokta** var.
Yükleme/tavan oranı $898$ denendi: $898^2\Rightarrow1{,}2\times10^{-6}$, gerekense
$2{,}6\times10^{-7}$ — **4,8 kat uzak.** İki noktaya kuvvet uydurmak türetim değildir.

⟹ **11.7-ii artık boş bir soru değil, fiziksel adayı olan bir soru:** doygunluk.

### 6-C.5 Yeni kalemler

| # | Kalem | Ağırlık |
|---|---|---|
| **W-1** | **Warp RİJİT mi preses eder, DİFERANSİYEL mi?** Tek $\omega_2$ ⟹ yarıçaptan bağımsız tek hız; bükülme kipi / dış tork ⟹ yarıçapa bağlı sarılma. **Ayırt edici, ve mevcut veriyle sınanabilir** | **kısa ve belirleyici** |
| **W-2** | Diferansiyel dönen yapıda W hangi $\omega_1$ ile eşleşir? (§6-C.3) | kavramsal, blokaj |
| **W-3** | Doygunluk ölçeklemesi (= 11.7-ii, adayı belli) | ağır |
| **W-4** | **Fatura denetimi:** 11.4.9 şu an *"warpın kaynağı… teorinin kapsamı dışındadır"* diyor ve F5'in payını $\%1$–$3$ hesaplıyor. Bu hat tutarsa o kayıt **revize edilir** — bozdurulmuş bir iddia var mı? | denetim, taşımadan önce |
| **W-5** | Warp yaygınlığının nicelleştirilmesi (sarmallarda warp kesri) — içkin okumanın en güçlü desteği | orta |

---

## 6-D. ✅ W-1 YÜRÜTÜLDÜ — **WARP RİJİT PRESES EDİYOR** *(literatür taraması, altıncı tur)*

Yazar izniyle literatür tarandı (arXiv). Üç bağımsız kaynak aynı yere çıkıyor.

### 6-D.1 Gözlemsel durum — ve kitaptaki sayı bayat

| Kaynak | Değer | Not |
|---|---|---|
| **11.4.9'un kullandığı** | $13$ km/s/kpc | ⚠ **BAYAT** |
| Poggio ve ark. 2020 (Gaia DR2) | $10{,}86$ km/s/kpc | **itiraz edildi** |
| **Chrobáková & López-Corredoira 2021** | $\beta=4^{+6}_{-4}$ | *"A Case against a Significant Detection of Precession"* — presesyonsuz warpı **dışlamıyor** |
| **Zhou ve ark. 2024** (Gaia DR3 Cepheid) | $4{,}9\pm1{,}6$ @ 13 kpc | *"low precession rate"* |
| **2025, Cepheid (en güncel)** | $\mathbf{4{,}86\pm0{,}88\pm2{,}14}$ | **"nearly uniform … beyond 12.5 kpc"** |

$$\omega_{warp}=1{,}575\times10^{-16}\ \mathrm{s^{-1}}\qquad\Longrightarrow\qquad \text{dönem}=\mathbf{1{,}26\ Gyr}$$

### 6-D.2 ✅ W-1'İN CEVABI: RİJİT — ve bu tam olarak aradığımız ayrım

2025 çalışmasının kapalı biçimi (aynen):

$$Z_w(t)=0{,}00019\,R^{3{,}08}\sin\!\big(\varphi-(3{,}87R-41{,}79+4{,}86\,t)\big)$$

**Zaman terimi $4{,}86\,t$'dir ve $R$ İÇERMEZ.** Yani düğüm çizgisi yarıçapla bükülüyor
($3{,}87R$, öncü sarmal) ama **bütün desen tek ve aynı hızla preses ediyor** — 12,5 kpc'nin
ötesinde *"nearly uniform."*

$$\boxed{\;\text{Warp RİJİT preses eder: yarıçaptan bağımsız TEK }\omega_2.\;}$$

**W-1'in iki dalından teorinin dalı çıktı.** §6-C.5'te kurulan ayrım şuydu: tek $\omega_2$ ⟹
rijit; bükülme kipi / dış tork ⟹ diferansiyel sarılma. **Gözlem rijit diyor.**

### 6-D.3 Ve rijitlik standart çerçevede **bir sorundur** — teorimizde değil

Bu, gözlemin teoriyi desteklediği asıl yer. **Sarılma (winding) problemi** literatürde adıyla
kayıtlı: diferansiyel dönen bir diskte warp **sarılıp yok olur.** Ideta ve ark. (1999, MNRAS)
aynen:

> *"the warping in the **oblate halo continues to wind up, and finally disappears.** … for the
> prolate halo model … the warping persisted … by **retaining the alignment of the line of
> nodes**."*

Yani standart çerçevede rijitliği ayakta tutmak için **haleye özel bir biçim** (prolat) ya da
başka bir düzenek gerekiyor — **ayarlanmış bir çözüm.**

**Teoride ise rijitlik bedavadır:** $\omega_2$ galaksinin 4B dönüş yapısının **tek** bir
niceliğidir; yarıçapa göre değişmesi için bir sebep yoktur. Sarılma problemi doğmaz, çünkü
preses eden şey diskin malzemesi değil, **kesitimizin arakesitidir** (11.7.1).

$$\text{Standart: rijitlik AÇIKLANMASI GEREKEN bir şey}\qquad\text{Teoride: rijitlik VARSAYILAN}$$

### 6-D.4 İki kitap düzeltmesi — ve biri teorinin lehine

**(a) 11.4.9'un $13$ km/s/kpc'si bayat** ⟹ güncel $4{,}86$.

**(b) Ve F5'in warp payı ÜÇE KATLIYOR.** 11.4.9 F5'in katkısını $0{,}15$–$0{,}41$ km/s/kpc
hesaplıyor ve *"payı %1–3'tür"* diyor — o oran $13$'e karşıydı:

| $\mathcal{A}$ | F5'in katkısı | $13$ üzerinden (kitap) | **$4{,}86$ üzerinden (güncel)** |
|---|---|---|---|
| $0{,}25$ | $0{,}15$ km/s/kpc | %1,2 | **%3,1** |
| $0{,}70$ | $0{,}41$ km/s/kpc | %3,2 | **%8,4** |

⟹ **F5'in warp payı %1–3 değil, %3–8.** Kitabın kendi hesabı, güncel gözlemle **daha güçlü**
hâle geliyor. *(Ve 11.4.9'un warp bastırma kolu da aynı yönde etkilenir — W-4'te denetlenecek.)*

### 6-D.5 Ölü parça büsbütün ölü

Güncellenen oranla Sgr A* hattı **daha da** kötüleşiyor: warp $1{,}26$ Gyr ↔ evrensel
$\omega_2/\omega_1$ ile BH devinimi $123$ yıl ⟹ oran $\mathbf{1{,}0\times10^{7}}$ (önce
$3{,}9\times10^6$). Tutması için gereken $\omega_2/\omega_1=1{,}03\times10^{-14}$. Ve kuplaj
elemesi ($2\times10^{-19}$) hiç değişmedi. **Kapandı.**

### 6-D.6 ⚠ Ve dürüst bir çatlak: düğüm çizgisinin BÜKÜLMESİ

Saf bir global $\omega_2$ **rijit presesyonu** verir, ama düğüm çizgisinin yarıçapla
**bükülmesini** ($3{,}87R$, öncü sarmal) **kendiliğinden vermez** — o statik bir radyal desendir
ve ek bir kaynak ister.

**Teori-içi aday var** ve uydurma değil: 11.4.9'un $\lambda_{etkin}=\frac{d\ln v_c}{d\ln R}
+\frac{\mathcal{A}}{2}\left(\frac{R}{h_z}\right)^2$'si **yarıçapla değişir** ($\mathcal{A}(R)$ ve
$h_z(R)$ üzerinden). Radyal olarak değişen bir kilit sertliği, denge düzleminin yarıçapla
**bükülmüş** olmasını doğal biçimde verebilir. Bu, 11.4.9'un zaten kayıtlı açık kalemi
**11.4-vi**'ya ($\mathcal{A}(R)$ ve $g(z)$) doğrudan bağlanır.

**Kalem W-6 olarak açıldı.** Bükülme türetilmeden hat "tam" sayılmayacak.

### 6-D.7 Bilanço

| Kalem | Sonuç |
|---|---|
| **W-1** rijit mi diferansiyel mi | ✅ **RİJİT** — teorinin dalı |
| Rijitliğin standart çerçevedeki statüsü | ✅ **Sorun** (sarılma problemi; prolat hale gerekiyor) — teoride bedava |
| **W-4** fatura | ⚠ **iki düzeltme çıktı:** $13\to4{,}86$; F5 payı %1–3 $\to$ **%3–8** |
| $\omega_2/\omega_1$ büyüklüğü | $0{,}28$–$0{,}55$ (12,5–25 kpc) — mertebe bir ✓, ama $\Omega$ yarıçapa bağlı ⟹ **W-2 açık** |
| **W-6** düğüm çizgisi bükülmesi | ⬜ **yeni** — teori-içi adayı var (11.4-vi'nın $\lambda_{etkin}(R)$'si) |
| Sgr A* doğrudan hattı | ❌ kapandı, $10^7$ ve $2\times10^{-19}$ |

> **Hattın statüsü: rijitlik sınavı geçildi.** Yapısal olarak teori standart çerçevenin
> ayarlanmış çözümüne ihtiyaç duymuyor. Kalan iki iş **büyüklük** (W-2) ve **bükülme** (W-6);
> ikisi de kavramsal, ve ikisinin de teori-içi adayı var.

---

## 6-E. ⚠ V-9 · BENİM KUPLAJ ELEMEM VİRÜSTÜ — 3.8.7 zaten kanalı kurmuş *(yedinci tur)*

Yazar 3.8.7'yi ("Galaksinin Kanat Çırpışı") gösterdi. **Teori warpın tam hesabını zaten
taşıyor, ve mekanizması benim §6-C.1'de elediğim şey.** Elememin gerekçesi yanlış kanaldı.

### 6-E.1 Hatam

§6-C.1(ii)'de kuplajı **çerçeve-sürüklenme** ile ölçtüm ($\Omega_{LT}=2\mathcal{G}J/c^2r^3
=8{,}6\times10^{-35}$, warpın $2\times10^{-19}$'u) ve *"karadelik dış diski eğemez"* dedim.

**3.8.7 kuplajı oradan almıyor.** Aynen:

> *"Merkez karadeliğin devinimi ekvator düzlemini sallıyorsa (3.8.6), bu sallanma diskin her
> yarıçapına aynı anda ulaşamaz; **akışkan boyunca dalga olarak dışa yayılır.** İç disk,
> motorun kavramasının mutlak olduğu bölgede sallanmayı neredeyse anında izler… Dışa gidildikçe
> kavrama zayıflar ve iletim gecikir."*

⟹ Kanal **ortamın kendisidir** — eğilme dalgası, çekimsel tork değil. Ben standart fiziğin
kanalını ölçüp teorinin kanalını elemiş oldum. **V-9: doğru soruya yanlış kanalla cevap.**

$$\boxed{\;\text{§6-C.1(ii)'nin } 2\times10^{-19} \text{ elemesi GERİ ÇEKİLDİ.}\;}$$

*(§6-C.1(i)'in **hız** elemesi geri çekilmiyor — o hâlâ geçerli bir gereklilik ve §6-E.3'te
karşılanıyor.)*

### 6-E.2 Ve 3.8.7 benim "yaşayan parça"mdan DAHA İYİ — çünkü bükülmeyi de veriyor

İki okuma yarışıyordu:

| Okuma | Rijit presesyon | **Düğüm çizgisi bükülmesi** ($3{,}87R$) |
|---|---|---|
| Benim §6-C.2: galaksinin **kendi** global $\omega_2$'si | ✅ verir | ❌ **vermez** (W-6 çatlağı) |
| **3.8.7: merkez motor + gecikmeli iletim** | ✅ verir (tek tempo) | ✅ **verir** — gecikme yarıçapla arttığı için faz kayması radyal desen kurar |

⟹ **3.8.7'nin okuması üstün, ve W-6 kitapta zaten cevaplı.** Benim global-$\omega_2$ okumam
gereksiz; onu terk ediyorum. *(Terk edilen rota silinmez — §6-C.2 süreç kaydı olarak kalır.)*

**Ve iki gözlem birlikte tam bu mekanizmanın imzası:** tek tempo (rijit) + statik radyal bükülme
(gecikme deseni). 2025 verisi ikisini bir arada veriyor.

> **⚠ İşaret denetimi gerekiyor.** 2025 modeli bükülmeyi **öncü** (leading) sarmal olarak
> tarif ediyor ($\varphi=3{,}87R+$sabit ⟹ büyük $R$'de büyük $\varphi$). Saf gecikme ise dış
> bölgeyi **geride** (trailing) bırakır. İkisi zıt olabilir — ya da düğüm çizgisi geometrisinde
> işaret dönüyordur. **Kalem W-6a: bu işaret çözülmeden bükülme "açıklandı" sayılmayacak.**

### 6-E.3 §6-C.1(i)'in hız gerekliliği — ve 3.8.8(iii)'ün çapasıyla ilk kez sayı

Hız elemesi şunu istiyordu: warp temposu merkez motorun temposuysa,
$\omega_2/\omega_1|_{SgrA^*}=1{,}03\times10^{-14}$ olmak zorunda (Dünya'nın $10^{-7}$'sinin
$10^{-7}$'si). **Yazarın zarf ipucu tam buraya oturuyor** — ve kitap zaten çapasını önermiş:

> **3.8.8(iii):** *"merkez karadeliğin içsel devinim frekansının… tahmini — burada
> **PSR B1828-11**'in ölçülmüş devinim çevrimi (yüzlerce gün; Stairs ve ark., 2000),
> **kütle-devinim ölçekleme yasasının ilk gözlemsel çapası** olarak kullanılabilir."*

Çapa hesaplandı ($P_{spin}=0{,}405$ s, $P_{devinim}\approx500$ gün):

| Gövde | 11.3'ün **zarf sınıfı** | $\omega_2/\omega_1$ |
|---|---|---|
| Dünya | **rijit zarf** | $1{,}06\times10^{-7}$ |
| Mars | **rijit zarf** | $1{,}64\times10^{-8}$ |
| **PSR B1828-11** | **zarfını fırlatmış** | $\mathbf{9{,}4\times10^{-9}}$ |
| Sgr A* | **zarf yok — tavanın kendisi** | *(gerekli)* $\mathbf{1{,}0\times10^{-14}}$ |

**Ve desen yazarın öngördüğü gibi çıkıyor:**

- **Zarf taşıyan/taşımış üç gövde $11$ kat içinde kümeleniyor** ($10^{-7}$–$10^{-8}$ bandı)
- **Tavandaki cisim $9\times10^{5}$ kat aşağıda**

⟹ 11.3'ün zarf merdiveni (rijit → plazma → fırlatmış → **tavan**) devinimde de görünüyor: zarf
kaybı bandı yavaşça aşağı çekiyor, **tavan ise uçurum yapıyor.** Ve teorinin kendi kayıtları
uçurumu bekliyor: BH tavanda (11.3.6), $\xi\to1$ (M-40), kafes kilitli ($\phi\to1$) ⟹ 3B dönüşü
**doygun**, W'ye taşacak pay kısılmış.

> **Dürüst sınır.** Dört nokta, ve dördüncüsü **ölçüm değil gereklilik.** $10^{-9}$ ile
> $10^{-14}$ arasında **ara nokta yok** (plazma zarflı sınıf — yıldızlar — eksik: Güneş'in eksen
> devinimi ölçülü değil). Dolayısıyla bu bir **desen**, türetilmiş yasa değil. PSR B1828-11'in
> devinim çevrimi de tartışmalıdır (250/500/1000 gün harmonikleri). **Yasa uydurulmayacak.**

### 6-E.4 Üç kitap düzeltmesi

| # | Nerede | Ne |
|---|---|---|
| **D-1** | **3.8.7** | $10{,}9$ km/s/kpc → **$4{,}86$** (2025 Cepheid). *Bölüm zaten Chrobáková itirazını karşı kayıt olarak taşıyor — güncelleme o kaydı güçlendirir.* |
| **D-2** | **11.4.9** | $13$ km/s/kpc → **$4{,}86$** |
| **D-3** | **11.4.9** | F5'in warp payı **%1–3 → %3–8** (aynı $0{,}15$–$0{,}41$ km/s/kpc katkısı, güncel taban) — **teorinin lehine** |

**Ve D-4 (kazanç):** rijitlik gözlemsel olarak **doğrulandı** (2025: *"nearly uniform beyond
12.5 kpc"*). 3.8.7 *"sarılma problemi hiç doğmaz"* diyor; artık bunun arkasında **ölçüm** var.
3.8.8'in 1. öngörüsü (devinimin **kalıcılığı**) de aynı yönde besleniyor.

### 6-E.5 Kalan kalemler — ve hepsi kitapta zaten kayıtlı

| Kalem | Durum |
|---|---|
| **W-1** rijitlik | ✅ **geçildi** (§6-D) |
| **W-4** fatura | ✅ üç düzeltme + bir kazanç (§6-E.4) |
| **W-6** bükülme | ✅ **mekanizma 3.8.7'de var** (gecikmeli iletim) · ⚠ **W-6a: işaret denetimi** açık |
| **W-2** büyüklük ($\omega_1$ tanımı) | 🚫 **gereksizleşti** — global-$\omega_2$ okuması terk edildi; 3.8.7'de $\omega_1$ merkez motorun kendi dönüşü |
| **W-3 / 11.7-ii** zarf ölçeklemesi | ⬜ **desen kuruldu, yasa yok** (§6-E.3) — 3.8.8(iii)'ün istediği iş |
| Sgr A* kuplajı | ✅ **elemem geri çekildi** (V-9) |
| Nicel türetim (CFD, $\eta_E$) | ⬜ **3.8.8(iv-i)** olarak zaten kayıtlı — bu dosyanın işi değil |

---

## 6-F. ❌ W-6a OLUMSUZ — bükülmenin işareti naif okumayla ZIT *(sekizinci tur)*

### 6-F.1 Hesap

2025 modelinin düğüm çizgisi ($Z_w=0$):

$$\varphi_{LON}(R,t)=3{,}87R-41{,}79+4{,}86\,t\qquad[\text{derece},\ R\ \text{kpc}]$$

| $R$ (kpc) | $12{,}5$ | $15$ | $20$ | $25$ |
|---|---|---|---|---|
| $\varphi_{LON}$ | $6{,}6°$ | $16{,}3°$ | $35{,}6°$ | $55{,}0°$ |

$\varphi_{LON}$ hem $R$ ile hem $t$ ile **artıyor** (prograd) ⟹ dış bölge **önde** = **öncü**
(leading) sarmal. *(Makalenin kendi ifadesi de "leading spiral pattern.")*

**Saf merkez-dışa gecikmeli iletim ne verir?** Dış bölge, merkezin $t-\tau(R)$ anındaki
yönelimini gösterir ve $\tau$ yarıçapla artar:

$$\varphi_{LON}(R,t)=\varphi_0+\omega_p t-\omega_p\tau(R)\qquad\Longrightarrow\qquad R\ \text{ile AZALIR}=\textbf{artçı}$$

$$\boxed{\;\text{İŞARETLER ZIT. Gözlem öncü, naif gecikme okuması artçı verir.}\;}$$

### 6-F.2 Ve dalga okuması aynı yere çıkıyor

Eğilme dalgasının faz yapısı:

| Faz | Düğüm çizgisi | Yayılım |
|---|---|---|
| $\sin(m\varphi+kR-\omega t)$ | $m\varphi=\omega t-kR$ ⟹ **artçı** | **dışa** |
| $\sin(m\varphi-kR-\omega t)$ | $m\varphi=\omega t+kR$ ⟹ **öncü** | **içe** |

⟹ Gözlenen **öncü** bükülme, naif okumada **içe doğru faz yayılımına** karşılık geliyor —
3.8.7'nin **birincil** mekanizmasının (merkez→dışa) tersi yön.

### 6-F.3 Hüküm — ve çatlağın gerçek genişliği

**Çatlak gerçek ama dar. Dokunulmayanlar:**

- ✅ **S biçiminin varlığı** — bir uç kalkık, karşı uç inik: gecikme deseni bunu verir, işaretten bağımsız
- ✅ **Rijit tempo** — tek motor, tek tempo (W-1'de gözlemsel olarak doğrulandı)
- ✅ **Sarılma probleminin doğmaması** — akışkan yaprak argümanı işaretten bağımsız

**Dokunulan tek şey:** bükülmenin **radyal işareti.**

**Ve niçin bu turda çözülemez:** işaret, saf advektif gecikmeden değil **eğilme dalgasının
dağılım bağıntısından** çıkar — ortamın $\eta_E$'si, $h_z(R)$ ve kilit sertliği
$\lambda_{etkin}(R)$ ile. **O bağıntı türetilmemiştir**, ve zaten kitabın kendi açık kalemidir:

> **3.8.8(iv-i):** *"Warp devinim hızının… merkez motorun devinim frekansına bağlanan, $\eta_E$
> içeren bir **CFD modelinden nicel türetimi**."*

⟹ **W-6a bu kalemin altına devredildi.** Naif okumayla zorlamak yerine, işaretin dağılım
bağıntısından çıkması beklenecek. *Bükülme "açıklandı" sayılmayacak.*

### 6-F.4 Ve bir ihtimal kaydı — zorlamadan

Öncü bükülme naif olarak **içe** faz yayılımına işaret ediyor. 3.8.7'nin **ikincil** katkısı tam
bunu içeriyor: *"dış kenarda ortam akıntısı bükülmeye yön verir ve genliği besler; uydu
galaksilerin geçişleri de akışkan yaprağa ek dalgalar bırakır."* Dış kenardan sürülen bir desen
içe doğru yayılır ve öncü bükülme verir.

**Ama bu ikircikli:** desen dışarıdan sürülüyorsa **tempo** da dış sınırdan gelir, o zaman
*"warp temposu = merkez motorun temposu"* zayıflar. Rijit tempo merkezden, bükülme dışarıdan
gelebilir mi — **iki kaynaklı okuma** — bu **W-6b** olarak kaydedildi ve **iddia olarak ileri
sürülmeyecek.**

---

## 6-G. W-6a İLERLEDİ — çerçeve yanlıştı, ve doğru çerçeve teorinin kendi $\nu$'sü *(dokuzuncu tur)*

§6-F'de işaret çelişkisini bulmuştum. **Çelişkinin kaynağı gecikme değil, gecikmeyi
"advektif" saymamdı.** Sallanma, ortama basılıp taşınan bir *sinyal* değil — akışkan yaprağın
**kendi dikey salınıcısının zorlanmış tepkisidir.** Ve o salınıcı teoride var: 11.4.5'in
$\nu_{kol}=\sqrt{4\pi\mathcal{G}\rho}$'su.

### 6-G.1 Önce bir denetim: teorinin $\nu_{kol}$'u galaktik diski tutuyor

Bu hesap kitapta hiç yapılmamış — 11.4.5'in kolektif kuyusu Satürn halkasında kurulmuş, galaktik
diske uygulanmamış:

| | Değer |
|---|---|
| Yerel disk yoğunluğu $\rho\approx0{,}1\,M_\odot/\mathrm{pc}^3$ | $6{,}77\times10^{-21}$ kg/m³ |
| **Teorinin $\nu_{kol}=\sqrt{4\pi\mathcal{G}\rho}$'su** | $\mathbf{2{,}38\times10^{-15}}$ s⁻¹ |
| Gözlenen Güneş dikey salınımı ($\sim75$ Myr, 3.8.6) | $2{,}66\times10^{-15}$ s⁻¹ |
| **oran** | $\mathbf{0{,}90}$ |

⟹ **%10 içinde.** 11.4.5'in kuyusu, Satürn halkasından galaktik diske **serbest parametre
eklenmeden** taşınıyor ve Güneş'in yunuslama frekansını veriyor. *(Bedava denetim; kayda değer.)*

### 6-G.2 Ve zorlanmış tepki çerçevesi işaret sorununu iyi tanımlı hâle getiriyor

$$\frac{\nu_{kol}}{\omega_p}\bigg|_{G\ddot{u}ne\c{s}}=\frac{2{,}38\times10^{-15}}{1{,}575\times10^{-16}}=\mathbf{15{,}1}$$

**Güneş civarı rezonansın çok üstünde** ⟹ tepki **eş fazlı**, gecikme yok. Bu, 3.8.7'nin
*"iç disk sallanmayı neredeyse anında izler, bu yüzden iç bölgeler düz görünür"* cümlesinin
mekanik karşılığıdır — ve "kavramanın mutlak olması" değil, **sert (rezonans üstü) salınıcı**
olması.

**Rezonans nerede?** $\nu_{kol}=\omega_p$ için $\rho=\omega_p^2/4\pi\mathcal{G}
=2{,}96\times10^{-23}$ kg/m³ — yerelin $229$'da biri. Üstel disk ($\rho\propto e^{-R/h_R}$):

| $h_R$ | Rezonans yarıçapı |
|---|---|
| $2{,}2$ kpc | $20{,}2$ kpc |
| $2{,}6$ kpc | $\mathbf{22{,}3}$ kpc |
| $3{,}0$ kpc | $24{,}5$ kpc |

$$\boxed{\;\text{Rezonans } R\approx20\text{–}24\ \mathrm{kpc}\ \text{— WARP BÖLGESİNİN TAM İÇİNDE.}\;}$$

### 6-G.3 Bunun anlamı — ve niçin işaret artık dışlanmıyor

Zorlanmış sönümlü salınıcının **radyal faz profili:**

| Bölge | $\nu/\omega_p$ | Tepki fazı |
|---|---|---|
| İç disk ($R\lesssim15$ kpc) | $\gg1$ | **eş fazlı** — düz, motoru izliyor ✓ |
| **Warp bölgesi (rezonans geçişi)** | $\to1$ | **faz $90°$ süpürüyor** ⟹ dik radyal faz gradyanı = **BÜKÜLME** |
| Dış kenar | $<1$ | ters fazlı |

⟹ **Bükülme, yaprağın sert rejimden yumuşak rejime geçtiği yerde doğar** — ve tam o geçiş warp
bölgesindedir. Advektif gecikme okuması bükülmeyi *tek işaretli* bir gecikmeye zorluyordu ve
**öncü** bükülmeyi dışlıyordu; zorlanmış tepki okumasında faz gradyanının işareti **sönüme
($\eta_E$) ve geçişin hangi yönden yapıldığına** bağlıdır — dolayısıyla **öncü bükülme
dışlanmıyor.**

$$\text{§6-F'nin çelişkisi: çözülmedi ama KALDIRILDI — yanlış çerçeveden doğuyordu.}$$

**Kalan iş netleşti:** işaret, $\nu_{kol}(R)$, $\omega_p$ ve $\eta_E$ ile kurulan sönümlü
zorlanmış tepkinin faz profilinden çıkacak. Bu tam olarak **3.8.8(iv-i)**'nin istediği
$\eta_E$'li nicel modeldir — artık hangi denklemin çözüleceği de belli.

### 6-G.4 Yan kazanç: karakteristik bir yarıçap doğuyor

11.4.9 şu an *"F5 karakteristik bir warp başlangıç yarıçapı öngörmez"* diyor — ve bu doğru,
çünkü **F5 için** doğru. Ama rezonans okuması **başka bir kanaldan** karakteristik bir yarıçap
veriyor ($\nu_{kol}=\omega_p$, $\approx22$ kpc). Bu, o kapsam kaydını çürütmüyor;
**yanına ikinci bir ölçek koyuyor.** *(Warpın gözlenen başlangıcı $\sim10$–$12$ kpc; rezonans
warpın ortası-dışı. Dolayısıyla rezonans "başlangıç" değil, **bükülmenin doğduğu** yer.)*
**Kalem W-7 olarak kaydedildi** — ikisi karıştırılmayacak.

---

## 6-H. ❌ W-3 KAPANDI — desen zarf sınıfına ait, sürekli bir parametreye DEĞİL *(dokuzuncu tur)*

Yasa uydurmamak için en makul sürekli aday sınandı: **boyutsuz spin $a^*=cJ/\mathcal{G}M^2$.**

| Gövde | $a^*$ | $\omega_2/\omega_1$ |
|---|---|---|
| Mars | $2{,}09\times10^{3}$ | $1{,}64\times10^{-8}$ |
| Dünya | $7{,}38\times10^{2}$ | $1{,}06\times10^{-7}$ |
| Sgr A* | $0{,}9$ | $1{,}03\times10^{-14}$ |
| PSR B1828-11 | $9{,}0\times10^{-4}$ | $9{,}4\times10^{-9}$ |

**Monoton değil.** $a^*$ sırası Mars > Dünya ≫ Sgr A* > PSR; $\omega_2/\omega_1$ sırası
Dünya > Mars > PSR ≫ Sgr A*. **PSR ile Sgr A* $a^*$'da komşu ama $\omega_2/\omega_1$'de 5
mertebe ayrı.** ⟹ $a^*$ deseni **organize etmiyor.**

$$\boxed{\;\text{Desen sürekli bir parametreye değil, 11.3'ün ZARF SINIFINA ait görünüyor.}\;}$$

**W-3 kapandı — olumsuz, ama bilgi veren bir olumsuzluk:** aranacak yer sürekli bir spin
parametresi değil, zarfın **varlığı/yokluğu** (rijit · plazma · fırlatmış · **tavan**). Ve plazma
sınıfı hâlâ boş (Güneş'in eksen devinimi ölçülü değil), $10^{-9}$–$10^{-14}$ arasında ara nokta
yok. **Yasa 3.8.8(iii)'te bekliyor; bu turda uydurulmadı ve $a^*$ denemesi tekrar edilmesin diye
kayda geçti.**

---

## 6-I. ❌ W-6a KAPANDI — hesap yapıldı, bükülme ÇIKMIYOR · ama bir ÖNGÖRÜ doğdu *(onuncu tur)*

§6-G'de *"öncü bükülme dışlanmıyor"* demiştim. **Teorinin kendi nicelikleriyle hesaplayınca
dışlanıyor.** Geri alıyorum.

### 6-I.1 Hesap — tümüyle teori-içi

**Girdiler, hepsi teorinin kendi malı:** $\nu_{kol}=\sqrt{4\pi\mathcal{G}\rho}$ (11.4.5) ·
$\omega_p=4{,}86$ km/s/kpc (3.8.7 motoru) · $\Omega=v_c/R$ (DY-2'nin madde kolu) ·
$\eta_E\lesssim2{,}3\times10^{-11}$ Pa·s (11.4.8).

**Zorlama frekansı dönen çerçevede** ($m=1$ desen için, kinematik — ithal değil):
$\omega_f=\Omega-\omega_p$.

| $R$ (kpc) | $\nu_{kol}$ | $\omega_f$ | $\nu/\omega_f$ |
|---|---|---|---|
| $8{,}2$ | $2{,}38\times10^{-15}$ | $7{,}12\times10^{-16}$ | $3{,}35$ |
| $16$ | $5{,}32\times10^{-16}$ | $2{,}88\times10^{-16}$ | $1{,}85$ |
| $20$ | $2{,}46\times10^{-16}$ | $1{,}99\times10^{-16}$ | $1{,}24$ |
| **$22$** | $1{,}68\times10^{-16}$ | $1{,}67\times10^{-16}$ | $\mathbf{1{,}01}$ |
| $25$ | $9{,}42\times10^{-17}$ | $1{,}28\times10^{-16}$ | $0{,}74$ |

⟹ **Dikey rezonans $R\approx22$ kpc** *(§6-G'nin $\nu=\omega_p$ okuması kabaydı; doğru koşul
$\nu=\omega_f$ ve sonuç aynı yere düşüyor).*

**Faz gecikmesi:** $\tan\delta=\dfrac{2\gamma\,\omega_f}{\nu^2-\omega_f^2}$

### 6-I.2 İki bağımsız yoldan olumsuz

**(a) İşaret ters.** $\nu$ yarıçapla üstel düşer, $\omega_f$ ise $1/R$ ile — yani $\nu/\omega_f$
**monoton azalır** ve $\delta$ **monoton $0\to180°$ artar.** Zorlanmış tepki forsun *gerisinde*
kalır; prograd dönen bir zorlamada bu **dış bölgenin geride olması** demektir:

$$\boxed{\;\delta \text{ monoton artıyor}\ \Longrightarrow\ \textbf{ARTÇI (trailing)}.\ \text{Gözlem ÖNCÜ.}\;}$$

**(b) Ve biçim de yanlış: rampa değil SIÇRAMA.** Sönüm teorinin kendi $\eta_E$ sınırından:

$$\gamma=\frac{9\eta_E}{2\rho_c r_t^2}\approx1{,}5\times10^{-31}\ \mathrm{s^{-1}}
\qquad\Longrightarrow\qquad \frac{\gamma}{\nu}\approx6\times10^{-17},\qquad Q\approx8\times10^{15}$$

*(Ve bu **üst sınır**la, $\Delta v^4$ bastırması **hariç** — §9 kuralı gereği: kanal dikey,
$\Delta v$ mm/s mertebesinde, dolayısıyla gerçek $\gamma$ daha da küçük ⟹ rezonans **daha da**
keskin.)*

$Q\sim10^{16}$ ⟹ $\delta$ 22 kpc'de neredeyse **basamak fonksiyonu**: içeride $0°$, dışarıda
$180°$. Gözlenen ise **$3{,}87°$/kpc'lik düzgün rampa** (12,5→25 kpc arası toplam $\approx48°$).

$$\boxed{\;\text{Teori keskin bir } 180° \text{ dönüşü verir; gözlem düzgün bir rampa gösterir.}\;}$$

### 6-I.3 Ama bir şey ÇIKIYOR — ve o bir öngörü

Basamak fonksiyonunun kendisi **S biçimini üretiyor:** rezonansın içinde tepki eş fazlı, dışında
**ters fazlı** ⟹ diskin bir yanı yukarı, karşı yanı aşağı. Yani:

| Gözlem | Merkez-motor zorlanmış tepkisi |
|---|---|
| **S biçiminin varlığı** | ✅ **çıkıyor** — rezonanstaki faz dönüşü |
| **Rijit tempo** | ✅ çıkıyor (tek motor, tek tempo) |
| Bükülmenin **işareti** | ❌ artçı çıkıyor, gözlem öncü |
| Bükülmenin **biçimi** | ❌ sıçrama çıkıyor, gözlem rampa |

**Ve olumsuzluk bir öngörüye dönüşüyor:**

> **Ö-W1 (yeni, yanlışlanabilir):** Merkez-motor zorlanmış tepkisi, **dikey rezonans yarıçapında
> ($R\approx20$–$24$ kpc) keskin bir faz tersinmesi** dayatır — teorinin kendi $\eta_E$ sınırı
> rezonansı $Q\sim10^{16}$ yaptığı için geçiş **dar** olmak zorundadır. Warp fazı o yarıçapta
> **düzgün geçiyorsa ve tersinme yoksa**, merkez-motor zorlanmış tepkisi bükülmenin kaynağı
> olamaz. *Gaia DR4'ün dış disk faz haritası bunu doğrudan sınar.*

### 6-I.4 Hüküm ve kalan tek aday

**Bükülme merkez motordan çıkmıyor.** Teorinin içinde kalan tek aday 3.8.7'nin **ikincil**
katkısıdır (*"dış kenarda ortam akıntısı bükülmeye yön verir"*) — dış kenardan sürülen bir desen
**içe** yayılır ve **öncü** bükülme verir ✓, ve sönüm sorunu doğmaz.

**Ama bedeli açık:** desen dışarıdan sürülüyorsa **tempo** da dış sınırdan gelir ve
*"warp temposu = merkez motorun temposu"* zayıflar. **İki kaynaklı okuma** (tempo merkezden,
bükülme dışarıdan) tutarlı olabilir ama **türetilmemiştir ve iddia olarak ileri sürülmeyecektir**
(**W-6b**).

| Kalem | Sonuç |
|---|---|
| S biçiminin varlığı · rijit tempo | ✅ merkez motordan çıkıyor |
| **Bükülmenin işareti ve biçimi** | ❌ **merkez motordan ÇIKMIYOR** |
| **Ö-W1** rezonansta keskin faz tersinmesi | ✅ **yeni yanlışlanabilir öngörü** |
| W-6b iki kaynaklı okuma | ⬜ türetilmedi, ileri sürülmeyecek |

> **Yöntem kaydı.** Bu sonuç **virüs ithal edilmeden** çıkarıldı: $\nu_{kol}$ 11.4.5'in,
> $\eta_E$ 11.4.8'in, $\Omega$ DY-2'nin, $\omega_p$ 3.8.7'nin. Standart warp kipi / hale
> torku / eğilme-dalgası dağılım bağıntısı **kullanılmadı.** Olumsuzluk teorinin kendi
> nicelikleriyle çıktı — ve bu yüzden **bağlayıcıdır.**

---

## 6-J. DÖRT TAAHHÜT KURULDU — üçü tuttu, biri tutmadı, ve tutmayan işareti KAPATIYOR *(on birinci tur)*

Yazar haklı olarak uyardı: söylediklerim teorinin kesinleşmiş iddiaları değildi. Dördü tek tek
kuruldu.

### C-1 ✅ KURULDU — ve salınıcının kim olduğunu **eylemsizlik** belirliyor

Warp yüzeyi ortamın ekvator düzlemi mi, madde mi? Sorunun cevabı tartışma gerektirmiyor:

| | Yoğunluk |
|---|---|
| Ortam ($\rho_0=\rho_n/4$, M-8) | $6{,}8\times10^{16}$ kg/m³ |
| Galaktik disk maddesi | $6{,}8\times10^{-21}$ kg/m³ |
| **oran** | $\mathbf{10^{37}}$ |

$$\boxed{\;\text{Madde ortamın düzlemini SALLAYAMAZ. Ortam SÜRÜCÜ, madde SALINICI.}\;}$$

3.8.7'nin *"motorun salladığı düzlem gerçekten bir akışkan yüzeydir"* ve 11.4.9'un *"disk F5'in
geometrik sabit noktasıdır"* kayıtları bununla tam uyumlu: düzlemin **kimliği** ortamın işi,
madde ona **oturur.**

> **⚠ VE BU BENİM BİR ÖNCEKİ TURDAKİ 13 kpc SONUCUMU GEÇERSİZ KILIYOR.** Orada
> $\omega_f=2\Omega-\omega_p$ almıştım (ortamın dönüşü). **Tutarsız:** salınıcı madde olduğuna
> göre onun dönüşü $\Omega$'dır. Geri-çağırmayı maddeden ($\nu_{kol}$), dönüşü ortamdan almak
> iki ayrı cismin niceliklerini karıştırmaktır. **Doğru koşul $\omega_f=\Omega-\omega_p$ ve
> rezonans $\approx22$ kpc'de kalıyor** — §6-I'deki değer. *(13 kpc yalnız sohbette söylendi,
> hiçbir dosyaya yazılmadı.)*

### C-2 ✅ KURULDU ve DOĞRULANDI — $\nu_{kol}$ tam olarak maddenin frekansı

11.4.5 $\nu_{kol}$'u tabakanın **kendi kütle-itim kuyusundaki** dikey frekans olarak türetiyor —
yani *maddenin düzlem etrafındaki* salınımı. C-1 salınıcıyı madde yaptığına göre bu **tam
aradığımız nicelik**, ve bağımsız denetimi var:

$$\nu_{kol}=\sqrt{4\pi\mathcal{G}\rho}=2{,}38\times10^{-15}\ \mathrm{s^{-1}}
\qquad\text{↔}\qquad \text{Güneş'in gözlenen yunuslaması }2{,}66\times10^{-15}\ \ (\%10)$$

F5'in katkısı $x=\frac{\mathcal{A}\kappa_5}{4}(v_c/\sigma_z)^2\approx0{,}02$–$0{,}1$ (11.4.9)
⟹ $\nu$'yü %1–5 yükseltir, sonucu değiştirmez. **Kuruldu.**

### C-3 ❌ KURULAMADI — prograd işaret dikey kanala geçmiyor

Umut şuydu: DY-2 $\Delta v=+v$ verdiği için 11.4.8 torku **prograd** buluyor (momentum
**artırıyor**); aynı işaret dikey kanalda da geçerse $\gamma<0$ olur ve desen **öncü** çıkar.

**Geçmiyor, ve nedeni tanımsal.** Azimutal kanalda $\Delta v$ **mutlak** bir kaymadır: ortam her
yarıçapta maddeden hızlıdır, dolayısıyla itki tek yönlüdür (prograd). Dikey kanalda ise sürükleme
**bağıl** hız üzerinedir:

$$-\gamma\big(\dot z_{madde}-\dot z_{düzlem}\big)$$

Bağıl-hız sürüklemesi **tanımı gereği** bağıl hareketi söndürür ⟹ $\gamma>0$. Ortamın azimutal
olarak önde olması, maddenin düzleme göre dikey hareketine bir **yön** vermez.

### C-4 — genlik kalemi, ama C-3 düşünce işaret için işlevsiz

Ters sönümün büyüklüğü ($R^{3{,}08}$ genlik büyümesini verecek olan) ancak $\gamma<0$ olsaydı
anlamlıydı. C-3 düştüğü için bu kalem **işaret sorununa katkı vermiyor.**

---

## 6-K. YAPISAL KAPI — ve işaretin nihai hükmü

$\gamma>0$ ile:

$$\tan\delta=\frac{2\gamma\,\omega_f}{\nu^2-\omega_f^2}\qquad\Longrightarrow\qquad \delta\in[0°,180°]\ \ \textbf{her zaman}$$

$$\boxed{\;\textbf{Zorlanan bir salınıcı zorlamayı önceleyemez. ÖNCÜ bir desen TEPKİ olamaz.}\;}$$

Bu bir parametre sorunu **değil**; nedensellik. Ve üç ayrı çerçeve denendi, üçü de aynı kapıya
çarptı:

| Deneme | Sonuç |
|---|---|
| §6-F: advektif gecikme | artçı |
| §6-G/§6-I: zorlanmış tepki, $\omega_f=\Omega-\omega_p$ | artçı |
| §6-J/C-3: DY-2'nin prograd işaretini taşımak | **taşınamıyor** ⟹ artçı |

$$\Longrightarrow\ \textbf{Gözlenen ÖNCÜ bükülme, merkez motora verilen bir TEPKİ DEĞİLDİR.}$$

**Bu, teorinin kesinleşmiş kalemlerinden çıkan bağlayıcı bir sonuçtur** ve dosyanın en sağlam
olumsuz bulgusudur.

### 6-K.1 Ayakta kalanlar — ve bunlar az değil

| Bulgu | Statü |
|---|---|
| **Rijit tempo** | ✅ tek motor, tek tempo; gözlemsel olarak doğrulandı (§6-D) |
| **S biçiminin varlığı** | ✅ rezonanstaki faz dönüşünden (içeride eş fazlı, dışarıda ters fazlı) |
| **$\nu_{kol}$ galaktik diskte tutuyor** | ✅ %10, serbest parametre yok — **kitapta yapılmamış denetim** |
| **Salınıcı maddedir, ortam sürücüdür** | ✅ $10^{37}$ eylemsizlik oranıyla kesin (C-1) |
| **Ö-W1:** rezonansta ($\approx22$ kpc) keskin faz tersinmesi | ✅ yanlışlanabilir öngörü, $Q\sim10^{16}$ |
| **Bükülmenin işareti** | ❌ **merkez motordan çıkmaz — yapısal, kapalı** |
| Bükülmenin kaynağı | ⬜ tek aday 3.8.7'nin **ikincil** kanalı (dış kenar); türetilmedi |

### 6-K.2 Teoriye ne söylüyoruz

Bükülme için teorinin iki seçeneği var ve **ikisi de dürüst:**

1. **Bükülmeyi ikincil kanala vermek** (dış kenarda ortam akıntısı, komşular). Dıştan sürülen
   desen içe yayılır ve **öncü** olur ✓. Bedeli: temponun da dış sınırdan gelme riski — iki
   kaynaklı okuma türetilmeli.
2. **Bükülmeyi kapsam dışı ilan etmek.** Rijit tempo, S biçimi ve rezonans yarıçapı zaten
   kazanç; bükülmenin radyal fazı için teori söz vermez.

**İkisi arasındaki seçim yazarın.** Bu dosya hiçbirini iddia olarak yazmayacak.

---

## 6-L. ⚠ V-10 · C-3'ÜN OLUMSUZLUĞU VİRÜS KAYNAKLIYDI — geri çekiliyor *(on ikinci tur)*

Yazar uyardı: *"C-3'ün olumsuzluğu bir virüse ait olmasın."* **Haklı çıktı.**

### 6-L.1 Nasıl tanımlamışım (yanlış) ↔ nasıl tanımlanmalı

$$\text{yazdığım: } -\gamma\big(\dot z_{madde}-\dot z_{\mathbf{d\ddot{u}zlem}}\big)
\qquad\text{doğrusu: } -\gamma\big(\dot z_{madde}-\dot z_{\mathbf{ortam}}\big)$$

Kuplaj madde ile **ortam** arasındadır; düzlemi rijit bir yüzey gibi almışım. Ama ortamın
**malzemesi** düzlemi $2\Omega$ ile taşır (DY-2), madde $\Omega$ ile. **2 çarpanını üçüncü kez
çökerttim.** Sonucu: madde tam yüzeyde otursa bile bağıl dikey hız sıfır **değil.**

$$\ddot u+\gamma\dot u+\nu^2u
=\underbrace{h\,\omega_f^2\sin(\omega_f t)}_{\text{GECİKME üretir}}
+\underbrace{\gamma\,h\,\Omega\cos(\omega_f t)}_{\textbf{ÖNCÜLÜK üretir}}$$

**İki bileşen diktir.** ⟹ §6-K'nın *"zorlanan salınıcı zorlamayı önceleyemez"* kapısı yalnız
**tek bileşenli** zorlama için geçerliydi.

$$\boxed{\;\textbf{§6-K'nın "öncü desen yapısal olarak yasak" hükmü GERİ ÇEKİLDİ.}\;}$$

### 6-L.2 Fatura — ve izleyicinin boyutuna göre ayrışıyor

Öncülük terimi kazanır: $\gamma\Omega\gtrsim\omega_f^2\ \Rightarrow\
\gamma\gtrsim\omega_f^2/\Omega\approx1{,}1\times10^{-16}$ s⁻¹.

Ve 11.4.8'in Stokes biçimi + M-43 ile $\gamma\propto\dfrac{\Delta v^4}{\rho_c\,r_t}$ — yani
**izleyicinin boyutuna ters.** Halka sınırından kalibre, warp kanalının
$\Delta v\approx h\Omega\approx11$ km/s'siyle (§9 kuralı gereği açıkça yazıldı):

| İzleyici | $\rho_c r_t$ | $\gamma$ (s⁻¹) | $\gamma/$gereken | Sonuç |
|---|---|---|---|---|
| **Gaz — atomik kafes** | $4{,}0\times10^{-8}$ | $2{,}7\times10^{-5}$ | $\mathbf{2{,}4\times10^{11}}$ | ortama **sıkı kilitli** |
| **Toz tanesi** (0,1 µm, silikat) | $3{,}0\times10^{-4}$ | $3{,}5\times10^{-9}$ | $\mathbf{3{,}2\times10^{7}}$ | **ara** |
| **Yıldız** (Güneş gibi) | $9{,}8\times10^{11}$ | $1{,}1\times10^{-24}$ | $\mathbf{9{,}7\times10^{-9}}$ | ortamdan **kopuk** |

$$\boxed{\;\text{TEORİNİN SIRALAMASI: } \textbf{GAZ}\ >\ \textbf{TOZ}\ >\ \textbf{YILDIZ}\;}$$

**Ve sıralama parametresizdir** — yalnız $\gamma\propto1/(\rho_c r_t)$'den çıkar, hiçbir ayar yok.

### 6-L.3 GÖZLEM — ve literatür bölünmüş

**Lehte, ve tam üç noktada:** Reylé, Marshall, Robin & Schultheis (2009, A&A 495, 819), 2MASS
yıldız sayımlarıyla — aynen:

> *"The positive longitude side is found to be easily modelled with a S shape warp but with a
> **slope significantly smaller than the slope seen in the HI warp**. … comparing with the warp
> seen in the dust, it seems to follow a **slope intermediate between the gas and the stars**."*

⟹ **HI > toz > yıldız.** Teorinin sıralamasının **birebir aynısı**, ve üçüncü nokta (tozun arada
olması) tesadüfle açıklanamaz — çünkü tozun $\rho_c r_t$'si de gerçekten arada.

**Aleyhte:** Momany ve ark. (2006, A&A 451, 515), aynı 2MASS verisiyle — *"the derived stellar
warp is **consistent (both in amplitude and phase-angle)** with that for the Galactic
interstellar dust and HI gas."* ⟹ fark **yok.**

$$\Longrightarrow\ \textbf{Literatür bölünmüş, ve teori bir taraf tutuyor.}$$

### 6-L.4 Ama bükülmenin işareti hâlâ ÇIKMIYOR — dürüst kayıt

Sıkı kilitleme rejiminde ($\gamma\gg\nu,\omega_f$) tepki **fazda ve yükseltilmiş** çıkıyor
($1+\Omega/\omega_f\approx2{,}5$–$3{,}2$), **öncü değil.** Kapı açıldı, arkasından öncülük
gelmedi. Ve yükseltme çarpanı yavaşça büyüyor; gözlenen genlik $R^{3{,}08}$ ile — çok daha dik,
yani genlik açıklaması da değil.

| Kalem | Statü |
|---|---|
| *"Öncü desen yapısal olarak yasak"* | ❌ **geri çekildi** (V-10) |
| Öncülük teriminin **varlığı** | ✅ türetildi: $\gamma h\Omega\cos$ |
| **Gaz > toz > yıldız sıralaması** | ✅ **türetildi ve Reylé+2009 ile örtüşüyor** · ⚠ Momany+2006 karşı |
| Bükülmenin **işareti** | ⬜ hâlâ açık — ama artık **yasak değil, üretilmedi** |

### 6-L.5 Ve bir kayıt: aynı virüs üç kez

| # | Nerede | Ne yaptım |
|---|---|---|
| V-9 | §6-C.1 | Kuplajı **çerçeve-sürüklenmeden** aldım, ortamdan değil |
| — | §6-J öncesi | Salınıcının dönüşünü **ortamdan** aldım, maddeden değil (13 kpc hatası) |
| **V-10** | §6-J / C-3 | Sürüklemenin referansını **düzlemden** aldım, ortamın malzemesinden değil |

**Üçünün kökü aynı: iki yoğunluk / iki hız ayrımını (DY-2) tam uygulamamak.** Bu dosyanın
kalıcı dersi: *warp hesabında hangi niceliğin **maddeye**, hangisinin **ortama** ait olduğu her
adımda açıkça yazılacak.*

---

## 7. GÜNLÜK

| Tarih | İşlem |
|---|---|
| 6 Ağustos 2026 (yedinci tur) | **V-9: kuplaj elememin kendisi virüstü — 3.8.7 kanalı zaten kurmuş** (§6-E). Yazar 3.8.7'yi ("Galaksinin Kanat Çırpışı") gösterdi; **teori warpın tam hesabını taşıyor** ve mekanizması benim §6-C.1'de elediğim şey. Hatam: kuplajı **çerçeve-sürüklenme** ile ölçtüm ($2\times10^{-19}$), oysa 3.8.7 kuplajı **ortamın kendisinden** alıyor — *"bu sallanma… akışkan boyunca dalga olarak dışa yayılır; iç disk neredeyse anında izler, dışa gidildikçe kavrama zayıflar ve iletim gecikir."* **Standart fiziğin kanalını ölçüp teorinin kanalını elemiş oldum ⟹ $2\times10^{-19}$ elemesi GERİ ÇEKİLDİ.** *(Hız elemesi geri çekilmiyor; §6-E.3'te karşılandı.)* **Ve 3.8.7'nin okuması benim "yaşayan parça"mdan üstün:** ikisi de rijit presesyonu verir, ama **yalnız 3.8.7 düğüm çizgisi bükülmesini de verir** (gecikme yarıçapla arttığı için faz kayması radyal desen kurar) ⟹ **W-6 kitapta zaten cevaplı**; global-$\omega_2$ okumam terk edildi (§6-C.2 süreç kaydı olarak kalıyor), **W-2 gereksizleşti.** 2025 verisi ikisini bir arada veriyor: tek tempo + statik radyal bükülme. ⚠ **W-6a açıldı:** 2025 modeli bükülmeyi **öncü** sarmal diyor, saf gecikme ise **geride** bırakır — işaret denetlenmeden bükülme "açıklandı" sayılmayacak. **Ve §6-C.1(i)'in hız gerekliliği ilk kez sayıya bağlandı — kitabın kendi önerdiği çapayla.** 3.8.8(iii) *"PSR B1828-11'in ölçülmüş devinim çevrimi, kütle-devinim ölçekleme yasasının ilk gözlemsel çapası olarak kullanılabilir"* diyor; hesaplandı ($P_{spin}=0{,}405$ s, $P_{dev}\approx500$ gün ⟹ $\omega_2/\omega_1=9{,}4\times10^{-9}$). **Zarf sınıflarına göre desen yazarın öngördüğü gibi çıktı:** Dünya (rijit zarf) $1{,}06\times10^{-7}$ · Mars (rijit) $1{,}64\times10^{-8}$ · **PSR B1828-11 (zarfını fırlatmış) $9{,}4\times10^{-9}$** · Sgr A* (zarf yok, **tavan**) *gerekli* $1{,}0\times10^{-14}$ ⟹ **zarf taşıyan üç gövde 11 kat içinde kümeleniyor, tavandaki cisim $9\times10^{5}$ kat aşağıda.** 11.3'ün zarf merdiveni devinimde de görünüyor: zarf kaybı bandı yavaşça çekiyor, **tavan uçurum yapıyor** — ve teorinin kayıtları uçurumu bekliyor (BH tavanda, $\xi\to1$, $\phi\to1$ ⟹ 3B dönüş doygun). **Dürüst sınır:** dört nokta, dördüncüsü **gereklilik değil ölçüm değil**; $10^{-9}$–$10^{-14}$ arasında ara nokta yok (plazma zarflı sınıf eksik); PSR B1828-11'in çevrimi tartışmalı (250/500/1000 gün). **Desen kuruldu, yasa uydurulmadı.** **Üç kitap düzeltmesi + bir kazanç:** D-1 (3.8.7: $10{,}9\to4{,}86$) · D-2 (11.4.9: $13\to4{,}86$) · **D-3 (11.4.9: F5'in warp payı %1–3 $\to$ %3–8, teorinin lehine)** · **D-4: rijitlik gözlemsel olarak doğrulandı** — 3.8.7'nin *"sarılma problemi hiç doğmaz"* iddiasının arkasında artık ölçüm var, ve 3.8.8'in 1. öngörüsü (devinimin kalıcılığı) aynı yönde besleniyor. |
| 6 Ağustos 2026 (altıncı tur) | **W-1 yürütüldü ve OLUMLU: warp RİJİT preses ediyor** (§6-D). Yazar izniyle arXiv tarandı. **Kitaptaki sayı bayat:** 11.4.9 $13$ km/s/kpc kullanıyor; Poggio 2020'nin $10{,}86$'sına **itiraz edildi** (Chrobáková & López-Corredoira 2021: $\beta=4^{+6}_{-4}$, presesyonsuz warpı dışlamıyor), Zhou ve ark. 2024 $4{,}9\pm1{,}6$, ve **en güncel (2025 Cepheid) $4{,}86\pm0{,}88\pm2{,}14$** ⟹ dönem $1{,}26$ Gyr. **W-1'in cevabı 2025 modelinin kapalı biçiminden okunuyor:** $Z_w(t)=0{,}00019R^{3{,}08}\sin(\varphi-(3{,}87R-41{,}79+4{,}86t))$ — **zaman terimi $R$ içermiyor** ⟹ düğüm çizgisi yarıçapla bükülüyor ama **bütün desen tek hızla preses ediyor**, *"nearly uniform beyond 12.5 kpc."* **⟹ RİJİT, yani §6-C.5'in ayrımında teorinin dalı.** **Ve asıl kazanç:** rijitlik **standart çerçevede bir sorundur** — sarılma (winding) problemi; Ideta ve ark. (1999) *"oblate halede warp sarılıp yok olur; prolat halede düğüm çizgisinin hizası korunarak sürer"* ⟹ standartta rijitlik için **haleye özel biçim** gerekiyor, **ayarlanmış çözüm.** Teoride ise $\omega_2$ tek bir global niceliktir, yarıçapla değişmesi için sebep yok; preses eden şey diskin malzemesi değil **kesitin arakesiti** (11.7.1) ⟹ **sarılma problemi doğmaz.** *Standartta rijitlik açıklanacak şey, teoride varsayılan.* **İKİ KİTAP DÜZELTMESİ, biri lehte:** (a) 11.4.9'un $13$'ü $\to4{,}86$; (b) **F5'in warp payı üçe katlıyor** — aynı $0{,}15$–$0{,}41$ km/s/kpc katkısı $13$ üzerinden %1–3 iken $4{,}86$ üzerinden **%3–8**. Kitabın kendi hesabı güncel gözlemle **güçleniyor.** **Ölü parça büsbütün öldü:** oran $3{,}9\times10^6\to\mathbf{1{,}0\times10^7}$, kuplaj elemesi ($2\times10^{-19}$) değişmedi. **⚠ Dürüst çatlak (W-6, yeni):** saf global $\omega_2$ rijit presesyonu verir ama düğüm çizgisinin **yarıçapla bükülmesini** ($3{,}87R$) vermez. **Teori-içi aday var ve uydurma değil:** 11.4.9'un $\lambda_{etkin}=d\ln v_c/d\ln R+(\mathcal{A}/2)(R/h_z)^2$'si yarıçapla değişiyor ($\mathcal{A}(R)$, $h_z(R)$) ⟹ radyal değişen kilit sertliği bükülmüş denge düzlemi verebilir; doğrudan **11.4-vi**'ya bağlanır. **Kalan iki iş kavramsal ve ikisinin de teori-içi adayı var:** W-2 (büyüklük — $\Omega$ yarıçapa bağlı olduğu için $\omega_2/\omega_1=0{,}28$–$0{,}55$) ve W-6 (bükülme). |
| 6 Ağustos 2026 (beşinci tur) | **Dosya yeniden açıldı: galaktik warp hattı** (§6-C). Yazar hipotezi: Samanyolu warpı presesyondan kaynaklanıyor; warp dönemi ile karadelik presesyonu kıyaslanacak; zarf faktörü devinime de girmeli. **Hipotez ikiye ayrıldı.** **ÖLÜ parça — warp ← Sgr A*:** ① hız $3{,}9\times10^6$ kat uyuşmuyor (warp 473 Myr ↔ evrensel $\omega_2/\omega_1$ ile BH devinimi 123 yıl; tutması için $\omega_2/\omega_1=2{,}75\times10^{-14}$ gerekir, Dünya'nın $2{,}6\times10^{-7}$'si); ② **ve asıl eleyen, $\omega_2$'den bağımsız: kuplaj yok** — $\Omega_{LT}(20$ kpc$)=8{,}6\times10^{-35}$ s⁻¹, warpın $2\times10^{-19}$'u; kütle tarafı da aynı yönde (BH, kapsanan kütlenin $1{,}8\times10^{-5}$'i). Karadelik doğru hızda dönse bile dış diski eğemez. **YAŞAYAN parça — warp = galaksinin KENDİ W-imzası; yazar onayladı** (*"warpın galaktik düzeyde olmasını onaylıyorum"*): BH bir neden değil **kardeş izdüşüm**, kuplaj sorunu tamamen kalkıyor, ve $\omega_2/\omega_1=\omega_{warp}/\Omega(20\,\mathrm{kpc})=\mathbf{1{,}18}$ — **mertebe bir, ayarlama yok**, teorinin dilinde izokliniğe yakın çift dönüş. Üçüncü destek: **warp yaygındır** — dış-tork açıklamaları her galaksi için ayrı kaynak ister, içkin W-bileşeni yaygınlığı kendiliğinden verir. **Yazar kaydı: bu hesap standart çerçevede yapılamaz**, çünkü $\omega_2$ diye bir nicelik orada yok. **Yaşayan parçanın kendi sorunu:** galaksi rijit değil ⟹ $\omega_1$ tanımsız; oran yarıçapa bağlı ($8{,}2$ kpc'de $0{,}48$, 20 kpc'de $1{,}18$) ⟹ **W-2 blokajı.** **Zarf ipucu yönü doğru** — 11.3.6 (BH tavanda), M-40 ($\xi\to1$), 11.3.7 ($\phi\to1$, kafes kilitli) üçü de doygun cisimde W payının kısılmasını destekliyor, ve gereken sıralama tam bu (galaksi $O(1)\gg$ gezegen $10^{-7}\gg$ BH $10^{-14}$) — **ama 14 mertebe iki noktaya uydurulmadı**; $898^2$ denendi, 4,8 kat uzak. **11.7-ii artık adayı olan bir soru: doygunluk.** Beş yeni kalem: **W-1** (warp rijit mi diferansiyel mi preses eder — **ayırt edici ve mevcut veriyle sınanabilir**) · W-2 · W-3 · **W-4** (11.4.9'un *"warp kapsam dışı"* kaydının fatura denetimi) · W-5 (warp yaygınlığının nicelleştirilmesi). |
| 6 Ağustos 2026 | Dosya açıldı. Kısım 11 kapsam taramasından doğdu: 11.2.8 Merkür/Venüs figür eksenini işliyor ama **Dünya'nın eksen devinimi kitapta hiç yok.** Gözlem tabanı toplandı ($50{,}29''$/yıl, $25.772$ yıl, $H=3{,}2737\times10^{-3}$). **Ön denetim yapıldı ve zincirin ilk halkası tuttu:** kitabın türettiği $J_2=1{,}0826\times10^{-3}$ ile $H=J_2/0{,}3307=3{,}2735\times10^{-3}$, gözlenenle **dört hanede** uyumlu. Dört kalem kuruldu; **K-2 (döngüsellik) K-1'den önce** — $C/MR^2$ Darwin–Radau'dan geliyorsa sınav $J_2$'yi kendisiyle sınar, ve 11.2.6'nın *"Darwin–Radau neden ana yöntem değildir"* bölümü okunmadan hüküm verilmeyecek. K-3'ün ön beklentisi: F5 saf $P_2$ olduğu için dejenere ⟹ tutarlılık kazancı, sınav değil. |
