# 4.2 Evrenakı'nın Matematiksel Modeli — I: Temel Model ve G'nin Türetimi (4.2.1–4.2.4)

Klasik mekanik, yüzyıllardır kütleçekimini $1/r^2$ ile sönümlenen evrensel bir kuvvet olarak kabul etmektedir. Evrenakı teorisinin amacı ise, bu ampirik gözlemi akışkanlar dinamiği temelleri üzerinden, "uzaktan anında etki" (action-at-a-distance) varsayımına başvurmadan türetebilmektir.

Bu bölümde, evrenin temel yapısını açıklamak amacıyla önerilen *Cosmofluid* yaklaşımının ilk matematiksel modeli, klasik alan teorilerinden ve akışkanlar mekaniğinden ilham alınarak kurulacaktır. Amaç, gözlenen kuvvetlerin fiziksel bir ortamın (Evrenakı'nın) hidrodinamik özelliklerinden doğal bir sonuç olarak ortaya çıktığını göstermektir.

## Ön Kavramsal Çerçeve: Evrenakı'nın Kütleyle Etkileşim Mekanizması

Aşağıdaki hidrodinamik denklemlere ve matematiksel ispatlara geçmeden önce, klasik mekaniğin en büyük eksikliklerinden birini gidermek ve Evrenakı'nın madde ile **nasıl** temas ettiğini fiziksel olarak tanımlamak gereklidir. Okuyucu, haklı olarak "Bu akışkan, içindeki kütleleri (örneğin bir gezegeni veya elmayı) fiziksel olarak nasıl tutuyor ve itiyor?" sorusunu sorabilir.

Daha önceki kısımlarda detaylandırıldığı üzere, etkileşimin temeli şu mekanik gerçeklere dayanır:

1. **Katı Duvar Yanılgısı (Porozite):** Atomik ve alt-atomik dünyada aşılmaz, mutlak "katı" yüzeyler yoktur. Gezegenler de dahil olmak üzere tüm maddeler, aralarında devasa boşluklar bulunan atomik ızgaralardan (grid) oluşur. Evrenakı, bu atomik boşlukların içinden, rüzgârın bir ağacın dalları arasından sızması gibi süzülür.
2. **Mikro-Sürtünme ve Spin:** Maddeyi oluşturan trilyonlarca alt-atomik parçacık sürekli bir dönüş (spin) halindedir. Bu dönüş, maddenin içinden geçen Evrenakı akışkanında lokal "viskoz sınır tabakaları" ve sayısız mikro-girdap yaratır. 
3. **Kümülatif Makro-Etki:** Tek tek her bir atomun Evrenakı ile girdiği bu mikro-sürtünmeler ve girdaplar birleşerek, Dünya gibi devasa bir cismin etrafında bütünsel ve devasa bir makro-girdap (vorteks) inşa eder. 

Kısacası Evrenakı maddeyi uzaktan soyut bir çekim kuvvetiyle hareket ettirmez; maddenin içindeki trilyonlarca dönen mikro-kütleye hidrodinamik olarak temas eder ve bu kümülatif mikro-sürtünme sayesinde kütleyi makro ölçekte sürükler, iter veya döndürür. İşte aşağıda detaylandırılacak olan Euler denklemleri, Basınç Gradyanları ($\nabla P$) ve kütle-itim formülleri, havada asılı duran soyut matematiğin değil, bu somut hidrodinamik temasın doğrudan makroskobik sonucudur.

## Sembol Tablosu (4.2 Bölümleri — I'den IV'e — İçin)

| Sembol | Anlamı | İlk geçtiği yer |
|--------|--------|------------------|
| $\rho$ | Evrenakı (Cosmofluid) yoğunluk alanı | 4.2.1 |
| $\vec{v}$ | Evrenakı hız alanı | 4.2.1 |
| $P$ | Evrenakı basınç alanı | 4.2.1 |
| $P_0$ | Derin uzaydaki (arka plan) maksimum basınç (eski yazım: metnin önceki sürümlerinde $P_\infty$ da kullanılıyordu; tek sembolde birleştirildi) | 4.2.3–4.2.4 |
| $S(x,t)$ | Süreklilik denklemindeki kaynak/kuyu terimi | 4.2.2 |
| $M$, $m$ | Merkezi kütle ve test kütlesi | 4.2.4 |
| $\alpha$ | Cosmofluid potansiyel sabiti (boyutu $[\text{s}^{-2}]$) | 4.2.4 |
| $\gamma_N$ | Cismin akışkanla aerodinamik etkileşim katsayısı ($\gamma_N = N V_n$) (eski yazım: $\gamma$; Kısım 6'daki Lorentz çarpanı $\gamma$ ile karışmaması için $\gamma_N$) | 4.2.4 |
| $N$, $V_n$, $m_n$ | Nükleon sayısı, tekil nükleon etkileşim hacmi ve kütlesi | 4.2.4 |
| $\rho_n$ | Nükleon öz yoğunluğu ($m_n / V_n$) | 4.2.4 |
| $\mathcal{G} = \alpha/\rho_n$ | Türetilen **yerel** kütle-itim katsayısı (yerleşik adıyla kütleçekim "sabiti" $G$) | 4.2.4 |
| $J_2$ | Dünya'nın basıklık (kütle dağılımı) katsayısı | 4.2.7 (Bölüm II) |
| $v_\theta$ | Teğetsel (dönüş) hızı | 4.2.9 (Bölüm III) |
| $H_0$ | Hubble sabiti | 4.2.11 (Bölüm III) |
| $\chi$ | Dispersiyon katsayısı (merceklenmede frekansa bağlı sapma) | 4.3 |

## 4.2.1 Cosmofluid Alan Tanımları (Kinematik)
Evrenakı (Cosmofluid), her noktada tanımlı sürekli bir ortamdan oluşur ve makroskopik ölçekte kusursuz bir akışkan gibi modellenir. Cosmofluid uzayda üç temel alan (field) ile tanımlanır:
- **Yoğunluk Alanı:** $\rho = \rho(x,t)$
- **Hız Alanı:** $\vec{v} = \vec{v}(x,t)$
- **Basınç Alanı:** $P = P(x,t)$

Bu alanlar, klasik akışkanlar mekaniğinde kullanılan büyüklüklerle doğrudan analojiktir. Farkı ise, Evrenakı'nın içinde maddelerin yüzdüğü bir okyanus değil, uzayın ta kendisi olmasıdır.

## 4.2.2 Süreklilik Denklemi (Kütle Korunumu)
Madde, uzayda sadece duran pasif bir nesne değildir; Cosmofluid içerisinde sürekli bir hidrodinamik bozulma (deplasman) yaratır. Akışkanlar mekaniğinde ortamın korunumu **Süreklilik (Continuity) Denklemi** ile ifade edilir:
$$ \frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \vec{v}) = S(x,t) $$

Buradaki $S(x,t)$ madde kaynak/kuyu (source/sink) terimidir. Ancak Evrenakı modelinde madde, uzay dokusunu sihirli bir şekilde "yok etmez" (yutmaz) veya "hiçlikten üretmez". Tıpkı ağzına kadar dolu bir havuza atılan devasa bir taşın kendi hacmi kadar suyu dışarı itmesi gibi, gezegenler ve yıldızlar da uzayda işgal ettikleri devasa kütle-hacim ile Evrenakı akışkanını dışarı doğru **deplase eder (öteler).** Madde tarafından yerinden edilen bu akışkan, uzayın o bölgesinde muazzam bir hidrodinamik gerilim ve basınç gradyanı (yoğunluk farkı) yaratır. Kütlenin büyüklüğü, ötelediği (deplase ettiği) Evrenakı miktarını belirler; bu da klasik mekaniğin "kütleçekim alanı" zannettiği o etki alanının (hidrodinamik basınç boşluğunun) ta kendisidir.

## 4.2.3 Euler Formülasyonu ve Deplasman Etkisi
Normal bir akışkanın hareketini modelleyen temel denklem Navier-Stokes denklemidir (Navier, 1823; Stokes, 1845). Ancak gezegenlerin yörüngelerinde milyarlarca yıl boyunca hız kaybetmeden hareket edebilmesi, uzayı dolduran bu ortamın klasik bir sürtünme (drag) yaratmadığını gösterir. Bu gözlem, Evrenakı'nın elektromanyetik dalgaları hissedilir biçimde zayıflatmadan taşıyabilen **ultra-akışkan (superfluid)** (Landau, 1941) karakteristiğine sahip olduğunu zorunlu kılar. Buradaki "ultra-akışkan" nitelemesi viskozitenin **sıfıra çok yakın** olduğunu söyler; *tam sıfır* olduğunu söylemez. Aşağıda viskozite terimlerinin düşürülmesi, hesabı kapalı forma getiren bir **idealleştirme limitidir** ($\mu \to 0^+$): sönüm ve deşarj süreçleri hesaba katıldığında sonlu $\eta_E$ terimi denkleme geri konur (bkz. Bölüm 1.3, 7. postülat kutusu; Bölüm 3.7.2 ve 3.10.4.2).

Kinematik viskozite sıfıra çok yakın olduğundan ($0 < \mu \ll 1$), viskozite terimleri **bu ölçekte** ihmal edilebilir ve Evrenakı'nın momentum dengesini tanımlayan **Euler Denklemi** (Euler, 1757) ortaya çıkar:

$$ \rho \left( \frac{\partial \mathbf{v}}{\partial t} + (\mathbf{v} \cdot \nabla)\mathbf{v} \right) = -\nabla P $$

Bu denklemin sağ tarafı, hareketi dikte eden **Basınç Gradyanını ($-\nabla P$)** ifade eder. Göksel hareketlerin ve yörünge dinamiklerinin itici gücü bu basınç gradyanı vektörüdür.
Kütle (örneğin Güneş), kendi hacmiyle Evrenakı ortamını dışarıya doğru iter (Deplasman Etkisi). Bu durum, yıldızın merkezinde bir Evrenakı seyrelmesi yaratırken, derin uzayda maksimum arka plan basıncı ($P_0$; eski yazım: $P_\infty$) oluşturur.

## 4.2.4 "Kütleçekim Sabiti" ($G$)'nin Doğası: Basınç Alanı Çözümü ve Yerel $\mathcal{G}$
*(Bu türetim, katalogda **M-28** olarak numaralanmıştır; boyut analizi ve kuyu-konvansiyonlu yazımı için oraya bakınız.)*

Kütlenin uzayda yarattığı "Deplasman Etkisi", Evrenakı akışkanında radyal bir hız/batış alanı oluşturur. Merkezi ve tekil bir kütle ($M$), çevresindeki Cosmofluid ortamında simetrik ve radyal bir basınç bozulumu yaratır.

Klasik fizikte gözlemsel verilere (Kepler yasalarına; Kepler, 1619) dayalı olarak başarıyla tespit edilen ters kare yasasının ($1/r^2$) altında yatan fiziksel mekanizmayı, Cosmofluid modelinde boş uzayın geometrik ve hidrodinamik zorunluluklarından doğrudan türetebiliriz. Madde kaynaklarının olmadığı ($S = 0$) ve Evrenakı yoğunluğunun lokal olarak sabit kaldığı ($\rho \approx$ sabit) durağan uzay bölgelerinde, akışkanın basınç alanı Laplace denklemini (Laplace, 1799) sağlamak zorundadır:
$$ \nabla^2 P = 0 $$

Küresel simetride bu diferansiyel denklemin fiziksel olarak anlamlı (sonsuzda sabit bir $P_0$ değerine yakınsayan) tek çözümü şöyledir:
$$ P(r) = P_0 - \frac{\alpha M}{r} $$

Burada $P_0$ derin uzaydaki (arka plan) maksimum Evrenakı basıncını, $\alpha$ ise Cosmofluid ortamının potansiyel sabitini ifade eder. Bu formül, salt teorik bir varsayım değil, üç boyutlu uzayın geometrik korunum yasalarının doğrudan sonucudur.
Bu basınç alanının gradyanını alırsak, merkeze doğru iten vektörel basıncı buluruz:
$$ \nabla P = \frac{\alpha M}{r^2} $$

Sistemdeki bir test parçacığının (örneğin gezegenin) Cosmofluid ile aerodinamik etkileşim/sürtünme (drag) katsayısına $\gamma_N$ dersek (eski yazım: $\gamma$; Kısım 6'daki Lorentz çarpanı $\gamma$ ile karışmaması için $\gamma_N$), parçacığa etkiyen kuvvet doğrudan bu basınç gradyanından türer ($\vec{F} = - \gamma_N \nabla P$):
$$ \mathbf{F} = -\gamma_N \frac{\alpha M}{r^2} \mathbf{\hat{r}} $$

Burada nesnenin efektif aerodinamik kesit/sürtünme katsayısı $\gamma_N$, onu oluşturan nükleonların (proton/nötron) toplam etkileşim hacmiyle doğru orantılıdır ($\gamma_N = N V_n$). Nesnenin kütlesi ise nükleon sayısı ile tekil nükleon kütlesinin çarpımıdır ($m = N m_n$). Dolayısıyla sürtünme katsayısının cismin kütlesine oranı, nükleon öz yoğunluğunun ($\rho_n = m_n / V_n$) tersine eşittir:
$$ \frac{\gamma_N}{m} = \frac{V_n}{m_n} = \frac{1}{\rho_n} $$

**Newton Limiti ve G Sabiti:**
Bu bağıntıyı yerleştirirsek, parçacığa etkiyen kuvvet:
$$ F = \left(\frac{\gamma_N}{m}\right) \frac{\alpha M m}{r^2} = \frac{\alpha}{\rho_n} \frac{M m}{r^2} $$
Bu denklem, Newton'un ünlü evrensel kütleçekim formülüyle ($F = G \frac{M m}{r^2}$) birebir örtüşür. Buradan, klasik kütleçekim sabitinin ($G$) teorideki karşılığı tanımlanır — teori yazımıyla $\mathcal{G}$:
$$ \mathcal{G} = \frac{\alpha}{\rho_n} $$

Bu sonuca göre, fizikte evrensel ve temel bir sabit olarak kabul edilen $G$, aslında Cosmofluid'in arka plan potansiyel sabiti ($\alpha$) ile baryonik maddenin (nükleonun) evrensel öz yoğunluğunun ($\rho_n$) oranıdır. [^3] Pay ortamın, payda maddenin sabitidir; ortam koşulları değiştiğinde $\mathcal{G}$ de değişir — teoride evrensel bir sabit değil, **yerel bir büyüklüktür** (Postülat 4). Güneş Sistemi'nde ölçülen $G$, $\mathcal{G}$'nin buradaki yerel değeridir. Kütle-itimin kökeni "uzaktan etki" değil, bizzat ortamın dinamik basınç dağılımıdır. Bu durum, Galileo'nun meşhur serbest düşme yasasını mekanik olarak açıklar: Cisimlerin ivmesi ($a = F/m = \mathcal{G} M/r^2$), kütlelerinden bağımsız olarak nükleon yoğunluğu ($\rho_n$) sabit olduğu için hepsi için eşittir.

[^3]: **Boyutsal Analiz Notu:** Newton mekaniğinde $G$ sabitinin birimi $[\text{m}^3 \text{ kg}^{-1} \text{ s}^{-2}]$'dir. Evrenakı modelinde $P(r) = P_0 - \frac{\alpha M}{r}$ denkleminden türetilen potansiyel sabiti $\alpha$'nın boyutu $[\text{s}^{-2}]$, nükleon öz yoğunluğu $\rho_n$'in boyutu ise $[\text{kg/m}^3]$'tür. Bu iki fiziksel parametrenin oranı ($\mathcal{G} = \alpha / \rho_n$), klasik kütleçekim sabitinin birimini ($[\text{m}^3 \text{ kg}^{-1} \text{ s}^{-2}]$) kusursuz şekilde sağlar.

### 4.2.4.1 1/r² Davranışı ve Gauss Teoremi
Modern fizikte $1/r^2$ sönümlemesi evrensel bir yasa olarak görülürken, Evrenakı modelinde bu durum yalnızca belirli koşullar sağlandığında ortaya çıkan geometrik bir zorunluluktur. Güneş Sistemi ölçeğinde yoğunluk ($\rho$) homojene yakın kabul edilebilir. Homojen bir ortamda, dışarı yayılan basınç akısı, Gauss teoremi (Gauss, 1813) gereği $A = 4\pi r^2$ yüzey alanına dağılır. Toplam akı korunduğu için, gradyan $1/r^2$ oranında azalmak zorundadır. Bu davranış mistik bir yasa değil, homojen Evrenakı'nın 3-boyutlu dağılımının doğal sonucudur. *(katalog: **Ek M-29**)*

