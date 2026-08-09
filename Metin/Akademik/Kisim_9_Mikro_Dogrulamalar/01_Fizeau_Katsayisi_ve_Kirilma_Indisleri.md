# 9.1 Fizeau Katsayısı ve Kırılma İndislerinin Doğrulaması

Işığın saydam maddede yavaşlaması ($c/n$), akan maddenin ışığı **kısmen** sürüklemesi (Fizeau, 1851) ve buna rağmen Dünya'nın hareketinin eşit kollu interferometrede **hiç** iz bırakmaması (Michelson & Morley, 1887) — optiğin bu üç ölçümü, on dokuzuncu yüzyılın bütün ortam kuramlarını öldüren tarihî üçlüdür. Kısım 2.6 ve 3.4.6 bu olguların **mekanizmasını** kurmuştu: ışık kütleli Zerrelerin katarıdır, hızı yerel Kavrama Yasası $c=\sqrt{P/\rho}$ ile belirlenir (M-1) ve saydam madde, moleküllerinin deplase ettiği hacim kesri $\phi$ kadar bir **düşük Evrenakı-basıncı** bölgesidir. Türetimler Ek M Blok D'dedir (M-15…M-18). Bu bölümün görevi mekanizma anlatmak değil, **doğrulamaktır**: kurulmuş mekaniğin sayıları ölçüm literatürüyle tek tek karşılaştırılır ve — bölümün asıl vuruşu — **durgun** ortamda ölçülen kırılma indisinin sabitlediği tek bir hacim kesrinin ($\phi$), **akan** ortamdaki sürüklemenin bütün nicel içeriğini **sıfır yeni parametreyle** ürettiği gösterilir: $f=\phi=1-1/n^2$.

Kırılma indisi böylece salt bir optik katsayı olmaktan çıkar: $n$, yerel Evrenakı havuzunun fiziksel bir özelliğidir — ortamın basınç-iletim hızının, moleküler deplasmanla ne kadar düşürüldüğünün doğrudan ölçüsü.

## 9.1.1 Doğrulanacak Gözlem Envanteri

Bu olgu ailesinin, herhangi bir modelin hesap vermek zorunda olduğu ölçülmüş içeriği şudur:

| # | Gözlem | Ölçülen değer / davranış | Kaynak |
|---|---|---|---|
| G-1 | Kırılma indisleri ve Snell yasası | su $n=1{,}3330$; CS₂ $1{,}63$; hava $1{,}000293$ | standart optik tabloları |
| G-2 | Işık suda **yavaşlar**: $c_{su}=c/n$ | doğrudan hız ölçümü; Newton tanecik kuramının "suda daha hızlı" öngörüsünü çürüttü | Foucault, 1850 |
| G-3 | Akan su ışığı **kısmen** sürükler | $f\approx0{,}48$ (kaba); tam sürükleme ($f=1$) ve sıfır sürükleme dışlanır; **hava kolunda sürükleme yok** | Fizeau, 1851 |
| G-4 | Hassas tekrar | $f = 0{,}434 \pm 0{,}020$ | Michelson & Morley, 1886 |
| G-5 | Dispersiyon düzeltmesi ve uzunluk bağımsızlığı | Lorentz'in $\frac{\omega}{n}\frac{dn}{d\omega}$ terimi işaretiyle ölçüldü; katsayı boru boyundan bağımsız | Zeeman, 1914–1922 |
| G-6 | Eşit kollu interferometrede yön anizotropisi **sıfır** | beklenen 30 km/s'lik "rüzgâr" yerine sıfırla uyumlu sonuç | Michelson & Morley, 1887 |
| G-7 | Ortamdan çıkan ışık **gecikmesiz** boşluk hızına döner | geçilen ortamın "hafızası" yok | standart optik |

G-3 ile G-6'nın birlikteliği envanterin tarihî tuzağıdır: kısmi sürükleme, ışığı taşıyan bir ortam **ister**; sıfır anizotropi, o ortamın rüzgârını **yasaklar**. Statik esir Fizeau'yu açıklar, M&M'de ölür; tam sürüklenen esir M&M'i açıklar, Fizeau'da ölür. Herhangi bir ortam kuramı bu iki ölçümü **aynı anda** vermek zorundadır — yüzleşme 9.1.5'tedir.

## 9.1.2 Kırılma İndisi Ayağı: $1/n^2 = 1-\phi$

M-15'in türetimi üç homojenleştirme girdisinden yürür (üçü de teorinin başka yerlerinde bağımsızca kuruludur): **(G1)** moleküller Evrenakı'yı yaratmaz/yok etmez, yalnız deplase eder — hacimce ortalama yoğunluk arka plan değerinde kalır ($\bar\rho_m=\rho_0$); **(G2)** her molekül, hacim kesri $\phi$ kadar yer kaplayan bir düşük-basınç cebidir (zıtlık kuralı, 2.4.2) — ortalama basınç $\bar P_m=P_0(1-\phi)$; **(G3)** deplase edilen pay, molekülün sürüklenme zarfı olarak onunla akar (Postülat 7'nin molekül ölçeği). Kavrama Yasası ortalanmış alanlarla uygulandığında:

$$\left(\frac{c}{n}\right)^2=\frac{\bar P_m}{\bar\rho_m}=c^2(1-\phi) \;\Longrightarrow\; \boxed{\frac{1}{n^2}=1-\phi}$$

Işık madde içinde **düşük Evrenakı basıncı** nedeniyle yavaşlar; hacimce ortalama yoğunluk sabittir. Bu, kütle-itim mekanizmasıyla (M-2) aynı dildir — ikisi de bir düşük-Evrenakı-basıncı olgusudur.

| Sınav | Teorinin sözü | Gözlem | Sonuç |
|---|---|---|---|
| G-1 yapı | $n$ her saydam ortam için tek fiziksel büyüklüğe ($\phi$: molekül başına etkin deplasman kesri) iner | $n$ ölçüm tablosu | ✅ yapı; $\phi$ **fit parametresi değil** — aşağıdaki yan kontrolle bağımsızca sınanır |
| G-1 yan kontrol | su $n=1{,}333$ ters okunursa $\phi=0{,}437$ | sıvı suyun moleküler hacim-doldurma kesri için bağımsız kestirimler ~0,36–0,40 | ✅ aynı bant (M-15) |
| G-2 Foucault | Zerre **tanecik olduğu hâlde** suda yavaşlar: hız yasası kuvvet-çekim değil, kavramadır — $P/\rho$ düşer, hız düşer | $c_{su}<c_{hava}$ | ✅ |
| G-7 çıkış | hız bir hafıza ya da itki değil, **yerel ortam özelliğidir**; boşluğa çıkan Zerre'nin patinajı biter, doğrusal↔rotasyonel dönüşüm tersinirdir (2.6.1) | gecikmesiz toparlanma | ✅ |

G-2'nin tarihî yükü özellikle kaydedilmelidir. Foucault'nun 1850 ölçümü, ders kitaplarında "tanecik kuramlarının mezarı" diye anılır; oysa öldürdüğü şey taneciğin kendisi değil, Newton'un **hız yasasıdır** — tanecik yoğun ortama *çekilerek hızlanıyordu*. Evrenakı Teorisi tanecikli bir ışık kuramıdır ve yavaşlamayı öngörür, çünkü Zerre'nin hızını ortamla kurduğu **kavrama** belirler, ortamın ona uyguladığı çekim değil. G-7 de aynı yasanın öbür yüzüdür: standart fizikte "foton neden çıkışta anında $c$'ye döner?" sorusu sorulamaz bile — hız tanım gereği sabittir; teoride ise soru gerçektir ve cevabı vardır: hız her noktada yerel $\sqrt{P/\rho}$'dur, taşınan değil **okunan** bir büyüklüktür.

## 9.1.3 Fizeau Ayağı: $f=\phi=1-\dfrac{1}{n^2}$

Akan ortam için yeni hiçbir kavram icat edilmez; M-16'nın muhasebesi M-15'in aynı iki bileşeninden yürür. Ortam bir süperpozisyondur: **arka plan Evrenakı'sı** evrenseldir, moleküller onu akıtamaz — hacim kesri $(1-\phi)$, hızı 0; **molekül deplasman payı** G3 gereği moleküllerle birlikte akar — hacim kesri $\phi$, hızı $u$. Zerre'nin gördüğü etkin ortam hızı hacim-kesri ağırlıklı ortalamadır:

$$u_{ort}=\phi\,u \;\Longrightarrow\; v_{lab}=\frac{c}{n}+\phi\,u \;\Longrightarrow\; \boxed{f=\phi=1-\frac{1}{n^2}}$$

| Sınav | Teorinin sözü | Gözlem | Sonuç |
|---|---|---|---|
| G-4 su | $f=1-1/1{,}333^2=0{,}437$ | $0{,}434\pm0{,}020$ (Michelson & Morley, 1886) | ✅ sapma %1'in altında |
| G-3 kabası | aynı değer | $\approx0{,}48$ (Fizeau, 1851; düşük hassasiyet) | ✅ |
| CS₂ | $f=1-1/1{,}63^2=0{,}624$ | Zeeman dizisiyle uyumlu | ✅ |
| G-3 hava kolu | gaz limiti: $f\to2(n-1)\approx6\times10^{-4}$ | Fizeau'nun hava kolunda sürükleme ölçülemedi | ✅ |
| G-5 uzunluk | katsayı yalnız $n$'ye bağlı; boru boyu ve akış geometrisi ayrıntısı girmiyor | Zeeman'ın uzunluk-bağımsızlık gözlemi | ✅ |

İki yapısal vuruş kaydedilmelidir:

**(a) Kısmilik ayarlanmış değil, zorunludur.** Gaz limiti iç tutarlılık sınavıdır: $\phi\to0$ iken ortam saf arka plana döner ve sürükleme kendiliğinden sıfırlanır. $f$'nin 0 ile 1 arasında kalması bir yumuşatma katsayısı değil, iki-bileşenli muhasebenin cebridir.

**(b) Sürükleme kütleyle değil hacimle ölçeklenir.** Suyun kütle yoğunluğunun ortam referans yoğunluğuna oranı ~$10^{-15}$ mertebesindedir (M-16); sürükleme kütleyle ölçeklenseydi akan su ışığı **hiç** sürüklemezdi. Ölçülen $0{,}434$, deplasman kafesinin bare çekirdek değil **atomun tamamı** olduğunun — elektron kabuğunun kütlece boş ama Evrenakı açısından dolu olduğunun — doğrudan gözlemsel kanıtıdır.

## 9.1.4 Dispersiyon İnce Yapısı: Zeeman'ın Terimi

M-17, renk düzeltmesini aynı Zerre-akışı resminden çıkarır: renk, katar içindeki ardışık Zerre **ritmidir** (2.3); ortam $u$ ile akarken moleküller bu ritmi kendi çerçevelerinde Doppler-kaymış görür ($\omega'=\omega(1-nu/c)$) ve indis kaymış ritimde değerlenir. Birinci mertebede:

$$v_{lab}=\frac{c}{n}+u\left[\,1-\frac{1}{n^2}+\frac{\omega}{n}\frac{dn}{d\omega}\,\right]$$

Köşeli parantezin son terimi, Lorentz'in dispersiyon-düzeltmeli katsayısının birebir aynısıdır ve **Zeeman'ın 1914–15'te ölçtüğü tam katsayıdır**; normal dispersiyonda $dn/d\omega>0$ olduğundan katkı pozitiftir — gözlenen işaretle uyumlu. ✅ Dürüst kayıt: $n(\omega)$ bağımlılığının kendisi bu türetimin girdisi değil, ölçümden alınan verisidir (standart fizikte de Lorentz katsayısı aynı yapıyla çalışır); dispersiyonun mikroskobik kökeni açık kalemdir (9.1.7/iii).

## 9.1.5 Tarihsel Sınamalarla Yüzleşme: Fresnel, Esir Paradoksu, Görelilik

**(a) Fresnel'in ad hoc katsayısı mekanik kimlik kazanır.** $f=1-1/n^2$ formülünü ilk yazan Fresnel'dir (1818): esirin madde içinde "yoğunlaştığını" ve yalnız fazlasının sürüklendiğini varsaydı. Katsayı doğruydu, gerekçesi savunulamazdı — esir hem katıdan geçecek kadar seyrek hem ışığı taşıyacak kadar katı olamıyordu. Teoride aynı ifade türetilir ve sürüklenen şeyin kimliği bellidir: esirin "fazlası" değil, moleküllerin deplase ettiği ve zarf olarak yanlarında taşıdıkları **hacim kesri**. $\phi$'nin bağımsız sınanabilirliği (paketlenme bandı, 9.1.2) bu kimliğin fit değil fizik olduğunun göstergesidir.

**(b) Fizeau–M&M paradoksu tek muhasebede çözülür.** Envanterin tuzağı (G-3 ↔ G-6), teoride tek soruya iner — kitabın kalıcı yöntem kaydıyla: *"yoldaki ortamın hangi kesri neyle hareket ediyor?"* Laboratuvar borusunda akan şey yalnız moleküllerdir; arka plan kesri $(1-\phi)$ durur, deplasman kesri $\phi$ akar → **kısmi** sürükleme. Dünya'nın uzaydaki hareketinde ise laboratuvardaki yerel ortamın kendisi, gezegenin gradyan hâkimiyet bölgesi içinde kütleyle birlikte taşınır; iki kesir de deney düzeneğine göre durgundur → yönsel anizotropi **sıfır**. Aynı Postülat 7, iki ölçekte iki zıt görünüm verir ve ikisi de ölçülmüştür. Üstüne M-18'in yapısal sonucu gelir: eşit kollu bir interferometre, teorinin öngördüğü skaler $c$-değişimine zaten **yapısal olarak kördür** ($L_1=L_2\Rightarrow\delta(\Delta\varphi)=0$) — M&M'in sıfırı teoriyle çelişmek şöyle dursun, teorinin beklediği sonuçtur; skaler kanalı açan asimetrik-kol tasarımı Kısım 5'in konusudur.

**(c) Özel Görelilik ile dejenerasyonun dürüst kaydı.** Standart fizik Fizeau katsayısını hız-toplama formülünün birinci-mertebe açılımından alır (von Laue, 1907): $v_{lab}=(c/n+u)/(1+u/nc)\approx c/n+u(1-1/n^2)$; dispersiyon terimi de aynı çatıdan çıkar. Yani bu arena, birinci mertebede ($u\ll c$) iki kuramı **sayıyla ayırt edemez** — bu bölüm bir ayırt edici sınav değil, iç tutarlılık ve kimlik doğrulamasıdır. Teorinin fazlası üç kalemdir: **(i)** katsayının mekanik kimliği — SR'de $1-1/n^2$ kinematik bir açılım katsayısıdır, teoride bağımsızca ölçülebilir bir hacim kesridir; **(ii)** kapsamın birliği — SR sürüklemeyi kinematikten alırken $n$'nin kendisini ve yavaşlama mekanizmasını ayrı bir ortam kuramına havale eder; teoride $n$, $f$ ve dispersiyon tek büyüklüğün üç yüzüdür; **(iii)** çapraz-ölçek bağı — aşağıdadır.

## 9.1.6 Kenetlenme: Tek Hacim Kesri, İki Ölçüm Ailesi

Bölümün bilançosu tek cümlede toplanır: **durgun suda ölçülen kırılma indisi $\phi=0{,}437$'yi sabitler; akan su deneyi, aynı kesri bağımsız bir düzenekte $0{,}434\pm0{,}020$ olarak geri okur.** Statik bir ölçüm (indis) dinamik bir öngörüye (sürükleme) sıfır yeni parametreyle dönüşür; aynı $\phi$ üçüncü bir gözlenebiliri (dispersiyon teriminin varlığı ve işareti) ve dördüncüsünü (gaz limitinde sürüklemenin ölçülmesi) taşır.

Kenetlenme optikle de bitmez. M-16'nın sonucu genel bir ifadedir: **maddenin sürüklediği ortam kesri $\phi$'dir** — aynı kesir, kavrama kesri olarak M-39/M-40'ın gök-mekaniği kanalına girer ve gezegen ölçeğindeki deplasman genliğini yönetir. Laboratuvarda akan sudaki ışık sürüklenmesi ile gezegen figürü/halka sınavları (Kısım 11), teoride **tek büyüklüğün iki ölçekteki tezahürüdür** — 3.4.6.4'ün "tek mekanizma, iki ölçek" iddiasının bağımsızca sınanabilir ayağı. 9.1.5/c'nin dejenerasyon kaydıyla birlikte okunduğunda teorinin bu arenadaki konumu şudur: birinci-mertebe optikte Lorentz–SR fenomenolojisini birebir üretir; ayırt edici içerik, $\phi$'nin optik dışına taşan kimliğindedir.

## 9.1.7 Açık Kalemler

Mekanizma kuruludur; aşağıdakiler mekanizma boşluğu değil, **hesap kalemleridir** (tümü 7.4 envanterine bağlanır):

i. **$\phi$'nin ilk-ilkeler hesabı:** molekül başına etkin deplasman hacminin, molekülün girdap yapısından türetimi (7.4 md.7). Su için ters-okunan $0{,}437$'nin paketlenme bandının (~0,36–0,40) hafifçe üstünde olması, etkin deplasmanın geometrik hacmi bir miktar aştığını söyler; bu payın mekanik hesabı bu kaleme aittir.
ii. **Yüksek indisli yalıtkanlar:** elmas $n=2{,}42$ ters okunursa $\phi=0{,}83$ — özdeş-küre paketlenme sınırının ($0{,}7405$) üstü. Tikel kafeslerde bu, ancak (i)'deki "etkin hacim > geometrik hacim" payıyla taşınabilir; rejimin sınırı ve kovalent ağ yapılarının okunması açıktır (M-15 geçerlilik sınırıyla birlikte).
iii. **Dispersiyonun mikroskobik kökeni:** $n(\omega)$ bağımlılığının, Zerre atış ritmi ile molekül girdaplarının rezonans tepkisi arasındaki bağdan türetimi (M-17 açık ucu; 7.4 md.7).
iv. **Taşıma katsayısı:** G3, deplase edilen payın *tamamının* molekülle aktığını (katsayı 1) varsayar; klasik hidrodinamiğin eklenmiş-kütle katsayısı ½'dir. Postülat 7'nin entrainment tanımıyla tutarlı olan 1 değerinin bağımsız hidrodinamik hesabı açıktır (M-16 açık ucu).
v. **Opak/metalik fazlar:** $n$'nin karmaşıklaştığı (soğurmalı) rejimde $\phi$ okuması ayrı argüman ister; delokalize elektron gazında $\phi\to1$ davranışı 11.4.1-(4)–(5)'te kurulmuştur, optik soğurma katsayısına bağlanması açıktır.

---

**Bölüm özeti:** Kırılma ve sürüklenme ailesi, esir kuramlarını öldüren ve Özel Görelilik'in ilk zaferi sayılan tarihî arenadır; bu bölümde aynı arena yalnız Kavrama Yasası ve moleküler deplasman kesri kullanılarak sayısal doğrulamadan geçirilmiştir. Kırılma indisi $1/n^2=1-\phi$ ile ortamın fiziksel bir özelliğine iner ve suyun $\phi$'si bağımsız paketlenme kestirimiyle aynı banda düşer; Fizeau katsayısı $f=\phi=1-1/n^2$ statik indisten sıfır parametreyle çıkar ve ölçümle %1 içinde örtüşür; Zeeman'ın dispersiyon terimi işaretiyle birlikte aynı resimden gelir; Fizeau'nun kısmi sürüklemesi ile M&M'in sıfırı, tek muhasebenin ("hangi kesir neyle akıyor?") iki ölçekteki zorunlu görünümü olarak uzlaşır. Işık suda yavaşlar çünkü tanecikli olmak yavaşlamaya engel değildir — hızı çekim değil kavrama belirler; ve çıkışta gecikmesiz toparlanır çünkü hız taşınan değil, yerel ortamdan okunan bir büyüklüktür. Birinci mertebede arena SR ile dejeneredir; teorinin ayırt edici içeriği, $\phi$'nin optiğin dışına — gezegen mekaniğinin kavrama kesrine — uzanan kimliğindedir (Kısım 11).
