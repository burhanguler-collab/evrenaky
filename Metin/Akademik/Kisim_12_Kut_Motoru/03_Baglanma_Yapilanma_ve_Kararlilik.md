# 12.3 Kutların Bağlanması, Yapılanması ve Kararlılığı

Kut vardır (12.1) ve 4B dönüşün izini taşır (12.2). Şimdi asıl soru: **Kutlar nasıl bir araya gelir?**

Bu bölüm yapının **nasıl kurulduğunu** anlatır. Kurulan yapının Kut'un dönüşünü nasıl **devraldığı** ise bir sonraki bölümün konusudur (12.4) — ve kitabın omurgası orasıdır.

Bu bölüm, Evrenakı Teorisi'nin atom altı yapıya bakan yüzüdür. Ama dikkat: burada atomların nasıl işlediği anlatılmıyor. Burada anlatılan, **daha alttaki katmanın kuralları** — Kutların hangi mesafede durduğu, hangi topluluklara oturduğu, hangi birlikteliklerin ayakta kaldığı. Ayakta kalan o birlikteliğin adı **Kutam**'dır (1.6 sözlüğü: "bir tutam Kut" — Kutlar bağ kurar, kimliklerini korur, tek ve daha büyük bir Kut'a dönüşmez); bu bölümde kurulan her kararlı birleşik bu adla anılır. Atomlara giden yol buradan geçer, ama yolun kendisi bu kitabın konusu değildir (12.6).

---

## 12.3.1 Başlangıç: Girdap Dinamiği Bağ Üretmez

İlk ve en önemli olumsuz sonuçla başlamak gerekir, çünkü bu kısımdaki her şey onun üzerine kuruludur.

İki eş yönlü Kut'un karşılıklı taşıma hızının **radyal bileşeni tam sıfırdır.** Birbirlerine ne yaklaşır ne uzaklaşırlar; ortak merkez etrafında yörüngeye girer, ayrımı korurlar.

$$v_{\text{radyal}} = 0 \qquad \text{(nokta girdap dinamiği, tam)}$$

Enerji de aynı şeyi söyler. Eş işaretli çiftte etkileşim enerjisi

$$E_{\text{int}} = -\frac{\Gamma_1\Gamma_2}{2\pi}\ln\frac{d}{d_{\text{ref}}}$$

($d_{\text{ref}}$: 2B nokta girdap sözleşmesinin standart referans uzunluğu; türevlere girmez.) Ve bu enerji, $d$ büyüdükçe **düşer** — yani ayrılmak bedavadır, hatta enerjice tercih edilir.

**Basınç haritası da doğrular:** eş yönlü çiftin tam ortasında hızlar birbirini götürür, $\rho = \rho_0$ (sırt, yüksek basınç); dışta hızlar toplanır, $\rho = 0{,}454$ (çukur). Boşluk düşük basınca gider ⟹ her Kut dışa bakar.

> **Sonuç:** Kutları bir arada tutan şey çıplak girdap dinamiği **değildir**.
> Bölümün geri kalanı, teorinin pulsasyon ve dalga sektörlerinden gelen kanalları
> kurar; hesaplanmış özel sınırlarla açık tam-kernel hesabını ayrı statüde tutar.

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

### κ türetilir: pulsasyon zincirinden kapalı biçim

Buraya kadar $\kappa$, simülasyonun kalibre edilmiş bir katsayısıydı; şimdi kapalı biçimi türetilebilir. 12.2.3'teki $w\to V\to\dot V$ zinciri, her Kut'un hacmini $\Omega=2\omega_2$ frekansında ve $\Delta V=\pi\varepsilon A_w^2$ genliğinde (küçük salınım sınırı) soluyan bir kaynak yapar. Eş fazda salınan iki özdeş Kut için Bjerknes kanalının zaman ortalaması, pulsasyonun ilk Fourier bileşeninden $\langle\dot V_1\dot V_2\rangle = \tfrac12\Omega^2\Delta V^2 = 2\omega_2^2\Delta V^2$ değerini alır; bunu Bjerknes ifadesine (bölüm başındaki işaret kuralıyla; $\kappa$ çekimin büyüklüğünü toplar) yerleştirmek $\kappa$'yı doğrudan verir:

$$\boxed{\;\kappa_{\mathrm{SI}} = \frac{\rho_0\,\omega_2^2\,\Delta V^2}{2\pi} = \frac{\pi}{2}\,\rho_0\,\omega_2^2\,\varepsilon^2\,A_w^4\;}$$

Bu biçimin iki yapısal özelliği vurgulanmalıdır. **Birincisi**, kuvvete giren büyüklük Kut'un toplam hacmi değil, hacminin **salınım genliğidir**: sabit duran hacim Bjerknes kanalında görünmez, kanal yalnız soluk alan payı görür. (Toplam hacmi genlik yerine koyan bir yazım, küçük salınımda hatayı genliğin dördüncü kuvvetiyle büyütür — $A_w/\varepsilon=0{,}1$'de yaklaşık dört bin kat aşırı tahmin.) **İkincisi**, hacim dördüncü eksen sapmasının karesine bağlı olduğundan pulsasyon frekansı ikinci açısal hızın iki katıdır ve $\kappa$'ya $\Omega^2=4\omega_2^2$ olarak girer. Genliğin dördüncü kuvvetiyle ölçeklenme ($A_w^4$), bağ kanalını dördüncü eksen salınımının şiddetine olağanüstü duyarlı kılar: genliği iki katına çıkarmak bağlanma katsayısını on altı katına çıkarır. Yüksek harmonikler eş fazlı çiftte kareler toplamı olarak katıldığından katkıları kesinlikle pozitiftir: **tam sinyalin ilk-harmonik ifadesi, tam değere göre bir alt sınırdır.** Kapalı küçük-genlik biçimi ise yalnız $A_w\ll\varepsilon$'da geçerlidir; tam-kapanma sınırında ($A_w\to\varepsilon$) genlik katsayıları tam eliptik integrallerle hesaplanmalıdır ve küçük-genlik uzantısı ilk harmoniği aşırı tahmin edebilir.

Bu türetim $\kappa_{\mathrm{SI}}$'yı bağımsız bir ayar sabiti olmaktan çıkarır; fakat tek başına denge uzaklığını kapatmaz. Çünkü Bjerknes kuvvetinin radyal bileşeni Magnus yasasıyla yörünge hızını yeniden ayarlar, teğetsel bileşeni ise ayrımı değiştirir. Dolayısıyla $d_e=\sqrt2r_e$ konduğunda kesinleşen büyüklük gerçek yörünge Mach sayısı değil, yalnız çıplak dolanım Mach sayısıdır:

$$\boxed{\;M_K\equiv\frac{K_{\mathrm{SI}}}{c_0d_e}=1\;}$$

Gerçek $M_{\mathrm{orb}}=v_\theta/c_0$, 12.3.4'teki iki bağlı denklemden $d_e$ ile birlikte çözülür. Böylece $d_e$ aynı hesapta hem girdi hem öngörü yapılmaz. $\varepsilon$, $A_w$ ve $\omega_2$ taban büyüklüklere bağlandığında doğrudan bu parametresiz bağlı sisteme girer; yeni bir kalibrasyon katsayısı eklenmez.

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

> **Geçerlilik notu — iki katman.** $M^7$ biçimi, düşük-Mach eşleştirmesine ek olarak çıplak nokta-girdap yörüngesi $\Omega=2K_{\mathrm{SI}}/d^2$ ikamesini kullanır. Tam sistemde Bjerknes kuvvetinin radyal bileşeni $\Omega$'yı yeniden ayarladığından temel değişken gerçek $\Omega_{\mathrm{orb}}$'dur; $M^7/d^5$ yasası ancak bu geri tepme ihmal edildiğinde geri kazanılan indirgenmiş sınırdır.

**Düşük-Mach önkatsayısı hesaplandı: $C_L^{(0)} = 8\pi^2$.** Eşleştirilmiş asimptotik açılım baş katsayıyı kapatır. İç (sıkıştırılamaz) çözümün kuadrupol terimi, dış bölgede $e^{2i\theta}$ açısal yapılı dışarı-giden dalgaya — $H_2^{(2)}(kr)$ Hankel çözümüne — eşlenir ($\omega = 2\Omega$, $k=\omega/c_0$); küçük-argüman eşleşmesi dalga genliğini $A=\Gamma a^2k^2/8$ olarak sabitler ve baş-mertebe güç integralini verir:

$$\boxed{\;P(d,\Omega_{\mathrm{orb}})=\frac{\rho_0\Gamma^2a^4\Omega_{\mathrm{orb}}^5}{c_0^4}\,F_L(M_{\mathrm{orb}},\ldots),\qquad a=\frac d2,\quad F_L(0,\ldots)=1\;}$$

Buradaki $F_L$, sonlu-Mach ve sonlu-çekirdek düzeltmesini taşıyan **türetilmiş yanıt fonksiyonudur; yeni bir sabit değildir.** Düşük-Mach baş eşleşmesi $C^{(0)}=1$'i verir. Yalnız radyal Bjerknes geri tepmesi ihmal edilip $\Omega_{\mathrm{orb}}=2K_{\mathrm{SI}}/d^2$ konursa

$$P_{\mathrm{LO}}\longrightarrow 8\pi^2\rho_0c_0^3dM_K^7,\qquad C_L^{(0)}=8\pi^2$$

sonucu geri gelir. Simülasyonun $\lambda=1$ seçimi bu indirgenmiş dalın normalizasyonudur; temel denklemin bağımsız fiziksel katsayısı değildir.

**Akustik tork, verilen gücü ek bir mobilite parametresi olmadan radyal hıza
çevirir.** Eş yönlü çift için toplam tork $-P/\Omega_{\mathrm{orb}}$, Kut başına
teğetsel fren $-P/(\Omega_{\mathrm{orb}}d)$ ve Magnus yasası

$$\boxed{\;\dot d_L=\frac{2P}{\rho_0\Gamma\Omega_{\mathrm{orb}}d}
=\frac{\Gamma d^3\Omega_{\mathrm{orb}}^4}{8c_0^4}\,
F_L(M_{\mathrm{orb}},\ldots)>0\;}$$

verir: yörünge enerjisi ve açısal impuls kaybı eş yönlü çifti dışarı sürer. Çıplak
nokta-girdap sınırında $\Omega_{\mathrm{orb}}=2K_{\mathrm{SI}}/d^2$ konduğunda
$\dot d_L=4\pi F_LK_{\mathrm{SI}}^5/(c_0^4d^5)$ geri gelir. İndirgenmiş işaret
yapısının enerji okuması şöyledir:

| | $E_{\text{girdap}}$ | yaklaşınca | enerji düşerse |
|---|---|---|---|
| Eş yönlü | $-(\Gamma^2/2\pi)\ln d$ | artar | **uzaklaşırlar** |
| Zıt yönlü | $+(\Gamma^2/2\pi)\ln d$ | azalır | **yaklaşırlar → yok olurlar** |

**Ve ışıma zayıf bir tashih değildir.** Bu kanalda geçen büyüklük cep-duvarı hızı değil,
çiftin gerçek yörünge Mach sayısıdır:

$$M_{\text{orb}}\equiv\frac{\Omega_{\text{orb}}d}{2c_0}.$$

Çıplak nokta-girdap taşımasının Mach sayısı ise
$M_K\equiv K_{\text{SI}}/(c_0d)$'dir. Ölçülen $d_e=\sqrt2r_e$ yerinde
$M_K=1$ tamdır; fakat Bjerknes kuvvetinin radyal bileşeni dönme hızını da değiştirdiği
için $M_{\text{orb}}$ ayrıca çözülmelidir. Dolayısıyla işletme noktası düşük-Mach
varsayımıyla güvence altında değildir; ışımayı sıfırlamak değil, tam sonlu-yayılım
çekirdeğiyle birlikte hesaplamak gerekir.

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
> kuadrupol momenti $2\Omega_{\text{orb}}$ frekansıyla salınır (12.3.3'ün başı).
> Dolayısıyla ışımayı yöneten ölçek **çiftin ayrımı $d$** ve gerçek
> $M_{\text{orb}}$'dur; Kut'un iç yarıçapı değildir.
>
> **Tezat yok, ama ayrım kritiktir:** cep duvarının $6\times10^{4}\,c_0$'ı çiftin
> kuadrupol ışıma Mach sayısı değildir; denkleme $M_{\text{orb}}$ girer. Bu iki hızı
> özdeşleştirmek, simetriyle elenen bir iç hızı yanlış kanala taşımaktır.

---

## 12.3.4 İndirgenmiş Yasa ve İşaret Yapısı

İlk koşumlarda kullanılan skaler denklem, radyal yaklaşma hızının iki kolunu model
birimlerinde şu biçimde temsil eder:

$$\boxed{\;U_{\text{red}}(d)=-\frac{\kappa\cos(\text{faz})}{d^2}
+\lambda\,g_i g_j\,\frac{K^5}{d^5}\;}$$

| | eş yönlü ($g_ig_j>0$) | zıt yönlü ($g_ig_j<0$) |
|---|---|---|
| Bjerknes kolu $-\kappa/d^2$ | çeker | çeker |
| Işıma kolu $+\lambda g_ig_j K^5/d^5$ | **iter** | **çeker** |
| **Sonuç** | **kararlı denge** | **DENGE YOK** |

$$\boxed{\;d_{\text{denge}} = \left(\frac{\lambda K^5}{\kappa}\right)^{1/3}\;}$$

**Zıt yönlü çift için kök yoktur** — iki hız kolu da içeri yönelir. 210 farklı
$(\kappa,\lambda,d)$ üçlüsünde dışa yönlü toplam sürüklenme veren **hiçbir** durum
bulunmadı.

> **Ters Kut'un bir yapıda duramaması, bir katsayı sonucu değil, işaret yapısının sonucudur.** Hiçbir parametre seçimi bunu değiştiremez.

Bu kök, **indirgenmiş modelin çıktısıdır**; temel teorinin bağımsız SI öngörüsü değildir.
Ölçülen $d_e=\sqrt2r_e$, indirgenmiş katsayıların kalibrasyon hedefidir. Temel düzeyde
$d_e$ ve $\Omega_e$ aşağıdaki iki bağlı denklemden, başka bir katsayı eklenmeden
birlikte çıkmalıdır.

Kuvvet yasasının iki teriminin dışında bir terime gerek olmadığı da vurgulanmalıdır: kısa erimli ayrı bir itme kanalı fiziksel olarak temelsizdir. Boşluk düşük basınca — yani girdaba **doğru** — çekilir; "cepler iç içe geçemez" gerekçeli bir itme ise ölçek olarak tutarsız olurdu, çünkü cepler ($2{,}29\times10^{-5}\,r_e$) küme aralığından ($\approx 1{,}4\,r_e$) yaklaşık **62 000 kat** küçüktür. Dengeyi kuran itme, türetilmiş ışıma kanalıdır.

### Hareket Denklemi: Boyut Kapanışı

Kut çiftinin radyal dinamiğini besleyen iki kanal farklı nicelikler üretir: Bjerknes
kanalı kuvvet, ışıma kanalı güç verir. Boyut köprüsü yeni bir hareketlilik sabitiyle
değil, teoride zaten bulunan **Magnus yasası** ve akustik tork muhasebesiyle kurulur.
Bir Kut üzerindeki birim uzunluk başına dış kuvvet $\tilde{\mathbf f}$ için

$$\tilde{\mathbf f}+\rho_0\Gamma\,\hat z\times(\mathbf v-\mathbf u)=0
\quad\Longrightarrow\quad
\mathbf v-\mathbf u=\frac{\hat z\times\tilde{\mathbf f}}{\rho_0\Gamma}.$$

Dolayısıyla $\tilde{\mathbf f}=\tilde f_r\hat r+\tilde f_\theta\hat\theta$ ise

$$v_\theta=\frac{K_{\mathrm{SI}}}{d}+\frac{\tilde f_r}{\rho_0\Gamma},
\qquad \dot r=-\frac{\tilde f_\theta}{\rho_0\Gamma},\qquad d=2r.$$

Bu eşitlik merkezcil kuvvet kilidini de gösterir: radyal Bjerknes bileşeni doğrudan
$d$'yi değil $\Omega_{\text{orb}}$'u değiştirir; ayrımı değiştiren onun gecikmeden
doğan teğetsel bileşenidir.

### Tek sonlu-yayılım çekirdeği

Radyal ve teğetsel bileşenler iki bağımsız yama değildir. İkisi aynı gecikmeli dalga
alanının izdüşümleridir. Hareketli bir hacim kaynağı için mevcut $c_0$ dalga sektörünün
gecikmeli potansiyeli şematik olarak

$$\phi_i(\mathbf x,t)=-\left.
\frac{\dot V_i(t_r)}{4\pi R_i\,[1-\mathbf n_i\!\cdot\!\boldsymbol\beta_i]}
\right|_{t_r},\qquad t-t_r=\frac{R_i(t_r)}{c_0},\qquad
p_i=-\rho_0\partial_t\phi_i$$

ve diğer Kut üzerindeki ortalama kuvvet

$$\mathbf F_{j\leftarrow i}=-\big\langle\delta V_j\,\boldsymbol\nabla p_i\big\rangle$$

ile belirlenir. Bu yüzden eş çift için sonuç yeni katsayılar koymadan

$$\boxed{\;\tilde{\mathbf f}_B=
\frac{\kappa_{\mathrm{SI}}}{L_{\mathrm{eff}}d^2}
\left[\mathcal R(M_{\text{orb}},q,\ldots)\hat r+
\mathcal T(M_{\text{orb}},q,\ldots)\hat\theta\right]\;}$$

biçiminde yazılır. $\mathcal R$ ve $\mathcal T$ **serbest fonksiyon ya da yeni sabit
değildir**; yukarıdaki Green çekirdeğinin, 12.1–12.2'de belirlenmiş Kut kaynağıyla
hesaplanacak iki izdüşümüdür. İşaret düzenimizde eş-fazlı durağan sınır
$\mathcal R\to-1$'dir; $\mathcal T$ sonlu yayılım nedeniyle doğar ve prograd ise
içe Magnus sürüklenmesi üretir.

Tam dairesel gecikme geometrisi de ek varsayım gerektirmez. Karşılıklı iki yörüngede

$$c_0\tau=d\cos y,\qquad y\equiv\frac{\Omega_{\text{orb}}\tau}{2},
\qquad \boxed{\;y=M_{\text{orb}}\cos y\;},\qquad
q\equiv\Omega_p\tau,\quad\Omega_p=2\omega_2.$$

Böylece daha önce ayrı ayrı istenen $M\ll1$,
$\Omega_p\gg\Omega_{\text{orb}}$ ve $k_pd\ll1$ koşulları temel kapanışın şartları
olmaktan çıkar; bunlar yalnız belirli asimptotik açılımların geçerlilik koşullarıdır.
İşletme noktası tam gecikmeli çekirdekte hesaplanır.

Işıma gücü de aynı gerçek yörünge frekansıyla yazılmalıdır:

$$P=\frac{\rho_0\Gamma^2(d/2)^4\Omega_{\text{orb}}^5}{c_0^4}
F_L(M_{\text{orb}},\ldots).$$

$F_L$ de aynı eylem/dalga sektöründen türeyen boyutsuz yanıt olup serbest katsayı
değildir. Toplam akustik tork $-P/\Omega_{\text{orb}}$ olduğundan, Kut başına fren
$\tilde f_{L,\theta}=-P/(\Omega_{\text{orb}}d)$ ve Magnus yasasından

$$\dot d_L=\frac{2P}{\rho_0\Gamma\Omega_{\text{orb}}d}
=\frac{\Gamma d^3\Omega_{\text{orb}}^4}{8c_0^4}F_L$$

çıkar. Bjerknes geri-tepkisi ihmal edilip
$\Omega_{\text{orb}}=2K_{\mathrm{SI}}/d^2$ konduğunda bu ifade tam olarak
$4\pi F_LK_{\mathrm{SI}}^5/(c_0^4d^5)$ düşük-Mach koluna döner; eski
$C_L^{(0)}=8\pi^2$ yazımı bu özel sınırın eşdeğer gösterimidir.

### Temel kapanış: iki bilinmeyen, iki denklem

Eş yönlü çiftin boyutça kapalı dinamiği artık

$$\boxed{\;
\frac{\Omega_{\text{orb}}d}{2}=
\frac{K_{\mathrm{SI}}}{d}+
\frac{\kappa_{\mathrm{SI}}}{\rho_0\Gamma L_{\mathrm{eff}}d^2}\,\mathcal R
\;}$$

$$\boxed{\;
\dot d=-\frac{2\kappa_{\mathrm{SI}}}{\rho_0\Gamma L_{\mathrm{eff}}d^2}\,\mathcal T
+\frac{\Gamma d^3\Omega_{\text{orb}}^4}{8c_0^4}\,F_L
\;}$$

olarak verilir; $\mathcal R$, $\mathcal T$ ve $F_L$ aynı çözümde
$(M_{\text{orb}},q,\ldots)$ üzerinde değerlendirilir. İlk denklem dönme hızını,
ikincisi ayrım akışını verir. Denge $\dot d=0$ ile birlikte çözülür ve kararlılık,
çözüm kolu üzerindeki $U(d)\equiv\dot d$ için

$$\boxed{\;U(d_e)=0,\qquad U'(d_e)<0\;}$$

koşuludur. Burada hiçbir yeni kuvvet, hız, aksiyom veya ayarlanabilir katsayı yoktur.
Açık iş, var olan eylemden üç yanıt fonksiyonunu hesaplamaktır.

Ölçülen $d_e=\sqrt2r_e$ yerine konduğunda yalnız

$$\boxed{\;M_K(d_e)=\frac{K_{\mathrm{SI}}}{c_0d_e}=1\;}$$

çıkar. Bu, çıplak dolaşım ölçeğinin kesin sonucudur; gerçek $M_{\text{orb}}$ ilk bağlı
denklemden bulunur. Dolayısıyla $d_e$ aynı paragrafta hem girdi hem bağımsız öngörü
sayılmaz. Teorinin güçlü sınaması şudur: iç parametrelerden türetilen çekirdek,
ölçülen değeri kullanmadan $d_e/r_e=\sqrt2$ kökünü ve $U'(d_e)<0$ işaretini vermelidir.

Denge noktasının güç okuması değişmez: ikinci dönüşün ($\omega_2$) beslediği
pulsasyon pompasından alınan güç, gecikmeli Bjerknes torku üzerinden yörüngeye ve
oradan akustik yayına akar. Denge, kaynağı ve kaybı duran bir sistem değil, iki akının
eşitlendiği **sürülen açık sistem** durumudur.

**İki gösterimin statüsü ayrıdır.** Küpkök yasası
$d_e=(\lambda K^5/\kappa)^{1/3}$, indirgenmiş simülasyon modelinin köküdür.
Yukarıdaki bağlı Green–Magnus sistemi ise temel kapanıştır. İndirgenmiş katsayılar
denge çevresinde bu sistemden okunabilir; temel sisteme geri taşınacak bağımsız
doğa sabitleri değildir.

**İndirgenmiş ayırt edici koşum yapıldı — iki yüzüyle.** *(i) Denge-dışı eğriler:* aynı dengeye ($d_e=\sqrt2$) kalibre edilmiş iki yasa sayısal olarak koşuldu. Denge yeri ve kararlılık özdeş; yaklaşma eğrileri ayrık — uzak-alan log-log eğimleri $-1{,}98$ ve $-2{,}94$ (kodlanan $-2$ ve $-3$ kollarıyla uyumlu), $d_0=3$'ten dengeye varış süresi aday biçimde yaklaşık iki kat uzun (6,7'ye karşı 12,9 model zamanı). Bu sonuç fiziksel yasayı doğrulamaz; indirgenmiş denklemin uygulama ve ölçek tutarlılığı kontrolünü geçtiğini gösterir. Fiziksel ayrım tam çok-Kut simülasyonunun uzak-yaklaşma protokolünde ve $(\mathcal R,\mathcal T,F_L)$ çekirdeğiyle sınanacaktır. *(ii) Kutam ölçeklemesi:* $d^{-2}$ temsili ölçülen $d\propto N$ değişmezliğini verir. $d^{-3}$ adayı, $\Delta V_{\text{Kutam}}\propto N$ varsayımıyla $d\propto N^{3/2}$ üretir. $d\propto N$'yi korumak için gereken $\Delta V_{\text{Kutam}}\propto N^{3/2}$ koşulunun cebirsel koşumda sonucu geri getirmesi bir fiziksel doğrulama değil, **kilit ve sınanabilir sonuç koşulunun tutarlılık kontrolüdür**. Tam çekirdekte buna $q_N$ sabitliği, dolayısıyla $\Omega_{p,N}\propto N^{-1}$ koşulu da eklenir. Asıl sınav, iki ölçeklemenin tam simülasyonda bağımsız ölçümüdür.

### İndirgenmiş Sözde-Potansiyel ve Yerel Kararlılık

İndirgenmiş skaler akış $U_{\text{red}}=-\kappa/d^2+\lambda K^5/d^5$,
yalnız görselleştirme amacıyla $U_{\text{red}}=-dV_{\text{red}}/dd$ biçiminde
yazılabilir:

$$V_{\text{red}}(d)=-\frac{\kappa}{d}+\frac{\lambda K^5}{4d^4}.$$

Bu temsilde

$$d_e=\left(\frac{\lambda K^5}{\kappa}\right)^{1/3},\qquad
E_{\text{geom}}\equiv-V_{\text{red}}(d_e)=\frac{3\kappa}{4d_e},\qquad
k_{\text{red}}\equiv V_{\text{red}}''(d_e)=\frac{3\kappa}{d_e^3},$$

ve $k_{\text{red}}d_e^2=4E_{\text{geom}}$ olur. Bunlar indirgenmiş
$d^{-2}\leftrightarrow d^{-5}$ eğrisinin geometrik özellikleridir; temel teorinin
korunumlu bağlanma enerjisi veya bağımsız fizik sabitleri değildir.

Donmuş-yanıt yaklaşımında Bjerknes sürüklenmesi $d^{-3}$ alınırsa doğru eşlenik
sözde-potansiyel

$$U_{\text{red}}=-\frac{A}{d^3}+\frac{B}{d^5},\qquad
V_{\text{red}}=-\frac{A}{2d^2}+\frac{B}{4d^4}$$

olur. $B=Ad_e^2$ kökünde

$$\boxed{\;E_{\text{geom}}=\frac{A}{4d_e^2},\qquad
k_{\text{red}}=\frac{2A}{d_e^4},\qquad
k_{\text{red}}d_e^2=8E_{\text{geom}}\;}$$

çıkar. Böylece önceki kuvvet-hız karışımından doğan bir-kuvvet hatası giderilir.

Tam Green–Magnus sisteminde $\mathcal R$, $\mathcal T$, $F_L$ ve
$\Omega_{\text{orb}}$ ayrımla birlikte değiştiği için genel bir skaler potansiyel
varsayılmaz. Yerel kararlılık doğrudan $U'(d_e)<0$ ile, gevşeme ise

$$\delta\dot d=U'(d_e)\delta d,\qquad
\boxed{\;\tau^{-1}=-U'(d_e)>0\;}$$

ile belirlenir. Sistem açık olduğundan
$\tfrac12m\dot d^2+V_{\text{red}}=\text{sabit}$ yazılamaz ve
$E_{\text{geom}}$ kesin ayırma işi ya da kütle açığı diye kullanılamaz. Böyle bir
enerji iddiası ancak tam eylemde kaynak, alan ve ışıma enerji muhasebesi birlikte
çıkarıldıktan sonra kazanılır.

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

## 12.3.6 İndirgenmiş Dinamikte Kümeleşme

Kalibre edilmiş indirgenmiş bağ kanalı devredeyken dağınık bir Kut topluluğunun ne
yaptığı sayısal olarak sınandı: 30 Kut'luk 12 bağımsız rastgele dizilim koşuldu.

| Ölçüt | Sonuç |
|---|---|
| Kümeleşme oluştu | **12/12** |
| Kutam boyutu $\le 8$ | **62/62 — istisnasız** |
| Boy histogramı | 4→7 · 5→21 · **6→22** · 7→11 · 8→1 |
| Ortalama boy | **5,65** |

**Koşum içinde boyut ayrıca ayarlanmadı.** Bulunan 5–8 aralığı, nokta-girdap
sektörünün bağımsız **Thomson kararlılık sınırıyla** karşılaştırıldı: düzgün çokgen
dizilim $N\le7$'ye kadar kararlıdır, merkeze bir Kut konursa sınır yaklaşık 10'a
çıkar. Bu örtüşme indirgenmiş dinamiğin güçlü bir iç tutarlılık bulgusudur; tam
çekirdeğin çok-Kut çözümünün yerine geçmez.

$$\Omega_N = \frac{\Gamma(N-1)}{4\pi R^2}$$

### Kalıcılık nasıl sağlanır: fırlatma

Topluluğun RMS yarıçapı tek başına yanıltıcı bir ölçüdür: bazı denemelerde *büyür* görünür. Çekirdek ayrı ölçüldüğünde tablo netleşir (14 deneme):

| | Tüm topluluk | **Çekirdek** | En uzak Kut |
|---|---|---|---|
| Normal 12 deneme | 0,34–0,48 | 0,34–0,48 | 8–10 |
| Deneme 6 | **3,35×** | **0,41** | **203** |
| Deneme 10 | **11,18×** | **0,36** | **720** |

**14 denemenin 14'ünde çekirdek büzülür.** "Yayılma" görülen durumlarda olan şey, 2–4 Kut'un 200–720 birim uzağa **fırlatılmasıdır**; kalan çekirdek aynı oranda — hatta biraz **daha sıkı** — bağlanır (fırlatanlarda ort. 0,385, fırlatmayanlarda 0,415).

> **İndirgenmiş koşumda** kalıcı çekirdek için ayrıca dış sönüm konmamıştır; sistem
> fazla enerjiyi üye atarak boşaltmıştır. Tam teoride akustik ışıma zaten içsel ortam
> kanalıdır ve enerji defteri onunla birlikte tutulacaktır (12.5).

### İndirgenmiş çok-komşu sıkışması: iki-cisim aralığından örgü aralığına

İndirgenmiş $d_{\text{denge}}$ bir **iki-cisim** büyüklüğüdür. Kümede ise her üye,
kodlanan uzak menzilli $1/d^2$ kolu üzerinden bütün komşularını görür; toplam etki en
yakın aralığı iki-cisim değerinin altına indirir. Aynı indirgenmiş yasa yeni terim
eklenmeden çok-cisim statik çözümünde kullanıldı:

| Dizilim | En yakın aralık / $d_{\text{denge}}$ | Sıkışma |
|---|---|---|
| 2-cisim (kontrol) | 1,0000 | %0 |
| 3-üçgen | 1,0000 | %0 — simetri gereği her çift kendi kökünde |
| 6-halka (merkezsiz) | 0,8551 | %14,5 |
| 7-altıgen (merkezli) | 0,9117 | %8,8 — merkez üye halkayı gevşetir |
| 19-örgü (iki kabuk) | **0,7573** | **%24,3** |

### Sayım tanımı: yakalama yarıçapı türetilmişle ölçeklenir

"Kutam" sayımının eşiği (yakalama yarıçapı) artık serbest bir sayı değildir: $1{,}2\,d_{\text{denge}}$ olarak türetilmiş denge aralığına bağlanır ve $\kappa$, $\lambda$ ile birlikte kendiliğinden ölçeklenir. Bu bir fizik değişikliği değil, sayım tanımının kapanmasıdır — ama sonucu ölçülebilirdir: yeniden-ölçüm kampanyasında (12 tohum × 30 Kut; iki tanım aynı tohumlarla, indirgenmiş dinamik) **sabit eşik**, bitişik iki yapıyı tek sayarak Thomson bandını delen 9–11 üyelik sahte Kutamlar üretti (58 Kutam'ın 6'sı band dışı); **ölçeklenen eşik** bandı istisnasız korudu (87/87, en büyük 8) ve ölçek-değişmezliği ölçümü iki tanımda bit-bit aynı çıktı — sayım fiziğe dokunmuyor, yalnız onu doğru okuyor. Boy istatistiklerinin bu bölümdeki mutlak değerleri eski sayımla alınmıştır; yeni sayımla sim-içi yeniden ölçüm açık kalemdedir.

İki kabuklu örgüde sıkışma **%24,3** çıkar ve aynı indirgenmiş dinamikte gözlenen
yaklaşık %25 ile örtüşür. Bu model düzeyinde perdeleme/ekranlama eklemek gerekmez;
tam teoride aynı nicel sonucun $\mathcal R$, $\mathcal T$ ve çoklu gecikmelerle
yeniden üretilmesi ayrı sınamadır. Merkezli dizilimde sıkışmanın azalması, Thomson
merkez-ayrıcalığının statik yüzüdür.

---

## 12.3.7 Bileşik Sınır Tabakası ve Ölçek Değişmezliği

Sıkı bir Kutam uzaktan **tek girdap** gibi görünür ve uzak alanı **iç dizilime kördür** (ölçüldü: düzgün çokgen / doğrusal dizi / yığın / rastgele küme → aynı $|v|$, fark $\sim10^{-6}$). Buradan:

$$|v| = \frac{|\Gamma_{\text{top}}|}{2\pi R} = \sqrt2\,c_0 \quad\Longrightarrow\quad \boxed{\;r_e(\text{Kutam}) = \left|\sum g\right|\cdot r_e\;}$$

$N=10$ ve $N=20$'de bağıl fark $1{,}2\times10^{-16}$. **Sınır tabakası Kut sayısıyla doğrusal büyür.**

Bunun doğrudan bir sonucu daha vardır: $\Gamma_{\text{top}} = 0$ olan Kutam'ın bileşik tabakası **yoktur** — uzaktan **görünmez**.

### Kutamlar arası mesafe: indirgenmiş sonuç ve tam-kernel sınaması

İndirgenmiş yasada çıplak dolanım ölçeklemesi
$M_K=K(|g_i|+|g_j|)/(c_0d)$ kullanıldığında eş Kutamlarda ışıma $\propto N^5$,
Bjerknes katsayısı $\propto N^2$ olur ve:

$$d_{\text{denge}} = \left(\frac{\lambda K^5}{\kappa}\right)^{1/3}\cdot N$$

| $N$ | 1 | 2 | 4 | 7 | 10 | 20 |
|---|---|---|---|---|---|---|
| $d_{\text{denge}}/N$ | 1,414214 | 1,414214 | 1,414214 | 1,414214 | 1,414214 | 1,414214 |
| $d_{\text{denge}}/(r_e^A + r_e^B)$ | **0,7071** | 0,7071 | 0,7071 | 0,7071 | 0,7071 | 0,7071 |

> **Tablodaki oran indirgenmiş modelde her boyutta aynıdır.** Bu, kodlanan ölçek
> değişmezliğinin cebirsel ve sayısal doğrulamasıdır; tam Green–Magnus çekirdeğinin
> sonucu olduğu henüz ilan edilmez.

Tam sistemde $d_N\propto N$ için yalnız kuvvet genliğinin ölçeklenmesi yetmez;
boyutsuz yanıtların da aynı noktada kalması gerekir:

$$M_{\text{orb},N}=\text{sabit},\qquad
q_N=\Omega_{p,N}\tau_N=\text{sabit},\qquad
(\mathcal R_N,\mathcal T_N,F_{L,N})=\text{sabit}.$$

$d_N\propto N$ ve sabit $M_{\text{orb},N}$, $\tau_N\propto N$ verdiğinden gerekli
öz-benzerlik koşulu

$$\boxed{\;\Omega_{p,N}\propto N^{-1}\;}$$

olur. Bu yeni bir postüla değil, ölçülecek ve yanlışlanabilecek bir sonuç koşuludur.
Aynı şekilde donmuş $d^{-3}$ Bjerknes kolunda doğrusal aralığı korumak için daha önce
bulunan $\Delta V_N\propto N^{3/2}$ genlik koşulu da bağımsız olarak sınanmalıdır.

Burada sıfır-fatura hükmü kesindir: Temel Sözleşme tek-Kut $\omega_2$'lerinin ortak
olduğunu söyler; bu yüzden $\Omega_{p,N}\propto N^{-1}$ ayrıca dayatılamaz. Tam
çekirdek $q$'ya duyarsız bir öz-benzer kol üretir veya mevcut çok-Kut dinamiği bu
kolektif frekansı kendiliğinden çıkarırsa doğrusal yasa temel teoriye yükselir.
Bunlardan biri türetilmedikçe tablodaki $d_N\propto N$, yalnız indirgenmiş modelin
ölçülmüş sonucudur. Böylece ölçek değişmezliğini kurtarmak için yeni frekans yasası
ya da genlik postülası eklenmez.

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

### Seçici süpürme: darbeler balanslıyı öteler, fazlalığı ayıklar

Yok-olma darbelerinin yapılar üzerindeki etkisi **seçicidir** ve bu seçicilik elle konmaz, iki olgudan çıkar. **Birincisi**, uzak kaynaklı darbe alanı bir Kutam üzerinde tekdüzedir: fark-terimi $R_{\text{Kutam}}/D$ ile bastırılır (öz-sınamada kilitli) — dolayısıyla **balanslı Kutam'a darbenin yapabileceği tek şey ortak ötelemedir.** İndirgenmiş modelde ölçüldü: balanslı Kutam, 32 katlık genlik aralığında tek üye kaybetmeden ötelendi (ötelenme genlikle orantılı: 0,08'den 12,2'ye), $Q_2$'si bozulmadı. Yapının kararlılığı ekstrem bir olay olmadan bozulamaz — bu bir varsayım değil, alan tekdüzeliğinin sonucudur. **İkincisi**, dolu kabuğa dışarıdan tutunan fazlalık üye **sığ yerel eşiktedir**: aynı fark-tepkisi çekirdek üyeyi yerinden oynatamazken fazlalığı koparabilir. Band altındaki katılım ise süpürme gerektirmez: kararlı 7'liye eklenen yeni üye, indirgenmiş modelde kabul edilip yapı simetrik 8'liye kendiliğinden tavlanır ($Q_2\to0$).

Böylece ters-Kut yok oluşları, ortama yalnız momentum bırakmaz; Kut topluluğu için bir **ayıklama banyosu** kurar: balanslı yapılar darbe yağmuru altında yalnız yer değiştirir, sığ tutunmuş fazlalıklar zamanla koparılır — ayakta kalan nüfus, balanslı ve kararlı dönen yapılardır. Simülasyonda bu mekanizma **sanal patlama** tanı düğmesiyle sınanır: gerçek yok-olma darbesiyle aynı dipol alanı sahne dışından enjekte edilir (yeni fizik girmez); balanssız bir Kutam'ın fazlalığının kopup kopmadığı balans satırından izlenir. Koparma tarafının nicel eşiği açık hesap kalemidir — yerel eşik metriğiyle yazılmalıdır, toplam koparma işi uzun-menzil kuyruğunca domine edildiği için yanıltır.

<p style="margin:20px 0;padding:16px;border:1px solid #22c55e;border-radius:10px;background:rgba(34,197,94,0.07)"><a href="Simulasyon/kisim12/kut_birlesme_yapilanma.html" target="_blank" rel="noopener" style="display:inline-block;padding:12px 22px;background:#166534;color:#ffffff;border-radius:8px;font-weight:700;text-decoration:none;font-size:1.05em">&#9654;&#65039; SİMÜLASYONU AÇ — Kutların birleşmesi ve yapılanması</a><br><span style="color:#a1a1aa;font-size:0.9em;display:inline-block;margin-top:8px">Bu kısmın ana laboratuvarı. Kutlar tek tek yerleştirilir ya da <b>⁂ KALABALIĞI SERP</b> ile onlarca Kut rastgele saçılır — her basışta yeni dizilim, çünkü kanıt gücü kümeleşmenin <b>her</b> dizilime gelmesindedir. <b>Ters Kut</b> eklenebilir ve yok olduğu, momentum darbesini bıraktığı izlenir. Bağ kanalı, ışıma katsayısı, faz farkı ve olay ölçeği canlı ayarlanır; <b>türetilmiş denge mesafesi</b> ve zıt çift için <b>kök olmadığı</b> panelde okunur. Bileşik sınır tabakaları kendi geçerliliklerini ölçüp bildirir; her Kutam'ın altında <b>balans satırı</b> okunur — Γ-ağırlıklı momentler gerçek konumlardan hesaplanır, komşu gelgiti "dış alan" etiketiyle ayrılır ve izole-balanssız Kutamlar ayrıca sayılır. 4B dönüşün 3B izi sağ panelde eşzamanlı çizilir. Fare tekerleğiyle yakınlaştırma, boş alanda sürükleyerek kaydırma, ⌖ ile sığdırma; ayrıca hız ve duraklat denetimleri. <b>229 öz-sınama</b> açılışta koşar. Tek dosya, dış bağımlılık yok.</span></p>

---

## 12.3.9 Sayısal Yöntem Notu

Işıma kanalı $1/d^5$ ile ıraksadığı için denklem **katıdır (stiff)**. Sabit adımlı integrasyon yeterli değildir: sabit $h = 0{,}004$ adımıyla koşulan zıt çift 283 birime savrulur; bağımsız bir sabit adımlı koşumda ise $\kappa=10$'da topluluk yarıçapı **64,9 kat** büyür. İkisi de fiziksel değil, sayısal artefakttır.

Simülasyon bu nedenle **uyarlamalı adım** kullanır: her alt adımda CFL koşulu ($h\,v_{\max} \le 0{,}02\,d_{\min}$) yeniden hesaplanır. Bu bir iyileştirme değil, **zorunluluktur** — ve bu bölümdeki her sayı onunla üretilmiştir.
