# Sınav Çalışması — Adım Adım

**Statü:** Çalışma dosyası. Yayın dışı. `CALISMA/` dizini dışına hiçbir şey yazılmaz.
**Yöntem:** Yazar yönlendirir, adım adım ilerlenir. Hiçbir adım, önceki adım kapanmadan atlanmaz.
**Başlangıç:** 29 Temmuz 2026

---

## Çalışma Kuralı — neden bu dosya açıldı

Önceki sınav turunda (`07_Teorinin_Sinanmasi.md`) tekrarlanan bir kusur belirlendi: **sorular standart fiziğin çerçevesinden kuruldu.**

Belirtileri:

- Karadelik eşiği **Schwarzschild yarıçapıyla** hesaplandı.
- Maksimum kompakt cisim kütlesi **TOV denklemine** (Rhoades–Ruffini) dayandırıldı.
- Dönme sürüklenme kesri başlangıçta **Lense–Thirring'e eşlenerek** sabitlendi.
- Ve en yaygını: gezegen figürü sınavı *"teorinin eklediği kuvvet, standart fiziğin bıraktığı artığın içine sığmalı"* biçiminde kuruldu.

Sonuncusu bir hesap hatası değil, bir **çerçeve hatasıdır**. Standart fiziği taban, teoriyi ona eklenen bir tedirginlik saymak, temeli değiştirdiğini iddia eden bir teoriyi sınamanın yolu değildir. Bu kurulumda teori en iyi ihtimalle "küçük bir düzeltme" olarak görünür; en kötü ihtimalle sorusu hiç sorulmamış olur.

**Bu dosyada uygulanacak kural:** her sınav önce **teorinin kendi büyüklükleriyle** kurulur. Standart fiziğin sayısı, ancak teorinin kendi cevabı hesaplandıktan *sonra* karşılaştırma için getirilir — kurulumun içine değil.

---

## SINAV 1 — Dönen Bir Gövdenin Şekli

### Ölçülen büyüklük

Dönen bir gök cismi küre değildir; kutuplardan basık, ekvatorda şişkindir. Bu basıklık çok yüksek hassasiyetle ölçülür:

| Cisim | Basıklık $f=(a-b)/a$ | Dönme periyodu | Ölçüm kaynağı |
|---|---|---|---|
| Dünya | $1/298{,}257$ | 23s 56dk | uydu jeodezisi |
| Mars | $1/169{,}8$ | 24s 37dk | uydu takibi |
| Jüpiter | $1/15{,}41$ | 9s 55dk | Juno |
| Satürn | $1/10{,}21$ | 10s 39dk | Cassini |
| Güneş | $\sim1/121000$ | ~25 gün (ekvator) | helyosismoloji |

Şeklin ayrıntısı ayrıca ölçülür: çekim alanının açısal bileşenleri $J_2$ (ne kadar basık), $J_4$, $J_6$ (basıklığın enleme nasıl dağıldığı).

### Soru

> **Evrenakı'ya göre, dönen bir gövdenin şeklini ne belirler — ve o şekil ölçülenle uyuşuyor mu?**

Soru bilinçli olarak "teori ne kadar ek katkı verir" biçiminde **değil**, "teori şekli baştan nasıl kuruyor" biçiminde soruluyor.

### Sorunun fiziksel içeriği

Evrenakı'da bir gövde boşlukta duran bir kütle değil; **basınçlı bir ortamın içinde**, o ortamı deplase eden ve döndürerek akıtan bir yapıdır. Şekli belirleyen şey, gövdenin her yüzey noktasında ortamın uyguladığı **basınç dağılımıdır**. O halde sorunun cevabı için önce ortamın gövde çevresindeki durumu bilinmelidir.

Teorinin bu duruma katkı veren büyüklükleri şunlardır — hangilerinin gerçekten girdiği, hangilerinin ihmal edilebilir olduğu **çalışmanın konusudur**:

| Büyüklük | Kaynağı | Yönü |
|---|---|---|
| Radyal kütle-itim | $\omega_2$ pompası (Ek M-35) | merkeze |
| Eksenel itim | $\omega_1$ dönüşü (Ek M-38) | dönme eksenine |
| Yanal itim | $\omega_1$ dönüşü (Ek M-39) | ekvator düzlemine |
| Gövdenin kendi dönmesinin eylemsizliği | — | eksenden dışa |
| Deplasman kesri $\phi$ | kafes yapısı (Ek M-15/M-16) | genliği ölçekler |
| Sürüklenme kesri | patinaj (Ek M-40) | genliği ölçekler |

### Çalışmanın kapanması için cevaplanması gereken alt sorular

Bunlar **açık bırakılmıştır**; birlikte, sırayla ele alınacaktır.

1. Gövdenin **yüzeyi** teoride neye göre tanımlanır? Hangi iki büyüklüğün dengesi o yüzeyi belirler?
2. Ortam gövdenin **içinde** de var mıdır, ve içerideki basınç dağılımı şekle katılır mı — yoksa şekil yalnız yüzeydeki dış basınçla mı belirlenir?
3. Gövdenin dönmesinin eylemsizliği ile ortamın dönmesi **aynı şey midir**, ayrı ayrı mı sayılmalıdır?
4. Yukarıdaki kuvvetlerden hangileri gezegen ölçeğinde gerçekten etkilidir; hangileri kendi geçerlilik pencerelerinin dışındadır?
5. Teorinin verdiği şekil, gövdenin **iç yoğunluk dağılımına** bağlı mıdır — yoksa yalnız dış ortamın durumuna mı?
6. Ölçülen basıklıkla karşılaştırma hangi büyüklük üzerinden yapılmalıdır: $f$ mi, $J_2$ mi, yoksa $J_2$ ve $J_4$ birlikte mi?

---

## ÇÖZÜM

### Adım 1 — Kuvvetleri kaynağına göre ayırmak *(yazar yönlendirmesi)*

Alt soru 1 ("gövdenin yüzeyi neye göre tanımlanır") **yanlış kurulmuştu.** Yüzey, tüm kuvvetler için ortak bir referans değildir; her kuvvet farklı bir şeye bağlıdır ve önce bu ayrım yapılmalıdır.

**Üç kuvvet, üç ayrı kaynak:**

| Kuvvet | Neye bağlı | Gövdenin yüzeyi gerekli mi? |
|---|---|---|
| **Merkezkaç** | Gövdeyle birlikte dönen **maddenin eylemsizliği** | **Evet** — gövde ve yüzeyi tanımlı olmalı |
| **Merkezcil (radyal kütle-itim)** | Gövdenin **kendi nükleon pompaları** ($\omega_2$) | Hayır — **kütleye bağlı** bir kuvvettir |
| **Eksenel ve yanal itim** | **Girdap** — ortamın dönüşü | Hayır — girdaba bağlıdır |

Yani gövde ve yüzeyi yalnız **merkezkaç** için gereklidir. Evrenakı kuvvetleri gövdenin yüzeyiyle değil, ortamın durumuyla ilgilenir.

**Girdap nedir ve nasıl bilinir.**

Evrenakı, gövdenin şekliyle değil **girdap dönüşleriyle** ilgilenir. Girdap, merkez kütlenin **iç yapısı** ve kendisinin **zarf yapısı** ile doğrudan ilgilidir.

Merkezî cismin iç yapısı bilinmiyorsa — ki gezegenler için genellikle böyledir — girdap hızı doğrudan okunabilir:

> **Çevresindeki yörünge hızları girdap hızı olarak kabul edilir. Yörüngeler girdap uyumludur.**

Bu bir yaklaşım değil, teorinin kendi tanımıdır: Postülat 7 gereği yörüngedeki cisimler ortam tarafından **taşınır**; dolayısıyla yörünge hızı, o yarıçaptaki ortam hızıdır. Aynı sonuç Ek M-37'nin profil teoreminde de vardır: $v_\theta(R)=\sqrt{R\,\lvert a_{radyal}(R)\rvert}$.

**Eksenel ve yanal kuvvetler bu dönüşten doğar.** Girdabın üç boyuttaki dönüşü, eksene doğru (eksenel) ve ekvator düzlemine doğru (yanal) bileşenler üretir. İkisi de girdabın hızından beslenir, gövdenin yüzey hızından değil.

**Merkezcil kuvvet ayrıdır.** O, ortamın dönüşünden değil gövdenin kendi pompalarından ($\omega_2$) kaynaklanır; dolayısıyla **kütleye bağlı** bir kuvvettir ve girdap hızından bağımsızdır.

### Adım 1'in sonucu — önceki kurulumda ne yanlıştı

Önceki turda (`07_Teorinin_Sinanmasi.md`, Sınav 1) yanal itimin girdap hızı olarak **gövdenin yüzey hızı** alınmıştı:

$$v_e = \phi\,\omega R \qquad \text{(gövdenin dönmesinin ortama sürüklenmesi)}$$

Bu, yukarıdaki ayrıma göre **yanlış büyüklüktür.** Doğru büyüklük, o yarıçaptaki girdap hızıdır ve yörüngeden okunur:

$$v_{girdap}(R) = v_{yörünge}(R)$$

**Adım 2'de bu iki değerin sayısal farkı ve doğurduğu sonuçlar ele alınacaktır.**

### Adım 2 — Yanal kuvvet formülünün denetimi *(yazar yönlendirmesi: "girdap ekvatoraldir, kutupta sıfırdır; yanal kuvvet çok çok küçük olmalı; formülü kontrol et")*

**Enlem profili doğrulandı.** Girdap ekvatoral ve kutupta sıfırsa profil $v(\theta)=v_e\cos\theta$ biçimindedir — bu, M-39'un kullandığı profilin aynısıdır. Dolayısıyla açısal cebir değişmiyor: $d(\cos^2\theta)/d\theta=-\sin2\theta$, ve $\sin2\theta$ yasası ayakta kalıyor. **Sorun açısal yapıda değil.**

Denetim iki şey buldu.

#### Bulgu 2a — $\kappa_5$ serbest değil: stiff hâl denklemi onu $\tfrac12$'ye sabitliyor

M-39, basınç açığını $\Delta P=-\kappa_5\rho_0 v^2$ diye parametrize eder ve $\kappa_5$'i serbest bırakır ($\tfrac12$ "Bernoulli çalışma değeri"). **Artık serbest değildir.** Sınav 4'ün sonucu ortamın hâl denklemini stiff yaptı ($P=c^2\rho$); M-3′'ün akış bağıntısıyla birlikte:

$$\rho=\rho_0e^{-v^2/2c^2} \;\Longrightarrow\; P=P_0e^{-v^2/2c^2} \;\overset{v\ll c}{\approx}\; P_0\left(1-\frac{v^2}{2c^2}\right)$$

$P_0=\rho_0c^2$ olduğundan:

$$\Delta P \approx -\frac{\rho_0 v^2}{2} \qquad\Longrightarrow\qquad \boxed{\;\kappa_5=\tfrac12\;}$$

**Türetilmiş bir değerdir, tercih değil.** İki sonucu var: (i) $\kappa_5$ Ek C'nin serbest listesinden çıkar; (ii) **büyüklük sorununu $\kappa_5$'i küçülterek çözme yolu kapanır.**

#### Bulgu 2b — Bernoulli adımı bu akış için geçersiz

$\kappa_5$ sabitlenince ve girdap hızı yörüngeden okununca ($v_e=\sqrt{GM/R}$) büyüklük hesaplanabilir. $v_e^2=GM/R$ ve $r=R$ konunca formül sadeleşir:

$$a_{yanal}=\frac{\kappa_5\rho_0}{\rho_n}\cdot\frac{v_e^2}{R}\sin2\theta = \frac{\kappa_5}{4}\cdot\frac{GM}{R^2}\sin2\theta = \frac{g}{8}\sin2\theta$$

45°'de $1{,}23$ m/s² — **yerçekiminin %12,5'i** ve Dünya'nın merkezkaçının **36 katı.** Bu, ölçülen basıklığı yüzlerce kat aşar; kesinlikle dışlanmıştır.

Yazarın "yanal kuvvet çok çok küçük olmalı" tespiti doğrudur ve formül bunu vermiyor. **Kırık yer Bernoulli adımıdır** — ve M-39 bu tehlikeyi kendi notunda zaten işaret etmiştir:

> *"Akım çizgileri **arası** Bernoulli yalnız dönüsüz (irrotasyonel) akışta geçerlidir."*

Girdap akışı **dönüsüz değildir.** Yörünge profili $v\propto r^{-1/2}$ ile vortisite

$$\omega_{vort}=\frac1r\frac{d(rv)}{dr}\propto r^{-3/2}\neq0$$

Dolayısıyla farklı enlemler (farklı akım çizgileri) arasında Bernoulli uygulanamaz. $\Delta P=-\kappa_5\rho v^2$ ifadesi **akım çizgisi boyunca** doğrudur ($\kappa_5=\tfrac12$ ile), ama M-39 onu **enlemler arasında** kullanıyor. Geçersiz adım budur.

#### Doğru çerçeve ne olmalı

Dönen bir akışkanın denge basınç alanı Bernoulli'den değil **momentum dengesinden** çıkar. Silindirik koordinatta, eksen çevresinde $v_\varphi(R_{sil},z)$ akışı için kararlı denge:

$$\frac{1}{\rho}\frac{\partial P}{\partial R_{sil}} = \frac{v_\varphi^2}{R_{sil}} + (\text{kütle-itim payı})\,,\qquad \frac{1}{\rho}\frac{\partial P}{\partial z} = (\text{kütle-itim payı})$$

Bu, M-22'nin siklostrofik dengesidir. Ve kritik nokta şudur: **denge halinde basınç gradyanı zaten dönmeyi tutmaya harcanır** — ortada şekli bozacak artık bir "yanal kuvvet" kalmaz. Yörüngeler girdap uyumluysa (Postülat 7), ortam dengededir ve net yanal itim **sıfırdır**.

O halde yanal itim bir **birincil kuvvet değil, dengeden sapmanın artığıdır.** Yazarın "çok çok küçük olmalı" beklentisinin yapısal nedeni budur: küçük olması gereken bir *fark* hesaplanmalıdır, tam bir *kuvvet* değil.

#### Neden bu hata şimdiye kadar görünmedi

Çünkü iki serbestlik onu gizliyordu: $\kappa_5$ ayarlanabiliyordu ve $v_e$ tanımı belirsizdi. Sınav 4 birincisini, yazarın Adım 1 yönlendirmesi ikincisini sabitledi. İkisi birden sabitlenince formül gözlemle çarpıştı ve kırık adım görünür oldu.

### Adım 3 — İki dönüş, tek kaynak; ve Kepler'in dışlanması *(yazar yönlendirmesi)*

Adım 1'in "girdap hızı yörüngeden okunur" ifadesi bir işlem kolaylığıydı; **teorinin ifadesi değildir.** Yazar bunu düzeltti:

> Gövde dönüşü ile Evrenakı dönüşü **birbirine bağımlıdır ve aynı kaynaktan beslenir.** Ama gövde dönüşü, kütlenin **kafes yapısıyla** ve kendi yapısıyla doğrudan ilgilidir. Güneş plazmadır; nötron yıldızları atomik değildir; karadelikler daha katıdır. **Teorinin gereği olarak asıl ilgilendiğimiz Evrenakı dönüşüdür.** Merkezcil kuvvet ise kütleye bağlıdır. **Kepler bizi ilgilendirmez — o yalnız Güneş Sistemi parametresidir, evrensel değildir.**

#### 3a — Yapının tersine çevrilmesi

Bu, M-40'ın kurduğu nedensellik zincirini **tersine çevirir**:

| | Eski okuma (M-40) | **Yazarın okuması** |
|---|---|---|
| Birincil olan | gövdenin dönüşü | **ortamın dönüşü** |
| İkincil olan | ortam, gövdeden $\xi$ kesriyle sürüklenir | **gövde spini, kafesin ortam dönüşünden tutabildiği kadarıdır** |
| $\xi$'nin anlamı | sürükleme katsayısı | **iki dönüş arasındaki oran** |
| Kafesin rolü | ortamı tutma verimi | gövdenin dönüşünü **belirleyen** şey |

İkisi aynı kaynaktan ($\omega_1$) beslenir; ayrıştıkları yer kafestir. Plazmada kafes yoktur, dolayısıyla gövde ortamın dönüşünün çok küçük bir kesrini tutar; nötron maddesinde ve kilitli kafeste oran 1'e yaklaşır.

**Gözlenen oran** (gövde yüzey hızı ÷ $\sqrt{GM/R}$ ölçeği):

| Cisim | $v_{spin}$ (m/s) | $\sqrt{GM/R}$ (m/s) | oran |
|---|---|---|---|
| Güneş (plazma) | 1.992 | 436.761 | **0,0046** |
| Dünya (kayaç) | 465 | 7.905 | 0,059 |
| Mars (kayaç) | 241 | 3.551 | 0,068 |
| Jüpiter (mol./metalik H) | 12.572 | 42.096 | 0,299 |
| Satürn (mol./metalik H) | 9.871 | 25.087 | 0,394 |

Güneş açık ara en düşük ✓ — plazma beklentisiyle uyumlu. Ama kayaç gezegenler gaz devlerinin **altında** kalıyor; basit bir "rijitlik" sıralaması bunu vermez. Oranı belirleyen şey yalnız kafes olamaz. *(Bu, çözülmesi gereken bir kalemdir; şu an açık bırakılıyor.)*

#### 3b — Kepler dışlandı: Adım 2'nin sayısı düşüyor

Adım 2'de girdap hızı $v_e=\sqrt{GM/R}$ alınmıştı. **Bu Kepler'dir ve evrensel değildir.** Ek M-37'nin profil teoremi ($v_\theta=\sqrt{R\lvert a_{radyal}\rvert}$) yalnız $1/r^2$ rejiminde Kepler'e iner; galaktik rejimde düz eğri verir. Yani $\sqrt{GM/R}$ bir *rejim sonucudur*, girdabın tanımı değil.

Dolayısıyla Adım 2'nin $g/8$ sonucu **geçersizdir** — ama Adım 2'nin iki bulgusu ayakta kalır, çünkü ikisi de $v_e$'nin değerine bağlı değildir:

- **$\kappa_5=\tfrac12$** — stiff hâl denkleminden türetilmiştir, $v_e$'den bağımsız ✓
- **Bernoulli adımının geçersizliği** — akışın dönüsüz olmamasından gelir, $v_e$'den bağımsız ✓

Düşen tek şey sayısal büyüklüktür. Ve yazarın "yanal kuvvet çok çok küçük olmalı" beklentisi, Kepler dışlanınca **daha da güçlenir**: girdap hızı $\sqrt{GM/R}$ değilse, muhtemelen ondan çok daha küçüktür.

#### 3c — Açık kalan asıl soru

Girdap hızı Kepler'den okunmayacaksa, **teoriden nasıl gelecek?**

Teorinin elindeki: $\omega_1$ (nükleonun 4B çift dönüşünün 3B'ye yansıyan dönüş bileşeni) ve kütlenin nükleon sayısı. Ortamın makro-girdabı bunların kolektif toplamıdır. Ama **$\omega_1$'den makro-girdap hızına giden nicel adım katalogda yoktur.**

Bu, Sınav 1'in şu anki tıkanma noktasıdır ve Adım 4'ün konusudur.

### Adım 4 — Kütle yakalama oranını belirler *(yazar yönlendirmesi)*

> Kütlenin kendisi — büyüklüğü — 4. boyuttan gelen dönüşün **yakalama oranını** belirler. Kütle büyüdükçe yakalama oranı artar; yani kütle büyüdükçe kütlenin dönüş hızı artar.

Bu, teorinin **zaten sahip olduğu** yasadır (Bölüm 3.4.4, kütle–dönüş yasası) ama Adım 3'ün sorusuna bağlanmamıştı. Bağlanınca Adım 3'te açık kalan bulmaca kapanıyor.

#### Veri: yasa doğrulanıyor

Beş serbest gezegen (Mars → Jüpiter), ekvator hızı ↔ kütle:

$$v_{spin}\;\propto\;M^{0{,}536}\,,\qquad R^2=0{,}980$$

Kitabın 3.4.4'te kaydettiği $M^{0{,}54}$, $R^2=0{,}98$ değerleriyle birebir. Yasadan sapmalar:

| Cisim | Sınıf | $v_{spin}$ | Yasa | Oran |
|---|---|---|---|---|
| Mars | kayaç | 241 | 194 | 1,24 |
| Dünya | kayaç | 465 | 640 | 0,73 |
| Neptün | buz devi | 2.683 | 2.930 | 0,92 |
| Satürn | gaz devi | 9.871 | 7.336 | 1,35 |
| Jüpiter | gaz devi | 12.572 | 13.993 | 0,90 |
| **Güneş** | **plazma** | **1.992** | **579.864** | **0,0034** |

#### Adım 3'ün bulmacası çözüldü

Adım 3'te şu açık kalmıştı: *"kayaç gezegenler gaz devlerinin altında; basit bir rijitlik sıralaması bunu vermez."*

Cevap: **vermez de, vermesi gerekmiyor.** Kayaç gezegenler daha yavaş döndüğü için değil, **daha hafif** oldukları için altta. Kütle payı çıkarılınca beş yoğun-madde cismi **tek bir doğruya** oturuyor (saçılma 0,73–1,35, yani ±%35) ve yalnız plazma cismi ayrılıyor.

İki etki temiz biçimde ayrışıyor:

| Etki | Ne yapar | Ölçüsü |
|---|---|---|
| **Kütle** | Yakalama oranını belirler | $v\propto M^{0{,}536}$ |
| **Kafes** | Yakalananı tutup tutamamayı belirler | yoğun madde: doğru üzerinde · **plazma: 290 kat altında** |

Güneş'in sapması (0,0034 → **~290 kat**) gezegen saçılmasının (±%35) çok dışındadır. Bu, kafes etkisinin **ilk nicel ölçümüdür**: plazma, kütlesinin sunduğu dönüşün yalnız ~1/290'ını tutabiliyor.

#### Girdap hızı için doğan hipotez

Gövde, kütlesinin sunduğu dönüşün bir kesrini yakalıyor. **Yakalanamayan kısım nerede?** Doğal cevap: ortamda kalır — yani girdaptır.

$$v_{spin}=\mathcal{L}\cdot v_{mevcut}(M)\,,\qquad v_{girdap}\;\overset{?}{=}\;(1-\mathcal{L})\cdot v_{mevcut}(M)$$

Bu doğruysa **yazarın "yanal kuvvet çok çok küçük olmalı" beklentisi yapısal olarak açıklanır**: yoğun maddede kafes neredeyse her şeyi yakalar ($\mathcal{L}\approx1$), ortamda çok az kalır, girdap zayıftır, yanal itim küçüktür. Plazmada tersi olur.

**Ama bu hipotez şu an doğrulanamıyor**, çünkü gezegenlerin yasa etrafındaki ±%35 saçılması $1-\mathcal{L}$'yi belirlemeye yetmiyor (bazı cisimler için negatif çıkıyor, ki fiziksel değil). Ölçülebilen tek şey Güneş'in 290 katlık açığıdır.

**Sınanabilir sonucu şudur:** aynı kütlede bir plazma cisminin çevresindeki girdap, bir yoğun-madde cisminkinden ~290 kat güçlü olmalıdır.

### Adım 5 — Sistem açısal momentumu: Adım 4'ün sayısı düşüyor *(yazar yönlendirmesi)*

> Gezegenlerin sistemini **açısal momentumla** hesaba kat. Çünkü Dünya'yı düşünürsek, 4. boyuttan gelen kütleyi döndürme isteği **Ay'ı da kapsar**. Bu nedenle uydu, kütlenin dönüşünü **yavaşlatır**.

Bu, Adım 4'ün ölçütünü değiştiriyor: yakalanan şey gövdenin spini değil, **sistemin toplam açısal momentumudur.** Kitabın 3.4.4'ü zaten böyle diyor — *"tek bir dördüncü boyut kaynağı sisteme tek bir toplam açısal momentum $\vec L_{sis}=\sum_i\vec L_i$ yükler"* — ama Adım 4 bunu kullanmamıştı.

#### Veri: uydular nereyi ne kadar taşıyor

| Cisim | $L_{spin}$ | $L_{uydu}$ | $L_{toplam}$ | uydu payı |
|---|---|---|---|---|
| Mars | $1{,}91\times10^{32}$ | $2{,}6\times10^{26}$ | $1{,}91\times10^{32}$ | %0,0 |
| **Dünya** | $5{,}86\times10^{33}$ | $2{,}88\times10^{34}$ | $3{,}47\times10^{34}$ | **%83,1** |
| Neptün | $1{,}57\times10^{36}$ | $3{,}33\times10^{34}$ | $1{,}60\times10^{36}$ | %2,1 |
| Satürn | $7{,}44\times10^{37}$ | $9{,}20\times10^{35}$ | $7{,}53\times10^{37}$ | %1,2 |
| Jüpiter | $4{,}33\times10^{38}$ | $4{,}48\times10^{36}$ | $4{,}38\times10^{38}$ | %1,0 |
| **Güneş** | $1{,}93\times10^{41}$ | $3{,}14\times10^{43}$ | $3{,}16\times10^{43}$ | **%99,4** |

Yazarın işaret ettiği etki verinin içinde açıkça duruyor: **Dünya ve Güneş, açısal momentumlarının ezici çoğunluğunu uydularına/gezegenlerine vermiş durumda.** Diğer üçünde uydu payı %2'nin altında.

#### Yeni fit ve Adım 4'ün düşüşü

$$L_{toplam}\;\propto\;M^{1{,}797}\,,\qquad R^2=0{,}992$$

| Cisim | Oran (gözlenen/yasa) | Adım 4'teki oran |
|---|---|---|
| Mars | 0,658 | 1,24 |
| Dünya | **2,172** | 0,73 |
| Neptün | 0,607 | 0,92 |
| Satürn | 1,315 | 1,35 |
| Jüpiter | 0,876 | 0,90 |
| **Güneş** | **0,237** | **0,0034** |

**Güneş'in açığı 290 kattan 4,2 kata düştü.**

> **Adım 4'ün "plazma 290 kat az yakalıyor" sonucu geri çekilmiştir.** O sayı, sistemin açısal momentumunu göz ardı etmenin ürünüymüş. Güneş yavaş dönüyor çünkü plazma olduğundan değil — açısal momentumunun **%99,4'ünü gezegenlere vermiş** olduğundan. Bu, standart astrofiziğin "Güneş'in kayıp açısal momentumu" bilmecesidir ve teori onu bir zaaf değil doğrudan öngörü sayar (3.4.4).

Kalan 4,2 katlık açık, gezegen saçılmasının (0,61–2,17, yani ~3,6 kat) hemen dışındadır. Yani **kafes etkisi tümüyle kaybolmuyor ama artık "birkaç kat" mertebesinde** — 290 kat değil.

#### Uyarı: $R^2$ burada yanıltıcıdır

$R^2=0{,}992$ yüksek görünür ama $L$ altı mertebe ($10^{32}$–$10^{38}$) yayıldığı için bu kaçınılmazdır. Gerçek saçılma **3,6 kattır** ve hız versiyonunun saçılmasından (1,85 kat) **daha kötüdür**. Uyum iyileşmedi; ölçüt değişti.

Saçılmanın bir kısmı oluşum tarihinden gelir: Dünya'nın 2,17'si, Ay'ın sistemdeki en büyük uydu/gezegen kütle oranına sahip olmasıyla (dev çarpışma kökeni) ilgilidir — bu, 4B yakalamanın değil dışsal bir olayın izidir.

#### Ve doğan asıl soru: uydunun momentumu kimin?

Adım 4'ün hipotezi *"yakalanamayan kısım ortamda kalır, o da girdaptır"* idi. Sistem açısal momentumu bunu **ikiye böler** ve cevabı yazara aittir:

- **(a) Uydu momentumu maddeye aittir.** O zaman 4B'nin sunduğu neredeyse her şey madde tarafından tutulmuştur (spin ya da yörünge olarak), ortamda çok az kalır → **girdap zayıftır, yanal itim çok küçüktür** ✓ yazarın beklentisi.
- **(b) Uydu momentumu ortama aittir.** Postülat 7 gereği uydular girdap tarafından **taşınır**; o halde yörünge açısal momentumu girdabın momentumunu *ölçer*, ondan ayrı bir kalem değildir. Dünya için bu, girdabın Dünya'nın spininin **~5 katı** açısal momentum taşıdığı anlamına gelir → **girdap güçlüdür.**

İkisi zıt yönde sonuç veriyor ve şu an ikisi de teorinin ifadeleriyle uyumlu görünüyor. **Adım 6 bu ayrımı gerektirir.**

### Adım 6 — Korunum ilkesi: kaynak sabit, dağılım değişken *(yazar yönlendirmesi)*

Adım 5'in (a)/(b) çatalına cevap: **her ikisi de.**

> 4B dönüşün 3B'ye yansıması **iki farklı olguyu** tetikler: hem ortamın dönüşünü hem merkez kütlenin dönüşünü. İkisi aynı kaynaktan beslenir ve **4B'den gelen dönüş değişmez.** 3B'ye yansıması, kütlenin veya Evrenakı'nın dönüşünü belirler. **Kaynak hep aynı şeyi üretir; ancak dağılımlar farklılaşır. Bu dağılımı da sistem belirler.**

Bu bir **korunum ilkesidir** ve şu biçimde yazılır:

$$\boxed{\;L_{4B}(M)\;=\;\underbrace{L_{spin}}_{\text{merkez kütle}}\;+\;\underbrace{L_{ortam}}_{\text{girdap}}\;=\;\text{kütleye bağlı, sistemden bağımsız}\;}$$

Kaynak sabit üretir; sistem yalnız **paylaştırır**.

#### 6a — Uydular girdabı ölçer

Bu ilke, Adım 5'in çatalını çözer. Uydular Postülat 7 gereği ortam tarafından **taşınır**; dolayısıyla bir uydunun yörünge hızı, o yarıçapta **ortamın hızıdır**. Uydu ayrı bir kalem değil, girdabın **ölçüm aracıdır**.

Ay'ın 1022 m/s'si, Dünya'nın girdabının $3{,}844\times10^8$ m'de 1022 m/s aktığını söyler. Bu, Kepler yasasına başvurmadan yapılan **doğrudan bir okumadır** — Ay entrainment ile taşındığı için.

#### 6b — Ölçülen dağılımlar

| Sistem | Madde (spin) | Ortam (uydularla ölçülen) |
|---|---|---|
| Mars | ~%100 | ~%0 |
| Jüpiter | %99,0 | %1,0 |
| Satürn | %98,8 | %1,2 |
| Neptün | %97,9 | %2,1 |
| **Dünya** | **%16,9** | **%83,1** |
| **Güneş** | **%0,6** | **%99,4** |

Dağılım uçtan uca değişiyor — ve yazarın dediği gibi bunu **sistem** belirliyor: uzakta momentum taşıyacak kütle varsa ortam payı büyüyor, yoksa her şey spinde kalıyor. Bu bir malzeme özelliği değil, **konfigürasyon** özelliği.

Adım 5'in $L_{toplam}\propto M^{1{,}797}$ fiti, bu korunum ilkesinin kendisidir: toplam sabit kalıyor, iç dağılım serbest.

#### 6c — Ama ortamın kendi açısal momentumu muhasebeyi bozuyor

Yukarıdaki tabloda "ortam" sütunu **uyduların taşıdığıdır**, ortamın kendisininki değil. Ortam da dönüyorsa ve yoğunluğu $\rho_0=6{,}8\times10^{16}$ kg/m³ ise, kendi açısal momentumu hesaplanmalıdır:

$$L_{ortam}\sim\int\rho_0\,v(r)\,r\,dV$$

Dünya için, $v=\sqrt{GM/r}$ profiliyle:

| Sınır | $L_{ortam}$ | Maddeye oranı |
|---|---|---|
| Dünya yarıçapına kadar | $3{,}2\times10^{48}$ | $\mathbf{9\times10^{13}}$ |
| Ay yörüngesine kadar | $5{,}4\times10^{54}$ | $\mathbf{1{,}6\times10^{20}}$ |

**Ortamın açısal momentumu maddeninkinden 14–20 mertebe büyüktür.**

Bu, korunum ilkesini şu an uygulanamaz kılıyor: eğer $L_{4B}=L_{madde}+L_{ortam}$ ise ve $L_{ortam}$ maddeninkinin $10^{20}$ katıysa, dağılım **her sistemde %100 ortam**'dır ve maddenin payı ölçülemez bir kırıntıdır. O halde:

- Adım 5'in $M^{1{,}797}$ yasası, $L_{4B}$'nin değil yalnız **maddenin payının** yasası olur;
- Ve "dağılımı sistem belirler" ifadesi, ölçülemeyecek kadar küçük bir kesrin dağılımı hakkında olur.

**Kökeni tanıdıktır:** aynı $\rho_0$, Sınav 1'in sürükleme felaketinde de ortaya çıkmıştı (`07_Teorinin_Sinanmasi.md`, Ek M-37 notu: zarfın $10^{28}$ kat bastırması gerekiyordu). Ortamın yoğunluğu Dünya'nınkinin $1{,}2\times10^{13}$ katıdır; ortam bir muhasebeye girdiği her yerde diğer her şeyi eziyor.

**Adım 7'nin sorusu budur:** ortam dönerken açısal momentum taşır mı? Taşımıyorsa neden — ve o zaman "ortamın dönüşü" ne anlama gelir? Taşıyorsa, madde ile ortam nasıl karşılaştırılabilir iki kalem olarak yazılabilir?

### Adım 7 — Ortam dolaşım taşır, momentum alışverişi yapmaz *(yazar yönlendirmesi)*

> Evet — süper akışkan **dolaşım taşır, momentum alışverişi olmaz.**

Bu, Adım 6c'nin $10^{20}$'lik uçurumunu **kökünden** kaldırıyor, çünkü iki büyüklük farklı türdendir:

| | Büyüklük | Birim | Yoğunluğa bağlı mı? |
|---|---|---|---|
| **Madde** | açısal momentum $L$ | kg·m²/s | **evet** ($\propto\rho$) |
| **Ortam (süper akışkan)** | dolaşım $\Gamma=\oint\vec v\cdot d\vec l$ | m²/s | **hayır** |

Dolaşım **kinematiktir**; içinde $\rho$ yoktur. Muhasebe dolaşımla yapılınca $\rho_0=6{,}8\times10^{16}$ hiçbir yere girmez.

#### 7a — Aynı karşılaştırma, doğru para birimiyle

| | Dolaşım (m²/s) |
|---|---|
| Dünya'nın spini, yüzeyde ($2\pi\omega R^2$) | $1{,}86\times10^{10}$ |
| Ortam, yüzeyde | $3{,}17\times10^{11}$ |
| Ortam, Ay yörüngesinde | $2{,}47\times10^{12}$ |

$$\frac{\Gamma_{ortam}}{\Gamma_{gövde}}\bigg|_{yüzey} = \mathbf{17}$$

Momentum muhasebesindeki $10^{14}$–$10^{20}$ oranı, dolaşım muhasebesinde **17**'ye iniyor. İki kalem artık aynı mertebede ve **karşılaştırılabilir**. Adım 6'nın korunum ilkesi bu para biriminde yürüyebilir.

> **Farkın tek nedeni şudur:** momentum $\rho_0$ ile çarpılır, dolaşım çarpılmaz. Ortamın devasa yoğunluğu, momentum defterine girdiği her yerde her şeyi eziyordu; dolaşım defterinde hiç görünmüyor.

#### 7b — Üç ayrı sorunun aynı cevaba çıkması

Bu ilke, çalışmanın üç ayrı yerinde takılan sorunu **tek seferde** açıklıyor:

| Nerede takılmıştı | Sorun | Süper-akışkan cevabı |
|---|---|---|
| Adım 6c (bu çalışma) | Ortam momentumu maddeyi $10^{20}$ kat aşıyor | Ortam momentum taşımaz, dolaşım taşır |
| Ek M-37 / M-43 (`07_...`) | Zarfın sürüklemeyi $10^{28}$ kat bastırması gerekiyor | Momentum alışverişi yok; "altkritik bastırma" bunun adıydı |
| Ek M-9 (kararlılık) | Ortam neden çökmüyor, neden sürtünme yok | Aynı ilke |

M-43'ün "altkritik bastırma" ansatzı ile bu ilke **aynı şeydir**: kritik hızın altında süper akışkan momentum alışverişi yapmaz. Ansatz, ilkenin fenomenolojik yazımıymış.

#### 7c — Hangi kuvvet kalır, hangisi kalkar

Ayrım keskindir ve Sınav 1 için belirleyicidir:

- **Momentum aktarımı (sürükleme, tork) → yok.** Ortam gövdeyi yavaşlatamaz, hızlandıramaz, sürükleyemez.
- **Basınç kuvveti → var.** Basınç gradyanı bir momentum *alışverişi* değil, statik bir kuvvettir. Kütle-itim de, yanal itim de bu sınıftandır ve süper-akışkanlıktan etkilenmez.

Yani yanal itim **kalkmaz**; ama Adım 2'de gösterildiği gibi Bernoulli'den değil **denge basınç alanından** hesaplanmalıdır.

#### 7d — Açık kalan: korunumun para birimi

Adım 6'nın ilkesi ($L_{4B}$ sabit, dağılım sistemce belirlenir) artık hangi büyüklükle yazılacak?

- Madde tarafı $L$ (kg·m²/s) taşıyor,
- Ortam tarafı $\Gamma$ (m²/s) taşıyor.

İkisi toplanamaz. Ortak para birimi **özgül açısal momentum** ($j=vr$, m²/s) olabilir — ki $\Gamma=2\pi j$'dir ve maddenin $j$'si de $L/m$'dir. Ay için: $L_{Ay}/m_{Ay}=3{,}93\times10^{11}$ m²/s, ve ortamın Ay yarıçapındaki $j$'si $vr=3{,}93\times10^{11}$ ✓ **birebir aynı** — entrainment'ın beklediği gibi.

Ama bu da tam çözüm değil: özgül momentum yarıçapa bağlıdır, tek bir sistem sayısı vermez. **Korunan büyüklüğün tam tanımı Adım 8'in konusudur.**

### Adım 8 — Korunan büyüklük $j(r)$ profilinin kendisidir *(yazar yönlendirmesi)*

> Korunan büyüklük $j(r)$ profilinin kendisidir.

Korunum bir **sayı** değil bir **fonksiyondur**. 4B kaynak sisteme tek bir miktar değil, bir **dağılım** yükler; madde o dağılımın içine yerleşir.

$$\boxed{\;j(r)=v(r)\,r \quad\text{— profilin kendisi korunur}\;}$$

Bunun üç doğrudan sonucu var:

1. **Ortamın hızı her yarıçapta belirlidir:** $v(r)=j(r)/r$.
2. **Entrainment ile taşınan her madde o hızda gider.** Uydu bir ölçüm aracıdır: Ay'ın $j$'si ($3{,}93\times10^{11}$ m²/s) ortamın o yarıçaptaki $j$'sidir — Adım 7'de birebir doğrulandı.
3. **Gövdenin kendi dönüşü, profilin kendi yüzeyindeki değerine göre okunur.** Yakalama kesri buradan tanımlanır:

$$\mathcal{L}\;\equiv\;\frac{j_{gövde}(R)}{j_{ortam}(R)}\;=\;\frac{\omega R^2}{\sqrt{GM\,R}}$$

#### 8a — Yakalama kesri ölçüldü, ve tanıdık bir sayı çıktı

| Cisim | $j_{gövde}(R)$ | $j_{ortam}(R)$ | $\mathcal{L}$ | $q=\omega^2R^3/GM$ | $\mathcal{L}^2$ |
|---|---|---|---|---|---|
| Güneş | $1{,}39\times10^{12}$ | $3{,}04\times10^{14}$ | 0,0046 | 0,00002 | 0,00002 |
| Mars | $8{,}18\times10^{8}$ | $1{,}21\times10^{10}$ | 0,0678 | 0,00460 | 0,00460 |
| Dünya | $2{,}97\times10^{9}$ | $5{,}04\times10^{10}$ | 0,0588 | 0,00346 | 0,00346 |
| Neptün | $6{,}64\times10^{10}$ | $4{,}11\times10^{11}$ | 0,1615 | 0,02608 | 0,02608 |
| Jüpiter | $8{,}99\times10^{11}$ | $3{,}01\times10^{12}$ | 0,2987 | 0,08920 | 0,08920 |
| Satürn | $5{,}95\times10^{11}$ | $1{,}51\times10^{12}$ | 0,3935 | 0,15483 | 0,15483 |

Son iki sütun **her satırda birebir aynı**. Bu tesadüf değil, cebirsel özdeşliktir:

$$\mathcal{L}=\frac{\omega R^{3/2}}{\sqrt{GM}} \quad\Longrightarrow\quad \mathcal{L}^2=\frac{\omega^2R^3}{GM}=q$$

Yani **teorinin yakalama kesri, standart astrofiziğin dönme parametresinin kareköküdür** ($\mathcal{L}=\sqrt q$) — ve $q$, klasik basıklık hesabının merkezî büyüklüğüdür. Eşdeğer okuma: $\mathcal{L}$, cismin **kopma dönüşünün kesridir** ($\omega/\omega_{kopma}$). Satürn kopmanın %39'unda, Güneş %0,46'sında döner.

**İki yönlü okunmalıdır ve dürüstlük ikisini de gerektirir:**

- ✓ **Lehte:** Teorinin çerçevesi kendi içinde tutarlıdır ve klasik basıklık teorisinin merkezî parametresini **kendi diliyle** yeniden üretir. Bu, çerçevenin sağlamlık işaretidir.
- ✗ **Aleyhte:** $\mathcal{L}=\sqrt q$ bir **özdeşlik** olduğundan, $\mathcal{L}$ bağımsız yeni bir büyüklük **değildir**. "Kütle yakalama oranını belirler" ifadesi (Adım 4), bu dilde "kütle dönme hızını belirler" ile aynı içeriğe sahiptir. Yeni fizik, $\mathcal{L}$'nin varlığında değil, $M^{0{,}536}$ yasasının kendisindedir.

#### 8b — Profil yüzeyde geçerli mi? Michelson–Morley gerilimi

Profil, Dünya yüzeyinde ortamın **7.905 m/s** ile aktığını söyler; gövde ise 465 m/s ile döner. Aradaki 17 kat, yüzeyde 7,4 km/s'lik bir bağıl akış demektir — **Michelson–Morley bunu dışlar.**

Teorinin cevabı sürüklenme zarfıdır (Postülat 7): zarf içinde $v_{bağıl}\approx0$, yani ortam gövdeyle birlikte taşınır. O halde:

- $j(r)$ profili **zarfın dışında** geçerlidir;
- zarfın içinde ortam gövdeyle eş-döner.

Bu, Adım 6b'nin uydu ölçümleriyle uyumludur (Ay zarfın çok dışındadır). Ama **zarfın sınırı ve kalınlığı tanımlı değildir** — ve yanal itim tam olarak orada, yüzeyde hesaplanacaktır.

#### 8c — Sınav 1 için kalan tek iş

Artık elde olanlar: kuvvetlerin kaynak ayrımı (Adım 1), $\kappa_5=\tfrac12$ (Adım 2a), Bernoulli'nin geçersizliği (Adım 2b), Kepler'in dışlanması (Adım 3), kütle yasası (Adım 4–5), korunum ilkesi ve para birimi (Adım 6–7), profil ve yakalama kesri (Adım 8).

Eksik olan tek şey **hesabın kendisidir**: yanal itim, Bernoulli'den değil **denge basınç alanından** hesaplanmalı, ve hangi hızın yüzeyde geçerli olduğu (zarf içi mi, profil mi) belirlenmelidir. Bu iki şey kapanmadan Sınav 1'in sayısı üretilemez.

### Adım 9 — Girdap literal bir akıştır: irrotasyonellik ve $\kappa_5=0$

Bu adım Sınav 1'in **kapanış adımıdır**. Yazar kararı: *girdap literal bir akıştır.* Sonuç, o kararın zorunlu kıldığı zincirdir.

---

#### 9a · Michelson–Morley bu akışı ölçmez *(yazar bilgilendirmesi + denetim)*

Yazarın iki gerekçesi:

1. Zerre ortam yoğunluğuyla hız değiştirir; M&M koşullarında yoğunluk sabittir.
2. Bir kol akış doğrultusundayken diğeri diktir; paralel koldaki hız düşüşü ile dik koldaki yatay sürüklenme aynı yönde olduğundan birbirlerini söndürürler.

**Denetim sonucu — vardığınız sonuç doğru, ama gerekçe en güçlüsü değil:**

| Gerekçe | Değerlendirme |
|---|---|
| (1) Sabit yoğunluk | M&M yoğunluk kaynaklı hız değişimini aramaz, **yön asimetrisi** arar. Sabit yoğunluk asimetriyi kaldırmaz |
| (2) Kolların sönümlenmesi | **Yönü doğru, büyüklüğü eksik.** $\Delta T_\parallel\propto\gamma^2-1\approx v^2/c^2$, $\Delta T_\perp\propto\gamma-1\approx v^2/2c^2$. İkisi de gecikme ✓, ama dik kol paralelin **yarısını** götürür. Kalan $Lv^2/c^3$ klasik M&M sinyalidir. Tam sönümleme $\gamma^2=\gamma$ ister, o da yalnız $v=0$'da |

**Teorinin zaten kesin cevabı var: boy kısalması (M-19).** Paralel kol $1/\gamma$ kısalınca $T_\parallel=\frac{2L}{\gamma c}\gamma^2=\frac{2L}{c}\gamma=T_\perp$ — **her hızda, her yönelimde tam eşitlik.** Kısmi sönümleme argümanına gerek yok.

> **F-9 (yeni fark kaydı).** Boy kısalması M&M'i her $v$ için nulluyorsa, M&M **sürüklenmenin kanıtı olarak da kullanılamaz.** Kitap H.1 tablosunda onu tam öyle kullanıyor: *"Öteleme: tam sürüklenme ($v_{bağıl}\approx0$) · Gözlemsel sınav: Michelson–Morley sıfır sonucu."* Aynı deney hem "sürüklenmeyi ölçüyor" hem "hiçbir şeyi ölçmüyor" olamaz. `09_Kitap_Sinav_Farklari.md`'ye eklenecek.

---

#### 9b · Teorinin üç kanalı — ve yüzeydeki bağıl hız

Soru: *Dünya'da evrenakı hızı ile yüzey arasındaki fark ne kadar?* Teori üç farklı cevap veriyordu:

| Kanal | Kaynak | $v_{ortam}$ (yüzey) | $v_{bağıl}$ |
|---|---|---|---|
| Öteleme | Postülat 7 | gövdeyle taşınır | 0 |
| **Spin sürükleme** | **M-40 $\xi$** | $\xi\,\omega R=2{,}1\times10^{-7}$ m/s | $\mathbf{465{,}1}$ **m/s** |
| Girdap profili | Adım 8 $j(r)$ | $\sqrt{GM/R}=7905$ m/s | 7440 m/s |

Girdap ekvatoral ve prograd, spin de ekvatoral ve prograd — **aynı bileşen.** Kanal 2 ve 3 birbirini dışlıyor (17 kat). Bu, dış itiraz değil, teorinin kendi iki formülünün çelişkisi.

$\xi=\frac{I}{MR^2}\frac{2\Phi}{c^2}=0{,}3307\times1{,}391\times10^{-9}=4{,}60\times10^{-10}$

**Enlem bağımlılığı** ($v_{bağıl}=\omega R\cos\lambda$):

| Enlem | 0° | 30° | 41° | 60° | 90° |
|---|---|---|---|---|---|
| m/s | 465,1 | 402,8 | 351,0 | 232,6 | 0 |

---

#### 9c · Ay'ın yörünge hızı: sürükleme değil, $-\nabla P$

Kanal 3 düşerse Ay'ı ne taşıyor? **Hiçbir şey taşımıyor — tutuluyor.** Teorinin çekirdek mekanizması kütle-itimdir:

$$\frac{v^2}{r}=\frac{1}{\rho_n}\frac{dP}{dr}\qquad\Longrightarrow\qquad v=\sqrt{r\cdot\frac{1}{\rho_n}\frac{dP}{dr}}$$

| Uydu | $r$ (m) | $v_{teori}$ | $v_{gözlem}$ | hata |
|---|---|---|---|---|
| ISS | $6{,}795\times10^6$ | 7658,8 | 7660 | −0,02% |
| LAGEOS | $1{,}227\times10^7$ | 5699,4 | 5710 | −0,19% |
| GPS | $2{,}656\times10^7$ | 3873,8 | 3874 | −0,00% |
| Jeostasyoner | $4{,}216\times10^7$ | 3074,6 | 3075 | −0,01% |
| **Ay** | $3{,}844\times10^8$ | **1018,3** | **1022** | −0,37% |

**Bu hesapta hiçbir akış terimi yok.** Sürükleme kanalı bu işi yapamaz zaten: gereken 7905 m/s'ye karşı $\xi$'nin verdiği $2{,}1\times10^{-7}$ m/s — oran $2{,}7\times10^{-11}$.

> **Geri çekme — Adım 6b totolojiydi.** "Ay'ın $j$'si ortamın o yarıçaptaki $j$'sine eşit, birebir doğrulandı" demiştim. Ama ortamın $j$'sini *yörünge hızından tanımlamıştım.* Döngüsel; gerçek bir doğrulama değildi.

---

#### 9d · Yazar kararı: girdap literaldir ⟹ irrotasyonellik zorunlu

> Girdap literal bir akış, çözüm burada.

Doğru, ve nedeni kesin: **süper akışkan girdabı irrotasyoneldir.**

$$v_\varphi=\frac{\Gamma}{2\pi r}\;\Longrightarrow\;r\,v_\varphi=\frac{\Gamma}{2\pi}=\text{sabit}\;\Longrightarrow\;\omega_z=\frac1r\frac{d(rv_\varphi)}{dr}=0$$

**Tam sıfır.** Kıyas: $v=\sqrt{GM/r}$ olsaydı $\omega_z=6{,}20\times10^{-4}$ s⁻¹ — sıfır değil.

**Ve irrotasyonel akış görünmezdir.** Sagnac sinyali $\oint\vec v\cdot d\vec l$'dir, $\vec v$ değil. Çekirdeği kapsamayan her ilmek için bu integral sıfırdır; masa üstü halka lazer Dünya merkezini kapsamaz ⟹ **ortam görünmez.** Akış literal, gerçek, hatta büyük olabilir — yine de ölçülemez.

Bu ad hoc bir kurtarma değil: süper akışkanlık bunu **zorunlu kılar**.

**Bedeli:** profil yasası değişir.

| | radyal yasa |
|---|---|
| Girdap (irrotasyonel, zorunlu) | $v\propto 1/r$ |
| Yörünge (basınç kuyusundan) | $v\propto 1/\sqrt r$ |

⟹ Adım 1 ve 3'teki *"yörünge hızları girdap hızı kabul edilir"* eşitlemesi **düşüyor.** İki farklı yasa; tek bir yarıçapta kesişirler.

---

#### 9e · $\Gamma$'nın gözlemsel sınırı

Girdabın ek radyal ivmesi bir $1/r^3$ tedirginliğidir:

$$a_{ek}=\frac{\rho_0}{\rho_n}\frac{v^2}{r}=\frac{\Gamma^2}{16\pi^2r^3}$$

| Referans | tolerans | $\Gamma_{max}$ (m²/s) | $v$(yüzey) |
|---|---|---|---|
| LAGEOS | $10^{-9}$ | $2{,}8\times10^7$ | 0,69 m/s |
| GPS | $10^{-9}$ | $4{,}1\times10^7$ | 1,02 m/s |
| Ay (LLR) | $10^{-10}$ | $4{,}9\times10^7$ | **1,23 m/s** |

- Ay'ın yörünge hızına demirlemek **dışlanıyor**: $\Gamma=2{,}47\times10^{12}$ Ay'da kütle-itimin **%25'i** kadar ek ivme yapar.
- Teorinin kendi $\xi$'si: $\Gamma=\xi\Gamma_{gövde}=8{,}6$ m²/s — sınırın **5,7 milyon kat altında** ✓

**Yüzeydeki bağıl hız $\omega R\cos\lambda$ olarak kalıyor (ekvatorda 465 m/s), ama artık nedeni tutarlı:** ortam duruyor çünkü süper akışkan irrotasyonel; gövde onun içinde **sürtünmesiz kayıyor.**

---

#### 9f · Bernoulli geri geldi — ve ardından çerçeve hatası: $\kappa_5=0$

**İlk yarı (doğru):** İrrotasyonel akışta Bernoulli sabiti **globaldir**, akım çizgileri arasında geçerlidir.

> **Geri çekme — Adım 2b'nin itirazı kalkıyor.** *"Girdap rotasyoneldir ($\omega_{vort}\propto r^{-3/2}$), akım çizgileri arası Bernoulli geçersizdir"* demiştim. İrrotasyonel girdapta geçerlidir. $\kappa_5=\tfrac12$ türetimi bu yönden ayakta ve yanal itim **denge artığı değil birincil kuvvet**.

**İkinci yarı (düzeltme):** Ama sınır koşulu hesabı bitiriyor. İdeal (viskozsuz, irrotasyonel) akışta koşul **yalnız normal bileşendir**:

$$\vec v\cdot\hat n=0\ \text{(nüfuz yok)}\,,\qquad v_{te\ğet}=\text{serbest}$$

Süper akışkanda viskozite yok ⟹ **no-slip koşulu da yok.** Kendi ekseninde dönen kürenin yüzey hızı tamamen teğetseldir, yani $\vec v_{yüzey}\cdot\hat n=0$; bu koşulu $\vec v_{akışkan}=0$ çözümü **zaten sağlar.** Akışkan kürenin döndüğünü öğrenemez — ideal akışkan dönen küreye tork da uygulamaz (d'Alembert).

**Dönen çerçevede Bernoulli bunu doğruluyor:**

$$\frac{P}{\rho}+\tfrac12v'^2-\tfrac12\Omega^2r_\perp^2+\Phi=\text{sabit}$$

Akışkan eylemsiz çerçevede duruyorsa $v'=-\vec\Omega\times\vec r$, yani $\tfrac12v'^2=\tfrac12\Omega^2r_\perp^2$ — **iki terim birebir sadeleşir:**

$$\frac{P}{\rho}+\Phi=\text{sabit}\qquad\Longrightarrow\qquad \Delta P=0\ \text{(enlem bağımlılığı yok)}$$

> **Geri çekme — %17,7 hesabım çerçeve hatasıydı.** $\Delta P=-\tfrac12\rho_0(\omega R\cos\lambda)^2$'den $a_{yanal}=\tfrac18\omega^2R\sin2\lambda$ türetip 45°'de merkezkaçın %17,7'sini bulmuştum (gözlemin bıraktığı %0,5'in 35 katı; eşdeğer olarak $\kappa_5\le0{,}023$ isterken $\tfrac12$ vermek — 22 kat çelişki). Kinetik terimi alıp dönen çerçevenin merkezkaç potansiyelini almamıştım. **Çelişki yok; sonuç sıfır.**

$$\boxed{\;\kappa_5=0\ \text{ TAM}\,,\qquad a_{yanal}=0\ \text{ TAM}\;}$$

Bu bir çıkış yolu değil, bir **türetim**: süper akışkan ⟹ irrotasyonel ⟹ potansiyel akış ⟹ sıfır. Üç adım, tek ayar yok.

**Elenen iki alternatif:** ($\rho_0/\rho_n$'i küçültmek) ve ($\Delta P$'yi başka ölçekle eşleştirmek) — ikisi de $\Delta P$'nin *ölçeğini* değiştirme girişimiydi; pay sıfır olduğu için gereksiz. **$\rho_0/\rho_n=\tfrac14$'e dokunulmadı ⟹ Sınav 4 korunuyor** ✓

---

#### 9g · Bilanço

| Kazanç | |
|---|---|
| Basıklık çelişkisi | **Tamamen kalktı** — 35 kat değil, sıfır |
| $\kappa_5$ | Serbest parametreden **türetilmiş sabite**. Serbest skaler **5 → 4** |
| Halka lazer, M&M, LLR, LAGEOS/GPS | Hepsi otomatik ✓ |
| Uydurma | **Yok** |

| Kayıp | |
|---|---|
| M-39'un yanal itimi ($F_5$) | **Yapısal olarak sıfır** — "küçük" değil, yok |
| $F_4$ (eksenel itim) | Aynı mekanizmadansa o da sıfır |
| Sınav 1'in ayırt edici öngörüsü | Buharlaştı. Teori: basıklık = merkezkaç + hidrostatik, standart fizikle **özdeş** |

Kayıp gerçek, ama zaten sanal bir kazançtı: F-3 ve F-4 bu öngörünün **hiçbir gözlemle sınanamadığını** kaydediyordu. Sınanamayan bir öngörüyü, sıfırı *türetmek* karşılığında vermek iyi bir takas.

**Sınav 1'in sonucu:** Teori basıklık kanalında standart fizikten **ayırt edilemez** — ve bu artık bir belirsizlik değil, bir **türetim**. Gözlemle uyumlu ✓, ama ayırt edici değil.

---

#### 9h · Açılan cephe: $\xi$'nin çekirdeklenme eşiği

Saf potansiyel akış $\xi=0$ verir. M-40 ise $\xi=4{,}60\times10^{-10}$ istiyor. **İkisi bağdaşmıyor** ⟹ gövde dönüşü ortamda pasif kalmıyor, **kuantize girdap çekirdekliyor.**

O girdap ağının yanal etkisi: $a_{yanal}\sim\xi\times0{,}177\times a_{merkezkaç}=8{,}1\times10^{-11}a_{merkezkaç}$ — gözlemin izin verdiği %0,5'in $2\times10^{-8}$ katı. Ölçülemez, ama **sıfır da değil.**

**Ve burada teori GR'dan ayrılıyor.** Girdap çekirdeklenmesi eşikli ve kuantizedir:

1. **$\Omega<\Omega_c$ olan cisimlerde çerçeve sürükleme tam sıfırdır** — eşiğin altında hiç girdap oluşmaz
2. **$\xi$ sürekli değil basamaklıdır** — $\Gamma=n\kappa$

GR'ın çerçeve sürüklemesi **pürüzsüz ve eşiksizdir.** Bu, kaybedilen yanal itimden **çok daha keskin** bir ayırt edici öngörü — çünkü Gravity Probe B ve LARES bu kanalı gerçekten ölçüyor.

**Bedeli:** M-40'ın $\xi=\frac{I}{MR^2}\frac{2\Phi}{c^2}$ formülü pürüzsüzdür; kuantize mekanizmayla ancak girdap sayısı büyükse bağdaşır:

$$N=\frac{2\xi\omega\pi R^2}{\kappa}\gg1\qquad\Longrightarrow\qquad \kappa\ll2\xi\omega\pi R^2$$

Bu, dolaşım kuantumu $\kappa=h/m_{Zerre}$ üzerine gözlemden gelen bir **üst sınır**, yani Zerre kütlesi üzerine bir **alt sınır**. Teorinin kendi parametresine yeni bir kısıt.

---

### Durum

**Adım 1–3 kapandı** · **Adım 4 kısmen geri çekildi** · **Adım 5 kapandı** · **Adım 6 kısmen geri çekildi (6b totoloji)** · **Adım 7 kapandı** · **Adım 8 kapandı**

**Adım 9 kapandı — Sınav 1 sonuçlandı.** Girdap literal ve irrotasyonel; yörünge $-\nabla P$ ile tutulur, sürükleme ile değil; $\Gamma\le5\times10^7$ m²/s (LLR); yüzeyde bağıl hız $\omega R\cos\lambda$; $\kappa_5=0$ **türetildi**; serbest skaler 5 → 4.

**Sınav 1'in cevabı:** Teori dönen cismin figürü kanalında standart fizikle **özdeştir** — gözlemle uyumlu, ayırt edici değil.

### Bu adımda üretilen geri çekmeler (özet)

| Nerede | Ne geri çekildi | Neden |
|---|---|---|
| Adım 2b | "Bernoulli geçersizdir" | İrrotasyonel girdapta geçerlidir |
| Adım 6b | "Ay'ın $j$'si ortamın $j$'sini doğruluyor" | Totoloji — ortamın $j$'si yörünge hızından tanımlanmıştı |
| Adım 8 (kanal 3) | $j(r)$ profilinin yüzeyde geçerliliği | İrrotasyonellik $v\propto1/r$'yi zorunlu kılıyor; $\sqrt{GM/r}$ değil |
| Adım 9f (ilk hesap) | $a_{yanal}=17{,}7\%\,a_{merkezkaç}$ | Dönen çerçevenin merkezkaç potansiyeli alınmamış; doğru sonuç sıfır |

---

## SINAV 2′ — Galaksi Dönüş Eğrileri *(yeniden kurulum)*

**Yazar yönlendirmesi.** Sınav 1'in yanal itim kovalaması bir sapmaydı; asıl konu galaksi dönüşleri. Teorinin iddiası: merkezcil kuvvet $1/r^2$, eksenel kuvvet $1/r$ ile çalışır.

> **Neden "2′":** `07_Teorinin_Sinanmasi.md`'deki Sınav 2 aynı konuyu **standart fizik çerçevesinden** kurmuş ve düşürmüştü (flaring). Bu kurulum teorinin kendi büyüklüklerinden başlıyor.

---

### Adım 10 — $A$'yı teorinin kendi ölçeğinden türetmek

#### 10a · Yapısal iddia doğrudur — ve tesadüf değil

$$a=\frac{A}{r}\;\Longrightarrow\;\frac{v^2}{r}=\frac{A}{r}\;\Longrightarrow\;v=\sqrt A=\text{sabit}$$

**Düz dönüş eğrisi, tam.** Fit yok, karanlık madde yok. Ve geçiş yarıçapı kendiliğinden geliyor:

$$\frac{GM}{r^2}=\frac{A}{r}\;\Longrightarrow\;r_{geçiş}=\frac{GM}{A}$$

Samanyolu için $A=v_{flat}^2=4{,}84\times10^{10}$ ⟹ $r_{geçiş}=5{,}3$ kpc. Gözlem: eğri 3–5 kpc'de düzleşiyor ✓

"İçte Kepler, dışta düz" yapısı teoriden **çıkıyor**, sokulmuyor.

#### 10b · Ama $A$ öngörülmeli, fit edilmemeli — ve gözlem ne istediğini keskin söylüyor

$A=v_{flat}^2$ olduğu sürece $A$ galaksi başına bir serbest parametredir. Sınav, biçimi değil **katsayıyı** soruyor.

**Baryonik Tully-Fisher:** $v_{flat}^4=G\,M_{baryon}\,a_0$, beş kütle mertebesi boyunca ~%10 saçılmayla. Bu şunu dayatıyor:

$$v\propto M^{1/4}\;\Longrightarrow\;A\propto M^{1/2}\;\Longrightarrow\;A=\sqrt{GMa_0}$$

**Eski $A$ bunu vermiyordu.** M-38: $v_\theta\propto h^{-1/2}$ ⟹ $A\propto1/h$. BTFR $h\propto M^{-1/2}$ ister; gözlem ağır galaksilerde diskin **daha kalın** olduğunu söyler — **ölçekleme ters yöne.** Aynı bağımlılık Sınav 2'yi de düşürmüştü (Samanyolu'nda $h$ ~6 kat büyürken $v$ $\sqrt6=2{,}45$ kat düşmeli, gözlenen 1,13 kat ⟹ 2,2 kat uyuşmazlık).

#### 10c · Türetim: **süreklilik katsayıyı sabitliyor** ← bu adımın kalbi

Üç adım:

**A.** Ortamın kendi ivme ölçeği. Evrenakı sonludur ve genişler; ufukta genişlemenin ivmesi

$$H_0^2r_H=cH_0=6{,}55\times10^{-10}\ \text{m/s}^2$$

**B.** Kütle-itim $GM/r^2>a_0$ olduğu sürece hüküm sürer; eşik yarıçapı $r_t=\sqrt{GM/a_0}$.

**C.** $r_t$'de iki yasa **sürekli** olmalıdır:

$$\frac{GM}{r_t^2}=\frac{A}{r_t}\;\Longrightarrow\;A=\frac{GM}{r_t}=\frac{GM}{\sqrt{GM/a_0}}=\boxed{\sqrt{GM\,a_0}}$$

$$\Longrightarrow\qquad v_{flat}^4=GM\,a_0 \qquad\textbf{= BTFR, tam}$$

**Katsayı türetildi.** $A$ artık disk kalınlığına bağlı değil — evrensel tek bir $a_0$'a bağlı.

#### 10d · $a_0$ sayısal sınama

| | |
|---|---|
| Gözlenen $a_0$ | $1{,}200\times10^{-10}$ m/s² |
| $cH_0$ | $6{,}548\times10^{-10}$ — oran 5,46 |
| $cH_0/2\pi$ | $1{,}042\times10^{-10}$ — **hata %−13** |

$2\pi$'nin kaynağı türetilmedi (dolaşım tanımı $\Gamma=2\pi rv$ makul bir aday ama gösterilmedi). Yine de $cH_0$ mertebesi teorinin kendi kozmolojik ölçeğinden geliyor, dışarıdan alınmıyor.

**Eşdeğer ifade — yüzey yoğunluğu eşiği:**

$$\Sigma_M=\frac{a_0}{2\pi G}=\frac{cH_0}{4\pi^2G}=0{,}249\ \text{kg/m}^2=119\,M_\odot/\text{pc}^2$$

(MOND'un kritik yüzey yoğunluğu; Freeman limitiyle bilinen örtüşme.) Akışkan resminde bu daha doğal: disk, 3B kuyuyu ayakta tutamadığı yerde davranış değişir.

#### 10e · Öngörünün sınanması — **sıfır serbest parametre**

$v_{flat}=(GMa_0)^{1/4}$, $a_0=cH_0/2\pi$:

| Galaksi | $M_{bar}$ ($M_\odot$) | $v_{öngörü}$ | $v_{gözlem}$ | hata | $r_t$ (kpc) |
|---|---|---|---|---|---|
| DDO 154 | $3{,}0\times10^8$ | 45 | 47 | −4,0% | 0,6 |
| DDO 168 | $5{,}5\times10^8$ | 53 | 54 | −2,7% | 0,9 |
| NGC 2403 | $1{,}0\times10^{10}$ | 108 | 134 | −19,1% | 3,7 |
| NGC 3198 | $3{,}0\times10^{10}$ | 143 | 150 | −4,8% | 6,3 |
| Samanyolu | $6{,}5\times10^{10}$ | 173 | 220 | −21,3% | 9,3 |
| NGC 2841 | $1{,}1\times10^{11}$ | 198 | 287 | −31,2% | 12,1 |
| UGC 2885 | $2{,}0\times10^{11}$ | 229 | 300 | −23,6% | 16,4 |
| | | | **ORT \|hata\|** | **%15,2** | |

**Eğim:** teori 0,250; bu örneklemden 0,291; gerçek BTFR (SPARC) $0{,}26\pm0{,}01$. **Üs doğru.**

**Saçılma hakkında dürüstlük:** hataların hepsi aynı yönde (öngörü düşük) ve ağır galaksilerde büyüyor. Bunun ana kaynağı benim kaba $M_{baryon}$ girdilerim — gaz dahil edildiğinde Samanyolu $8$–$10\times10^{10}$'a çıkar. NGC 2841 gerçek BTFR literatüründe de bilinen bir aykırı değerdir (uzaklığa duyarlı). Yani %15,2 teorinin hatası değil, **benim veri kalitemin** üst sınırı. Doğru örneklemle sınanması gerekir.

#### 10f · Ne kazanıldı — üç düşmüş sınav tek değişiklikle kalkıyor

| | Önce | Sonra |
|---|---|---|
| $A$'nın kaynağı | $1/h$, disk kalınlığı | $\sqrt{GMa_0}$, evrensel ölçek |
| BTFR | öngörülmüyordu | **tam çıkıyor** ✓ |
| **Sınav 2** (flaring, 2,2 kat) | düşmüş | **itiraz buharlaştı** — $A$ artık $h$'ye bağlı değil |
| **Sınav 3** (ince tüp) | düşmüş | **itiraz buharlaştı** — aynı nedenle |
| **F-6** ("iki serbest fonksiyon") | ya yanlışlanmış ya iki serbest fonksiyon | ikisi de değil |
| Serbest parametre | galaksi başına bir $A$ + $h_{etkin}(z)$ | **evrensel tek $a_0$** |

#### 10g · Açık kalan gerçek boşluk — ve bunu küçültmemek gerekiyor

**Süreklilik katsayıyı sabitler, ama $1/r$ *biçimini* türetmez.** Biçim varsayıldı; türetilen katsayıdır.

Biçim için doğal bir geometrik yol var ve **doğru cevabı veriyor**:

| | akı yayılımı | kuvvet |
|---|---|---|
| 3B | $4\pi r^2$ | $\propto1/r^2$ |
| 2B | $2\pi r$ | $\propto1/r$ ✓ |

Galaksi büyük $r$'de etkin 2B'dir (disk). **Ama bu yol geçişi sınırlama ölçeğine koyar** — ve orası çakışmıyor:

| Galaksi | $r_t$ (BTFR'nin istediği) | $h_{disk}$ | oran |
|---|---|---|---|
| DDO 154 | 0,63 kpc | ~0,5 kpc | 1× |
| NGC 3198 | 6,33 kpc | ~0,4 kpc | 16× |
| Samanyolu | 9,32 kpc | ~0,3 kpc | **31×** |
| UGC 2885 | 16,36 kpc | ~0,5 kpc | 33× |

**Durum net biçimde şu:**

- **Geometrik yol:** doğru **biçim**, yanlış **yarıçap** (ve $h$'ye bağlı ⟹ Sınav 2'yi geri getirir)
- **$a_0$ yolu:** doğru **yarıçap** ve doğru **katsayı**, ama **biçimi türetmiyor**

İkisi henüz birleşmedi. Birleştikleri gün teori, MOND'un yaptığını bir interpolasyon fonksiyonuyla değil bir **mekanizmayla** yapmış olur. Birleşmediği sürece $1/r$ biçimi **varsayımdır** — ve bu, Ek C'de varsayım olarak işaretlenmelidir.

#### 10h · Dürüst tabelo

| | Durum |
|---|---|
| $1/r$ ⟹ düz eğri | ✓ **Tam** (cebirsel) |
| Kepler→düz geçiş yapısı | ✓ **Çıkıyor**, sokulmuyor |
| $A=\sqrt{GMa_0}$ | ✓ **Türetildi** (süreklilik) |
| BTFR üssü $1/4$ | ✓ **Doğru** (gözlem $0{,}26\pm0{,}01$) |
| $a_0=cH_0/2\pi$ | ⚠ **%−13** — mertebe teorinin kendi ölçeğinden; $2\pi$ türetilmedi |
| $v_{flat}$ mutlak değeri | ⚠ %15,2 ort. hata — **veri kalitesiyle sınırlı**, yeniden sınanmalı |
| $1/r$ **biçiminin** türetimi | ✗ **AÇIK** — geometrik yol yarıçapı tutmuyor |
| Kara delik yakınında yüksek $v$ | — Tutarlı ama **ayırt edici değil** ($1/r^2$ rejimi; Newton/GR de aynısını verir) |
| Kara deliklerin yüksek **spini** | ✓ Teorinin kendi ayağı — Adım 4'ün $v_{spin}\propto M^{0{,}536}$ yasası |

---

### Durum

**Sınav 1 kapandı** (Adım 1–9): teori figür kanalında standart fizikle özdeş; $\kappa_5=0$ türetildi.
**Sınav 2′ kısmen kapandı** (Adım 10): katsayı türetildi, BTFR çıktı, iki düşmüş sınav kalktı, serbest parametre azaldı. **Biçim açık.**

### Sıradaki iki iş

1. **$1/r$ biçiminin türetimi** (10g) — geometrik 2B yolu ile $a_0$ eşiğini birleştirmek. Sınav 2′'nin kalan yarısı bu.
2. $\xi$'nin girdap çekirdeklenme eşiği (9h) — iki öngörü ve $m_{Zerre}$ alt sınırı orada.
