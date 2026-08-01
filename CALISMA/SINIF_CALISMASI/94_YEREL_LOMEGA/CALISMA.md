# 94_YEREL_LOMEGA — $\ell_\omega$ yerel kütleden kurulmalı · Çalışma dosyası

> ### ⚡ NİHAİ KURULUM (1 Ağustos 2026 · karar: [86_NIHAI](../86_NIHAI/CALISMA.md))
>
> Bu dosyanın analizi **eski (A) kurulumla** yapıldı ve tarihsel kayıt olarak duruyor.
> Nihai kurulum: yerel $\ell_\omega$ + $a_0=1{,}75\times cH_0/16{,}1$. Nihai sayılar: Bu dosyanın B kurulumu **nihai kurulumun kendisi oldu**; $a_0$ çarpanı olarak da buranın sayısal çözümü (×1,77≈×1,75) seçildi. Boru hattı, paneller ve defter yenilendi.


**141 galaksi · fit yok · yeni parametre yok · $a_0$ oynatılmadı**

Hesap: `../../yerel_lomega_sinavi.py` · Çıktılar: [`SONUC.csv`](SONUC.csv) ·
[`YONTEM.md`](YONTEM.md) · [`yerel_lomega.png`](yerel_lomega.png)

**Türetim denetimi: [`TURETIM.md`](TURETIM.md)** — B, M-38'den çıkarılabilir mi? Cevap: hayır,
ama açık **tek bir cümleye** indi — 6.5.4.3 Adım 2'nin *tutarlı toplanma* varsayımı.

---

## 0. Bu bir düzeltme değil, bir tutarsızlığın giderilmesi

Mevcut kurulum F4'ü şöyle yazıyordu:

$$v_{F4}^2 = \frac{\mathcal{G}\,\overbrace{M_{kaps}(R)}^{\textbf{YEREL}}}{\ell_\omega(\underbrace{M_{bar}}_{\textbf{TOPLAM}})}$$

**Aynı terimin payında yarıçap içi, paydasında galaksinin tamamı var.** Teori bunu
gerektirmiyor. $\ell_\omega = q_n/(2\gamma_n)$ — pulsasyon debisinin dolanım debisine oranı.
İkisi de $R$ yüzeyinden geçen **akıdır**; akı teoremi gereği $R$ **içindeki** maddeden doğar.
Toplam kütleyi oraya koymak, teorinin kendi akı tanımının dışına çıkmaktır.

Tutarlı hâli:

$$\boxed{\;\ell_\omega(R)=\sqrt{\frac{\mathcal{G}M_{kaps}(R)}{a_0}} \;\Longrightarrow\;
v_{F4}^2=\sqrt{\mathcal{G}\,M_{kaps}(R)\,a_0}\;}$$

**Yeni parametre yok. $a_0$'a dokunulmadı. Fit yok.** Yalnız aynı büyüklüğün iki yerde aynı
tanımla kullanılması sağlandı.

---

## 1. Bunu veri söyledi — $\ell_\omega$ doğrudan ölçüldü

$a_0$ hiç kullanılmadan, her galakside her yarıçapta:

$$\ell_\omega^{ölç}(R) = \frac{\mathcal{G}M_{kaps}(R)}{v_{gözl}^2 - V_{bar}^2}$$

| Ölçüm | Sonuç | Teorinin varsayımı |
|---|---|---|
| $\ell_\omega \propto M^p$ | $p = \mathbf{0{,}506}$ | 0,500 — **doğrulandı** (fark 0,006) |
| $\ell_\omega^{ölç}/\ell_\omega^{yasa}$ | 0,676 | 1,0 → $a_0$ ×2,19 |
| $d\log\ell_\omega/d\log R$ | $\mathbf{+0{,}56}$ | **0** — yanlış |

İlk satır çok önemli: **teorinin $\ell_\omega=\sqrt{\mathcal{G}M/a_0}$ kütle yasası, veriden
bağımsız olarak 0,006 hassasiyetle doğrulanıyor.** Sorun yasada değil, hangi kütlenin
konulduğunda.

Üçüncü satır çözümü veriyor: dış bölgede $M_{kaps}\propto R^{1{,}5}$ civarındadır ve
$\sqrt{M_{kaps}}\propto R^{0{,}75}$. Ölçülen eğim tam bu mertebede.

---

## 2. Sonuç 1 — dönüş eğrisi hatası **her sınıfta** düşüyor

| Sınıf | n | RMS A | RMS B | kazanç | sapma A | sapma B | $k_A$ | $k_B$ |
|---|---|---|---|---|---|---|---|---|
| Sa–Sab | 12 | 27,67 | 26,72 | −3% | $-10{,}9\%$ | $-9{,}1\%$ | ×2,67 | ×2,03 |
| Sb–Sbc | 29 | 25,35 | 24,55 | −3% | $-6{,}2\%$ | $-5{,}4\%$ | ×1,69 | ×1,58 |
| Sc–Scd | 30 | 21,35 | **17,22** | **−19%** | $-13{,}5\%$ | $-10{,}8\%$ | ×2,33 | ×1,89 |
| Sd | 16 | 20,87 | **14,18** | **−32%** | $-22{,}8\%$ | $-17{,}5\%$ | ×3,76 | ×2,67 |
| Sdm–Sm | 28 | 18,12 | **12,07** | **−33%** | $-16{,}7\%$ | $-11{,}7\%$ | ×2,84 | ×1,95 |
| Im | 26 | 7,67 | **5,85** | **−24%** | $-6{,}2\%$ | $-2{,}1\%$ | ×1,47 | ×1,14 |
| **TÜMÜ** | **141** | **19,51** | **15,90** | **−19%** | $-12{,}4\%$ | $-9{,}1\%$ | ×2,21 | **×1,77** |

**102/141 galakside B daha iyi.** Kazanç geç tiplerde en büyük — beklendiği gibi: gaz zengini
sistemlerde $M_{kaps}(R)$ eğri boyunca çok büyür, yani yerel/toplam ayrımı orada en çok fark
eder.

> **B tek başına, sıfır yeni parametreyle, ×2,21 kalibrasyon yamasının yaptığı işi yapıyor:**
> 15,90 ↔ 15,88. Yani "$a_0$ ×2,2 küçük kalıyor" açığının büyük kısmı $a_0$'ın değil,
> **toplam kütleyi yerel yere koymanın** eseriymiş.

---

## 3. Sonuç 2 — asıl sonuç: $\ell_\omega$ yasasının **yarıçap izi siliniyor**

$\ell_\omega^{ölç}/\ell_\omega^{yasa}$ oranının yarıçapa göre eğimi (F4 payı > 0,40 kesiti,
125 galaksi). Yasa doğruysa bu **sıfır** olmalı:

| Kurulumun varsaydığı $\ell_\omega$ | eğim (medyan) | saçılma |
|---|---|---|
| **A** · $\sqrt{\mathcal{G}M_{bar}/a_0}$ (sabit) | $\mathbf{+0{,}558}$ | 0,176 dex |
| **B** · $\sqrt{\mathcal{G}M_{kaps}(R)/a_0}$ | $\mathbf{-0{,}025}$ | 0,091 dex |

**Sıfırdan ayırt edilemiyor.** Saçılma da yarıya iniyor.

Bu, bu çalışmanın en güçlü tek sonucudur: **teorinin $\ell_\omega$ yasası, doğru kütleyle
kurulduğunda galaksinin içinde yarıçap boyunca hiçbir sistematik iz bırakmıyor.** Sıfır
serbest parametreli bir yapısal öngörü, 125 galakside 0,025 hassasiyetle doğrulanmış oluyor.

---

## 4. Sonuç 3 — açık kalemler daralıyor, ama kapanmıyor

| | A | B |
|---|---|---|
| Sınıf çarpan bandı | ×1,47 – 3,76 (2,57 kat) | **×1,14 – 2,67** (2,34 kat) |
| Sınıf saçılması | 0,138 dex | **0,113 dex** (−%18) |
| Galaksi başına saçılma | 0,445 dex | 0,424 dex (−%5) |
| RAR artık eğimi | $+0{,}1013$ | **$+0{,}0791$** (−%22) |
| RAR medyan artık | $-0{,}109$ dex | **$-0{,}055$ dex** (yarıya) |

97_BTFR md. 2'nin açık kalemi **daralıyor ama duruyor.** Galaksi başına saçılmanın %5
azalması, bunun büyük kısmının başka bir şeyden geldiğini söylüyor.

95_RAR'ın biçim sorunu da **azalıyor ama bitmiyor** ($+0{,}101 \to +0{,}079$). Yani geçiş
biçimi hâlâ tam değil — ama artık sorun $\ell_\omega$'nın kütle bağımlılığında değil, başka
yerde.

---

## 5. Denetim — teorinin en güçlü sonucu bozulmadı

| | BTFR eğimi | $M_{kaps}(R_{dış})/M_{bar}$ |
|---|---|---|
| A · mevcut | 3,660 | 1,000 |
| **B · yerel** | **3,660** | 1,000 |

Dış ölçüm noktasında $M_{kaps}\to M_{bar}$ olduğu için A ile B **orada tam olarak örtüşür.**
BTFR eğimi, 96_ETG'nin dış nokta sonucu ve 95_RAR'ın derin limiti **değişmez.** B yalnız
eğrinin iç/orta kısmına dokunur — zaten sorunun olduğu yere.

**Bir bonus:** 96_ETG'nin $g_{öng}=g_{bar}+\sqrt{g_{bar}a_0}$ türetimi B ile **yaklaşım
olmaktan çıkıp tam eşitlik oluyor** ($\mathcal{G}M = a_{bar}R^2$ adımı artık aynı kütleyi
kullanıyor). O dosyanın 7.2 dürüstlük kaydı kapanıyor.

---

## 6. Dürüstlük kayıtları

1. **Bu bir seçim değil, bir zorunluluk iddiasıdır — ve iddia edilmiştir, türetilmemiştir.**
   "$\ell_\omega$ akı oranıdır, akı $R$ içindeki maddeden doğar" cümlesi makuldür ama
   M-38'in kendi türetiminden **satır satır çıkarılmamıştır.** Bu yapılana kadar B, "veriyle
   uyumlu ve teoriyle tutarlı görünen kurulum"dur; "teoriden çıkan kurulum" demek için
   6.5.4'te $\ell_\omega=q_n/2\gamma_n$ ifadesinin yarıçap bağımlılığı açıkça yazılmalıdır.
2. **Kazanç geç tiplerde büyük, erken tiplerde küçük** (−%3). Erken sarmallarda $M_{kaps}$
   zaten hızla doyduğu için A ile B neredeyse aynı. Yani B, erken tiplerin sorununu
   **çözmüyor** — Sa–Sab hâlâ ×2,03 istiyor ve RMS 26,7'de.
3. **$M_{kaps}\approx 0$ olan en iç noktalar 3. maddedeki ölçümden çıkarıldı.** Orada
   $\ell_\omega^{ölç}\to 0$ olur ve $\log$ eğimini yapay olarak şişirir. Bu bir kez hataya
   yol açtı: kırpma korumasız iken A'nın eğimi $+1{,}26$ çıkıyordu, doğrusu $+0{,}56$.
   Koruma betikte açıkça yazılıdır.
4. **F4 payı > 0,40 kesiti bir seçimdir.** 96_ETG/95_RAR'ın 0,25 eşiğinden farklı, daha sıkı.
   0,25 ile de denendi, sonuç yön olarak aynı. Ama seçilmiş bir sayıdır.
5. **$V_{bar}$ hâlâ SPARC'tan, evrensel Newton $G$'siyle geliyor.** Teori $\mathcal{G}$'nin
   değişken olduğunu söylüyorsa bu bir **dış girdidir** ve bu sınavda da düzeltilmedi.
   Adım 2'nin konusu.
6. **B, açık kalemleri daraltıyor ama hiçbirini kapatmıyor.** Sınıf saçılması, RAR biçim
   sürüklenmesi ve kalan ×1,77 çarpanı **duruyor.** B bir çözüm değil, bir temizliktir.

---

## 7. Ne çıktı — üç cümle

1. **Teorinin $\ell_\omega=\sqrt{\mathcal{G}M/a_0}$ yasası doğrudur** — kütle üssü veriden
   bağımsız olarak 0,506 ölçüldü (yasa 0,500) ve doğru kütleyle kurulduğunda yarıçap izi
   $-0{,}025$'e, yani sıfıra iniyor.
2. **Yanlış olan yasa değil, hangi kütlenin konulduğuydu.** Yerel $M_{kaps}(R)$'ye geçmek
   dönüş eğrisi hatasını %19 düşürüyor, hiçbir parametre fitlemeden, BTFR eğimine
   dokunmadan.
3. **Kalan $a_0$ açığı ×2,21'den ×1,77'ye indi.** Geri kalanı ve sınıf saçılması hâlâ açık —
   sıradaki hedef $\mathcal{G}$'nin ve dolayısıyla $a_0$'ın yerelliği.

## 8. Bundan çıkan iş

| # | İş | Neden |
|---|---|---|
| **1** | **B'yi bütün sınavlara uygula** (01–07, 95, 96, 97) ve sayıları yenile | tek tutarlı kurulum olmalı; şu an dosyalar A ile yazılı |
| ~~2~~ | ~~M-38'den türet~~ → [`TURETIM.md`](TURETIM.md) | ✅ **yapıldı.** Türetilemedi; açık *Adım 2'nin tutarlı toplanma varsayımına* indirgendi. Sıradaki hedef: **tutarlılık kütlesi $M_{tut}$** |
| ~~3~~ | ~~$\mathcal{G}_{yerel}$'i ölç~~ → [`93_G_YEREL`](../93_G_YEREL/CALISMA.md) | ✅ **yapıldı.** Eğim $-0{,}093$, işaret doğru; ama $\mathcal{G}\leftrightarrow\Upsilon_*$ dejenerasyonu **yapısal olarak kırılamıyor** |
| 4 | Kalan ×1,77'yi $c_{yerel}=\sqrt{P_n/\rho_n}$ üzerinden $a_0$'a bağla | md. 3'ten sonra $a_0$ [S] → [T] olabilir |
| 5 | Erken sarmalların ayrı sorununu incele | md. 6.2 — B onlara yaramıyor |

**Madde 2 en kritik.** B'nin sayısal başarısı onu doğru yapmaz; teoriden çıktığı gösterilene
kadar bu dosya bir **ölçüm**, bir türetim değildir.
