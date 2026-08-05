# Taslak: Klasik Gelgit Açmazı ve Evrenakı Çözümü

Bu taslak belge, klasik (Newton) fiziğin gelgiti açıklarken düştüğü kavramsal açmazı — özellikle kuvvet vektörlerinin yönü ile sıvının fiziksel davranışı arasındaki uyumsuzluğu — ve Evrenakı teorisinin Kuvvet 1 (Gradyan) ve Kuvvet 2 (Sıkıştırma) ile sunduğu kusursuz hidrodinamik çözümü karşılaştırmak için hazırlanmıştır. Ana metinlere yedirmeden önce üzerinde çalışabilmemiz için taslak olarak oluşturulmuştur.

<div style="background: #121212; padding: 20px; border-radius: 12px; border: 1px solid #404040; box-shadow: 0 10px 30px rgba(0,0,0,0.8); margin: 20px 0; text-align: center;">
<h3 style="margin-top: 0; margin-bottom: 20px; color: #fff; font-weight: 600; letter-spacing: 1px; text-shadow: 0 0 10px rgba(0, 229, 255, 0.5);">Animasyon: Newton'un "Çekim" Çelişkisi vs Evrenakı'nın "Basınç" Çözümü</h3>
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
<text x="200" y="50" fill="#9ca3af" font-family="sans-serif" font-size="12" text-anchor="middle">Çekim (Pull) Yanılgısı</text>
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

## Metinsel Argüman: Klasik Model Neden Yanlışlanmalıdır?

### 1. Newton'un "Çekim" Açmazı
Klasik fiziğe göre kütleçekim tek yönlü bir **çekme (pull)** kuvvetidir. Gelgitte ön yüz Ay'a doğru kabarır çünkü "daha çok çekilir". Ancak arka yüzdeki okyanusun kabarması bu mantıkla açıklanamaz: Ay'ın arka yüzdeki suyu uzaya doğru **itmesi** fiziksel olarak imkansızdır. Newton fiziği bu saçmalığı şu kinematik illüzyonla yamamaya çalışır: *"Ay arka yüzdeki suyu değil, Dünya'nın katı gövdesini suyun altından çeker. Su geride kaldığı için uzaya kabarmış gibi görünür."*

Bu açıklama hidrodinamiğin temel yasalarını yok sayar. Yönü Ay'a dönük olan bir vektör (daha zayıf da olsa çekim kuvveti), bir sıvı bloğunu zıt yöne fışkırtamaz. Klasik modelin gelgit tensörü matematiksel olarak tutarlı rakamlar verse de, **vektörlerin nedenselliği tamamen yanlıştır.**

### 2. Evrenakı'nın Kusursuz Hidrolik Çözümü
Evrenakı kuramında çekim yoktur, **basınç ve gradyan** vardır.
* **Kuvvet 2 (Taban Sıkıştırma):** Dünya uzayda boşlukta süzülmez; Evrenakı tarafından her yönden (ön, arka, yanlar) merkeze doğru acımasızca sıkıştırılır (Kuvvet 2).
* **Kuvvet 1 (Gradyan):** Ay'ın varlığı bu taban basıncında bir gradyan (boşluk/çukur) yaratır. 

**Nasıl Kabarır?**
Yanlardan (kutuplar ve ekvatordan) içeri doğru tam güçle bastıran Kuvvet 2, Ay-Dünya ekseninde (ön ve arka) zayıflar. Elinizle ortasından sıktığınız bir su balonu nasıl yanlardan ezilip uçlardan fışkırırsa, Dünya'nın okyanusları da tam olarak böyle davranır. 

**Sonuç:** Arka yüzdeki su uzaya doğru "çekildiği" veya "geride kaldığı" için değil, yanlardan ezilen suyun gidecek başka hiçbir yeri olmadığı için (basınç açığına doğru) **hidrolik olarak itildiği/pompalandığı** için kabarır. Vektörler absürt bir şekilde uzaya doğru çeken kancalar değil, sıvıyı uçlara doğru süpüren akışkan basınçlarıdır.

---

## 3. Matematiksel Çarpışma: "Gerçek Vektörler" vs "Matematiksel Hile"

Newton fiziğinin gelgit açıklamasındaki asıl skandal, kendi kütleçekim formüllerini uyguladığınızda çıkan **gerçek vektörler** ile, gelgiti kurtarmak için uydurdukları **göreli vektörler** arasındaki uçurumdur. Şimdi bu savunmayı kendi vektörleriyle ve fiziğin en temel ilkesiyle (İş ve Enerji) ezip geçelim. Kesin olarak savunabilecekleri hiçbir şey kalmayacak.

### Newton'un Kendi Vektörlerindeki Gerçek (Eylemsiz Sistem Hesaplaması)
Dünya'nın merkezini orijin $(0,0,0)$ alalım. Ay'ı $+x$ yönünde (sağda) $r$ uzaklığına yerleştirelim. Arka yüzdeki (Ay'a zıt) bir damla suyun koordinatı $x = -b$'dir.

Şimdi mutlak uzayda (herhangi bir referans kaydırması yapmadan) $x = -b$ noktasındaki suyun ivmesini hesaplayalım:
1. **Dünya'nın Kütleçekimi:** Suyu merkeze (orijine) doğru çeker. Sınır noktası $-b$'de olduğu için çekim yönü $+x$'tir.
   $\vec{a}_{Dünya} = \mathbf{+} \frac{GM_{Dünya}}{b^2} \hat{x} \quad (+g)$
2. **Ay'ın Kütleçekimi:** Ay $+x$ yönünde olduğu için suyu yine sağa, $+x$'e doğru çeker. Ay ile su arasındaki mesafe $(r - (-b)) = r+b$'dir.
   $\vec{a}_{Ay} = \mathbf{+} \frac{GM_{Ay}}{(r+b)^2} \hat{x}$

**Gerçek Net İvme:** $\vec{a}_{net} = \mathbf{+} \frac{GM_{Dünya}}{b^2} \hat{x} \mathbf{+} \frac{GM_{Ay}}{(r+b)^2} \hat{x}$

Gördüğünüz gibi, arka yüzdeki bir damla suyun üzerindeki İKİ gerçek kütleçekim ivmesi de **ARTI (+) işaretlidir ve İÇERİ (Ay'a) DOĞRU** bakmaktadır. Dışarı (uzaya) yani eksi $(-x)$ yönüne bakan HİÇBİR vektör yoktur!

Peki Newtoncular bu içeri bakan (+) vektörlerden nasıl dışarı doğru (-) bir kabarma çıkarırlar?
Şu matematiksel hileyle: Ay, arka taraftaki suyu Dünya'nın merkezinden daha zayıf çektiği için ($\frac{GM}{(r+b)^2} < \frac{GM}{r^2}$), suyun $+x$ yönündeki ivmesi Dünya'nın $+x$ yönündeki ivmesinden küçüktür. 
Sisteme fiktif bir merkezkaç kuvveti ekleyerek Dünya'nın merkez ivmesini ($\frac{GM_{Ay}}{r^2}$) denklemlerden çıkartırlar:
$$ \vec{a}_{göreli} = \mathbf{+} \frac{GM_{Ay}}{(r+b)^2} \hat{x} \mathbf{-} \frac{GM_{Ay}}{r^2} \hat{x} \approx \mathbf{-} \frac{2GM_{Ay}b}{r^3} \hat{x} $$

İşte suyu uzaya doğru ittiği varsayılan o sihirli **EKSİ (-)** ivme budur. Gerçekte uzaya iten hiçbir fiziksel kuvvet yoktur; o eksi işaret, denklemde büyük bir pozitif sayıyı küçük bir pozitif sayıdan çıkardıkları için (sırf referansı merkeze sabitlemek uğruna) ortaya çıkan matematiksel bir illüzyondur.

### Öldürücü Darbe: "Kuvvet Eksikliği" İş Yapamaz!
Fiziğin en temel yasasıdır: Milyarlarca ton okyanus suyunu yerçekimine karşı metrelerce yukarı kaldırmak (potansiyel enerji kazandırmak) için fiziksel bir **İŞ (Work)** yapılmalıdır. İş yapmak için ise gerçek bir fiziksel kuvvetin suyu itmesi veya çekmesi gerekir ($W = F \cdot x$).

Newton matematiğinin itiraf ettiği şey şudur: Arka yüzdeki suyun kabarmasının sebebi Ay'ın onu çekmesi değil, Ay'ın onu **YETERİNCE ÇEKMEMESİDİR** (kuvvet zafiyeti). 
İşte Newton modelinin iflas ettiği nokta tam burasıdır: **Bir kuvvetin "eksikliği" veya "yokluğu" fiziksel bir iş yapamaz!** Sizi itmeyen bir el, sizi havaya kaldıramaz. Dünya suyun altından kayıyor demek, kinematik bir illüzyondur. Suyu yukarı kaldırıp kabartacak enerjiyi (basıncı) üretecek aktif bir fiziksel kuvvet Newton'un denkleminde yoktur. Sırf ivmelerin farkını aldılar diye, ortaya çıkan o hayali "eksi vektör" okyanusu kaldıran bir enerjiye dönüşemez.

* **Klasik matematik** *"Su (Dünya altından kaydığı için) uzaya doğru çekilir"* der ki bu absürt bir paradokstur.
* **Evrenakı matematiği** *"Su, yanlardan (F2) uygulanan artmış basınçtan kaçmak için, direncin düştüğü uçlardan (F1 gradyanı) dışarı pompalanır"* der. Hem matematiği hem vektörleri fiziksel nedenselliğe %100 oturur.

---

## 4. Düşünce Deneyi: "Üç Cisim Paradoksu" ve Newton'un Anti-Yerçekimi İllüzyonu

Newton fiziğinin gelgit matematiğindeki (referans kaydırarak çıkarma yapma) mantık hatasını bir düşünce deneyiyle tamamen çıplak bırakalım. 

Uzayın derinliklerinde, yan yana dizilmiş 3 tane devasa asteroit (kütle) hayal edin:
**(Cisim 1) ----- (Cisim 2 - Merkez) ----- (Cisim 3 - Çekici Büyük Kütle)**

Cisim 3 (Ay/Kara delik görevinde) çok büyük bir kütle olsun. Cisim 1 ise Cisim 2'nin arkasında, ona doğru serbestçe düşen bir gök taşı olsun. 
* Gerçekte (Mutlak uzayda) ne olur? Cisim 3'ün devasa çekimi sayesinde **her üç cisim de sağa (Cisim 3'e) doğru ivmelenir.** Kütleçekimi sadece çektiği için, ortadaki Cisim 2, solundaki Cisim 1'i kendine doğru (sağa) çeker. Kısacası hiçbir cisim diğerini geriye doğru itmez.

**Newton'un Gelgit Matematiğini Uygulayalım — Sayısal Kanıt:**

Kütleleri somutlaştıralım. Büyük Cisim 3 kütlesi $M$, Cisim 2 ve Cisim 1 kütlesi $m$ olsun ve aralarındaki mesafe $d$ olsun:

* Cisim 1'in Cisim 3'e göre ivmesi: $a_1 = \frac{GM}{(2d)^2} = \frac{GM}{4d^2}$ *(Sağa doğru, +x)*
* Cisim 2'nin Cisim 3'e göre ivmesi: $a_2 = \frac{GM}{d^2}$ *(Sağa doğru, +x)*

Her iki ivme de **artı (+), yani sağa (Cisim 3'e) doğrudur.** Newton'un kütleçekimi bu iki cismi de aynı yöne çekmektedir. Gerçek fizik net: **Hiçbiri diğerinden uzaklaşmaz.**

Şimdi klasik gelgit matematiğini uygulayalım — Cisim 2'yi referans alalım ve onun ivmesini çıkaralım:
$$\vec{a}_{göreli,1} = a_1 - a_2 = \frac{GM}{4d^2} - \frac{GM}{d^2} = \frac{GM}{d^2}\left(\frac{1}{4} - 1\right) = \mathbf{-}\frac{3GM}{4d^2}$$

Formülden çıkan sonuç **EKSİ (-)** yani sola (Cisim 3'ten uzağa) doğrudur. Oysa Cisim 3'ün kütleçekimi, Cisim 1'i hâlâ sağa doğru çekmektedir! **Gerçek vektörler sağa bakarken, Newton'un gelgit matematiği sola bakmaktadır.**

Yani bu matematiksel çıkarma işlemi, gerçekte Cisim 3'e doğru koşan Cisim 1'in, sanki Cisim 2'den "kaçıyor" veya "itiliyormuş" gibi davrandığını söyler. Bu, kütleçekiminin kendisini inkâr etmektir.

Aynı hesabı Cisim 2'nin ön tarafına (Cisim 3'e daha yakın bir Cisim 0) yaparsak:
$$\vec{a}_{göreli,0} = a_0 - a_2 = \frac{GM}{(0.5d)^2} - \frac{GM}{d^2} = \frac{4GM}{d^2} - \frac{GM}{d^2} = \mathbf{+}\frac{3GM}{d^2}$$

Ön taraftaki cisim Cisim 2'den **pozitif (+) yani ayrışır** şekilde çıkıyor. Newton'un kendi matematiğine göre ortadaki cisim (Dünya/Cisim 2), hem önündeki hem de arkasındaki cisimleri kendinden **uzağa doğru iter.** Kütleçekiminin sadece çektiği bir evrende bu sonuç fiziksel bir saçmalıktır; salt koordinat hilesi budur.

---

## 5. "Non-İnertial Referans Meşrudur" Savunmasının Kapatılması

Bu noktada klasik fizikçilerin yapacağı tek savunma şudur: *"Non-inertial (ivmeli/dönüşümlü) referans sisteminde çalışmak meşrudur. Dünya serbest düşmede olduğu için, merkezkaç (fiktif/sözde) kuvvetler ortaya çıkar ve bu fiziksel olarak kabul edilebilir."*

Bu savunmayı üç ayrı silahla kapatıyoruz:

### Silah 1: Fiktif Kuvvet Beyan Edilmeli
Fizik pratiğinde non-inertial sistemlerde çalışmak meşrudur **ancak** bu durumda denkleme eklenen fiktif (merkezkaç) kuvvetin açıkça beyan edilmesi zorunludur. Klasik gelgit anlatısı bunu yapmaz. Ders kitaplarında ve popüler anlatılarda "Ay arka tarafı daha az çektiği için okyanus uzaya doğru kabarır" diye öğretilir; fiktif kuvvetten söz edilmez. Bu, fiziksel bir illüzyonu, gerçek bir kuvvetmiş gibi sunmaktır.

### Silah 2: Fiktif Kuvvet Enerji Üretemez
Fiktif (sözde) kuvvetler, yalnızca koordinat dönüşümünün matematiksel bir yapay ürünüdür. Gerçek bir enerji kaynağına sahip değildirler. Milyarlarca ton okyanus suyunu yerçekimine karşı metrelerce kaldırmak için gerçek bir enerji kaynağı şarttır. Eğer "enerjiyi Ay sağlıyor" derlerse o zaman şunu sorun: Ay, arka taraftaki suyu çekmek için gerçek anlamda iş yapmaktadır ama yönü içeri (Ay'a doğru) değil midir? Ay'a doğru çekilen su nasıl oluyor da tam ters yönde yukarı kalkıyor? Yanıt veremezmler.

### Silah 3: Gerçek Gözlem Testi — Geoid Çelişkisi
Eğer Newton'un modeli doğruysa (Ay, Dünya'nın katı gövdesini suyun altından çekiyor), o zaman uzun vadede Dünya'nın katı kabuğunun da Ay yönünde hafifçe yükselmesi ve Ay'ın zıt tarafında da kabarması beklenir. Ancak Dünya'nın gerçek şekli olan **Geoid** ölçüldüğünde şu tablo ortaya çıkar: Dünya'nın şekli, katı kabuk üzerindeki **yerçekimi potansiyeli yüzeyi** tarafından belirlenir ve bu yüzey, sıvı basıncına göre şekillenir. Jeodezi bize, gelgidin Dünya'nın katı kabuğunu gerçekten deforme ettiğini göstermektedir, fakat bu deformasyon milimetre mertebesindedir ve Ay'ın sözde "eksi vektörle uzağa ittiği" yönde değil, doğrudan **Ay'a doğru** çekme yönündedir. Newton modeli bu gözlemle bile çelişir: Katı kabuğu Ay yönünde çeken kuvvet de eksi değil artı olduğu için Geoid şekli Newton'un gelgit modeliyle değil, gerçek kütleçekim potansiyeliyle açıklanmaktadır.

---

## 6. Kesin Özet: Newton'un Savunabileceği Hiçbir Şey Kalmadı

| İddia | Newton'un Cevabı | Çürütme |
|---|---|---|
| Arka yüzdeki su neden kabarıyor? | "Dünya suyun altından Ay'a kaçıyor" | Kuvvet eksikliği iş yapamaz ($W = F \cdot x$, $F=0$ ise $W=0$) |
| Vektör işareti neden eksi (-)? | "Non-inertial referans, fiktif kuvvet" | Fiktif kuvvet enerji üretemez; ve hiçbir zaman açıkça beyan edilmez |
| Matematiksel tutarlılık? | "Diferansiyel kütleçekim tensörü tutarlı" | Aynı matematiği 3 cisme uygulayınca kütleçekimi birbirinden uzaklaştırır — saçmalık |
| Gözlemsel kanıt? | "Gelgit gözlemleniyor" | Gözlem var ama **açıklama** yanlış; aynı gözlemi Evrenakı sıfır paradoksla açıklıyor |

**Sonuç:** Klasik kütleçekim modelinde gelgiti açıklamak için kullanılan diferansiyel (fark) ivme matematiği, eylemsiz bir referans sisteminde uygulandığında sıfır eksi vektör üretir. Eksi vektörü elde etmek için sisteme fiktif bir kuvvet eklenmesi zorunludur; bu da enerjisiz bir koordinat hilesidir. Aynı matematiksel operasyon keyfi 3 cisme uygulandığında kütleçekiminin birbirini itmesine yol açar. Bu, Newton'un gelgit açıklamasının fiziksel bir temeli olmadığını, koordinat matematiğinin gözlemi yamama girişiminden ibaret olduğunu kesin ve tartışmasız biçimde kanıtlar.
