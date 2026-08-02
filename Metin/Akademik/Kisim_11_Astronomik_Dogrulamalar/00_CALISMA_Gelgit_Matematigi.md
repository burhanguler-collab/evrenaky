# ÇALIŞMA DOSYASI — Gelgit Matematiği (11.1 / M-36)

> [!WARNING]
> **Bu bir yayın bölümü değildir.** Site menüsüne (`app.js`) kayıtlı değildir ve kayıtlı
> olmayacaktır. Kısım 11'in çalışma tezgâhıdır.
>
> **Dosyanın varlık sebebi:** Kısım 8 (Ekler / Ek M) ve Kısım 10 (Yörünge Doğrulaması)
> yazmaya kapalıdır; yalnız yazarın her seferinde vereceği özel izinle değiştirilebilir.
> Bu nedenle M-36'nın yeniden türetimi ve Ek M'de yapılması *önerilen* her değişiklik
> **önce buraya kopyalanır ve burada işlenir.** Onay gelirse tek seferde asıl dosyaya taşınır;
> gelmezse burada kayıt olarak durur.
>
> **Statü:** Bölüm 2 türetimi tamamlandı ve sayısal olarak denetlendi (Bölüm 3).
> Bölüm 5'teki iki karar yazarı bekliyor.

---

## 0. Kapsam ve kurallar

| | |
|---|---|
| **Hedef bölüm** | 11.1 Diferansiyel Sıkıştırma: Gelgit Tensörü ve Denge Gelgiti |
| **İlgili katalog girdisi** | Ek M-36 (Blok H) — *dokunulmaz*, kopyası Bölüm 1'de |
| **Yan katalog girdileri** | M-26 (hidrostatik top), M-35 (radyal kütle-itim) — *dokunulmaz* |
| **Yazılabilir dosya** | yalnız `Kisim_11_.../01_Denge_Gelgiti_ve_Tensor_Matematigi.md` ve bu dosya |
| **İzin gerektiren** | Bölüm 4'te listelenen her kalem |

**Tespit edilen asıl sorun.** Yayındaki 11.1, Ek M-36'nın ~%85 birebir kopyasıdır. Kısım 11'e
kadar gelen okur yeni hiçbir şey almamaktadır; üstelik türetim yapılmamış, **sonuç yazılmıştır.**
Bu çalışmanın amacı 11.1'i gerçek bir türetime çevirmektir. **Hiçbir sayısal sonuç değişmez**
(Bölüm 3 bunu doğrular); değişen, sonuçların nereden geldiğidir.

---

## 1. ARŞİV — Ek M-36'nın birebir kopyası

> Aşağısı `Kisim_8_Ekler/18_5_Kuvvet_Matematigi.md` satır 87–162'nin değiştirilmemiş
> anlık görüntüsüdür. **Karşılaştırma referansıdır; burada düzenlenmez.**
> Düzenlenmiş sürüm Bölüm 2'dedir.

<details>
<summary>M-36 · Gelgit Tensörü ve Denge Gelgiti · [T] — orijinal metin</summary>

**Kullanıldığı bölümler:** 3.2.1 (Kuvvet 2), 3.9.2–3.9.2.2. Bağlı katalog: M-26 (hidrostatik tepki tarafı), M-35.

**Kilit tez:** Kuvvet 2 bağımsız bir kuvvet değildir; **M-35'in uzaysal türevidir.** Gelgit hiçbir yeni parametre gerektirmez.

**Varsayımlar**

1. M-35'in alanı geçerlidir: $P(r)=P_0-\alpha M/r$, dolayısıyla $a_r=-\mathcal{G}M/r^2$.
2. Test cismi noktasal değil, yarıçapı $b\ll r$ olan uzanımlı gövdedir.
3. Kaynaktan uzakta ortam kaynaksızdır: $\nabla^2 P=0$ (M-28 Varsayım 1).

**Adımlar** — Gövde merkezi $r$'de, gövde üzerindeki nokta merkezden $\vec\xi$ kadar uzakta olsun:

$$\Delta a_i(\vec\xi) = \frac{\partial a_i}{\partial x_j}\xi_j + O(\xi^2),\qquad T_{ij}\equiv\frac{\partial a_i}{\partial x_j} = -\frac{1}{\rho_n}\partial_i\partial_j P$$

**(a) Eksenel bileşen:** $T_\parallel = \frac{da_r}{dr} = +\frac{2\mathcal{G}M}{r^3}$

**(b) Yanal bileşenler:** Kaynaksız bölgede iz sıfırdır: $\mathrm{tr}\,T = 0 \Rightarrow T_\parallel + 2T_\perp = 0 \Rightarrow T_\perp = -\mathcal{G}M/r^3$

**Sonuç:** $\left(T_\parallel, T_\perp, T_\perp\right) = \frac{\mathcal{G}M}{r^3}(+2,-1,-1)$, $\sum\lambda_i = 0$

**Nicel öngörü:** Gelgit potansiyeli $\Psi_T=-\frac{GMb^2}{2r^3}(3\cos^2\psi-1)$ ve serbest yüzey koşulu $g\,h+\Psi_T=$ sabit ile: $\Delta h = \frac{3}{2}\frac{M}{M_\oplus}\left(\frac{b}{r}\right)^{3}b$ → Ay 0,53 m · Güneş 0,25 m · büyük gelgit 0,78 m · küçük gelgit 0,29 m · oran 2,7.

**Geçerlilik Sınırı:** $b\ll r$ birinci mertebe; iz sıfırlığı yalnız kaynaksız bölgede; denge gelgiti statiktir (kayma ~3°, M-26).

**Açık Uçlar:** (i) şişkinlik kaymasının $\eta_E$ ile bağı; (ii) gövde içi ($r<b$) rejimde tensör izinin $q_n$ kaynak yoğunluğuyla ilişkisi.

</details>

### Orijinalde saptanan dört yapısal boşluk

1. **Çift şişkinliğin nedeni yok.** "İki uç da dışa kaçar" deniyor ama merkez ivmesinin neden
   çıkarıldığı — yani çerçeve adımı — hiç yazılmamış. Bu adım Newton'da bir muhasebe seçimidir;
   teoride **Postülat 7'nin fiziksel sonucudur** ve en büyük katma değer buradadır.
2. **İz sıfırlığı girdi olarak kullanılmış.** $T_\perp$ izden çıkarılıyor, sonra "izsizlik
   korunum yasasının kendisidir" deniyor — döngüsel. Doğrusu: $T_\perp$ bağımsız türetilir,
   iz **sonuç** olarak çıkar.
3. **Nedensellik tensörden çıkmıyor.** $(+2,-1,-1)$ simetrik bir nesnedir; "yan sıkıştırma
   nedendir" cümlesi ondan türetilemez. Nedensellik ancak **basınç alanının kendisine**
   inilerek kurulur.
4. **$\Delta h$ bir yükseklik değil, tepe–çukur genliğidir.** $3/2$ katsayısı tam olarak bundan
   gelir. Etiket yanlış; düzeltilince gözlemle örtüşme **güçlenir** (açık okyanusta bildirilen
   ~0,5 m de bir genliktir).

Ek olarak iki notasyon ihlali: $\Psi_T$ içinde $G$ yazılı (olması gereken $\mathcal{G}$) ve
$h$ sembolü Anayasa S-4'e aykırı ($h$ yalnız Planck sabitidir).

---

## 2. YENİDEN TÜRETİM (çalışma sürümü)

### 2.0 Notasyon

| Sembol | Anlam |
|---|---|
| $M$ | Gelgiti yaratan kaynağın kütlesi (Ay veya Güneş) |
| $r$ | Kaynak ile gövde merkezi arası uzaklık |
| $b$ | Gövde yarıçapı (Dünya), $b\ll r$ |
| $\vec\xi$ | Gövde merkezinden ölçülen iç konum, $|\xi|\le b$ |
| $\psi$ | $\vec\xi$ ile gövde–kaynak ekseni arasındaki açı |
| $\Phi$ | **İtim potansiyeli**, $\Phi\equiv(P-P_0)/\rho_n$ |
| $\Psi_T$ | Gelgit potansiyeli (taşınan çerçevedeki artık) |
| $\zeta$ | Serbest yüzey yükseltisi — **yeni sembol, karar gerekiyor** (bkz. 4.3) |

### 2.1 Varsayımlar

1. **M-35'in alanı geçerlidir:** $P(r)=P_0-\alpha M/r$, dolayısıyla $a_r=-\mathcal{G}M/r^2$ ve $\mathcal{G}=\alpha/\rho_n$.
2. **Uzanımlı gövde:** $b\ll r$; açılım birinci mertebede kesilir.
3. **Akı korunumu:** Kaynaktan uzakta deplasman akısı ne yaratılır ne yok edilir (Adım 2.3'te nicelenir).
4. **Taşınan gövde çerçevesi (Postülat 7):** Gövde, sürüklenme zarfı içinde akıntıyla **bir bütün olarak** taşınır.
5. **$\rho_n$ evrenseldir:** Nükleon öz yoğunluğu bileşimden bağımsızdır (R-6: $2{,}7\times10^{17}$ kg/m³). *Bu varsayımın bedeli 2.7'de tahsil edilir.*

### 2.2 İtim potansiyeli — ödünç alınmaz, tanımlanır

Kütle-itim yasası $\vec a=-\frac{1}{\rho_n}\nabla P$'dir (R-4). $\rho_n$ sabit olduğundan bu
ifade tam bir potansiyele indirgenir:

$$\Phi \equiv \frac{P-P_0}{\rho_n} \;\Longrightarrow\; \vec a = -\nabla\Phi,\qquad \Phi(r)=-\frac{\mathcal{G}M}{r}$$

Bu, standart fizikten alınmış bir kütleçekim potansiyeli **değildir**: basınç alanının nükleon
öz yoğunluğuna bölünmüş hâlidir ve birimi $\mathrm{J/kg}$ değil, doğrudan
$\mathrm{Pa}/(\mathrm{kg\,m^{-3}})$'tür — aynı boyut, farklı köken.

### 2.3 Çerçeve adımı — çift şişkinlik buradan doğar

Gövde merkezi $\vec r$'de, gövde üzerindeki nokta $\vec r+\vec\xi$'dedir. Alan açılır:

$$\vec a(\vec r+\vec\xi) = \vec a(\vec r) + (\vec\xi\cdot\nabla)\vec a + O(\xi^2)$$

**Kritik adım:** Postülat 7 gereği gövde akıntıyla bir bütün olarak taşınır; $\vec a(\vec r)$
gövdenin **her** noktasına aynı şekilde etki eder ve gövdeyi deforme etmez. Deformasyonu yapan,
yalnızca ondan sapan artıktır:

$$\boxed{\;\Delta\vec a(\vec\xi) \equiv \vec a(\vec r+\vec\xi) - \vec a(\vec r) = \mathsf{T}\,\vec\xi,\qquad T_{ij}=\frac{\partial a_i}{\partial x_j}=-\frac{1}{\rho_n}\partial_i\partial_j P\;}$$

> **Newton'la fark burada başlar.** Klasik türetimde $\vec a(\vec r)$'nin çıkarılması, eylemsiz
> çerçeveye geçmek için yapılan bir muhasebe işlemidir. Teoride ise çıkarılan şey *fiziksel
> olarak taşınan* kısımdır: sürüklenme zarfı gövdeyi ortak ivmeyle götürür, geriye kalan
> gerçekten de gövdenin hissettiği tek şeydir. **Çerçeve seçimi değil, çerçeve tespitidir.**

$\mathsf{T}$ simetrik olduğundan $\Delta\vec a(-\vec\xi)=-\Delta\vec a(\vec\xi)$: eksenin iki
ucundaki artık ivmeler zıt yönlüdür, yani **ikisi de merkezden dışa** bakar. Çift şişkinlik,
ek bir varsayım olmadan, doğrudan bu simetriden çıkar.

### 2.4 Akı korunumu → $\nabla^2P=0$

M-35'in ortam tepkisi $\dfrac{dP}{dr}=\dfrac{C\,Nq_n}{4\pi r^2}$ idi. Kaynağı çevreleyen
herhangi bir $S$ küresi üzerinden basınç gradyanı akısı:

$$\oint_S \nabla P\cdot d\vec A = \frac{C\,Nq_n}{4\pi r^2}\cdot 4\pi r^2 = C\,Nq_n = \text{sabit}$$

Akı **yarıçaptan bağımsızdır.** Diverjans teoremiyle, kaynağı içermeyen herhangi bir kabukta

$$\int_V \nabla^2 P\,dV = \oint_{S_{dış}}\!\!\nabla P\cdot d\vec A - \oint_{S_{iç}}\!\!\nabla P\cdot d\vec A = 0 \;\Longrightarrow\; \nabla^2P=0$$

**Fiziksel okuma:** Kaynaktan çıkan deplasman akısı yolda ne çoğalır ne eksilir — Evrenakı
yaratılmaz, yok edilmez. Bu, soyut bir alan özelliği değil, **doğrudan korunum ifadesidir.**

*Bu sonucu şimdi kullanmayacağız.* Bir sonraki adımda tensörü ondan bağımsız kuracak, sonra
iki yolun çakıştığını göstereceğiz.

### 2.5 Tensörün üç bileşeninin bağımsız türetimi

**(a) Eksenel bileşen.** Doğrudan radyal ivmenin türevi:

$$T_\parallel = \frac{da_r}{dr} = \frac{d}{dr}\!\left(-\frac{\mathcal{G}M}{r^2}\right) = +\frac{2\mathcal{G}M}{r^3}$$

**(b) Yanal bileşen — iz varsayımı kullanılmadan, saf geometriden.** Merkezden $\xi_\perp$ kadar
yana kaymış noktada ivme yine kaynağa doğrudur; büyüklüğü $\mathcal{G}M/r'^2$ ($r'=\sqrt{r^2+\xi_\perp^2}\simeq r$),
fakat doğrultusu merkez hattından $\xi_\perp/r$ kadar sapar. Eksene dik bileşen:

$$a_\perp = -\frac{\mathcal{G}M}{r'^2}\cdot\frac{\xi_\perp}{r'} \simeq -\frac{\mathcal{G}M}{r^3}\,\xi_\perp \;\Longrightarrow\; T_\perp = -\frac{\mathcal{G}M}{r^3}$$

Bu tamamen $1/r^2$ alanının **yakınsama geometrisidir**: radyal çizgiler kaynağa doğru
birbirine yaklaşır, gövdenin yanakları merkez hattına doğru itilir.

**(c) İz artık bir sonuçtur.**

$$\mathrm{tr}\,\mathsf{T} = T_\parallel + 2T_\perp = \frac{2\mathcal{G}M}{r^3} - \frac{2\mathcal{G}M}{r^3} = 0$$

$$\boxed{\;(T_\parallel,\,T_\perp,\,T_\perp) = \frac{\mathcal{G}M}{r^3}\,(+2,\,-1,\,-1),\qquad \mathrm{tr}\,\mathsf{T}=0\;}$$

> **Kazanç.** Orijinal türetimde izsizlik bir *varsayımdı* ve sonuç ondan çıkarılıyordu; burada
> üç bileşen de bağımsız türetildi ve iz **kendiliğinden** sıfır çıktı. Üstelik
> $\mathrm{tr}\,\mathsf{T}=-\frac{1}{\rho_n}\nabla^2P$ olduğundan bu, 2.4'ün akı korunumuyla
> birebir aynı ifadedir: **iki bağımsız yol aynı sıfırı verir.** "İzsizlik = korunum yasası"
> cümlesi artık slogan değil, iki yönden doğrulanmış teoremdir.

### 2.6 Basınç okuması — nedensellik burada kurulur

$(+2,-1,-1)$ simetrik bir nesnedir ve tek başına "yan sıkıştırma nedendir" demeye izin vermez.
Nedensellik ancak fiziksel alana — basınca — inilerek kurulur. 2.3'ün çerçevesinde, taşınan
kısım çıkarıldıktan sonra geriye kalan artık potansiyel, açılımın ikinci mertebe terimidir:

$$\Psi_T(\vec\xi) = -\tfrac12\left(T_\parallel\xi_\parallel^2 + T_\perp\xi_\perp^2\right) = -\frac{\mathcal{G}M}{2r^3}\left(2\xi_\parallel^2-\xi_\perp^2\right)$$

$\xi_\parallel=\xi\cos\psi$, $\xi_\perp=\xi\sin\psi$ konarak kapalı biçim:

$$\boxed{\;\Psi_T(\xi,\psi) = -\frac{\mathcal{G}M\xi^2}{2r^3}\left(3\cos^2\psi-1\right)\;}$$

Buraya kadar her şey ivme dilindeydi. Şimdi $\Phi=(P-P_0)/\rho_n$ tanımını tersine çevirip
**artık basınç alanını** yazalım:

$$P_T(\xi,\psi) = \rho_n\Psi_T = -\frac{\rho_n\mathcal{G}M\xi^2}{2r^3}\left(3\cos^2\psi-1\right)$$

Gövde yüzeyinde ($\xi=b$) iki uç değer:

| Konum | $3\cos^2\psi-1$ | $P_T$ | Okuma |
|---|---|---|---|
| Eksen ($\psi=0°,180°$) | $+2$ | $-\dfrac{\rho_n\mathcal{G}Mb^2}{r^3}$ | **basınç açığı** |
| Yanaklar ($\psi=90°$) | $-1$ | $+\dfrac{\rho_n\mathcal{G}Mb^2}{2r^3}$ | **basınç fazlası** |

**Nedensellik artık türetilmiştir.** Taşınan bileşen fiziksel olarak çıkarıldıktan sonra geriye
kalan, gerçek bir basınç alanıdır: **yanaklarda yüksek, eksende düşük.** Su $-\nabla P$ yönünde,
yani yanaklardan eksene akar. Sıkıştırma nedendir, kabarma sonuçtur — ve açık/fazla oranının
tam $2{:}1$ olması, $(+2,-1,-1)$ özdeğer yapısının basınç dilindeki karşılığıdır.

*Newton'da bu tabloya karşılık gelen hiçbir şey yoktur; klasik türetimde basınç alanı yoktur,
yalnız ivme farkı vardır.*

**M-26 ile çapraz denetim.** Yanakların ekseni ne kadar aştığı:

$$P_T(90°)-P_T(0°) = +\frac{3}{2}\cdot\frac{\rho_n\mathcal{G}Mb^2}{r^3} > 0$$

M-26'nın hidrostatik topu, tamamen farklı bir yoldan (derinlik–basınç muhasebesi) aynı işareti
vermişti: $F_{yan}-F_{dikey}\propto\rho g r>0$. İki bağımsız argüman, aynı elipsoid. ✓

### 2.7 Eşdeğerlik ilkesi: varsayım değil, sonuç

Tensör $T_{ij}=-\frac{1}{\rho_n}\partial_i\partial_jP$ biçimindedir. Buradaki $\rho_n$
**nükleon öz yoğunluğudur** — su, kaya, demir, cıva fark etmez; hepsi aynı nükleonlardan
kuruludur ve hepsi aynı $\rho_n$'yi taşır. Dolayısıyla gelgit ivmesi, üzerine etki ettiği
maddenin bileşiminden **zorunlu olarak** bağımsızdır.

Newton'da bu bağımsızlık bir postülattır (eylemsiz kütle = kütleçekimsel kütle). Burada
türetilmiştir: tek bir evrensel $\rho_n$ olduğu için başka türlüsü yazılamaz.

**Bunun bedeli ve sınavı:** İfade tersine de okunur — $\rho_n$'nin evrenselliği bozulsaydı
gelgit bileşime bağlı olurdu. Bu, teoriyi eşdeğerlik ilkesi testlerine (Eöt-Wash tipi burulma
terazileri, MICROSCOPE) doğrudan bağlar: o testlerin null sonuçları, teoride $\rho_n$
evrenselliğinin sınavıdır.

### 2.8 Serbest yüzey ve denge gelgiti

Serbest yüzey, toplam potansiyelin sabit olduğu yüzeydir:

$$g\,\zeta(\psi) + \Psi_T(b,\psi) = \text{sabit},\qquad g=\frac{\mathcal{G}M_\oplus}{b^2}$$

**Sabit, hacim korunumundan sabitlenir.** Su yaratılmadığına göre $\langle\zeta\rangle=0$
olmalıdır; $\langle 3\cos^2\psi-1\rangle=0$ (Legendre $P_2$'nin küre ortalaması sıfırdır)
olduğundan sabit **tam olarak sıfırdır.** Bu adım orijinalde atlanmıştı.

$$\zeta(\psi) = -\frac{\Psi_T}{g} = \frac{\mathcal{G}Mb^2}{2r^3}\cdot\frac{b^2}{\mathcal{G}M_\oplus}\left(3\cos^2\psi-1\right) = \frac{1}{2}\,\frac{M}{M_\oplus}\left(\frac{b}{r}\right)^3 b\,\left(3\cos^2\psi-1\right)$$

> **$\mathcal{G}$ sadeleşti.** Sonuçta ne $\mathcal{G}$, ne $\alpha$, ne $Cq_n$ kaldı — yalnız
> kütle oranı ve geometri. Denge gelgiti **sıfır parametreli** bir öngörüdür; teorinin serbest
> kalemlerinin hiçbirine dokunmaz.

$A\equiv\dfrac{M}{M_\oplus}\left(\dfrac{b}{r}\right)^3 b$ kısaltmasıyla:

$$\zeta(0°)=+A \quad(\text{kabarma tepesi}),\qquad \zeta(90°)=-\tfrac12 A \quad(\text{çukur})$$

$$\boxed{\;\Delta\zeta \equiv \zeta(0°)-\zeta(90°) = \frac{3}{2}\,\frac{M}{M_\oplus}\left(\frac{b}{r}\right)^{3} b\;}$$

> **Etiket düzeltmesi (önemli).** $3/2$ katsayısı buradan gelir: kabarma merkez seviyenin
> $+A$ üstüne çıkarken, yanaklar $-A/2$ altına iner. Yani $\Delta\zeta$ bir **yükseklik değil,
> tepe–çukur tam genliğidir.** Orijinaldeki "çıkan yükseklik" etiketi yanlıştır — ve düzeltme
> iddiayı **güçlendirir**, çünkü açık okyanus için bildirilen ~0,5 m değeri de bir genliktir.
> Doğru etiketle örtüşme birebir olur.

### 2.9 Bernoulli ve Statik Alan Uzlaştırması (Kısım 3.9.2 ile Bağlantı)

> [!NOTE]
> **Kavramsal Uzlaştırma:** Kısım 3.9.2'de gelgit mekanizması, Ay'ın Evrenakı akıntısını hızlandırması ve hızlanan akışkanın basıncının düşmesi (Bernoulli Prensibi) üzerinden nitel olarak açıklanmıştır. Bu bölümdeki tensörel türetim ise statik $P(r) = P_0 - \alpha M/r$ alanı üzerinden yürütülmüştür. 
> İki yaklaşım birbiriyle çelişmez, aynı gerçeğin farklı referans çerçevelerinden okunmasıdır:
> Adım 2.3'te kurulan **taşınan çerçevede** gövde akıntıyla beraber hareket eder; bağıl hız sıfırdır ve alan gövdeye göre statik görünür (Laplace/Tensör matematiği uygulanır).
> Gövdenin dışından, **akıntının içinden** bakan bir gözlemci için ise aynı basınç farkları, akışkanın hızlanıp yavaşlaması (Bernoulli dinamiği) olarak okunur. Her iki çerçeve de yanaklardaki diferansiyel sıkıştırmanın fiziksel gerçekliğini doğrular.

---

## 3. Sayısal denetim — hiçbir sayı değişmedi

$b=6{,}371\times10^6$ m.

| Kaynak | $M/M_\oplus$ | $(b/r)^3$ | $A$ = tepe | çukur $=-A/2$ | $\Delta\zeta=\tfrac32A$ |
|---|---|---|---|---|---|
| Ay | $1{,}229\times10^{-2}$ | $4{,}553\times10^{-6}$ | $+0{,}357$ m | $-0{,}178$ m | **0,535 m** |
| Güneş | $3{,}331\times10^{5}$ | $7{,}724\times10^{-14}$ | $+0{,}164$ m | $-0{,}082$ m | **0,246 m** |

| Denetim kalemi | Hesap | Sonuç | M-36'daki değer |
|---|---|---|---|
| Güneş/Ay gelgit oranı (genlikten) | $0{,}246/0{,}535$ | $0{,}460$ | 0,46 ✓ |
| Güneş/Ay gelgit oranı (tensörden) | $\frac{M_\odot}{M_{Ay}}\left(\frac{r_{Ay}}{r_\odot}\right)^3=\frac{2{,}709\times10^7}{389{,}2^3}$ | $0{,}460$ | 0,46 ✓ |
| Büyük gelgit (hizalı) | $0{,}535+0{,}246$ | **0,781 m** | 0,78 ✓ |
| Küçük gelgit (dik) | $0{,}535-0{,}246$ | **0,289 m** | 0,29 ✓ |
| Büyük/küçük oranı | $0{,}781/0{,}289$ | **2,70** | 2,7 ✓ |
| Toplam itim oranı (karşılaştırma) | $\frac{M_\odot}{M_{Ay}}\left(\frac{r_{Ay}}{r_\odot}\right)^2$ | $179$ | 179 ✓ |

**Sonuç: yeniden türetim M-36'nın altı sayısal sonucunu da birebir üretir.** Değişen tek şey
`0,53 m`'nin *ne olduğu*: yükseklik değil, tepe–çukur genliği.

### 3.1 Bonus — M-36'nın ikinci açık ucu kapanıyor

M-36 "gövde içi ($r<b$) rejimde tensör izinin $q_n$ kaynak yoğunluğuyla ilişkisi" kalemini
açık bırakmıştı. Hesap kısa: gövde içinde akı artık sabit değildir, kapsanan nükleon sayısıyla
büyür. Kaynak yoğunluğu $n_n=\rho_{madde}/m_n$ ile

$$\nabla^2P = C\,q_n\,n_n = \frac{C\,q_n\,\rho_{madde}}{m_n} \;\Longrightarrow\; \mathrm{tr}\,\mathsf{T} = -\frac{1}{\rho_n}\nabla^2P = -\frac{C\,q_n}{4\pi\rho_n m_n}\cdot 4\pi\rho_{madde}$$

M-35'in $\mathcal{G}=\dfrac{Cq_n}{4\pi\rho_n m_n}$ ayrıştırmasıyla:

$$\boxed{\;\mathrm{tr}\,\mathsf{T}\big|_{i\varsigma} = -4\pi\mathcal{G}\rho_{madde}\;}$$

Yani teori, gövde içinde **Poisson denkleminin tam karşılığını** üretir — yeni parametre
girmeden, doğru katsayıyla. Bu bir ayırt edici öngörü değil, bir **tutarlılık kapanışıdır**:
kaynaksız bölgede iz sıfır, kaynak içinde $-4\pi\mathcal{G}\rho$. *(Kalem kapatılabilir —
ama M-36'ya işlemek izin gerektirir; bkz. 4.1.)*

---

## 4. İzin bekleyen kalemler (Kısım 8 — DOKUNULMADI)

Aşağıdakilerin hiçbiri uygulanmamıştır. Onay verilirse tek partide işlenir.

### 4.1 Ek M-36'da önerilen değişiklikler

| # | Kalem | Gerekçe | Risk |
|---|---|---|---|
| 1 | Varsayım 3'ü "akı korunumu"na çevir, $\nabla^2P=0$'ı türet | İzsizlik girdi olmaktan çıkıp sonuç olur (2.4 + 2.5c) | yok — sonuç aynı |
| 2 | $T_\perp$'yi geometriden bağımsız türet | Döngüsel akıl yürütme kalkar | yok |
| 3 | $\Psi_T$'de $G\to\mathcal{G}$ | Anayasa R-1 / S-20 ihlali | yok |
| 4 | $\Delta h\to\Delta\zeta$ ve "yükseklik"→"tepe–çukur genliği" | Anayasa S-4 ihlali + etiket hatası | yok — sayı değişmiyor |
| 5 | Açık Uç (ii)'yi kapat: $\mathrm{tr}\,\mathsf{T}|_{iç}=-4\pi\mathcal{G}\rho$ | 3.1'de hesaplandı | yok |
| 6 | Çerçeve adımını (Postülat 7) ekle | En büyük katma değer; şu an hiç yok | yok |

**Not:** İzin verilmezse 11.1 ile M-36 arasında bilinçli bir sapma doğar (11.1 düzgün notasyonlu
ve doğru etiketli, M-36 eski hâlinde). Anayasa'da bu tür bilinçli tutarsızlıkların kayda
geçirildiği emsal vardır ("Bunun bilinen bedeli" kaydı). Sapma bu dosyada tutulur.

### 4.2 Ek M-26'da önerilen değişiklik

Yok. M-26'nın hidrostatik argümanı bağımsız bir yoldur ve 2.6'nın çapraz denetiminde
**doğrulanmıştır** — dokunmaya gerek yok, yalnız 11.1'den atıf verilecek.

### 4.3 $\zeta$ sembolü — ✔ ÇÖZÜLDÜ (yazar kararı, 2 Ağustos 2026)

$\zeta$ = serbest yüzey yükseltisi, **S-27 olarak Anayasa'ya kaydedildi**
(`Matematik_Notasyon_Anayasasi.md`, Bölüm II). Gelgit genliği $\Delta\zeta$ ile yazılır;
$\Delta h$ geçersizdir (S-4), $\Delta\eta$ kullanılmaz ($\eta_E$ ile çakışır).

### 4.4 Ek D sembol sözlüğü — ✔ İZİN VERİLDİ VE İŞLENDİ (2 Ağustos 2026)

Yazar `Kisim_8_Ekler/08_Sembol_Sozlugu.md` için özel izin verdi. **İşlenenler (D.4–D.5):**

| Girdi | İşlem | Not |
|---|---|---|
| $\zeta$ | **yeni** — serbest yüzey yükseltisi, $\Delta\zeta$ genlik formülü, S-27 atfı | Δh ve Δη yasakları yazıldı |
| $\mathsf{T}$, $T_{ij}$ | **yeni** — gelgit tensörü, $(+2,-1,-1)$, iç rejimde $-4\pi\mathcal{G}\rho$ | |
| $\Psi_T$ | **yeni** — gelgit potansiyeli + artık basınç alanı $P_T=\rho_n\Psi_T$, 2:1 oranı | |
| $\psi$ | **yeni** — gelgit açısı; $\Psi_{Evrenakı}$ ile karışmaması notu | |
| $\vec\xi$ | **yeni + çakışma çözümü** | aşağıya bkz. |
| $\Phi$ | **güncellendi** (ek kayıt) — $\Phi\equiv(P-P_0)/\rho_n$ olarak tanımlandığı, $\Lambda=1-\Phi/c^2$'deki $\Phi$ ile aynı büyüklük olduğu, farkın kökende olduğu | mevcut girdi silinmedi, üstüne eklendi |

**Çözülen sembol çakışması ($\xi$).** Ek D'de $\xi$ zaten **dönme sürüklenme kesridir**
(M-40, skaler). M-36 ve 11.1 ise $\vec\xi$'yi **gövde içi konum vektörü** olarak kullanıyor —
R-1 (tek sembol tek anlam) ihlali, ve bu ihlal M-36'dan beri mevcuttu. Çözüm, dosyanın kendi
emsaline uyduruldu ($\Gamma$ girdisindeki "bağlamla ayrılır" kaydı): gelgit bağlamında daima
**vektörel $\vec\xi$**, sürüklenme bağlamında daima **skaler $\xi$**; ikisi hiçbir denklemde
birlikte geçmez. Ayrım her iki girdiye de yazıldı. *Yeniden adlandırma yapılmadı — $\vec\xi$
gelgit literatürünün ve M-36'nın yerleşik yazımıdır, değiştirmek M-36'ya dokunmayı gerektirirdi.*

---

## 5. Karar durumu

**(a) Kanonik yer — ✔ ÇÖZÜLDÜ.** Tam türetim 11.1'de durur; M-36 olduğu gibi kalır
(Kısım 8 kapalı). Sapma 4.1'de kayıtlıdır.

**(b) Bernoulli uzlaştırması — ✔ ÇÖZÜLDÜ (yazar kararı, 2 Ağustos 2026): kutu 11.1'e
girer, 3.9.2'ye dokunulmaz.** Kutunun içeriği (11.1'de yazılacak): 3.9.2'nin Bernoulli
anlatısı ile bu bölümün statik gradyan türetimi **aynı alanın iki çerçevedeki okunuşudur.**
Taşınan gövde çerçevesinde (2.3) ortam gövdeye göre durgundur ve alan statik
$P(r)=P_0-\alpha M/r$ olarak görünür; gövdeye göre akan çerçevede aynı alan, hızın arttığı
yerde basıncın düştüğü bir Bernoulli profili olarak okunur. İki okuma arasındaki geçiş,
2.3'te çıkarılan ortak taşınma teriminin ta kendisidir. **Nicel sonuç tek yerden gelir:**
sayılar statik gradyandan türetilir (Bölüm 3); Bernoulli okuması mekanizmanın yerel
görünümüdür, ikinci bir hesap kalemi değildir.

**(c) $\sim3°$ şişkinlik kayması — ✔ ÇÖZÜLDÜ (2 Ağustos 2026), fakat beklenenden farklı sonuçla.**

*Terk edilen rota.* Kaymanın Ek M-43'ün altkritik bastırmasından çıkacağını ve teorinin **ilk
ayırt edici gelgit öngörüsü** olacağını yazmıştım. **Yanlıştı.** Yazar düzeltmesi: buradaki
sürükleme atomiktir, Evrenakısal değil.

*İkinci düzeltme — gerekçenin kendisi de yanlıştı.* İlk gerekçeyi "Evrenakı katı maddeyi engel
görmez, geçtiği şeyi **sürükleyemez**, tutamağı yoktur" diye yazmıştım. Bu **kategorik inkâr
Postülat 7 ile çelişir** ($\eta_E$ sıfıra yakın ama **kesinlikle sıfır değil**) ve teorinin
$\eta_E$'yi kullandığı bütün olguları (retrograd sönüm, kilitlenme, halka bending-wave) havada
bırakır. Yazar düzeltmesi: ortam sürükler, ama etkisi ancak **zaman genişliğinde** görünür.
Gerekçe nicel zaman-ölçeği argümanına çevrildi:

| Kanal | Gevşeme zamanı |
|---|---|
| Maddesel | $\tau_{madde}\simeq QP/2\pi \approx 8{,}5\times10^{4}$ s ($\approx24$ sa) |
| Evrenakı | $\tau_E = 2\rho_cb^2/9\eta_E \approx 1{,}5\times10^{21}$ s ($\approx5\times10^{13}$ yıl = evren yaşının ~3500 katı) |
| Oran | $\tau_E/\tau_{madde}\approx1{,}8\times10^{16}$ |

12,4 saatlik bir zorlamaya, 16 mertebe daha yavaş bir kanal derece mertebesinde faz
kazandıramaz. $\tau_E$ üstelik **en cömert** tahmindir (Stokes yazımı; M-43'ün altkritik
bastırması daha da büyütür). İkinci gerekçe ölçülen ~3,7 TW yitimin sığ deniz taban
sürtünmesinde olması. **İki kanal rakip değil, farklı zaman pencerelerinde çalışıyor** —
hangisinin baskın olduğunu olgunun periyodu belirliyor.

*Doğru muhasebe — iki ayrı rol.* Kaymayı **madde** yapar (okyanus–taban sürtünmesi);
kayan şişkinliğin torkunu **Evrenakı** taşır (gradyan lobu, 3.9.4). Teorinin katkısı kaymayı
üretmek değil, torku taşıyan aracıyı adlandırmaktır.

*Hesap (yapıldı).* $\Gamma=\tfrac32k_2\sin(2\varepsilon)\,\mathcal{G}M_{Ay}^2R_\oplus^5/r^6 = dL/dt$,
$L=M_{Ay}\sqrt{\mathcal{G}M_\oplus r}$, ölçülen $dr/dt=3{,}8$ cm/yıl:

| | |
|---|---|
| $L$ | $2{,}88\times10^{34}$ kg·m²/s |
| $dL/dt$ | $4{,}50\times10^{16}$ N·m |
| $\mathcal{G}M_{Ay}^2R_\oplus^5/r^6$ | $1{,}17\times10^{18}$ N·m |
| $k_2\sin2\varepsilon$ | $0{,}0256$ |
| $\varepsilon$ ($k_2=0{,}35\ldots0{,}20$) | $2{,}10^\circ \ldots 3{,}68^\circ$ |
| karşılık gelen $Q$ | $13{,}7 \ldots 7{,}8$ |

Gözlenen $\sim3^\circ$ bandın içinde ✓; çıkan $Q\approx8\!-\!14$ Dünya'nın bağımsız bilinen
gelgit $Q$'suyla (~12) örtüşüyor ✓. **Ama ayırt edici değil:** tork bağıntısı standart
kuramla ortak, $k_2$ ve $Q$ malzeme özellikleri.

*Kalan tek teoriye-özgü kalem — artık nicel.* Malzeme sürtünmesi sıfır olan bir gövdede
standart kuram $\varepsilon=0$ der; teoride $\eta_E\ne0$ olduğu için sıfırlanmayan bir
**artık kayma tabanı** kalır. Faz katkıları gevşeme zamanlarıyla ters orantılı olduğundan
büyüklüğü yazılabilir:
$$\varepsilon_E\approx\varepsilon_{madde}\frac{\tau_{madde}}{\tau_E}\approx3^\circ\times5{,}6\times10^{-17}\approx2\times10^{-16}\ \text{derece}$$
Sayı ayrımın hem **gerçek** (sıfır değil, standart kuramdan farklı) hem **ölçülemez** olduğunu
aynı anda söylüyor → bugün sınav değil. Ayırt edici sınav gelgitte değil, teorinin $\eta_E$'yi
zaten kullandığı **uzun-pencere** olgularında aranmalı (retrograd göç, kilitlenme, halka sönümü
— 11.3.2, M-43).

*Doğan yeni bulgu — 3.9.4 ile gerilim.* Hesap uzaklaşmanın **tamamını** lob torkuna yüklüyor
ve ancak öyle $\sim3^\circ$ veriyor. Kozmolojik seyrelme tabanı kayda değer bir pay taşısaydı
açı gözlenenin altına düşerdi. Yani sonuç **lob teriminin baskın olduğunu** söylüyor —
3.9.4'ün *karşı-kayıt* paragrafıyla uyumlu, aynı bölümün *açılış* paragrafındaki "uzaklaşmanın
asıl kaynağı kozmolojiktir" ifadesiyle **çelişkili.** 3.9.4 Kısım 3'tedir (yazmaya açık) ama
dokunulmadı — yazar kararı bekliyor.

---

## 5.1 Kuvvet envanteri — yazar düzeltmesi (2 Ağustos 2026)

**Düzeltilen hata.** Türetimin ilk sürümü çerçeve adımını **Postülat 7'nin sürüklenme
zarfına** dayandırıyordu. Bu yanlıştı: sürüklenme zarfı Kuvvet 3'ün (M-37, $\omega_1$ kolu)
sıfırıncı mertebesidir, oysa **Ay kilitlidir ve makro-girdabı bastırılmıştır** — dönüş kolu
kapalıdır. Kilitli bir kaynak Dünya'ya Kuvvet 3, 4 veya 5 uygulayamaz.

**Doğrusu.** Çerçeve adımı zaten **Kuvvet 1'in kendisinden** çıkar: $\vec a=-\nabla P/\rho_n$
ve $\rho_n$ evrensel olduğu için alanın ortak bileşeni her nükleona aynı ivmeyi verir, gövdeyi
taşır ama deforme etmez. Postülat 7'ye hiç gerek yoktur.

**Kazanç — kısıt değil, temizlik.** Düzeltme türetimi zayıflatmaz, güçlendirir:

| Kuvvet | Kol | Kilitli kaynakta | 11.1'deki rolü |
|---|---|---|---|
| 1 — Radyal kütle-itim | $\omega_2$ | **açık** | tek girdi |
| 2 — Diferansiyel sıkıştırma | $\omega_2$ | **açık** | çıktı (1'in türevi) |
| 3 — Vorteks sürüklenmesi | $\omega_1$ | kapalı | yok |
| 4 — Eksenel itim | $\omega_1$ | kapalı | yok |
| 5 — Yanal itim | $\omega_1$ | kapalı | yok |

Gelgitin tamamı **tek kuvvete** iner ve tensörün $(+2,-1,-1)$ yapısı $\omega_1$ kökenli hiçbir
terimle karışmadan saf çıkar. 11.1.2'ye kutu, 11.1.1'e varsayım 5, 11.1.7'ye 3. madde olarak
işlendi. 11.1.7'nin eski 1. maddesi ("çerçeve Postülat 7'den gelir") **kaldırıldı**; çerçeve
adımı artık 2. maddenin ($\rho_n$ evrenselliği) altına, aynı kök olduğu kaydıyla yazıldı.

**Açık soru — Güneş dönüyor.** Ay için envanter temiz, ama **Güneş kilitli değildir**:
$\omega_1$ kolu açıktır, dolayısıyla Güneş'in Dünya'ya uyguladığı gelgite ilkece Kuvvet 4/5
katkısı karışabilir. Gözlem bunun ölçülemez olduğunu söylüyor (Güneş/Ay oranı saf $1/r^3$'ün
verdiği 0,460'tır, sapma yok). Bu bir **üst sınır** demektir ve muhtemelen $\kappa_5$'i
sınırlar. Hesaplanmadı; 11.1'e de yazılmadı. Yazar kararı bekliyor.

---

## 6. Değişiklik günlüğü

| Tarih | İşlem |
|---|---|
| 2 Ağustos 2026 | Dosya açıldı. M-36 arşiv kopyası alındı (Bölüm 1). Yeniden türetim yazıldı (Bölüm 2): çerçeve adımı, akı korunumu, bağımsız $T_\perp$, basınç nedenselliği, EP sonucu, hacim korunumuyla sabitlenen serbest yüzey. Sayısal denetim yapıldı — altı sonucun altısı da tuttu (Bölüm 3). M-36'nın ikinci açık ucu kapatıldı ($\mathrm{tr}\,\mathsf{T}|_{iç}=-4\pi\mathcal{G}\rho$). Kısım 8'e **dokunulmadı.** |
| 2 Ağustos 2026 | Yazar kararları alındı: **(a)** tam türetim 11.1'de · **(b)** Bernoulli uzlaştırma kutusu 11.1'e, 3.9.2'ye dokunulmaz · **S-27** ($\zeta$) Anayasa'ya kaydedildi. Yeni izin kalemi açıldı: 4.4 (Ek D sembol sözlüğü senkronu). **(c)** hâlâ açık. |
| 2 Ağustos 2026 | **11.1 baştan yazıldı** (yazar talimatı: önceki taslak dikkate alınmadı, silindi). Nihai yapı 11.1.1–11.1.9: notasyon+varsayımlar · **kuvvet envanteri** (kilitli kaynak, $\omega_1$ kapalı) + 11.2 ayrım uyarısı · itim potansiyeli + çerçeve adımı (Kuvvet 1'den) + Bernoulli uzlaştırma kutusu · akı korunumu + üç bileşen + iz teoremi · basınç nedenselliği (2:1) + M-26 çapraz denetimi · genlik + Güneş/Ay + büyük/küçük + dürüstlük kaydı · eşdeğerlik ilkesi · Newton sınırı · geçerlilik + iç rejim kapanışı + 3° açık kalemi. |
| 2 Ağustos 2026 | **Çembersellik açıkça yazıldı** (yazar düzeltmesi). Eksik: $-1$ özdeğerinin **iki katlı dejenere** olduğu yazılıydı ama bunun fiziksel anlamı — gradyan yapısının Ay'a bakmayan bütün yanlarda **eşit** olması, dolayısıyla sıkıştırmanın noktasal kıstırma değil **ekseni saran eşit basınçlı kuşak** olması — söylenmemişti. 11.1.4(b)'ye "Sıkıştırmanın çembersel olması" paragrafı, özdeğer tablosuna dejenerasyon etiketi, tabloya "Mekanizmanın üç adımı" özeti (ön–arka farkı → çembersel kuşak → çift kabarma) ve 11.1.5'e basınç dilindeki karşılığı ($P_T$ azimuttan bağımsız) eklendi. Ayrıca karşılıklılık notu: aynı geometri Ay'ı da sıkar, kilitli olduğu için orada kabarma magmada kalıcılaşır (mascon, 3.9.5). |
| 2 Ağustos 2026 | **"Gelgit ekseni" terimi tanımlandı** (yazar düzeltmesi — kritik). Metinde "eksen" on yerde niteliksiz geçiyordu; 11.2 baştan sona **dönme ekseninden** bahsettiği için okurun ikisini birleştirmesi kaçınılmazdı. Terim notasyon tablosuna girdi, 11.1.3'e `[!CAUTION]` uyarı kutusu eklendi (üç gerekçe: yönelim · kuşak ekvator değildir · **günde iki gelgitin sebebi tam olarak bu ayrımdır**, ardışık tepeler arası 12 sa 25 dk; ayrıca günlük eşitsizlik aynı geometriden), ve niteliksiz geçen her "eksen" → "gelgit ekseni" olarak düzeltildi (11.1.3, 11.1.4 ×4, 11.1.5 ×3, 11.1.8, 11.1.9). Kutuya 11.2 ile ayrım cümlesi de kondu. |
| 2 Ağustos 2026 | *(geçersiz — üstteki satırla değiştirildi)* İlk yazım turu (11.1.1–11.1.8). Yazarın kendi taslağı korundu, üzerine eklendi: akı korunumunun bağımsız türetimi (Gauss), özdeğer tablosu, artık basınç alanı $P_T$ tablosu ve 2:1 oranı, M-26 çapraz denetimi, büyük/küçük gelgit (0,781 / 0,289 / 2,70), **11.1.6** eşdeğerlik ilkesi, **11.1.7** Newton'la sınır tablosu, **11.1.8** geçerlilik sınırı + iç rejim kapanışı + 3° açık kalemi. Düzeltilenler: "milimetrik doğruluk" iddiası → mertebe-ve-yapı doğrulaması dürüstlük kaydı; $\pm P_T$ muğlaklığı → sayısal tablo; "ekvatordan sıkılan" → "yanaklardan"; başlık düzeyi `###`→`##` (11.2/11.3 ile hizalandı); 11.1.5 başlığı "Yükseklik"→"Genlik". **Ek D izinle işlendi** (4.4), $\xi$ çakışması çözüldü. **Kaynakça:** Touboul 2022 ve Schlamminger 2008 eklendi (11.1.6'nın EP sınavı için). Kısım 10'a ve M-36'ya **dokunulmadı.** |
