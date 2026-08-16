# ÇALIŞMA — Kutamların Dikey Birleşmesi: Katmanlaşma ve Zerre'ye Giden Yol

**Durum:** Tartışma açık — hiçbir kalem yayına taşınmadı.
**Açılış:** 16 Ağustos 2026 (yazar sorusu üzerine).
**Kapsam bekçisi:** Bu dosya *bileşim programına* aittir. Kutam hiçbir hesaba girmez
(1.6, Açıklama Tabanı); buradaki her nicelik **keşif düzeyinde** ve parametriktir.
Yayın adayı tek şey mekanizma anlatısıdır, sayılar değil.

---

## 0. Soru (yazarın koyduğu biçimiyle)

Kutamlar 4B fazıyla **yatayda** (kendi düzlemlerinde) bağ kuruyor — simülasyon bunu
işletiyor. Ama Zerre gibi üst katmanların doğması için Kutamların **üst üste binmesi**
(dikey birleşme) gerekiyor. Zerre 3B'de dönerken küre kabul edilmişti; az yoğun
Evrenakı'ya girince dönüşü hızlanıyor ve **disk** hâlini alıyor. İstiflenen Kutamlar
3B'de döndüğünde üst üste bağlar merkeze yaklaşıp diski üretmeli. **Dikeyde birleşme
nasıl olur?**

---

## 1. Teoriden eldeki yapıtaşları

| Yapıtaşı | Kaynak | Bu soruya katkısı |
|---|---|---|
| ω₂ ortak — bütün Kutlar aynı 4B dönüşün parçası | 1.4.12 | Faz kilidi **yönden bağımsızdır**: dikey komşu da eş fazlıdır |
| Bjerknes kuvveti $\kappa\cos\Delta\varphi/d^2$ | 12.3.2; Bjerknes 1906, Crum 1975 | Akustik monopol etkileşimi **izotroptur** — düzlem seçmez |
| Yoğunluk yasası $\rho=\rho_0 e^{-u}$, $u=\lvert v\rvert^2/2c_0^2$ | 1.3 / sim çekirdeği | Süperpozisyonun basınç imzasını **yön yönüne** okutur |
| Eş-yönlü çift **yan yana**: ortada hızlar götürür → $\rho=\rho_0$ **SIRT** | 12.3.1 (ölçüldü) | Yatayda girdap kanalı **itici** |
| Çekirdek = "kaynak yığını, kare katmanlar, her biri kendi düzleminde" | 1.6 Örgü maddesi | Teoride **katman-istifi emsali zaten var** |
| "Cepler iç içe geçemez" | 12.3 (ışıma gerekçesi) | Dikeyde sert çekirdek → istif **kimlik korur** (R1'in dikey yüzü) |
| Thomson tavanı: tek katman $N\le7$ (+merkez ≈8) | 12.3.7 (62/62) | Büyüme yatayda TIKALI → kütle ancak **katmanla** artar |
| Zerre: basık/disk, $\varepsilon=0$, $D_{XW}=0$, devinimsiz, $v_{cev}=\sqrt2 c_0$ | 1.6 Zerre/Salınımlı Dönme; M-3 | Hedef yapının **kabul ölçütleri** |
| Duvar hızı $\sqrt2\,c_0$, $c_0=\sqrt{P/\rho}$ **yerel** | M-3; Postülat 4 | Az yoğun ortam → $c_0\uparrow$ → dönüş hızlanır (yazarın öncülü) |

---

## 2. ANA BULGU — dikey bağ kanalı teoride zaten kurulu, üstelik yataydan güçlü

### 2.1 Girdap kanalının yön anizotropisi (türetildi)

Aynı iki eş-yönlü dönücüyü iki biçimde yerleştir, teorinin kendi süperpozisyonunu uygula:

**Yan yana (yatay):** orta noktada teğet hızlar **zıt** yönlüdür, birbirini götürür:
$$\lvert v\rvert_{orta}=0 \;\Rightarrow\; u=0 \;\Rightarrow\; \rho=\rho_0 \quad\text{(SIRT — yüksek basınç, İTER)}$$
Bu ölçülmüştü (12.3.1): yatay bağı girdap kanalı **veremez**; bağ Bjerknes + ışıma
dengesinden gelir, aralık $d_{denge}=(\lambda K^5/\kappa)^{1/3}$.

**Üst üste (dikey, ortak eksen):** orta düzlemde, eksenden $r$ uzaklıkta iki katmanın
teğet hızları **aynı** yönlüdür, toplanır:
$$\lvert v\rvert_{orta}=2f\,v_{tek}(r),\quad f\le1 \;\Rightarrow\; u_{orta}=4f^2 u_{tek}
\;\Rightarrow\; \rho_{orta}=\rho_0 e^{-4f^2u_{tek}} \quad\text{(BOŞLUK — alçak basınç, BASTIRIR)}$$

Sınır tabakası yarıçapında $u_{tek}=1$; katmanlar değişmeye yakınken ($f\to1$):
$$\boxed{\;\rho_{orta}\approx\rho_0e^{-4}\approx0{,}018\,\rho_0\;}$$

**Tek cümlelik sonuç:** *Aynı iki yapı yan yana durunca aralarına ρ₀'lık SIRT örüyor,
üst üste durunca ρ₀e⁻⁴'lük BOŞLUK açıyor. Dış Evrenakı basıncı yatayda ayırır, dikeyde
bastırır — bu, kütle-itimin mikro kopyasıdır ve disk bu anizotropinin kendisidir.*

### 2.2 Klasik çapalar (yeni fizik değil)

- **Helmholtz (1858) / halka sıçraması (leapfrogging):** eş-yönlü koaksiyel girdap
  halkaları birbirini çeker ve içinden geçer; sönümlü ortamda bu, bağlı koaksiyel
  çifte oturur. Dikey çekim, girdap mekaniğinin ders kitabı sonucudur.
- **Biot–Savart analojisi:** girdap ipliği ↔ akım halkası. Aynı yönlü akım taşıyan
  iki koaksiyel halka **çekişir**; eksenden sapınca **hizalayıcı tork** doğar —
  istif kendiliğinden koaksiyelleşir.
- **von Kármán döner-akışı / Ekman emmesi:** dönen disk ekseni boyunca akışkan pompalar;
  iki eş-dönüşlü disk arasındaki boşluk emilir (çay yaprağı etkisinin kuzeni).

### 2.3 Dikeyde Bjerknes de çalışır

Bjerknes kuvveti hacim salınımından doğar; **yön seçmez**. ω₂ ortak olduğundan dikey
komşunun fazı da kilitlidir → $\kappa\cos\Delta\varphi/s^2$ ekseni boyunca da çekicidir.
Yani dikey bağın İKİ çekici kanalı var (Bjerknes + girdap boşluğu), yatayın ise BİR
(Bjerknes; girdap kanalı orada iter). **Dikey bağ yataydan sıkıdır** — istif, düzlem
içi aralıktan daha dar dikey aralığa oturur → yapı doğal olarak **basıktır**.

### 2.4 Dikey sert çekirdek — R1'in dikey yüzü

İç içe geçmeyi ne engeller? "Cepler iç içe geçemez" (12.3'ün ışıma gerekçesindeki ilke)
+ pulsasyon yapan sınır tabakalarının örtüşme sınırı. Kimlikler korunur: istif, tek
büyük Kut'a **çökmez** (R1'in dikey ifadesi). **AÇIK KALEM:** dikey denge aralığını
($s_{denge}$) veren itme yasasının türetimi — adaylar: yakın-alan Bjerknes düzeltmesi
(sonlu boyut), ışımanın eksenel lobu, cep elastikliği. Bu dosyanın bir sonraki iş kalemi.

---

## 3. Diskleşme — yazarın küre→disk anlatısının mekanizması

İstif z ekseni etrafında dönerken boşluk emmesi $\Delta P\propto\rho\,(\Omega r)^2$ ile
büyür → eksenel sıkışma $\Omega^2$ ile artar. Az yoğun Evrenakı'da $c_0=\sqrt{P/\rho}$
yükselir → duvar hızı $\sqrt2\,c_0$ yükselir → $\Omega=\sqrt2 c_0/r$ artar → istif daha
sert bastırılır; yatay aralık ise $d_{denge}$ kuyusuna kilitli (az genişler). Net sonuç
**basıklaşma** — Maclaurin sferoidinin teori-içi karşılığı. Yazarın öncülüyle birebir:
*az yoğun ortam → hızlanan dönüş → disk.*

---

## 4. İki istif geometrisi — dikey "hangi eksen"?

| Ölçüt (Zerre'nin bilinen özelliği) | **(A) z-istifi** (3B ekseni) | **(B) w-istifi** (4B ekseni) |
|---|---|---|
| Disk biçimi (basık) | ✔ doğal (2.1–2.3 anizotropisi) | ✔ 3B kesitte tek katman görünür — "çok basık" |
| Boyutsal salınım (birinci imza, 1.4.7/1.4.11) | dolaylı (ω₂ zaten var) | ✔✔ **doğrudan**: ω₂ dönüşü istifi ε-kesitten ileri-geri geçirir — nefes alma GÖRÜNTÜSÜ istifin kendisidir |
| $\varepsilon=0$, $D_{XW}=0$ (devinimsiz) | ✔ hizalı+dengeli katmanlarla | w-dağılımı simetrikse ✔ |
| Bağ yasası biliniyor mu? | ✔ 3B hidrodinamik (bölüm 2) | ✘ w-yönlü kuvvet erimi türetilmedi (4B akustiği: 1/d³?) — AÇIK |
| Kütlenin 3B'de "içeride" olması | ✔ | kısmen — üyelerin çoğu kesit dışında |

**Karma aday (tartışmaya öneri):** istif ekseni tam z değil, **w'ye yatık** olsun
(4B'de eğik istif). Tek istif, iki izdüşüm verir: z-bileşeni **diski**, w-bileşeni
**nefesi** (boyutsal salınım). Zerre'nin iki imzası tek geometriden çıkar.

---

## 5. Balans ön-şartı — makinenin işi neden katmanlaşmanın kapısıdır

Zerre'nin devinimsizliği **kusursuz eksenel simetri** ister ($D_{XW}=0$; Salınımlı
Dönme maddesi). İstifte bu, ancak **her katman dengeliyse** (Q2≈0) ve katmanlar
hizalıysa mümkündür: tek dengesiz katman $D_{XW}\neq0$ taşır → devinim → Zerre değil.
**Sonuç:** simülasyondaki makinenin balans eleği (dışlama, kaynaşma, kapı/emiş) üst
katmana geçişin **kalite kapısıdır** — yalnız dengeli Kutamlar istiflenebilir.
Thomson tavanıyla birlikte resim tamamlanır: yatay büyüme 8'de durur, kütle **katman
katman** eklenir → üst yapının kütlesi katman sayısıyla kuantalıdır. *(Katman sayısı ↔
m_z ilişkisi HESABA GİRMEZ — kapsam bekçisine takılır; burada yalnız geometri konuşulur.)*

---

## 6. Açık kalemler

1. **s_denge türetimi** — dikey itme kanalı (2.4'teki adaylar arasından) ve dikey/yatay
   aralık oranı. En öncelikli kalem: anizotropi iddiasının niceliği buna bağlı.
2. **w-yönlü kuvvet yasaları** — 4B akustik monopolün erimi; (B)/karma senaryonun önü.
3. **Hizalama torkunun zaman ölçeği** — istif kendiliğinden koaksiyelleşir mi, makine
   benzeri bir eleğe mi muhtaç?
4. **İstifin toplam sınır tabakası** — $r_e^{istif}$ katman sayısıyla nasıl ölçeklenir?
   (yatayda $\lvert\Sigma g\rvert r_e$ türetilmişti; dikeyde?)
5. **Sınama yolu** — (i) önce 1B eksenel istif modeli (iki-üç katman, analitik +
   mini koşum; simülasyona DOKUNMADAN ayrı sayfa), (ii) sonuç olumluysa ve yazar
   isterse sim'e "istif kipi". *(Toplu üretim kuralı: yazar onayı olmadan kod yok.)*

## 7. Yazara tartışma soruları

1. Dikey eksen: **z mi, w mi, karma mı?** (Tablo §4 — karma aday iki imzayı birden veriyor.)
2. Diskin basıklık oranı (kalınlık/çap) gözlemsel bir çapaya bağlanabilir mi, yoksa
   şimdilik serbest mi kalsın?
3. §2.1'in $\rho_0$ SIRT ↔ $\rho_0e^{-4}$ BOŞLUK karşıtlığı, 12.3'e (yayına) mekanizma
   anlatısı olarak taşınmaya aday mı — yoksa önce s_denge türetimi mi beklesin?
4. 1B istif mini-modeline başlayayım mı? (ayrı çalışma sayfası, sim'e dokunmadan)

---

---

## 8. SORU 1 (yazar) — Elimizde 6-7'li Kutamlar var; bir Zerre için kaç Kutam gerekir?

**Önce dürüst sınır:** kütle yolu İLKECE kapalıdır — Kut'a kütle/sembol tahsis edilmemiştir
(Anayasa 21), $m_z$ ölçülen girdidir; "Kutam kütlesi × sayı = $m_z$" hesabı yapılamaz ve
yapılmamalıdır. Sayıya giden iki yol GEOMETRİ ve ÖZ-BENZERLİKtir; ikisi de keşif düzeyinde.

**Yol A — öz-benzerlik (12.5: "aynı yasalar her katta").** Kutlar hangi yasalarla
Kutam'a oturuyorsa (uzakta çekim, yakında itme, Thomson bandı), Kutamlar da üst yapıya
aynı biçimli yasalarla oturmalıdır — 12.5'in ölçek değişmezliği tam bunu söyler
($d\propto N$, aynı $d_{denge}/(r_e^A+r_e^B)$ oranı her boyda). O hâlde **dikey istif
sayısının da kendi Thomson-benzeri bandı olmalıdır: K ∈ 5–8, tipik 6–7.**

**Yol B — küre geometrisi (yazarın şartı: birleşik form 3B'de küre).**
6-7'li Kutam'ın geometrik yarıçapı: halka $d_{denge}$'de → $R_{geo}\approx d_{denge}+r_e
= 2{,}41\,r_e$ → **çap $\approx 4{,}83\,r_e$**. K katmanlı istifin kalınlığı
$(K{-}1)\,s_{denge}+2r_e$. Küre koşulu (kalınlık = çap):
$$ (K-1)\,s_{denge} \approx 2{,}83\,r_e \quad\Longrightarrow\quad K = 1 + \frac{2{,}83\,r_e}{s_{denge}} $$
| $s_{denge}$ | $0{,}4\,r_e$ | $0{,}5\,r_e$ | $0{,}7\,r_e$ | $1{,}0\,r_e$ | $1{,}4\,r_e$ |
|---|---|---|---|---|---|
| K | 8,1 | 6,7 | 5,0 | 3,8 | 3,0 |

**Kesişim:** İki yol, $s_{denge}\approx0{,}4$–$0{,}7\,r_e$ (yatay aralığın ⅓–½'si)
olduğunda **aynı sayıda buluşur: K ≈ 6–7 Kutam.** Bu, §2'nin "dikey bağ yataydan
sıkıdır" bulgusuyla kendiliğinden tutarlıdır — iki çekici kanal (Bjerknes + boşluk)
tek çekiciye karşı, aralığı yarıya indirmesi makuldür.

**Çalışma cevabı:** $\boxed{\text{Zerre} \approx 6\text{–}7 \text{ Kutam} \approx 36\text{–}49 \text{ Kut}}$
(6×6=36 … 7×7=49; band uçlarıyla 25–64). Öz-benzerliğin estetiği: **her basamak 6-7'li** —
6-7 Kut → Kutam, 6-7 Kutam → Zerre. Kesinleşme $s_{denge}$ türetimine bağlıdır (açık kalem
6.1); 1B istif modeli bu sayıyı ölçer.

---

## 9. SORU 2 (yazar) — Kendiliğinden birleşme 4B mi, 3B mi? (Şart: birleşik form 3B'de KÜRE)

**Cevap iki katmanlı: tutkal 4B'den, geometri 3B'den — ve küre şartın seçimi kendisi yapıyor.**

1. **Faz kilidi (tutkal) her durumda 4B'nindir.** Bjerknes bağı ω₂ ortak fazından güç
   alır (1.4.12); bu, yatayda da dikeyde de aynı 4B kaynağıdır. "4B mi 3B mi" sorusu
   tutkal için değil, **istif ekseninin hangi uzayda yattığı** için sorulmalıdır.

2. **Yatay (düzlem-içi) kendiliğinden birleşme kanalı ÖLÇÜLMÜŞ biçimde KAPALIDIR.**
   İki Kutam yan yana gelemez: kompozit ışıma duvarı $d\propto N$ kilidi koyar
   (12.3.7'de 62/62 ölçüm; simülasyonda Kutamların örgü kurup ayrı durmasının nedeni
   tam bu). Yani kendiliğinden büyüme **zaten dikeye mecburdur** — doğanın açık
   bıraktığı tek kapı istiftir.

3. **Küre şartı z-eksenini (3B'yi) seçer, w'yi eler:**
   - **z-istifi:** gövde 3B'de yükselir; K≈6-7'de kalınlık=çap → **KÜRE ✔** (§8).
     Az yoğun ortamda $\Omega^2$ sıkışması basıklaştırır → **disk ✔** — yazarın
     küre→disk anlatısı birebir çıkar.
   - **w-istifi:** 3B kesitte gövde HEP tek katman kalınlığında görünür — küre formu
     **asla oluşmaz ✘**; kütlenin çoğu kesit dışında kalır. Elenir.
   - **Küçük w-yatıklığı** (isteğe bağlı süs): ana istif z'de kalmak şartıyla hafif
     w-eğimi, boyutsal salınım görüntüsünü zenginleştirir — küreyi bozmadan. Karar
     sonraya bırakılabilir; ana seçimi değiştirmez.

**Seçim önerisi:** *Kendiliğinden birleşme: 3B'de, z-ekseni boyunca istif; bağın fazı
4B'den (ω₂), çekimi 3B hidrodinamiğinden (eksenel Bjerknes + girdap-boşluk emmesi
$\rho_0e^{-4}$; §2). Küre, K≈6-7 katmanda kendiliğinden; disk, az yoğun ortamda
dönüş hızlanınca.* — Bu seçim §4 tablosundaki (A)'nın, karma seçeneği süs olarak
saklı tutarak benimsenmesidir.

---

## 10. YAZAR KARARI — 16 Ağustos 2026 (kesinleşti; "dosyaya işle" talimatıyla)

1. **İstif ekseni: 3B, z-ekseni.** Kutamlar kendiliğinden z boyunca istiflenir;
   w-istif elendi (3B'de küre veremez). Küçük w-yatıklığı İLERİDE isteğe bağlı
   süs olarak yeniden değerlendirilebilir — ana kararı değiştirmez.
2. **Bağın anatomisi:** faz kilidi (tutkal) 4B'den — ω₂ ortak (1.4.12);
   çekim 3B hidrodinamiğinden — eksenel Bjerknes + girdap-boşluk emmesi
   ($\rho_{orta}\approx\rho_0e^{-4}$, §2.1). Yatay kanal ölçülmüş $d\propto N$
   kilidiyle kapalı → büyüme dikeye mecbur (§9.2).
3. **Zerre'nin kuruluşu:** ≈ **6-7 Kutam** (≈36-49 Kut) z-istifi; dinlenme formu
   **küre** (kalınlık=çap, K≈6-7'de); az yoğun Evrenakı'da dönüş hızlanınca
   $\Omega^2$ sıkışmasıyla **disk**. Öz-benzerlik damgası: her basamak 6-7'li.
   *(Sayı keşif düzeyindedir; kesinleşme $s_{denge}$ ölçümüne bağlı — §11.)*

---

## 11. SIRADAKİ İŞ — 1B Eksenel İstif Modeli (BAŞLANMADI; limit yenilenince ilk iş)

**Amaç:** $s_{denge}$'yi ölçmek; §8 kesişimini ($s\in[0{,}4,0{,}7]\,r_e$ ⟹ K≈6-7)
doğrulamak ya da K'yi revize etmek. **Ana simülasyona DOKUNULMAZ** — ayrı, bağımsız
mini sayfa/koşum (toplu üretim kuralı: yazar onayı alındı, bu iş sırada).

**Dosya adı (açılacak):** `websitesi/CALISMA/Kutam_Birlesmesi/00_CALISMA_Istif_1B_Modeli.md`
(+ gerekirse tek dosyalık mini koşum sayfası aynı klasörde). *(Not: yazar bu çalışma
dosyasını 16 Ağu 2026'da `CALISMA/Kutam_Birlesmesi/` klasörüne taşıdı — iş parçacığının
bütün yeni dosyaları bu klasöre açılır.)*

**Model bileşenleri:**
- (a) **Eksenel Bjerknes:** $F_B(s)=-\kappa_B/s^2$ (çekici; ilk varsayım
  $\kappa_B=\kappa$ — aynı kanal, aynı katsayı).
- (b) **Girdap-boşluk emmesi:** katman = $N\Gamma$ dolanımlı halka; orta-düzlem hız
  alanı Biot–Savart benzeşimiyle (akım halkası $v_\theta(r,z)$ formülü); basınç açığı
  $\Delta P=P_0(1-e^{-u_{orta}})$, $u_{orta}=(v_1{+}v_2)^2/2c_0^2$; kuvvet
  $F_E(s)=\int\Delta P\,dA$ — sayısal integral (halka yaklaşımı yeter).
- (c) **İtme adayları** (hangisi $s_{denge}$'yi koyuyor — modelin ana sorusu):
  (i) yakın-alan Bjerknes düzeltmesi ($s\sim R$ iken monopol kırılır),
  (ii) cep sert çekirdeği ($s_{min}=2R_{cep}$ — gerçek ölçekte ~10⁻⁵ r_e; ekran
  ölçeği ayrık tutulacak, ana simdeki "olay ölçeği" dersi burada da geçerli),
  (iii) ışımanın eksenel lobu — deneme terimi $-\lambda_z K^5/s^5$, $\lambda_z$
  parametrik.

**Ölçülecekler:** $s_{denge}(N,\kappa,\lambda_z)$ · $K_{küre}=1+2{,}83\,r_e/s_{denge}$ ·
iki katmanın bağlı kalıp kalmadığı (leapfrog sönümü) · eğik katmanda hizalama
torkunun işareti (kendiliğinden koaksiyelleşme).

**Kabul ölçütleri:** $s_{denge}\in[0{,}4,0{,}7]\,r_e$ ⟹ §8-§10 damgası doğrulanır
(K≈6-7 kesinleşir). Dışına düşerse §8 tablosuyla K revize edilir ve §10.3 güncellenir.
Mini modelde de öz-sınama alışkanlığı: en az 5 sınama ($s\to\infty$ limitleri, tek
katman nötrlüğü, işaretler, integral yakınsaması, simetri).

---

## 12. KALDIĞIMIZ YER — oturum devri notu (bağlamsız devam için)

**Bu iş parçacığının durumu:** §10 kararı kesin; §11 işi tanımlı ve BAŞLANMADI.
Devam = §11'deki dosyayı açıp modeli kurmak.

**Simülasyon (`CALISMA/Kut_Birlesme_Yapilanma.html`):** 240/240 öz-sınama; Evrenakı
makinası (R1-R7 + kaynaşma + besleme + seçici geçirgenlik + histerezisli renk) çalışır
ve ölçülmüş durumda (60 Kut → 10/10 dengeli, örn. 8✓+9×6✓). Bu turda eklendi ve
**henüz tarayıcıda koşulmadı:** sağ-üst sahne kipi düğmesi (bölünmüş→yalnız 4B→yalnız
3B döngüsü; etiket sıradakini söyler) ve dilde öbek→Kutam çevirisi (135 geçiş,
JS dizgileri tipografik kesme ile korundu; sözdizimi taramaları temiz). **Yedek:**
`Kut_Birlesme_Yapilanma_YEDEK_20260816.html` (sahne düğmesi + Kutam çevirisi ÖNCESİ).

**Kitap:** 1.6'ya **Kutam** maddesi (sözlük kalıbında; Bjerknes 1906 adlı; Kut→Kutam→Zerre;
"Sınır Tabakası ile karıştırılmamalıdır" notu; *(ayrıntılı işleniş: Bölüm 12.3)*).
Kısım 12'de 42 "öbek" geçişi Kutam'a çevrildi (5 dosya); 12.3 girişine adlandırma
cümlesi. KARNE'ye iki kayıt düşüldü (Kutam basamağı + terminoloji hizalaması).

**Devam sırası (öncelikli → sonraki):**
1. §11 — 1B eksenel istif modeli (s_denge ölçümü).
2. Sahne kipi düğmesi + Kutam dilinin tarayıcı doğrulaması (yazar "set bitti" deyince;
   beklenen: 240/240 + üç kipin döngüsü + etiketlerde Kutam).
3. Model sonucuna göre: §2.1 SIRT↔BOŞLUK anlatısı + §10 kararının 12.3'e taşınması
   (aşağıdaki aday kalem; yalnız "sonuçlandı" kararıyla, tek partide).

## İzin bekleyen kalemler (yayına taşıma adayları)

- **[ADAY — henüz taşınmaya hazır DEĞİL, §11 modeli bekliyor]** §2.1 anizotropi
  anlatısı (SIRT ρ₀ ↔ BOŞLUK ρ₀e⁻⁴; "kütle-itimin mikro kopyası") + §10 kararı
  (z-istifi; Zerre ≈ 6-7 Kutam; küre→disk) → hedef: 12.3'e yeni alt bölüm
  ("Kutamların İstiflenmesi") + 1.6 Kutam maddesine tek cümlelik ek.
  Taşıma şartı: $s_{denge}$ ölçümü kabul bandında çıkarsa.

## Süreç kaydı

- 16 Ağu 2026: Dosya açıldı. §2.1 anizotropi türetimi ilk kez burada yazıldı
  (teorinin kendi yasalarından: süperpozisyon + $\rho=\rho_0e^{-u}$). Klasik çapalar
  bağlandı (Helmholtz sıçraması, Biot–Savart, von Kármán/Ekman). İki istif geometrisi
  + karma aday konuldu; balans ön-şartı makineye bağlandı.
- 16 Ağu 2026 (2. tur): Yazarın iki sorusu işlendi. §8: Zerre ≈ 6-7 Kutam (≈36-49 Kut) —
  öz-benzerlik (12.5) ile küre-geometrisi $s_{denge}\approx0{,}4$–$0{,}7\,r_e$'de
  kesişiyor; kütle yolunun ilkece kapalı olduğu açıkça yazıldı. §9: küre şartı istif
  eksenini 3B/z olarak seçti; w-istif elendi (3B'de küre veremez); yatay kanalın
  ölçülmüş $d\propto N$ kilidi "dikeye mecburiyet" gerekçesine bağlandı.
- 16 Ağu 2026 (3. tur): Yazar kararı damgalandı (§10: z-istifi, 6-7 Kutam, küre→disk).
  Kullanım limiti azaldığı için §11 işine BAŞLANMADI — bilinçli erteleme, yarım iş
  bırakmama kuralı. §11'e modelin tam tarifi (bileşenler, ölçülecekler, kabul
  ölçütleri, dosya adı), §12'ye oturum devri notu yazıldı; İzin bekleyen kalemlere
  ilk aday (şartlı) kondu. Devam noktası: §11 dosyasını açmak.
