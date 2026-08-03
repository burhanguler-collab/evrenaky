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

## 4. İzin kalemleri — ✅ TAMAMI İŞLENDİ (3 Ağustos 2026, "kilitler açıldı")

> **Kapanış kaydı.** Yazar kilitleri açtı. Aşağıdaki 4.1'in altı önerisi, 4.4'ün Ek D senkronu,
> 5.5.5'in M-37 düzeltmesi ve 5.6.4'ün M-25 güncellemesi **tek partide işlendi.** Kısım 3 ile
> Ek M arasındaki bilinçli sayı sapması **kalmadı** (grep doğrulamalı: eski $\Delta h$, $GMb^2$,
> "23 kat", "17 kat", "430 km", "7,93 km" hiçbir yerde geçmiyor).
>
> **M-36'ya işlenenler:** Varsayım 3 → akı korunumu · Adım 0 (Gauss ile $\nabla^2P=0$) ·
> Adım 1 çerçeve (Kuvvet 1'den, Postülat 7'den değil) · $T_\perp$ geometriden bağımsız türetim ·
> çembersellik + dejenerasyon · iz **sonuç** olarak · $\Psi_T$'de $G\to\mathcal{G}$ ·
> $\Delta h\to\Delta\zeta$ + genlik etiketi + hacim korunumu · artık basınç alanı ve 2:1 oranı ·
> iki açık uç **kapatıldı** (3° atomik sürtünme; iç rejim $-4\pi\mathcal{G}\rho$) · yeni açık uç
> (dönen kaynak, 11.1.8) · özdeğer tablosu · geçerlilik sınırı · "Kullanıldığı bölümler"e 11.1.
>
> **M-37:** sıfırıncı mertebe "zarf" olarak yeniden yazıldı (taşıma değil, sürükleme bastırıcısı).
>
> **M-25:** Varsayım 1 (kapılış → serbest düşme), Adım 1'e ortam profili $v_\theta=2v_{kopma}$,
> iki muhasebe zinciri (874 km/s · 439 kat · 15,8 km/s · 34 kat), Adım 4'e "kopma hızının iki
> katı" kapanışı, kutulu sonuç.

<details>
<summary>Arşiv — işlenmeden önceki izin listesi</summary>

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

</details>

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

## 5.14 KATEGORİ AYRIMI KURULDU — beş kuvvet + denge yasaları (3 Ağustos 2026)

### 5.14.1 Yazarın önerisi ve benim karşı çıkışım

Yazar M-22'yi **altıncı kuvvet** ("Evrenakı Merkezkaç Kuvveti") yapmayı önerdi. Karşı çıktım,
üç gerekçeyle — üçüncüsü belirleyici:

1. **M-22 bir kaynak değil, denge koşulu.** F1–F5 alanı üretir; M-22 var olan alanla ortamın
   dönüşünün uyumlu olduğunu söyler.
2. **Postülat 9'un köken haritasına sığmıyor.** Ne $\omega_1$'den ne $\omega_2$'den doğuyor.
3. **Çift sayma tehlikesi — ve bunu bugün zaten düzelttik.** §5.8.1'de yazarın M-22 paragrafındaki
   *"F1 (içeri) ile M-22 (dışarı) kavgası"* ifadesini tam bu yüzden düzeltmiştim. F6 yapılırsa hata
   geri gelir ve somut bir bug üretir: $F_1+F_6$ yazan biri **aynı gradyanı iki kez sayar.**

Maliyet ölçümü: "beş kuvvet" 11 dosyada 26 yerde geçiyor + Postülat 9. Yapılabilirdi — sorun
maliyette değil, doğrulukta.

### 5.14.2 Ama sezilen boşluk gerçekti

Yeni olan şey *"merkezkaç bir kuvvettir"* değil; **ortamın maddeden ayrı kendine ait bir
dinamiği olduğu ve bunun ölçülebilir bir şey öngördüğü** ($2\times$ kayma). Ve bunun **evi yoktu:**
M-22 Blok F'de "radyal momentum dengesi" diye duruyordu, oysa Blok H'nin her yerinde kullanılıyor.

### 5.14.3 Çözüm: kategori ekle, kuvvet sayısını değiştirme

**Yazarın yerleştirme fikri benim varsayılanımdan daha iyiydi.** Ben H.0'a bir atıf satırı
koyacaktım; yazar *"beş kuvvetin altında işle"* dedi. Haklı: Blok H'yi okuyanın M-22'nin
varlığından haberi yoktu, ve kategori ayrımı ancak kuvvetlerin sayıldığı yerde görünürse öğretir.
Beş kuvvetten **sonra** koymak da mantıksal sırayı kodlar: önce üreten, sonra tepki veren.

**Tek düzeltmem:** M-22 girdisi taşınmadı (12 dosyada ~25 atıf, M-numaraları bloğa kilitli).
**Rolü ve kategorisi** Blok H'ye, **türetimi** Blok F'de kaldı, çapraz bağlandı.

### 5.14.4 İşlenenler

| Yer | Ne yapıldı |
|---|---|
| **Blok H, H.0** | Yeni *"İki kategori: kuvvetler ve denge yasaları"* tablosu + `[!WARNING]` çift sayma uyarısı. Köken haritası "beş kuvvet" olarak etiketlendi; denge yasalarının haritada yer almadığı yazıldı |
| **Blok H, M-39'dan sonra** | **Yeni bölüm: "DENGE YASALARI — kuvvet değil, tepki"**. **DY-1** (M-22: siklostrofik denge, yön tablosu, "kuvvet olmadığının kanıtı", merkezkaçın neden sanal olmadığı ama altıncı kuvvet de olmadığı). **DY-2** (iki yoğunluk ayrımı + **Ortam–Madde Kayma Yasası**, kutulu $v_\theta=2v_{madde}$, beş sistemlik kayma tablosu, savrulma mekanizması, 2 çarpanının **dört** bağımsız yolu, kayma tabakası açık kalemi) |
| **Blok H kapsam cümlesi** | *"iki kuvvet-olmayan girdiyle kapanır"* → **yanlıştı**, artık altı tane var (M-42, 43, 45, 47, 48, 49). İki türe ayrıldı: **(a)** denge yasaları, **(b)** çerçeve/rejim girdileri |
| **Blok F, M-22 başlığı** | Başlığa *"DENGE YASASI (kuvvet değil)"* etiketi + kategori kutusu + DY-1'e geri bağlantı + "toplanmaz" uyarısı |

**Postülat 9, "beş kuvvet" adı ve 26 geçiş: dokunulmadı.** Çift sayma kapısı kapalı.

---

## 5.13 M-37 ADIMLAR A — kaçırılmış kalıntı düzeltildi (3 Ağustos 2026)

**Kaynak: dış denetim (Gemini/antigravity).** Bulgu **doğru ve benim gözden kaçırdığım bir
yerdi:** §5.5.2'de M-37'nin *sıfırıncı-mertebe kutusunu* düzeltmişim, ama **hemen altındaki
türetim basamaklarını** bırakmışım.

**Çelişki:** Adımlar A'nın 2. adımı *"Sürüklenme zarfı gereği cisim ortamla eş hızlıdır:
$v_{yör}=v_\theta$"* diyor ve tek bir profil çözüyordu — yani girdinin kendi düzeltme kaydıyla,
M-9 ile ve 11.3.1 ile çelişiyordu.

**Düzeltme (fatura: sıfır).** Adım kaldırıldı; iki profil baştan ayrı türetildi:

$$v_{yör}=\sqrt{R\,|a_{madde}|}\,,\qquad v_\theta=\sqrt{\tfrac{\rho_n}{\rho_0}}\,v_{yör}=2\,v_{yör}$$

**Hiçbir gözlemsel sayı değişmedi**, yalnız etiketler ayrıştı:

| | Madde (gözlenen) | Ortam (öngörü) |
|---|---|---|
| Dünya yörüngesi | **29,79 km/s** ✓ (ölçüm 29,78) | 59,58 km/s |
| Düz rejim | **220 km/s** ✓ | 440 km/s |

**Kazanç:** M-9'un *"madde düşer, ortam dolaşır"* kuralı artık bu bloğun **içinde** matematiksel
olarak da kuruluyor — dışarıdan getirilmiş bir kural değil, aynı $\nabla P$'nin iki yoğunlukla
okunmasının sonucu. Bu, çarpanı görmenin **dördüncü** bağımsız yolu.

### Dış denetimin atladığı üç yan kalem (birlikte düzeltildi)

Gemini yalnız 2. adımı işaret etti ve *"3-4 satırlık formül metni"* dedi. Aynı bölümün üç ardıl
yeri de eski adıma dayanıyordu:

| # | Yer | Sorun | Düzeltme |
|---|---|---|---|
| 1 | Üç-rejim tablosu | Tek "çıkan profil" kolonu; düz rejim satırı gözlenen $v_0$'ı ortamın hızı sayıyordu | **İki kolon**: madde (gözlenen) / ortam (öngörü); *"gözlenen daima orta kolondur"* notu |
| 2 | Sonuç paragrafı | *"Serbest kalan… yalnız geçiş yarıçapı $r_0$'dır (Ek C P1 buna göre daraltılmalıdır)"* | $r_0$ **M-38'de türetildi** (§5.10); cümle güncellendi |
| 3 | Kapanış alıntısı | Düz eğriyi üç öğeden çıkarıyor, üçüncüsü **"sürüklenme zarfı"** | Üçüncü öğe **maddenin serbest düşmesi (M-2)** oldu; zarfın türetimde yer almadığı açıkça yazıldı |
| 4 | Geçerlilik Sınırı | *"Adımlar A'nın 2. adımı tam sürüklenme varsayar…"* — kaldırılmış bir adıma atıf | İki gerçek koşula indirildi: dairesel yörünge + kararlı eksenel simetrik dönüş |

**Sweep sonucu temiz:** kitapta `v_yör=v_θ`, "ortamla eş hızlı", "akışkana hapsolur" kalıntısı
kalmadı (düzeltme kayıtları hariç); galaktik zincirde (Kısım 6/7/10) düz dönüş eğrisini zarfa
bağlayan hiçbir atıf yok.

---

## 5.12 $h$ KAPANDI — ve Sınav 3'ün başarısızlığı yeniden açıldı (3 Ağustos 2026)

### 5.12.1 Soru yanlış kurulmuştu

M-38'in Adım 3'ü zaten *"$h$ sadeleşir"* diyor. Yani $h$'ın **değeri** sonuca hiç girmiyor.
Gereken tek şey, akının enjekte edildiği kalınlık ile $R$'deki yanağın kalınlığının aynı olması:

$$\text{akı yoğunluğu}\propto\frac{\Gamma(R)}{2\pi R}\cdot\frac{h_{inj}}{h(R)}$$

Soru "$h$ kaçtır?" değil, **"tabaka dışa giderken dikeyde yayılır mı?"**

### 5.12.2 Türetim: yayılamaz — Postülat 7'den, 22 mertebe marjla

Dolanım taşıyan tabakanın kalınlığı ideal akışkanda değişmez (Helmholtz/Kelvin); yalnız viskoz
difüzyonla yayılır: $\delta\sim\sqrt{\nu_E t}$, $\nu_E=\eta_E/\rho_0\approx4{,}9\times10^{-22}$ m²/s.

| Sistem | $t=R/v$ | $\delta$ | $h$ | Marj |
|---|---|---|---|---|
| Samanyolu (10 kpc) | $1{,}4\times10^{15}$ s | $8{,}3\times10^{-4}$ m | $9\times10^{18}$ m | $10^{22}$ |
| Dev disk (50 kpc) | $6{,}2\times10^{15}$ s | $1{,}7\times10^{-3}$ m | $3\times10^{19}$ m | $2\times10^{22}$ |

**Ve sonuç $\eta_E$'ye duyarlı değil:** koşulun bozulması için $\eta_E\gtrsim4\times10^{39}$ Pa·s
gerekir — kullanılan değerin $10^{44}$ katı. **Varsayım 3 artık teorem.**

### 5.12.3 İkinci sonuç: tabakalar İÇ İÇE — ve Sınav 3 yanlış geometriyle koşulmuş

Difüzyon yoksa $z$'deki nükleonun akısı $z$'de kalır ⟹ $a_{F4}(R,z)\propto\rho_*(z)$: **dikey
profil kaynağın dikey kütle profilini izler.** Sınav 3 (6.6.4) ise **tek ve düzgün** bir tüp
($h_0=0{,}15$ kpc) varsayıp **basamak** öngörmüş ve şu gerekçeyle başarısız ilan edilmişti:
*"sorun genlikte değil fonksiyonun biçiminde: teori basamak, gözlem rampa veriyor."*

İç içe resim **rampa** verir. NGC 891 kaba yeniden hesap ($h_z\approx1{,}5$ kpc):

| $\lvert z\rvert$ (kpc) | Gözlenen | Tek tabaka | **İç içe** |
|---|---|---|---|
| 0,15 | 228 | 146 | **223** |
| 0,5 | 222 | 146 | **210** |
| 1 | 215 | 146 | **194** |
| 2 | 200 | 146 | **172** |

Sapma **54–82 → 2–28 km/s**; biçim düzeliyor.

### 5.12.4 ⚠ Bu bir geçilmiş sınav DEĞİL

Üç eksik açıkça kaydedildi: **(i)** $h_z=1{,}5$ kpc **varsayıldı**, NGC 891'in gerçek dikey kütle
profili kullanılmadı; **(ii)** $v_{bar}$'ın $z$ bağımlılığı ihmal edildi; **(iii)** düzlem dışı
gazın dairesel yörüngede olup olmadığı denetlenmedi — Sınav 3'ün kendi 2. sonucu gazın baryonik
Kepler tabanının **altına** indiğini bulmuştu, ki bu gazın dairesel yörüngede *olmadığının*
işaretidir (fountain) ve o durumda M-37 zaten uygulanamaz (10.6.3 kapsam kaydı).

**İddia yalnızca şu:** Sınav 3 **yanlış geometriyle** yürütülmüştür ve **yeniden koşulmalıdır.**
Yeni koşum serbest parametre eklemez — $h_z$ NGC 891 için 21 cm/optik veriden bağımsızca bilinir.
Sınavın yeni statüsü: **açık, yeniden koşum bekliyor.** *(Anayasa'nın "Sınav 3 başarısız" kaydı
bu nedenle yeniden değerlendirmeye açılmıştır.)*

### 5.12.5 Üçüncü sonuç: flaring öngörüsü düzeltildi

Eski kutu, baryonik diskin kalınlaşmasının akı tüpünü de kalınlaştırıp dönüş eğrisini
düşüreceğini varsayıyordu. **Difüzyon olmadığına göre yanlış:** iç diskten gelen akı dış diskin
kalınlaşmasından etkilenmez. $1/R$'yi bozan şey, dış bölgede **kalın katmana enjekte edilen yeni
kütlenin** akısının daha geniş alana dağılmasıdır ⟹ dış kolda F4, ham kapsanan kütleyi değil
**dikey kalınlıkla ağırlıklanmış** kütleyi izlemelidir. Bu, **Sınav 2'nin** ("yayılan disk")
başarısızlığının da yeniden okunmasını gerektirir — 7.4'e kalem olarak yazıldı.

### 5.12.6 İşlenen yerler

M-38: Varsayım 3'e "artık teorem" kaydı · yeni bölüm *"$h$'ın $R$-Bağımsızlığının Türetimi"*
(marj tablosu, $\eta_E$ duyarsızlığı, iç içe tabaka sonucu, NGC 891 yeniden hesabı, üç eksik
kaydı, flaring düzeltmesi) · Açık Uçlar'da $h$ kalemi kapatıldı.

---

## 5.11 3.9.4 ÇELİŞKİSİ ÇÖZÜLDÜ — açısal momentum bütçesiyle (3 Ağustos 2026)

### 5.11.1 Çelişki

3.9.4 aynı bölüm içinde iki zıt şey söylüyordu:

| Paragraf | İddia |
|---|---|
| **Açılış** | *"Ay'ın 3,8 cm uzaklaşmasının **asıl kaynağı** kozmolojik bir süreçtir"*; uzaklaşma + gün uzaması + yörünge yavaşlaması = *"tek kozmolojik sürecin **üç yüzü**"*; gelgit frenlemesi *"yalnızca ikincil bir katkı"* |
| **Karşı-kayıt** | *"Kozmolojik seyrelme… bu tablonun üzerine binen, işaretten bağımsız ve **çok daha yavaş bir taban terimidir**; uydunun net kaderini lob teriminin işareti belirler"* |

### 5.11.2 Ayırt edici muhasebe — iki bağımsız ölçüm

| Ölçüm | Kaynak | Değer |
|---|---|---|
| Ay'ın kazandığı $dL/dt$ | LLR, $dr/dt=3{,}8$ cm/yıl | $+4{,}50\times10^{16}$ kg·m²/s² |
| Dünya'nın kaybettiği $dL/dt$ | gün uzaması 2,3 ms/yüzyıl (gelgit bileşeni) | $-4{,}93\times10^{16}$ |
| **Denge** | — | **%91** |

**Bütçe gelgit aktarımıyla tek başına kapanıyor.** Kozmolojik terime kalan pay $\lesssim$%10.

### 5.11.3 Neden bu tuzağa düşülmüş — ve ikinci ölçüm nasıl kesiyor

Kozmolojik tahminin mertebesi **tesadüfen çok yakın:** $r_{Ay}H_0=2{,}75$ cm/yıl, gözlenenin
**%72'si.** Bu yakınlık gerçek ve yanıltıcı.

Ayrımı kesen ikinci ölçüm **kayma açısı**:

| Senaryo | $k_2\sin2\varepsilon$ | $\varepsilon$ ($k_2=0{,}30$) |
|---|---|---|
| Lob %100 | 0,0256 | **2,45°** — gözlenen ~3° ✓ |
| Kozmolojik %72 | 0,0072 | **0,68°** — gözlenenin ¼'ü ✗ |

### 5.11.4 Karar ve işlenen yerler

**Lob torku baskın; kozmolojik seyrelme taban terimi ($\lesssim$%10).** Ve **gün uzaması ayrı bir
imza değil** — aynı aktarımın öteki ucu. "Üç yüz" iddiası ikiye iner ve ikisi tek olguya bağlanır.

| Yer | Ne yapıldı |
|---|---|
| **3.9.4 sonuç paragrafı** | Baştan yazıldı: iki aday, bütçe tablosu, "neden karıştırılmaya açık" kutusu ($rH_0$ tesadüfü), kayma açısıyla ayrım, karar + iki alt sonuç, düzeltme kaydı |
| **3.9.1** | *"asıl kaynağı bu yerel sürtünme değil, kozmolojik"* → **aktarım**, %91 bütçe, kozmoloji taban |
| **3.9.7 (arşiv paragrafı)** | *"gün uzaması seyrelmenin üç imzasından biri"* → arşivin **aradığı şey değişti**: birincil sınav aktarım bütçesinin çağlar boyunca kapanması, kozmolojik taban ikincil ve hassasiyet altında. **Dürüst kayıt eklendi:** paleontolojik gün-uzunluğu kayıtlarının bilinen gerilimi, teorinin de standart açıklamayı kullandığı ve **ayrı öngörüsü olmadığı** yazıldı |
| **11.1.9 açık kalem** | "Açık kalem" → **"Kapanmış kalem"**; 3.9.4 ile gerilim kaydı kaldırıldı, yerine bütçe sayıları |

### 5.11.5 Dürüstlük kaydı — bu bir kazanım değil, bir düzeltme

Bu tur teoriye yeni bir öngörü **kazandırmadı**; tersine **bir iddiayı geri aldı.** Uzaklaşma ve
gün uzaması artık standart gelgit muhasebesiyle **ortak** açıklanıyor ve teorinin bu iki olguda
ayrışan bir sözü yok. Kazanç yalnızca tutarlılıkta: iç çelişki kalktı ve kozmolojik taban
gerçekçi (ölçülemez) konumuna indi.

---

## 5.10 $r_0$ TÜRETİLDİ — serbest parametre değildi, kitap onu zaten ölçüyordu (3 Ağustos 2026)

### 5.10.1 Türetim

F4'ün genliği ve F1 ile kesişme yarıçapı, 6.5.4.3'ün kendi zincirinden **kapalı biçimde** çıkar.
İki ivme:

$$a_{F1}=\frac{\mathcal{G}M}{r^2}\,,\qquad a_{F4}=\frac{\mathcal{G}M}{\ell_\omega^{etkin}\,R} \quad\text{(6.5.4.3 Adım 5+6, }\ \ell_\omega^{etkin}=\ell_\omega\sqrt N)$$

Eşitlendiğinde geçiş yarıçapı doğrudan düşer:

$$\boxed{\;r_0=\ell_\omega^{etkin}=\ell_\omega\sqrt{\frac{M}{m_n}}=\sqrt{\frac{\mathcal{G}M}{a_0}}\;,\qquad A_4=\frac{\mathcal{G}M}{r_0}=\sqrt{\mathcal{G}M\,a_0}\;}$$

*(Son eşitlik $a_0=\mathcal{G}m_n/\ell_\omega^2$ tanımıyla özdeştir; iki yazım arasındaki %6 fark
$a_0$'ın kalibre değeri ile M-45 türetimi arasındaki bilinen %12'nin karekökü.)*

**Ve bu ifade kitapta zaten var:** 10.7.1'in ölçüm formülü $\ell_\omega^{etkin}(R)=\sqrt{\mathcal{G}M_{kaps}(R)/a_0}$'dır — yani **$r_0\equiv\ell_\omega^{etkin}$.** Kitap $r_0$'ı serbest
parametre sanarken aslında onu 141 galakside ölçüyordu.

### 5.10.2 Doğrulama — zaten yapılmış

| Ölçüt | Ölçülen | Türetim |
|---|---|---|
| Kütle üssü ($r_0\propto M^p$) | **0,506** | 0,500 ✓ |
| Yarıçap izi (galaksi içi sistematik) | **−0,025** (saçılma 0,091 dex) | 0 ✓ |
| Samanyolu $r_0$ | — | **10,4 kpc** — düz dönüş eğrisinin başladığı yer ✓ |

$r_0$'ın galaksiden galaksiye beş mertebe yayılmasının tamamı $\sqrt M$ çarpanıdır. **Serbest
kalem listesinden çıkar** ($A_4$ ile birlikte): Blok H'nin "üç bağımsız serbest kalem"i
($(Cq_n)$, $r_0$, $\kappa_5$) **ikiye** iner.

### 5.10.3 Ama gezegen ölçeğinde bir yanlışlama üretiyor

Türetilen yasa $\varepsilon(r)\equiv a_{F4}/a_{F1}=r/r_0$ verir. Dünya için $r_0=15{,}2$ AU:

| | Değer |
|---|---|
| $\varepsilon_{Ay}=r_{Ay}/r_0$ | $1{,}69\times10^{-4}$ |
| Apsidal katkı ($\Delta\varpi=-\pi\varepsilon$/yörünge) | $-0{,}406^\circ$/yıl |
| Gözlenen apsidal presesyon | $+40{,}7^\circ$/yıl |
| **Pay** | **%1,00** |

Ay kuramı LLR ile milimetre/mas mertebesinde modellenmiştir; **%1'lik modellenmemiş bir terim
kesin olarak dışlanır.** Ayrıca M-38'in kendi $\varepsilon_{Ay}<2\times10^{-5}$ sınırı 8,4 kat
ihlal edilir. Yani **F4 gezegen ölçeğinde işliyor olsaydı, Ay verisi teoriyi yanlışlardı.**

### 5.10.4 Kaçış zaten kitabın geçerlilik alanı — ve Ay verisi onu DOĞRULUYOR

M-38'in kendi koşulu: $1/R$ yasası **yalnız $h(R)=$ sabit** ise çıkar; yayılan (flaring) akı
tüpünde yasa $1/R^2$'ye döner ve *"küresel durumdan hiçbir ayrım kalmaz."* Sabit kalınlıklı akı
tüpü ise **dönerek desteklenen bir disk** gerektirir.

- **Galaksi:** diski var → F4 var → $r_0=10{,}4$ kpc ✓
- **Yalıtılmış gezegen/uydu:** disk yok → akı küresel → **F4'ün $1/R$ rejimi yok** → $\varepsilon=0$ ✓

Ve bu kısıt **uydurma değil, kitapta zaten ilan edilmiş.** 10.6.3'ün kapsam kaydı:

> *"bu 16 galaksi HI halkası olan, **dönen** erken tiplerdir… Basınç-destekli sistemler —
> eliptiklerin yıldız kinematiği, cüce küreseller — teorinin bugünkü **geçerlilik alanının
> dışındadır**."*

**Kazanç:** M-38'in $h=$ sabit varsayımı, "sessiz varsayım"dan **gözlemsel olarak gerekli
koşula** yükselir. Ay'ın apsidal presesyonu artık bir yanlışlama değil, disk koşulunun
**bağımsız doğrulamasıdır**: F4 disksiz de işliyor olsaydı %1'lik anomali görülürdü, görülmüyor.

### 5.10.5 Bedel: §5.3 diferansiyel dönüş hattı gezegen ölçeğinde ölüyor

Türetilmiş $A_4=\sqrt{\mathcal{G}Ma_0}=174{,}8$ m²/s² ile Dünya yüzeyinde
$\lambda=a_{F4}/a_{merkezkaç}=8{,}1\times10^{-4}$ — 6.6.2'nin $10^{-4}$'ünden **8 kat büyük**,
ama $\lambda\to1$ hedefinden hâlâ **1200 kat** uzak. Ve disk koşulu uygulanırsa gezegen ölçeğinde
$\lambda$ **tam sıfırdır.**

**Sonuç:** *"F4 merkezkaçı yener, dönen cisimler bu yüzden parçalanmaz"* tezi, **yalıtılmış
gövdeler için kapanmıyor** — çünkü F4'ün $1/R$ rejimi orada mevcut değil. Tezin yaşayabileceği
yer disk-destekli sistemlerdir; oradaki karşılığı ise gezegen figürü değil, **disk kararlılığı**
olur. §5.3 bu kapsamla yeniden çerçevelenmelidir.

### 5.10.6 İşlenen yerler (3 Ağustos 2026)

| Dosya | Ne yapıldı |
|---|---|
| **Ek M-38** | Açık uç 1 kapatıldı; yeni bölüm *"$r_0$'ın Türetimi — serbest parametre değildir"* (kesişim türetimi, $r_0\equiv\ell_\omega^{etkin}$ kimliği, 141-galaksi doğrulama tablosu, Ay apsidal denetimi, disk koşulunun gözlemsel zorunluluğu). Kalan boşluk **$h$** olarak yeniden tanımlandı. |
| **Blok H parametre tablosu** | $r_0$: **F** → **T**, "Ek C P1 ile bağlı" kaydı kaldırıldı |
| **Blok H kapanış zinciri** | *"bağımsız serbest kalemler yalnız **üçtür**: $(Cq_n)$, $r_0$, $\kappa_5$"* → **ikidir**: $(Cq_n)$, $\kappa_5$ |
| **Ek C** (1.3) | **Yeni satır 21** — $r_0$, rozet **[T]**, türetim + doğrulama + geçerlilik alanı |
| **Ek C.1 dürüst sayım** | Yeni gerekçe **(0)**: $r_0$ ve $A_4$ türetildi, P1 bağı koptu, Blok H sayımı üçten ikiye indi. *(Ek C'nin 5 skaler + 2 profil başlık sayımı değişmez — $r_0$ orada zaten ayrı kalem değildi.)* |
| **Ek D** | $\ell_\omega^{etkin}$ girdisine **$\equiv r_0$** kimliği eklendi — nicelik zaten **[T]** rozetliydi, eksik olan tek şey $r_0$'ın o nicelik olduğunun görülmesiydi. $v_0,r_0$ girdisi ve bilanço notu güncellendi. |
| **Blok G** | *"$v_0$ ve $r_0$ … **serbesttir** [Ek C, P1]"* → türetildi, P1'in kalan içeriği yalnız yoğunluk profilinin biçimi |
| **6.6.2 (Sınav 1)** | $r_0$'ın serbest olduğunu varsayan paragrafa güncelleme kutusu: türetilmiş $A_4$ kalibre sınırın 8,4 katı → Ay apsidal presesyonu %1 → F4 gezegen ölçeğinde yok → **aşağıdaki F4 payı hesabı gezegen figürü için geçersiz**, dolayısıyla $\kappa_5\lesssim0{,}02$ sınırı bu tarafta **güçleniyor** |

**Beklenmedik teyit:** Ek D, $\ell_\omega^{etkin}$'i baştan beri **"türetilmiş (T)"** diye
işaretlemiş. Yani nicelik zaten türetilmiş sayılıyordu; kitabın kaçırdığı tek şey $r_0$'ın
**o niceliğin ta kendisi** olduğuydu. Türetim yeni bir sonuç üretmedi — mevcut iki kaydın aynı
şey olduğunu gösterdi.

### 5.10.7 Kalan tek açık uç

$h$'ı ne belirler? Disk kalınlığı gözlemden bilinir (21 cm), ama teoriden türetilmemiştir — ve
Güneş Sistemi'nin kendi gezegen diskinin "disk" sayılıp sayılmayacağı da tanımlanmamıştır. Bu,
M-38'in kalan **tek** yapısal boşluğudur ve artık $r_0$ değil, **$h$**'tır. *(M-38'in
"flaring öngörüsü" bunu kısmen sınanabilir kılıyor: $h$ arttığı yarıçapta dönüş eğrisi düzlükten
sapmalı; 21 cm kalınlık profili ile dış kol birlikte fit edilmelidir.)*

---

## 5.9 M-39 SINAV 1 İLE HİZALANDI — Anayasa'nın bekleyen bedeli kapandı (3 Ağustos 2026)

Anayasa'nın devam notu şunu kayda geçirmişti: *"Ek M-39 şu an hâlâ 'imza $J_4$'tedir' ve
'$\kappa_5\lesssim0{,}1$' diyor; Sınav 1 ikisinin de düzeltilmesi gerektiğini gösterdi."*
**İkisi de düzeltildi**, altı yerde:

| # | Yer | Eski | Yeni |
|---|---|---|---|
| 1 | M-39 başlık bölümü | *"İmza $J_2$'de değil $J_4$'tedir"* | *"İmza F5'te değil F4'tedir — ve $\kappa_5$ elenmiştir"* |
| 2 | M-39 gövde | profil farkından $J_4$ imzası çıkarımı | **çürütüldü:** kuvvet profillerinin farkı potansiyelin multipolünü belirlemez; F5'in potansiyeli **saf $P_2$**, hiçbir harmonikte imza yok. Kutulu $\Phi_{yanal}/\Phi_{merkezkaç}=2\kappa_5(\rho_0/\rho_n)\phi^2$ eklendi |
| 3 | M-39 sınır | $\kappa_5\lesssim0{,}1$ ($\rho_0/\rho_n=\tfrac18$, $k=\tfrac12$, %0,5) | **$\kappa_5\lesssim0{,}02$** ($\tfrac14$, $k=0$ Sınav 4, %0,42) — çalışma değeri **on kat** fazla; Sınav 1↔4 bağımlılığı kaydedildi |
| 4 | M-39 Açık Uç 1 | *"$\kappa_5$'in $J_4$'ten kalibrasyonu (öncelikli iş)"* — 4 cisimden tek $\kappa_5$ | **YÜRÜTÜLEMEZ** ilan edildi; Güneş satırının $\phi_\odot\approx0$ hatası ayrıca kaydedildi. **Yerine:** aynı çok-cisimli sınav **F4** üzerinden — engel $A_4$/$r_0$'ın türetilmemiş olması (M-38'in kalan boşluğu) |
| 5 | M-39 Geçerlilik + H.0 parametre tablosu + H.3 kısıt satırı | $\lesssim0{,}1$ | $\lesssim0{,}02$, gerekçesiyle |
| 6 | H.1 özet tablosu | *"imza $J_4$'te"* | *"figür harmoniklerinde imza YOK (saf $P_2$) — kalan tek imza 45° deseni"* |

**Yeni bölüm eklendi: "$J_4$ kanalı gerçekten açık — ama F4 için."** Merkezkaç $J_4$'e birinci
mertebede katkı vermez, F4 verir; indüklenen $J_4$ %4–8, **işaret kontrolü geçti** (F4'ün $P_4$
katsayısı pozitif → negatif $J_4$; gözlenen de negatif ve hidrostatikten derin). Ayrıca F4'ün
$P_2$ katkısı $J_2$'yi **azaltır** — şişmeye karşı çalışır, 11.2.3'ün aday mekanizması. Dürüst
sınır da yazıldı: hidrostatik referans ~%10 belirsiz, manto katkısı ayrıştırılmamış → *"olumsuz
olmayan ilk sonuç"*, geçilmiş sınav değil.

**Sonuç:** F5 çürütülmedi ama **görünmez** oldu — gözlemsel içeriği yalnız 45° desenine kaldı.
Anayasa'nın "bilinen bedel" kaydı artık geçerli değil; M-39 ile gövde metni (11.2) hizalı.

---

## 5.8 M-22'ye MERKEZKAÇ PARAGRAFI + 11.2 DÜZELTMESİ (3 Ağustos 2026)

### 5.8.1 M-22 — yazarın paragrafı düzeltilerek işlendi

Yazar M-22'ye bir "Merkezkaç Kuvvetinin Mekanik Temeli" paragrafı eklemişti. **Tez doğru
(merkezkaç sanal değil), gerekçesi iki yerde hatalıydı:**

| Hata | Doğrusu |
|---|---|
| *"dönen ortamın oluşturduğu **dışa doğru** basınç gradyanı"* | $dP/dr>0$ basıncın dışa **arttığı** anlamına gelir; kuvvet $-\nabla P$ olduğundan **içe** bakar. Gradyan merkezcildir. |
| *"F1 (içeri itim) ile M-22 (dışarı itim) **kavgası**"* | F1 ile M-22 iki rakip kuvvet değil, **aynı gradyan.** F1 gradyanı kurar; M-22 o gradyanın ortamın dönüşüyle dengede olduğunu söyler — bir **denge koşulu.** |

**Ama yazarın sezgisi gerçek bir dışa-savrulma etkisini yakalıyordu** ve o etki bulundu:
gradyanın yönü değil, **iki yoğunluğun farkı.** Madde aynı gradyanı $\rho_n$ ile hisseder ve
$\rho_n=4\rho_0$ olduğundan ortamın hızında dönmeye kalksa gereken merkezcil ivmenin ancak
dörtte birini alır → **dışa savrulur**, ancak $v_\theta/2$'de dengeye oturur. Santrifüjde yoğun
maddenin dışa çökmesiyle aynı mekanizma.

**Bu, 2 çarpanını görmenin ÜÇÜNCÜ bağımsız yolu** (diğerleri: M-9'un doğrudan ifadesi,
M-25'in muhasebe zincirleri) ve M-9'un *"madde düşer, ortam dolaşır"* cümlesinin **mekanik
nedeni.** M-22'ye yön tablosu, döner-kova analojisi, savrulma türetimi, kutulu
$v_{madde}=v_\theta/2$ ve düzeltme kaydı olarak işlendi; "Kullanıldığı bölümler"e 11.3.1 ve
bağlı katalog (M-9, M-8, M-25) eklendi.

### 5.8.2 Bölüm 11.2 — üç yerde düzeltme

| Yer | Düzeltme |
|---|---|
| **11.2.3** ("Plazma ve Yıldızlar") | *"Tam iyonize plazmada $\phi\approx0$, yanal itim sıfırlanır"* **kaldırıldı.** Üç gerekçeyle: (i) kavrama nükleon düzeyindedir, iyonizasyon elektronu söker — kavramayı kimyasal bağa yüklemek "Evrenakı için katı madde yoktur" kuralıyla da çelişir; (ii) $\phi_\odot\approx0$ Güneş'in makro girdabını iptal eder ve Kısım 3.8'in tamamını yıkar; (iii) iki satır aşağıda **iyonize metalik hidrojenli** Jüpiter'e en yüksek $\phi$ verilir. Ayrıca istisna **gereksizdi**: Sınav 1 $\kappa_5\lesssim0{,}02$ ile F5'i her yerde görünmez buldu. Yerine: Güneş $J_2$'si uyumlu ama $\phi$ ölçümü **değil** ($\phi_\odot\lesssim0{,}9$), ve küçük çıkışı **iki büyük terimin birbirini yemesinden** olabilir (F4 merkezkaçın zıddına — 6.6.2 işaret kontrolü ✓). |
| **11.2.3** (yeni kazanç) | Oranın $\omega$'dan bağımsızlığı yazıldı: **bir hızda kararlı olan cisim her hızda kararlıdır** — dönen cisimlerin parçalanmaması için ayrı mekanizma gerekmiyor. Ayrıca $\rho_0/\rho_n=\tfrac14$'ün serbest olmadığı (M-8) kaydı. |
| **11.2 girişi + 11.2.4** | $J_4$ imzası F5'e atfediliyordu. Sınav 1: F5 **saf $P_2$**, hiçbir harmonikte ayrı imzası yok; imza **F4'te** (%4–8, işaret doğru). İkisi de düzeltildi, dürüst sınırlarıyla (hidrostatik referansın ~%10 belirsizliği, hidrostatik-olmayan manto katkısı). |

**Kalan (Ek M-39):** girdi hâlâ *"imza $J_4$'tedir"* ve *"$\kappa_5\lesssim0{,}1$"* diyor. Anayasa
bunu bilinen bedel olarak kaydetmişti; artık gövde metni düzeltildiği için **M-39 ile Kısım 11
arasında sapma var.** Sıradaki kalem.

---

## 5.7 ANİMASYON VE BETİK SWEEP'İ — kod içindeki virüs (3 Ağustos 2026)

Yazar talimatı: *"galaktik animasyonlara ve galaktik çalışmalara da bunları işle."* Virüs bir
yerde **kodun içinde** çıktı ve animasyon kitabın tam tersini öğretiyordu.

### 5.7.1 `Simulasyon/evrenaki_girdap_animasyonu.html` — üç hata, üçü düzeltildi

| # | Bulunan | Düzeltme |
|---|---|---|
| 1 | `drawSatellite`: `var w = omegaAt(sat.r, sn)` — **uydunun açısal hızı girdap profilinden ve spin'den alınıyordu** | `omegaMadde(sat.r)` — Kepler profili, **spin'den bağımsız.** Kaydırıcı 0'a çekilse de uydu dolanır. |
| 2 | `drawMass`: yorum *"Pervane/Kütle, sürüklediği sıvıdan DAHA HIZLI dönmelidir"*, kod gövdeyi girdaptan hızlı döndürüyordu (25,0 ↔ 17,5) | **Ters çevrildi** (1,2 ↔ 7,75). Yorum 3.8.1.1'in 439 katına ve 3.8.2'nin motoruna atıfla yeniden yazıldı; görünürlük sıkıştırması etiketlendi. |
| 3 | Tek profil (`omegaAt`) hem ortam hem uydu için kullanılıyordu | **İki ayrı profil:** `omegaMadde(r) ∝ r^(−3/2)` (F1, spin'den bağımsız) ve `omegaOrtam(r,sn) = 2·omegaMadde(r)·(1+sn)` — M-9'un tam 2 çarpanı tabanda, ω₁ katkısı kaydırıcıda. |

Efsane ve altyazı da yeniden yazıldı: *"Uydu — akıntıda sürüklenir"* → *"Uydu — **düşer**, akıntıya
kapılmaz"*; altyazı artık kaydırıcıyı 0'a çekmeyi bir **sınav** olarak sunuyor ve Merkür/Venüs
öngörüsünü doğru mekanizmaya (3.4.4 girdap rekabeti) bağlıyor, yörüngenin yokluğuna değil.

**Doğrulama (konsolda, kaynak fonksiyonlar birebir yeniden kurularak):** uydunun $\omega$'sı
spin'den bağımsız ✓ · spin=0'da ortam/uydu oranı **tam 2,000** ✓ · hız profili üssü **−0,500**
($v\propto1/\sqrt r$, kitabın türettiği) ✓ · gövde devri ortamdan yavaş ✓. Konsol hatasız.
*(Görsel doğrulama yapılamadı — Browser pane kapalıyken `requestAnimationFrame` duruyor.)*

### 5.7.2 Temiz çıkanlar

| Dosya / grup | Denetim |
|---|---|
| **Kısım 10** metni (10 dosya) | virüs yok ✓ — zincir zaten madde seviyesinde |
| `Simulasyon/kisim10/panel_*.html` | yasa değişmedi ($v^2=v_{bar}^2+\sqrt{\mathcal{G}Ma_0}$), güncelleme gerekmiyor ✓ |
| **Galaktik betikler** (`CALISMA/*.py`) | madde seviyesinde fit; tek eşleşme `gozlemsel_ayirma_sinavi.py`'de "asimetrik sürükleme" — elenmiş basınç desteği adayı, ayrı konu ✓ |
| `dokuz_postulat_turu.html` | *"lokal zarfı kendileriyle birlikte sürüklerler"* — bu **doğru** okuma (zarf eş-hareketli, sürtünme yok); dokunulmadı ✓ |
| `ay_yorunge_dengesi.html` | yörünge **düzlemini** anlatıyor (3.9.3), hızını değil ✓ |
| `ay_gelgit_sirali.html` | gelgit mekanizması; kapılışla ilgisi yok ✓ |

### 5.7.3 Üretim durumu

Değişiklikler **birikmiş durumda**; `firebase_update_site.py` / site üretimi **çalıştırılmadı**
([[toplu-uretim-kurali]]: yazar "set bitti" demeden koşum yok).

---

## 5.6 GALAKTİK CEPHE KAPANDI — tam sweep ve düzeltmeler (3 Ağustos 2026)

Yazar talimatı: *"her şeyi hallet bu galaktik problem olmaktan çıksın."* Kitap baştan sona
tarandı; virüsün bulunduğu her yer ve M-9 ile değişen her sayı düzeltildi.

### 5.6.1 Virüsün bulunduğu yerler

| Yer | Durum | Ne yapıldı |
|---|---|---|
| **3.8.1** — *"akıntı katmanlarına kapılmış… boşlukta düşmediğini"* | ✅ düzeltildi | Yörünge anlatısı yeniden yazıldı: gezegen kapılmaz, **aynı alanda düşer.** İki denge/iki yoğunluk kutusu eklendi; iki profilin **biçimi** aynı, **genliği** iki katlı. Eski yazımın kaydı düşüldü. |
| **11.3.1** — *"uydu bu akışkana hapsolur"* | ✅ düzeltildi (§5.5) | Başlık dahil baştan yazıldı |
| **Ek M-37** sıfırıncı mertebe | ⛔ **izin bekliyor** | Düzeltme metni 5.5.5'te hazır |

### 5.6.2 M-9 ile ikiye katlanan sayılar

Ortamın hızı artık türetiliyor: $v_\theta(R)=2\sqrt{\mathcal{G}M/R}$ — yani **o gövdenin kopma
hızının tam iki katı.** Mekanik sürükleme hipotezinin talebi böylece iki katına çıkıyor ve
argüman **güçleniyor:**

| Yer | Eski | Yeni | Ek kazanç |
|---|---|---|---|
| **3.8.1.1** (Güneş) | 430 km/s · 23 kat | **874 km/s · 439 kat** | 874 = **2× kopma hızı** (437) → çifte imkânsız |
| 3.8.1.1 (çekirdek notu) | "430'un elli katı altında" | "874'ün **yüz katı** altında" | — |
| 3.8.1.1 (soru cümlesi) | "katbekat hızlı" | "dört yüz kattan fazla hızlı" | — |
| **3.9.4** (Dünya-Ay) | 7,93 km/s · 17 kat | **15,8 km/s · 34 kat** | 15,8 = **2× kopma hızı** (7,91) |
| 3.9.4 md.3 | "17 katlık açık" | "34 katlık açık" | — |
| **Ek M-25** (katalog) | 23 ve 17 kat | 47 ve 34 olmalı | ⛔ **izin bekliyor** |

**Yeni ve genel sonuç:** her gövde için ortamın yüzey hızı $=2v_{kopma}$. Mekanik hipotez
gövdenin **kopma hızının iki katında** dönmesini talep eder — yani girdabı üretebilecek devirde
gövde var olamaz. Bu bir tesadüf değil, $v_\theta=2\sqrt{\mathcal{G}M/R}$'nin her yerde aynı
okunuşudur. 3.8.1.1 ve 3.9.4'e işlendi.

### 5.6.3 Etkilenmediği doğrulananlar

| Kalem | Denetim |
|---|---|
| $a_0$, $\ell_\omega$, BTFR, M-45 %12 kapanışı | M-38 Adım 4'te $C/\rho_n$ **açıkça** yazılı; yasa $v^2=R\,a_{madde}$ biçiminde ⟹ zincir madde seviyesinde ✓ |
| 173 galaksi fit kalitesi | dokunulmadı, medyan RMS 12,6 km/s ✓ |
| Kepler, $P_0$, R-5, M-42, ışık bükülmesi | dokunulmadı ✓ |
| 3.4.1 kütle-itim ispatı | M-22 geçerli (M-9 sahip çıkıyor) ⟹ ayakta ✓ |
| Simülasyon/HTML dosyaları | R-8 taraması: hiçbir fizik sayısı koda gömülü değil ✓ (bulunan "430" değerleri CSS/SVG koordinatı) |
| Anayasa, kitap özeti | eski sayı geçmiyor ✓ |

### 5.6.4 Galaktik cephede kalan: iki izin kalemi

1. **Ek M-37** sıfırıncı mertebe tanımı (metin 5.5.5'te hazır) — risk yok, sayısal sonuç değişmiyor.
2. **Ek M-25** muhasebe zincirleri: 23 → 47 ve 17 → 34; kutulu sonuçtaki
   $v_{girdap}/v_{mekanik}$ oranları ve "iki zincirin ortak okuması" cümlesi.

Bu ikisi işlenene kadar Kısım 3 ile Ek M arasında **bilinçli bir sayı sapması** vardır ve burada
kayıtlıdır. Onun dışında galaktik cephe kapanmıştır.

---

## 5.5 ÇARPAN SORUNU ÇÖZÜLDÜ — çarpan hata değil, virüs başka yerde (3 Ağustos 2026)

### 5.5.1 Kitap çarpanı zaten yazmış: Ek M-9

M-9'un Geçerlilik Sınırı, kelimesi kelimesine:

> *"Kütle çevresindeki gradyan bölgesinde ortam tepkisiz değildir — Euler denklemi gereği
> gradyana cevap verir; ama cevabı düşmek değil **dolaşmaktır**: $\dfrac{\nabla P}{\rho_0}=\dfrac{v_\theta^2}{r}$
> ... Katı deplasman cebi (nükleon) ise akıp dengelenemez; bütün hâlde itilir.*
> **Madde düşer, ortam dolaşır.**"

$\rho_0$ **açıkça** yazılı. Yani $\rho_0/\rho_n=1/4$ ve ondan doğan 2 çarpanı teorinin **kasıtlı
yapısıdır**, hata değil. Sonuç: $P_0$'a, R-5'e, M-42'ye, ışık bükülmesine **dokunmaya gerek yok.**

**Yazarın "merkezkaç reel olmalı" tezi böylece tam olarak doğrulanmıştır** — M-22 gerçek bir
denge ve M-9 ona $\rho_0$ ile açıkça sahip çıkıyor.

### 5.5.2 Newtonyen virüs: "kapılış yörüngeyi sağlar"

İki yerde, aynı hastalık:

| Yer | Metin | Sorun |
|---|---|---|
| **Ek M-37**, sıfırıncı mertebe | *"Cisim ortamla gider ($v_{bağıl}=0$). Kuvvet değil taşınmadır; **yörünge hareketinin kendisini sağlar**"* | M-9 ile doğrudan çelişir |
| **11.3.1** | *"Sürüklenme zarfı nedeniyle uydu bu akışkana hapsolur ($v_{yör}=v_\theta$)"* → $v_\theta=\sqrt{\mathcal{G}M/R}$ | iki yoğunluğu karıştırır |

**Virüsün cinsi:** *"gezegeni yörüngede ne tutuyor?"* sorusuna bir **taşıyıcı** aramak. Bu
Newtonyen bir soru kalıbıdır; teoride cevap taşıyıcı değil, **madde düşer.** Taşıma mekanizması
aramak, yörüngeyi bir kuvvet dengesi sanmaktan gelir.

**Gözlem M-9'u seçiyor:** gezegenler $\sqrt{\mathcal{G}M/r}$ hızında dolanır. Kapılış yörüngeyi
sağlıyor olsaydı $2v_{Kepler}$'de olurlardı.

**Postülat 7'nin doğru okunuşu:** sürüklenme zarfı bir taşıma mekanizması değil, **yerel
sürükleme bastırıcısıdır.** M&M null'u zarfın içinden gelir; yörünge zarftan değil serbest
düşmeden gelir. Zarf bir sınır tabakasıdır, akışın tamamı değil.

### 5.5.3 Zincirin tamamı kapandı

| Kalem | Durum |
|---|---|
| Galaktik zincir ($a_0$, $\ell_\omega$, BTFR, M-45 %12) | ✓ madde seviyesinde, **dokunulmaz** |
| Kepler | ✓ madde serbest düşer |
| M-22 / merkezkaçın reelliği | ✓ geçerli, M-9 sahip çıkıyor |
| $\rho_0/\rho_n=1/4$, $P_0$, ışık bükülmesi | ✓ dokunulmaz |
| 3.4.1'in kütle-itim ispatı | ✓ ayakta (5.4.4'ün endişesi kalktı) |
| **Kapılış hipotezi** | ✗ **reddedildi** — M-9 ve gözlem birlikte dışlıyor |
| **M-37 sıfırıncı mertebe + 11.3.1** | ✗ düzeltilecek (11.3.1 yapıldı; M-37 izin bekliyor) |

### 5.5.4 Kazanç: 2 çarpanı bir öngörüye dönüştü

$$\Delta v=v_\theta-v_{madde}=\left(\sqrt{\rho_n/\rho_0}-1\right)v_{madde}=v_{madde}$$

**Kayma, yörünge hızının kendisine eşittir** — her yarıçapta, her sistemde, serbest parametresiz.
Merkür 47,9 · Dünya 29,8 · Jüpiter 13,1 · Ay yörüngesi 1,02 · Güneş galaktik yarıçap 220 km/s.
$\rho_n/\rho_0=4$'ün doğrudan sınavı. 11.3.1'e tablo olarak işlendi.

**Yeni açık kalem:** zarf gövdeyle giderken çevre ortam iki kat hızlı aktığından zarf sınırında
bir **kayma tabakası** doğar; yitimi ve torku hesaplanmamıştır (M-43 altkritik bastırma adayı).

### 5.5.5 M-37 için hazırlanan düzeltme — İZİN BEKLİYOR

`Kisim_8_Ekler/18_5_Kuvvet_Matematigi.md`, M-37'nin "iki mertebe" kutusu. **Mevcut:**

> - **Sıfırıncı mertebe (sürüklenme):** Cisim ortamla gider ($v_{bağıl}=0$). Kuvvet değil
>   **taşınmadır**; yörünge hareketinin kendisini sağlar.

**Önerilen:**

> - **Sıfırıncı mertebe (zarf):** Gövdeyi saran zarf içinde bağıl hız sıfıra iner ve klasik
>   $F_d\propto\rho v_{bağıl}^2$ sürüklemesi kaybolur (M&M null'unun kaynağı). Bu bir **taşıma
>   mekanizması değildir** — yörünge hareketini sağlayan şey zarf değil, maddenin basınç
>   gradyanında serbest düşmesidir ($v_{madde}=\sqrt{\mathcal{G}M/R}$). Ortamın kendi dolaşımı
>   bundan ayrıdır ve $\sqrt{\rho_n/\rho_0}=2$ kat hızlıdır (**M-9**, "madde düşer, ortam
>   dolaşır"); zarf sınırında bir kayma tabakası kalır.

**Gerekçe:** mevcut yazım M-9'un Geçerlilik Sınırı ile doğrudan çelişiyor ve literal alındığında
gezegenleri $2v_{Kepler}$'e koyuyor. **Risk:** yok — M-37'nin birinci mertebesi ($\eta_E$, artık
kuplaj, $\tau_{ret}$) ve bütün sayısal sonuçları değişmiyor.

*(Aynı partide 4.1'in altı önerisi ve 4.4'ün Ek D senkronu da var.)*

---

## 5.4 $\rho_0$ ↔ $\rho_n$ ÇARPANI — bulundu, galakside sınandı, karantinaya alındı (3 Ağustos 2026)

### 5.4.1 Sorun

Aynı $dP/dr$'yi iki denklem tarif ediyor ve farklı yoğunluklara bölüyor:

$$\text{M-22 (ortam):}\ \ \frac{dP}{dr}=\rho_0\frac{v_\theta^2}{r} \qquad\qquad \text{M-2/M-35 (madde):}\ \ \frac{dP}{dr}=\rho_n\frac{\mathcal{G}M}{r^2}$$

Eşitlenince $v_\theta=\sqrt{\rho_n/\rho_0}\,\sqrt{\mathcal{G}M/r}=\mathbf{2}\sqrt{\mathcal{G}M/r}$.
Çarpan **tam** ($\rho_0/\rho_n=1/4$, R-5'ten türeme) ve **rejimden bağımsız** — düz dönüş
rejiminde de aynı 2 çıkıyor. 11.3.1 ise $|a_{radyal}|=v_\theta^2/R$ yazarak $dP/dR$'yi $\rho_0$'a
bölüp sonucu $\rho_n$'ye bölünmüş ivmeye eşitliyor: **iki yoğunluk karışmış.**

### 5.4.2 Galaktik sınav — 173 galaksi, SPARC rotmod

Çarpan galaktik zincire girseydi $v_{F4}$ ortamın hızı olurdu, yıldızlarınki yarısı, $v^2$'de
dörtte biri, dolayısıyla $a_0$ **16'ya bölünürdü**. Tüm örnekleme koşuldu
($v^2=v_{bar}^2+\sqrt{a_0\mathcal{G}M_{kaps}}$, $Y_{disk}=0{,}5$, $Y_{bulge}=0{,}7$, 3345 nokta):

| Senaryo | $a_0$ [m/s²] | Medyan RMS | Talebe oran |
|---|---|---|---|
| **Galaksilerin talebi** (ortak fit) | $6{,}7\times10^{-11}$ | **12,6 km/s** | 1,00 |
| Kitabın kalibresi | $7{,}67\times10^{-11}$ | 12,9 | 1,15 ✓ |
| M-45 türetimi | $8{,}60\times10^{-11}$ | 13,6 | 1,28 ✓ |
| **M-45/16 (çarpan doğruysa)** | $5{,}38\times10^{-12}$ | **27,6** | **0,08 ✗** |

Talep bandı (%10 RMS toleransı): $5{,}1\times10^{-11}$ – $8{,}6\times10^{-11}$.
Çarpan senaryosu bandın **on kat altında**; medyan RMS ikiye katlanıyor ve **173 galaksinin
132'si kötüleşiyor.**

$$\boxed{\text{Galaksiler } \rho_0/\rho_n \text{ çarpanının galaktik zincire girmesini dışlıyor.}}$$

### 5.4.3 Bunun anlamı — Kısım 10 güvende, hata yerel

Galaksiler, teorinin galaktik zincirindeki hızın **maddenin yörünge hızı** olduğunu söylüyor;
ortamınki değil. Dolayısıyla:

- **Kısım 10'un hiçbir sonucu etkilenmiyor.** $a_0$, $\ell_\omega$, BTFR, M-45 kapanışı — hepsi
  yerinde. Dünkü "14 kat sapma" endişesi galaktik veriyle **çürütüldü.**
- Hata, sonuçta değil **gerekçede**: 11.3.1'in profil teoreminin *sonucu* doğru
  ($v_*=\sqrt{\mathcal{G}M/R}$ — bu zaten maddenin dairesel yörünge şartı), ama *türetimi* yanlış.
  M-22 üzerinden gitmek gereksiz ve yanlış; doğru türetim tek satır: madde $a_{madde}$ altında
  dairesel yörüngede ise $v^2=R\,a_{madde}$. M-22'ye hiç gerek yok.
- Geriye M-22'nin **kendi** iddiası kalıyor: ortam saf dönüşteyse 2× döner. Bu bir yörünge
  iddiası değil, **ortam hakkında ayrı bir iddia** — ve tek gözlemsel sonucu Güneş yarıçapında
  220 km/s'lik Evrenakı rüzgârı olurdu.

### 5.4.4 Kalan iki kalem

1. **11.3.1 / M-37'nin gerekçesi düzeltilmeli** (sonuç değil). Kısım 11 açık, Ek M kapalı.
2. **M-22 kütle çevresinde geçerli mi?** Varsayım 2 "saf teğetsel akış" der; M-35'in pompası
   radyal akı üretir. Geçerli değilse hem 2× ortam dönüşü hem 220 km/s rüzgâr iddiası düşer,
   **ama 3.4.1'in "kütle-itim Euler'in zorunluluğudur" ispatı da dayanağını kaybeder.**
   *(Not: pompa salınımlıysa net radyal akı sıfırdır ve çelişki kalkar — $q_n$'nin sürekli mi
   salınımlı mı olduğu belirleyici, doğrulanmadı.)*

---

## 5.3 DİFERANSİYEL DÖNÜŞ HATTI VE MERKEZKAÇ ENTEGRASYONU — ✔ RESMİ OLARAK ENTEGRE EDİLDİ (3 Ağustos 2026)

> **Entegrasyon Kaydı (3 Ağustos 2026):** Merkezkaç kuvvetinin "sanal eylemsizlik" olmaktan çıkarılıp, dönen ortamın dışa dönük radyal basıncı olan **M-22** ile resmen özdeşleştirilmesi kitaba (Ek M, Kısım 6.6, Kısım 3, vs.) işlenmiştir. Bu entegrasyonun **Galaktik Düz Dönüş Eğrisini** bozmadığı, aksine $v_{yildiz} = v_{ortam} \sqrt{\rho_{ortam}/\rho_n}$ ilişkisiyle yıldızın hızını sabit $v_{ortam}$ profiline kilitleyerek düz eğriyi doğrudan türettiği ispatlanmıştır.

> **Statü uyarısı.** Bu bölüm 11.1'e **işlenmemiştir** ve olduğu gibi işlenemez. Kapsamı
> 11.1'i aşar (11.2 gezegen figürü, 3.8 Güneş girdabı, 6.6 Sınav 1). Burada tutulan şey
> bir tez, dayanakları, ve **karşısındaki nicel engel**dir. Yazar kararı bekliyor.

### 5.3.1 Tez (yazar)

1. Güneş **diferansiyel** döner; etki ekvator düzeyinde yoğunlaşır.
2. Ekvator düzleminde oluşan **eksenel itim (F4)** hem F5'i hem **merkezkaçı** yener.
3. Ekvatoral hız arttıkça F4 de onunla birlikte artar.
4. Dönen cisimlerin parçalanmamasının sebebi budur — **neredeyse tüm hızlarda.**
5. Kuvvet düzgün silindirik olsaydı başka sonuç verirdi; F4'ü ekvatorda aşırı büyüten şey
   **diferansiyel dönüştür.**
6. Güneş'in $J_2$'si sade hidrostatik olduğu için değil, **iki büyük terim birbirini yediği
   için** küçüktür.
7. Merkezkaç bu teoride sanal değil **reel** olmalıdır ve Evrenakı'da karşılığı bulunmalıdır;
   ikisi aynı kaynaktan beslendiği için ölçeklemelerinin **berabere** olması beklenir.

### 5.3.2 Merkezkaçın Evrenakı karşılığı zaten yazılı: M-22

$$\frac{dP}{dR}=\rho\,\frac{v_\theta^{2}}{R}$$

Dönen ortam kendi merkezkaç gereksinimini basınç gradyanıyla karşılar. Yani merkezkaç sanal
kuvvet değil, **dönen ortamın radyal basınç dengesidir.** F4 de aynı dönen ortamdan doğar.
Tek kaynak ⟹ aynı $\rho v^2$ ölçeklemesi ⟹ **beraberlik zorunlu, tercih değil.**

### 5.3.3 Yapısal sonuç: oran hızdan bağımsız

$$\lambda \equiv \frac{F_4}{F_{merkezka\varsigma}} = \text{sabit},\qquad \lambda\ne\lambda(\omega)$$

| Sonuç | İfade |
|---|---|
| **Hıza bağlı kopma eşiği yok** | Newton'da $\omega$ arttıkça merkezkaç/çekim oranı büyür ve 1'i aşar. Burada oran $\omega$ ile büyümez: **bir hızda kararlı olan her hızda kararlıdır.** |
| **Tavan kalkmaz, yükselir** | $v_{kopma}^{etkin}=v_{kopma}^{Newton}/\sqrt{1-\lambda}$; $\lambda\to1$'de tamamen kalkar |
| **$\lambda$ ölçülebilir** | $\lambda = 1-\dfrac{J_2^{ölçülen}}{J_2^{Newton,hidrostatik}}$ — her dönen gövde bir veri noktası |

Bu, 11.2'yi bir açıklamadan **Güneş Sistemi çapında bir $\lambda$ ölçümüne** çevirir.

### 5.3.4 Sınav 1 (Bölüm 6.6.2) tezi KISMEN DOĞRULUYOR

Kitapta zaten yapılmış ve **kitaba işlenmemiş** bir sınav var. İki bulgusu tezi destekliyor:

| Bulgu | 6.6.2'nin sözü | Tez açısından |
|---|---|---|
| **F4'ün işareti** | *"F4'ün pozitif $P_2$'si $J_2$'yi **azaltır** — yani şişmeye karşı çalışır ✓"* | **Tam olarak tezin dediği.** F4 merkezkaçın zıddına çalışıyor |
| **İmzanın yeri** | *"imza F5'te değil **F4**'te"* · $J_4$ kanalı açık, işaret doğru, %4–8 | Tezin "F4 baskın" vurgusuyla uyumlu |
| **F5 elendi** | $\kappa_5\lesssim0{,}02$ — *"yanal itim, gezegen figüründe ölçülebilir etki bırakmıyor"* | 11.2.3'ün $\kappa_5=0{,}5$ çalışma değeri **25 kat fazla**; Dünya'nın %0,42 fazlasını F5'e yüklemek artık savunulamaz |

**Bu, 11.2.3'ün "$\phi\approx0$, yanal itim sıfırlanır" cümlesinin neden yanlış olduğunun ikinci
ve bağımsız kanıtıdır:** F5 zaten her yerde görünmez ($\kappa_5\lesssim0{,}02$); Güneş'e özel bir
iptal gerekçesi uydurmaya gerek yoktu. Ve iptal gerekçesi olarak seçilen $\phi\approx0$,
Güneş'in girdabını da iptal ettiği için teorinin kendi omurgasını kesiyordu.

### 5.3.5 ⚠ İDDİA EDİLEN ENGEL DENETLENDİ — GEÇERSİZ

6.6.2 şunu diyor: *"F4, yüzeyde merkezkaçtan $10^{4}$ kat zayıftır"* · *"F4, F5'i götürecek
güçte değildir — dört mertebe yetersiz."* Bunu ilk turda tezin karşısındaki nicel engel olarak
kaydetmiştim. **Denetim sonucu: bu sayı kurulmamıştır ve engel sayılamaz.** Beş bulgu:

**(1) Aritmetik doğru.** $A_4=20{,}7$ m²/s², $\varepsilon_{yüzey}=3{,}3\times10^{-7}$,
merkezkaç/$g=3{,}45\times10^{-3}$, oran $9{,}6\times10^{-5}$ — hepsi birebir yeniden üretildi.
Hata hesapta değil zincirdedir.

**(2) Üst sınır, değer gibi yazılmış.** Girdi $\varepsilon_{Ay}<2\times10^{-5}$ bir **sınırdır**;
çıktı da sınırdır. "…$10^4$ kat zayıftır" bir ölçüm beyanıdır. "F4 F5'i götürecek güçte değildir"
cümlesi bu yanlış statüyü miras alır.

**(3) Rejim tutarsızlığı — asıl hata.** Aynı adım $r_0>1{,}9\times10^{13}$ m $\approx$ **128 AU**
veriyor. Bu, Ay yörüngesini **49.000 kat**, Dünya yüzeyini **3 milyon kat** $r_0$'ın *içinde*
bırakır. M-38 ise açıkça $r_0$'ın içinde yasanın $a\propto1/R$ değil **Rankine çekirdeği
$a\propto R$** olduğunu yazar. Hesap, kendi sonucunun geçersiz ilan ettiği bölgede dış rejim
yasasını kullanıyor — **döngüsel.**

İç rejimde yeniden kurulduğunda iki şey birden değişir:
- $\varepsilon_{yüzey}/\varepsilon_{Ay}=(R_\oplus/r_{Ay})^3=4{,}6\times10^{-6}$
  ⟹ $F_4/F_{merkezkaç}<2{,}6\times10^{-8}$ (dört değil **sekiz** mertebe), **ama**
- Ay $r_0$'ın içindeyse Ay'ın $A_4$ üzerindeki sınırı da buharlaşır:
  $\varepsilon_{Ay}=A_4r_{Ay}^3/(GMr_0^2)$ ile aynı gözlem $A_4\lesssim5\times10^{10}$ verir —
  $20{,}7$'ye göre **2,4 milyar kat gevşek.**

Yani $10^{-4}$ ne lehte ne aleyhte bir sayıdır; **kurulmamıştır.**

**(4) Kategori hatası.** $\Delta\varpi\simeq-\pi\varepsilon$ bağıntısı $a=A/r^2+B/r$ **merkezi**
yasası için türetilmiştir. F4 silindiriktir ($\hat R$, $\hat r$ değil) ve Ay'ın yörüngesi Dünya
ekvatoruna **18°–29° eğiktir** — orada F4 merkezi değildir, düzlem dışı bileşeni vardır ve
apsidal presesyonun yanı sıra **düğüm gerilemesi** üretir. Pertürbasyon analizi silindirik
geometri ve eğik yörünge için yeniden yapılmadan bu sınır F4'e ait değildir.

**(5) Dünya'nın sayısı, öznesiz cümleyle evrenselleştirilmiş.** "yüzeyde" = *Dünya'nın*
yüzeyinde; sınır *Ay'ın* yörüngesinden geliyor. Dünya neredeyse katı-cisim döner. Tez F4'ü
**diferansiyel dönüşün** beslediğini söylediğine göre bu sayı Güneş'e taşınamaz.

**Sonuç:** Tezin karşısında nicel bir engel yoktur — çünkü niceliğin kendisi yoktur. $A_4$
gerçekten serbesttir ve serbestliği 6.6.2'nin sandığından mertebelerce geniştir. Bu, tezi
doğrulamaz; **önündeki yolu açar.** Gerçek iş 5.3.6'daki iki kalemdir.

### 5.3.6 Açık uçlar — tezin yaşaması için kapatılması gerekenler

1. **$A_4$'ün genliği serbesttir.** 6.6.2: *"F4'ün genliği $A_4$'e, o da $1/R$ rejiminin iç kesim
   yarıçapı $r_0$'a bağlıdır — ve $r_0$'ın gezegen ölçeğindeki değeri teoride sabitlenmiş
   değildir."* Yani $10^{-4}$ türetilmiş değil, kalibre edilmiştir. Ama serbest bir parametreyi
   büyütmek öngörü üretmez; **$r_0$ türetilmeden bu hat sınav olamaz.** (M-38'in kendi "Açık
   Uçlar" listesinde de bu, bloğun *kalan tek yapısal boşluğu* olarak yazılıdır.)
2. **Diferansiyel dönüşün F4 geometrisine girişi türetilmemiştir.** M-38 düzgün silindirik akı
   varsayar ($h=$ sabit). Enleme bağlı $v_e(\theta)$ profilinin akı geometrisini nasıl değiştirdiği
   yazılmalı. Bu yapılmadan "diferansiyel dönüş F4'ü ekvatorda aşırı büyütür" bir hipotezdir.
3. **İşaret dağılımı çözülmeli.** F4 basıklığı azaltır (6.6.2 ✓), F5 artırır. 11.2.3 Dünya'da
   **fazla** ölçüyor; F5 elendiyse ($\kappa_5\lesssim0{,}02$) o fazla ne? Jeofizik zaten bağımsız
   açıklıyor olabilir — 6.6.2 bunu açıkça yazıyor: *"O açıklama fazlanın tamamını hesaba katarsa
   teorinin payı sıfıra iner."*
4. **Sınav 1'in kitaba işlenmemiş olması.** Anayasa'nın devam notu bunu bilinçli bir karar olarak
   kaydediyor ve bedelini de yazıyor: Ek M-39 hâlâ *"imza $J_4$'tedir"* ve *"$\kappa_5\lesssim0{,}1$"*
   diyor, ikisi de düzeltilmeli. Bu hat yazılacaksa o karar da açılmalı.

### 5.3.7 Değerlendirme

**Tezin yönü doğru, dayanağı kısmen hazır, niceliği açık.** Sınav 1 F4'ün işaretini bağımsız
olarak doğrulamış ve imzanın F4'te olduğunu söylemiştir — tez buraya oturur. Fakat $10^4$'lük
açık, "F4 merkezkaçı yener" ifadesini bugünkü sayılarla **taşımaz**; taşıması $r_0$'ın
türetilmesine bağlıdır. Bu yüzden hat, 11.1'e bir sonuç olarak değil, **Kısım 11'e ayrı bir
araştırma kalemi** ya da 6.6'nın devamı olarak girmelidir.

---

## 5.2 AYIRT EDİCİ SINAV — bölümün statüsü değişti (2 Ağustos 2026)

**Yazar talimatı:** "sınava dönsün." Bölüm artık tutarlılık türetimi değil, **ayırt edici sınav** taşıyor.

**Sınavın kaynağı (yazar tespiti):** *F4 Ay için kapalı, Güneş için değil; F5 de Güneş için açık.*
Ay kilitli → saf F1 → tensör $(+2,-1,-1)$, iz $=0$. Güneş dönüyor → F1+F4+F5.

### GEOMETRİ DÜZELTMESİ (yazar) — ilk türetimim yanlıştı

**Hatam:** F4'ü küresel-radyal $B/r$ terimi olarak aldım ve "iz sıfırdan çıkar" sonucunu buna
dayandırdım. **F4 küresel değil silindiriktir** (M-38: akı silindir yanağından geçer,
$a\propto1/R$, $R$ = dönme eksenine dik uzaklık). Ayrıca **F4 varsa F5 de vardır** (yazar
kuralı — ikisi de $\omega_1$ ürünü); F5 meridyeneldir ($-\hat\theta$, $\sin2\theta$).

**Doğru türetim** (sayısal Jacobian ile doğrulandı, ekvator düzleminde):

| Alan | Geometri | Tek başına tensör | İz |
|---|---|---|---|
| F1 | küresel $1/r^2$ | $(+2,-1,-1)$ | $0$ |
| F4 | silindirik $1/R$ | $(+1,-1,0)$ | $0$ |
| F5 | meridyenel $\sin2\theta$ | $(0,0,-2a_5/r)$ | $-2a_5/r$ |

$$(T_1,T_2,T_3)=\frac{A}{r^3}\bigl(2+\beta,\,-(1+\beta),\,-(1+\gamma)\bigr),\qquad \mathrm{tr}\,\mathsf{T}=-\gamma A/r^3$$
$\beta\equiv Br/A$ (F4), $\gamma\equiv2a_5r^2/A$ (F5). Özvektörler: gelgit ekseni · yörünge
doğrultusu · ekliptiğe dik.

**İki ayrı imza, iki ayrı kuvvetten:**
- **F4 → dejenerasyon kırılır, iz KORUNUR.** (İlk yazdığımın tersi.) Kuşak çember değil elips.
- **F5 → iz İHLAL EDİLİR.** $\nabla\!\cdot\!\vec a_5=-2a_5/r$ ekvatorda sıfır değil; kuvvetin
  kendisi orada sıfır ama türevi maksimum. **Bağıntı F5'in radyal yasasından bağımsız**
  ($n=1,2,3$ için sayısal olarak doğrulandı) — sonucun en sağlam kısmı.

**Newton arka planı:**
- Dejenerasyon kırılması: Newton'da $J_2$'den gelir, Güneş için $J_2(R_\odot/r)^2\approx5\times10^{-12}$;
  $\beta$'nın presesyon üst sınırı $10^{-9}$ → **200 kat keşif penceresi.**
- Boşlukta iz: Newton'da $\nabla^2\Phi=0$ gereği **tam sıfır**, her mertebede → **arka plan yok.**
  Temiz kanal budur.

**Newton neden üretemez.** Klasik dış alanda kaynağın dönmesi yer almaz ($J_2$ hariç, o da farklı açısal yapı) ve boşlukta iz $\nabla^2\Phi=0$ gereği **her kaynak için, her uzaklıkta** sıfırdır. Newton'da kilitli uydu ile dönen yıldızın tensörü aynı yapıdadır.

**Terk edilen kanal — skaler genlik.** Önce %46 oranını ölçüm kanalı yapmıştım
($\varepsilon_\odot=2(R_{ölç}/0{,}4602-1)$). **Apsidal presesyon bunu öldürüyor:** M-38'in
$\Delta\varpi\simeq-\pi\varepsilon$ bağıntısı, Merkür'ün $0{,}1''$/yy kalıntısıyla
$\varepsilon(\text{Merkür})<3{,}7\times10^{-10}$, 1 AU'ya taşınınca $\lesssim10^{-9}$ verir
(işaret de ters: $-\pi\varepsilon$ geri presesyondur, Merkür anomalisi ileri). Oranda beklenen
sapma $\sim5\times10^{-10}$ → ölçülemez. Skaler oran **sınav değil, tutarlılık sınırıdır.**

**Kalan gerçek kanal — tensörün özdeğerleri ayrı ayrı.** Sınav skaler bir sayıda değil,
tensörün **yapısında**. İki bağımsız imza (yukarıdaki geometri düzeltmesine bkz.):
dejenerasyon kırılması ($\beta$, F4) ve boşlukta iz ($\gamma$, F5). Gözlemsel karşılığı
gradyometri: Ay ve Güneş bileşenleri frekansta zaten ayrık, kilitli Ay kontrol görevi görüyor.

**Dürüst statü:** yapı türetilmiş ve parametresiz; iz bağıntısı F5'in radyal yasasından bile
bağımsız. **Genlikler öngörülmemiş** ($\kappa_5$ serbest [F]; $\beta$ presesyonla $\lesssim10^{-9}$).
Biçim: "şu sayı çıkmalı" değil, **"şu iki yapı bulunmalı, yoksa $\beta$ ve $\kappa_5$ şundan küçüktür."**

**Yapılmayan:** üç özdeğeri ayrı ayrı çekmek için gereken gradyometri hassasiyetinin
değerlendirmesi ($J_2$ ve okyanus yükleme arka planından ayrıştırma dâhil). 7.4 kalemine yazıldı.

**Ölçek kaydı (yazar):** F4/F5 dönüş kolundan beslenir; Güneş çok yavaş döndüğü için yerel pay
ölçülebilire yaklaşır ama belirleyici olamaz. Galakside aynı iki kuvvet baskındır. İki ortamın
Evrenakı dönme hızları kıyaslanabilir değildir — **Kepler evrensel yasa değil, belirli bir kol
dengesinin yerel sonucudur.** 11.1.8'in sonuna kutu olarak işlendi.

**Geri alınan hatam:** Ayırt ediciyi ilk denememde $r_t=\sqrt{\mathcal{G}M/a_0}$ geçiş yarıçapına ve **Oort bulutuna** bağlamıştım (Güneş için 8790 AU). **Yanlıştı:** Ek M-38 $1/R$ rejimini bireysel gövdelere değil **galaktik kolektif vortekse** atar ($r_0$ kpc mertebesi) ve Güneş Sistemi'ni açıkça Kepler rejiminde tutar. Doğru ayırt edici, uzaklık rejimi değil **kaynağın dönme durumudur.**

**İşlendiği yerler:** 11.1 giriş kutusu (statü değişti) · 11.1.6 (%46 → ölçüm kanalı notu) · **11.1.8 baştan yazıldı** (başlık "Newton'la Sınır ve Ayırt Edici Sınav"; özdeşlik tablosuna "kilitli kaynak için" kaydı; karışım türetimi; iki kanal; dürüst statü tablosu) · 11.1.9 (kapsam kaydı: kayma kanalında sınav yok, sınav 11.1.8'de).

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
| 2 Ağustos 2026 | **Diferansiyel dönüş hattı açıldı → §5.3** (yazar tezi). Merkezkaçın Evrenakı karşılığı M-22'de bulundu; $\lambda=F_4/F_{merkezkaç}$'ın hızdan bağımsızlığı ve kopma tavanının yükselmesi türetildi; $\lambda$'nın $J_2$'den ölçülebilirliği kuruldu. **6.6.2 (Sınav 1) taraması yapıldı:** F4'ün işareti bağımsız doğrulanmış (şişmeye karşı ✓), imza F4'te, $\kappa_5\lesssim0{,}02$ ile F5 elenmiş — bu, 11.2.3'ün "$\phi\approx0$" cümlesinin ikinci bağımsız çürütmesi. **Ama $10^4$'lük nicel açık kaydedildi** ($\lambda_\oplus\approx10^{-4}$); diferansiyel dönüş bunu kapatmıyor. Hat 11.1'e **işlenmedi**, ayrı araştırma kalemi olarak duruyor. |
| 2 Ağustos 2026 | **§5.3.5 denetlendi ve geri alındı.** 6.6.2'nin *"F4 merkezkaçtan $10^4$ kat zayıftır"* sayısı tezin karşısındaki engel diye kaydedilmişti; denetimde **kurulmamış** olduğu çıktı (5 bulgu: üst sınır değer gibi yazılmış · **rejim tutarsızlığı** — $r_0>128$ AU kendi zincirini geçersiz kılıyor, Ay 49.000 kat içeride · iç rejimde $A_4$ sınırı 2,4 milyar kat gevşiyor · apsidal formül merkezi yasa için, F4 silindirik + Ay yörüngesi 18–29° eğik · Dünya'nın sayısı öznesiz evrenselleştirilmiş). **Tezin önünde nicel engel yok**; gerçek iş 5.3.6'daki $r_0$ türetimi. |
| 3 Ağustos 2026 | **$\rho_0/\rho_n$ çarpanı bulundu ve galakside sınandı → §5.4.** M-22 ile M-2 aynı $dP/dr$'yi farklı yoğunluklara bölüyor; tam 2 çarpanı, rejimden bağımsız. **173 SPARC galaksisinde test edildi** (3345 nokta): galaksiler $a_0=6{,}7\times10^{-11}$ talep ediyor, çarpan senaryosu ($5{,}4\times10^{-12}$) bandın 10 kat altında, medyan RMS 12,6→27,6 km/s, 132/173 kötüleşiyor. **Çarpan galaktik zincire girmiyor — Kısım 10 güvende.** Hata sonuçta değil gerekçede: 11.3.1'in profil teoremi doğru sonucu yanlış yoldan çıkarıyor. Kalan: M-22'nin kütle çevresinde geçerliliği (3.4.1'in ispatı buna bağlı). |
| 3 Ağustos 2026 | **ÇARPAN SORUNU KAPANDI → §5.5.** Ek M-8 ve M-9 okundu. **M-9 çarpanı zaten yazmış:** *"Madde düşer, ortam dolaşır"*, $\nabla P/\rho_0=v_\theta^2/r$ — $\rho_0$ açıkça. Yani 2 çarpanı hata değil, teorinin kasıtlı yapısı; $P_0$/R-5/M-42/ışık bükülmesi **dokunulmadı**. Newtonyen virüs başka yerde: **"kapılış yörüngeyi sağlar"** (M-37 sıfırıncı mertebe + 11.3.1) — *"gezegeni ne tutuyor?"* sorusuna taşıyıcı aramak. Gözlem M-9'u seçiyor. **Kapılış hipotezi reddedildi.** Galaktik zincir, Kepler, M-45, 3.4.1 hepsi ayakta. **11.3.1 yeniden yazıldı** (iki denge/iki yoğunluk, serbest düşme türetimi, Postülat 7'nin doğru okunuşu, kayma tablosu, galaktik zincire etkisizlik). Çarpan bir **öngörüye** dönüştü: $\Delta v=v_{madde}$, parametresiz. M-37 düzeltmesi 5.5.5'te izin bekliyor. |
| 3 Ağustos 2026 | **GALAKTİK CEPHE KAPANDI → §5.6.** Tam sweep: virüs 3.8.1'de bulundu (yörünge anlatısının tamamını taşıyordu) ve düzeltildi. M-9 ile ikiye katlanan sayılar güncellendi: **3.8.1.1** 430→**874 km/s**, 23→**439 kat**; **3.9.4** 7,93→**15,8 km/s**, 17→**34 kat**. Yeni genel sonuç: ortamın yüzey hızı $=2v_{kopma}$ ⟹ mekanik hipotez gövdenin kopma hızının iki katında dönmesini talep eder, **çifte imkânsız** — argüman güçlendi. Etkilenmediği doğrulananlar: $a_0$/$\ell_\omega$/M-45/BTFR (M-38 Adım 4'te $C/\rho_n$ açık), 173 galaksi fiti, $P_0$/R-5/M-42, 3.4.1, simülasyonlar (R-8 taraması temiz). Kalan: **M-37 ve M-25** izin bekliyor. |
| 3 Ağustos 2026 | **KİLİTLER AÇILDI — bütün izin kalemleri tek partide işlendi.** Ek M-36 (altı öneri + iki açık uç kapatıldı + yeni açık uç), Ek M-37 (sıfırıncı mertebe → "zarf"), Ek M-25 (kapılış→serbest düşme, ortam profili $v_\theta=2v_{kopma}$, 874/439 ve 15,8/34, kopma-hızı kapanışı). Ek D zaten yapılmıştı. **Kısım 3 ↔ Ek M sapması kalmadı** (grep doğrulamalı). Galaktik cephe tamamen kapandı. |
| 3 Ağustos 2026 | **Animasyon/betik sweep'i → §5.7.** Virüs `evrenaki_girdap_animasyonu.html`'de **kodun içinde** bulundu: uydunun açısal hızı girdap profilinden ve spin'den alınıyor, gövde girdaptan hızlı döndürülüyordu (*"pervane sürüklediği sıvıdan daha hızlı dönmelidir"*) — kitabın tam tersi. İki ayrı profile ayrıldı (`omegaMadde` spin'den bağımsız, `omegaOrtam = 2×` M-9 tabanı), gövde devri ters çevrildi, efsane ve altyazı yeniden yazıldı. Konsolda doğrulandı: oran tam 2,000 · profil üssü −0,500 · uydu spin'den bağımsız ✓. Kısım 10, panel'ler, galaktik betikler ve diğer animasyonlar **temiz** çıktı. Üretim koşulmadı (toplu üretim kuralı). |
| 2 Ağustos 2026 | *(geçersiz — üstteki satırla değiştirildi)* İlk yazım turu (11.1.1–11.1.8). Yazarın kendi taslağı korundu, üzerine eklendi: akı korunumunun bağımsız türetimi (Gauss), özdeğer tablosu, artık basınç alanı $P_T$ tablosu ve 2:1 oranı, M-26 çapraz denetimi, büyük/küçük gelgit (0,781 / 0,289 / 2,70), **11.1.6** eşdeğerlik ilkesi, **11.1.7** Newton'la sınır tablosu, **11.1.8** geçerlilik sınırı + iç rejim kapanışı + 3° açık kalemi. Düzeltilenler: "milimetrik doğruluk" iddiası → mertebe-ve-yapı doğrulaması dürüstlük kaydı; $\pm P_T$ muğlaklığı → sayısal tablo; "ekvatordan sıkılan" → "yanaklardan"; başlık düzeyi `###`→`##` (11.2/11.3 ile hizalandı); 11.1.5 başlığı "Yükseklik"→"Genlik". **Ek D izinle işlendi** (4.4), $\xi$ çakışması çözüldü. **Kaynakça:** Touboul 2022 ve Schlamminger 2008 eklendi (11.1.6'nın EP sınavı için). Kısım 10'a ve M-36'ya **dokunulmadı.** |
