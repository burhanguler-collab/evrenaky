## DÜŞMANCA DENETİM — β=1 İDDİASI

Bağımsız yeniden hesap yapıldı (ana oturumun betikleri **kullanılmadı**; kendi türetimim + kendi mpmath/scipy kodlarım). Betikler: `C:\Users\ASUS\AppData\Local\Temp\claude\C--Users-ASUS-Desktop-EvrenAKI-KITAP3\af8a4f91-3ca3-4d3f-8118-deaefaba8858\scratchpad\dusman.py`, `hat3b.py`, `hat_ortam.py`, `son.py`

---

### HAT 1 — ETKİN METRİK MEŞRU MU? · **VERDİKT: AYAKTA**

Zinciri açıkça sınadım. M-42'nin tablosu: saat $f\propto\Lambda$, cetvel $\ell\propto\Lambda$, yayılma $c_{loc}=c_0\Lambda^2$.
- $d\tau=\Lambda\,dt$, $dl_{\rm proper}=dx/\Lambda$ ⟹ $c_0^2d\tau^2=\Lambda^2c_0^2dt^2-\Lambda^{-2}dx^2$, yani **tam olarak** $g_{tt}=-\Lambda^2,\ g_{ij}=\Lambda^{-2}\delta_{ij}$.
- Yerel ölçüm: $(dx/\Lambda)/(\Lambda dt)=c_{loc}/\Lambda^2=c_0$ ✓ (Lorentz null).
- Ve tersten: $-mc_0^2\!\int\!\Lambda\sqrt{1-V^2/c_{loc}^2}\,dt \equiv -mc_0^2\!\int\! d\tau$ bu metrikle **birebir aynı ifade**.

Metrik bir GR ithali değil, M-42 tablosunun defter tutmasıdır. **Ama iki load-bearing kalem var:**
1. **İzotropi varsayılıyor.** $\ell\propto\Lambda$ her yönde eşit alınıyor. Radyal/teğetsel farklı ölçeklenirse $\gamma\ne1$ ve sonuç çöker. M-42 bunu açıkça söylemiyor; $\Lambda$ skaler olduğu için savunulabilir ama **yazılmalı**.
2. **$m/\Lambda^3$ eylemsizliği.** Eylemden çıkan momentum $p=mV/(\Lambda^3\Lambda_{kin})$. Bu yeni fizik değil, aynı cetvel/saat ölçeklemesinin ivmeye uygulanması ($a_{yerel}=a_{koord}/\Lambda^3$) — ama kitapta hiçbir yerde yazılı değil ve **43"'nin çoğunu o taşıyor** (bkz. Hat 3).

---

### HAT 2 — EYLEMİN MEŞRULUĞU · **VERDİKT: AYAKTA (beklenmedik derecede güçlü)**

Bu, denetimin en olumlu bulgusu. `11.4.8.1` kendi kutusunda şunu yazıyor:

$$\Lambda=\Lambda_{grav}\cdot\Lambda_{kin},\qquad \Lambda_{grav}=1-\Phi/c^2,\qquad \Lambda_{kin}=\sqrt{1-V^2/c^2}$$

ve kapsam kuralı (2) $M=V/c_{loc}$ diyor, yani $\Lambda_{kin}=\sqrt{1-V^2/c_{loc}^2}$. M-21 ise $\nu_{tik}\propto\Lambda/\gamma$ veriyor. Bunları birleştirin:

$$S=-mc_0^2\!\int\!\Lambda_{toplam}\,dt=-mc_0^2\!\int\!\Lambda_{grav}\sqrt{1-V^2/c_{loc}^2}\;dt$$

**Eylem, SR'den alınmamıştır: teorinin kendi Zerre-Saati tik sayısının Kozmik Zaman üzerinden integralidir.** $\Lambda_{grav}$ M-42'den, $\Lambda_{kin}$ 11.4.8.1'in Prandtl–Glauert türetiminden geliyor; ikisi de mevcut ve [T]. Çarpım kuralı da kitabın kendi kutusunda yazıyor.

**Kapatılmamış tek adım:** *"cisim iç faz birikimini ekstremum yapan yolu izler"* varyasyon ilkesi kitapta YOK. Işık için Fermat var (Fermat kırılması), madde için de Blok I eylem programı var ama parçacık yörüngesi için faz-ekstremum ilkesi yazılmamış. Bu **yeni bir ilke değil ama yazılmamış bir ilke**.

---

### HAT 3 — KUVVET YASASI İLE ÇELİŞKİ · **VERDİKT: ŞÜPHELİ → İDDİA AYAKTA, AMA ANA OTURUMUN DELİLİ ÇÖKTÜ**

Bu hat üç ayrı bulgu verdi; en kritik olan **ikincisi**.

**3a — "Statik tam eşleşme (oran 1,0000000000)" BİR KİMLİKTİR, delil değildir.**
Analitik olarak gösterdim:
- eylem, $V=0$: $a=-c_0^2\Lambda^3\,d\Lambda/dr$ (çünkü $ma/\Lambda^3=-mc_0^2\nabla\Lambda$)
- M-2: $a=-\frac{1}{\rho_n}\frac{dP}{dr}=-\frac{P_0}{\rho_n}\frac{d\Lambda^4}{dr}=-\frac{c_0^2}{4}\cdot4\Lambda^3\frac{d\Lambda}{dr}=-c_0^2\Lambda^3\frac{d\Lambda}{dr}$ ✓

**Her $\Lambda$ için özdeş.** Sayısal denetim (5 farklı $\Lambda$, 2 yarıçap): oran = **1,0** — üstel, lineer, $\sqrt{1-2x}$, $(1+4x)^{-1/4}$, $e^{-x+x^2}$ hepsi. Gerekli tek girdi $P=P_0\Lambda^4$ (= $c_{loc}^2=P/\rho_0$ + $P_0=\rho_0c_0^2$). **SINAV C ayırt edici değildir; üstel yapıyı desteklemez. Ana oturumun 3 numaralı sonucu delil listesinden çıkarılmalı.**

**3b — SAF M-2, MERKÜR'DE İŞARETİ TERS VERİYOR.** (en sert bulgu)
$a=-(GM/r^2)e^{-4\mu/r}$'yi Newton kinematiğiyle (hız terimleri yok) Binet ile çözdüm:

| dinamik | Merkür | oran/GR |
|---|---|---|
| saf M-2 kuvvet yasası, üstel $P$ | **−28,6537 "/yy** | **−2/3** |
| saf M-2, lineer $\Lambda$ | −21,4903 "/yy | −1/2 |
| eylem (tam) | +42,98052 "/yy | +1,0000001 |

Analitik doğrulama: $\Delta\varpi=-4\pi\mu/p=-\tfrac23\times$GR ✓. Saf kuvvet yasası **79 593 σ** dışlanır ve **geri presesyon** verir.

$$\underbrace{-0{,}6667}_{\text{M-2 statik kanal}}+\underbrace{+1{,}6667}_{\text{hız-bağımlı terimler}}=1{,}0000\ \times\text{GR}$$

**43"'nin %167'si M-2'de olmayan terimlerden gelir.** Yani: β=1 üstel basınç profilinin sonucu **değildir**; üstel profil **artı** eylemin hız-bağımlı eylemsizliğinin ($\Lambda^{-3}\Lambda_{kin}$) ortak sonucudur. Merkür kapanışı M-2'ye değil, **eyleme** aittir.

**3c — M-2'nin kapsam kaydı düzeltilmeli.** Eşleşme yalnız **arka plan koordinat** biçiminde geçerli. Yerel-özel biçimde ($a_{yerel}=a/\Lambda^3$, $\nabla_{yerel}=\Lambda\nabla$) oran $\Lambda$ olur, 1 olmaz. M-2'nin $\vec a$ ve $\nabla$'sı arka plan Kartezyen niceliklerdir — bu kitapta yazılı değil.

---

### HAT 4 — KOORDİNAT/GAUGE · **VERDİKT: AYAKTA ama tanımlayıcı seçim load-bearing**

**(i) Presesyon gauge-bağımsız ✓.** Aynı fiziksel yörüngeyi areal yarıçapta ($R=r e^{\mu/r}$) yeniden parametrize ettim:
- izotropik $r$: 42,9805227887 "/yy
- areal $R$: 42,9805227887 "/yy — fark **2,3×10⁻²¹**

**(ii) AMA $\chi$'nin $1/r$'si HANGİ $r$'de? Bu seçim sonucun tamamını taşıyor.**
$\nabla^2\chi=-q_nn_m$ (M-46) hangi koordinatta yazıldığı belirtilmemiş. İki okuma:

| $\chi\propto 1/r$ nerede | $\Lambda$ | $\kappa$ | Merkür | σ |
|---|---|---|---|---|
| **izotropik (düz arka plan)** | $e^{-x}$ | 1 | **42,9805** | **0,69** |
| areal yarıçap | $e^{-x+x^2}$ | 3 | 28,6537 | −15 918 |

Teorinin cevabı var ve tutarlı (Postülat: uzay DÜZ, $r$ bozulmamış ortamın koordinatı ⟹ izotropik), **ama yazılmamış** ve alternatifi 1,5 kat sapma veriyor. Açık aksiyom olarak kayda geçmeli.

---

### HAT 5 — GÖZLEM DEĞERİ · **VERDİKT: AYAKTA, değer doğru; ama PPN-çerçeve-bağımlı**

Park ve ark. 2017 (AJ 153, 121; MESSENGER menzil ölçümü) doğrulandı:
- toplam presesyon **575,3100 ± 0,0015** "/yy
- göreli (gravitoelektrik) katkı **42,9799 ± 0,0009** "/yy — **ölçülen**, öngörü değil ✓
- $J_2=(2{,}25\pm0{,}09)\times10^{-7}$, katkısı **0,0286 ± 0,0011** "/yy (32 σ mertebesinde! ayrı fit ediliyor)
- **$(\beta-1)=(-2{,}7\pm3{,}9)\times10^{-5}$**, $\gamma$ Cassini'ye sabitlenmiş

**Kullanılan gözlem değeri doğru, 0,69 σ da doğru** — ve bağımsız yolla doğrulandı: $\beta=1$'i doğrudan yayınlanmış $\beta$ kısıtıyla karşılaştırınca **0,692 σ** çıkıyor (aynı sayı). Lineer $\beta=1/2$: **12 820 σ**.

**Üç uyarı:** (a) 42,9799 bir PPN indirgemesidir — $\beta$–$J_2$ dejenerasyonu periyodik pertürbasyonlarla kırılmış; (b) $\gamma=1$ (Cassini) **varsayılıyor** — üstel yapı $\gamma=1$ verdiği için kullanım meşru, ama bu bir girdi; (c) sayıyı "bağımsız ölçüm" gibi sunmak yanlış olur — teori PPN-uyumlu olduğu için kullanılabilir.

---

### HAT 6 — İKİNCİ MERTEBE TUTARLILIK · **VERDİKT: ŞÜPHELİ — sınav DEJENERE, ve asıl sınav zaten açık kalem**

**PSR B1913+16:** $\dot\omega_{GR}=4{,}226597$ °/yıl hesapladım ($P_b=0{,}322997449$ g, $e=0{,}6171334$, $M=2{,}828378\,M_\odot$); ölçülen 4,226585 ± 0,000004. Üstel yapı 1PN'de GR ile **özdeş** ⟹ geçer. Lineer 4,93103 °/yıl ⟹ ölür.

**Ama bu bir sınav değil:** $\dot\omega$ kütleleri **ölçmek için** kullanılıyor; $\beta,\gamma$ etkisi kütlelerle tam dejenere. 2PN göreli mertebe $\mu/p=3{,}5\times10^{-6}$, ölçüm hassasiyeti $9{,}5\times10^{-7}$ — 2PN gözlenebilir mertebede AMA kütle serbestliğine emiliyor.

**Asıl 2PN/2.5PN sınavı $\dot P_b$'dir ve teori onu HESAPLAYAMIYOR.** Kitabın kendi kaydı (Blok I, M-44 Açık Uçlar): *naif okuma gözlenen daralmanın $10^9$ katını veriyor, bastırma mekanizması yazılmamış.* Yani: üstel yapı ikili pulsarı **geçmiyor, sınavı erteliyor**.

**Merkür de 2PN'i sınamıyor:** $\mu/p=2{,}66\times10^{-8}$ ≪ hassasiyet $2{,}09\times10^{-5}$. Doğruladım — $\Lambda=1-x+x^2/2+C_3x^3$ ailesinde:

| $C_3$ | −1/6 (üstel) | 0 | 1 | 100 | 10 000 |
|---|---|---|---|---|---|
| σ | 0,692 | 0,692 | 0,691 | 0,565 | −12,0 |

**Merkür yalnızca $\kappa=1$'i (yani $x^2$ katsayısını, yani $\beta$'yı) sınar. "Üstel" biçim Merkür tarafından SEÇİLMEZ.**

---

### HAT 7 (denetim sırasında ortaya çıktı, görevde yoktu) — TERCİHLİ ÇERÇEVE · **VERDİKT: EN CİDDİ AÇIK KALEM**

$\Lambda_{kin}$'in $V$'si **yerel ortama göre**dir (11.4.8.1, açık ifade). Hesap sessizce **ortamın Güneş çerçevesinde durgun** olduğunu varsayıyor. Ortam $w$ ile akıyorsa eylem $-\frac{m}{\Lambda^3}\vec V\!\cdot\!\vec w$ terimi kazanıyor; $\Lambda^{-3}=1+3\Phi/c_0^2$ olduğundan bu **tam devre türevi değildir** ⟹ $\alpha_1$-tipi tercihli-çerçeve kuvveti.

Doğrudan sayısal yörünge integrasyonuyla (DOP853, olay yakalamalı perihel takibi) ölçtüm:

| $|w_\perp|$ | Merkür presesyonu | sapma |
|---|---|---|
| 0 | 42,9809 "/yy | — |
| 100 m/s | 42,6991 | **313 σ** |
| 1 km/s | 40,1623 | 3 132 σ |
| 10 km/s | 14,7263 | 31 394 σ |
| **370 km/s** (CMB dipolü) | **−1104,30** | **1 274 754 σ** |

Etki $w$'de **doğrusal**, $w^2/c^2$ ile bastırılmıyor. 1 σ eşiği:

$$\boxed{|w_\perp|\lesssim 0{,}32\ \mathrm{m/s}\ ;\qquad |\Omega_{ortam}|\lesssim1{,}4\times10^{-18}\ \mathrm{rad/s}\ \ (v_\phi\lesssim 8\times10^{-8}\ \mathrm{m/s})}$$

**İki sonucu var:**
1. Güneş Sistemi ortama göre 370 km/s ile gidiyorsa Merkür kapanışı **yok olur** — teori ortamın Güneş kütle merkeziyle ~0,3 m/s içinde birlikte hareket etmesini **zorunlu kılar**. Bu, 11.4.8.1'in *"Kavrama yolu tükenmiştir… Teori bir postülat eksilir"* hükmüyle **doğrudan gerilim** hâlindedir: zarf/kavrama ışık izotropisi için gereksizleşti ama **Merkür için geri gerekiyor**.
2. M-22/DY-1'in ortam **dolaşımı** ($\Omega_{ortam}$) Merkür yörüngesinde $1{,}4\times10^{-18}$ rad/s'nin (Güneş spininin $5\times10^{-13}$'ü) altında olmalı. 6.3'ün ekvatoral vorteks/yörünge anomalileri sayılarıyla **çapraz denetlenmemiş**.

---

### HAT 8 (denetim sırasında ortaya çıktı) — $\Phi$'NİN İKİ TANIMI ÇELİŞİYOR · **VERDİKT: KİTAPTA MEVCUT KUSUR, artık load-bearing**

Ek D · S-28 (17 Ağu 2026 kararı): $\Phi\equiv(P_0-P)/\rho_n$ **tanım**. Öneri: $\Lambda=\exp(-\Phi/c_0^2)$, $P=P_0\Lambda^4$. İkisi birlikte duramaz:

$$\Phi_P/c_0^2=\tfrac14(1-\Lambda^4)\quad\text{vs}\quad \Phi_\chi/c_0^2=-\ln\Lambda$$

| yer | göreli fark |
|---|---|
| Güneş yüzeyi | $-4{,}2\times10^{-6}$ |
| $r=10\mu$ | **−17,6 %** |
| $r=2\mu$ | **−56,8 %** |

Ayrışma tam olarak **$\beta$'yı belirleyen mertebede**. (Kusur önerinin ürünü değil: mevcut lineer M-42'de de $\Phi_P=c_0^2(x-1{,}5x^2+\dots)\ne c_0^2x$ — kitap zaten aşırı-belirlenmiş.) Çözüm: $\Phi\equiv\alpha\chi$ **birincil** olacak (tam $1/r$, M-46 Poisson'undan), $\Phi=(P_0-P)/\rho_n$ ve M-8'in $\Delta P=\rho_n\Phi$'si **birinci mertebe bağıntısı** statüsüne inecek.

---

### DENETİMİN LEHTE BULGULARI (düşmanca çalışırken çıktı)

1. **Lineer yapı Merkür'den bağımsız olarak da ölü.** $\beta=1/2$ ⟹ Nordtvedt $\eta_N=4\beta-\gamma-3=-2$; LLR $|\eta_N|<4{,}5\times10^{-4}$. Üstel: $\eta_N=0$ **tam**. Yani $\kappa=1$'i sabitleyen ikinci bağımsız gözlem var *(kayıt: teorinin kendi iki-cisim/öz-enerji yapısı yazılmadığı için bu okuma [F])*.
2. **Pozitiflik argümanı gerçek ve teoriye ait.** Lineer $P=P_0(1-4\mu/r)$, $r<4\mu$'de $P<0$ verir — M-7'nin yırtılmama tabanını ihlal eder. Üstel hiçbir $r$'de ihlal etmez. Merkür'den bağımsız bir yapısal gerekçe.
3. **Gölge:** $b_{krit}=2e\mu=5{,}43656\mu$ vs GR $3\sqrt3\mu=5{,}19615\mu$ ⟹ **+4,627 %** ✓ doğrulandı. EHT ile çatışmıyor: Sgr A* **1,04 σ**, M87* **0,65 σ** — ama ayırt de etmiyor.

### DERİVASYON GEREKÇESİNE SALDIRI · **VERDİKT: ŞÜPHELİ**

Önerinin gerekçesi *"stiff ortamda $K=\rho c^2=P$, dolayısıyla $dP/d\chi\propto P$"*. **Bu, M-44'ün yazılma sebebi olan günahı işliyor:** $K=\rho(\partial P/\partial\rho)_\chi$ **birinci** kısmi türevdir; $(\partial P/\partial\chi)_\rho$ **ikincisidir** ve deplasman kanalında $\delta\rho=0$ ($k=0$). Birinciden ikincisinin ölçeklemesini çıkarmak iki kısmi türevi karıştırmaktır.

Alternatif "yerellik" okumasını da sınadım: $\varepsilon=(C/\rho_0)/\omega_n$ sabit ⟹ $C\propto\rho_0\omega_n\propto\Lambda$ ⟹ $\kappa=-2$ ⟹ 15 919 σ **dışlanır**. Yani yerellik ilkesi üsteli tek başına vermiyor; **yalnız $C\propto P$ okuması $\kappa=1$ veriyor ve o okumanın türetimi yok.**

**Dürüst statü: $\kappa$ türetilmiş [T] değil, Merkür'den kalibre edilmiş [F] tek serbest ikinci-mertebe katsayısıdır** — tam olarak PPN $\beta$'nın fit edilmesiyle aynı statü. Kazanç yine gerçek: **bir** katsayı sabitlenip gölge (+4,63 %), ufuksuzluk, $M_{min}$ öngörü olarak çıkıyor.

---

## HÜKÜM (tek cümle)

**β=1 matematiği sağlamdır ve çürütülemedi — Merkür gerçekten kapanıyor (0,69 σ, yayınlanmış $\beta$ kısıtıyla bağımsız doğrulandı) ve lineer yapı 12 820 σ ile ölüyor; ama iddianın sahibi üstel basınç profili DEĞİL, eylemin hız-bağımlı terimleridir (43"'nin %167'si), saf M-2 tek başına işareti ters verir (−28,65"/yy), "üstel" biçim Merkür tarafından seçilmez (yalnız $\kappa=1$ sınanır), ve tüm sonuç ortamın Güneş çerçevesinde 0,32 m/s içinde durgun olması varsayımına asılıdır.**

## KİTABA GİREBİLMESİ İÇİN KAPATILMASI GEREKEN KALEMLER

| # | Kalem | Ağırlık |
|---|---|---|
| **1** | **Ortamın durgunluğu.** $\Lambda_{kin}$'in $V$'si yerel ortama göre; hesap $w=0$ varsayıyor. $|w_\perp|\le0{,}32$ m/s ve $|\Omega_{ortam}|\le1{,}4\times10^{-18}$ rad/s türetilmeli/savunulmalı; 11.4.8.1'in *"kavrama tükendi / bir postülat eksildi"* hükmüyle uzlaştırılmalı; 6.3'ün ekvatoral vorteks sayılarıyla çapraz denetlenmeli. **KRİTİK — kapatılmadan yazılmamalı** |
| **2** | **M-2'nin kapsamı yeniden yazılmalı.** (a) $\vec a=-\nabla P/\rho_n$ **arka plan koordinat** biçimidir, yerel-özel değil; (b) hareketli cisim için tek başına **yetersiz** ve Merkür'de **ters işaret** verir; (c) tam dinamik $p=mV/(\Lambda^3\Lambda_{kin})$ momentumundan gelir. Sayı kayda: −28,6537 "/yy = −2/3 GR | KRİTİK |
| **3** | **"SINAV C tam eşleşme" delil listesinden çıkarılmalı.** Oran 1,0 her $\Lambda$ için özdeştir (5 adayda sayısal doğrulandı); ayırt edici değil, yalnız eylem↔M-2 tutarlılık denetimi | YÜKSEK — mevcut yazım aşırı iddia |
| **4** | **$\kappa$'nın statüsü [F] yazılmalı.** $K=P$ gerekçesi M-44'ün iki-kısmi-türev yasağını çiğniyor; yerellik okuması $\kappa=-2$ veriyor (dışlanır). $\kappa=1$ Merkür'den kalibredir. Envanterde serbest skaler **5→6**'ya çıkar mı, denetlenmeli | YÜKSEK |
| **5** | **$\Phi$'nin tanımı (Ek D · S-28, 17 Ağu 2026) düzeltilmeli.** $\Phi\equiv\alpha\chi$ birincil; $\Phi=(P_0-P)/\rho_n$ ve M-8'in $\Delta P=\rho_n\Phi$'si **birinci mertebe** olarak yeniden etiketlenmeli. Ayrışma $r=2\mu$'de %57 | YÜKSEK |
| **6** | **$\chi$'nin $1/r$'sinin koordinatı aksiyom olarak yazılmalı.** "Düz arka plan = izotropik Kartezyen." Areal okuma $\kappa=3$ ⟹ 28,65 "/yy (−15 918 σ) | ORTA |
| **7** | **Cetvel izotropisi ($\ell\propto\Lambda$ her yönde) M-42'de açıkça beyan edilmeli** — $\gamma=1$ ona asılı | ORTA |
| **8** | **Faz-ekstremum varyasyon ilkesi yazılmalı.** $S=-mc_0^2\!\int\!\Lambda_{toplam}dt$ M-21+11.4.8.1'den çıkıyor; "yol iç fazı ekstremum yapar" adımı kitapta yok | ORTA |
| **9** | **İkili pulsar "geçildi" diye yazılmamalı.** 1PN kütlelerle dejenere; asıl sınav $\dot P_b$ ve M-44'ün $10^9$ kat fazlalık kalemi hâlâ açık | ORTA — dürüstlük |
| **10** | **"Merkür üstel yapıyı doğruluyor" denmemeli.** Sınanan yalnız $\kappa=1$; $C_3$ (x³) 100'e kadar ayırt edilemiyor. Üstelin kendine özgü içeriği yalnız güçlü alanda (gölge +4,63 %, EHT'de 1,04 σ / 0,65 σ — çatışmıyor ama ayırt de etmiyor) | ORTA |
| **11** | Nordtvedt $\eta_N=0$ lehte argümanı [F] etiketiyle girmeli (teorinin iki-cisim/öz-enerji yapısı yazılmadı) | DÜŞÜK |

Sources: [Park et al. 2017, AJ 153, 121 (IOPscience)](https://iopscience.iop.org/article/10.3847/1538-3881/aa5be2) · [ADS kaydı](https://ui.adsabs.harvard.edu/abs/2017AJ....153..121P/abstract)