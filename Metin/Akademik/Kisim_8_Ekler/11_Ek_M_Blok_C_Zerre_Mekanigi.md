# Ek M — Merkezî Türetim Kataloğu · Blok C: Zerre Mekaniği (Mikro Evren)

Şablon ve rozet sistemi için bkz. Blok A (M-1..M-6) girişi.

---

## M-10 · Fotoelektrik Enerji Muhasebesi · **[S]**

**Kullanıldığı bölümler:** 2.2.2–2.2.3, 2.4.2 (Yön Kuralı kutusundaki $(c_0^2+k_a v_{cev}^2)$ atfı), Postülat 4 (1.3), 2.6.5, 7.4.

### Varsayımlar
1. Işık, kütleli Zerrelerin ($m_z$, Postülat 4) katarlarından oluşur; fotoelektrik olay soyut enerji emilimi değil, ardışık kinetik darbelerin birikimidir (2.2.2).
2. **Şiddet–frekans ayrımı (D-21):** frekans $\nu$, tek bir katarın *içindeki* ardışık Zerre vuruş ritmidir; şiddet, birim alana düşen *katar sayısıdır*. Tek elektron tek katarla etkileşir; dolayısıyla birikim yalnızca $\nu$ ile ölçeklenir, şiddetten bağımsızdır.
3. Zerre–elektron çarpışması elastik kinematiğe tabidir; elektron, Zerre'den çok daha ağır bir hedeftir ($m_z \ll m_e$).
4. Her Zerre, öteleme enerjisine ek olarak evrensel çevresel hızı $v_{cev}$ ile dönme enerjisi taşır. Bu hız Ek A.2'nin duvar hızıdır ve boyuttan bağımsızdır: $v_{cev} = \sqrt{2}\,c_0 = 4{,}24\times10^8$ m/s (M-3). Atalet katsayısı $k_a$'dır; Zerre kusursuz küre değil, kendi dönüşüyle basık (eksenel simetrik) bir gövde olduğundan $k_a = 1/2$'dir.*

*\*Notasyon notu (Ek D · S-1): atalet katsayısı gövde metninde (2.2.2) $k$ olarak geçer; $k$ sembolü kitap genelinde ρ–P eşlik oranına ayrıldığından katalogda **$k_a$** kullanılır.*

### Adımlar
1. **Tek-vuruş aktarım kesri $\eta$ (standart elastik kinematik):** Kütlesi $m$ olan bir mermi, duran kütlesi $M$ olan bir hedefe kafa kafaya elastik çarptığında, momentum ve enerji korunumundan hedefin aldığı enerji kesri
$$\frac{\Delta E}{E} = \frac{4\,mM}{(m+M)^2}$$
olur. $m \ll M$ limitinde payda $M^2$'ye gider ve kesir $\approx 4m/M$'ye sadeleşir. $m = m_z$, $M = m_e$ ikamesiyle:
$$\eta \approx \frac{4\,m_z}{m_e} = \frac{4 \times 1{,}47\times10^{-35}}{9{,}11\times10^{-31}} \approx 6{,}5\times10^{-5}$$
Bu, kafa kafaya (maksimum) aktarımın kesridir; eğik vuruşlar daha azını aktarır. Pinpon topunun bovling topuna çarpması gibi: mermi enerjisinin neredeyse tamamıyla geri seker. Elektronun tek vuruşla değil, **ardışık rezonansla** (2.2.3) kopmasının mekanik zorunluluğu budur.
2. **Tek Zerre'nin taşıdığı enerji:** öteleme + dönme:
$$E_{Zerre} = \tfrac12 m_z c_0^2 + \tfrac12 k_a\, m_z v_{cev}^2 = \tfrac12 m_z\left(c_0^2 + k_a\, v_{cev}^2\right) \;\overset{k_a=1/2,\;v_{cev}=\sqrt{2}\,c_0}{=}\; m_z c_0^2 \approx 8{,}25\ \text{eV}$$
$k_a = 1/2$ ve $v_{cev} = \sqrt{2}\,c_0$ konduğunda $k_a v_{cev}^2 = c_0^2$ olur; dönme payı öteleme payına **tam eşit** çıkar (öteleme $4{,}12$ eV + dönme $4{,}12$ eV). Dönme terimi bu muhasebede ihmal edilmez.
3. **Muhasebe:** Yüzey bağlanma enerjisi $\Phi$ ile sökülen elektronun kinetik enerjisi $E_{ke}$, rezonans penceresi boyunca peş peşe çarpan $N$ Zerre'nin her vuruşta aktarabildiği payların toplamıdır.

### Sonuç
$$\boxed{\Phi + E_{ke} = N \cdot \eta \cdot \tfrac{1}{2} m_z \left(c_0^2 + k_a\, v_{cev}^2\right)\,, \qquad \eta \approx \frac{4\,m_z}{m_e} \approx 6{,}5\times10^{-5}}$$

**Sayısal zincir:** $E_{Zerre} = \tfrac12 m_z\left(c_0^2 + k_a v_{cev}^2\right) = m_z c_0^2 \approx 8{,}25$ eV (tek Zerre'nin taşıdığı toplam enerji: öteleme $4{,}12$ eV + dönme $4{,}12$ eV) → tek vuruşta aktarılan pay $\delta = \eta \cdot E_{Zerre} \approx 5{,}4\times10^{-4}$ eV → tipik sökme işi ($\Phi + E_{ke} \approx 4$ eV) için $N \approx 7{,}5\times10^3$ vuruş → morötesi eşik ritminde ($\nu \approx 9{,}7\times10^{14}$ Hz) birikim süresi $N/\nu \approx 7{,}7\times10^{-12}$ s, yani **birkaç pikosaniye** — ölçülen nanosaniye-altı "gecikmesiz" emisyonla (Lawrence & Beams, 1927) uyumlu.

### Geçerlilik Sınırı
- Rozet **[S]**: $m_z$ değeri ilk-ilkelerden türetilmemiştir ve türetilmesi beklenmez — $m_z$, teorinin **ölçülen girdi parametresidir** (Standart Model'de $m_e$ nasıl girdiyse öyle). Fotoelektrik veri ($\Phi$, $E_{ke}$, $\nu$) ile Postülat 4'ün evrensel $m_z$ değerinin tutarlılığı, bu girdinin **ölçek denetimidir**. $N$, girdi verildiğinde bu veriyle belirlenir.
- **Ölçek denetimi — açıkça:** Yukarıdaki kutulu denklem $\eta = 4m_z/m_e$ yerine konduğunda
  $$\Phi + E_{ke} = \frac{2N m_z^2}{m_e}\left(c_0^2 + k_a\, v_{cev}^2\right) = \frac{4N m_z^2 c_0^2}{m_e}$$
  hâlini alır ($k_a = 1/2$ ve $v_{cev} = \sqrt{2}\,c_0$ konduğunda $c_0^2 + k_a v_{cev}^2 = 2c^2$): **bir denklem, iki bilinmeyen** ($N$, $m_z$). $m_z$ ölçülen girdi olarak verildiğinde denklem $N$'yi belirler. Çizelgedeki $m_z \approx 1{,}47\times10^{-35}$ kg değerinin ölçek denetimi, sayısal zincirin ilk halkasında duran şu eşleşmedir:
  $$\tfrac12 m_z c_0^2 \;\simeq\; \Phi \;\approx\; 4\ \text{eV}\,, \qquad E_{Zerre} = m_z c_0^2 \;\simeq\; 2\Phi \;\approx\; 8{,}25\ \text{eV}$$
  Yani tek Zerre'nin **öteleme payı**, tipik metal iş fonksiyonu ölçeğine oturur; dönme payı buna tam eşit olduğundan Zerre'nin taşıdığı toplam enerji iş fonksiyonunun iki katı mertebesindedir. Ters çözüm, çapanın kendisiyle ($\simeq4$ eV) $m_z \approx 1{,}43\times10^{-35}$ kg verir — çizelge değerinden ~%3 sapma, çapanın genişliği içinde. Bu bir *ölçek denetimidir*, bağımsız bir tayin değil: iş fonksiyonları malzemeye göre ~2–5 eV arasında değişir, dolayısıyla denetim $m_z$'ye kendiliğinden $\sim\pm25\%$ genişlik bırakır. Bu genişlik çapanın genişliğidir; $m_z$'nin statüsünü — ölçülen girdi parametresi — değiştirmez.
- **Bağın yönü — dürüstlük kaydı.** Muhasebede $N=\nu\tau$ konulduğunda standart $h\nu$ ile eşleşme $h \leftrightarrow 4\tau m_z^2 c_0^2/m_e$ verir. Ancak yukarıdaki birikim hesabı bundan **bağımsız değildir**: $N=(\Phi+E_{ke})/\delta = h\nu/\delta$ olduğundan $N/\nu \equiv h/\delta \equiv \tau$ çıkar. Yani iki yol cebirsel olarak tek bağıntıdır ve ikisinin de $7{,}7$ ps vermesi bir sağlama değil, bir özdeşliktir. **Bu ek $h$'ın sayısal değerini üretmez;** yaptığı şey $h$'ı iki mekanik büyüklüğe ($\delta$, $\tau$) **ayrıştırmaktır**. Ayrıştırma boş değildir — $\delta$ artık $m_z$'den tam hesaplanır — ama sayısal bir öngörü olarak sunulamaz. $\tau$'nun $h$'ı kullanmayan bağımsız tayini açık kalemdir. *(Ek C parametre çizelgesinin 1. satırı bu bağı ters yönde okuyup "Planck sabitinden türetim" yazıyordu; 30 Temmuz 2026'da düzeltildi.)*
- $\eta$, kafa kafaya elastik çarpışmanın üst sınırıdır; gerçek vuruş geometrisi dağılımı $N$'yi yukarı esnetebilir (mertebe değişmez).
- Elektron burada standart kinematik hedef olarak alınmıştır; girdap iç yapısının (2.1) aktarım verimine düzeltmesi ihmal edilmiştir.

### Açık Uçlar
- Vuruş geometrisi dağılımının (eğik çarpışmalar) $\eta$ üzerinden $N$'ye etkisinin nicelleştirilmesi.

---

## M-11 · Frekans Doğrusallığı ve $h = \delta\tau$ Özdeşliği · **[S]**

**Kullanıldığı bölümler:** 2.2.3, 2.6.5 (Zerre Paketi), 2.10.1, 7.2, 7.4, Ek C.

### Varsayımlar
1. M-10'un enerji muhasebesi geçerlidir; tek-vuruş aktarımı sabittir.
2. Elektron girdabının evrensel bir **kopma penceresi** ($\tau$) vardır: sökülme kararını, bu pencere boyunca biriken enerji belirler (2.2.3).
3. Vuruş ritmi katar-içi frekans $\nu$'dür; pencere boyunca gelen vuruş sayısı bu ritimle orantılıdır. (Şiddet, paralel katar sayısını sayar ve tek elektronun muhasebesine girmez — M-10, Varsayım 2.)

### Adımlar
1. **Tek-vuruş aktarımı** tek sembole toplanır:
$$\delta = \eta \cdot \tfrac{1}{2} m_z \left(c_0^2 + k_a\, v_{cev}^2\right)$$
2. Kopma penceresi boyunca gelen vuruş sayısı:
$$N = \nu\,\tau$$
3. Pencere boyunca biriken enerji:
$$E_{biriken} = \delta \cdot N = \delta \cdot \nu\tau = (\delta\tau)\,\nu$$
4. Bağlanma enerjisi düşüldüğünde sökülen elektronun kinetik enerjisi $\nu$ ile **doğrusaldır**:
$$E_{ke} = (\delta\tau)\,\nu - \Phi$$
5. **Gözlemle özdeşleme:** Millikan'ın doğruladığı fotoelektrik doğrunun eğimi Planck sabitidir (Planck, 1901; Millikan, 1916); eğimlerin eşitlenmesi $h$'ye mekanik bir ontoloji verir:
$$h = \delta\tau$$
6. **Paket ölçeği (2.6.5):** Kaynağın kopma penceresi boyunca ateşlediği wake-kilitli katar dilimi $N = \nu\tau$ mermilik Zerre Paketi'dir; toplam etkin enerjisi
$$E_{paket} = \delta \cdot N = (\delta\tau)\,\nu = h\nu$$
Standart fiziğin tek "foton" sözcüğü teoride iki gerçekliğe ayrışır: **uçuş birimi** bu dilimdir (Zerre Paketi — nesne adı değil, $\varphi$'si ortak katar diliminin kısaltması), **ölçüm birimi** ise alıcı penceresinin ısırığıdır. Paket **yayım birimidir** (kaynak penceresinin ürünü), **teslim kuantumu değildir**: dedektör merdiveninin ($N_p \cdot h\nu$; $N_p$: soğurma olayı sayısı) adresi alıcı penceresidir — her soğurma olayı $(\delta\tau)\nu$'lük bir pencere alışverişidir; kaynak ve alıcı pencereleri aynı evrensel $\tau$'yu taşıdığından iki uç aynı $h\nu$'de buluşur. *(Düzeltme kaydı, 8 Ağustos 2026: erken yazım "enerji yalnızca tam paket kuantumlarıyla teslim edilir" diyordu; kesikliliği ışığın kendisine geri yazdığı — "foton"u paket adıyla ihya ettiği — için terk edildi. Kesikliliğin adresi alıcıdır; bkz. 9.2.1, 9.4.3.)*
7. **Türetilmiş sabit:** Açısal biçimlerde kullanılan indirgenmiş sabit, tanım gereği
$$\hbar = \frac{h}{2\pi} = \frac{\delta\tau}{2\pi}$$
olarak kaydedilir (örn. $\sigma_x\sigma_p \geq \hbar/2$, 2.10.2).

### Sonuç
$$\boxed{E_{ke} = (\delta\tau)\,\nu - \Phi\,, \qquad h = \delta\tau\,, \qquad E_{paket} = h\nu\,, \qquad \hbar = \frac{h}{2\pi}}$$

Planck sabiti temel bir doğa gizemi değil, iki mekanik büyüklüğün — tek-vuruş aktarımı ile kopma penceresinin — çarpımıdır.

### Geçerlilik Sınırı
- Rozet **[S]**: gözlemle özdeşlenen şey **çarpım** $(\delta\tau)$'dur; bileşenler ise artık serbest değildir. $\delta$, M-10'un muhasebesinden kapalı biçimde çıkar ($\delta = \eta\,E_{Zerre} = 4m_z^2c^2/m_e \approx 5{,}4\times10^{-4}$ eV), kopma penceresi de ondan okunur ($\tau = h/\delta \approx 7{,}8$ ps). Dolayısıyla $h$'nin ölçülmüş değeri iki bilinmeyeni birden değil, yalnız $\tau$'yu bağlar.
- Doğrusallık, kopma penceresinin $\nu$'den bağımsız (evrensel) olduğu varsayımına dayanır; $\tau$'nun malzemeye veya frekansa zayıf bağımlılığı doğrudan sınanabilir bir sapma üretir.

### Açık Uçlar
- $\delta$ ve $\tau$'nun bağımsız **deneysel** ölçümü: ikisi de artık türetilmiş olduğundan bu ölçümler kalibrasyon değil, teorinin sınavıdır (7.4).
- 2.6.5'in 50/50 istatistiği, paket varış fazı $\varphi$'nin düzgün dağılımlı olduğu varsayımına dayanır; bu dağılımın kaynak mekaniğinden türetimi açıktır.

---

## M-12 · Zerre Boyutları: $V_z$, $r_z$ · **[T]**

**Kullanıldığı bölümler:** 2.2.2, Postülat 4 (1.3), Ek D (R-6 sabit tablosu), 7.2.

### Varsayımlar
1. Zerre, atom çekirdeğiyle (nükleon) aynı aşırı sıkışmış girdap fazındadır; öz yoğunluğu nükleon öz yoğunluğuna eşittir: $\rho_n = 2{,}7\times10^{17}$ kg/m³ (Postülat 4; S-18 gereği tercih edilen sembol $\rho_n$'dir).
2. Zerre kütlesi evrenseldir: $m_z = 1{,}47\times10^{-35}$ kg (Postülat 4).
3. Zerre kusursuz küre değildir; kendi dönüşüyle basık (eksenel simetrik) bir gövdedir. Hacim, yoğunluk tanımından gelir ve geometriden bağımsızdır; küre idealizasyonu yalnızca hacimden **eşdeğer (ortalama) yarıçap** okumak için kullanılır.

### Adımlar
1. Hacim, Newtonyen tanımdan:
$$V_z = \frac{m_z}{\rho_n} = \frac{1{,}47\times10^{-35}}{2{,}7\times10^{17}} \approx 5{,}44\times10^{-53} \text{ m}^3$$
2. Eşdeğer küre yarıçapı, hacim formülünün tersinden:
$$r_z = \left(\frac{3V_z}{4\pi}\right)^{1/3} \approx 2{,}35\times10^{-18} \text{ m}$$
Buradaki $r_z$, gövdenin ekvator ya da kutup yarıçapı değil, **eşdeğer hacimli kürenin (ortalama) yarıçapıdır**; $V_z$ ise $m_z/\rho_n$'den geldiği için geometriden bağımsızdır.

### Sonuç
$$\boxed{V_z = \frac{m_z}{\rho_n} \approx 5{,}44\times10^{-53} \text{ m}^3\,, \qquad r_z \approx 2{,}35\times10^{-18} \text{ m}}$$

Işık, kütlesiz bir dalga değil; ölçülebilir atalete ve nükleer öz yoğunluğa sahip bir akışkan mermisidir.

### Sayısal Çapraz Kontrol
- **Klasik elektron yarıçapı** $r_e^{(kl)} \approx 2{,}8\times10^{-15}$ m (Tiesinga ve ark., 2021) ile kıyas: $r_z/r_e^{(kl)} \approx 8\times10^{-4}$ — yarıçapça yaklaşık **binde bir**. *(Sembol notu: üst-imli yazım, M-3′'ün $e$-katlanma yarıçapı $r_e$'siyle çakışmayı önlemek içindir.)* (Kıyasın hangi yarıçapla yapıldığı zorunlu olarak belirtilir: Evrenakı Teorisi'nde elektron noktasal değil, geniş hacim süpüren bir girdaptır; bkz. 2.1.)
- **Saçılma üst sınırı:** elektronun nokta-parçacık üst sınırı $\sim 10^{-18}$ m'dir (Bourilkov, 2001); $r_z \approx 2{,}35\times10^{-18}$ m bu ölçekle aynı mertebededir — Zerre boyutu, mevcut saçılma çözünürlüğünün hemen altında/civarında kalır.

### Geçerlilik Sınırı
Sonuç, iki Postülat 4 girdisinin ($m_z$, $\rho_n$) aritmetik sonucudur; rozet **[T]** bu türetimin kendi içindeki zorunluluğunu işaretler, girdilerin statüsünü ($m_z$: teorinin ölçülen girdi parametresi, bkz. M-10) devralmaz. $V_z$ geometriden bağımsızdır; $r_z$ ise eşdeğer küre yarıçapı olduğundan gövdenin basıklığı ekvator ve kutup yarıçaplarına $O(1)$ ayrışma getirir.

### Açık Uçlar
- Basık gövdenin ekvator/kutup yarıçapı ayrışmasının, eşdeğer $r_z$ etrafındaki $O(1)$ genişliğinin nicelleştirilmesi.
- $r_z$ ölçeğinin doğrudan deneysel imzası (saçılma veya kırınım kanalında).

---

## M-13 · SN 1987A Yol-İçi Yavaşlama Üst Sınırı · **[S]**

**Kullanıldığı bölümler:** 2.4.4, 2.4.2 (Yön Kuralı), 4.3 (dispersiyon/renk imzası), Ek C satır 3 ($k$ eşlik oranının bağımsız ölçüm programı), 7.4.

### Varsayımlar
1. Işığın patinajı, Evrenakı'nın $P/\rho$ oranının düştüğü bölgelerin olayıdır ($c_0 = \sqrt{P/\rho}$, M-1); nötrino tutunma mekanizmasına bağımlı değildir ve oyalanmadan geçer (2.1, 2.4.4).
2. SN 1987A gözlem girdileri: uzaklık ≈ 168.000 ışık yılı (Büyük Macellan Bulutu); nötrino–optik varış farkı ≈ 3 saat (Hirata ve ark., 1987; Bionta ve ark., 1987; Alekseev ve ark., 1988).
3. Gecikme iki bileşenin toplamıdır (gecikme bütçesi):
$$D_{toplam} = D_{zarf} + D_{yol}$$
$D_{zarf}$: yıldız zarfı içindeki madde-içi patinaj (standart fiziğin "şok çıkışı gecikmesi" dediği sürecin teorideki karşılığı); $D_{yol}$: güzergâhtaki zayıf ama birikimli galaktik gradyanların yol-içi patinaj payı.

### Adımlar
1. Toplam yol süresi saate çevrilir:
$$T_{yol} = 168.000 \text{ yıl} \approx 1{,}5\times10^{9} \text{ saat}$$
2. En muhafazakâr atama yapılır: 3 saatlik farkın **tamamı** yol-içi yavaşlamaya yazılsa bile,
$$\frac{\Delta v}{c} \lesssim \frac{D_{toplam}}{T_{yol}} = \frac{3}{1{,}5\times10^{9}} = 2\times10^{-9}$$
3. Gerçekte $D_{zarf} > 0$ olduğundan (SN 2008D X-ışını parlaması, SN 2016gkg çıkış yükselişi bu bileşeni bağımsız kanaldan gözler), yol payı bu sınırın da altındadır; Crab pulsarının milisaniyelik nabızlarında renkler arası varış saçılmasının yokluğu $D_{yol}$'u ayrıca küçük bir kesirle sınırlar (2.4.4).

### Sonuç
$$\boxed{\left.\frac{\Delta v}{c}\right|_{yol} \lesssim 2\times10^{-9} \qquad \text{(yol-içi ortalama yavaşlama üst sınırı)}}$$

### Geçerlilik Sınırı
- Rozet **[S]**: sınır tek bir gözlem olayından (SN 1987A) çıkarılmıştır ve **yol-içi ORTALAMA** yavaşlamayı bağlar; yerel/geçici patinaj epizodlarını tek tek bağlamaz.
- Bütçenin iki bileşeni ($D_{zarf}$, $D_{yol}$) bu veriden **tek başına ayrıştırılamaz**; üst sınır, tamamının yola yazıldığı muhafazakâr durumdur.
- Güzergâh, gerçek galaksiler-arası boşluğu neredeyse hiç içermez (BMB, Samanyolu'nun ~50 kpc'deki uydusudur); sınır, derin uzayın tam-tutunma bölgesi için ayrı bir ölçüm değildir.

### Açık Uçlar
- Gecikme bütçesinin ayrıştırılması: bir sonraki galaktik süpernovada gecikmenin progenitör tipiyle mi (→ $D_{zarf}$) yoksa güzergâh uzunluğuyla mı (→ $D_{yol}$) ölçeklendiğinin tespiti; farklı uzaklıklardaki nötrinolu süpernovalarla gecikme–mesafe ilişkisi (2.4.4).
- $\chi$ ölçekli renk-saçılması imzası: $D_{yol}$ ne kadarsa varışta o kadar mavi–kırmızı ayrışması olmalıdır (4.3); pulsar nabız hizalamaları bu imzayı bugünden sınırlar, gelecekteki hassas ölçümler yol payını doğrudan ölçebilir.

---

## M-14 · Bell Programı: $v_m$ Alt Sınırından $\Sigma$'ya · **[A]**

**Kullanıldığı bölümler:** 2.10.1, 2.9.2.1 (Malus geçit mekaniği), Ek A.3, Ek B.4 (arka plan kararlılığı), M-4, M-5, 6.0, 7.4, 7.5.

### Varsayımlar
1. M-5'in sonucu: kohezyon kanalının elastik sinyal hızı $v_m = \sqrt{\Sigma/\rho_0} = c_0\sqrt{\Sigma/P_0}$; bu kanal enerji/madde taşımaz, ortam topografyasının (gradyan deseninin) ayar sinyalidir.
2. Dolanıklık korelasyonları, iki kanadı birden kapsayan **önceden şekillenmiş basınç topografyasının** paket-çifti geçitlemesidir (2.10.1, Katman 2); topografya kurulumu kohezyon kanalıyla yayılır.
3. Bell-tipi "etki hızı" deneyleri, kanatlar arası koordinasyon hızına gözlemsel alt sınır koyar: $v > 10^4\,c_0$ (Salart ve ark., 2008).

### Adımlar
1. Gözlemsel alt sınır doğrudan $v_m$'ye atanır ve M-5 bağıntısıyla $\Sigma$'ya çevrilir:
$$\frac{v_m}{c} > 10^4 \;\Longrightarrow\; \frac{\Sigma}{P_0} = \left(\frac{v_m}{c}\right)^2 > 10^8$$
(Sık karışan nokta: $10^4$ hız oranıdır; $10^8$ onun karesidir.)
2. Aynı sınır, madde-doğum eşiğini aşağıdan destekler (M-4, M-6): $\Sigma \gg P_0$ limitinde
$$v_{kav} \approx \sqrt{2}\,v_m > 1{,}4\times10^4\,c_0$$
3. **Kalibrasyon yolu:** korelasyon bozulması bir gün ölçülür ve $v_m$ sonlu bir değerde yakalanırsa, kohezyon dayanımı pascal cinsinden sabitlenir:
$$\Sigma = P_0\left(\frac{v_m}{c}\right)^2$$
Ölçülmedikçe her yeni deney alt sınırı yükseltir — iki sonuç da bilgi vericidir: dolanıklık, madde doğumu ve arka plan kararlılığı (Ek B.4) tek $\Sigma$ üzerinde kenetlenir.

### Sonuç
$$\boxed{\frac{\Sigma}{P_0} = \left(\frac{v_m}{c}\right)^2 > 10^8\,, \qquad v_{kav} \approx \sqrt{2}\,v_m > 1{,}4\times10^4\,c_0\,, \qquad \Sigma = P_0\left(\frac{v_m}{c}\right)^2}$$

**Yanlışlanabilir öngörü:** $v_m$ sonludur; baz uzunluğu $L$ ve ayar-anahtarlama süresi $t$ için $L > v_m \cdot t$ rejimine ulaşan bir deneyde topografya yetişemez ve CHSH istatistiği $S \leq 2$'ye **düşmelidir** — kuantum mekaniği bozulma öngörmez; ayrışma noktası budur.

### Geçerlilik Sınırı
- Rozet **[A]**: $\Sigma/P_0$ yalnızca **alttan** sınırlıdır; tam değeri serbesttir (Ek C satır 9). Bell laboratuvarları burada çürütme değil, ortam kohezyonunun ölçüm programıdır.
- **GW170817 notu:** kütleçekim dalgası* hızının $10^{-15}$ hassasiyetle $c_0$'ye eşitlenmesi (Abbott ve ark., 2017) **sıkışma kanalını** bağlar; kohezyon kanalını bağlamaz. Teoride "kütleçekim dalgası" denen basınç salınımları basınç kanalının olayıdır ve $c_0$ ile yayılır; kütle-itim alanının statik topografya kurulumu ise kohezyon kanalını kullanır — iki-kanal ayrımının beklediği tablo tam budur (2.10.1).
- Kanatlar arasında hiçbir *sinyal* yolculuk etmez; $\varphi$ fazları yerel ve kontrolsüz kaldığından geçit mesaj göndermekte kullanılamaz — sinyalsizlik korunur.

*\*"Kütleçekim dalgası" burada standart fiziğin gözlem adı olarak aktarılmaktadır; teorinin kendi dilinde olgu, kütle-itim alanındaki basınç salınımıdır.*

### Açık Uçlar
- $\cos^2(a-b)$ korelasyon yapısının topografya/geçit mekaniğinden **nicel** türetimi; nitel mekanizma kurulmuştur (2.9.2.1: Malus geçidinde geçirgenlik = hız bileşeni $\cos\theta$ × sağ geçen katar kesri $\cos\theta$), nicelleştirilmesi 7.4'ün açık işidir.
- Kohezyon-kanalı özdeşleştirmesinin mekanizma-önerisi statüsünden çıkarılması: $L > v_m t$ rejimine ulaşan deney tasarımı (7.5).
