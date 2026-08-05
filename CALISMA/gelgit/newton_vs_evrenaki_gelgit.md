# Gelgit: Klasik Diferansiyel Anlatı ve Evrenakı'nın Hidrodinamik Çözümü

Bu bölüm, gelgit olgusunu iki ayrı çerçevede inceler. Önce klasik (Newton) formülasyonun hangi niceliği hesapladığı, bu niceliğin işaretinin nereden geldiği ve kabarmayı fiilen hangi kuvvetin ürettiği adım adım ayrıştırılır. Ardından Evrenakı kuramının Kuvvet 1 (gradyan) ve Kuvvet 2 (taban sıkıştırma) çiftiyle aynı olguyu tek adımda nasıl verdiği gösterilir. Amaç, klasik matematiğin sayısal doğruluğunu tartışmak değil; o sayıların ardındaki **nedensellik zincirini** ve suyu kaldıran gerçek faili açığa çıkarmaktır.

<div style="background: #121212; padding: 20px; border-radius: 12px; border: 1px solid #404040; box-shadow: 0 10px 30px rgba(0,0,0,0.8); margin: 20px 0; text-align: center;">
<h3 style="margin-top: 0; margin-bottom: 20px; color: #fff; font-weight: 600; letter-spacing: 1px; text-shadow: 0 0 10px rgba(0, 229, 255, 0.5);">Animasyon: Klasik "Çekim" Anlatısının Açık Sorusu vs Evrenakı'nın "Basınç" Çözümü</h3>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" style="max-width: 800px; background: #050505; border: 1px solid #333; border-radius: 8px;">
<defs>
<marker id="okKirmizi" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
<path d="M 0 0 L 10 5 L 0 10 z" fill="#ef4444" />
</marker>
<marker id="okMavi" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
<path d="M 0 0 L 10 5 L 0 10 z" fill="#00e5ff" />
</marker>
<marker id="okSari" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
<path d="M 0 0 L 10 5 L 0 10 z" fill="#fde047" />
</marker>
<radialGradient id="ayGlow" cx="50%" cy="50%" r="50%">
<stop offset="0%" stop-color="#cbd5e1" stop-opacity="0.8" />
<stop offset="100%" stop-color="#cbd5e1" stop-opacity="0" />
</radialGradient>
</defs>
<line x1="400" y1="50" x2="400" y2="380" stroke="#333" stroke-width="1.5" stroke-dasharray="5 5"/>
<!-- SOL PANEL: NEWTON (ABSÜRT TABLO) -->
<text x="200" y="30" fill="#ef4444" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle">Klasik Fizik (Newton)</text>
<text x="200" y="50" fill="#9ca3af" font-family="sans-serif" font-size="12" text-anchor="middle">Çekim (Pull) Anlatısı</text>
<!-- Ay (Sol Panel) -->
<circle cx="360" cy="220" r="15" fill="url(#ayGlow)" />
<circle cx="360" cy="220" r="6" fill="#e2e8f0" />
<text x="360" y="250" fill="#cbd5e1" font-family="sans-serif" font-size="11" text-anchor="middle">Ay</text>
<!-- Dünya ve Su (Sol Panel) -->
<circle cx="200" cy="220" r="45" fill="#1e3a8a" opacity="0.6"/>
<ellipse cx="200" cy="220" rx="55" ry="40" fill="none" stroke="#60a5fa" stroke-width="2" opacity="0.8">
<animate attributeName="rx" values="45;55;45" dur="3s" repeatCount="indefinite" />
<animate attributeName="ry" values="45;40;45" dur="3s" repeatCount="indefinite" />
</ellipse>
<circle cx="200" cy="220" r="40" fill="#047857" />
<!-- Newton Kuvvet Vektörleri (Hepsi Ay'a doğru çekiyor) -->
<g stroke="#ef4444" stroke-width="2.5">
<line x1="240" y1="220" x2="300" y2="220" marker-end="url(#okKirmizi)" />
<text x="270" y="210" fill="#ef4444" font-family="sans-serif" font-size="12" text-anchor="middle">Güçlü</text>
<line x1="200" y1="220" x2="240" y2="220" stroke-width="2" marker-end="url(#okKirmizi)" opacity="0.7"/>
<line x1="160" y1="220" x2="180" y2="220" stroke-width="1.5" marker-end="url(#okKirmizi)" />
<text x="170" y="210" fill="#ef4444" font-family="sans-serif" font-size="12" text-anchor="middle">Zayıf</text>
</g>
<!-- Çelişki İşareti -->
<circle cx="130" cy="220" r="14" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4 2"/>
<text x="130" y="224" fill="#f59e0b" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">?</text>
<text x="200" y="320" fill="#ef4444" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">AÇMAZ:</text>
<text x="200" y="340" fill="#9ca3af" font-family="sans-serif" font-size="12" text-anchor="middle">Kuvvet Ay'a doğru (çekim) ise,</text>
<text x="200" y="358" fill="#9ca3af" font-family="sans-serif" font-size="12" text-anchor="middle">arka taraftaki su NEDEN ters yöne</text>
<text x="200" y="376" fill="#9ca3af" font-family="sans-serif" font-size="12" text-anchor="middle">(uzaya doğru) kabarıyor?</text>
<!-- SAĞ PANEL: EVRENAKI (HİDROLİK TABLO) -->
<text x="600" y="30" fill="#00e5ff" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle">Evrenakı Teorisi</text>
<text x="600" y="50" fill="#9ca3af" font-family="sans-serif" font-size="12" text-anchor="middle">F2 (Taban) ve F1 (Gradyan) Birleşimi</text>
<!-- Ay (Sağ Panel) -->
<circle cx="760" cy="220" r="15" fill="url(#ayGlow)" />
<circle cx="760" cy="220" r="6" fill="#e2e8f0" />
<text x="760" y="250" fill="#cbd5e1" font-family="sans-serif" font-size="11" text-anchor="middle">Ay</text>
<!-- Dünya ve Su (Sağ Panel) -->
<circle cx="600" cy="220" r="45" fill="#1e3a8a" opacity="0.6"/>
<ellipse cx="600" cy="220" rx="55" ry="40" fill="none" stroke="#60a5fa" stroke-width="2" opacity="0.8">
<animate attributeName="rx" values="45;55;45" dur="3s" repeatCount="indefinite" />
<animate attributeName="ry" values="45;40;45" dur="3s" repeatCount="indefinite" />
</ellipse>
<circle cx="600" cy="220" r="40" fill="#047857" />
<!-- Evrenakı Vektörleri -->
<g stroke="#00e5ff" stroke-width="3">
<line x1="600" y1="150" x2="600" y2="180" marker-end="url(#okMavi)">
<animate attributeName="y1" values="140;150;140" dur="3s" repeatCount="indefinite" />
</line>
<line x1="600" y1="290" x2="600" y2="260" marker-end="url(#okMavi)">
<animate attributeName="y1" values="300;290;300" dur="3s" repeatCount="indefinite" />
</line>
</g>
<text x="600" y="130" fill="#00e5ff" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Yanlardan Ezilme (F2)</text>
<text x="600" y="320" fill="#00e5ff" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Yanlardan Ezilme (F2)</text>
<g stroke="#fde047" stroke-width="2.5" stroke-dasharray="3 2">
<line x1="560" y1="220" x2="520" y2="220" marker-end="url(#okSari)" />
<line x1="640" y1="220" x2="680" y2="220" marker-end="url(#okSari)" />
</g>
<text x="520" y="200" fill="#fde047" font-family="sans-serif" font-size="11" text-anchor="middle">Basınç Yırtığı</text>
<text x="680" y="200" fill="#fde047" font-family="sans-serif" font-size="11" text-anchor="middle">Basınç Çukuru</text>
<text x="600" y="340" fill="#00e5ff" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">ÇÖZÜM:</text>
<text x="600" y="360" fill="#9ca3af" font-family="sans-serif" font-size="12" text-anchor="middle">Su uzaya "çekilmez". Yanlardan (F2)</text>
<text x="600" y="378" fill="#9ca3af" font-family="sans-serif" font-size="12" text-anchor="middle">ezilen devasa sıvı kütlesi, basıncın zayıfladığı</text>
<text x="600" y="396" fill="#9ca3af" font-family="sans-serif" font-size="12" text-anchor="middle">ön ve arka vanalardan hidrolik olarak fışkırır.</text>
</svg>
</div>

## Metinsel Argüman: Kabarmanın Faili Kimdir?

### 1. Klasik Anlatının Zayıf Halkası
Klasik fizikte kütleçekim tek yönlü bir **çekme (pull)** kuvvetidir. Gelgitte ön yüzün Ay'a doğru kabarması bu çerçeveye sorunsuz oturur: orası "daha çok çekilir". Zorluk arka yüzdedir. Ay'ın arka yüzdeki suyu uzaya doğru **itmesi** mümkün olmadığına göre, oradaki kabarma neyle açıklanacaktır? Popüler ve ders kitabı anlatısının verdiği cevap kinematiktir: *"Ay arka yüzdeki suyu değil, Dünya'nın katı gövdesini suyun altından çeker. Su geride kaldığı için uzaya kabarmış gibi görünür."*

Bu cümlenin sorunu yanlış hesap yapması değildir — klasik gelgit tensörü sayısal olarak doğrudur ve gözlemle uyuşur. Sorun, cümlenin **faili göstermemesidir.** Yönü Ay'a dönük bir vektör, tek başına bir sıvı bloğunu ters yöne yükseltemez; suyu metrelerce kaldıran iş başka bir şey tarafından yapılmak zorundadır. Bu bölümün izini sürdüğü soru budur: o "başka şey" nedir, ve klasik anlatı onu neden adlandırmaz?

### 2. Evrenakı'nın Kusursuz Hidrolik Çözümü
Evrenakı kuramında çekim yoktur, **basınç ve gradyan** vardır.
* **Kuvvet 2 (Taban Sıkıştırma):** Dünya uzayda boşlukta süzülmez; Evrenakı tarafından her yönden (ön, arka, yanlar) merkeze doğru acımasızca sıkıştırılır (Kuvvet 2).
* **Kuvvet 1 (Gradyan):** Ay'ın varlığı bu taban basıncında bir gradyan (boşluk/çukur) yaratır. 

**Nasıl Kabarır?**
Yanlardan (kutuplar ve ekvatordan) içeri doğru tam güçle bastıran Kuvvet 2, Ay-Dünya ekseninde (ön ve arka) zayıflar. Elinizle ortasından sıktığınız bir su balonu nasıl yanlardan ezilip uçlardan fışkırırsa, Dünya'nın okyanusları da tam olarak böyle davranır. 

**Sonuç:** Arka yüzdeki su uzaya doğru "çekildiği" veya "geride kaldığı" için değil, yanlardan ezilen suyun gidecek başka hiçbir yeri olmadığı için (basınç açığına doğru) **hidrolik olarak itildiği/pompalandığı** için kabarır. Vektörler uzaya doğru çeken kancalar değil, sıvıyı uçlara doğru süpüren akışkan basınçlarıdır.

---

## 3. Matematiksel Çarpışma: "Gerçek Vektörler" vs "Çerçeveye Bağlı Vektörler"

Klasik gelgit anlatısındaki asıl kırılma noktası, kütleçekim formüllerini eylemsiz çerçevede uyguladığınızda çıkan **gerçek vektörler** ile, gelgiti anlatmak için kullanılan **göreli vektörler** arasındaki farktır. Bu farkı önce kendi vektörleriyle, sonra fiziğin en temel ilkesiyle (İş ve Enerji) ortaya koyalım.

### Newton'un Kendi Vektörlerindeki Gerçek (Eylemsiz Sistem Hesaplaması)
Dünya'nın merkezini orijin $(0,0,0)$ alalım. Ay'ı $+x$ yönünde (sağda) $r$ uzaklığına yerleştirelim. Arka yüzdeki (Ay'a zıt) bir damla suyun koordinatı $x = -b$'dir.

Şimdi mutlak uzayda (herhangi bir referans kaydırması yapmadan) $x = -b$ noktasındaki suyun ivmesini hesaplayalım:
1. **Dünya'nın Kütleçekimi:** Suyu merkeze (orijine) doğru çeker. Sınır noktası $-b$'de olduğu için çekim yönü $+x$'tir.
   $\vec{a}_{Dünya} = \mathbf{+} \frac{GM_{Dünya}}{b^2} \hat{x} \quad (+g)$
2. **Ay'ın Kütleçekimi:** Ay $+x$ yönünde olduğu için suyu yine sağa, $+x$'e doğru çeker. Ay ile su arasındaki mesafe $(r - (-b)) = r+b$'dir.
   $\vec{a}_{Ay} = \mathbf{+} \frac{GM_{Ay}}{(r+b)^2} \hat{x}$

**Gerçek Net İvme:** $\vec{a}_{net} = \mathbf{+} \frac{GM_{Dünya}}{b^2} \hat{x} \mathbf{+} \frac{GM_{Ay}}{(r+b)^2} \hat{x}$

Gördüğünüz gibi, arka yüzdeki bir damla suyun üzerindeki İKİ gerçek kütleçekim ivmesi de **ARTI (+) işaretlidir ve İÇERİ (Ay'a) DOĞRU** bakmaktadır. Dışarı (uzaya) yani eksi $(-x)$ yönüne bakan HİÇBİR vektör yoktur!

Peki bu içeri bakan (+) vektörlerden nasıl dışarı doğru (-) bir kabarma çıkarılır?
Şu adımla: Ay, arka taraftaki suyu Dünya'nın merkezinden daha zayıf çektiği için ($\frac{GM}{(r+b)^2} < \frac{GM}{r^2}$), suyun $+x$ yönündeki ivmesi Dünya'nın $+x$ yönündeki ivmesinden küçüktür. Referans Dünya'nın merkezine sabitlenir ve merkez ivmesi ($\frac{GM_{Ay}}{r^2}$) denklemden çıkarılır:
$$ \vec{a}_{göreli} = \mathbf{+} \frac{GM_{Ay}}{(r+b)^2} \hat{x} \mathbf{-} \frac{GM_{Ay}}{r^2} \hat{x} \approx \mathbf{-} \frac{2GM_{Ay}b}{r^3} \hat{x} $$

İşte suyu uzaya doğru ittiği varsayılan o **EKSİ (-)** ivme budur. Bu nicelik uydurma değildir; Dünya yüzeyine göre suyun gerçekten yükseldiğini doğru biçimde betimler. Ancak betimlediği şey bir **ayrışmadır** — suya etkiyen itici bir kuvvet değil. Eksi işaret, eylemsiz çerçevede hiçbir yerde bulunmaz; yalnızca referans Dünya'nın merkezine sabitlendiğinde, iki pozitif ivmenin farkı olarak doğar. Kısacası bu vektörün işareti fizikten değil, **çerçeve seçiminden** gelir.

### Kritik Soru: Suyu Fiilen Kaldıran Kuvvet Hangisidir?
Fiziğin en temel yasasıdır: Milyarlarca ton okyanus suyunu metrelerce yukarı kaldırmak (potansiyel enerji kazandırmak) için fiziksel bir **İŞ (Work)** yapılmalıdır ve iş yapan şey gerçek bir kuvvet olmak zorundadır ($W = F \cdot x$). O halde soru nettir: klasik modelde bu işi **hangi kuvvet** yapmaktadır?

Klasik modelin dürüst cevabı, popüler anlatının verdiği cevap değildir. Suyu fiilen kaldıran, "uzaya doğru çeken eksi vektör" değil, **okyanustaki basınç gradyanıdır.** Ay'ın çekiminin okyanus boyunca farklı şiddette olması sıvıda bir gerilme yaratır; sıvı bu gerilmeyi basınç farkına çevirir; suyu yükselten de bu basınçtır. Yani klasik model kabarmayı **iki adımda** kurar:

1. Merkezin ivmesi çıkarılarak bir **fark** niceliği elde edilir (eksi vektör). Bu nicelik gerçektir, ama bir kuvvet değil, iki düşüşün farkıdır ve işareti seçilen çerçeveye bağlıdır.
2. Okyanus bu farkı, suyu gerçekten kaldıran şeye — **basınca** — dönüştürür.

Modelin zayıf yeri, işin yapılmaması değildir; iş yapılır. Zayıf yer, **birinci adımın anlatıya kuvvet diye sokulmasıdır.** Ders kitabı cümlesi olan *"Ay arka yüzü daha az çektiği için su uzaya kabarır"*, bir kuvveti değil bir defter kaydını fail gibi göstermektedir. Sizi itmeyen bir el sizi kaldırmaz — sizi kaldıran, o elin altındaki basınçtır; klasik model de bunu yapar, ama adını ikinci adıma saklar.

* **Klasik model:** İki adım. İlk adımın işareti çerçeveye bağlıdır; kaldıran kuvvet ancak ikinci adımda ortaya çıkar ve anlatıda görünmez.
* **Evrenakı:** Tek adım. Su, yanlardan (F2) uygulanan artmış basınçtan kaçarak, direncin düştüğü uçlardan (F1 gradyanı) dışarı pompalanır. Kaldıran kuvvet baştan itibaren basınçtır; ara nicelik, çerçeve seçimi ve işaret dönüşümü gerekmez.

---

## 4. Düşünce Deneyi: Üç Cisim — Eksi İşaret Neyi Betimler?

Klasik gelgit matematiğindeki çıkarma işleminin **ne verdiğini ve ne vermediğini** basit bir düşünce deneyiyle netleştirelim. 

Uzayın derinliklerinde, yan yana dizilmiş 3 tane devasa asteroit (kütle) hayal edin:
**(Cisim 1) ----- (Cisim 2 - Merkez) ----- (Cisim 3 - Çekici Büyük Kütle)**

Cisim 3 (Ay/Kara delik görevinde) çok büyük bir kütle olsun. Cisim 1 ise Cisim 2'nin arkasında, ona doğru serbestçe düşen bir gök taşı olsun. 
* Gerçekte (Mutlak uzayda) ne olur? Cisim 3'ün devasa çekimi sayesinde **her üç cisim de sağa (Cisim 3'e) doğru ivmelenir.** Kütleçekimi sadece çektiği için, ortadaki Cisim 2, solundaki Cisim 1'i kendine doğru (sağa) çeker. Kısacası hiçbir cisim diğerini geriye doğru itmez.

**Newton'un Gelgit Matematiğini Uygulayalım — Sayısal Kanıt:**

Kütleleri somutlaştıralım. Büyük Cisim 3 kütlesi $M$, Cisim 2 ve Cisim 1 kütlesi $m$ olsun ve aralarındaki mesafe $d$ olsun:

* Cisim 1'in Cisim 3'e göre ivmesi: $a_1 = \frac{GM}{(2d)^2} = \frac{GM}{4d^2}$ *(Sağa doğru, +x)*
* Cisim 2'nin Cisim 3'e göre ivmesi: $a_2 = \frac{GM}{d^2}$ *(Sağa doğru, +x)*

Her iki ivme de **artı (+), yani sağa (Cisim 3'e) doğrudur.** Kütleçekim bu iki cismi de aynı yöne çekmektedir; **hiçbiri diğerini geriye doğru itmez.** Ancak düşüş şiddetleri eşit değildir — Cisim 2 daha hızlı düşer. Bu farkın sonucunu şimdi görelim.

Şimdi klasik gelgit matematiğini uygulayalım — Cisim 2'yi referans alalım ve onun ivmesini çıkaralım:
$$\vec{a}_{göreli,1} = a_1 - a_2 = \frac{GM}{4d^2} - \frac{GM}{d^2} = \frac{GM}{d^2}\left(\frac{1}{4} - 1\right) = \mathbf{-}\frac{3GM}{4d^2}$$

Formülden çıkan sonuç **EKSİ (-)** yani sola (Cisim 3'ten uzağa) doğrudur. Oysa Cisim 3'ün kütleçekimi, Cisim 1'i hâlâ sağa doğru çekmektedir! **Gerçek vektörler sağa bakarken, Newton'un gelgit matematiği sola bakmaktadır.**

Bu sonucun ne olduğunu ve ne olmadığını kesin ayırmak gerekir. Eksi işaret **yanlış değildir**: Cisim 1 ile Cisim 2 arasındaki mesafe gerçekten büyümektedir ve bu, çerçeveden bağımsız, ölçülebilir bir gerçektir. Eksi işaretin doğru okunuşu budur — *ayrışma*.

Yanlış olan, bu ayrışmanın **"Cisim 2, Cisim 1'i kendinden uzağa itiyor"** diye anlatılmasıdır. Ortada iten hiçbir şey yoktur; her üç cisim de Cisim 3'e doğru, farklı hızlarda düşmektedir. Ayrışma, iki düşüşün *farkıdır* — bir kuvvetin yönü değil. Klasik gelgit anlatısı tam bu noktada, ayrışmayı betimleyen bir niceliği, suyu kaldıran aktif bir kuvvetmiş gibi sunmaktadır.

Aynı hesabı Cisim 2'nin ön tarafına (Cisim 3'e daha yakın bir Cisim 0) yaparsak:
$$\vec{a}_{göreli,0} = a_0 - a_2 = \frac{GM}{(0.5d)^2} - \frac{GM}{d^2} = \frac{4GM}{d^2} - \frac{GM}{d^2} = \mathbf{+}\frac{3GM}{d^2}$$

Ön taraftaki cisim de Cisim 2'den **ayrışır** ($+$). Yani ortadaki cisim, hem önündeki hem arkasındaki cisimden uzaklaşmaktadır — ve bu, gerçekten olan şeydir. Ancak "ortadaki cisim ikisini de kendinden **itiyor**" cümlesi, aynı olgunun yanlış anlatımıdır: kütleçekimi yalnızca çekmektedir, ayrışmayı doğuran şey çekimin *farklı şiddetleridir*. Gelgit matematiğinin verdiği nicelik ayrışma hızıdır; itme kuvveti değildir.

---

## 5. "Non-İnertial Referans Meşrudur" Savunmasının Kapatılması

Bu noktada klasik fizikçilerin yapacağı tek savunma şudur: *"Non-inertial (ivmeli/dönüşümlü) referans sisteminde çalışmak meşrudur. Dünya serbest düşmede olduğu için, merkezkaç (fiktif/sözde) kuvvetler ortaya çıkar ve bu fiziksel olarak kabul edilebilir."*

Bu savunmayı iki ayrı silahla kapatıyoruz:

### Silah 1: Fiktif Kuvvet Beyan Edilmeli
Fizik pratiğinde non-inertial sistemlerde çalışmak meşrudur **ancak** bu durumda denkleme eklenen fiktif (merkezkaç) kuvvetin açıkça beyan edilmesi zorunludur. Klasik gelgit anlatısı bunu yapmaz. Ders kitaplarında ve popüler anlatılarda "Ay arka tarafı daha az çektiği için okyanus uzaya doğru kabarır" diye öğretilir; fiktif kuvvetten söz edilmez. Bu, çerçeveye bağlı bir muhasebe terimini, gerçek bir kuvvetmiş gibi sunmaktır.

### Silah 2: Enerji Defteri Ancak Basınca Dönülünce Kapanır
Fiktif kuvvetler seçilen çerçeveye bağlı muhasebe terimleridir; ivmeli bir çerçevede iş yapıyormuş gibi görünebilirler, ama enerji defteri yalnızca eylemsiz çerçeveye dönüldüğünde kapanır. Eylemsiz çerçevede ise ortada tek bir itici vektör yoktur: bütün kütleçekim vektörleri Ay'a doğrudur (§3).

O halde arka yüzdeki suyu kaldıran gerçek fail nedir? Bu soruya klasik modelin verebileceği tek tutarlı cevap **basınç gradyanıdır** — yani suyu kaldıran şey, anlatıda öne sürülen "eksi vektör" değil, okyanusun kendi içinde ilettiği kuvvettir. Bu cevap verildiği anda tartışma biter: kabarmanın faili basınçtır. Evrenakı da tam olarak bunu söyler, ama basıncı ara bir çerçeve dönüşümüne gerek kalmadan, doğrudan Kuvvet 1 ve Kuvvet 2'den üretir. Klasik model doğru faile ancak ikinci adımda ulaşır; Evrenakı işe oradan başlar.

---

## 6. Özet: Neyi Reddediyoruz, Neyi Reddetmiyoruz

Aşağıdaki tablo, tartışmanın sınırını kesin biçimde çizer. Reddedilen, klasik hesabın sayıları veya tutarlılığı değildir; reddedilen, o sayıların üzerine kurulan **mekanizma anlatısıdır.**

| İddia | Klasik Cevap | Değerlendirme |
|---|---|---|
| Arka yüzdeki su neden kabarıyor? | "Dünya suyun altından Ay'a kaçıyor" | Suyu kaldıran iş, bu kinematik ifadeyle değil, ancak **basınç gradyanıyla** yapılabilir ($W = F \cdot x$); anlatı faili atlıyor |
| Vektör işareti neden eksi (-)? | "Non-inertial referans, fiktif kuvvet" | İşaret çerçeveye bağlıdır ve eylemsiz çerçevede kaybolur; üstelik popüler anlatıda fiktif kuvvet hiçbir zaman beyan edilmez |
| Matematiksel tutarlılık? | "Diferansiyel kütleçekim tensörü tutarlı" | Matematik tutarlıdır; verdiği nicelik **ayrışmadır**, itme kuvveti değil. Tutarsız olan matematik değil, ona giydirilen "uzaya itiliyor" anlatısıdır |
| Gözlemsel kanıt? | "Gelgit gözlemleniyor" | Gözlem var ama **açıklama** yanlış; aynı gözlemi Evrenakı sıfır paradoksla açıklıyor |

**Sonuç:** Klasik gelgit matematiğinin ürettiği eksi vektör, eylemsiz çerçevede hiçbir yerde görünmez; ancak Dünya merkezi referans alınıp merkezin serbest düşme ivmesi çıkarıldığında doğar. Bu nicelik gerçektir ve ayrışmayı doğru betimler — ama betimlediği şey bir **fark**tır, suyu kaldıran aktif bir kuvvet değil. Kaldırma işini klasik modelde de sonuçta okyanustaki **basınç gradyanı** yapar; fark niceliği yalnızca o gradyana giden ara bir defter kaydıdır ve kendi başına bir enerji kaynağı değildir.

Evrenakı'nın üstünlük iddiası bu nedenle "onların eksi işareti sahtedir" değildir. İddia şudur: klasik model kabarmayı iki adımda kurar ve ilk adımı, fiziksel karşılığı yalnızca seçilen çerçevede tanımlı bir farktır; Evrenakı ise aynı kabarmayı tek adımda, baştan basınç olarak üretir. Kuvvet 2'nin yanlardan uyguladığı taban sıkıştırması ile Kuvvet 1'in açtığı gradyan, ön ve arka uçtaki iki kabarmayı da tek ve aynı hidrodinamik mekanizmadan, ek varsayım veya çerçeve seçimi gerektirmeden verir.

---

## Kaynakça

1. Newton, I. (1687). *Philosophiæ Naturalis Principia Mathematica*, Kitap III — gelgitlerin ilk diferansiyel ele alınışı.
2. Butikov, E. I. (2002). "A dynamical picture of the oceanic tides." *American Journal of Physics*, 70(9), 1001–1011. — Gelgit kabarmalarının, radyal bileşenden çok teğetsel bileşen ve akış tarafından belirlendiğini gösteren çalışma.
3. Cartwright, D. E. (1999). *Tides: A Scientific History.* Cambridge University Press. — Gelgit açıklamalarının tarihsel gelişimi ve klasik anlatının yerleşmesi.
4. Melchior, P. (1983). *The Tides of the Planet Earth*, 2. baskı. Pergamon Press. — Katı Dünya ve okyanus gelgitlerinin ölçüm temelli incelenmesi.
5. Agnew, D. C. (2015). "Earth Tides." *Treatise on Geophysics*, Cilt 3, Elsevier. — Gelgit potansiyeli ve gözlemsel karşılıkları.
6. Misner, C. W., Thorne, K. S. & Wheeler, J. A. (1973). *Gravitation.* W. H. Freeman. — Jeodezik sapma ve gelgit tensörünün çerçeveden bağımsız niteliği.
7. Lowrie, W. (2007). *Fundamentals of Geophysics*, 2. baskı. Cambridge University Press. — Gelgit kuvvetlerinin jeofiziksel formülasyonu.
