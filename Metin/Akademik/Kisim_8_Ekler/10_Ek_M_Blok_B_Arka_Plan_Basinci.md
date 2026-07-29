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
6. Yoğunluk tabanı Kavrama Yasası'ndan (M-1, $c=\sqrt{P/\rho}$ eşitliğinin arka plan hâli $\rho_0 = P_0/c^2$):
$$\rho_0 = \frac{P_0}{c^2} \ge \frac{1{,}6\times10^{25}}{(2{,}998\times10^8)^2} \approx 1{,}8\times10^{8}\ \text{kg/m}^3$$

### Sonuç
$$\boxed{P_0 \;\ge\; 1{,}6\times10^{25}\ \text{Pa}\,, \qquad \rho_0 = \frac{P_0}{c^2} \;\ge\; 1{,}8\times10^{8}\ \text{kg/m}^3 \qquad (\Sigma = 0\ \text{muhafazakâr hâl})}$$

Bu bir kesin değer değil, güvenli tarafta kalan bir **tabandır**; ortamın gerçek basıncı bağımsız sabitlemeyle (M-8) bu tabanın sekiz–dokuz mertebe üzerinde çıkar.

### Geçerlilik Sınırı
- Sonuç, kohezyonun sıfır sayıldığı en muhafazakâr hâldir. Kohezyon hesaba katıldığında genel koşul $P_0 + \Sigma > \Delta P$ biçimini alır (M-4); $\Sigma/P_0 > 10^8$ olduğundan genel koşul her durumda devasa marjla sağlanır.
- İç gradyan profili homojen-küre idealleştirmesidir; gerçek yoğunluk profili $\Delta P$'yi $O(1)$ düzeyinde değiştirir, alt sınırın mertebesini değiştirmez.

### Açık Uçlar
- 5. adımdaki iki kat emniyet payının nicel gerekçelendirilmesi (çekirdek profili düzeltmeleriyle) veya kaldırılıp $\Delta P$'nin doğrudan taban alınması.
- Kohezyonlu genel koşul $P_0+\Sigma>\Delta P$ ile bu muhafazakâr alt sınırın tek metinde birleştirilmesi (7.4 md.10-i; M-4 Açık Uçlar ile ortak kalem).

---

## M-8 · Arka Plan Basıncının Gözlemsel Sabitlenmesi · **[S]**

**Kullanıldığı bölümler:** Ek B.3, 1.3 Postülat kutuları, 2.4.2 Yön Kuralı ($k$ oranının ana tanım evi), 7.4 md.10; Ek C satır 3–5. Bağlı katalog: **M-42** (ölçek yapısı $\Lambda$; bu türetimin 2 çarpanının kaynağı).

### Varsayımlar
1. Kavrama Yasası (M-1): $c=\sqrt{P/\rho}$.
2. Kütle yakınındaki durum değişimi bir **deplasman** sürecidir (ortamın adiyabatik dalga tepkisi değil — ayrım için Ek M-44). Yoğunluğun basınca eşlik oranı $k$ ile parametrelenir (2.4.2 Yön Kuralı) ve deplasman süreci için **$k=0$**'dır: basınç düşer, ortalama yoğunluk korunur (M-15 G2; M-30 Varsayım 1). Aşağıdaki adımlar genel $k$ ile yürütülüp sonuçta bu değer konur:
$$\frac{\delta\rho}{\rho_0} = k\,\frac{\delta P}{P_0}\,, \qquad 0 \le k < 1$$
($k<1$: teori, basıncın oransal olarak daima daha hızlı düştüğünü söyler; kesin oran açık iştir.)
3. Gözlemsel girdi: yüzey potansiyel genliği $\Phi/c^2 \approx 7\times10^{-10}$ ($\Phi$: standart fiziğin yüzey kütleçekim potansiyeli, burada yalnızca ölçülen genliğin etiketi).
4. Yüzeydeki basınç açığı, M-7'nin gradyan integral yapısından: $\Delta P_{yüzey} = \rho_n\,\Phi$ (çünkü $|\nabla P| = \rho_n g$ ve $\int g\,dr = \Phi$).
5. **Ölçek yapısı (M-42):** madde ölçeği $\Lambda = 1-\Phi/c^2$ ile saat $f\propto\Lambda$, yayılma hızı $c\propto\Lambda^2$; dolayısıyla $\delta c/c = 2\,\delta f/f$, yani $\delta c/c = -2\Phi/c^2$. Bu 2 çarpanı **ışık bükülmesi ölçümünden** ($1{,}751''$, Güneş kenarı) sabitlenmiştir — kızıla kaymadan değil. Kalibrasyon kaynağının bu değişimi aşağıda 2. adımın gerekçesidir.

### Adımlar
1. Kavrama Yasası'nın logaritmik diferansiyeli:
$$\frac{\delta c}{c} = \frac{1}{2}\left(\frac{\delta P}{P_0} - \frac{\delta\rho}{\rho_0}\right) = \frac{1-k}{2}\cdot\frac{\delta P}{P_0}$$
2. Yayılma hızındaki kayma, ölçek yapısının verdiği genliğe eşitlenir. Postülat 3 gereği saat hızı yerel ortama kilitlidir; ancak saat ile yayılma hızı **aynı** çarpanla ölçeklenmez: M-42 gereği $\delta c/c = 2\,\delta f/f = -2\Phi/c^2$. (Eski türetim $\delta c/c=\delta f/f$ varsayıyordu; bu varsayım ışık bükülmesini gözlenenin tam yarısı kadar veriyordu.) Yüzeydeki değerle, genlik olarak:
$$\frac{1-k}{2}\cdot\frac{\Delta P_{yüzey}}{P_0} = \frac{2\Phi}{c^2}$$
3. $\Delta P_{yüzey} = \rho_n\Phi$ ikamesi yapılır; $\Phi$ her iki yanda sadeleşir — sonuç kütleden **bağımsız, evrensel** çıkar (M-42 gereği $\delta c/c = -2\Phi/c^2$):
$$\frac{1-k}{2}\cdot\frac{\rho_n\,\Phi}{P_0} = \frac{2\Phi}{c^2} \;\Longrightarrow\; P_0 = \frac{1-k}{4}\,\rho_n c^2$$
4. Yoğunluk, $\rho_0 = P_0/c^2$ ile birlikte gelir.

### Sonuç
$$\boxed{P_0 = \frac{1-k}{4}\,\rho_n c^2 \sim 10^{33}\text{–}10^{34}\ \text{Pa}\,, \qquad \rho_0 = \frac{P_0}{c^2} = \frac{1-k}{4}\,\rho_n \sim 10^{16}\text{–}10^{17}\ \text{kg/m}^3}$$

$k=0$ özel hâlinde $P_0 \approx 6{,}1\times10^{33}$ Pa ve $\rho_0 \approx 6{,}8\times10^{16}$ kg/m³ $= \rho_n/4$: madde, okyanustan kopuk bir yabancı cisim değil, okyanusun yalnızca ~4 kat sıkışmış girdap fazıdır — monizm burada nicelleşir.

### Sayısal Çapraz Kontroller
- **Pürüz oranı:** Dünya'nın toplam basınç çukuru $\Delta P \approx 0{,}83\times10^{25}$ Pa (M-7), $P_0$'ın yanında $\Delta P/P_0 \sim 10^{-9}$'luk bir pürüzdür — gözlenen saat kaymalarının $10^{-9}$–$10^{-10}$ mertebesiyle birebir aynı orandır ✓.
- **Alt sınır tutarlılığı:** Sabitlenen değer, M-7'nin muhafazakâr tabanının sekiz–dokuz mertebe üzerindedir ($6{,}1\times10^{33}/1{,}6\times10^{25}\approx3{,}8\times10^{8}$); yırtılmama koşulu kohezyondan bağımsız olarak devasa marjla sağlanır ✓.

### Geçerlilik Sınırı
- $k$ eşlik oranı teoride henüz taahhüt edilmemiştir; sonuç bu nedenle yalnızca $O(1)$ düzeyinde belirsizdir (aralık yazımının nedeni budur). $P_0$ daima tam biçimiyle $\frac{1-k}{4}\rho_n c^2$ yazılır; $\approx \tfrac14\rho_n c^2$ kısaltması yalnızca "(k=0 özel hâli)" notuyla kullanılabilir.
- Türetim zayıf-alan (yüzey) genliğiyle yapılmıştır; güçlü sıkışma rejiminde ($k\to1$) doğrusal eşlik parametrelemesi geçerliliğini yitirir.

### Açık Uçlar
- **Kalibrasyon kaynağı notu (M-42):** $P_0$ artık kütleçekimsel kızıla kaymadan değil, **ışık bükülmesinden** ($1{,}751''$) sabitlenir — 2 çarpanını veren gözlem odur. Kızıla kayma bu zincirde serbest kalır ve **öngörü** konumuna geçer ($\delta f/f = -\Phi/c^2$); dolayısıyla GPS/Pound–Rebka artık girdi değil, bağımsız doğrulamadır. Ayrıntı ve muhasebe: **M-42**.
- $k$'nın SN 1987A gecikme bütçesiyle (2.4.4) bağımsız çapraz kontrolü (Ek C satır 3; 7.4).
- Bağımsızlık notu: $G$'nin türetimi (M-28) yalnızca gradyan bağlaşımına ($\alpha$) dayanır ve $P_0$'ın mutlak değerinden bağımsızdır — bu sabitleme onu etkilemez; iki zincirin ayrıklığının açıkça belgelenmesi.

---

## M-9 · Ortamın Ağırlıksızlığı Teoremi · **[T]**

**Kullanıldığı bölümler:** Ek B.4, 1.3 Postülat kutuları (Postülat 1'in "ağırlıksız ortam" ifadesinin kanıt statüsü), 7.4 md.10.

### Varsayımlar
1. Teoride çekim diye bağımsız bir kuvvet yoktur; tek alan basınçtır, tek kuvvet $-\nabla P$'dir (Postülat 6, M-2). Standart fiziğin Poisson denklemi $\nabla^2\Phi = 4\pi G\rho_{toplam}$ — yani kütle yoğunluğunun kendiliğinden çekim alanı kaynakladığı önermesi — teorinin **reddettiği gizli varsayımdır**: ortam "ağırlıklı" değildir.
2. Kavrama Yasası (M-1) ve arka plan sabitlemesi (M-8) geçerlidir.
3. Kavitasyon eşiği (M-4): $v_{kav} = \sqrt{2}\,c\,\sqrt{1+\Sigma/P_0} \gg c$.

### Adımlar
1. **Ağırlıksızlık.** Ağırlık, kütlenin değil gradyanın — yani deplasmanın — özelliğidir (M-2: kuvvet $-\gamma_N\nabla P$'dir, $\rho$'nun değil). Homojen arka plan basınç alanının sıfır noktasıdır (datum): $\nabla P_0 = 0$ olduğundan hiçbir parçası kuvvet hissetmez; ortam kendi üzerine çökmez. Arşimet analojisi: kaldırma kuvveti nasıl mutlak yoğunluğun değil yoğunluk *farkının* olayıysa, Evrenakı ağırlığı da mutlak $\rho_0$'ın değil deplasman *açığının* olayıdır. $10^{16}$–$10^{17}$ kg/m³'lük ortamın "neden tartılmadığı" sorusu, 1. varsayımdaki reddedilen Poisson önermesini gizlice geri sokar.

   **Kozmolojik biçimi (aynı sorunun büyük ölçekte tekrarı).** Aynı itiraz kozmolojide daha keskin görünür: $\rho_0 \approx 6{,}8\times10^{16}$ kg/m³, kritik yoğunluğun ($\rho_{kritik}\approx9\times10^{-27}$ kg/m³) yaklaşık **43 mertebe** üstündedir; standart çerçevede böyle bir ortam evreni anında kapatırdı. Cevap aynı tek satırdır ve yeni varsayım gerektirmez: $\Omega$ parametreleri ve kritik yoğunluk, *doğrudan tartılmış* büyüklükler değildir — genişleme hızı, yapı oluşumu ve CMB akustik fiziğinden **Friedmann/Poisson kaynaklanması varsayılarak** çıkarılan büyüklüklerdir. Teori tam olarak o kaynaklanmayı reddettiği için $\rho_0$ bu çıkarımlara hiç girmez. Bu gözlemlerin kısıtladığı şey ortamın mutlak yoğunluğu değil, **deplasman envanteridir** (girdap/madde bütçesi ve onun gradyan alanı). Arşimet analojisinin kozmolojik karşılığı: okyanusun kendi yoğunluğu değil, içindeki cisimlerin açtığı hacim tartılır.

   Bu, gözlemsel yükü ortadan kaldırmaz, **yerini değiştirir:** açık olan şey $\rho_0$'ın büyüklüğü değil, CMB akustik pik oranlarının ve ilksel bolluk oranlarının teorinin kendi deplasman büyüklüklerinden nicel üretilmesidir (Bölüm 3.7.4 mekanizma düzeyinde kurar; nicel program 7.4'te kayıtlıdır).
2. **Kararlılık (Jeans'in iki bacağının da yokluğu).** Klasik öz-kütleçekimli akışkanda homojen durum kararsızdır (Jeans, 1902): yoğunlaşan bölge daha çok çeker, çöküş büyür. Evrenakı'da bu geri-beslemenin iki bacağı da yoktur: (i) yoğunlaşan bölge kimseyi çekmez, yalnızca basıncını yükseltir; (ii) sıkıştırılabilirlik pozitif olduğundan her yoğunluk pürüzü basınç dalgası olarak dağılır. İkinci bacak nicel olarak da kapalıdır. Dalga, deplasman alanı donmuşken ilerler ve o kanalda hâl denklemi Kavrama Yasası'nın kendisidir (**Ek M-44**), $P=c^2\rho$:
$$\left(\frac{\partial P}{\partial\rho}\right)_{\chi} = c^2 \;>\; 0 \qquad\Longrightarrow\qquad c_{pürüz}=c$$
Yani her yoğunluk pürüzü **tam $c$ hızında** yayılan bir basınç dalgası olarak dağılır. Sıkıştırılabilirlik her koşulda pozitif olduğundan kararsızlık penceresi hiçbir rejimde açılmaz; homojen durum yalnızca izinli değil, ortamın **tek doğal taban durumudur.**

Bu, ortamın **stiff (Zel'dovich) akışkan** olması demektir — ses hızının ışık hızına tam eşit olduğu, nedensel olarak en katı hâl. Gözlemsel karşılığı doğrudandır: GW170817'nin kütleçekim dalgası ↔ ışık eşitliği ($10^{-15}$ hassasiyet) bu kanalı bağlar ve **otomatik olarak sağlanır**.

> *Düzeltme kaydı (29 Temmuz 2026): bu adımın bir ara sürümü dağılma hızını $c/\sqrt k$ yazıyordu. O yazım, Ek B.3'ün **deplasman** bağıntısını bir hâl denklemi sanan bir türetime dayanıyordu ve GW170817 ile 6,5 mertebe çelişiyordu. Ek M-44 iki kanalı ayırınca ($\chi$ sabit ↔ $\rho$ sabit) sıkışma hızının **tam $c$** olduğu görüldü — yani bu girdinin özgün metni doğruydu.*

Postülat 4 ile çelişki yoktur: $c$ Zerre'nin çizgisel öteleme sınırıdır ve sıkışma kanalı da tam orada durur; ortamın $c$'yi **aşan** kanalı ayrıdır ve kohezyon kanalıdır ($v_m=c\sqrt{\Sigma/P_0}$, M-5).
3. **Vakum kararlılığı (kendiliğinden madde doğumu yok).** Arka planın "kaynayıp" kendiliğinden girdap-madde üretmesi için yerel akışın $v_{kav} = \sqrt{2}\,c\,\sqrt{1+\Sigma/P_0}$ eşiğine ulaşması gerekir (M-4); $\Sigma \gg P_0$ kohezyonlu süper-akışkanda rastgele dalgalanmalar bu eşiğe ulaşamaz. Uzayın durup dururken maddeye dönüşmemesi aynı çerçevenin bedava sonucudur.

### Sonuç
$$\boxed{\nabla P_0 = 0 \;\Rightarrow\; \text{homojen arka plan kuvvetsiz, kararlı ve doğurgan-değildir:}\quad \text{ortam ağırlıksızdır — tanım değil, teorem.}}$$

### Geçerlilik Sınırı
- Teorem homojen arka plan içindir. Kütle *çevresindeki* gradyan bölgesinde ortam tepkisiz değildir — Euler denklemi gereği gradyana cevap verir; ama cevabı düşmek değil **dolaşmaktır**: gradyan, dolaşımın merkezcil ivmesiyle siklostrofik dengede taşınır,
$$\frac{\nabla P}{\rho_0} = \frac{v_\theta^2}{r}$$
(Postülat 7–8'in sürüklenme ve vorteks alanları). Katı deplasman cebi (nükleon) ise akıp dengelenemez; bütün hâlde itilir. **Madde düşer, ortam dolaşır.**
- 2. adımın dalga-dağılma bacağı, $dP/d\rho = c^2/k$ türetimi sayesinde **$k$'nın izinli tüm aralığında ve her sıkışma genliğinde** geçerlidir; ayrı bir "güçlü sıkışma rejimi" çekincesi gerekmez. *(Düzeltme kaydı, 28 Temmuz 2026: bu satırın önceki sürümü kanıtı $k\ll1$ ile sınırlıyordu. Sınırlama, M-1'in uzlaştırma notundaki $k$ etiketi karışıklığından doğan bir yanılgıydı — $P\propto\rho$ hâli $k=1$'e karşılık gelir, $k\ll1$'e değil. Etiket düzeltilince çekinceye gerek kalmadı.)*
- Kanıtlanan şey, **çöküşe karşı kararlılıktır** (Jeans tipi geri-besleme yok, $dP/d\rho>0$). Tam doğrusal-olmayan kararlılık — şok oluşumu, türbülans başlangıcı — ortamın hareket denklemlerinin bir eylem ilkesinden türetilmesini gerektirir; bu, teorinin bilinen ve ayrıca kayıtlı açığıdır (7.4).
- Kozmolojik biçimin cevabı (1. adım) bir **tutarlılık** sonucudur: $\rho_0$ ile kritik yoğunluk arasındaki 43 mertebelik farkın çelişki olmadığını gösterir, CMB/ilksel bolluk oranlarını üretmez.

### Açık Uçlar
- Siklostrofik denge profilinin ($v_\theta(r)$) kütle çevresi sürüklenme zarfıyla (Rampa profili, Ek C satır P2) nicel eşlenmesi.
- **Üç kanalın ortak mikro-modeli.** Ortamın üç ayrı tepki hızı vardır ve üçü ayrı katsayılardan gelir: **sıkışma** ($c_{pürüz}=c$, stiff hâl denklemi), **kohezyon/kesme** ($v_m=c\sqrt{\Sigma/P_0}>10^4c$, $\Sigma$'dan) ve **deplasman** (hız değil, $k=0$ ile tanımlı statik tepki). Sürekli ortamlar mekaniği bunlar arasında bir bağ gerektirmez — hacim ve kesme modülleri genel bir ortamda bağımsız malzeme sabitleridir ve M-5 bu bağımsızlığı açıkça varsayar. Açık olan soru: nükleonun vakum cepli girdap yapısı, üçünü birden veren tek bir mikro-model olabilir mi? Olursa $\Sigma$ de türetilmiş hale gelir ve Ek C'den bir kalem daha düşer. Bu, eylem ilkesi programına bağlıdır (7.4 md.14, Ek M-44 Açık Uçlar).
