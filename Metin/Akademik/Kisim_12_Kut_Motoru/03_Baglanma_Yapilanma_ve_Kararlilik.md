# 12.3 Kutların Bağlanması, Yapılanması ve Kararlılığı

Kut vardır (12.1) ve 4B dönüşün izini taşır (12.2). Şimdi asıl soru: **Kutlar nasıl bir araya gelir?**

Bu bölüm yapının **nasıl kurulduğunu** anlatır. Kurulan yapının Kut'un dönüşünü nasıl **devraldığı** ise bir sonraki bölümün konusudur (12.4) — ve kitabın omurgası orasıdır.

Bu bölüm, Evrenakı Teorisi'nin atom altı yapıya bakan yüzüdür. Ama dikkat: burada atomların nasıl işlediği anlatılmıyor. Burada anlatılan, **daha alttaki katmanın kuralları** — Kutların hangi mesafede durduğu, hangi topluluklara oturduğu, hangi birlikteliklerin ayakta kaldığı. Atomlara giden yol buradan geçer, ama yolun kendisi bu kitabın konusu değildir (12.6).

---

## 12.3.1 Başlangıç: Girdap Dinamiği Bağ Üretmez

İlk ve en önemli olumsuz sonuçla başlamak gerekir, çünkü bu kısımdaki her şey onun üzerine kuruludur.

İki eş yönlü Kut'un karşılıklı taşıma hızının **radyal bileşeni tam sıfırdır.** Birbirlerine ne yaklaşır ne uzaklaşırlar; ortak merkez etrafında yörüngeye girer, ayrımı korurlar.

$$v_{\text{radyal}} = 0 \qquad \text{(nokta girdap dinamiği, tam)}$$

Enerji de aynı şeyi söyler. Eş işaretli çiftte etkileşim enerjisi

$$E_{\text{int}} = -\frac{\Gamma_1\Gamma_2}{2\pi}\ln d$$

ve bu, $d$ büyüdükçe **düşer** — yani ayrılmak bedavadır, hatta enerjice tercih edilir.

**Basınç haritası da doğrular:** eş yönlü çiftin tam ortasında hızlar birbirini götürür, $\rho = \rho_0$ (sırt, yüksek basınç); dışta hızlar toplanır, $\rho = 0{,}454$ (çukur). Boşluk düşük basınca gider ⟹ her Kut dışa bakar.

> **Sonuç:** Kutları bir arada tutan şey girdap dinamiği **değildir**. Başka bir kanal gerekir. Bu bölümün geri kalanı o kanalı kurar — ve onu **türetir**, seçmez.

---

## 12.3.2 Birinci Kanal: Bjerknes Çekimi

12.2'nin birinci imzası her Kut'un **pulsasyon** yaptığını söylüyordu. Pulsasyon yapan iki kavite, akışkanda birbirine kuvvet uygular — bu, akustikte **ikincil Bjerknes kuvveti** adıyla bilinen ve kabarcıklarda rutin olarak gözlenen olgudur:

$$F = -\frac{\rho\langle \dot V_1 \dot V_2\rangle}{4\pi d^2}$$

- **Aynı fazda** pulsasyon ⟹ $\langle\dot V_1\dot V_2\rangle > 0$ ⟹ **ÇEKİCİ**
- **Zıt fazda** ⟹ **İTİCİ**

Ve teori faz uyumunu **kendisi sağlar**: bütün Kutlar aynı 4B dönüşün parçasıdır, $\omega_2$ ortaktır. Kuvvet, kavitenin hacim salınımından doğduğu için tam olarak **sınır tabakalarının örtüştüğü yerde** üretilir.

Model birimlerinde:

$$F_{\text{Bjerknes}}(d) = \frac{\kappa\cos(\text{faz})}{d^2}$$

> **Tek başına $1/d^2$ çekimi bağ değil, çöküş üretir.** Saf çekici bir terim ayrımı sıfıra indirir; orada girdap hızı $K/d$ ıraksar ve çift savrulur. Sayısal deney de bunu doğrular: yalnız bu terimle koşulan çiftte ayrım 2'den 4,97'ye, kalabalık toplulukta 40'a savruldu. **Denge mesafesi olmayan çekim bağ üretmez.** İkinci bir kanal zorunludur.

---

## 12.3.3 İkinci Kanal: Akustik Işıma — Türetim

İkinci kanal seçilmedi, **türetildi**. Ve bu, kısmın en teknik ama en belirleyici sayfasıdır.

**Kaynak.** Dönen bir Kut çiftinin uzak alan açılımında dipol terimi sıfırdır ($z_1 + z_2 = 0$), ilk terim kuadrupoldür ve frekansı $2\Omega$'dır:

$$-\frac{z_1^2+z_2^2}{2z^2} = -\frac{a^2 e^{2i\Omega t}}{z^2}$$

Dipolün yokluğu fizikseldir: **net momentum ışınamaz.**

**2B Lighthill çözümü.** Sıkıştırılabilir ortamda:

$$\frac{\partial^2 p'}{\partial t^2} - c_0^2\nabla^2 p' = c_0^2\frac{\partial^2 T_{ij}}{\partial x_i \partial x_j}, \qquad T_{ij} = \rho_0 v_i v_j$$

2B Green fonksiyonu $|G| = \tfrac14\sqrt{2/\pi kR}$ ile uzak alanda $|p| = k^2|G||Q|$, ve birim uzunluk başına güç:

$$\boxed{\;P = \frac{k^3|Q|^2}{8\rho_0 c_0}\;}$$

$|Q| = C\rho_0\Gamma a^2\Omega$ ve $\Omega = \Gamma/4\pi a^2$ konunca $|Q| = C\rho_0\Gamma^2/4\pi$ ($a$'dan bağımsız), ve:

$$P \sim \rho_0 c_0^3 \, a \, M^{7}$$

**$n = 7$.** (3B kuadrupol $M^8$ verir; 2B bir mertebe daha verimlidir.)

> **Geçerlilik notu.** $M^7$ bir **asimptotik ölçek yasasıdır**: klasik aeroakustik türetim küçük Mach açılımında kurulur ve nicel kesinliği $M \ll 1$'de en yüksektir. Bu bölümde yasa, $M \approx 0{,}94$'te bir **mertebe kestirimi** olarak kullanılır; kuadrupol önkatsayısı zaten hesaplanmamıştır (12.5.7). Bölümün taşıyıcı sonuçları — işaret yapısı, $1/d^5$ biçimi ve denge kökünün varlığı — önkatsayının nicel kesinliğine dayanmaz; yüksek Mach'ta değişebilecek olan şey yönlülük ve sayısal güçtür, işaret ve üstel yapı değil.

**Enerji dengesi rateyi tam belirler — serbest parametre yoktur:**

$$\dot d = \frac{dE/dt}{dE/dd} = \mp\frac{2\pi d P}{\rho\Gamma^2} \;\sim\; \mp\frac{K^5}{d^5}$$

$$\boxed{\;F_{\text{ışıma}}(d) = -\lambda\,g_i g_j\,\frac{K^5}{d^5}\;}$$

**İşaret duyarlılığı elle konmadı** — $dE/dd$'nin işaretinden geldi:

| | $E_{\text{girdap}}$ | yaklaşınca | enerji düşerse |
|---|---|---|---|
| Eş yönlü | $-(\Gamma^2/2\pi)\ln d$ | artar | **uzaklaşırlar** |
| Zıt yönlü | $+(\Gamma^2/2\pi)\ln d$ | azalır | **yaklaşırlar → yok olurlar** |

**Ve ışıma zayıf bir tashih değildir.** Işıma kanalında geçen $M$, **çiftin ayrımındaki**
karşılıklı taşıma hızıdır: $d_{\text{denge}}$'de $M \approx 0{,}94$, sınır tabakasında
$M = 1{,}414$. $M\sim1$'de akustik kayıp dönmeyle **aynı mertebede** çalışır. Sönümü sıfır
almak bir yaklaşım değil, **hatadır**.

> **Ölümcül görünen itiraz — ve cevabı.** Kut'un **cep duvarındaki** hız
> $6{,}16\times10^{4}\,c_0$'dır (12.1.1). Işıma $M^7$ ile gittiğine göre orada
> $M^7 \approx 3\times10^{33}$ olur; bir Kut kendini anında ışıyıp yok etmez mi?
>
> **Etmez, ve sebebi geometriktir:** tek başına düzgün dönen bir Kut **eksenel
> simetriktir**. Eksenel simetrik ve **kararlı** bir akışta $T_{ij}$ zamana bağlı
> değildir; zamana bağlı çokkutup momenti yoksa **ışıma da yoktur** — hız ne kadar
> süpersonik olursa olsun. Lighthill kaynağı $\partial^2 T_{ij}/\partial x_i\partial x_j$
> bir **değişim** gerektirir, büyüklük değil. Bu cevap, $M^7$ yasasının o hızlardaki
> geçerliliğinden de bağımsızdır: simetri argümanı kesindir, ölçek yasası gerektirmez.
>
> Işıma ancak simetri **kırılınca** doğar: iki Kut ortak merkez etrafında dönerken
> kuadrupol momenti $2\Omega$ frekansıyla salınır (12.3.3'ün başı). Dolayısıyla
> ışımayı yöneten ölçek **çiftin ayrımı $d$**'dir, Kut'un iç yarıçapı değil — ve
> orada $M \approx 0{,}94$'tür.
>
> **Tezat yok, ama ayrım kritiktir:** cep duvarının $6\times10^{4}\,c_0$'ı ışımaya
> **girmez**; çiftin $0{,}94\,c_0$'ı **girer**. İkisini karıştırmak, türetimi 33
> mertebe yanlış yapar.

---

## 12.3.4 Toplam Yasa ve İşaret Yapısı

$$\boxed{\;F(d) = \frac{\kappa\cos(\text{faz})}{d^2} \;-\; \lambda\,g_i g_j\,\frac{K^5}{d^5}\;}$$

| | eş yönlü ($g_ig_j>0$) | zıt yönlü ($g_ig_j<0$) |
|---|---|---|
| Bjerknes $\kappa/d^2$ | çeker | çeker |
| Işıma $-\lambda g_ig_j K^5/d^5$ | **iter** | **çeker** |
| **Sonuç** | **kararlı denge** | **DENGE YOK** |

$$\boxed{\;d_{\text{denge}} = \left(\frac{\lambda K^5}{\kappa}\right)^{1/3}\;}$$

**Zıt yönlü çift için kök yoktur** — her iki terim de çekicidir, toplam her mesafede pozitiftir. 210 farklı $(\kappa,\lambda,d)$ üçlüsünde $F \le 0$ olan **hiçbir** durum bulunmadı.

> **Ters Kut'un bir yapıda duramaması, bir katsayı sonucu değil, işaret yapısının sonucudur.** Hiçbir parametre seçimi bunu değiştiremez.

**Ve $d_{\text{denge}}$ bir girdi değil, çıktıdır.** Küme aralığı artık bir **öngörüdür**.

Kuvvet yasasının iki teriminin dışında bir terime gerek olmadığı da vurgulanmalıdır: kısa erimli ayrı bir itme kanalı fiziksel olarak temelsizdir. Boşluk düşük basınca — yani girdaba **doğru** — çekilir; "cepler iç içe geçemez" gerekçeli bir itme ise ölçek olarak tutarsız olurdu, çünkü cepler ($2{,}29\times10^{-5}\,r_e$) küme aralığından ($\approx 1{,}4\,r_e$) yaklaşık **62 000 kat** küçüktür. Dengeyi kuran itme, türetilmiş ışıma kanalıdır.

---

## 12.3.5 Yok Olma ve Birleşme: İki Olay, Tek Ölçüt

| Olay | Koşul | $\Gamma_{\text{top}}$ | Sonuç |
|---|---|---|---|
| **Yok olma** | zıt çift, $d = 2(R_{\text{cep},1}+R_{\text{cep},2}) = 4R_{\text{cep}}$ | $0$ | Hendek köprülenir, $P_0$ cebi çökertir |
| **Birleşme** | eş çift, $d = R_{\text{cep},1}+R_{\text{cep},2} = 2R_{\text{cep}}$ | $2\Gamma$ | Cepler değer, tek büyük Kut |

$$\frac{d_{\text{yok}}}{d_{\text{bir}}} = 2 \quad\text{tam}$$

**Zıt çift, eş çiftten tam iki kat uzakta olay yaşar.** Bu asimetri türetilmiştir, konmamıştır.

### Eş yönlü Kutlar neden birleşmez

Akışkanlar dinamiğinde eş yönlü girdaplar ancak **ayrım/çekirdek oranı $\lesssim 3{,}2$** olursa birleşir. Kut için çekirdek $r_e$ **değil** — gerçek boşluk $R_{\text{cep}}$'tir:

| | Değer |
|---|---|
| $R_{\text{cep}}$ | $2{,}294\times10^{-5}\,r_e$ |
| Kümede tipik aralık $d$ | $\sim 1{,}4\,r_e$ |
| **Aralık/boşluk oranı** $d/R_{\text{cep}}$ | **$\approx 6{,}2\times10^{4}$** |
| Birleşme ölçütü (ayrım/çekirdek) | $< 3{,}2$ |
| **Eşikten uzaklık** | **$\sim 2\times10^{4}$ kat** |

Boşluklar, aralarındaki mesafenin yaklaşık **62 binde biri** kadardır. Ve modelin kendi eşiği ($d_{\text{bir}} = 2R_{\text{cep}}$) akışkan ölçütüyle ($3{,}2R_{\text{cep}}$) yalnız **1,60 kat** farklıdır — biri *"boşluklar değince"*, öteki *"çekirdekler ~3 yarıçap yaklaşınca"* diyor. **İki bağımsız yol aynı yeri gösteriyor.**

> **Teori açısından bu zorunludur:** Kut bölünmezdir; $g=2$ olan nesne artık Kut değildir. Bileşik sınır tabakası (12.3.7) ikilemi çözer — büyük yapılar kurulur, Kut bölünmez kalır.

---

## 12.3.6 Kümeleşme: Boyut Kendiliğinden Belirlenir

Bağ kanalı devredeyken dağınık bir Kut topluluğu ne yapar? Bu soru sayısal deneyle sınandı: 30 Kut'luk 12 bağımsız rastgele dizilim koşuldu.

| Ölçüt | Sonuç |
|---|---|
| Kümeleşme oluştu | **12/12** |
| Öbek boyutu $\le 8$ | **62/62 — istisnasız** |
| Boy histogramı | 4→7 · 5→21 · **6→22** · 7→11 · 8→1 |
| Ortalama boy | **5,65** |

**Boyut ayarlanmadı.** 5–8 aralığı, bağımsız olarak türetilen **Thomson kararlılık sınırıdır**: düzgün çokgen dizilim $N \le 7$'ye kadar kararlıdır, merkeze bir Kut konursa sınır ~10'a çıkar. İki ayrı hesap aynı sayıya düştü.

$$\Omega_N = \frac{\Gamma(N-1)}{4\pi R^2}$$

### Kalıcılık nasıl sağlanır: fırlatma

Topluluğun RMS yarıçapı tek başına yanıltıcı bir ölçüdür: bazı denemelerde *büyür* görünür. Çekirdek ayrı ölçüldüğünde tablo netleşir (14 deneme):

| | Tüm topluluk | **Çekirdek** | En uzak Kut |
|---|---|---|---|
| Normal 12 deneme | 0,34–0,48 | 0,34–0,48 | 8–10 |
| Deneme 6 | **3,35×** | **0,41** | **203** |
| Deneme 10 | **11,18×** | **0,36** | **720** |

**14 denemenin 14'ünde çekirdek büzülür.** "Yayılma" görülen durumlarda olan şey, 2–4 Kut'un 200–720 birim uzağa **fırlatılmasıdır**; kalan çekirdek aynı oranda — hatta biraz **daha sıkı** — bağlanır (fırlatanlarda ort. 0,385, fırlatmayanlarda 0,415).

> **Kalıcı kümeleşme için dış bir sönüm kanalına gerek yoktur.** Sistem fazla enerjiyi **üye atarak** boşaltır. Bu, yıldız kümelerinden bilinen buharlaşmalı soğuma mekanizmasının ta kendisidir (12.5).

---

## 12.3.7 Bileşik Sınır Tabakası ve Ölçek Değişmezliği

Sıkı bir öbek uzaktan **tek girdap** gibi görünür ve uzak alanı **iç dizilime kördür** (ölçüldü: düzgün çokgen / doğrusal dizi / yığın / rastgele küme → aynı $|v|$, fark $\sim10^{-6}$). Buradan:

$$|v| = \frac{|\Gamma_{\text{top}}|}{2\pi R} = \sqrt2\,c_0 \quad\Longrightarrow\quad \boxed{\;r_e(\text{öbek}) = \left|\sum g\right|\cdot r_e\;}$$

$N=10$ ve $N=20$'de bağıl fark $1{,}2\times10^{-16}$. **Sınır tabakası Kut sayısıyla doğrusal büyür.**

Bunun doğrudan bir sonucu daha vardır: $\Gamma_{\text{top}} = 0$ olan öbeğin bileşik tabakası **yoktur** — uzaktan **görünmez**.

### Öbekler arası mesafe de aynı ölçekte

Işımanın $g$ bağımlılığı ($M = K(|g_i|+|g_j|)/d$) hesaba katılınca eş öbeklerde ışıma $\propto N^5$, Bjerknes $\propto N^2$ olur ve:

$$d_{\text{denge}} = \left(\frac{\lambda K^5}{\kappa}\right)^{1/3}\cdot N$$

| $N$ | 1 | 2 | 4 | 7 | 10 | 20 |
|---|---|---|---|---|---|---|
| $d_{\text{denge}}/N$ | 1,414214 | 1,414214 | 1,414214 | 1,414214 | 1,414214 | 1,414214 |
| $d_{\text{denge}}/(r_e^A + r_e^B)$ | **0,7071** | 0,7071 | 0,7071 | 0,7071 | 0,7071 | 0,7071 |

> **Oran her boyutta aynıdır.** 20'lik bir öbek, tek bir Kut'la aynı bağıl mesafede durur. Bu **ölçek değişmezliğidir** ve 12.5'in ana kanıtıdır.

### Gösterimin kendi geçerliliği

Bileşik tabakayı **daire** olarak çizmek her $N$ için aynı kesinlikte değildir. Çizilen halkada $|v|$ ölçüldü:

| $N$ | $|v|$ hatası | açısal dalgalanma | yargı |
|---|---|---|---|
| 2 | %0,50 | **%28,55** | yaklaşık |
| 3 | %0,014 | %4,81 | iyi |
| 4 | %0,001 | %0,99 | tam |
| 6 | %0,000 | %0,05 | **TAM** |
| 8–20 | %0,000 | **%0,00** | **TAM** |

Belirleyici olan mesafe oranı değil **simetridir**: düzgün $N$-gende eşit aralıklı kaynakların toplamı, $N$'in katı olmayan bütün harmonikleri götürür ⟹ ilk düzeltme $N$. mertebeden ve $(R_{\text{küme}}/R_d)^N$ ile düşer.

Simülasyon bunu **kendisi ölçer ve söyler**: dalgalanma %15'in altındaysa düz yeşil halka, %15–35 arası turuncu kesikli, üstünde kırmızı noktalı — yanında sapma yazılı.

---

## 12.3.8 Momentum Nereye Gidiyor

Yok olmada ortama geçen impuls $I = \Gamma d$, $c_0$ hızıyla yayılan **dipol** desenli bir basınç darbesi olarak çıkar. İzotrop bir darbe simetri gereği net momentum taşıyamaz; lob zorunludur.

**Dipolün iki lobu da momentumu aynı yönde taşır:**

- **Ön lob** — sıkışma ($\delta\rho > 0$), Kut'u **dışa iter** → momentum $+\hat I$
- **Arka lob** — seyrelme ($\delta\rho < 0$), Kut'u **içe çeker** → momentum yine $+\hat I$

Çember üzerine yerleştirilmiş sekiz sondanın **sekizinde de** $v_y > 0$ ölçüldü; toplam $+0{,}5715$, $\sum v_x = 0$.

> Darbe Kutları **dağıtmaz**, $\hat I$ doğrultusunda **sürükler**. Her yöne iten bir darbe net momentum taşıyamazdı — korunum bunu yasaklar.

<p style="margin:20px 0;padding:16px;border:1px solid #22c55e;border-radius:10px;background:rgba(34,197,94,0.07)"><a href="Simulasyon/kisim12/kut_birlesme_yapilanma.html" target="_blank" rel="noopener" style="display:inline-block;padding:12px 22px;background:#166534;color:#ffffff;border-radius:8px;font-weight:700;text-decoration:none;font-size:1.05em">&#9654;&#65039; SİMÜLASYONU AÇ — Kutların birleşmesi ve yapılanması</a><br><span style="color:#a1a1aa;font-size:0.9em;display:inline-block;margin-top:8px">Bu kısmın ana laboratuvarı. Kutlar tek tek yerleştirilir ya da <b>⁂ KALABALIĞI SERP</b> ile onlarca Kut rastgele saçılır — her basışta yeni dizilim, çünkü kanıt gücü kümeleşmenin <b>her</b> dizilime gelmesindedir. <b>Ters Kut</b> eklenebilir ve yok olduğu, momentum darbesini bıraktığı izlenir. Bağ kanalı, ışıma katsayısı, faz farkı ve olay ölçeği canlı ayarlanır; <b>türetilmiş denge mesafesi</b> ve zıt çift için <b>kök olmadığı</b> panelde okunur. Bileşik sınır tabakaları kendi geçerliliklerini ölçüp bildirir. 4B dönüşün 3B izi sağ panelde eşzamanlı çizilir. Fare tekerleğiyle yakınlaştırma, boş alanda sürükleyerek kaydırma, ⌖ ile sığdırma; ayrıca hız ve duraklat denetimleri. <b>220 öz-sınama</b> açılışta koşar. Tek dosya, dış bağımlılık yok.</span></p>

---

## 12.3.9 Sayısal Yöntem Notu

Işıma kanalı $1/d^5$ ile ıraksadığı için denklem **katıdır (stiff)**. Sabit adımlı integrasyon yeterli değildir: sabit $h = 0{,}004$ adımıyla koşulan zıt çift 283 birime savrulur; bağımsız bir sabit adımlı koşumda ise $\kappa=10$'da topluluk yarıçapı **64,9 kat** büyür. İkisi de fiziksel değil, sayısal artefakttır.

Simülasyon bu nedenle **uyarlamalı adım** kullanır: her alt adımda CFL koşulu ($h\,v_{\max} \le 0{,}02\,d_{\min}$) yeniden hesaplanır. Bu bir iyileştirme değil, **zorunluluktur** — ve bu bölümdeki her sayı onunla üretilmiştir.
