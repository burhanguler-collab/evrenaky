# 87_ETKIN_YASA — MOND mirasının eritilmesi: kimlik, miras defteri, ayrışma programı

**Karar:** MOND'a ayrı bir "rakip teori" muamelesi yapılmaz; ampirik kazanımı teorinin mevcut yapısı
içinde **eritilir.** Gerekçe: MOND bir mekanizma değil, doğru yakalanmış bir **etkin yasadır** — ve
teorinin F1+F4 toplamı o etkin yasayı zaten üretmektedir. Kepler'in Newton'a oranı neyse, MOND'un
Evrenakı'ya oranı odur.

> **Terminoloji şerhi (bağlayıcı):** MOND, standart fiziğin programıdır — Newton'un "kütleçekim"
> yasasını düşük ivmede değiştirir, **sabit $G$** ve **evrensel $a_0$** varsayar. Bu üç kavramın
> üçü de teoride yoktur: bizde kütleçekim değil **kütle-itim**, sabit $G$ değil **yerel
> $\mathcal{G}=\alpha/\rho_n$** (Postülat 4, M-28), evrensel $a_0$ değil mikro-kökenli, ortam
> kanallı **[S]** rozetli $a_0$ vardır. Aşağıda MOND anlatılırken onların dili tırnak içinde
> standart-fizik aktarımı olarak geçer.

---

## 1. Kimlik tespiti — nihai denklem, MOND ailesinin bir üyesidir

Teorinin resmî galaktik denklemi (6.5.4.4):

$$v^2(R)=R\,a_{F1}(R)+\sqrt{\mathcal{G}\,M_{kaps}(R)\,a_0}
\qquad\Longleftrightarrow\qquad
g = g_{bar}+\sqrt{g_{bar}\,a_0}$$

(yerel yazım $a_{F4}=\sqrt{a_{F1}\,a_0}$ — özdeşlik küresel simetride tamdır, yassı diskte iki okuma ayrışır ve ölçülmüştür: [BESLEME_SINAVI.md](BESLEME_SINAVI.md); ivme diline geçiş $g=v^2/R$ iledir). MOND
yazımıyla bu, $g=\nu(y)\,g_{bar}$, $y=g_{bar}/a_0$ olmak üzere:

$$\boxed{\;\nu_{teori}(y) = 1 + y^{-1/2}\;(y\leq1),\qquad 1+y^{-3/2}\;(y>1)\;}$$

*(parçalı biçim, pencerenin resmîleşmesiyle — M-47; yüksek ivmedeki daha dik sönüm türetilmiştir, seçilmemiştir)*

— Milgrom (1983) programının bilinen geçiş-fonksiyonu ailelerinden biridir. **Ama bir farkla:**
MOND'da $\nu$ elle seçilir (veriye uyan alınır); teoride $\nu$ diye bir nesne yoktur — iki gerçek
kuvvetin (F1 küresel akı + F4 silindirik vortisite akısı) toplamı bu biçimi **zorunlu kılar.**
Derin limitte ($y\ll1$) $v^4=\mathcal{G}M_{bar}a_0$ (baryonik Tully-Fisher, 6.5.4.5'te türetildi),
Newton limitinde ($y\gg1$) $g\to g_{bar}$.

**Sonuç:** MOND'un otuz yılda biriktirdiği ampirik başarı, bu kimlik üzerinden teorinin mirasıdır —
*ölçülmesi koşuluyla.* Ölçüldü (md. 3).

## 2. MOND neden başarılıydı — dört neden, dördünün adresi

| # | Başarı nedeni | MOND'daki statüsü | Teorideki adresi |
|---|---|---|---|
| 1 | Doğru **etkin yasa**: disk dinamiği gerçekten $g_{bar}+\sqrt{g_{bar}a_0}$ gibi davranır | veriden tahmin; $\nu$ açıklamasız | F1+F4 süperpozisyonu (M-35 + M-37/M-38; 6.5.4.4) |
| 2 | Tek küresel ölçek $a_0$, halo başına 2–3 fit yerine | $a_0$ açıklamasız; "$cH_0$" folkloru | $a_0=\mathcal{G}m_n/\ell_\omega^2$ biçimi türetilmiş, değeri [S]; aday kapanış M-45; $cH_0$ okuması yüksek-$z$'de 6/6 dışlandı (`90_YUKSEK_Z`) |
| 3 | Ölçüt **ivme** — LSB öngörüleri önceden tuttu | "neden ivme?" cevapsız | Profil teoremi $v_\theta=\sqrt{R\,a}$ (M-37) + eş-güç (M-45) ivme-ölçekli biçimi zorlar |
| 4 | Derin rejimde ölçek değişmezliği ($v$ sabit) | simetri varsayımı | silindirik akının $1/R$'si (M-38) otomatik verir |

## 3. Miras defteri — MOND'un "teoremleri", teorinin ölçülmüş sonuçları olarak

Hepsi **nihai kurulumla** (yerel $\ell_\omega$ + $a_0=7{,}39\times10^{-11}$ m/s² [S]) ölçülmüştür;
hiçbirinde galaksi başına fit yoktur:

| MOND'un ampirik kazanımı | Teorideki ölçüm | Kaynak |
|---|---|---|
| BTFR eğimi ($\approx4$'e yakın, ΛCDM veremiyor) | **3,734** — gözlenen bandın (3,530–3,738) **içinde**; ΛCDM zinciri 2,716 | [`97_BTFR`](../97_BTFR/CALISMA.md) |
| BTFR normalizasyonu | **0,984** (eski kurulumun ×2,02 açığı nihai kurulumla kapandı) | `97_BTFR` üst kutu |
| BTFR saçılmasının darlığı | sıfır parametreli biçim 0,236 dex; iki parametreli serbest fit ancak 0,217 | `97_BTFR` md. 2 |
| RAR'ın tekliği ("one law") | 2693 nokta, medyan artık **−0,003 dex** (nihai); iç saçılma **0,075 dex** (kurulum-A ölçümü, gözlenenin %26'sı — nihai kurulumda yeniden ölçülmedi) | [`95_RAR`](../95_RAR/CALISMA.md) |
| Renzo kuralı / yerellik (baryon deseni ↔ eğri deseni) | ikinci terim $M_{kaps}(R)$'den beslenir; galaksi-içi yarıçap artığı $-0{,}025\approx0$ | [`94_YEREL_LOMEGA`](../94_YEREL_LOMEGA/CALISMA.md) |
| $\ell$-ölçeğinin kütle yasası (MOND'da örtük) | $\ell_\omega=\sqrt{\mathcal{G}M_{kaps}/a_0}$: 158 galakside eğim 1,03 (beklenen 1,00), $\rho=+0{,}88$ | kitap 6.5.4.5 |

**Devralınmayan tek parça md. 4'tedir.**

## 4. Geçiş biçimi — mirasın devralınamayan parçası ve nedeni

MOND'un veriye fitlenmiş geçiş eğrisi (McGaugh ve ark. 2016: $g=g_{bar}/(1-e^{-\sqrt{g_{bar}/g_\dagger}})$,
$g_\dagger=1{,}20\times10^{-10}$ m/s² **fitli**) artığı düz bırakır; teorinin toplamsal biçimi
nihai kurulumda **+0,051 dex/dex** artık eğimi bırakır (`95_RAR` üst kutu; eski kurulumda +0,084 idi).
İki biçimin analitik farkı ($y=g_{bar}/a_0$; $g_\dagger/a_0=1{,}62$):

| $y$ | $\nu_{teori}=1+y^{-1/2}$ | McGaugh-fit | fark |
|---|---|---|---|
| 0,1 | 4,16 | 4,55 | $-8{,}5\%$ |
| 0,3 | 2,83 | 2,86 | $-1{,}3\%$ |
| 1 | 2,00 | 1,84 | $+8{,}8\%$ |
| 10 | 1,32 | 1,09 | $+20{,}6\%$ |
| 100 | 1,10 | 1,00 | $+10{,}0\%$ |

Desen, 95_RAR'ın kuşak ölçümünün aynısıdır: derin uçta eksik, Newton yakasında fazla. **Bu fark
$a_0$ oynatılarak kapatılamaz** (95_RAR md. 3: iki uç ayrı yöne ister). Doğru iş, MOND'un
$\nu$'sünü kopyalamak değil, **F1 ile F4'ün toplanma biçimini M-37'den türetmektir** — toplamanın kendisi artık türetilmiştir ([TOPLANMA_TURETIMI.md](TOPLANMA_TURETIMI.md) md. 1: lineer süperpozisyon, [T-koşullu]); borç F4'ün **genlik/pencere yasasına** daralmıştır (95_RAR md. 9 iş 1; kitapta 7.4 madde 12(h)). Geçiş yarıçapı $r_0$'ın türetimi (Blok H, H.2 öncelik 1) aynı işin
öbür yüzüdür: MOND'un keyfî $\nu$'süne karşı teorinin cevabı **geometridir** (küresel→silindirik
akı).

**KAPANIŞ (M-47):** o geometri yazılmıştır — Rankine penceresi ([PENCERE_TURETIMI.md](PENCERE_TURETIMI.md))
RAR.mrt eğimini $+0{,}0002\approx0$'a çeker; devralınamayan parça türetimle kapanmış, pencere
resmî denkleme alınmıştır. Kalan tek iç borc galaksi-içi $-0{,}033$'tür.

## 5. Ayrışma programı — MOND'un tökezlediği her yer, teorinin sınav alanı

| # | Kalem | MOND'un durumu | Teorinin durumu ve öngörüsü | Sınav durumu |
|---|---|---|---|---|
| A1 | Görelilik uzantısı | TeVeS, GW170817 ile düştü ("kütleçekim dalgası" hızı) | Dalga kanalı **yerel $c$'de** (M-44); kısıt otomatik sağlanır, kütle-itim eylemden çıkar (M-46) | ✅ yapısal olarak kapalı |
| A2 | $a_0$'ın kozmik kaderi | $a_0\sim cH_0$ folkloru → $a_0(z)$ beklenir | mikro köken → $a_0$ kozmik zamanla **değişmez** | ✅ sınandı: $z=0{,}85$–$2{,}4$'te 6/6 kozmik okuma dışlandı (`90_YUKSEK_Z`) |
| A3 | Ortam/çevre kanalı | $a_0$ evrenseldir; sınıf bandını üretemez | $\mathcal{G}$ yerel + $\lambda$ (kaskad) → sınıf bandı gerçek; $\lambda$–incelik ($v/\sigma$) bağıntısı | ✅ ilk işaret: $+0{,}49$, $p=0{,}019$ ($n=18$; G-8); $n\gtrsim40$ bekliyor |
| A4 | Geçiş fonksiyonu | fitli $\nu$; "basit" $\nu$ Güneş Sistemi kısıtlarıyla gergin | geometrik $r_0$; F4'ün kaynağı disk dolanımı olduğundan Güneş Sistemi'nde **yapısal sıfır** (Ay'da $\varepsilon\sim10^{-15}$, G-5) | ⏳ toplanma biçiminin türetimi açık (md. 4) |
| A5 | Dış alan etkisi (EFE) | sonradan yamanır; güçlü eşdeğerlik ilkesini kırar | dış ortam akısının F4'ü bozması **doğal** (λ kanalının dış-alan yüzü); MOND'dan ayırıcı ikincil imza: kısmi korelasyonda zayıflama | ⛔ **koşuldu — UYGULANAMAZ** ([EFE_PROTOKOL.md](EFE_PROTOKOL.md) md. 6): erratum-düzeltmeli katalog edinildi ($n=141$ eşleşme) ama $e_{\rm env}$ aralığı 0,71 dex, 1-dex kapısını geçemedi; görülen sayılar hükümsüz kayda alındı; meşru yol Paper II çevre verisiyle **yeni** protokol — artık **nicel biçimle** (M-49: eğri düşüşü $g_{kaps}=g_{ext}$'te başlar) yazılabilir |
| A6 | Geniş çift yıldızlar | sürümleri iç dinamikte artış öngörür; literatür çekişmeli (Chae 2023: var · Banik ve ark. 2024: yok) | galaktik F4 çift ölçeğinde düzgün alandır → iç dinamik Newton; öz-F4 kanalı taşıyıcısız | ✅ **hesaplandı** ([GENIS_CIFT.md](GENIS_CIFT.md)): sapma ≲$10^{-4}$ (baskın terim galaktik gelgit); karşı-olgusal öz-F4 %24–158 olurdu — ikili sınav keskin |
| A7 | Kümeler (~2 kat açık) | kalıcı başarısızlık; sterile nötrino yaması | F4 geometrisi disk/girdap yapısına bağlı; küme = sirkülasyon kuyuları programı (kitap 3.7.4, Bullet dahil) — nicel türetim **hesap kalemidir** (7.4) | ⏳ hesap kalemi |

**Okuma:** A1–A3 bugün itibarıyla teorinin *kazandığı* ayrışmalardır; A4 tek iç borçtur. A6'nın
hesabı yapılmıştır (koşullu Newton öngörüsü, ≲$10^{-4}$ — [GENIS_CIFT.md](GENIS_CIFT.md)); A5'in
protokolü koşulmuş ve geçerlilik kapısında düşmüştür (**uygulanamaz** — [EFE_PROTOKOL.md](EFE_PROTOKOL.md) md. 6;
yeni protokol Paper II verisini bekler);
A7 hesap kalemidir.

## 6. Dürüstlük kayıtları

1. **Öncelik hakkı:** BTFR/RAR düzenliliklerini ampirik olarak bulan ve keskinleştiren
   Milgrom–McGaugh–Lelli çizgisidir. Eritme, "bu bağıntıları biz bulduk" demek değildir; "bu
   bağıntıların mekanizması ve türetimi bizdedir, ayrışma noktalarında da onlardan ayrılırız"
   demektir.
2. **$a_0\neq g_\dagger$:** bizim $a_0=7{,}39\times10^{-11}$ [S] ile MOND'un $g_\dagger=1{,}20\times10^{-10}$
   aynı sabit değildir (oran 1,62) — çünkü biçimler farklıdır; sayılar biçimden bağımsız
   karşılaştırılamaz. Birinin değeriyle öbürünün formülünü kullanmak md. 4'teki farkı iki katına
   çıkarır (95_RAR bunu kuşak kuşak ölçtü).
3. **Statü disiplini:** kimlik tespiti bir türetim değildir ve $a_0$'ın rozetini değiştirmez —
   [S] kalır; [T]'ye geçiş M-45'in iki dış koşuluna bağlıdır (bağımsız $\ell_\omega$ + hakem).
4. **Miras defterinin sınırı:** md. 3'ün ölçümleri SPARC'tandır; $a_0$ da aynı örneklemden kalibre
   edilmiştir. BTFR/RAR satırları bu yüzden *tam bağımsız* doğrulama değildir (97_BTFR md. 6.5) —
   bağımsızlık ancak A5–A6 sınavlarından ve SPARC-dışı $\ell_\omega$ ölçümünden gelir.
5. **A6'nın iki ucu açık:** geniş-çift literatürü kendi içinde çelişiyor; teorinin "Newton'a
   yakın" beklentisi de **hesapsız bir beklentidir** — düzgün-alan sadeleşmesinin artığı
   türetilmeden öngörü sayılmaz. G-10 satırı bu nedenle çürütme koşuluyla birlikte yazıldı.
6. Bu rapor yeni ölçüm içermez; md. 3–4'ün bütün sayıları 94/95/97/90 klasörlerinin ve kitabın
   kayıtlı sonuçlarıdır. Tek yeni hesap md. 4'ün analitik $\nu$ tablosudur.

## 7. Bundan çıkan iş

| # | İş | Adres |
|---|---|---|
| 1 | **F1+F4 toplanma biçiminin M-37'den türetimi** (geçiş biçimi; $r_0$ ile aynı iş) | 95_RAR iş 1 · H.2 öncelik 1 · 7.4-12(h) |
| 2 | ~~EFE protokolü~~ → yazıldı, koşuldu: **uygulanamaz** (Kapı 3 — $e_{\rm env}$ aralığı 0,71 dex < 1 dex); süreç ihlali dahil her şey kayıtlı ([EFE_PROTOKOL.md](EFE_PROTOKOL.md) md. 6). Sıradaki: Chae+2021 (Paper II) genişletilmiş çevre kestirimleriyle yeni protokol | bu klasör |
| 3 | ~~Geniş-çift sadeleşme hesabı~~ → **yapıldı** ([GENIS_CIFT.md](GENIS_CIFT.md)): Newton'dan sapma ≲$10^{-4}$, koşullu; kalan: Gaia analizlerinin literatür izlemesi | bu klasör |
| 4 | ~~Besleme sınavı ($M_{kaps}$ ↔ $g_{bar}$)~~ → **yapıldı** ([BESLEME_SINAVI.md](BESLEME_SINAVI.md)): iki okuma diskte ayrışıyor (kitaba şerh düşüldü, 6.5.4.4); $g_{bar}$-besleme eşit kalibrasyonla RMS'te 0,25 km/s önde ama biçim borcu duruyor; RAR.mrt↔rotmod eğimleri ortak konvansiyonda aynı yönde çıktı (işaret notu düzeltildi — BESLEME_SINAVI md. 3.4). Dış not (Gemini) denetimden geçirildi: RMS tablosu doğrulandı, BTFR iddiaları ve "karanlık madde etkisi" çerçevesi reddedildi | bu klasör |
| 8 | ~~Pencere türetimi~~ → **TÜRETİLDİ, [T-aday]** ([PENCERE_TURETIMI.md](PENCERE_TURETIMI.md)): M-30'un Rankine iç kolu + $r_0=\ell_\omega^{etkin}$ özdeşleştirmesi → $W=\min(1,a_0/g_{kaps})$, **sıfır yeni parametre**; küresel sürüklenme $-0{,}043\to-0{,}002$, galaksi-içi $-0{,}074\to-0{,}033$, medRMS $12{,}76\to12{,}48$ (84/141), band dokunulmadı, taban yok, derin limit/BTFR korundu; üs-1 kontrolü daha kötü (üs ayarlanmadı). **RESMİLEŞTİ (M-47; kullanıcı onayı)** — aşağı-akış koşumları tamam: `../../pencere_sinavi.py` → [SONUC_PENCERE.csv](SONUC_PENCERE.csv) (defter 12,48 · RAR.mrt eğimi +0,0002 · yüksek-z 5/6 bant içi · BTFR $W{=}1$ 139/141 · çarpan kararlılığı $r{=}0{,}98$ → λ/σ ayakta); kitap: 10.2.1, 6.5.4.4, M-47, Ek C-20, 10.9, 10.10 | bu klasör |
| 18 | **KAPANIS KARARI (kullanıcı onayıyla):** matematik cephesi kitapta KAPANDI — denklemin her öğesi türetilmiş; bundan sonraki her iş veri işi. Kanıt programı bilinçli olarak DİŞA AÇIK bırakıldı: kalan sınavları bağımsız araştırmacıların koşması = sınamanın kendisi. İşlendi: 6.5.5 (başlık + kapanış paragrafı), 10.10.4 md. 4. G1 gradyan defterde ölçülmüş-alternatif olarak açık kalır (kitap dışı) | kitap |
| 17 | ~~Chae düşen-eğri protokolü~~ → **KOŞULDU — BİRİNCİL UYGULANAMAZ (güç kapısı)** ([CHAE_DUSEN_PROTOKOL.md](CHAE_DUSEN_PROTOKOL.md)): Paper II tab:env (109 galaksi, bağımsız LSS çevre alanı) indirildi; eşleşen n=61; MOND'un kendi öngördüğü etki (0,080) tekil eğim hatasının (0,138) altında → keskin M-49 ↔ yumuşak AQUAL ayrışamaz. İşaretler: çevre korelasyonu sıfırla uyumlu (ρ=−0,11, p=0,39); 61/61 galakside W_dış=1 (teori SPARC'ta çevre imzası ÖNGÖRMEZ — yanlışlanabilir keskin fark kaydı); H2 kestiricisinin vekilliği çürük çıktı (ẽ_fit gözlenen eğimle bile korelasyonsuz). Sonraki yol: çevre-kutulu yığma protokolü / WALLABY | bu klasör |
| 16 | ~~Eliptik dış-σ sınavı (G-12)~~ → **KOŞULDU + GEÇTİ** ([ELIPTIK_SIGMA.md](ELIPTIK_SIGMA.md)): SLUGGS 22 galaksi (Forbes+2017, 3. bağımsız aile), medyan +0,051 dex (kendi Υ konvansiyonumuzla −0,004), saçılma 0,092; 2–10 R_eff arası yarıçapta düz; en kötü tekil M87 (−0,195, küme merkezlisi — A7 açık kalemiyle tutarlı). **M-48 [T-aday]→[T] koşulu sağlandı** — kitap işlemesi kullanıcı onayı bekliyor | bu klasör |
| 15 | ~~Gradyan denklemi denemesi~~ → **KOŞULDU + türetim girişimi DESTEKLENMEDİ** ([GRADYAN_DENEMESI.md](GRADYAN_DENEMESI.md)): G1 tam zincirde gerçek kazanımlar ölçtü (RMS 12,04 · BTFR norm 0,992 · Sb–Sbc 18,92; dSph/MIGHTEE etkilenmez) ama üç ayrıştırma kazancı temel olmaktan çıkardı: $f_{geo}$ imzası yok (ρ=−0,005), kazanç difüz, RMS-optimalde iki besleme eşit (k=1,10'da 11,87↔11,92). Kelvin/düzlemsel-akı türetim adayı yan-sınavda çürüdü. **P resmî kalır**; G1 ölçülmüş-alternatif olarak açık — meşrulaşma yolu: $f_{geo}$'nun λ/koherens fiziğinden yan-öngörülü türetimi | bu klasör |
| 14 | ~~Örneklem-dışı HI (MIGHTEE)~~ → **GEÇTİ** ([MIGHTEE_SINAVI.md](MIGHTEE_SINAVI.md); Ponomareva+2021, MeerKAT derin alan, SPARC örtüşmesi sıfır, n=57): BTFR sıfır-noktası sıfır yeniden-kalibrasyonla — iki yanlı hız tanımının braketi $[-0{,}026,+0{,}083]$ teori bandını $[0,+0{,}053]$ içine alır; $a_0$'ın **ikinci** bağımsız-aile doğrulaması (iki ayrı rejimden). Kalan: yarıçap-çözümlü örneklem-dışı koşum (WALLABY tarzı) | bu klasör |
| 13 | ~~dSph sınavı~~ → **KOŞULDU** ([DSPH_SINAVI.md](DSPH_SINAVI.md); McConnachie 2012, SPARC-dışı ilk aile, 28 sistem): **M-48+$a_0$ örneklem-dışı GEÇTİ** (medyan $+0{,}009$ dex, saçılma 0,172; sıfır yeniden-kalibrasyon) — bağımsızlık arenasının ilk fiilî kapanış adımı; **M-49**: büyük uydularda lehte işaret ($+0{,}109\to+0{,}042$; And II tam isabet), küçük klasikler gelgit-karıştırıcılı (hüküm yok) | bu klasör |
| 12 | ~~EFE terimi~~ → **TÜRETİLDİ (M-49, [T-aday])** ([EFE_TURETIMI.md](EFE_TURETIMI.md)): egemenlik yarıçapı $r_e=\sqrt{\mathcal{G}M/g_{ext}}$ + sonlu-kolon uzak alanı → $W_{dış}=\min(1,\sqrt{g_{kaps}/g_{ext}})$; tam-baskında yarı-Newton $\mathcal{G}_{etkin}=\mathcal{G}(1+\sqrt{a_0/g_{ext}})$ — SEP ihlali türetildi; Fornax 10,5–14,9 (gzl ~11–12); Chae imzası (eğri düşüşü) ve SPARC süptilliği türer; G-13 eklendi; A5'in yeni protokolü artık nicel biçimle yazılabilir | bu klasör |
| 11 | ~~Basınç-destekli köprü~~ → **TÜRETİLDİ (M-48, [T-aday])** ([KOPRU_TURETIMI.md](KOPRU_TURETIMI.md)): küresel izdüşüm lemması ($\sin\theta$ sadeleşir — küresel sistem diskle aynı radyal yasada; 96_ETG açıklandı) + Jeans köprüsü $v_c=\sqrt2\sigma$ + **Faber–Jackson türetimi** $\sigma^4=\mathcal{G}M_{bar}a_0/4$; Fornax mertebe denetimi 17,8≈18 km/s; kovan tam-beslemesi açıklandı; kitap: 6.5.4.9 kapsamı güncellendi, G-12 eklendi; kalan: dış-σ verisiyle nicel sınav + sıcak-bileşen λ + EFE | bu klasör |
| 10 | ~~Kaynak ayrımı (kovan→F4?)~~ → **sınandı, keskin biçim REDDEDİLDİ** ([KAYNAK_AYRIMI.md](KAYNAK_AYRIMI.md)): kovan-baskin sistemlerde çöküş (×1,5 RMS), galaksi-içi eğim bozuluyor; resmî $M_{kaps}$ toplam kalır. Kısmi-katkı versiyonu basınç-destekli köprüye bağlandı ve köprü türetildi (M-48, iş 11): kovanın tam-beslemesi $\sqrt N$ teoreminin sonucu çıktı; kalan ikinci-mertebe sıcak-bileşen λ'ı | bu klasör |
| 9b | **Vitrin kararı (kullanıcı):** paneller **öngörü arenası** ilan edildi — skorboard "SERBEST PARAMETRE: EVRENAKI 0 · ΛCDM (fit) 2" + fitli eğriler/metrik satırları panellerden çıkarıldı (ETG'nin fitli $g_\dagger$ eğrisi arena-dışı/kapalı). **Ayırım ilkesi kayıtlı:** teorinin aleyhindeki gerçek ölçümler (RMS, gereken çarpan, W/2 tuzağı...) defterde ve kitapta aynen durur — panelden çıkan yalnız rakibin fit koltuk değneğidir; panel banner'ı fitli kıyas defterine işaret eder (6.5.3). Kitapta ton ayarı: 6.5 girişi + 6.5.5 + 10.10.4-3 ölçülmüş-zafer diliyle güncellendi | tamam |
| 9 | **Kuyruk:** (a) ~~etkileşimli paneller~~ → **geçirildi**: 3 üreteç güncellendi (eo + fit + JS öngörü fonksiyonlarına $W$; $a_0=7{,}67	imes10^{-11}$), 9 HESAP paneli yeniden üretildi ve 9 Kısım-10 kopyasına dağıtıldı (18/18'de M-47 izi doğrulandı; banner'a pencere cümlesi eklendi); kıtap içi 6.5.2 simülatörü bilinçli dokunulmadı (pedagojik ilk kurulum); ~~kalan görsel~~ → `toplu_defter.py` P sütunuyla pencereye geçirildi ve `k10_toplu_defter.png` yeniden üretildi (A→P 8/1); (b) ~~97 BTFR tam boru hattı~~ → **koşuldu (v3)**: eğim 3,717 (bant içi — 3,750 bayrağı çözüldü), norm 0,978, gereken ×1,11 (yarıçap bandı ×1,00–1,11); kalan: 95'in biçimsel yeniden koşumu; (c) Sdm aykırı eğiminin pencere sonrası yeniden ölçümü | bekliyor |
| 7 | ~~Sınıf-içi sürüklenme sınavı~~ → **koşuldu** ([SINIF_ICI_SURUKLENME.md](SINIF_ICI_SURUKLENME.md)): sınıflar-arası bileşen $\approx0$, galaksi-İÇİ eğim $-0{,}074$ — sürüklenme λ'nın değil, radyal pencerenin imzası; iki borç ayrıştı (λ→band, pencere→sürüklenme); tek türetim hedefi: kanal-arası bastırma/$r_0$ penceresi (H.2 öncelik 1), ölçüsü: galaksi-içi eğimi sıfıra çekmek | bu klasör |
| 6 | ~~Toplanma türetimi~~ → **kısmen kapandı** ([TOPLANMA_TURETIMI.md](TOPLANMA_TURETIMI.md)): basit toplam lineer süperpozisyondan türetildi ([T-koşullu]; koşul: F4'ün eylem terimi — Blok I açık ucu); kayma-ağırlıklı koherens hipotezi iki biçimde sınandı ve **REDDEDİLDİ** (öz-uyumlu: RMS 30,8; baryon-kayma: 15,6); kalan iki mekanik aday: kanal-arası bastırma + derin ucun λ payı (ayrıştırma sınavı: sınıf-içi sürüklenme) | bu klasör |
| 5 | ~~Vortisite kararı~~ → **verildi** ([VORTISITE_KARARI.md](VORTISITE_KARARI.md)): tek-üslü tarama ($f_{geo}^{\alpha/2}$, adil kalibrasyonla) — kısmi vortisite sığ yeğleniyor ($\alpha\approx0{,}5$–$0{,}75$, kazanç 0,35 km/s, [aday]); **öz-tutarlı besleme KESİN DIŞLANDI** ($g\geq a_0$ tabanı, ×22 ihlal) — girdap kendi akışından beslenemez, kaynak baryonların dolanımıdır; resmî denklem B'de kalır; türetim hedefi üçlü: $\alpha$ + biçim eğimi + taban yasağı | bu klasör |
| 4 | Küme ölçeğinde F4/sirkülasyon-kuyusu nicel türetimi | 3.7.4 programı · 7.4 |
| 5 | $\lambda$ $n\gtrsim40$ doğrulaması (A3'ün kesinleşmesi) | `85_TUTARLILIK_YASASI` (bekliyor) |

Bu tespit raporu Claude Fable 5 tarafından üretilmiştir; sayısal dayanakları ilgili çalışma
klasörlerinin kayıtlı sonuçlarıdır.
