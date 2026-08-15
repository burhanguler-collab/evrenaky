# ÇALIŞMA DOSYASI — Güneş'in İç Dönme Profili ve Takoklin

> **Statü:** Çalışma dosyası. Yayın bölümü **değil**, site menüsüne kayıtlı **değil**.
> **Yöntem:** Bütün türetim ve denetim burada. Hedef dosyaya yalnız yazar *"sonuçlandı"*
> dediğinde, **tek partide**. Terk edilen rotalar silinmez.
>
> **Hedef dosya:** `Kisim_11_.../08_Gunesin_Ic_Donme_Profili_ve_Takoklin.md` (**11.8**, iskelet hazır)
> **Karne:** `websitesi/Metin/Akademik/00_KARNE_Dogrulama_Durumu.md`
>
> **Açılış:** 6 Ağustos 2026 · **Yazım planı:** 7 Ağustos 2026

---

## 0. NEDEN BU DOSYA

Kısım 11'in kriz taramasından çıktı. Kitabın 7.7'sinde **23 kriz kalemi** var, ama neredeyse
hepsi kozmoloji ve yüksek enerji astrofiziğinden. **Teorinin en güçlü olduğu alan — akışkan ve
dönme mekaniği — kriz envanterinde neredeyse yok.** Tarama sonucu: *"Güneş'in dönme profili /
takoklin"* kitapta **hiç geçmiyor** (0 dosya).

Oysa olgu teorinin tam merkezinde: bir dönen gövdenin **içindeki** ortamın nerede ve ne kadar
kavradığı sorusu. Kitapta bu soruyu soran bir makine zaten var (3.4.4'ün kavrama klifi), ama
**Güneş'in iç profiline hiç uygulanmamış.**

---

## 1. GÖZLEM TABANI

Helyosismoloji (SOHO/MDI, GONG, SDO/HMI) Güneş'in iç dönme hızını yarıçapın ve enlemin
fonksiyonu olarak ölçer. Üç ayrı yapı görülür ve **üçü de sağlam ölçümdür:**

| Bölge | Dönme davranışı | Değer |
|---|---|---|
| **Işınım bölgesi** ($r\lesssim0{,}7R_\odot$) | neredeyse **rijit** — enlemden bağımsız | $\Omega/2\pi\approx430$ nHz ($\approx26{,}9$ gün) |
| **Konveksiyon bölgesi** ($0{,}7$–$1{,}0R_\odot$) | **diferansiyel** — ekvator hızlı, kutup yavaş | ekvator $\approx456$ nHz ($25{,}4$ g) · kutup $\approx340$ nHz ($\approx34$ g) |
| **Takoklin** | ikisi arasındaki **ince kayma katmanı** | $r=0{,}693\pm0{,}003\,R_\odot$ · kalınlık $\lesssim0{,}04\,R_\odot$ |

Ek iki yapı:

- **Yüzeye yakın kayma katmanı:** $r>0{,}95R_\odot$'da dönme dışa doğru **azalır**.
- **Çekirdek** ($r<0{,}2R_\odot$): kötü kısıtlı, kararsız çözümler.

**Konveksiyon bölgesinin tabanı $0{,}713R_\odot$'dadır** — yani takoklin tabanın **hemen altında**
oturuyor, üstünde değil. Bu ayrıntı önemli olabilir.

**Nicel çerçeve:**

$$\frac{\Omega_{ekvator}}{\Omega_{kutup}}\approx1{,}34
\qquad
\frac{\text{takoklin kalınlığı}}{R_\odot}\lesssim0{,}04
\qquad
\frac{\Omega_{ışınım}-\Omega_{kutup}}{\Omega_{ekvator}-\Omega_{kutup}}\approx0{,}8$$

Son oran şunu söylüyor: **ışınım bölgesi kutup hızında değil, ekvatora yakın bir hızda dönüyor.**
Kayma katmanı bu yüzden kutuplarda daha keskin.

---

## 2. STANDART FİZİKTEKİ DURUM — kriz nerede tam olarak

**Kriz "açıklama yokluğu" değil, "türetim yokluğu"dur.** Ayrımı baştan yazmak gerekiyor, çünkü
hakem *"bu çözülmüş"* diye reddedebilir:

| Soru | Standart durumu |
|---|---|
| Diferansiyel dönme neden var? | **Açıklanır** — konveksiyon + Coriolis (Reynolds gerilmeleri) dönme momentumunu yeniden dağıtır |
| Profilin **biçimi** nereden çıkar? | **Türetilmez.** Ortalama-alan ve global konveksiyon simülasyonları profili üretmek için ayarlanır; gözlenen profil dinamo modellerine **girdi** olarak konur |
| Işınım bölgesi neden **rijit**? | Açık soru. Zayıf iç manyetik alan ya da dalga taşınımı öneriliyor; hiçbiri kesinleşmedi |
| Takoklin neden bu kadar **ince**? | **Açık soru.** Kendi başına bir literatür (*"tachocline confinement problem"*) — manyetik hapsetme mi, anizotropik türbülans mı? |

⟹ **Hedef üçüncü ve dördüncü satır.** Birinci ve ikinci satıra saldırmak hata olur.

> **⚠ Bu dosyanın ilk kuralı.** İddia *"standart fizik diferansiyel dönmeyi açıklayamıyor"*
> **olmayacak** — açıklıyor. İddia, varsa, şu olacak: *"profilin geçiş yarıçapı ve inceliği
> serbest parametreye başvurmadan çıkar."* Bu daha zayıf, ama savunulabilir bir hedeftir.

---

## 3. TEORİNİN ELİNDEKİ PARÇALAR — envanter

| Parça | Nerede | Ne veriyor | Statü |
|---|---|---|---|
| **İç kavrama kesri** $\mathcal{R}=\phi$ | Sözlük, M-15/M-16 | Kafesin **içindeki** ortamı yöneten oran; deplasman hacim kesri | **[T]**, serbest değil |
| **Dönme sürüklenme kesri** $\xi$ | Ek M-40 (+M-42) | $\vec\Omega_{ortam}=\xi\,\vec\omega_{gövde}$, $\ \xi=\frac{I}{MR^2}\frac{2\Phi}{c^2}$ | **[T]** |
| **Kavrama klifi** $g(R)$ | 3.4.4 | Ortamın gövde **spinine** tutunmasının keskin kesilmesi | fenomenoloji |
| **Zarf sınıfları** | 11.3 | rijit → plazma → fırlatılmış → tavan | **[T]** |
| **DY-2** | Ek M | $v_{ortam}=2v_{madde}$, $\Delta v=+v_{madde}$ | **[T]** |
| **Yörünge kuplajı** $\gamma\propto\Delta v^4/(\rho_cr_t)$ | 11.4.8 + M-43, 11.5.3'te kalibre | Ortam–madde kuplajının **kalibre edilmiş** yasası | **[T]** |

**İlk hesap (yapıldı, kaydedilir):** Güneş için dönme sürüklenme kesri

$$\xi_\odot=\frac{I}{MR^2}\cdot\frac{2\Phi}{c^2}
=0{,}070\times\frac{2\times1{,}907\times10^{11}}{8{,}988\times10^{16}}
=\mathbf{3{,}0\times10^{-7}}$$

Dünya'nın $4{,}605\times10^{-10}$'una göre **645 kat** büyük, ama hâlâ $10^{-7}$.
⟹ **Ortamın Güneş'in dönüşüne dışsal tutunması bu profili süremez.** Aranacak yer $\xi$ değil,
**iç kavrama** ($\phi$) ve klifin kendisi.

---

## 4. GERİLİM VE BOŞLUK — asıl iş

### K-1 · GEÇİŞ YARIÇAPI TEORİDEN ÇIKAR MI? *(ana kalem)*

Takoklin $r=0{,}693R_\odot$'da. Teori bu yarıçapı **bağımsız olarak** üretebilir mi?

Aranacak yerler: iç kavrama kesri $\phi$'nin yoğunlukla değişimi · deplasman yüzeyi $R_\phi$'nin
Güneş için nerede oturduğu (11.4.1'de tanımlı) · 11.3'ün zarf sınıfı geçişinin karşılığı.

**Denetim ölçütü baştan:** yarıçap **serbest bir parametre ayarlanarak** tutturulursa kalem
kapanmaz, düşer. Tutması için girdisi kitapta zaten türetilmiş bir nicelikten gelmeli.

### K-2 · İNCELİK — $\lesssim0{,}04R_\odot$ neden bu kadar keskin?

Standart fizikte bu ayrı bir problem (*tachocline confinement*). Teorinin klifi **dik** olduğu
için ilk bakışta uygun görünüyor — 3.4.4 aynen: *"kavrama klifi çok dik olduğundan pençe fiilen
günberide kavrar."* Ama **diklik orada nicelleştirilmemiştir**; $g(R)$'nin biçimi yazılı değil.

⟹ Klifin **kalınlığını** veren bir bağıntı olmadan bu kalem açılamaz. İlk iş $g(R)$'nin
biçimini yazmak.

### K-3 · İŞARET — neden ekvator hızlı?

Gözlem: ekvator kutuptan **hızlı**. Teori bir işaret öngörüyor mu, yoksa ikisi de mümkün mü?

Bağlanacak yer: F5'in $\sin2\theta$ yasası (11.4.2–11.4.4) enlem bağımlılığı olan **tek** kuvvet.
F5 ekvatorda ve kutupta sıfır, $45°$'de maksimum — **diferansiyel dönmenin deseni ise monotondur.**
İkisi aynı biçimde değil. **Bu, kalemin olumsuz kapanma ihtimalinin en yüksek olduğu yer.**

### K-4 · IŞINIM BÖLGESİ NEDEN RİJİT?

11.3'ün **rijit zarf** sınıfı burada doğrudan işe yarayabilir: ışınım bölgesi konvektif
karışmadığı için kafesi bozulmamış bir "rijit zarf" gibi davranıyor olabilir.
**Ama dikkat:** 11.3 yıldızları kütle–spin yasasının **dışında** tutuyor (dönüşleri yaşla
belirlenir, Skumanich). Zarf sınıfını yıldızın **içine** taşımak yeni bir adımdır ve
gerekçelendirilmeden yapılamaz.

---

## 5. BAŞTAN GÖRÜLEN TUZAKLAR — bunlara düşmeyeceğiz

| # | Tuzak | Neden |
|---|---|---|
| **T-1** | **Güneş'in yavaş dönüşünü yeniden açmak** | Kitap o kalemi kapatmış: 11.2.7 önerilen *"sızma kesri $\varepsilon$"*'yi **sınayıp geri çekti**, ve 3.4.4 *"manyetik frenlemeyi dışlamadığından güneş açısal momentum problemi için teoriye ek parametre gerekmez"* diyor. **Bu dosyanın konusu iç profil, genel dönüş hızı değil.** |
| **T-2** | Standart fiziğe *"diferansiyel dönmeyi açıklayamıyor"* demek | Açıklıyor (§2). Hedef **türetim**, açıklama değil |
| **T-3** | Geçiş yarıçapını serbest parametre ayarlayarak tutturmak | 11.4.9'un geçiş yarıçapı kaydıyla aynı standart: türetilmezse **kazanılmış sınav sayılmaz** |
| **T-4** | Yıldızlar için kütle–spin yasasını kullanmak | 11.3 yıldızları **kapsam dışı** bırakıyor (yaşla belirlenen dönüş) |
| **T-5** | Konveksiyonu ortamla açıklamaya çalışmak | Konveksiyon standart termodinamiktir; teorinin orada işi yok, ve girmek gereksiz cephe açar |
| **T-6** | $\xi$'yi iç profile uygulamak | $\xi$ **dışsal** sürüklenmedir ($3{,}0\times10^{-7}$, §3) — iç kavrama $\phi$ ile karıştırılmayacak. *(Bu, oturma dosyasının üç kez ısırdığı "hangi nicelik maddeye, hangisi ortama ait" virüsünün aynısı.)* |

---

## 6. SIRA

| Sıra | Kalem | Tür | Durum |
|---|---|---|---|
| **1** | **$g(R)$'nin biçimini yazmak** — klifin kalınlığı ve konumu | türetim | ⬜ **açık, önkoşul.** K-1 ve K-2 buna bağlı |
| 2 | **K-1** — geçiş yarıçapı | türetim + sınav | ⬜ ana kalem |
| 3 | **K-2** — incelik | türetim | ⬜ 1'e bağlı |
| 4 | **K-3** — işaret ve genlik | denetim | ⬜ **olumsuz çıkma ihtimali yüksek** (F5'in $\sin2\theta$'sı monoton desene uymuyor) |
| 5 | **K-4** — ışınım bölgesinin rijitliği | kavramsal | ⬜ T-4'e dikkat |
| son | Kaynakça kalemleri | derleme | ⬜ taşımada |

---

## 7. KAYNAK ADAYLARI *(taşımada 11.9'a)*

- **Schou, J., ve ark. (1998).** *Helioseismic studies of differential rotation…* ApJ 505, 390. (SOHO/MDI iç dönme profili — ana referans.)
- **Kosovichev, A. G., ve ark. (1997).** Takoklinin yeri ve kalınlığı.
- **Charbonneau, P., ve ark. (1999).** *Helioseismic constraints on the structure of the solar tachocline.* ApJ 527, 445.
- **Spiegel, E. A., & Zahn, J.-P. (1992).** *The solar tachocline.* A&A 265, 106. (Hapsetme probleminin kurucu makalesi.)
- **Howe, R. (2009).** *Solar interior rotation and its variation.* Living Reviews in Solar Physics. (Derleme.)

*(Künyeler taşıma anında doğrulanacak — bu satırlar aday listesidir, kaynakçaya doğrulanmadan
girmez.)*

---

## 8. GÜNLÜK

| Tarih | İşlem |
|---|---|
| 6 Ağustos 2026 | Dosya açıldı. Kısım 11'in **kriz taramasından** doğdu: 7.7'nin 23 kaleminin neredeyse hiçbiri akışkan/dönme mekaniğinden değil, ve *"Güneş'in dönme profili / takoklin"* kitapta **0 dosyada** geçiyor. Gözlem tabanı kuruldu (§1): ışınım bölgesi rijit ($\approx430$ nHz), konveksiyon bölgesi diferansiyel (ekvator $456$ ↔ kutup $340$ nHz, oran $1{,}34$), takoklin $r=0{,}693R_\odot$ ve kalınlık $\lesssim0{,}04R_\odot$. **Krizin yeri kesin olarak sınırlandı** (§2): standart fizik diferansiyel dönmeyi **açıklıyor** ama profilin biçimini **türetmiyor**; ışınım bölgesinin rijitliği ve takoklinin inceliği ise kendi başına açık sorulardır (*tachocline confinement problem*). ⟹ Hedef üçüncü ve dördüncü satır; ilk ikisine saldırmak yasak (T-2). **İlk hesap yapıldı:** $\xi_\odot=3{,}0\times10^{-7}$ (Dünya'nın 645 katı ama hâlâ $10^{-7}$) ⟹ **ortamın dışsal tutunması bu profili süremez**, aranacak yer iç kavrama $\phi$ ve klifin kendisi. **Dört kalem açıldı** (K-1 geçiş yarıçapı · K-2 incelik · K-3 işaret · K-4 rijitlik) ve **önkoşul belirlendi:** $g(R)$'nin biçimi kitapta yazılı değil, K-1 ve K-2 ona bağlı. **Altı tuzak baştan yazıldı** (§5); en önemlisi **T-1**: Güneş'in genel yavaş dönüşü bu dosyanın konusu **değil** — kitap o kalemi 11.2.7'de kapatmış, *"sızma kesri $\varepsilon$"*'yi sınayıp geri çekmiş, ve manyetik frenlemeyi dışlamadığı için ek parametre gerekmediğini kaydetmiştir. **T-6** ise oturma dosyasının üç kez ısırdığı virüsün aynısı: hangi niceliğin maddeye, hangisinin ortama ait olduğu her adımda yazılacak. **Dürüst ön kayıt: K-3 olumsuz çıkabilir** — F5 enlem bağımlılığı olan tek kuvvet ama $\sin2\theta$ deseni ($45°$'de maksimum) gözlenen monoton desene uymuyor. |
