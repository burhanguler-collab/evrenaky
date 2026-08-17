# Ek M — Merkezî Türetim Kataloğu · Blok G: Evrensel Sabitler ve Kozmoloji

> Şablon ve rozet sistemi için bkz. Blok A (M-1..M-6) girişi. Her türetim beş sabit başlıkla yazılır: **Varsayımlar → Adımlar → Sonuç → Geçerlilik Sınırı → Açık Uçlar.** Rozetler Ek C statü kodlarıyla ortaktır: **[T]** türetilmiş · **[S]** gözlemle sabitlenmiş · **[A]** aralıkla sınırlanmış · **[K]** kalibre edilmiş / betimleyici fit.

---

## M-28 · Kütle-İtim Katsayısının Türetimi (yerleşik adıyla "kütleçekim sabiti"): $\mathcal{G} = \alpha/\rho_n$ · **[T (yapı) / S ($\alpha$ değeri)]**

**Kullanıldığı bölümler:** 4.2.4 (ana türetim), Postülat 6 (1.3), M-2 (ivme denklemi), 4.2.9.1, Ek C satır 2 ve 12.

### Varsayımlar
1. Kütle, Evrenakı ortamında radyal simetrik bir basınç bozulumu (deplasman kuyusu) yaratır; kaynak terimsiz ($S=0$) ve yoğunluğun yaklaşık sabit kaldığı ($\rho \approx$ sabit, $k \ll 1$ rejimi) durağan bölge incelenir.
2. Cisme etkiyen kuvvet, basınç gradyanından türer ve cismin etkileşim hacmiyle orantılıdır (M-2): $\vec F = -\gamma_N \nabla P$.
3. Nükleon öz yoğunluğu $\rho_n = 2{,}7\times10^{17}$ kg/m³ evrenseldir (Postülat 4; Ek C satır 2).

### Adımlar
1. **Alan denklemi:** Kaynak terimsiz, sabit yoğunluklu durağan bölgede basınç alanı Laplace denklemini sağlar:
$$\nabla^2 P = 0$$
2. **Küresel çözüm:** Sonsuzda arka plan değeri $P_0$'a yakınsayan, küresel simetrik tek fiziksel çözüm:
$$P(r) = P_0 - \frac{\alpha M}{r}$$
Burada $\alpha$ Cosmofluid gradyan bağlaşım sabitidir; boyutu $[\text{s}^{-2}]$ (Ek D · S-2).
3. **Gradyan (kuyu konvansiyonu):** $\dfrac{\partial P}{\partial r} = +\dfrac{\alpha M}{r^2} > 0$ — basınç merkezden uzaklaştıkça artar (M-2'nin bağlayıcı işaret konvansiyonu). Kuvvetin yönü $-\hat r$'dir: cisim yüksek basınçtan alçak basınca, yani merkeze doğru **itilir**.
4. **Kuvvet:** $\vec F = -\gamma_N \nabla P = -\gamma_N \dfrac{\alpha M}{r^2}\hat r$. Burada $\gamma_N = N V_n$, $N$ nükleonlu cismin toplam etkileşim hacmidir. *(Notasyon notu — Ek D · S-8: kaynak metin 4.2.4'te bu büyüklük $\gamma$ yazılıydı; Lorentz çarpanı $\gamma$ ile karışmaması için katalog yazımı $\gamma_N$'dir.)*
5. **Cinsten bağımsızlık:** Kütle $m = N m_n$ olduğundan
$$\frac{\gamma_N}{m} = \frac{V_n}{m_n} = \frac{1}{\rho_n}$$
— oran, cismin ne olduğundan bağımsız tek evrensel sayıdır.
6. **Kuvvetin kapalı biçimi:**
$$F = \frac{\gamma_N}{m}\cdot\frac{\alpha M m}{r^2} = \frac{\alpha}{\rho_n}\,\frac{Mm}{r^2}$$
7. **Newton eşlemesi:** $F = G\,\dfrac{Mm}{r^2}$ biçimiyle birebir örtüşme, standart fiziğin $G$'sini bileşik bir büyüklük olarak tanımlar — teori yazımıyla $\mathcal{G}$.

### Sonuç
$$\boxed{\mathcal{G} = \frac{\alpha}{\rho_n}}$$

Kütleçekim sabiti $G$ (yerleşik ad), temel bir doğa sabiti değil; **ortamın bir sabiti** ($\alpha$) ile **maddenin bir sabitinin** ($\rho_n$) oranıdır — teori bu oranı $\mathcal{G}$ yazar ve onu evrensel değil **yerel** sayar (Postülat 4): ortam koşulları değiştiğinde $\mathcal{G}$ değişir, ölçülen $G$ onun Güneş Sistemi'ndeki yerel değeridir. Kütle-itimin kökeni uzaktan etki değil, ortamın basınç dağılımıdır. Galileo'nun eşit-düşme gözlemi buradan teorem olarak çıkar: $a = F/m = \mathcal{G}M/r^2$, $\rho_n$ evrensel olduğundan cisimden bağımsızdır (M-2).

**Boyut analizi:** $[\mathcal{G}] = \text{m}^3\,\text{kg}^{-1}\,\text{s}^{-2}$; sağ taraf $[\alpha]/[\rho_n] = [\text{s}^{-2}]/[\text{kg/m}^3] = \text{m}^3\,\text{kg}^{-1}\,\text{s}^{-2}$ ✓.

### Geçerlilik Sınırı
- $S=0$, $\rho \approx$ sabit ve durağanlık varsayımlarının geçerli olduğu bölgeler (Güneş sistemi ölçeği; homojen rejim). Yoğunluğun değiştiği rejimde $1/r^2$ biçimi bozulur (bkz. M-29, M-30).
- **Dürüst kayıt:** $\alpha$'nın sayısal değeri ilk ilkelerden türetilmemiştir; ölçülen $G$ üzerinden **sabitlenir** [S] (Ek C satır 12). Türetimin kazancı $G$'nin sayısını üretmek değil, $G$'nin **bileşik yapısını** (ortam sabiti / madde sabiti) ve $1/r^2$ ile eşit-düşmenin mekanik kökenini göstermektir.

### Açık Uçlar
- $\alpha$'nın Zerre-ölçeği mekaniğinden bağımsız türetimi (7.4).
- $V_n$'nin (nükleon başına etkin etkileşim hacmi) bağımsız belirlenmesi (M-2 ile ortak açık uç).

---

## M-29 · $1/r^2$ Yasasının Geometrik Kökeni (Gauss) · **[T]**

**Kullanıldığı bölümler:** 4.2.4.1 (ana metin), 4.2.4, 4.2.8 (bozulduğu rejim), M-28, M-30.

### Varsayımlar
1. İncelenen bölge kaynak terimsizdir ($S=0$) ve Evrenakı yoğunluğu homojene yakındır.
2. Uzay üç boyutludur; gradyan akısı süreklidir.

### Adımlar
1. Kaynak terimsiz bölgede $\nabla^2 P = 0$ olduğundan, herhangi bir kapalı yüzeyden geçen toplam gradyan akısı korunur (Gauss teoremi, 1813):
$$\oint_A \nabla P \cdot d\vec A = \text{sabit}$$
2. Küresel simetride bu akı $A = 4\pi r^2$ yüzeyine dağılır. Toplam akı korunduğu için:
$$|\nabla P| \cdot 4\pi r^2 = \text{sabit} \;\Longrightarrow\; |\nabla P| \propto \frac{1}{r^2}$$
3. Bu, M-28'in 2. adımındaki $P(r) = P_0 - \alpha M/r$ çözümünün geometrik yüzüdür: $1/r$ potansiyeli ile $1/r^2$ gradyanı aynı korunumun iki yazımıdır.

### Sonuç
$$\boxed{|\nabla P| \propto \frac{1}{r^2} \quad \text{(homojen, kaynaksız, 3-boyutlu bölgede)}}$$

$1/r^2$ mistik bir evrensel yasa değil, üç boyutlu uzayda akı korunumunun geometrik zorunluluğudur. Kütle-itim "uzaktan çekim" değildir; kuvvetin uzaklıkla sönümü, gradyan akısının küre yüzeyine dağılmasından ibarettir.

### Geçerlilik Sınırı
Yalnızca homojen ($\rho \approx$ sabit), kaynaksız ve küresel simetrik rejimde geçerlidir. Silindirik vorteks geometrisinde (galaktik ölçek) akı $2\pi r$ çevresine dağılır ve profil değişir — bkz. M-30. $1/r^2$'nin "bozulması" teorinin tutarsızlığı değil, geometrinin değişmesinin öngörülen sonucudur.

### Açık Uçlar
- Küreselden silindirik rejime geçiş bölgesinin (ara ölçekler) nicel modellenmesi.

---

## M-30 · Galaktik Girdap Basınç Profilleri (Rankine Bileşik Girdabı) · **[T]**

**Kullanıldığı bölümler:** 4.2.9.1–4.2.9.2 (ana metin), 4.2.8, 6.2.8, Ek C satır P1, 7.4 madde 1 ve 5.

### Varsayımlar
1. Galaktik ölçekte Evrenakı yoğunluğu yaklaşık sabittir: $\rho \approx$ sabit ($k \ll 1$ rejiminin uzantısı; gradyanlarda asıl değişen basınçtır — Yön Kuralı, 2.4.2).
2. Dönen akışkanda radyal denge siklostrofik dengedir (M-22):
$$\frac{dP}{dr} = \rho\,\frac{v_\theta^2}{r}$$
3. Galaktik vorteks, akışkanlar mekaniğinin klasik **Rankine bileşik girdabı** yapısındadır: iç bölgede katı-cisim dönüşü $v_\theta = \omega r$; geçiş yarıçapı $r_0$'ın ötesinde düz-hız bölgesi $v_\theta = v_0$.

### Adımlar
1. **İç bölge** ($r < r_0$): $v_\theta = \omega r$ yerleştirilir:
$$\frac{dP}{dr} = \rho\,\omega^2 r \;\Longrightarrow\; P(r) = P_{merkez} + \tfrac{1}{2}\rho\,\omega^2 r^2$$
— parabolik profil; basınç merkezde sonlu ve düzgündür (kuyu dibi patolojisizdir).
2. **Dış bölge** ($r > r_0$): $v_\theta = v_0$ yerleştirilir:
$$\frac{dP}{dr} = \rho\,\frac{v_0^2}{r} \;\Longrightarrow\; P(r) = P_{ref} + \rho\,v_0^2 \ln\!\left(\frac{r}{r_0}\right)$$
— logaritmik basınç kuyusu. $\rho$ sabit olduğundan her iki integral meşrudur ve iki parça $r_0$'da sürekli eklenir.
*(Notasyon notu — Ek D · S-17: buradaki $P_{ref}$, log profilin $r=r_0$'daki entegrasyon referansıdır; derin uzay arka plan basıncı $P_0$ ile **karıştırılmamalıdır**. Gövde metninde [4.2.9.2] bu referans için $P_0$ yazımı geçer; katalog yazımı $P_{ref}$'tir, gövde geçişi Faz 5'te yapılacaktır.)*
3. **Kepler tutarlılık denetimi** (4.2.9.1): Güneş sistemi rejiminde $v_\theta^2 = GM/r$ (Kepler) siklostrofik dengeye girdi olarak konursa $dP/dr = \rho\,GM/r^2$ çıkar. Dürüstlük gereği: bu bir *doğrulama* değil, **tutarlılık denetimidir** — Kepler girdi olduğundan $1/r^2$ çıktısı beklenen sonuçtur. Gösterdiği şey, siklostrofik dengenin Newton davranışıyla çelişmeden yaşayabildiğidir.
4. **Gözlemle karşılaştırma — ve statüsünün dürüst kaydı.** Gözlenen galaktik dönüş eğrileri tam bu bileşik deseni çizer: içte hız $r$ ile yaklaşık doğrusal yükselir, $r_0$ civarında kırılıp düzleşir. Standart fizik iki kolu iki ayrı bileşenle (baryonik disk + karanlık madde halesi) fit etmek zorundadır; bileşik girdapta ikisi tek yapının iki bölgesidir — **kavramsal ekonomi buradadır.**

   *(Statü uyarısı — bu bir "bedava öngörü" **değildir**: düz kol Varsayım 3'te $v_\theta=v_0$ olarak **girdi alınmıştır**, dolayısıyla çıktısının düz olması beklenen sonuçtur. 3. adımın Kepler için uyguladığı ölçüt burada da geçerlidir; ikisi aynı döngüdür.)*

5. **Düz kolun gerçek türetimi M-38+M-37 zinciridir.** Bu girdi Rankine profilini varsayar; ama teori düz eğriyi **türetebilir** ve o yol buradan geçmez:
$$\underbrace{h=\text{sabit}}_{\text{M-38 Varsayım 3}}\;\Rightarrow\;\underbrace{a\propto1/R}_{\text{silindirik akı}}\;\Rightarrow\;\underbrace{v_\theta=\sqrt{R|a|}=v_0}_{\text{M-37 profil teoremi}}$$
   Düz dönüş eğrisinin öngörü statüsü kazanması bu zincire bağlıdır; bu girdinin katkısı ise **basınç profilini** (logaritmik kuyu) ve iki kolun tek yapıda birleşmesini vermektir. Zincirin dayandığı $h_d=$ sabit koşulu ayrıca yanlışlanabilir bir sonuç doğurur: diskler dışa doğru kalınlaştığından (enjeksiyon kalınlığı $h_{inj}(R)$ artar) dönüş eğrisi büyük $R$'de düzlükten **sapmalıdır** — $h_{inj}(R)$ ile dönüş eğrisinin ortak fiti (M-38).

### Sonuç
$$\boxed{P(r) = \begin{cases} P_{merkez} + \tfrac{1}{2}\rho\,\omega^2 r^2\,, & r < r_0 \quad (v_\theta = \omega r) \\[4pt] P_{ref} + \rho\,v_0^2 \ln(r/r_0)\,, & r > r_0 \quad (v_\theta = v_0) \end{cases}}$$

**Rejim tablosu — tek denklemin üç yüzü:**

| Ölçek | Hız profili | Kuvvet/gradyan davranışı | Gözlemsel karşılık |
|---|---|---|---|
| Güneş sistemi (homojen, küresel) | $v_\theta^2 = GM/r$ | $1/r^2$ | Kepler yasaları |
| Galaktik iç bölge ($r<r_0$) | $v_\theta = \omega r$ | $F \propto r$ | Dönüş eğrisinin doğrusal kolu |
| Galaktik dış bölge ($r>r_0$) | $v_\theta = v_0$ | $F \propto 1/r$ | Düz dönüş eğrisi (karanlık maddesiz) |
| Kozmolojik | $\vec v = H_0 \vec r$ | $v \propto r$ | Hubble akışı (M-31) |

### Geçerlilik Sınırı
- Logaritmik profil $r \to \infty$'da ıraksar; fiziksel olarak profil galaktik ölçekle sınırlıdır. Dış kesimde arka plan basıncı $P_0$'a bağlanma (kesim yarıçapı) modellenmemiştir — bkz. Açık Uçlar.
- $\rho \approx$ sabit varsayımı P1 çalışma hipotezidir (Ek C satır P1); yoğunluk profili değişirse integraller yeniden alınmalıdır.

### Açık Uçlar
- **Kesim yarıçapı:** Log kuyunun dış kesimde $P_0$'a nasıl bağlandığı (profilin kapanışı) modellenmemiştir.
- $r_0$ **türetilmiştir** (Ek M-38, 3 Ağustos 2026): $r_0=\sqrt{\mathcal{G}M/a_0}=\ell_\omega^{etkin}$, iki kanalın ivmesinin kesişiminden; onunla birlikte $v_0^2=A_4=\sqrt{\mathcal{G}Ma_0}$ de kapanır. İkisi de artık serbest kalem değildir ve Ek C'de **satır 21 [T]** olarak kayıtlıdır. *(Önceki kayıt bunları P1'e bağlayıp serbest sayıyordu.)* P1'in kalan içeriği yalnız yoğunluk profilinin biçimidir.

---

## M-31 · Hubble Bağıntısı: $H_0 = S_{kozmik}/3\rho$ · **[T]**

**Kullanıldığı bölümler:** 4.2.11.1 (ana metin), 3.7.2 (deşarj mekanizması), Ek C satır 13.

### Varsayımlar
1. Kozmik ölçekte Evrenakı korunumu süreklilik denklemiyle yazılır; global bir kaynak terimi $S_{kozmik}$ (evrensel deşarj; 3.7.2) vardır.
2. Hubble akışı gözlemsel girdidir (Hubble, 1929): $\vec v = H_0 \vec r$.
3. Evrenakı yoğunluğu global ölçekte kararlı durumdadır: $\partial\rho/\partial t \approx 0$.

*(Yazım notu: kaynak metinde ve Ek C çizelgesinde $S_{kosmik}$ yazımı geçer; katalog tek yazımı $S_{kozmik}$'tir.)*

### Adımlar
1. Süreklilik denklemi:
$$\frac{\partial \rho}{\partial t} + \nabla\cdot(\rho\vec v) = S_{kozmik}$$
2. Hubble hız alanının diverjansı:
$$\nabla\cdot\vec v = \nabla\cdot(H_0\vec r) = 3H_0$$
3. Kararlı durum ($\partial\rho/\partial t \approx 0$) ve $\rho \approx$ sabit ile:
$$3\rho H_0 = S_{kozmik}$$

### Sonuç
$$\boxed{H_0 = \frac{S_{kozmik}}{3\rho} \qquad\Longleftrightarrow\qquad S_{kozmik} = 3\rho_0 H_0}$$

Hubble sabiti $H_0$, mistik bir "metrik genişleme" oranı değil; Evrenakı'nın global hacimsel kaynak/deşarj teriminin mekanik ölçüsüdür. Ters okuma Ek C satır 13'ün sabitleme kaydıdır: $S_{kozmik} = 3\rho_0 H_0$, ölçülen $H_0$ üzerinden sabitlenir [S].

### Geçerlilik Sınırı
- Türetim kararlı durum ($\partial\rho/\partial t \approx 0$) ve global homojenlik varsayar; yerel (galaktik/küme) ölçekte $H_0$ akışı bu denklemin konusu değildir.
- $\vec v = H_0\vec r$ **gözlemsel girdidir**; teori bu hız alanını türetmez, mekanik karşılığını verir.

### Açık Uçlar
- $S_{kozmik}$'in içsel deşarj mekanizmasından ($\kappa_d$; 3.1.8, 3.7.2) bağımsız türetimi — şu an yalnızca $H_0$ üzerinden sabitlenmektedir.
- İvmelenen genişlemenin (basınç gevşemesi senaryosu, 4.2.11.2) nicelleştirilmesi (7.4).

---

## M-32 · Kromatik Merceklenme Parametrizasyonu · **[K]**

**Kullanıldığı bölümler:** 4.3.4–4.3.5 (ana metin), 6.5 (kanıt taksonomisi), 7.4 (açık işler).

### Varsayımlar
1. Merceklenme, uzay-zaman eğriliği değil, kütle çevresindeki Evrenakı gradyanında hidrodinamik optik kırılmadır; yerel ışık hızı $c_0 = \sqrt{P/\rho}$ konuma göre değişir.
2. Kırılma bir ortam olayı olduğundan **kromatik** olmak zorundadır: farklı frekanslı Zerre katarları farklı patinaj yapar, sapma renge bağlıdır. (Standart görelilikte sapma akromatiktir; fark çift taraflı bir ayrım testidir.)

### Adımlar
1. Sapma açısının dalga boyuna bağlılığı, referans dalga boyu $\lambda_0$ çevresinde doğrusal parametrize edilir:
$$\theta(\lambda) = \theta_0\left[1 + \chi\,\frac{\lambda - \lambda_0}{\lambda_0}\right]$$
Girdiler: $\theta_0 = 1{,}75''$ ($\lambda_0 = 550$ nm, Güneş teğet sınırı); $\chi = 5\times10^{-4}$ (boyutsuz, **fenomenolojik** dispersiyon katsayısı).
2. Sayısal değerlendirme:
$$\theta_{mavi}(450\text{ nm}) = 1{,}749841''\,, \qquad \theta_{kırmızı}(650\text{ nm}) = 1{,}750159''$$
3. Fark:
$$\Delta\theta = \theta_{kırmızı} - \theta_{mavi} = 0{,}000318'' = 318\ \mu\text{as}$$

### Sonuç
$$\boxed{\theta(\lambda) = \theta_0\left[1 + \chi\,\frac{\lambda-\lambda_0}{\lambda_0}\right]\,, \qquad \Delta\theta(450\text{–}650\text{ nm}) = 318\ \mu\text{as}}$$

Standart görelilikte bu fark tam sıfırdır; sıfırdan farklı herhangi bir kromatik sapma ölçümü ayrım gücü taşır. Kuazar mikro-merceklenme boyut anomalisinin (4.3.4) çözümü de aynı parametrizasyonun geriye dönük uygulamasıdır.

### Geçerlilik Sınırı
- **Bu bir parametrizasyondur, türetim değildir** — rozet bu yüzden [K]'dir. $\chi$, gradyan mekaniğinden hesaplanmamış; fenomenolojik olarak konmuştur. 6.7 taksonomisinde statüsü **kalibrasyon**dur; "kanıt" statüsü ancak $\chi$ bağımsız kalibre edildikten sonra ileriye dönük testle kazanılabilir. Bölümün mevcut kanıt değeri niteldir: öngörünün *kromatik olması* (GR'de özdeş sıfır).
- Doğrusal biçim, $|\lambda-\lambda_0|/\lambda_0 \lesssim O(1)$ görünür bant çevresinde geçerli yerel açılımdır.

### Açık Uçlar
- $\chi$'nin gradyan mekaniğinden (patinaj/dispersiyon dinamiğinden) ilk-ilkelerle türetimi ve bağımsız kalibrasyonu (7.4).
- ~~$\theta_0 = 1{,}75''$ değerindeki **2× faktörünün** Evrenakı mekaniğinden nicel türetimi (analojik argüman düzeyinde)~~ → **güncellendi (17 Ağustos 2026):** 2× artık analojik değil, ölçek yapısının sonucudur — $c_{loc}=c_0\Lambda^2 \Rightarrow n_{eff}=1+2\Phi/c_0^2$ (**Ek M-42**; bükülme ölçümüyle sabitlenmiştir). Açık kalan, $\Lambda$ üslerinin mikro-mekanik türetimidir (M-42 Açık Uçlar).
- Gaia kromatiklik kalibrasyon artıklarında $318\ \mu$as imzasının aranması (ileriye dönük test).

---

## M-33 · Fiber İçi Işık Hızı Ölçüm Hesabı · **[S]**

**Kullanıldığı bölümler:** 5.2.9.2 (ana metin), 5.2.8.1 (yankı analojisi), 5.2.10–5.2.12 (yöntem ve bulgular), 7.4 madde 11.

### Varsayımlar
1. Fiber osilatör, yankı döngüsü ilkesiyle çalışır: ışığın fiberdeki uçuş süresi + elektroniğin tepki süresi, kendi kendini besleyen bir açma-kapama döngüsünün periyodunu belirler.
2. Fiber boyu $l$ ve elektronik tepki süreleri ($t_r$, $t_f$) sabittir; frekans değişimi yalnızca fiber içi ışık hızındaki değişimi yansıtır.

*(Notasyon notu — Ek D · S-15/S-16: kaynak metin 5.2.9.2'de fiber içi hız $C$, osilatör frekansı $f$ yazılıydı; katalog yazımı $c_f$ (fiber içi hız) ve $\nu_{osc}$ (osilatör frekansı)'tır.)*

### Adımlar
1. **Döngü denklemi:** Bir osilasyon turunun süresi = uçuş süresi + devre tepkisi:
$$\frac{1}{\nu_{osc}} = \frac{l}{c_f} + t_r + t_f$$
2. **Ters çözüm** ($c_f$ için):
$$c_f = \frac{\nu_{osc}\, l}{1 - \nu_{osc}(t_r + t_f)}$$
3. **Girdiler** (HFBR-53A5VEMZ veri sayfası + düzenek): $l = 30{,}63$ m; $t_r = t_f = 6$ ns (3 ns × 2 kenar); $\nu_{osc} = 5.472.870$ Hz.
4. **Hesap:**
- Pay: $\nu_{osc}\,l = 5.472.870 \times 30{,}63 = 167.634.008$ m
- Payda: $1 - 5.472.870 \times 12\times10^{-9} = 0{,}93432556$ (boyutsuz)
$$c_f = \frac{167.634.008}{0{,}93432556} \approx 1{,}794\times10^8 \text{ m/s}$$

### Sonuç
$$\boxed{c_f = \frac{\nu_{osc}\, l}{1 - \nu_{osc}(t_r + t_f)} \approx 1{,}794\times10^8 \text{ m/s}}$$

Deneyin amacı bu mutlak değer değil, **değişimlerin** izlenmesidir: $l$, $t_r$, $t_f$ sabitken her frekans değişimi doğrudan $c_f$ değişimidir. Düzenek çözünürlüğü $\Delta\nu \approx 1$ Hz karşılığı **35 m/s**'dir (payda karesi dahil tam duyarlılık; kaba $c_f/\nu_{osc}$ yaklaşımı 33 verir); raporlanan ~4500 m/s'lik kütle etkisi (5.2.11) bu gürültü tabanının ~128 katıdır.

### Geçerlilik Sınırı
- Hesap, tüm devre gecikmesinin veri sayfası $t_r + t_f$ değerlerinden ibaret olduğunu varsayar; sistematik ek gecikmeler mutlak $c_f$ değerini kaydırır fakat *değişim* ölçümünü etkilemez.
- **Dürüst kayıt:** Karşılık gelen etkin kırılma indisi $n = c_0/c_f \approx 1{,}67$, standart fiber camının $1{,}46$–$1{,}50$ aralığının **üzerindedir**. Olası nedenler: hesaba girmeyen ek elektronik gecikme (yükselteç/algılama katları) veya etkin olmayan kablo boyu. Bu fark, mutlak değerin değil değişim ölçümünün kanıt taşıdığının ayrıca gerekçesidir.

### Açık Uçlar
- $n \approx 1{,}67$ fazlalığının kaynak tayini: ek gecikme kalemlerinin bağımsız ölçümü (ör. kısa-fiber kalibrasyonu ile devre gecikmesinin ayrıştırılması).
- Sıcaklık-kontrollü tekrar ve taban kayması kaynak tayini programı (7.4 madde 11; D-23 kararı).

---

## M-34 · Parametre Envanteri (Ek C Çapraz Referansı) · **[—]**

**Kullanıldığı bölümler:** Ek C (Kısım 1, Bölüm 1.3 sonu), Ek C.1 (dürüst sayım), 7.4 (sabitleme programı), bu kataloğun tüm rozetleri.

Bu girdi bir türetim değil, **yönlendirme kaydıdır.** Teorinin 21 skaler + 2 profil satırlık tam statü çizelgesi (T/S/A/F/G kodları, değerler ve her serbest parametreyi sabitleyecek gözlem) **Ek C**'dedir.

**Dürüst sayım (Ek C.1):** Gerçekten serbest kalem **5 skaler** ($\Sigma$'nın tam değeri, $n$, $\kappa_d$, $\tau$, $\delta$) **+ 2 profil fonksiyonu** ($\rho(r)$ galaktik profili, Rampa profili). *(28–29 Tem 2026: $\eta_E$ → $n$ — Ek M-43 boyutlu viskozite katsayısını boyutsuz bastırma üssüne çevirdi; **$k$ listeden çıktı** — Ek M-44 iki değişkenli hâl denklemiyle $k=0$'ı türetti; $\xi$ [S]→[T] — Ek M-40. Toplam 6 → 5.)* Karşılaştırma: Standart Model 19'dan fazla serbest parametre taşır; ΛCDM kozmolojisi bunlara 6 parametre daha ekler. Sayı azlığı avantaj *adayıdır*, kanıt değildir — avantaja dönüşmesi Ek C'nin son sütunundaki sabitleme programının yürütülmesine bağlıdır.

Bu katalogdaki **[T]/[S]/[A]/[K]** rozetleri Ek C'nin statü kodlarıyla ortak dildedir. Her M-girdisinin dayandığı serbest parametreler, o girdinin kendi **Geçerlilik Sınırı / Açık Uçlar** bölümünde kayıtlıdır (bu blokta örn.: M-28 → $\alpha$ [S, Ek C satır 12]; M-30 → $\rho(r)$ profili [F, Ek C satır P1] — $r_0$ artık **türetilmiştir** [T, Ek C satır 21, M-38], $v_0$ genlik çapası [A]; M-31 → $S_{kozmik}$ [S, Ek C satır 13]; M-32 → $\chi$ [K, fenomenolojik]).
