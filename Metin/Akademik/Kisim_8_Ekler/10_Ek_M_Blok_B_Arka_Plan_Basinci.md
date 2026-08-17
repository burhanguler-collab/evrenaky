# Ek M — Merkezî Türetim Kataloğu · Blok B: Arka Plan Basıncı ve Ağırlıksızlık

> Şablon ve rozet sistemi için bkz. Blok A (M-1..M-6) girişi.

---

## M-7 · Yırtılmama Koşulu ve $P_0$ Alt Sınırı · **[T]**

**Kullanıldığı bölümler:** Ek B.2, 1.3 Postülat kutuları, M-8 (girdi: $\Delta P$ integral yapısı), 7.4 md.10.

### Varsayımlar
1. Kütle-itim denklemi geçerlidir (M-2): $\vec a = -(1/\rho_n)\nabla P$; kuyu konvansiyonu gereği kütle çevresinde $dP/dr>0$.
2. Evrenakı sürekli bir akışkandır; kararlı var oluşunun asgari koşulu, hiçbir noktada mutlak basıncın (kohezyonsuz hâlde) sıfırın altına inmemesidir.
3. Muhafazakâr hâl: kohezyon dayanımı sıfır sayılır ($\Sigma = 0$; bkz. M-4).

### Adımlar
1. **Yüzey gradyanı (M-2'nin tersinden okunması).** Bu ara adım kaynak metinde örtük bırakılmıştı; burada açıkça yazıyoruz. Kütle-itim denklemi $\vec a = -(1/\rho_n)\nabla P$ yüzeyde ölçülen $g \approx 9{,}8$ m/s² ivmesine uygulanıp gradyan çekilirse:
$$|\nabla P|_{yüzey} = \rho_n\, g \approx (2{,}7\times10^{17}\ \text{kg/m}^3)(9{,}8\ \text{m/s}^2) \approx 2{,}6\times10^{18}\ \text{Pa/m}$$
Boyut kontrolü: $[\text{kg/m}^3][\text{m/s}^2] = \text{Pa/m}$ ✓.
2. **İç bölgede lineer gradyan.** Dünya içinde $r$ yarıçapının kuşattığı nükleon kütlesi $r$ ile azaldığından gradyan merkeze doğru lineer olarak sıfıra iner (homojen küre yaklaşımı):
$$\nabla P(r) = \frac{\alpha M r}{R^3}$$
3. **Merkez–yüzey basınç açığı.** Değişken gradyanın merkezden yüzeye integrali, sabit-gradyan düz hesabına kıyasla yarı değeri verir:
$$\Delta P = \int_0^{R_\oplus} \nabla P(r)\, dr = \tfrac{1}{2}\,|\nabla P|_{yüzey}\cdot R_\oplus \approx \tfrac{1}{2}(2{,}6\times10^{18})(6{,}37\times10^6) \approx 0{,}83\times10^{25}\ \text{Pa}$$
4. **Yırtılmama koşulu.** Merkezde mutlak basınç $P_0 - \Delta P$'dir; kohezyonsuz akışkanın yırtılmaması için $P_0 > \Delta P$ gerekir.
5. **Emniyet payı (kaynakta sessiz kalınan nokta).** Kaynak metnin ilan ettiği taban $P_0 \ge 1{,}6\times10^{25}$ Pa'dır; bu, 3. adımdaki $\Delta P \approx 0{,}83\times10^{25}$ Pa değerine **muhafazakâr yaklaşık iki kat emniyet payı uygulanmış** hâlidir. Pay; homojen-küre idealleştirmesini, çekirdek yoğunluk profili düzeltmelerini ve $g$'nin iç bölgedeki sapmalarını kaba biçimde karşılamak içindir.
6. Yoğunluk tabanı Kavrama Yasası'ndan (M-1, $c_{loc}=\sqrt{P/\rho}$ eşitliğinin arka plan hâli $\rho_0 = P_0/c_0^2$):
$$\rho_0 = \frac{P_0}{c_0^2} \ge \frac{1{,}6\times10^{25}}{(2{,}998\times10^8)^2} \approx 1{,}8\times10^{8}\ \text{kg/m}^3$$

### Sonuç
$$\boxed{P_0 \;\ge\; 1{,}6\times10^{25}\ \text{Pa}\,, \qquad \rho_0 = \frac{P_0}{c_0^2} \;\ge\; 1{,}8\times10^{8}\ \text{kg/m}^3 \qquad (\Sigma = 0\ \text{muhafazakâr hâl})}$$

Bu bir kesin değer değil, güvenli tarafta kalan bir **tabandır**; ortamın gerçek basıncı bağımsız sabitlemeyle (M-8) bu tabanın sekiz–dokuz mertebe üzerinde çıkar.

### Geçerlilik Sınırı
- Sonuç, kohezyonun sıfır sayıldığı en muhafazakâr hâldir. Kohezyon hesaba katıldığında genel koşul $P_0 + \Sigma > \Delta P$ biçimini alır (M-4); $\Sigma/P_0 > 10^8$ olduğundan genel koşul her durumda devasa marjla sağlanır.
- **Koşul yalnız basınç açığını değil, ortamın taşıdığı her gerilmeyi bağlar** *(17 Ağustos 2026'da eklendi)*. Bunun bir sonucu, ortamın **katı dönüşünün yasaklanmasıdır**: $\Omega$ ile katı dönen bir ortamda merkezcil gereksinim $\tau=\rho_0\Omega^2r^2/2$ gerilmesi ister ve bu $r$ ile **sınırsız büyür**; $r_{max}=\sqrt2\,v_m/\Omega$'da yırtılmama koşulu ihlal edilir. Ortam sınırsızsa (monizm) her $\Omega\neq0$ sonlu bir yarıçapta yırtar ⟹ **$\Omega=0$ tam**. Türetim ve gözlemsel karşılığı: **Ek M-53** (Ayak 2).
- İç gradyan profili homojen-küre idealleştirmesidir; gerçek yoğunluk profili $\Delta P$'yi $O(1)$ düzeyinde değiştirir, alt sınırın mertebesini değiştirmez.

### Açık Uçlar
- 5. adımdaki iki kat emniyet payının nicel gerekçelendirilmesi (çekirdek profili düzeltmeleriyle) veya kaldırılıp $\Delta P$'nin doğrudan taban alınması.
- Kohezyonlu genel koşul $P_0+\Sigma>\Delta P$ ile bu muhafazakâr alt sınırın tek metinde birleştirilmesi (7.4 md.10-i; M-4 Açık Uçlar ile ortak kalem).

---

## M-8 · Arka Plan Basıncının Gözlemsel Sabitlenmesi · **[S]**

**Kullanıldığı bölümler:** Ek B.3, 1.3 Postülat kutuları, 2.4.2 Yön Kuralı ($k$ oranının ana tanım evi), 7.4 md.10; Ek C satır 3–5. Bağlı katalog: **M-42** (ölçek yapısı $\Lambda$; bu türetimin 2 çarpanının kaynağı).

### Varsayımlar
1. Kavrama Yasası (M-1): $c_{loc}=\sqrt{P/\rho}$.
2. Kütle yakınındaki durum değişimi bir **deplasman** sürecidir (ortamın adiyabatik dalga tepkisi değil — ayrım için Ek M-44). Yoğunluğun basınca eşlik oranı $k$ ile parametrelenir (2.4.2 Yön Kuralı) ve deplasman süreci için **$k=0$**'dır: basınç düşer, ortalama yoğunluk korunur (M-15 G2; M-30 Varsayım 1). Aşağıdaki adımlar genel $k$ ile yürütülüp sonuçta bu değer konur:
$$\frac{\delta\rho}{\rho_0} = k\,\frac{\delta P}{P_0}\,, \qquad 0 \le k < 1$$
(Genel-$k$ yazımı yalnız türetimin yapısını göstermek içindir; deplasman kanalında değer taahhütlüdür: $k=0$ — M-44'ün kutulu sonucu.)
3. Gözlemsel girdi: yüzey potansiyel genliği $\Phi/c_0^2 \approx 7\times10^{-10}$ ($\Phi$: standart fiziğin yüzey kütleçekim potansiyeli, burada yalnızca ölçülen genliğin etiketi).
4. Yüzeydeki basınç açığı, M-7'nin gradyan yapısının **dış-bölge** integralinden: $\Delta P_{yüzey} = \int_R^\infty \rho_n g\,dr = \rho_n\,\Phi$ (çünkü $|\nabla P| = \rho_n g$ ve $\int_R^\infty g\,dr = \Phi$; M-7'nin *iç-bölge* integrali ayrı büyüklüktür — merkez–yüzey düşüşü, bunun yarısı).
5. **Ölçek yapısı (M-42):** madde ölçeği $\Lambda = 1-\Phi/c_0^2$ *(birinci mertebede; tam biçim $\Lambda=e^{-\Phi/c_0^2}$ — **Ek M-55**)* ile saat $f\propto\Lambda$, yayılma hızı $c_{loc}\propto\Lambda^2$; dolayısıyla $\delta c/c_0 = 2\,\delta f/f$, yani $\delta c/c_0 = -2\Phi/c_0^2$. Bu 2 çarpanı **ışık bükülmesi ölçümünden** ($1{,}751''$, Güneş kenarı) sabitlenmiştir — kızıla kaymadan değil. Kalibrasyon kaynağının bu değişimi aşağıda 2. adımın gerekçesidir.

### Adımlar
1. Kavrama Yasası'nın logaritmik diferansiyeli:
$$\frac{\delta c}{c_0} = \frac{1}{2}\left(\frac{\delta P}{P_0} - \frac{\delta\rho}{\rho_0}\right) = \frac{1-k}{2}\cdot\frac{\delta P}{P_0}$$
2. Yayılma hızındaki kayma, ölçek yapısının verdiği genliğe eşitlenir. Postülat 3 gereği saat hızı yerel ortama kilitlidir; ancak saat ile yayılma hızı **aynı** çarpanla ölçeklenmez: M-42 gereği $\delta c/c_0 = 2\,\delta f/f = -2\Phi/c_0^2$. (Eski türetim $\delta c/c_0=\delta f/f$ varsayıyordu; bu varsayım ışık bükülmesini gözlenenin tam yarısı kadar veriyordu.) Yüzeydeki değerle, genlik olarak:
$$\frac{1-k}{2}\cdot\frac{\Delta P_{yüzey}}{P_0} = \frac{2\Phi}{c_0^2}$$
3. $\Delta P_{yüzey} = \rho_n\Phi$ ikamesi yapılır; $\Phi$ her iki yanda sadeleşir — sonuç kütleden **bağımsız, evrensel** çıkar (M-42 gereği $\delta c/c_0 = -2\Phi/c_0^2$):
$$\frac{1-k}{2}\cdot\frac{\rho_n\,\Phi}{P_0} = \frac{2\Phi}{c_0^2} \;\Longrightarrow\; P_0 = \frac{1-k}{4}\,\rho_n c_0^2$$
4. Yoğunluk, $\rho_0 = P_0/c_0^2$ ile birlikte gelir.

### Sonuç
$$\boxed{P_0 = \frac{1-k}{4}\,\rho_n c_0^2 \;\xrightarrow{\;k=0\ (\text{M-44})\;}\; 6{,}07\times10^{33}\ \text{Pa}\,, \qquad \rho_0 = \frac{P_0}{c_0^2} = \frac{\rho_n}{4} \approx 6{,}8\times10^{16}\ \text{kg/m}^3}$$

$\rho_0 = \rho_n/4$: madde, okyanustan kopuk bir yabancı cisim değil, okyanusun yalnızca ~4 kat sıkışmış girdap fazıdır — monizm burada nicelleşir.

### Sayısal Çapraz Kontroller
- **Pürüz oranı:** Dünya'nın merkez–yüzey basınç düşüşü $\Delta P \approx 0{,}83\times10^{25}$ Pa (M-7), $P_0$'ın yanında $\Delta P/P_0 \sim 10^{-9}$'luk bir pürüzdür — gözlenen saat kaymalarının $10^{-9}$–$10^{-10}$ mertebesiyle birebir aynı orandır ✓.
- **Alt sınır tutarlılığı:** Sabitlenen değer, M-7'nin muhafazakâr tabanının sekiz–dokuz mertebe üzerindedir ($6{,}07\times10^{33}/1{,}6\times10^{25}\approx3{,}8\times10^{8}$); yırtılmama koşulu kohezyondan bağımsız olarak devasa marjla sağlanır ✓.

### Geçerlilik Sınırı
- $k$ eşlik oranı deplasman kanalı için **taahhütlüdür**: $k=0$ (M-44'ün kutulu sonucu; Ek C'de [T]). $P_0$ tam biçimiyle $\frac{1-k}{4}\rho_n c_0^2$ yazılır ve değeri $\tfrac14\rho_n c_0^2 = 6{,}07\times10^{33}$ Pa'dır. *(Düzeltme kaydı, 9 Ağustos 2026: eski "henüz taahhüt edilmedi / $O(1)$ belirsiz" kaydı ve $10^{33}$–$10^{34}$ aralık yazımı, M-44 öncesi dönemin kalıntısıydı.)*
- Türetim zayıf-alan (yüzey) genliğiyle yapılmıştır; güçlü sıkışma rejiminde ($k\to1$) doğrusal eşlik parametrelemesi geçerliliğini yitirir.

### Açık Uçlar
- **Kalibrasyon kaynağı notu (M-42):** $P_0$ artık kütleçekimsel kızıla kaymadan değil, **ışık bükülmesinden** ($1{,}751''$) sabitlenir — 2 çarpanını veren gözlem odur. Kızıla kayma bu zincirde serbest kalır ve **öngörü** konumuna geçer ($\delta f/f = -\Phi/c_0^2$); dolayısıyla GPS/Pound–Rebka artık girdi değil, bağımsız doğrulamadır. Ayrıntı ve muhasebe: **M-42**.
- $k$'nın SN 1987A gecikme bütçesiyle (2.4.4) bağımsız çapraz kontrolü (Ek C satır 3; 7.4).
- Bağımsızlık notu: $\mathcal{G}$'nin türetimi (M-28) yalnızca gradyan bağlaşımına ($\alpha$) dayanır ve $P_0$'ın mutlak değerinden bağımsızdır — bu sabitleme onu etkilemez; iki zincirin ayrıklığının açıkça belgelenmesi.

---

## M-9 · Ortamın Ağırlıksızlığı Teoremi · **[T]**

**Kullanıldığı bölümler:** Ek B.4, 1.3 Postülat kutuları (Postülat 1'in "ağırlıksız ortam" ifadesinin kanıt statüsü), 7.4 md.10.

### Varsayımlar
1. Teoride çekim diye bağımsız bir kuvvet yoktur; tek alan basınçtır, tek kuvvet $-\nabla P$'dir (Postülat 6, M-2). Standart fiziğin Poisson denklemi $\nabla^2\Phi_N = 4\pi G\rho_{toplam}$ ($\Phi_N$: Newton'un öz-kütleçekim potansiyeli, Ek D · S-28) — yani kütle yoğunluğunun kendiliğinden çekim alanı kaynakladığı önermesi — teorinin **reddettiği gizli varsayımdır**: ortam "ağırlıklı" değildir.
2. Kavrama Yasası (M-1) ve arka plan sabitlemesi (M-8) geçerlidir.
3. Kavitasyon eşiği (M-4): $v_{kav} = \sqrt{2}\,c_0\,\sqrt{1+\Sigma/P_0} \gg c_0$.

### Adımlar
1. **Ağırlıksızlık.** Ağırlık, kütlenin değil gradyanın — yani deplasmanın — özelliğidir (M-2: kuvvet $-\gamma_N\nabla P$'dir, $\rho$'nun değil). Homojen arka plan basınç alanının sıfır noktasıdır (datum): $\nabla P_0 = 0$ olduğundan hiçbir parçası kuvvet hissetmez; ortam kendi üzerine çökmez. Arşimet analojisi: kaldırma kuvveti nasıl mutlak yoğunluğun değil yoğunluk *farkının* olayıysa, Evrenakı ağırlığı da mutlak $\rho_0$'ın değil deplasman *açığının* olayıdır. $10^{16}$–$10^{17}$ kg/m³'lük ortamın "neden tartılmadığı" sorusu, 1. varsayımdaki reddedilen Poisson önermesini gizlice geri sokar.

   **Kozmolojik biçimi (aynı sorunun büyük ölçekte tekrarı).** Aynı itiraz kozmolojide daha keskin görünür: $\rho_0 \approx 6{,}8\times10^{16}$ kg/m³, kritik yoğunluğun ($\rho_{kritik}\approx9\times10^{-27}$ kg/m³) yaklaşık **43 mertebe** üstündedir; standart çerçevede böyle bir ortam evreni anında kapatırdı. Cevap aynı tek satırdır ve yeni varsayım gerektirmez: $\Omega$ parametreleri ve kritik yoğunluk, *doğrudan tartılmış* büyüklükler değildir — genişleme hızı, yapı oluşumu ve CMB akustik fiziğinden **Friedmann/Poisson kaynaklanması varsayılarak** çıkarılan büyüklüklerdir. Teori tam olarak o kaynaklanmayı reddettiği için $\rho_0$ bu çıkarımlara hiç girmez. Bu gözlemlerin kısıtladığı şey ortamın mutlak yoğunluğu değil, **deplasman envanteridir** (girdap/madde bütçesi ve onun gradyan alanı). Arşimet analojisinin kozmolojik karşılığı: okyanusun kendi yoğunluğu değil, içindeki cisimlerin açtığı hacim tartılır.

   Bu, gözlemsel yükü ortadan kaldırmaz, **yerini değiştirir:** açık olan şey $\rho_0$'ın büyüklüğü değil, CMB akustik pik oranlarının ve ilksel bolluk oranlarının teorinin kendi deplasman büyüklüklerinden nicel üretilmesidir (Bölüm 3.7.4 mekanizma düzeyinde kurar; nicel program 7.4'te kayıtlıdır).
2. **Kararlılık (Jeans'in iki bacağının da yokluğu).** Klasik öz-kütleçekimli akışkanda homojen durum kararsızdır (Jeans, 1902): yoğunlaşan bölge daha çok çeker, çöküş büyür. Evrenakı'da bu geri-beslemenin iki bacağı da yoktur: (i) yoğunlaşan bölge kimseyi çekmez, yalnızca basıncını yükseltir; (ii) sıkıştırılabilirlik pozitif olduğundan her yoğunluk pürüzü basınç dalgası olarak dağılır. İkinci bacak nicel olarak da kapalıdır. Dalga, deplasman alanı donmuşken ilerler ve o kanalda hâl denklemi Kavrama Yasası'nın kendisidir (**Ek M-44**), $P=c_0^2\rho$:
$$\left(\frac{\partial P}{\partial\rho}\right)_{\chi} = c_0^2 \;>\; 0 \qquad\Longrightarrow\qquad c_{pürüz}=c_0$$
Yani her yoğunluk pürüzü **tam $c_0$ hızında** yayılan bir basınç dalgası olarak dağılır. Sıkıştırılabilirlik her koşulda pozitif olduğundan kararsızlık penceresi hiçbir rejimde açılmaz; homojen durum yalnızca izinli değil, ortamın **tek doğal taban durumudur.**

Bu, ortamın **stiff (Zel'dovich) akışkan** olması demektir — ses hızının ışık hızına tam eşit olduğu, dalga sertliği en yüksek hâl. *(Adlandırma notu: standart kozmoloji bu hâle "nedensel olarak en katı" der, çünkü o çerçevede $c$ nedensellik tavanıdır; teoride $c_0$ tavan değildir — kohezyon kanalı $v_m>10^4c_0$ ile çalışır (M-5). Buradaki üstünlük sertliktir, tavan değil.)* Gözlemsel karşılığı doğrudandır: GW170817'nin kütleçekim dalgası ↔ ışık eşitliği ($10^{-15}$ hassasiyet) bu kanalı bağlar ve **otomatik olarak sağlanır**.

> *Kanal uyarısı: dağılma hızı $c_0/\sqrt k$ **değildir.** O okuma, Ek B.3'ün **deplasman** bağıntısını bir hâl denklemi sanmaktan doğar ve GW170817 ile 6,5 mertebe çelişir. Ek M-44 iki kanalı ayırır ($\chi$ sabit ↔ $\rho$ sabit) ve sıkışma hızı **tam $c_0$** çıkar.*

Postülat 4 ile çelişki yoktur: $c_0$ Zerre'nin çizgisel öteleme sınırıdır ve sıkışma kanalı da tam orada durur; ortamın $c_0$'yi **aşan** kanalı ayrıdır ve kohezyon kanalıdır ($v_m=c_0\sqrt{\Sigma/P_0}$, M-5).
3. **Arka plan kararlılığı (kendiliğinden madde doğumu yok; standart çatıda "vakum kararlılığı").** Arka planın "kaynayıp" kendiliğinden girdap-madde üretmesi için yerel akışın $v_{kav} = \sqrt{2}\,c_0\,\sqrt{1+\Sigma/P_0}$ eşiğine ulaşması gerekir (M-4); $\Sigma \gg P_0$ kohezyonlu süper-akışkanda rastgele dalgalanmalar bu eşiğe ulaşamaz. Uzayın durup dururken maddeye dönüşmemesi aynı çerçevenin bedava sonucudur.

### Sonuç
$$\boxed{\nabla P_0 = 0 \;\Rightarrow\; \text{homojen arka plan kuvvetsiz, kararlı ve doğurgan-değildir:}\quad \text{ortam ağırlıksızdır — tanım değil, teorem.}}$$

### Geçerlilik Sınırı
- Teorem homojen arka plan içindir. Kütle *çevresindeki* gradyan bölgesinde ortam tepkisiz değildir — gradyana cevap verir. **Cevabın biçimi ortamın kohezyonuna bağlıdır ve iki koldur.** Kohezyonsuz (Euler) limitte statik denge imkânsızdır ($\nabla\!\cdot\!\sigma=-\nabla P\neq0$) ve tek çıkış dolaşmaktır: gradyan, dolaşımın merkezcil ivmesiyle siklostrofik dengede taşınır,
$$\frac{\nabla P}{\rho_0} = \frac{v_\theta^2}{r}$$
Ama Evrenakı kohezyonludur (M-4, M-5: $\Sigma/P_0>10^8$) ve kohezyon kanalı kesme modülü rolündedir; dolayısıyla **ikinci kol açıktır: ortam kuyuyu dolaşmadan, statik elastik dengede tutabilir** ($\tau_{rr}=\rho_n\Phi/2$, $\Sigma$'nın on dört–on beş mertebe altında — **Ek M-51**). Gözlem bu ikinci kolu **seçer**: dört bağımsız gözlem ailesi (Merkür günberi, Ay perigee, Titan apsisi, Io apsisi) dolaşımı dışlar (**Ek M-52**), ve dolaşımın yokluğu üç yapısal nedenden türetilir (**Ek M-53**). Katı deplasman cebi (nükleon) ise akıp dengelenemez; bütün hâlde itilir. **Madde düşer, ortam gerilir.**
  *(Düzeltme kaydı, 17 Ağustos 2026: eski yazım *"cevabı düşmek değil dolaşmaktır"* diyor ve siklostrofik dengeyi tek seçenek sunuyordu; bu, Euler denkleminin — kohezyonsuz akışkanın — sonucudur ve teorinin kendi ortamı için eksiktir. Postülat 7–8'in sürüklenme ve vorteks alanları öteleme sektöründe geçerliliğini korur.)*
- 2. adımın dalga-dağılma bacağı, hâl denkleminin $\chi$-sabit kanalından gelen $(\partial P/\partial\rho)_\chi = c_0^2$ türetimi (Ek M-44) $k$'dan bağımsız olduğu için **$k$'nın izinli tüm aralığında ve her sıkışma genliğinde** geçerlidir; ayrı bir "güçlü sıkışma rejimi" çekincesi gerekmez. *($k$ yalnız deplasman kanalının parametresidir, dalga kanalına hiç girmez; $dP/d\rho=c_0^2/k$ okuması, yukarıdaki Kanal Uyarısı'nın dışladığı eski türetimdi — düzeltme kaydı, 9 Ağustos 2026.)*
- Kanıtlanan şey, **çöküşe karşı kararlılıktır** (Jeans tipi geri-besleme yok, $dP/d\rho>0$). Tam doğrusal-olmayan kararlılık — şok oluşumu, türbülans başlangıcı — ortamın hareket denklemlerinin bir eylem ilkesinden türetilmesini gerektirir; bu, teorinin bilinen ve ayrıca kayıtlı açığıdır (7.4).
- Kozmolojik biçimin cevabı (1. adım) bir **tutarlılık** sonucudur: $\rho_0$ ile kritik yoğunluk arasındaki 43 mertebelik farkın çelişki olmadığını gösterir, CMB/ilksel bolluk oranlarını üretmez.

### Açık Uçlar
- ~~Siklostrofik denge profilinin ($v_\theta(r)$) kütle çevresi sürüklenme zarfıyla nicel eşlenmesi~~ → **yeniden tanımlandı (17 Ağustos 2026):** eşlenecek nicelik dolaşım değil, **kohezyon payı ile dolaşım payının bölüşümüdür** (Ek M-51'in genel denge ifadesi). Gezegen ölçeğinde gözlem bölüşümü fiilen tümüyle kohezyona verir ($\lvert\Omega_{ortam}\rvert\le1{,}4\times10^{-18}$ s⁻¹, Ek M-52); kalan iş, zarf sınırındaki kayma tabakasının (Rampa profili, Ek C satır P2) yitim ve tork muhasebesidir.
- **Üç kanalın ortak mikro-modeli.** Ortamın üç ayrı tepki hızı vardır ve üçü ayrı katsayılardan gelir: **sıkışma** ($c_{pürüz}=c_0$, stiff hâl denklemi), **kohezyon/kesme** ($v_m=c_0\sqrt{\Sigma/P_0}>10^4c_0$, $\Sigma$'dan) ve **deplasman** (hız değil, $k=0$ ile tanımlı statik tepki). Sürekli ortamlar mekaniği bunlar arasında bir bağ gerektirmez — hacim ve kesme modülleri genel bir ortamda bağımsız malzeme sabitleridir ve M-5 bu bağımsızlığı açıkça varsayar. Açık olan soru: nükleonun vakum cepli girdap yapısı, üçünü birden veren tek bir mikro-model olabilir mi? Olursa $\Sigma$ de türetilmiş hale gelir ve Ek C'den bir kalem daha düşer. Bu, eylem ilkesi programına bağlıdır (7.4 md.16, Ek M-44 Açık Uçlar).

---

## M-51 · Ortamın Statik Dengesi: Kuyu Kesmeyle Tutulur · **[T]**

**Kullanıldığı bölümler:** M-9 (Geçerlilik Sınırı — bu girdi onu tamamlar), M-4/M-5 (kohezyon kanalı), M-2 (kütle-itim), M-22/M-37 (ortam profili), 3.4.x. Bağlı katalog: **M-52**, **M-53**.

### Varsayımlar
1. Kütle çevresinde basınç kuyusu vardır: $dP/dr>0$, dış alanda $P(r)=P_0-\rho_n\Phi(r)$ ile $\Phi=\mathcal{G}M/r\ge0$ (M-2'nin kuyu konvansiyonu; M-46'nın $\chi$ Poisson'u).
2. Ortam yalnız izotropik basınç taşımaz: **kohezyon dayanımı $\Sigma$ vardır** (M-4) ve $\Sigma$ kesme/gerilme kanalının modülü rolündedir — $v_m=\sqrt{\Sigma/\rho_0}$ (M-5). Gözlemsel taban $\Sigma/P_0>10^8$ (Salart ve ark., 2008).
3. Durağan hâl ($\partial\vec v/\partial t=0$) ve küresel simetri.

### Adımlar
1. **Euler denklemi kohezyonsuz limittir.** Gerilme tensörü yalnız izotropik alınırsa ($\sigma_{ij}=-P\delta_{ij}$), statik denge imkânsızdır: $\nabla\!\cdot\!\sigma=-\nabla P\neq0$; ortamın tek çıkışı dolaşmaktır.
2. **Kohezyonlu ortamda gerilme tensörü izsiz bir pay taşır:** $\sigma_{ij}=-P\delta_{ij}+\tau_{ij}$, $\operatorname{tr}\tau=0$. Statik denge $\nabla\!\cdot\!\sigma=0$; küresel simetride radyal bileşen
$$\frac{d\sigma_{rr}}{dr}+\frac{2\sigma_{rr}-\sigma_{\theta\theta}-\sigma_{\varphi\varphi}}{r}=0$$
3. İzsizlik ($\tau_{rr}+2\tau_{\theta\theta}=0\Rightarrow\tau_{rr}-\tau_{\theta\theta}=\tfrac32\tau_{rr}$) konularak:
$$\frac{d\tau_{rr}}{dr}+\frac{3\tau_{rr}}{r}=\frac{dP}{dr}=\frac{\rho_n\mathcal{G}M}{r^2} \;\Longleftrightarrow\; \frac{1}{r^3}\frac{d\left(r^3\tau_{rr}\right)}{dr}=\frac{\rho_n\mathcal{G}M}{r^2}$$
4. Sonsuzda sönen çözüm (homojen kol $C/r^3$ için $C=0$).

### Sonuç
$$\boxed{\;\tau_{rr}=\frac{\rho_n\mathcal{G}M}{2r}=\frac{\rho_n\Phi}{2}=\frac{\Delta P}{2}\,,\qquad \tau_{\theta\theta}=\tau_{\varphi\varphi}=-\frac{\tau_{rr}}{2}\;}$$

Kuyuyu tutmak için gereken kesme gerilmesi, **basınç açığının tam yarısıdır** ve ortam bunu **dolaşmadan** sağlar. Genel denge, dolaşım ile kohezyonun bölüşümüdür:
$$\frac{1}{\rho_0}\frac{dP}{dr}=\underbrace{\frac{v_\theta^2}{r}}_{\text{dolaşım payı}}+\underbrace{\frac{1}{\rho_0}\left(\frac{d\tau_{rr}}{dr}+\frac{3\tau_{rr}}{r}\right)}_{\text{kohezyon payı}}$$
$v_\theta=2v_{yör}$ (M-37), kohezyon payının sıfır olduğu **kohezyonsuz üst sınırdır**; $v_\theta=0$ izinlidir ve kohezyon tüm yükü taşır.

> **Madde kesmeyi görmez — bağlayıcı kayıt.** M-2'nin Varsayım 2'si itimin **deplase edilen hacimle** orantılı olduğunu söyler; deplase hacim bir **skalerdir** ve deplasman cebi gerilme tensörünün **izine** (basınca) bağlanır. $\tau$ **izsizdir**, saf hacim dışlamasıyla çiftlenmez. Sonuç: ortam kendini kesmeyle ayakta tutar (madde bunu hissetmez), madde yalnız basınç gradyanını hisseder — **M-2 aynen geçerlidir.**

> **$\Sigma$'nın yapısal görevi — bu girdinin en önemli sonucu.** $\Sigma$ bu girdiden önce yalnız Bell tipi deneylerden alttan sınırlı, teorinin başka hiçbir yerine yük taşımayan bir kalemdi. M-52 ile birlikte statüsü değişir: ortam dolaşmak *zorunda kalırsa* kapalı elips yörüngeler var olamaz, ve kuyuyu dolaşmadan tutan tek mekanizma kohezyondur. Dolayısıyla **kohezyon kanalı, Kepler yörüngelerinin var olabilmesinin yapısal koşuludur** — $\Sigma$ için Bell deneylerinden **tamamen bağımsız ikinci bir gerekçe.** *(Nicel yeni bir alt sınır vermez; gereken $\tau$ zaten $\Sigma$'nın çok altındadır. Kazanç yapısaldır.)*

### Sayısal Çapraz Kontroller
$\Sigma$'nın yalnız **alt sınırıyla** ($\Sigma\ge10^8P_0=6{,}07\times10^{41}$ Pa):

| Konum | $\Phi/c_0^2$ | $\tau_{rr}$ (Pa) | $\tau_{rr}/\Sigma$ |
|---|---|---|---|
| Merkür yörüngesi | $2{,}55\times10^{-8}$ | $3{,}10\times10^{26}$ | $5{,}1\times10^{-16}$ |
| Dünya yörüngesi | $9{,}87\times10^{-9}$ | $1{,}20\times10^{26}$ | $2{,}0\times10^{-16}$ |
| Güneş yüzeyi | $2{,}12\times10^{-6}$ | $2{,}58\times10^{28}$ | $4{,}2\times10^{-14}$ |
| Dünya yüzeyi | $6{,}96\times10^{-10}$ | $8{,}45\times10^{24}$ | $1{,}4\times10^{-17}$ |
| Samanyolu (Güneş yarıçapı) | $4{,}45\times10^{-7}$ | $5{,}40\times10^{27}$ | $8{,}9\times10^{-15}$ |
| Nötron yıldızı yüzeyi | $0{,}172$ | $2{,}09\times10^{33}$ | $3{,}4\times10^{-9}$ |

**On dört–on beş mertebe marj**; nötron yıldızı yüzeyinde dahi dokuz mertebe. Elastik zorlanma $\varepsilon\sim\tau/\Sigma\sim10^{-16}$.

### Geçerlilik Sınırı
- Küresel simetri ve durağan hâl varsayılmıştır; dönen/basık kaynaklarda $\tau$'nun açısal yapısı devreye girer.
- Homojen kolun ($C/r^3$) katsayısı sonsuzda sönme koşuluyla sıfırlanmıştır; **kaynak içinde** eşleme yapılmamıştır.
- Marjlar $\Sigma$'nın alt sınırıyladır; gerçek $\Sigma$ büyükse marj yalnız büyür (bu yönde duyarsız).
- Yalnız elastik (modül) rol kullanılmıştır; kesmenin akış/viskozite kanalıyla ilişkisi kurulmamıştır.

### Açık Uçlar
- Zarf sınırındaki **kayma tabakası** (Dünya zarfı $\sim30$ km/s, Güneş zarfı $\sim220$ km/s) statik resimde gerçek bir kesme tabakasıdır; gereken gerilme $\sim\rho_0v^2=3{,}3\times10^{27}$ Pa ile $\Sigma$'nın altındadır, ama yitim ve tork hesabı açıktır (7.4).
- Kaynak içi eşleme ve $\tau$'nun gövde sınırındaki sürekliliği.
- $\Sigma$'nın kesme **modülü** mü **dayanımı** mı olduğunun ayrımı (M-4/M-5 ikisini tek sembolle taşır); elastik zorlanma hesabı modül okumasını gerektirir.

---

## M-52 · Ortam Dönüşü Kilit Teoremi: $\Omega_m=2n$ · **[T]**

**Kullanıldığı bölümler:** M-9, M-22, M-37 (profil teoreminin statüsü), M-51, 6.3, 11.3, 11.4, 11.5. Bağlı katalog: **M-53**.

### Varsayımlar
1. Siklostrofik dolaşım hipotezi (M-22/M-37'nin ortam kolonu): $w(r)=v_\theta(r)=2v_{yör}(r)=2\sqrt{\mathcal{G}M/r}$. *(Oran $\sqrt{\rho_n/\rho_0}=2$ tamdır; $\rho_0=\rho_n/4$, M-8.)*
2. Cismin dinamiği **yerel ortama göre** tanımlıdır (11.4.8.1: *"$V$, maddenin yerel ortama göre hızıdır"*).
3. Yörünge dairesele yakın; dolaşım yörünge düzleminde.

### Adımlar
1. **Dolaşan ortamın açısal hızı:**
$$\Omega_m=\frac{w(r)}{r}=\frac{2\sqrt{\mathcal{G}M/r}}{r}=2\sqrt{\frac{\mathcal{G}M}{r^3}}=\boxed{2n}$$
$n$ ortalama harekettir. **Oran kütleden ve yarıçaptan bağımsızdır.**
2. **Dinamiği ortama referanslı bir cismin apsisleri ortamla birlikte sürüklenir.** Katı dolaşım limitinde bu, eş-dönen çerçeveye geçmenin doğrudan sonucudur: o çerçevede yörünge kapalı elipstir, laboratuvar çerçevesinde $\Omega_m$ ile devinir. Diferansiyel dolaşımda sürüklenme hızı mertebe olarak yine $\Omega_m$'dir.
3. **Kategorik sonuç:** $\Omega_m=2n$ ise apsis çizgisi **her radyal periyotta tam iki tur** atar; yörünge kapalı elips değil, hızla dönen bir rozettir.

### Sonuç
$$\boxed{\;\text{Siklostrofik dolaşım}\;\Longrightarrow\;\Omega_{apsis}=2n\;\Longrightarrow\;\textbf{kapalı elips yörünge var olamaz}\;}$$

> **Gözlenen kapalı elipslerin varlığı, tek başına, ortamın dolaşmadığının kanıtıdır.** Bu bir hassasiyet sınavı değildir: siklostrofik hipotez altında Kepler yörüngeleri hiç oluşmaz. Ölçüm hassasiyeti yalnız **kalan** dönüşün üst sınırını belirler.

### Sayısal Çapraz Kontroller
**(a) Teorem denetimi.** $\Omega_m/n$ oranı Merkür, Ay, Titan ve Mimas'ta **2,0000000000**.

**(b) Satürn sistemi** ($J_2$-hâkim apsidal presesyonla kıyas, $\dot\omega=\tfrac32nJ_2(R_S/a)^2(1-e^2)^{-2}$):

| Uydu | $a$ (km) | Gözlenen apsis periyodu | Dolaşımın vereceği | **Dışlama** |
|---|---|---|---|---|
| Mimas | 185.539 | 1,0 yıl | 11,3 saat | $7{,}8\times10^2$ |
| Enceladus | 237.948 | 2,4 yıl | 16,5 saat | $1{,}3\times10^3$ |
| Dione | 377.396 | 12,0 yıl | 1,4 gün | $3{,}2\times10^3$ |
| Rhea | 527.108 | 38,7 yıl | 2,3 gün | $6{,}3\times10^3$ |
| **Titan** | 1.221.870 | **733 yıl** | **8,0 gün** | $\mathbf{3{,}4\times10^4}$ |

*(Iapetus'ta Güneş pertürbasyonu $J_2$'yi aşar; sağlam sınır Titan'dır. Phoebe için dolaşan ortam 4 Gyr'de $5{,}3\times10^9$ tur verirdi.)*

**(c) Dört bağımsız ortam:**

| Ortam | Sınayan gözlem | Dışlama | Kalan dönüş üst sınırı |
|---|---|---|---|
| **Güneş** | Merkür günberi $575{,}3100\pm0{,}0015''$/yy (Park ve ark., 2017) | $1{,}9\times10^6$ | $\lvert\Omega\rvert\le2{,}3\times10^{-18}$ s⁻¹ |
| **Dünya** | Ay perigee presesyonu 8,85 yıl (LLR) | $2{,}4\times10^2$ | $\lesssim2\times10^{-16}$ s⁻¹ |
| Dünya | LAGEOS-2 ($J_2$-hâkim) | $4{,}5\times10^3$ | — |
| **Satürn** | Titan apsisi | $3{,}4\times10^4$ | $\lesssim2{,}7\times10^{-15}$ s⁻¹ |
| **Jüpiter** | Io apsisi ($J_2$-hâkim) | $3{,}2\times10^3$ | — |

**(d) Merkür'ün yeni rolü.** $\lvert\Omega_{ortam}\rvert\le1{,}4\times10^{-18}$ s⁻¹ (1σ), yani Merkür yörüngesinde teğetsel hız $\le81$ nm/s; bir tam tur $1{,}4\times10^{11}$ yıl = evren yaşının **on katı**. Güneş sisteminin ortamı, evren yaşı ölçeğinde fiilen dönmemektedir. **Standart görelilikte bu okumanın karşılığı yoktur** — orada ortam yoktur.

### Geçerlilik Sınırı
- Kilit **yörünge apsisleri** üzerinden çalışır; apsis ölçümü olmayan ölçeklerde (galaktik) doğrudan uygulanamaz — orada hüküm M-53'ün Ayak 1'inden gelir.
- 2. adımın diferansiyel dolaşım hâli mertebe argümanıdır; katsayı sayısal olarak doğrulanmıştır, analitik genel çözüm verilmemiştir.
- Satürn/Jüpiter dışlamaları $J_2$-hâkim apsidal hızla kıyaslanmıştır; gerçek efemerid artıklarıyla sınırlar bir–iki mertebe sıkışabilir.
- Sonuç madde ölçeği $\Lambda$'nın **biçiminden bağımsızdır**; yalnız yörünge kinematiği ve ortama-referanslılık kullanılır.

### Açık Uçlar
- Iapetus kanalının gerçek efemerid artıklarıyla işlenmesi (Satürn sınırı $\sim10^{-17}$ s⁻¹'e inebilir).
- Galaktik ortamın dönüş durumunun bağımsız gözlemsel kilidi (apsis kanalı yok).
- **Statü değişimi kaydı.** M-37'nin $v_\theta=2v_{yör}$ profil teoremi **kohezyonsuz üst sınır** statüsüne iner: türetimi doğrudur ($\sqrt{\rho_n/\rho_0}=2$ tam) ama zorunluluk değildir ve gezegen ölçeğinde gözlemle dışlanmıştır. M-22'nin *"dönen ortam merkezkaç gereksinimini basınç gradyanıyla karşılar"* varsayımı **opsiyonel dinamik durum** olarak okunmalıdır. M-37'nin **madde kolonu** ($v_{yör}=\sqrt{R\lvert a_{madde}\rvert}$, gözlenen dönüş eğrisi) bundan **etkilenmez** — o yalnız M-2 ve akı geometrisini kullanır.
- **Bedel kaydı (dürüst).** Dolaşıma dayanan retrograd/prograd sürükleme asimetrisi ($\Delta v=v$ ↔ $3v$, sürükleme $\propto\Delta v^4$ ⟹ **81 katı**; Triton, DY-2) statik ortamda **oran 1**'e iner. Prograd hesaplar değişmez ($\lvert v-2v\rvert=\lvert v-0\rvert=v$); yalnız retrograd kalemler 81 kat zayıflar ve Phoebe'nin $\eta_E$ sınırı **gevşer**. 7.4 md.15 bu ayrımı zaten sınav olarak kaydetmiştir; statik çözüm *"fark sıfır"* öngörür — kaybedilen bir öngörü değil, **karara bağlanmış** bir öngörü.

---

## M-53 · Dolaşımın Yokluğunun Türetimi: Üç Ayak · **[T]**

**Kullanıldığı bölümler:** M-4, M-5, M-7, M-9, M-43, M-51, M-52.

> **Neden gerekli:** M-51 dolaşımın yokluğunu **izinli** kılar, M-52 onu **gözlemsel olarak** doğrular. Ama açısal momentum serbest bir başlangıç koşuludur; teorinin *neden* sıfır olduğunu söylemesi gerekir — yoksa sonuç "şanslı başlangıç koşulu" olarak kalır.

### AYAK 3 (yük taşıyıcı) — Madde ortamı döndüremez
Kesmeyi yaratacak tek kaynak maddedir; iki bağımsız kanal da kapalıdır.

**(a) Enerji kanalı.** Maddenin dönme enerji yoğunluğu ile $\Sigma$ kıyası:

| Sistem | $E_{dönme}/V$ (Pa) | $/\Sigma$ |
|---|---|---|
| Güneş (dönme) | $1{,}7\times10^{14}$ | $2{,}8\times10^{-28}$ |
| Jüpiter | $1{,}5\times10^{11}$ | $2{,}4\times10^{-31}$ |
| Güneş sistemi yörünge KE | $5{,}0\times10^{4}$ | $8{,}3\times10^{-38}$ |
| Galaksi (dönme) | $2{,}4\times10^{-10}$ | $4{,}0\times10^{-52}$ |

**(b) Sürüklenme kanalı.** M-43'ün altkritik bastırması $\sim10^{28}$ ⇒ tork kanalı kapalı.

M-9'un teoremiyle birleşince (*"homojen durum yalnızca izinli değil, ortamın tek doğal taban durumudur"*): **kesme hiç doğmadı.** Açısal momentum maddede kalır — yıldızın spininde ve gezegenlerin yörüngelerinde; gözlenen de budur.

### AYAK 1 — Diferansiyel dönüş bir denge durumu değildir
M-5 kohezyon kanalını **kesme modülü** rolünde kurar ($\Sigma\leftrightarrow G_s$, $v_m=\sqrt{\Sigma/\rho_0}>10^4c_0$). Kesme modülü olan ortam **kararlı kesme akışı taşımaz**: diferansiyel dönüş zorlanma biriktirir, elastik geri-çağırma devreye girer, sistem sıfır-kesme durumu etrafında **salınır**. Siklostrofik profil ($\Omega\propto r^{-3/2}$) bu yüzden bir denge çözümü değildir.

Salınım periyodu $L/v_m$:

| Ölçek | $L/v_m$ | Yörünge / salınım |
|---|---|---|
| Ay yörüngesi | $1{,}3\times10^{-4}$ s | $1{,}8\times10^{10}$ |
| **Merkür yörüngesi** | **0,019 s** | $\mathbf{3{,}9\times10^{8}}$ |
| 1 AU | 0,050 s | $6{,}3\times10^{8}$ |
| Galaksi (10 kpc) | 3,3 yıl | $6{,}7\times10^{7}$ |
| Hubble yarıçapı | **$1{,}37\times10^{6}$ yıl** | $1{,}0\times10^{4}$ |

**(i)** M-52'nin ölçtüğü sekülér apsis hızı tanım gereği $\langle w\rangle/r=0$'dır. **(ii)** Hubble ölçeğinde elastik denkleşme evren yaşının $10^{-4}$'üdür; ilksel diferansiyel dönüş, hangi başlangıç koşulundan başlanırsa başlansın $10^4$ denkleşme süresi önce silinmiş olurdu.

### AYAK 2 — Katı dönüş, sınırsız kohezyonlu ortamda yasaktır
Kesme içermeyen tek dönüş katı dönüştür; Ayak 1 onu dışlamaz. Ama merkezcil gereksinim gerilme ister:
$$\frac{dP}{dr}=\rho_0\Omega^2r \;\Longrightarrow\; \tau_{gerekli}=\frac{\rho_0\Omega^2r^2}{2}\,,\qquad r_{max}=\frac{\sqrt{2\Sigma/\rho_0}}{\Omega}=\frac{\sqrt2\,v_m}{\Omega}$$
$r>r_{max}$'ta **M-7'nin yırtılmama koşulu ihlal edilir.** Yırtılma gözlenebilir evrenin içinde olmasın koşuluyla yapısal sınır $\lvert\Omega\rvert<3{,}3\times10^{-14}$ s⁻¹ (gözlem bundan $1{,}4\times10^4$ kat sıkı). **Ortam sınırsızsa** (monizm) her $\Omega\neq0$ sonlu bir yarıçapta yırtar:
$$\boxed{\;\text{sınırsız kohezyonlu ortam}\;\Longrightarrow\;\Omega=0\ \text{tam}\;}$$

### Sonuç
$$\boxed{\;\text{Diferansiyel dönüş: denge değil (Ayak 1)}\;\cdot\;\text{Katı dönüş: M-7 ihlali (Ayak 2)}\;\cdot\;\text{Madde onu kuramaz (Ayak 3)}\;}$$
Dolaşımın yokluğu artık izin verilen bir seçenek değil, **üç bağımsız yapısal nedenin sonucudur.**

### Sayısal Çapraz Kontroller ve iş bölümü kaydı
**⚠ Ayak 1 tek başına yetmez ve bu açıkça kaydedilmelidir.** Viskozite sıfıra yakın olduğundan salınım **sönmez**: Kelvin–Voigt sönüm süresi ($\eta\le2{,}3\times10^{-11}$ Pa·s ile) 1 AU ölçeğinde $5{,}3\times10^{40}$ yıl. Ve $\langle w\rangle=0$ olsa da $\langle w^2\rangle\neq0$; $\Lambda_{kin}$ $\lvert v-w\rvert$'ye bağlı olduğundan bu bir ek saat terimi verir, $\langle w^2\rangle/2c_0^2$. Merkür yörüngesinde $w_{genlik}=f\,v_{yör}$ için terim$/(\Phi/c_0^2)=f^2/4$:

| $f$ | $w_{genlik}$ | terim$/(\Phi/c_0^2)$ |
|---|---|---|
| 1,0 | 47,9 km/s | **0,25** |
| 0,1 | 4,8 km/s | $2{,}5\times10^{-3}$ |
| **0,02** | **957 m/s** | $\mathbf{10^{-4}}$ |

Tam genlikte terim, kızıla kayma genliğinin **kendisi mertebesindedir** ve kalibrasyonu çökertir. Kızıla kaymanın $\sim10^{-4}$ bağıl doğrulanması (GPS; Pound–Rebka) **$w_{genlik}\le0{,}02\,v_{yör}$** dayatır. **Çözüm: salınım hiç uyarılmadı** — Ayak 3 + M-9.

> **İş bölümü bağlayıcıdır:** Ayak 3 + M-9 kesmenin *hiç doğmadığını*, Ayak 1 *doğsa bile kararlı kalamayacağını*, Ayak 2 katı dönüşün de yasak olduğunu gösterir.

### Geçerlilik Sınırı
- Ayak 2'nin en güçlü kolu ($\Omega=0$ tam) ortamın **uzaysal sınırsızlığına** dayanır; monizm bunu ima eder ama kozmolojik erimle ($S_{kozmik}$, M-31) ilişkisi yazılmamıştır. Hubble-kesikli kolda sonuç $3{,}3\times10^{-14}$ s⁻¹'de kalır.
- Sayılar $\Sigma$'nın alt sınırıyladır ve **duyarlılık ters yönlüdür:** büyük $\Sigma$ Ayak 1 ve 3'ü güçlendirir, Ayak 2'nin yapısal sınırını ($\propto v_m$) gevşetir.
- Ayak 1'in salınım genliği ilksel koşula bağlıdır ve teori onu türetmez; kısıt gözlemseldir.
- Kelvin–Voigt sönüm hesabı $\eta_E$'yi ortamın kesme viskozitesi olarak okur; bu özdeşleştirme kurulmamıştır ($\eta_E$ artık kuplaj katsayısıdır, M-43).

### Açık Uçlar
- Ortamın uzaysal eriminin kozmolojik çatıyla eşlenmesi.
- Salınım genliğinin ilksel değerinin teori-içi türetimi.
- Galaktik ölçekte hüküm: denkleşme süresi 3,3 yıl olduğundan galaktik ortam da diferansiyel dönemez — M-37'nin galaktik **ortam kolonunu** da dışlar (madde kolonu etkilenmez).

---

## M-54 · Mach Sonucu: Yerel Eylemsizlik Çerçevesinin Küresel Kilidi · **[T]**

**Kullanıldığı bölümler:** M-5, M-51, M-53; 7.7 (modern fiziğin açık krizleri), 11.3 / 11.4.8.1 (tercihli çerçeve).

### Sorun
**Yerel eylemsizlik çerçevesi neden uzak maddeye göre dönmez?** Newton'da bu bir tanımdır (mutlak uzay); genel görelilikte kozmolojik madde dağılımından gelen bir uyum sorunudur (Mach ilkesi). Hiçbir çatıda mekanik bir taşıyıcısı yoktur.

### Varsayımlar
1. Ortam **tek sürekli** gövdedir (Postülat 1, monizm).
2. Kesme rijitliği vardır: $v_m=\sqrt{\Sigma/\rho_0}>10^4c_0$ (M-5).
3. Ortam dolaşmaz (M-51, M-52, M-53).

### Adımlar
1. Bir ortam yaması komşularına göre dönmek isterse kesme zorlanması doğar; elastik geri-çağırma bunu $v_m$ hızıyla iletir.
2. Ölçek $L$ üzerinde dönüş durumunun denkleşme süresi $L/v_m$'dir.
3. Her yerel yama **küresel ortam durumuna elastik olarak kilitlidir**; küresel durum ise dönmeyendir (M-53).

### Sonuç
$$\boxed{\;\text{Yerel eylemsizlik çerçevesi, kesme rijitliği yoluyla küresel ortam durumuna kilitlidir}\;}$$
Yerel eylemsizlik çerçevesinin uzak maddeye göre dönmemesi, bu teoride bir postülat ya da kozmolojik uyum değil, **kohezyon kanalının bedava sonucudur.**

> **Tercihli çerçevenin yeni okuması.** Teoride tercihli çerçeve **vardır** — ama küresel olarak **tek ve dönmeyendir**. 11.4.8.1'in *"tercihli çerçeve ortadan kalkmaz, yalnız doğrusal rejimde gözlenemez hâle gelir"* kaydı böylece dönme sektöründe tamamlanır: orada tercihli çerçeve yalnız gözlenemez değil, **küresel olarak biriciktir**.

### Sayısal Çapraz Kontroller
| Ölçek | Kesme denkleşme süresi $L/v_m$ |
|---|---|
| Güneş sistemi (100 AU) | **5,0 saniye** |
| Galaksi (10 kpc) | **3,3 yıl** |
| Gözlenebilir evren ($1{,}3\times10^{26}$ m) | **$1{,}37\times10^{6}$ yıl** |

Evren yaşının ($1{,}38\times10^{10}$ yıl) $10^{-4}$'ü ⇒ kilitlenme kozmolojik ölçekte **anlıktır**.

### Geçerlilik Sınırı
- Sonuç **dönme (kesme)** sektörüne ilişkindir; **öteleme** sektöründe tercihli çerçeve zarf hiyerarşisiyle yerelleşir (Postülat 7; 11.4.8.1). İkisi karıştırılmamalıdır.
- $v_m$ alt sınırıyla hesaplanmıştır; büyük $\Sigma$ denkleşmeyi yalnız hızlandırır.
- Nicel bir Mach-tipi öngörü türetilmemiştir; sonuç **mekanizma düzeyindedir**.

### Açık Uçlar
- Kalan sızıntının nicelenmesi: sonlu $v_m$ ile kilitlenme tam değil, $\sim L/v_m$ gecikmelidir; gözlemsel imzası hesaplanmalıdır.
- CMB dipolüyle (öteleme sektörü) ve galaktik dönüşle (kesme sektörü) çapraz denetim.
- Standart fizikteki Mach tartışmasıyla (Brans–Dicke, Lense–Thirring kozmolojik toplamı) karşılaştırmalı kutu — 7.7'ye adaydır.
