# Ek M — Merkezî Türetim Kataloğu · Blok D: Optik ve Fizeau Ailesi

> Şablon ve rozet sistemi için bkz. Blok A (M-1..M-6) girişi.
>
> **Blokun kapsamı:** Işığın (Zerre'nin) madde içindeki davranışının dört türetimi: kırılma indisinin ilk-ilke türetimi (M-15), Fizeau sürükleme katsayısı (M-16), dispersiyon (Lorentz) düzeltmesi (M-17) ve interferometre faz duyarlılığı ile asimetrik kol tasarımının gerekçesi (M-18). Dördü de tek bir mekanik resimden — sürüklenme zarfının molekül ölçeğindeki hâlinden (Postülat 7) ve Kavrama Yasası $c_{loc}=\sqrt{P/\rho}$'dan (M-1) — beslenir.
>
> **Notasyon uyarısı (S-12, S-21):** Bu blokta $\phi$ **daima moleküllerin hacim kesridir**; interferometre **fazı** ise $\varphi$ ile gösterilir (M-18). Momentum-ağırlıklı ortalama hız, gövde metninde (3.4.6.3) $w$ olarak geçer; katalogda Ek D · S-12 gereği $u_{ort}$ yazılır ($w$ dördüncü eksen koordinatına ayrılmıştır).

---

## M-15 · Kırılma İndisinin İlk-İlke Türetimi: $1/n^2 = 1-\phi$ · **[T]**

**Kullanıldığı bölümler:** 3.4.6.3, 2.6 (ışığın maddede yavaşlaması), 6.4, 5.1, 7.4 md.7.

### Varsayımlar
Üç girdi, homojenleştirme aksiyomları olarak alınır (üçü de teorinin başka yerlerinde bağımsızca kuruludur):

1. **(G1 — Korunum)** Moleküller Evrenakı'yı yaratmaz ve yok etmez, yalnızca deplase eder (iter). Hacimce ortalama **Evrenakı yoğunluğu** ortam içinde de arka plan değerindedir: $\bar\rho_m=\rho_0$.
2. **(G2 — Basınç karışım kuralı)** Her molekül, hacim kesri $\phi$ kadar yer kaplayan bir **düşük Evrenakı-basıncı cebidir** (zıtlık kuralı: atomik yoğunluk ile Evrenakı basıncı terstir; bkz. 2.4.2). Hacimce ortalama Evrenakı basıncı: $\bar P_m = P_0(1-\phi)$.
3. **(G3 — Sürüklenme zarfı)** Her molekülün deplase ettiği Evrenakı payı, o molekülün sürüklenme zarfı olarak onunla birlikte akar (Postülat 7'nin molekül ölçeğindeki hâli). Bu varsayım M-15'te yalnızca ortamın iki-bileşenli yapısını tanımlar; dinamik rolü M-16'da devreye girer.

**Ölçek gerekçesi (homojenleştirmenin meşruiyeti):** Işığın "dalga boyu" ölçeği (~500 nm), tipik molekül aralığından (~0,3 nm) yaklaşık üç mertebe büyüktür; Zerre bu yüzden tek tek molekülleri değil, ortamın **hacimce ortalanmış** hâlini örnekler. Ortalama alma işlemi bu ölçek ayrımına dayanır.

*(Burada $P$ ve $\rho$ daima Evrenakı'nın basıncı ve yoğunluğudur; atomik/moleküler yoğunlukla karıştırılmamalıdır.)*

### Adımlar
1. Kavrama Yasası (M-1) yerel biçimiyle uygulanır: Zerre'nin bir ortamdaki sürati, o ortamın Evrenakı basınç-iletim hızıdır ve ortalanmış alanlarla yazılır:
$$\left(\frac{c_0}{n}\right)^2=\frac{\bar P_m}{\bar\rho_m}$$
2. G1 ve G2 ikame edilir:
$$\left(\frac{c_0}{n}\right)^2=\frac{P_0(1-\phi)}{\rho_0}=c_0^2(1-\phi)$$
3. Sadeleştirme doğrudan kırılma indisini verir.

### Sonuç
$$\boxed{\;\frac{1}{n^2}=1-\phi\;\Longleftrightarrow\; n=\frac{1}{\sqrt{1-\phi}}\;}$$

Kavramsal çekirdek: **ışık madde içinde düşük *Evrenakı basıncı* nedeniyle yavaşlar**; hacimce ortalama Evrenakı yoğunluğu sabit kalır. Bu, kütle-itim mekanizmasıyla (M-2) tam aynı dildir — ikisi de bir düşük-Evrenakı-basıncı olgusudur.

### Yan Kontrol (bağımsız tutarlılık)
Su için $n=1{,}333$ ters okunursa $\phi = 1-1/n^2 = 0{,}437$ çıkar. Sıvı suyun moleküler paketlenme (hacim doldurma) kesri için bağımsız kestirimler ~0,36–0,40 aralığındadır; türetimin istediği hacim kesri, moleküler ölçekten gelen bu değerle aynı mertebede ve yakın banttadır. $\phi$ burada serbest fit parametresi değil, fiziksel anlamı bağımsızca sınanabilir bir büyüklüktür.

### Geçerlilik Sınırı
- Homojenleştirme, ışık ölçeği ≫ molekül aralığı koşuluna bağlıdır; molekül-ölçeğine inen yapılar (ör. nanofotonik boşluklar) için ortalama alma geçersizleşir.
- Türetim tek frekanslıdır; $n$'nin renge bağlılığı (dispersiyon) burada değil, M-17'de ve 7.4 md.7'de ele alınır.
- $\phi \to 1$ limiti ($n\to\infty$) fiziksel değildir; moleküler paketlenmenin geometrik üst sınırları $\phi$'yi 1'in belirgin altında tutar.
  > **Kapsam: bu yasak yalnız *tikel kafesler* içindir.** Argüman özdeş, geçilmez kürelerin paketlenme sınırına dayanır ($\pi/\sqrt{18}=0{,}7405$) ve moleküler/iyonik maddede geçerlidir. **Delokalize bir elektron gazına uygulanamaz:** metalik ve tam iyonize fazlarda kafes tikel değildir, elektron yoğunluğu ara hacmi de doldurur ve $\phi\to1$ **fiziksel hâle gelir** (11.4.1-(5): eşik altı bir cep için metalik hidrojende 30, Güneş plazmasında 3.000–11.000 protonluk boşluk gerekir ⟹ $\phi=1-\delta$, $\delta\lesssim10^{-13}$). Nötron maddesinde ise elektron gazı yoktur ve yasak **geçerli kalır** ($\phi\approx0{,}7$–$0{,}9$, paketlenme-sınırlı).

### Açık Uçlar
- $\phi$'nin (molekül başına etkin deplasman hacminin) birinci-ilkelerle, molekül girdap yapısından hesabı (7.4 md.7).
- G2'deki "cep içinde basınç ~0" idealleştirmesinin kısmi-basınçlı genel hâli.

---

## M-16 · Fizeau Sürükleme Katsayısı: $f=\phi=1-\dfrac{1}{n^2}$ · **[T]**

**Kullanıldığı bölümler:** 3.4.6.3–3.4.6.4, 6.4, 7.4 md.7.

### Varsayımlar
1. M-15'in sonucu ve G1–G3 aksiyomları.
2. Ortam iki bileşenin süperpozisyonudur ($\Psi_{Evrenakı}=\Psi_0+\sum_i\psi_i$, bkz. 1.3.1): **arka plan Evrenakı'sı** evrenseldir, moleküller onu akıtamaz — durgundur; **molekül deplasman payı** ise G3 gereği moleküllerle birlikte $u$ hızıyla akar.
3. Zerre balistiktir; ortamın toplu hareketi çizgisel hıza Galile toplamıyla eklenir (düşük hız rejimi, $u \ll c_0$).

### Adımlar
1. **Bileşenlerin yoğunluk payları.** Hacim kesirleriyle ağırlıklandırılır: durgun arka plan $(1-\phi)$ kesrini, moleküllerle birlikte akan deplasman payı $\phi$ kesrini kaplar. Her ikisinin yoğunluğu $\rho_0$ olduğundan payları $\rho_0(1-\phi)$ (hız 0) ve $\rho_0\phi$ (hız $u$), toplamı ise **tam olarak $\rho_0$**'dır — M-15'in $\rho=\rho_0$ kabulüyle birebir aynı muhasebe.
2. **Momentum-ağırlıklı ortalama hız.** Zerre'nin gördüğü etkin ortam hızı, momentum ağırlıklı ortalamadır:
$$u_{ort}=\frac{\rho_0(1-\phi)\cdot 0+\rho_0\phi\cdot u}{\rho_0(1-\phi)+\rho_0\phi}=\frac{\rho_0\phi\,u}{\rho_0}=\phi\,u$$
*(Ağırlıklandırma uyarısı: paylar $\rho_0$ ve $\rho_0\phi/(1-\phi)$ alınamaz — toplamı $\rho_0/(1-\phi)>\rho_0$ çıkar ve madde içinde arka plandan **daha yoğun** bir ortam ima eder; bu, M-15'in "molekül = düşük basınç cebi" aksiyomuyla ve $\rho=\rho_0$ kullanımıyla çelişir. Doğru olan hacim kesri ağırlıklandırmasıdır; **sonuç $u_{ort}=\phi u$'dur.**)*
*(Notasyon notu: bu büyüklük gövde metninde — 3.4.6.3 — $w$ olarak yazılıdır; Ek D · S-12 gereği katalogda $u_{ort}$ kullanılır.)*
3. **Galile toplamı.** Laboratuvar hızı: $v_{lab}=\dfrac{c_0}{n}+u_{ort}=\dfrac{c_0}{n}+\phi\,u$; sürükleme katsayısı tanım gereği $f=\phi$.
4. **M-15 ile birleştirme.** $\phi = 1-1/n^2$ ikamesi kapalı formu verir.

### Sonuç
$$\boxed{\,f=\phi=1-\frac{1}{n^2}\,}$$

Katsayı yalnızca $n$'ye bağlıdır; boru uzunluğundan ve akış geometrisinin ayrıntısından bağımsızdır (Zeeman'ın uzunluk-bağımsızlık gözlemiyle uyumlu).

> **$\phi$'nin ikinci rolü: kavrama kesri (Ek M-39, M-40).** Bu türetimin sonucu optikle sınırlı değildir. Elde edilen şey genel bir ifadedir: **maddenin sürüklediği ortam kesri $\phi$'dir, $(1-\phi)$ taşınmaz.** Aynı kesir, gök cisimlerinin deplasman genliğini de yönetir ve M-40'ın iç kavrama kanalını tanımlar ($\mathcal{R}=\phi$). **$\phi$ hıza değil genliğe girer:** iki-fazlı taşıma muhasebesi $\Delta P=-\kappa_5(\phi\rho_0)v^2$ ile $p=1$ verir (M-39, Varsayım 4).
>
> Bunun iki sonucu vardır:
> - **Kavrama kütleyle değil hacimle ölçeklenir.** Su için $\phi=0{,}437$ iken $\rho_{su}/\rho_n=3{,}7\times10^{-15}$'tir — 14 mertebe fark. Deplasman kafesi bare nükleon değil **atomun tamamıdır**: elektron kabuğu kütlesel olarak boş, Evrenakı açısından doludur. Fizeau'nun ölçtüğü $0{,}434\pm0{,}020$ bunu doğrudan doğrular — kütle ölçeklemesi geçerli olsaydı akan su ışığı hiç sürüklemezdi.
> - **Çapraz-ölçek iddiası.** Laboratuvarda akan sudaki ışık sürüklenmesi ile gezegen basıklığının $J_4$ imzası, teoride **tek bir büyüklüğün** iki ölçekteki tezahürüdür. Bu, 3.4.6.4'ün "tek mekanizma, iki ölçek" iddiasının üçüncü ayağıdır ve bağımsızca sınanabilir.
>
> *Sınır:* $\phi=1-1/n^2$ saydam ortamlar için türetildi. Opak/metalik fazlarda ($n$ karmaşık) ve iyonize plazmada okunması ayrı argüman gerektirir; o argüman **11.4.1-(4)–(5)**'te kurulmuştur ve hacim kesri her fazda tanımlı kalır. *(Dikkat: "bağlı kafes çözülünce $\phi$ çöker" biçimindeki yaygın okuma **yanlıştır ve işareti terstir.** Kafes çözülünce $\phi$ çökmez; delokalize elektron gazı ara hacmi doldurduğu için **1'e çıkar.**)*

### Doğrulama Tablosu
| Ortam | $n$ | Öngörü $f=1-1/n^2$ | Ölçüm | Durum |
|---|---|---|---|---|
| Su | 1,333 | 0,437 | 0,434 ± 0,020 (Michelson & Morley, 1886) | ✓ (%1'in altında sapma) |
| Karbon disülfür (CS₂) | 1,63 | 0,624 | Zeeman dizisi ile uyumlu | ✓ |
| Gaz limiti | $n\to 1$ | $f\to 2(n-1)\to 0$ | Seyreltik ortamda sürükleme kaybolur | ✓ |

Gaz limiti aynı zamanda iç tutarlılık sınavıdır: $\phi\to 0$ iken ortam saf arka plana döner ve sürükleme sıfırlanır — mekanizmanın "kısmi"liği yapısaldır, ayarlanmış değildir.

### Geçerlilik Sınırı
- $u \ll c_0$ (Galile toplamı) ve M-15'in homojenleştirme koşulları.
- Türetim tek frekanslıdır; renge bağlı ek terim M-17'dedir.
- Michelson–Morley'in sıfır sonucu ile çelişki yoktur: gezegen ölçeğinde zarf yerel Evrenakı'yı **tam** taşır (M&M sıfır), molekül ölçeğinde her molekül **yalnızca kendi deplasman payını** taşır (Fizeau kısmi) — aynı Postülat 7'nin iki ölçekteki görünümü (3.4.6.4; interferometre tarafı için M-18).

### Açık Uçlar
- **G3'ün "tam taşıma" katsayısı.** Türetim, deplase edilen Evrenakı'nın *tamamının* molekülle aktığını (taşıma katsayısı 1) varsayar. Klasik hidrodinamikte bir kürenin sürüklediği eklenmiş kütle (added mass) katsayısı ½'dir; teorinin 1 varsayımı Postülat 7'nin entrainment tanımıyla tutarlıdır ama bağımsız bir hidrodinamik hesapla doğrulanmalıdır (7.4 md.7).

---

## M-17 · Dispersiyon Düzeltmesi (Lorentz Katsayısı) · **[T]**

**Kullanıldığı bölümler:** 3.4.6.5, 6.4, 7.4 md.7.

### Varsayımlar
1. M-16'nın sonucu ($u_{ort}=\phi u$ entrainment payı).
2. Zerre bir **mermi akışıdır**; renk, katarın içindeki ardışık Zerre ritmidir (2.3). Ortam $u$ ile aktığında bu ritim molekül çerçevesinde Doppler ile kayar.
3. Zerre–molekül etkileşimi, molekülün *kendi çerçevesinde gördüğü* ritme göre gerçekleşir; dolayısıyla kırılma indisi kaymış frekansta değerlenir: $n = n(\omega')$.
4. $n(\omega)$ bağımlılığı ölçümden alınır (dispersiyonun mikroskobik kökeni bu türetimin girdisi değildir; bkz. Açık Uçlar).

### Adımlar
1. **Doppler ritim kayması.** Ortam ışıkla aynı yönde $u$ hızıyla aktığında moleküller Zerreleri daha seyrek yakalar; ortam içi hız $c_0/n$ olduğundan molekül çerçevesindeki ritim:
$$\omega'=\omega\left(1-\frac{nu}{c_0}\right)$$
2. **İndisin kaymış frekansta değerlenmesi.** Taylor açılımıyla ($\omega'-\omega=-\omega n u/c_0$):
$$n(\omega')\approx n(\omega)-\frac{dn}{d\omega}\cdot\frac{\omega n u}{c_0}$$
3. **Sürat payı.** $c_0/n(\omega')$ birinci mertebede genişletilir:
$$\frac{c_0}{n(\omega')}\approx\frac{c_0}{n}+u\,\frac{\omega}{n}\frac{dn}{d\omega}$$
4. **Sentez.** Bu renk payı, M-16'nın entrainment payıyla ($u_{ort}=(1-1/n^2)u$) toplanır:
$$v_{lab}=\frac{c_0}{n}+u\left[\,1-\frac{1}{n^2}+\frac{\omega}{n}\frac{dn}{d\omega}\,\right]$$

### Sonuç
$$\boxed{\;v_{lab}=\frac{c_0}{n}+u\left[\,1-\frac{1}{n^2}+\frac{\omega}{n}\frac{dn}{d\omega}\,\right]\;}$$

Köşeli parantezin son terimi, Lorentz'in dispersiyon-düzeltmeli katsayısının birebir aynısıdır ve **Zeeman'ın (1914–15) ölçtüğü tam katsayıdır.** Normal dispersiyonda $dn/d\omega>0$ olduğundan renk katkısı pozitiftir: sürükleme artar — Zeeman'ın gözlediği işaretle uyumlu. Böylece Fizeau ailesinin hem ana katsayısı (M-16) hem ince renk yapısı (M-17), tek bir Zerre-akışı resminden çıkar.

### Geçerlilik Sınırı
- Birinci mertebe ($u/c_0$'de doğrusal) açılım; $u \ll c_0$.
- $n(\omega)$ **ölçümden alınır**; türetim, verili bir dispersiyon eğrisinin hareketli ortamda nasıl ek sürükleme ürettiğini hesaplar — dispersiyonun kendisini üretmez. (Standart fizikte de yapı aynıdır: Lorentz katsayısı, osilatör modelinden bağımsız olarak $n(\omega)$ verisiyle çalışır.)
- Frekans ayrımı: burada $\omega$ açısal ritimdir; katar frekansı $\nu$ ile ilişki standarttır ($\omega = 2\pi\nu$), Ek D · S-15 gereği $f$ frekans için kullanılmaz.

### Açık Uçlar
- **Dispersiyonun mikroskobik kökeni:** $n$'nin renge bağlılığının, Zerre atış ritmi ile molekül girdaplarının rezonans tepkisi arasındaki bağdan türetilmesi (7.4 md.7).

---

## M-18 · İnterferometre Faz Duyarlılığı ve Asimetrik Kol Tasarımı · **[T]**

**Kullanıldığı bölümler:** 3.4.5, 5.1, 7.4 (T-3/T-9 kayıtları), 7.5 tablosu.

*(Notasyon notu: kaynak metinlerde faz $\varphi$/φ ailesiyle yazılıdır; hacim kesri $\phi$ ile (M-15/M-16) karışmaması için katalogda faz daima $\varphi$ ile gösterilir — Ek D · S-21.)*

### Varsayımlar
1. İki kollu bir interferometrede her kol, ışığı $L$ yolunda gidiş-dönüş taşır; kaynak açısal ritmi $\omega$ sabittir.
2. Sürüklenme zarfı **yönsel** bağıl hızı sıfırlar, ancak **skaler** $P/\rho$ büyüklüğüne saydamdır: yerel $c_0=\sqrt{P/\rho}$, dış kozmik ortamın değerini izler (3.4.5, "Zarfın İki Ayrı İşlevi"). Yani laboratuvarda esir rüzgârı yoktur, ama $c_0$'nin skaler zaman değişimi ($c_0\to c_0+\delta c$) düzeneğe ulaşır.
3. Kollar rijittir; $\delta L$ değişimleri (termal vb.) sistematik kalemi olarak ayrıca ele alınır.

### Adımlar
1. **Tek kol fazı.** Gidiş-dönüş faz katkısı:
$$\varphi=\omega\cdot\frac{2L}{c_0}$$
2. **İki kol farkı.**
$$\Delta\varphi=\frac{2\omega}{c_0}\,(L_1-L_2)$$
3. **Skaler $c_0$ değişimine duyarlılık.** $c_0\to c_0+\delta c$ varyasyonu alınır:
$$\delta(\Delta\varphi)=-\frac{2\omega}{c_0^2}\,(L_1-L_2)\,\delta c$$
4. **İki yapısal sonuç:**
   - **(i) Eşit kollu düzenek skaler değişime kördür.** $L_1=L_2$ ise $\delta(\Delta\varphi)=0$ — kol uzunluğu, hassasiyet veya işletme süresi ne olursa olsun. Klasik Michelson–Morley bu sınıftadır: yalnızca **anlık yön anizotropisini** görür; zarf onu sıfırladığından sonuç sıfırdır. **M&M'in null sonucu teoriyle çelişmez** — düzenek, teorinin öngördüğü büyüklüğe yapısal olarak kapalıdır.
   - **(ii) Asimetrik kollar skaler değişimi ölçer.** $L_1\ne L_2$ yapılırsa $\delta(\Delta\varphi)\propto(L_1-L_2)\,\delta c$ sıfırdan ayrılır. Kısım 5 düzeneğinin kolları bu yüzden **kasıtlı olarak eşitsizdir** (15/45 cm; 3:1 oran): $L_1-L_2=30$ cm'lik kaldıraç, skaler $c_0$ driftini faz kaymasına çevirir.
5. **Tamamlayıcılık teoremi.** Eşit kollu M&M ile asimetrik kollu Kısım 5 düzeneği **farklı fiziksel büyüklükleri** ölçer (yönsel anizotropi vs skaler zaman değişimi); ikisinin sonuçları çelişmez, ikili imza oluşturur: *eşit kolda sıfır + asimetrik kolda drift.*

### Sonuç
$$\boxed{\;\delta(\Delta\varphi)=-\frac{2\omega}{c_0^2}\,(L_1-L_2)\,\delta c\;;\qquad L_1=L_2\Rightarrow\text{skaler }\delta c\text{'ye yapısal körlük}\;}$$

### Sistematikler (bağlayıcı uyarı)
Termal genleşme kaynaklı $\delta L$, faz farkında $\delta(\Delta\varphi)=\frac{2\omega}{c_0}\,\delta(L_1-L_2)$ üretir — **skaler $\delta c$ ile aynı imzada** bir yavaş kaymadır (dejenerasyon). Farklı uzunluktaki kollar farklı termal genleşme yaşadığından, aylar ölçeğindeki ölçümde sıcaklık kontrolü ve sıcaklık-bağımsızlık gösterimi **şarttır**; bu kontrolün raporu deney fazının (Kısım 5 tam yazımı, T-9) kalemidir.

### Geçerlilik Sınırı
- Türetim skaler ve birinci mertebedir ($\delta c/c_0 \ll 1$); kaynak ritmi $\omega$'nun kendisinin $\delta c$'den etkilenmediği (veya etkisinin ortak-mod olarak düştüğü) varsayılır.
- Yönsel etkiler bilinçli olarak dışarıda tutulmuştur: zarf onları sıfırlar (3.4.5); buradaki analiz yalnızca skaler kanalı kapsar.

### Açık Uçlar
- **Beklenen sinyal genliği:** teorinin, yerel kozmik ortam değişimlerinden doğan $\delta c/c_0$ mertebesini bağımsızca öngörmesi (şu an ölçüm-güdümlü; öngörü 7.4 kalemidir).
- Termal dejenerasyonun deney raporunda nicel kapatılması (T-9; deney yazım fazına planlıdır).
