# Kitap ↔ Sınav Bulguları Fark Kaydı

**Amaç.** Yazar kararıyla sınav çalışması **yayın dışıdır** ve yalnız `CALISMA/` dizininde yürütülür; kitap bölümleri sınav bulgularıyla **değiştirilmez**. Bu dosya, o kararın zorunlu tamamlayıcısıdır: kitabın hangi ifadelerinin sınav bulgularıyla artık örtüşmediğini **tek tek, konumuyla ve düzeltme metniyle** kaydeder.

Böylece iki şey sağlanır:
1. Bilinen farklar **sessizce unutulmaz** — hiçbiri "gözden kaçmış hata" konumuna düşmez.
2. Yazar ileride yayımlamaya karar verirse, liste **mekanik olarak uygulanabilir** durumdadır.

**Durum tarihi:** 29 Temmuz 2026
**Kaynak:** `CALISMA/07_Teorinin_Sinanmasi.md` (Sınav 1–5) · `CALISMA/10_Sinav_Calismasi_Claude.md` (Sınav 1 yeniden kurgu, Adım 1–9)

> **⚠ Adım 9 bu listeyi kısmen geçersiz kıldı.** `10_Sinav_Calismasi_Claude.md` Adım 9, süper akışkan irrotasyonelliğinden **$\kappa_5=0$'ı türetti** (yanal itim yapısal olarak sıfır). Bu, F-1 · F-2 · F-3 · F-4'ün hepsini tek bir düzeltmeyle birleştiriyor — aşağıda **F-1′** olarak kaydedildi. Eski kayıtlar tarihsel iz olarak bırakıldı, ama **uygulanacak olan F-1′'dir.**

---

## 0. Karar kaydı

| | |
|---|---|
| Sınav bölümünün statüsü | **Yayın dışı çalışma dosyası** (`CALISMA/`) |
| `app.js` menü girişi | **Kaldırıldı** (6.6 ve Gemini Eki); Kaynakça 6.6'ya döndü |
| Kitap bölümlerine işleme | **Yapılmayacak** — yazar kararı |
| Bu dosyanın işlevi | Farkları izlenebilir tutmak |

**İstisna — daha önce yetkiyle işlenmiş olan:** Sınav 4'ün *çözümü* (stiff hâl denklemi, $k=0$) yazar onayıyla kitaba yayılmıştır ve kitapta **doğru** durmaktadır. Bu dosyadaki farklar Sınav 1, 2, 3 ve 5'e aittir.

---

## 1. Kitapta bilinerek bırakılan yanlış/eksik ifadeler

Hepsi `Kisim_8_Ekler/18_5_Kuvvet_Matematigi.md` içindedir (Blok H).

### F-1 · M-39: "İmza $J_2$'de değil $J_4$'tedir" (satır ~487)

| | |
|---|---|
| **Kitap ne diyor** | Yanal itimin imzası $J_4$ ve $J_6$'dadır; merkezkaç bu deseni taklit edemez |
| **Bulgu** | **Yanlış.** F5'in potansiyeli saf $P_2$'dir ($\Phi_5=\text{sbt}-\tfrac{2A_5}{3}P_2$) ve radyal bağımlılığı da merkezkaçla özdeştir ($\propto r^2$). Hiçbir harmonikte ayrı imza bırakmaz |
| **Kaynak** | Sınav 1, "F5 için: $J_4$'te imza yoktur" |
| **Düzeltme** | Bölüm, dejenerelik türetimiyle değiştirilmeli; $J_4$ imzasının **F4'e (eksenel itim)** ait olduğu yazılmalı |
| **Neden önemli** | Bu, gerekçesi hatalı bir sonuç: "profiller farklı görünüyor" ⟹ "multipol içeriği farklı" çıkarımı geçersizdir |

### F-2 · M-39 ve H.0/H.3: $\kappa_5\lesssim0{,}1$ (satır 24, 1066)

| | |
|---|---|
| **Kitap ne diyor** | $\kappa_5\lesssim0{,}1$ |
| **Bulgu** | $\kappa_5\lesssim\mathbf{0{,}02}$. Eski değer $\rho_0/\rho_n=\tfrac18$ ($k=\tfrac12$) kullanıyordu; Sınav 4 $k=0$'ı sabitledi ⟹ $\rho_0/\rho_n=\tfrac14$ ⟹ sınır 2,5 kat sıkıldı |
| **Ek kayıt** | Gözlem yalnız **çarpımı** bağlar: $\kappa_5\phi^2\le0{,}0084$. $0{,}02$ değeri $\phi_\oplus\approx0{,}6$ tercihine dayanır (M-15'in $\phi=1-1/n^2$'si), gözleme değil |
| **Kaynak** | Sınav 1, "Veri ve sonuç — Dünya" + "Dört Cisim Sınavı" |

### F-3 · M-39 Açık Uç 1: "$\kappa_5$'in $J_4$'ten kalibrasyonu" (satır ~568)

| | |
|---|---|
| **Kitap ne diyor** | Dört cisim (Dünya, Jüpiter, Satürn, Güneş) $\Delta_4$ üzerinden tek $\kappa_5$ vermeli — çok gözlemli yanlışlama sınavı |
| **Bulgu** | **Sınav kurulamıyor.** Dünya kalibrasyon; Güneş'te hassasiyet 7–25 kat yetersiz (S/N = 0,04–0,14); Jüpiter/Satürn'ün hidrostatik referansı gravite alanından fit ediliyor — döngüsel. Bağımsız kısıt sayısı **sıfır** |
| **Düzeltme** | Açık uç, "ayırt edici bir gözlem var mı?" sorusuna dönüştürülmeli |

### F-4 · H.3: "Yanal itim gaz devlerinde güçlü, Güneş'te yok" (satır ~1067)

| | |
|---|---|
| **Bulgu** | Sınanamaz. Güneş'in null sonucu $\phi\approx0$'ı **desteklemiyor**: $\phi_{Güneş}=\phi_{Dünya}$ olsa bile etki ($9\times10^{-10}$) solar $J_2$ belirsizliğinin ($\sim10^{-8}$) bir mertebe altında kalır |

### F-5 · M-38: Yayılma (flaring) öngörüsü (satır ~303)

| | |
|---|---|
| **Kitap ne diyor** | "Kalınlaşan diskte düz eğrinin sürmesi modeli çürütür" — **yapılmamış** bir sınav gibi |
| **Bulgu** | **Sınav yapıldı ve başarısız oldu.** $v_\theta\propto h^{-1/2}$ Samanyolu için 8,5→20 kpc arasında **3,4 kat** düşüş gerektiriyor; gözlenen **1,13 kat**. Ters okunuşla izinli $h$ büyümesi ≤1,27 kat, gözlenen ~6 kat |
| **Kaynak** | Sınav 2 |

### F-6 · M-38 + M-30: Düz dönüş eğrisinin türetimi

| | |
|---|---|
| **Kitap ne diyor** | $h=$sabit ⟹ $a\propto1/R$ ⟹ $v_\theta=$sabit zinciri bir **türetim** olarak sunuluyor |
| **Bulgu** | Zincirin ilk halkası ($h=$sabit, gaz katmanıyla özdeşleştirildiği biçimiyle) **çürütüldü**. İnce-tüp çıkışı da çürütüldü (Sınav 3). Geriye yumuşak kenarlı tüp kalıyor, o da **ikinci** bir serbest fonksiyon ($h_{etkin}(z)$) getiriyor |
| **Sonuç** | Teorinin karanlık madde alternatifi şu an ya **yanlışlanmış** ya **iki serbest fonksiyona dayanıyor** |
| **Kaynak** | Sınav 2 + Sınav 3 |

### F-7 · M-40: Minimum karadelik kütlesi (satır ~722–728, 1069)

| | |
|---|---|
| **Kitap ne diyor** | $M_{\min}\approx8{,}3\,M_\odot$ → 4–8 $M_\odot$; kütle boşluğu **yapısal eşik** |
| **Bulgu** | **Öngörü geri çekilmeli.** Üç gerekçe: (i) $\rho_n$ sıkışma tavanı değil — stiff hâl denkleminde tavan yok ve nötron yıldızları $\rho_n$'i 1,4 kat aşıyor; (ii) hesap Newton-hacmi ↔ Schwarzschild-yarıçapı melezi; (iii) konu **güçlü alan rejimine** ait ve M-42 yalnız 1PN veriyor |
| **Doğru okuma** | Stiff ortam nedensellik sınırını doyurur ⟹ **daha ağır** nötron yıldızlarına izin verir (Rhoades–Ruffini tavanı ~4 $M_\odot$). Kütle boşluğunu dolduran cisimler (GW190814'ün 2,6 $M_\odot$'ı) teoriyi sıkıştırmıyor, **destekliyor** |
| **Uyarı** | ~4 $M_\odot$ GR'dan (TOV) ödünçtür; teori kendi kompakt cisim denklemlerini türetmemiştir |
| **Kaynak** | Sınav 5 |

### F-8 · H.1 tablosu: M-39 satırı (satır ~1008)

"imza $J_4$'te" ve "$\kappa_5\lesssim0{,}1$" — F-1 ve F-2 ile aynı düzeltmeler.

---

---

## 1′. Adım 9'un getirdiği kayıtlar

### F-1′ · M-39 bütünüyle: yanal itim **yapısal olarak sıfırdır** *(F-1, F-2, F-3, F-4'ü birleştirir)*

| | |
|---|---|
| **Kitap ne diyor** | Yanal itim $F_5$ gerçek bir kuvvettir; $\kappa_5\lesssim0{,}1$ serbest parametredir; imzası $J_4$'tedir; dört cisim tek $\kappa_5$ vermelidir |
| **Bulgu** | **$\kappa_5=0$ TAM.** Süper akışkan ⟹ girdap irrotasyonel ⟹ potansiyel akış ⟹ dönen kürede sınır koşulu $\vec v\cdot\hat n=0$ zaten $\vec v=0$ ile sağlanır ⟹ akışkan cismin döndüğünü öğrenemez ⟹ $\Delta P=0$. Dönen çerçeve Bernoulli'sinde $\tfrac12v'^2$ ile $\tfrac12\Omega^2r_\perp^2$ birebir sadeleşir |
| **Kaynak** | Adım 9d, 9f |
| **Düzeltme** | M-39 bir *öngörü* bölümünden bir *türetim* bölümüne dönüşmeli: yanal itim yoktur, ve **neden olmadığı** süper akışkanlıktan türetilir. $\kappa_5$ serbest listeden çıkar |
| **Serbest skaler** | **5 → 4** ($\kappa_5$ türetildi). Ek C'de $\kappa_5$ satırı F→T |
| **Neden iyi haber** | Basıklık çelişkisi kalkıyor, dört gözlem (halka lazer, M&M, LLR, LAGEOS/GPS) otomatik geçiliyor, ve tek bir ayar yapılmıyor |
| **Bedeli** | Sınav 1'in ayırt edici öngörüsü kayboluyor: teori figür kanalında standart fizikle **özdeş**. Ama F-3/F-4 zaten o öngörünün sınanamadığını kaydetmişti |

### F-9 · H.1 tablosu: M&M sürüklenmenin kanıtı olarak kullanılamaz

| | |
|---|---|
| **Konum** | `Kisim_8_Ekler/18_5_Kuvvet_Matematigi.md` H.1 tablosu, "Öteleme" satırı (~satır 1008 civarı) |
| **Kitap ne diyor** | *"Öteleme: tam sürüklenme ($v_{bağıl}\approx0$) · Gözlemsel sınav: Michelson–Morley sıfır sonucu"* |
| **Bulgu** | M-19'un boy kısalması M&M'i **her $v$ için** nulluyor: $T_\parallel=\frac{2L}{\gamma c}\gamma^2=\frac{2L}{c}\gamma=T_\perp$. Dolayısıyla sıfır sonuç sürüklenmeyi **desteklemez** — hiçbir şey söylemez |
| **Düzeltme** | M&M satırı "tutarlılık kontrolü" olarak yeniden yazılmalı, "gözlemsel sınav" olarak değil. Öteleme sürüklenmesinin gerçek sınavı Fizeau/Sagnac tipi **birinci mertebe** deneylerdir |
| **Kaynak** | Adım 9a |

### F-11 · M-38: $A$'nın kaynağı disk kalınlığı değil, evrensel ivme ölçeğidir *(F-5 ve F-6'yı kaldırır)*

| | |
|---|---|
| **Kitap ne diyor** | Eksenel itim düz eğriyi verir; $v_\theta\propto h^{-1/2}$; $h=$sabit ⟹ $a\propto1/R$ ⟹ $v=$sabit |
| **Bulgu** | $A$'nın $h$'ye bağlanması **hem BTFR'yi hem flaring sınavını düşürüyor.** Doğrusu: $r_t$'de sürekliliğin zorunlu kıldığı $A=\sqrt{GMa_0}$, $a_0\simeq cH_0/2\pi$ |
| **Kazanç** | BTFR **tam** çıkıyor ($v^4=GMa_0$, üs 1/4, gözlem $0{,}26\pm0{,}01$) · **Sınav 2'nin (flaring, 2,2 kat) ve Sınav 3'ün (ince tüp) itirazları buharlaşıyor** çünkü $A$ artık $h$'den bağımsız · Serbest parametre: galaksi başına bir $A$ + $h_{etkin}(z)$ ⟹ **evrensel tek $a_0$** |
| **Sayısal** | $a_0=cH_0/2\pi$: %−13. $v_{flat}$ öngörüsü 7 galakside ort. %15,2 — ama saçılma kaba $M_{baryon}$ girdilerinden, teoriden değil; **doğru örneklemle yeniden sınanmalı** |
| **Açık kalan** | $1/r$ **biçimi** türetilmedi, varsayıldı. Geometrik 2B yolu ($4\pi r^2\to2\pi r$) doğru biçimi veriyor ama geçişi $h$'ye koyuyor ve orası 1–33 kat çakışmıyor. **Ek C'de $1/r$ varsayım olarak işaretlenmeli** |
| **Kaynak** | Adım 10 (`10_Sinav_Calismasi_Claude.md`) |
| **Not** | **F-5 ve F-6 bu kayıtla kapanır** — o iki kayıt $h$-bağımlılığının sonuçlarıydı |

### F-10 · M-40: $\xi$ pürüzsüz formülle kuantize mekanizma arasında

| | |
|---|---|
| **Kitap ne diyor** | $\xi=\frac{I}{MR^2}\frac{2\Phi}{c^2}$ — pürüzsüz, eşiksiz |
| **Bulgu** | Saf potansiyel akış $\xi=0$ verir. $\xi\neq0$ ancak **kuantize girdap çekirdeklenmesiyle** olur; o da eşiklidir ve basamaklıdır. Pürüzsüz formül yalnız $N=\frac{2\xi\omega\pi R^2}{\kappa}\gg1$ ise geçerli |
| **Kazanç** | İki yeni **ayırt edici** öngörü: (i) $\Omega<\Omega_c$ cisimlerde çerçeve sürükleme **tam sıfır**; (ii) $\xi$ basamaklı. GR'da ikisi de yok. Ayrıca $\kappa=h/m_{Zerre}$'ye üst sınır ⟹ $m_{Zerre}$'ye **alt sınır** |
| **Durum** | Açık iş — Adım 10'un konusu |
| **Kaynak** | Adım 9h |

---

## 2. Boşa düşen atıf

| Konum | Sorun |
|---|---|
| `Kisim_8_Ekler/19_Ek_M_Blok_I_Eylem_Ilkesi.md:114` | *"Bölüm 6.6.5'teki Sınav 4 bunu yanlışladı"* — Bölüm 6.6 artık kitapta yok. Atıf `CALISMA/07_Teorinin_Sinanmasi.md`'ye yönlendirilmeli ya da metin sınav referansı olmadan yeniden yazılmalı |

*Not: M-3′ ve M-6'daki düzeltmeler sınav bölümüne atıf içermez (M-44'e atıf verirler), dolayısıyla etkilenmemiştir.*

---

## 3. Kitapta **doğru** duran, dokunulmaması gerekenler

Sınav 4'ün çözümü yazar onayıyla işlendi ve kitapta tutarlıdır. Karışıklık olmaması için kaydedilir:

- **$k=0$**, türetilmiş (Ek C satır 3: F→T); serbest skaler sayısı **6 → 5**
- **Stiff hâl denklemi** $P=c^2\rho$; sıkışma kanalı ses hızı **tam $c$**; GW170817 otomatik sağlanıyor
- **$P_0=\tfrac14\rho_nc^2=6{,}07\times10^{33}$ Pa** kesin; $\rho_0=\rho_n/4$
- **Ek M-44** iki değişkenli hâl denklemiyle baştan yazıldı
- **Ek M-3′** (sıkıştırılabilir yeniden türetim): $\sqrt2c$ = yoğunluğun e-katlanma hızı; çekirdek için kavitasyon gerekmiyor; %18 sorunu çözüldü
- **Ek M-5 / M-9**: "sıkışma kanalının hızı $c$'dir" — **orijinal metin doğrudur**, bir ara turda yapılan $c/\sqrt k$ düzeltmesi hatalıydı ve geri alındı

---

## 4. Çalışma dizini envanteri

| Dosya | İçerik |
|---|---|
| `07_Teorinin_Sinanmasi.md` | Sınav 1–5, yürütülemeyen üç sınav, dürüst tabelo |
| `08_Teorinin_SinanmasiGemini.md` | Dört-cisim taslağı (denetlendi; bulguları 07'ye birleştirildi) |
| `09_Kitap_Sinav_Farklari.md` | **bu dosya** |
| `10_Sinav_Calismasi_Claude.md` | Sınav 1 yeniden kurgu, yazar yönlendirmesiyle Adım 1–9. **$\kappa_5=0$ türetimi burada** |

---

## 5. Yayımlama kararı verilirse: uygulama sırası

Öncelik, hatanın okuyucuyu ne kadar yanılttığına göre:

1. **F-11** — $A=\sqrt{GMa_0}$. Kitabın **en büyük iddiasını** (karanlık madde alternatifi) yanlışlanmış durumdan çalışır duruma getiriyor, BTFR'yi kazandırıyor, iki düşmüş sınavı kaldırıyor ve serbest parametre azaltıyor. Kazancı en yüksek kalem bu. *(Uyarı: $1/r$ biçimi varsayım olarak işaretlenmeli.)*
2. **F-1′** — $\kappa_5=0$ türetimi. Var olmayan bir kuvvet yayımda duruyor; tek kalemde F-1, F-2, F-3, F-4 ve F-8'i kapatır. Serbest skaler 5→4, yani Ek C ve özet tablolar da etkilenir.
3. **F-7** — geri çekilmesi gereken bir öngörü yayımda duruyor.
4. **F-9** — M&M'in kanıt değeri. Tek satır ama epistemik olarak önemli.
5. **F-10** — $\xi$'nin kuantize mekanizması. Yeni öngörüler önce türetilmeli.
6. **Boşa düşen atıf** (bölüm 2) — tek satır.

**Kapsanan eski kayıtlar — ayrı ayrı uygulanmamalıdır:**

| Eski | Kapsayan |
|---|---|
| F-1, F-2, F-3, F-4, F-8 | **F-1′** |
| F-5, F-6 | **F-11** |

Böylece uygulanacak kalem sayısı 8+1'den **6'ya** düştü, ve ikisi (F-11, F-1′) kitabın lehine değişiklik.

Uygulanırsa Anayasa'ya ayrı bir TUR kaydı düşülmelidir.
