# Ek M — Merkezî Türetim Kataloğu · Blok A: Temel Yasalar ve Hız Merdiveni

> **Ek M sistemi nasıl çalışır:** Kitabın tüm çok adımlı türetimleri bu katalogda, kalıcı [M-n] numaralarıyla toplanmıştır. Gövde bölümleri yalnızca *sonuç* denklemini ve fiziksel sezgiyi taşır; tam türetim, varsayımları ve geçerlilik sınırıyla birlikte buradadır. Her türetim beş sabit başlıkla yazılır: **Varsayımlar → Adımlar → Sonuç → Geçerlilik Sınırı → Açık Uçlar.** Sembol standardı için bkz. Ek D (Sembol Sözlüğü).
>
> **Statü rozetleri (Ek C ile ortak dil):** **[T]** ilk-ilkelerden türetilmiş · **[S]** gözlemle sabitlenmiş · **[A]** aralıkla sınırlanmış · **[K]** kalibre edilmiş / betimleyici fit (türetim değildir, dürüstçe işaretlenir).

---

## M-1 · Kavrama Yasası: $c = \sqrt{P/\rho}$ · **[T]**

**Kullanıldığı bölümler:** Postülat 4 (1.3), 2.4.2, 2.10.1, 3.4.5–3.4.6, 4.2.15, 6.2, Kısım 5'in tüm deney programı.

### Varsayımlar
1. Evrenakı, sıkıştırılabilir bir süper-akışkandır (Postülat 1); yerel basıncı $P$, yerel yoğunluğu $\rho$ dinamik alanlardır.
2. Işık (Zerre), bu ortama *tutunarak* ilerler; çizgisel hızının üst sınırı, ortamın mekanik sinyal iletme hızıdır (sonik analoji: bir akışkanda basınç sinyali sesten hızlı taşınamaz).

### Adımlar
1. Bir akışkanda küçük basınç bozuntularının yayılma hızı Newton–Laplace biçimindedir: $v_s^2 = dP/d\rho$ (Newton, 1687; Laplace, 1816).
2. Evrenakı'nın çalışma rejimi, yoğunluğun basınca zayıf eşlik ettiği ($k \ll 1$; bkz. M-8 ve Yön Kuralı, 2.4.2) doğrusal rejimdir: $P \approx A\rho$ biçiminde tek katsayılı hâl ilişkisi.
3. Doğrusal rejimde iki biçim özdeşleşir:
$$P = A\rho \;\Longrightarrow\; \frac{dP}{d\rho} = A = \frac{P}{\rho}$$
4. Zerre'nin kavrama (tutunma) limiti bu sinyal hızına eşitlenir.

### Sonuç
$$\boxed{c = \sqrt{\frac{P}{\rho}}\,, \qquad c_0 = \sqrt{\frac{P_0}{\rho_0}} = 2{,}998\times10^8 \text{ m/s}, \qquad \rho_0 = \frac{P_0}{c^2}}$$

$c$ evrensel bir sabit değil, **yerel ve türetilmiş** bir büyüklüktür; arka plan değeri $P_0$, $\rho_0$ çifti tarafından belirlenir.

### Geçerlilik Sınırı
- **Oran biçimi ($c^2 = P/\rho$) resmî biçimdir** ve kitap boyunca kullanılır. Diferansiyel biçim yalnızca kararlılık argümanlarında (M-9) geçer ve **oran biçiminden türetilir, ona eşit değildir.** Eşlik oranının tanımı ($\delta\rho/\rho_0 = k\,\delta P/P_0$, Ek B.3) integre edilince $\rho \propto P^{k}$, yani $P \propto \rho^{1/k}$ elde edilir; buradan
$$\frac{dP}{d\rho} = \frac{1}{k}\cdot\frac{P}{\rho} = \frac{c^2}{k}$$
  İki biçim yalnız $k=1$'de özdeştir ($P\propto\rho$); $k<1$ olduğu sürece diferansiyel biçim daima **$1/k$ kat büyüktür.** Bu ayrışma genliğe değil yalnız $k$'ya bağlıdır — sabit $k$ için her sıkışma genliğinde aynı çarpanla geçerlidir. Kitabın bütün fenomenolojisinde (Yön Kuralı, $P_0$ sabitlemesi, kızıla kayma) oran biçimi esas alınır.
  *(Düzeltme kaydı, 28 Temmuz 2026: bu maddenin önceki sürümü $P\propto\rho$ hâlini $k\ll1$ ile eşliyordu; doğrusu $k=1$'dir. Etiket karışıklığı M-9'un kararlılık çekincesine taşınmıştı, orada da giderildi.)*
- Yasa, Zerre'nin *çizgisel öteleme* hızını sınırlar; kohezyon kanalının elastik sinyal hızını ($v_m$, M-5) sınırlamaz. $c$ mutlak bir üst sınır değildir (Postülat 4).

### Açık Uçlar
- $P(\rho)$ hâl denkleminin (ve $A$ katsayısının) Zerre-ölçeği mekaniğinden birinci-ilkelerle türetimi (7.4).
- $k$ eşlik oranının bağımsız ölçümü (SN 1987A gecikme bütçesi; Ek C satır 3).

---

## M-2 · Kütle-İtim Denklemi ve İşaret Konvansiyonu · **[T]**

**Kullanıldığı bölümler:** Postülat 6 (1.3), 1.5, 3.4.1–3.4.2, 3.8.6, 4.2.4, 6.0.

### Varsayımlar
1. Uzayda tek kuvvet aktörü, Evrenakı basınç alanının uzaysal değişimidir ($\nabla P$).
2. Bir cisme etkiyen itim, cismin nükleonlarının deplase ettiği hacimle orantılıdır; nükleon öz yoğunluğu $\rho_n \approx 2{,}7\times10^{17}$ kg/m³ evrensel sabittir (Postülat 4).

### Adımlar
1. $N$ nükleonlu bir cismin etkileşim hacmi $\gamma_N = N V_n$; kütlesi $m = N m_n$; oran $\gamma_N/m = V_n/m_n = 1/\rho_n$ cinsten bağımsızdır.
2. Cisme etkiyen net kuvvet, yüksek basınçtan alçak basınca doğru iter: $\vec F = -\gamma_N \nabla P$.
3. İvme: $\vec a = \vec F/m = -(\gamma_N/m)\nabla P$.

### Sonuç
$$\boxed{\vec a = -\frac{1}{\rho_n}\nabla P}$$

Boyut kontrolü: $[\text{Pa/m}]/[\text{kg/m}^3] = \text{m/s}^2$ ✓. $\rho_n$ evrensel olduğundan ivme cisimden bağımsızdır — **Galileo'nun eşit-düşme gözlemi teoremdir, rastlantı değil.**

### İşaret (Kuyu) Konvansiyonu — bağlayıcı
- Kütle çevresinde basınç kuyusu: $dP/dr > 0$ (merkezden uzaklaştıkça basınç artar).
- Kuvvet ve ivme daima **eksi** işaretle yazılır: $\vec a = -\nabla P/\rho_n$; merkeze doğru itim buradan çıkar.
- $\nabla P$ tek başına "kuvvet" olarak adlandırılamaz; skaler basınç farkı $\Delta P$ ile gösterilir, $\nabla P$ ile asla eşitlenmez.
- Çok bileşenli alanlarda: $\nabla P_{toplam} = \nabla P_r + \nabla P_{spin}$ (radyal deplasman + dönüş kaynaklı bileşen; Ek B.1).

### Geçerlilik Sınırı
Denklem, cismin sürüklenme zarfı içindeki bağıl hızının sıfır olduğu (Postülat 7) ve $\rho_n$'nin sabit kaldığı standart madde için geçerlidir.

### Açık Uçlar
- $\gamma_N$'nin nükleon başına etkin hacminin ($V_n$) bağımsız belirlenmesi; $G = \alpha/\rho_n$ türetimiyle bağı için bkz. M-28.

---

## M-3 · Denge Yüzey Hızı: $\sqrt{2}\,c$ · **[T]**

> **Okuma sırası.** Aşağıdaki türetim sıkıştırılamaz Bernoulli ile yapılmıştır ve **tarihsel/pedagojik** değerdedir: sonucu doğru sayıya ulaştırır ama yanlış gerekçeyle. Geçerli türetim **M-3′**'tür (bu girdinin sonunda) ve sıkıştırılabilir hâl denklemini kullanır. İki türetimin sonucu aynı sayıdır ($\sqrt2c$), **anlamı farklıdır**: burada "basıncın sıfırlandığı cep duvarı", M-3′'te "yoğunluğun e-katlanma ölçeği".

**Kullanıldığı bölümler:** Postülat 5 (1.3), Ek A.2, 2.10.1, 7.4 md.10.

### Varsayımlar
1. Nükleon, merkezinde vakum cebi ($P_{cep} \approx 0$) barındıran, çeperi yüksek hızla dönen bir girdap zarfıdır.
2. Girdap alanı 2-boyutlu ideal potansiyel girdaptır: $v_\theta(r) = \Gamma/2\pi r$ ($\Gamma$: sirkülasyon).
3. **Sıkıştırılamaz Bernoulli kullanılır:** $P(r) = P_0 - \tfrac12 \rho_0 v_\theta^2(r)$.
   > ⚠️ Bu, **ortamın sıkıştırılamaz olduğu** anlamına gelmez — Postülat 1 ortamı sıkıştırılabilir kurar ve bu teorinin bel kemiğidir. İfade yalnızca *hesapta kullanılan denklemin adıdır*: Bernoulli'nin $\rho$'yu akım çizgisi boyunca sabit tutan biçimi. Yaklaşımın bu türetimde ne kadar ağır olduğu Geçerlilik Sınırı'nda nicelenmiştir — **hafif bir idealleştirme değildir.**

### Adımlar
1. Cep duvarında ($r = r_{cep}$) basınç sıfıra iner:
$$P_0 - \tfrac12\rho_0 v_{duvar}^2 = 0$$
2. Çözüm:
$$v_{duvar} = \sqrt{\frac{2P_0}{\rho_0}} = \sqrt{2}\cdot\sqrt{\frac{P_0}{\rho_0}} = \sqrt{2}\,c$$
3. **Evrensellik (çekim noktası):** Cep yarıçapı sirkülasyondan gelir: $r_{cep} = \Gamma/2\pi\sqrt{2}c$. Zarf hızlanırsa cep genişler, hız düşer; yavaşlarsa cep daralır, hız artar — sistem $\sqrt{2}c$'ye geri oturur. Duvar hızı $\Gamma$'dan **bağımsızdır**: her vakum-cepli girdap, boyutu ne olursa olsun aynı yüzey hızında döner.
4. **Zorunluluk:** $\tfrac12\rho_0 v^2 < P_0$ ise cep basınç açığını üretemez ve çöker → yüzeyi $c$-altı hızda dönen kararlı madde var olamaz.

### Sonuç
$$\boxed{v_{denge} = \sqrt{2}\,c \approx 4{,}24\times10^8 \text{ m/s}}$$

### Sayısal Çapraz Kontrol
Gözlemsel girdi: proton için $v_{ekvator} = 2\pi\nu_c R_p \approx 5\times10^8$ m/s ($\nu_c \approx 10^{23}$ Hz, $R_p = 0{,}84$ fm). Fark ~%18. Ters okuma: $\nu = \sqrt{2}c/2\pi R_p \approx 8\times10^{22}$ Hz — Compton frekansıyla mertebe + $O(1)$ uyumu.

### Geçerlilik Sınırı

Üç idealleştirme kullanılmıştır: sıkıştırılamaz Bernoulli, 2B ideal girdap, tam-sıfır cep basıncı. **Birincisi hafif değildir ve bu türetimin sonucunu mertebe göstergesine indirir.**

**Yaklaşım rejim dışında kullanılmıştır.** Ortamın sıkışma kanalındaki ses hızı **tam olarak $c$**'dir ($P=c^2\rho$ stiff hâl denklemi, **Ek M-44**). Dolayısıyla $v_{duvar}=\sqrt2\,c$ noktasında

$$\mathrm{Mach}=\frac{\sqrt2\,c}{c}=1{,}41 \qquad\Longrightarrow\qquad \textbf{süpersonik}$$

Sıkıştırılamaz Bernoulli $M^2\ll1$ ister; yaklaşımın kendi hata tahmini $\delta\rho/\rho\sim M^2/2$'dir ve $M=1{,}41$'de bu **%100**'dür. Yani yaklaşım küçük bir düzeltme payı bırakmıyor, **geçerlilik bölgesinin dışında** çalışıyor.

**Sıkıştırılabilir hesap ne veriyor?** Stiff hâl denklemiyle kararlı akış enerji denklemi ($\tfrac12v^2+h=$ sbt, $h=c^2\ln\rho$):

$$v^2 = 2c^2\ln\frac{\rho_0}{\rho}$$

Bunun iki sonucu vardır ve ikisi de 1. ile 4. adımı etkiler:

- **$v=\sqrt2\,c$'de basınç sıfıra inmez.** $\ln(\rho_0/\rho)=1$ ⟹ $\rho=\rho_0/e=0{,}37\rho_0$ ve $P=0{,}37\,P_0$. Yani 1. adımın "cep duvarında basınç sıfırdır" ifadesi sıkıştırılamaz yaklaşımın ürünüdür.
- **Vakum cebi hiçbir sonlu hızda oluşmaz.** $P\to0$ için $\rho\to0$, o da $v\to\infty$ gerektirir. Stiff bir akışkanda **düzgün seyrelmeyle** vakum cebi açılamaz.

**Cep oluşumunun doğru aracı M-4'tür.** Cep, düzgün seyrelmeyle değil **yırtılmayla** (kohezyon yenilmesiyle) açılır; eşiği $v_{kav}=\sqrt2\,c\sqrt{1+\Sigma/P_0}$'dır ve $\Sigma/P_0>10^8$ olduğundan $v_{kav}>10^4c$'dir. Malzeme kopma eşiği ile akım-çizgisi hesabı farklı araçlardır; M-3 mevcut bir cebin *denge* hâlini, M-4 yeni cep *açma* eşiğini tarif eder.

---

## M-3′ · Sıkıştırılabilir Yeniden Türetim: $\sqrt2\,c$ Neden Hayatta Kalıyor

*(29 Temmuz 2026'da eklendi. Yukarıdaki sıkıştırılamaz türetimin yerine geçer; sonuç sayısı korunur, **anlamı değişir**.)*

### Doğru araç: kararlı akış entalpi denklemi

Kararlı, dönüsüz, barotropik akışta $\tfrac12v^2+h=$ sabittir ve bu bağıntı **Mach sayısından bağımsız** geçerlidir (Crocco teoremi). Potansiyel girdap eksen dışında dönüsüzdür, dolayısıyla süpersonik çekirdekte de kullanılabilir. Stiff hâl denklemiyle ($P=c^2\rho$, Ek M-44) entalpi $h=\int dP/\rho=c^2\ln\rho$ olduğundan, sonsuzda durgunluk koşuluyla:

$$\boxed{\;v^2 = 2c^2\ln\frac{\rho_0}{\rho}\;}$$

### Sonuç 1: keskin duvar yok, üstel seyrelme var

Ters çevrilip $v=\Gamma/2\pi r$ konulunca çekirdek profili çıkar:

$$\rho(r)=\rho_0\exp\!\left(-\frac{v(r)^2}{2c^2}\right)=\rho_0\exp\!\left(-\frac{\Gamma^{2}}{8\pi^{2}c^{2}r^{2}}\right)$$

Yoğunluk merkeze doğru **üstel olarak** azalır ve hiçbir sonlu yarıçapta sıfırlanmaz. "Cep duvarı" diye keskin bir yüzey yoktur.

| $v/c$ | $\rho/\rho_0$ | $r/r_e$ | |
|---|---|---|---|
| 1,000 | 0,607 | 1,414 | sıkışma kanalında $M=1$ |
| 1,414 | **0,368** | **1,000** | **e-katlanma noktası** |
| 1,668 | 0,249 | 0,848 | protonun gözlenen ekvatoru |
| 3,035 | 0,010 | 0,466 | etkin vakum sınırı (%1) |
| 5,000 | $4\times10^{-6}$ | 0,283 | fiilen boş |

### Sonuç 2: $\sqrt2\,c$, yoğunluğun e-katlanma hızıdır

Profilin doğal ölçeği, üstelin 1 olduğu noktadır:

$$\rho=\frac{\rho_0}{e}\;\Longrightarrow\;\ln\frac{\rho_0}{\rho}=1\;\Longrightarrow\;\boxed{\;v=\sqrt2\,c\;}$$

**Sayı korunur, gerekçesi değişir.** Sıkıştırılamaz hesap $\sqrt2c$'yi "basıncın sıfırlandığı duvar hızı" diye veriyordu; doğrusu **üstel seyrelmenin e-katlanma ölçeğidir** ve orada $\rho=P/c^2$ arka planın %37'sindedir, sıfır değil. Bu keyfi bir tanım değil: e-katlanma, üstel bir profilin kanonik ölçeğidir (ölçek yüksekliği gibi).

### Sonuç 3: evrensellik aynen korunur

E-katlanma yarıçapı sirkülasyondan gelir ve **eski $r_{cep}$ formülünün birebir aynısıdır**:

$$r_e=\frac{\Gamma}{2\pi\sqrt2\,c}$$

Dolayısıyla M-3'ün 3. adımındaki çekim-noktası argümanı geçerliliğini korur: her vakum-cepli girdap, $\Gamma$'sı ne olursa olsun **kendi e-katlanma yarıçapında aynı hızda** döner. Evrensellik yaklaşımın değil profilin özelliğidir.

### Sonuç 4: çekirdek için kavitasyon **gerekmiyor**

Sıkıştırılamaz resimde vakum cebi ancak basınç sıfıra inerek — yani ortam yırtılarak — açılabiliyordu; bu, M-4'ün $v_{kav}=\sqrt2c\sqrt{1+\Sigma/P_0}>10^4c$ eşiğini gerektiriyordu ve $\sqrt2c$ ile arasında dört mertebe uyuşmazlık vardı.

Sıkıştırılabilir resimde bu gerilim **kalkıyor**: çekirdek bir *yırtık* değil, bir **seyrelmedir**. $v\gtrsim3c$'de yoğunluk zaten %1'in altına iniyor ve $v\sim5c$'de fiilen boşluk oluşuyor — kohezyon yenilmesine ihtiyaç yok. $\Sigma$ ve $v_{kav}$ başka işler için (kohezyon kanalı $v_m$, M-7'nin yırtılmama koşulu) anlamlı kalır, ama **nükleon çekirdeğini açmak için gerekmezler.**

### Sonuç 5: %18 sorunu çözülüyor — çünkü sorun yokmuş

En önemli sonuç bu. Sıkıştırılamaz resimde $\sqrt2c$ *keskin bir duvarın* hızıydı, dolayısıyla protonun gözlenen ekvator hızı ($5\times10^8$ m/s $=1{,}668\,c$) ile arasındaki %18 fark açıklanması gereken bir **tutarsızlıktı**.

Sıkıştırılabilir resimde ikisi **aynı düzgün profilin iki komşu noktasıdır**:

| Nokta | $v/c$ | $\rho/\rho_0$ |
|---|---|---|
| E-katlanma ölçeği (teorik referans) | 1,414 | 0,368 |
| Protonun kompozit ekvatoru (gözlem) | 1,668 | 0,249 |

Profil sürekli olduğu için iki farklı "yüzey" tanımının %18 farklı hız vermesi **beklenen** şeydir; çelişki değildir. Yani ~%18, bir düzeltme bütçesi de, rejim ihlalinin işareti de değil — **keskin duvar varsayımının yarattığı yapay bir problemdi ve varsayım kaldırılınca ortadan kalktı.**

### Geçerlilik Sınırı (M-3′)

- **Derin seyrelme rejiminde hâl denklemi en az sınanmış yerdedir.** $P=c^2\rho$'nun $\rho\to0$'a kadar geçerli olduğu varsayılmıştır; gerçek ortamın çok seyrek limitte stiff kalıp kalmadığı bilinmemektedir.
- **Çekirdeğin tamamı süpersoniktir** ($M=1$ noktası $r=1{,}414\,r_e$'dedir). Entalpi bağıntısı bu rejimde geçerlidir (dönüsüz, şoksuz), ama şok oluşumu olasılığı ayrıca incelenmemiştir.
- **Yoğunluk katmanlı girdabın kararlılığı denetlenmemiştir.** Rayleigh ölçütü potansiyel girdapta marjinaldir; yoğunluk gradyanının katkısı hesaplanmalıdır.
- 2B ideal girdap ve tekil-Zerre idealleştirmeleri korunmuştur; kompozit zarf için etkin $\Gamma$ dağılımı hâlâ açıktır.

### Açık Uçlar (M-3′)
- Derin seyrelme limitinde hâl denkleminin sınanması (çok seyrek rejimde stiff mi?).
- Yoğunluk katmanlı potansiyel girdabın kararlılık analizi.
- Kompozit (çok-Zerreli) zarfta etkin $\Gamma$ dağılımı ve profilin buna duyarlılığı.
- ~~%18 farkın düzeltme kalemlerine dağıtılması~~ → **kapandı**: fark bir hata payı değil, sürekli profilde iki farklı yüzey tanımının doğal sonucudur. 7.4 md.10(ii) buna göre okunmalıdır.
- Kompozit (çok-Zerreli) zarfta etkin $\Gamma$ dağılımı.

---

## M-4 · Kavitasyon Eşiği ve Kohezyon Dayanımı: $v_{kav}$, $\Sigma$ · **[T]** *(Σ: [A])*

**Kullanıldığı bölümler:** Ek A.3, 2.10.1, 7.4 md.10.

### Varsayımlar
1. Evrenakı, basıncına ($P_0$) ek olarak bir **kohezyon (çekme) dayanımına** ($\Sigma$) sahiptir: akışkan, mutlak sıfır basıncın altında $-\Sigma$'ya kadar gerilime yırtılmadan dayanır. (Klasik analog: suyun teorik çekme dayanımı ~$10^2$ MPa, atmosfer basıncının ~bin katı; Briggs, 1950.)
2. M-3'ün Bernoulli kurulumu geçerlidir.

### Adımlar
1. Yırtılma (kavitasyon), zarf hızının basınç *ve* kohezyon toplamını tüketmesiyle başlar:
$$P_0 + \Sigma - \tfrac12\rho_0 v_{kav}^2 = 0$$
2. Çözüm ve $\rho_0 = P_0/c^2$ ikamesi:
$$v_{kav} = \sqrt{\frac{2(P_0+\Sigma)}{\rho_0}} = \sqrt{2}\,c\,\sqrt{1+\frac{\Sigma}{P_0}}$$

### Sonuç
$$\boxed{v_{kav} = \sqrt{2}\,c\,\sqrt{1+\frac{\Sigma}{P_0}} \gg c \qquad (\Sigma/P_0 > 10^8)}$$

### Geçerlilik Sınırı
$\Sigma$ şu an yalnızca alttan sınırlıdır (Bell deneyleri üzerinden, bkz. M-5); tam değeri serbesttir (Ek C satır 9).

### Açık Uçlar
- $\Sigma$'nın bağımsız bir gözlemle tam sabitlenmesi.
- Yırtılmama koşulunun kohezyonlu genel hâli $P_0 + \Sigma > \Delta P$ ile Ek B.2'nin muhafazakâr ($\Sigma=0$) alt sınırının tek metinde birleştirilmesi (7.4 md.10-i).

---

## M-5 · Kohezyon Kanalı Sinyal Hızı: $v_m$ · **[T]** *(alt sınır: [A])*

**Kullanıldığı bölümler:** 2.10.1 (Bell/dolanıklık programı), 6.0, 7.5 satır 8.

### Varsayımlar
1. Sürekli ortamlar mekaniğinde iki bağımsız sinyal kanalı vardır: **sıkışma** (hız: $\sqrt{dP/d\rho}$) ve **kesme/gerilme** (hız: $\sqrt{G_s/\rho}$, $G_s$: kesme modülü).
2. Evrenakı'da sıkışma kanalının direnci $P_0$ (ve eşlik oranı $k$), kesme/kohezyon kanalının direnci $\Sigma$'dır (M-4). İki kanal **bağımsız modüllerden** beslenir; bu bağımsızlık aşağıdaki türetimin dayanağıdır.
   *(Düzeltme kaydı, 28 Temmuz 2026: bu varsayımın önceki sürümü "sıkışma kanalının hızı $c$'dir" diyordu. Doğrusu $\sqrt{dP/d\rho} = c/\sqrt{k}$'dır — M-9. $c=\sqrt{P/\rho}$ Zerre'nin **öteleme** sınırıdır, ortamın akustik dalga hızı değil; M-1'in Geçerlilik Sınırı bu ayrımı kurar. Aşağıdaki $v_m$ türetimi bu düzeltmeden **etkilenmez**, çünkü yalnız $\rho_0=P_0/c^2$ oran biçimini kullanır.)*

### Adımlar
1. Kohezyon kanalının elastik sinyal hızı, kesme-hızı formunun $G_s \to \Sigma$ karşılığıdır:
$$v_m = \sqrt{\frac{\Sigma}{\rho_0}}$$
2. $\rho_0 = P_0/c^2$ ikamesiyle:
$$v_m = \sqrt{\frac{\Sigma c^2}{P_0}} = c\,\sqrt{\frac{\Sigma}{P_0}}$$
3. **Gözlemsel alt sınırın çevrimi:** Bell-tipi deneyler dolanıklık koordinasyonuna $v > 10^4 c$ alt sınırı koyar (Salart ve ark., 2008). Bu doğrudan $\Sigma$'ya çevrilir:
$$\frac{v_m}{c} > 10^4 \;\Longleftrightarrow\; \frac{\Sigma}{P_0} = \left(\frac{v_m}{c}\right)^2 > 10^8$$
(Sık karışan nokta: $10^4$ hız oranıdır, $10^8$ onun karesidir.)

### Sonuç
$$\boxed{v_m = \sqrt{\frac{\Sigma}{\rho_0}} = c\,\sqrt{\frac{\Sigma}{P_0}} > 10^4\,c\,, \qquad \Sigma = P_0\left(\frac{v_m}{c}\right)^2}$$

### Geçerlilik Sınırı
$v_m$ **enerji/madde taşımaz**; ortam topografyasının (gradyan deseninin) ayar sinyalidir. GW170817 kısıtı (kütleçekim dalgaları $c$'de, $10^{-15}$ hassasiyet) sıkışma kanalını bağlar, kohezyon kanalını bağlamaz.

### Açık Uçlar
- Yanlışlanabilir öngörü: baz uzunluğu $L$ ve ayar-anahtarlama süresi $t$ için $L > v_m t$ rejiminde CHSH istatistiği $S \le 2$'ye düşmelidir (2.10.1).
- $\cos^2(a-b)$ korelasyonunun geçit mekaniğinden nicel türetimi (2.9.2.1'in nitel mekanizmasının nicelleştirilmesi; 7.4).

---

## M-6 · Hız Merdiveni Sıralama Teoremi · **[T]**

**Kullanıldığı bölümler:** Ek A (tablo), 2.4.1, 2.10.1, 7.2.

### Varsayımlar
M-1, M-3, M-4, M-5'in sonuçları.

### Adımlar
1. $\sqrt{2} > 1$ olduğundan $c < \sqrt{2}c$.
2. $\Sigma/P_0 > 10^8$ iken $v_m/\sqrt{2}c = \sqrt{\Sigma/2P_0} > 10^{3{,}5} \gg 1$, dolayısıyla $\sqrt{2}c < v_m$.
3. $\Sigma \gg P_0$ limitinde:
$$v_{kav} = \sqrt{2}c\sqrt{1+\Sigma/P_0} \;\approx\; \sqrt{2}c\cdot\sqrt{\Sigma/P_0} = \sqrt{2}\,v_m$$
yani $v_m < v_{kav} \approx \sqrt{2}\,v_m$.
4. Maddeyi *yaratan* saf alt-bileşen hızları tanım gereği yırtılma eşiğinin üzerindedir: $v_{kav} \le v_{saf}$.

### Sonuç
$$\boxed{c \;<\; \underbrace{\sqrt{2}c}_{v_{denge}\,\approx\, v_{ekvator}} \;<\; \underbrace{c\sqrt{\Sigma/P_0}}_{v_m} \;<\; \underbrace{\sqrt{2}c\sqrt{1+\Sigma/P_0}}_{v_{kav}\,\approx\,\sqrt{2}v_m} \;\le\; v_{saf}}$$

| Hız | Rolü | Değer |
|---|---|---|
| $c$ | Kavrama/patinaj sınırı **ve sıkışma kanalının ses hızı** — "Mach 1" burada mecaz değil, tam eşitliktir ($P=c^2\rho$ stiff hâl denklemi, Ek M-44) | $2{,}998\times10^8$ m/s |
| $\sqrt{2}c$ | Girdap çekirdeğinde **yoğunluğun e-katlanma hızı** ($\rho=\rho_0/e$); $\Gamma$'dan bağımsız, evrensel (M-3′) | $4{,}24\times10^8$ m/s |
| $v_m$ | Kohezyon kanalı ayar sinyali | $>10^4 c$ |
| $v_{kav}$ | Yırtılma (madde yaratma) eşiği | $\approx\sqrt{2}\,v_m$ |
| $v_{saf}$ | Alt-bileşenlerin saf dönüş hızları | $> v_{kav}$ |

### Geçerlilik Sınırı
- **Basamakların statüsü (29 Temmuz 2026'da netleşti).** Birinci basamak **tam eşitliktir**: $c$, hem Zerre'nin öteleme sınırı hem sıkışma kanalının ses hızıdır ($P=c^2\rho$, Ek M-44) — GW170817 kısıtının teoride otomatik sağlanmasının nedeni budur. İkinci basamak da **türetilmiştir**: M-3′'ün sıkıştırılabilir hesabı $\sqrt2c$'yi yoğunluğun e-katlanma hızı olarak verir ve değer $\Gamma$'dan bağımsızdır.
- **$v_{denge}\approx v_{ekvator}$ eşleşmesindeki ~%18, bir hata payı değildir.** M-3′ çekirdekte keskin duvar olmadığını, üstel bir yoğunluk profili bulunduğunu gösterir; e-katlanma noktası ($1{,}414c$) ile protonun kompozit ekvatoru ($1{,}668c$) aynı profilin iki komşu noktasıdır. İki farklı yüzey tanımının farklı hız vermesi beklenen sonuçtur.
- **Basamak aralıkları çok geniştir**, dolayısıyla sıralama teoremi tanım ayrıntılarına duyarsızdır: $v_m>10^4c$ olduğundan ikinci basamağın hangi yoğunluk kesrinde tanımlandığı sıralamayı değiştirmez.

### Açık Uçlar
- $v_{saf}$'ın nicel tahmini (yalnızca alttan sınırlı).
