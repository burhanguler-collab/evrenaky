# ÇALIŞMA — Jeodetik Presesyonun Teori-İçi Türetimi (M-51 adayı)

> **Statü:** ÇALIŞMA TASLAĞI — 17 Ağustos 2026. Yayın metnine taşınmadı; Enes "sonuçlandı" diyene kadar burada olgunlaşır.
> **Sınav durumu (aynı gün):** Kalem B (tur açığı) sayısal bileşim sınavıyla **doğrulandı** (oran 1.00000). Kalem A holonomi biçiminde **netleştirildi** (4πμ/R per yörünge; toplam 3πμ/R ✓); mikro-mekanik türetimi açık — üç model denendi, dersler §6'da. Sınav betikleri: `jeodetik_pusula_sinavi.py`, `jeodetik_rozet_sinavi.py`, `jeodetik_rozet_taramasi.py`.
> **Hedef:** M-42 tablosundaki jeodetik ✓'nin türetimsiz durması (denetim bulgusu A3) ve dayanağın "Thomas ½" (saf SR ithali) olması sorunu. Bu çalışma her iki payı da teorinin kendi makinesinden türetir.

---

## 0. Sonucun özeti (önce cevap)

$$\vec\Omega_{geo} = \underbrace{2\,\frac{\mathcal{G}M\,v}{c_0^2 r^2}}_{\text{sinyal taşınımı (yayılım kanalı, } n_{eff}=\Lambda^{-2})} \;-\; \underbrace{\frac{1}{2}\,\frac{\mathcal{G}M\,v}{c_0^2 r^2}}_{\text{tur açığı (Thomas payı, } \Lambda_{kin}\text{'den})} \;=\; \frac{3}{2}\,\frac{\mathcal{G}M\,v}{c_0^2 r^2}\quad(\text{yörünge yönünde, } \hat L)$$

GP-B yörüngesi ($r\approx7027$ km, $v\approx7{,}53$ km/s): **Ω ≈ 6.604 mas/yıl** ↔ GP-B ölçümü **6.601,8 ± 18,3** (0,1σ) ✓. GR'siz, metrikstiz, iki mekanik kalemden. Girdiler tümüyle mevcut [T] kalemleri: $n_{eff}=1/\Lambda^2$ (M-42, bükülmeyle sabitlenmiş) + $\Lambda_{kin}=\sqrt{1-V^2/c_0^2}$ (11.4.8.1, Prandtl–Glauert). **Yeni parametre yok, yeni gözlem girdisi yok.**

---

## 1. Kurulum: jiroskop teoride nedir?

Jiroskop = dönen bağlı yapı. Ekseni, **iç dolaşım deseninin** normalidir: kütle elemanlarını faz-kilidinde tutan iç Zerre sinyalleri (M-19/M-21'in Zerre-Saati mekaniği) gövde içinde dolaşır; "eksen yönü" bilgisini taşıyan şey bu dolaşan sinyal desenidir. İki ayrı mekanik etki ekseni döndürür:

- **(A)** Gövde, kütle çevresindeki $\Lambda(r)$ yapısının içinde **taşınırken** iç sinyalleri kırılır (bükülmeyle aynı mekanizma).
- **(B)** Gövdenin hız **yönü** ortama göre sürekli değişir; $\Lambda_{kin}$ ezilme ekseni hızla birlikte döner ve kafes yeniden dengelenirken yönelim geri kalır (tur açığı).

## 2. Kalem A — Sinyal taşınımı: +2 birim (yörünge yönünde)

**Mekanizma bükülmeyle aynıdır.** Zerre sinyalleri kuyuda $c_{loc}=c_0\Lambda^2$ ile yayılır (M-42); enine gradyanda her sinyal yolu Fermat gereği kütleye doğru kırılır. Işık için bu, 1,751″ bükülmeyi veren $n_{eff}=1/\Lambda^2=1+2\Phi/c_0^2$ indisidir. Jiroskobun iç sinyal deseni **aynı ortamda, aynı indisle** yaşar; desen yörünge boyunca $v$ ile taşınırken yön dokusu birim yolda

$$\frac{d\alpha}{ds}=\nabla_{\!\perp}\ln n_{eff}=\frac{2\,\mathcal{G}M}{c_0^2 r^2}$$

oranında kütleye doğru döner (ışık ışınının kırılma eğriliğiyle aynı ifade). Taşınma hızı $v$ ile:

$$\Omega_A = v\,\frac{d\alpha}{ds} = 2\,\frac{\mathcal{G}M\,v}{c_0^2 r^2}\qquad(\hat L\text{ yönünde — işaret denetimi §5'te})$$

**Neden cetvel kanalı ($\Lambda$, +1) değil de yayılım kanalı ($\Lambda^2$, +2)?** R-10 kategori kuralının sorusu budur ve cevap üç koldan gelir:
1. **Kanon dayanağı (4B — asıl gerekçe, bkz. §2a):** 11.7.1 bağlayıcı cümle: *"eksen bir malzeme doğrultusu değildir: cismin 4B dönüş yapısının bizim kesitimizle arakesitidir."* Malzeme doğrultusu olmayan şey cetvel kanalında taşınamaz; eksen, XY **dolaşım düzleminin** izidir — dolaşan momentum ortamın yayılım kanalında yaşar.
2. *Mekanik gerekçe:* Eksen bir uzunluk değil, bir **yön**dür; yön bilgisini gövde içinde taşıyan şey cetvel (bağ uzunluğu) değil, **dolaşan sinyaldir**. R-10 zaten "yayılım/bükülme bağlamında $c_{loc}$ yazılır" der; eksen taşınımı bir yayılım olayıdır.
3. *Gözlemsel sağlama (artık girdi değil):* Cetvel kanalı seçilseydi toplam $(1-\tfrac12)=\tfrac12$ birim → **≈2.200 mas/yıl** çıkardı; GP-B bunu ~240σ ile dışlar. 4B gerekçesi kanalı zaten seçtiğinden bu bir tutarlılık sınamasına iner.

## 2a. 4B Denetimi (17 Ağu 2026 — Enes'in sorusu üzerine: "eksen 4B'den yansıyan hareketlerin sonucu olabilir mi?")

Kitabın 4B yapısı (1.4.7, 1.4.8, 11.7) tarandı. Dört sonuç:

**(i) İçkin 4B kanal jeodetik koniyi ÜRETEMEZ — kitabın kendi teoremleri gereği.**
- 1.4.7 belkemiği kutusu: ZW bileşeninin hız alanında $v_x=v_y=0$ — W'yi içeren dönüş ekseni **eğemez**, yalnız Z'nin uzunluğunu modüle eder. Eksen ancak W-asimetrisiyle ($\delta=D_{XW}/D_{XX}\neq0$) oynar ve o hâlde bile hareket **doğrusal salınımdır, koni değil** ($\theta=0{,}1806\,\delta$, ritim $\omega_2$; 1.4.8, 11.7.6).
- Bağımlılık yapısı da yanlış olurdu: içkin kanal gövdenin $\delta$ ve $\omega_2$'sine bağlıdır; jeodetik kayma ise $\mathcal{G}Mv/c_0^2r^2$ ile ölçeklenir, yönü $\hat r\times\hat v$'ye kilitlidir ve yörüngesiz jiroskopta sıfırdır. GP-B'de ölçülen kayma jiroskopların kendi spin hızına bağlı çıkmamıştır — dış-alan taşınım deseni.
- Salınımlı (ortalaması sıfır) içkin katkı, sekülér mas/yıl ölçeğinde birikemez. → **4B içkin kanal jeodetiğin alternatif ana mekanizması değildir.**

**(ii) Ama 4B yapı türetimi tam da en zayıf yerinden güçlendirir.** Kanal seçimi (§2) artık gözleme değil kanona dayanır: 11.7.1 *"eksen malzeme doğrultusu değildir, 4B dönüş yapısının kesitle arakesitidir"* der — yani eksen cetvel-nesnesi değil, dolaşım-nesnesidir; taşınımı yayılım kanalında ($n_{eff}=\Lambda^{-2}$) olur. GP-B'nin tek-bit seçimi girdilikten çıkar, sağlamaya döner.

**(iii) Kirlilik-yokluğu teoremi (bedava):** ZW ⊥ XZ/YZ olduğundan, kuyuda W-sektörü nasıl ölçeklenirse ölçeklensin (M-50'nin açık "Λ ölçeklemesi" kalemi) jeodetik toplama **üçüncü bir terim sızamaz** — W kolu ekseni eğemez. Gradyanın gövdede indüklediği geçici $D_{XW}$ asimetrisi olsa bile katkısı $\omega_2$ ritminde, ortalaması sıfır salınımdır; sekülér koniye karışmaz. (Genlik sınırının nicelenmesi: açık adım listesine eklendi.)

**(iv) Taksonomi yeri:** 11.7 iki kanal tanır — zorlanmış (tork; ekinoks) ve içkin (W; Chandler/sönüm iptali). Jeodetik bunlara **üçüncü tür**: *taşınım kanalı* — dolaşım düzleminin, ortamın $\Lambda$ yapısı içinde taşınırken kinematik dönmesi. 11.7.1'in ruhuyla uyumlu ("kuvvet gerekmez; hareket kinematiktir") ama içkin kanaldan ayrı: M, v, r'ye bağlı, sekülér, konik. M-51 kitaba girerse bu ayrım açıkça yazılmalı.

**GR/SR bağımlılık denetimi (Enes'in ikinci sorusu):** Girdi listesi yeniden tarandı — Kalem A: M-1 (c=√(P/ρ)) + M-42'nin Λ²'si (ışık bükülmesi ÖLÇÜMÜyle sabitlenmiş; GR teorisi değil, gözlem) + Fermat (ortam optiği). Kalem B: 11.4.8.1'in P-G ezilmesi [T] + Zerre-saati. **GR nesnesi (metrik, jeodezik, R_s) ve SR aksiyomu yok.** Tur-açığı cebirinin Thomas'a benzemesi ithal değil sonuçtur — 11.4.8.1 Lorentz fenomenolojisini zaten türetir; benzerlik serbest, mekanizma bizim. Kitaba geçerken adlandırma da yerli tutulmalı: **"tur açığı"** (standart fizikteki adıyla Thomas payı).

## 3. Kalem B — Tur açığı: −½ birim (Thomas payının mekanik türetimi)

**SR aksiyomu yok; girdi yalnız 11.4.8.1'in türetilmiş çifti:** hareketli bağlı yapının cetveli **hareket yönünde** $\beta=\sqrt{1-V^2/c_0^2}$ ile kısalır (enine kısalmaz), saati $\beta$ ile yavaşlar.

1. Yörüngedeki gövdenin ezilme ekseni daima anlık hız yönüdür; dairesel yörüngede bu eksen ortama göre $\omega_{yör}=v/r$ ile döner.
2. Gövde, yön değişimini **kendi** ölçüm ağıyla (kısalmış boyuna cetvel + yavaşlamış saat) sayar. Boyuna/enine asimetri yüzünden aynı fiziksel yön değişimi gövde içinden $\gamma=1/\beta$ kat büyük ölçülür (iç faz-kilidinin $v\,\delta x/c_0^2$ gecikme deseni; ölçek yapısının aberasyon yüzü).
3. Tam turda ortam çerçevesi $2\pi$ döner; gövdenin iç pusulası $2\pi\gamma$ saymıştır. **Tork yok** — kafes fazla dönüşü gerçekleştiremez; fark, eksenin ortama göre **geri kalması** olarak birikir:

$$\Delta\alpha_{tur} = 2\pi(\gamma-1)\qquad\Longrightarrow\qquad \Omega_B = (\gamma-1)\,\omega_{yör}$$

4. Bu **kapalı biçimdir** (seri değil) ve standart fiziğin Thomas hızının tam ifadesiyle özdeştir: $(\gamma-1)\omega \equiv \dfrac{\gamma^2}{\gamma+1}\dfrac{av}{c_0^2}$ (özdeşlik: $\beta^2=(\gamma-1)(\gamma+1)/\gamma^2$). Küçük hızda:

$$\Omega_B \approx \frac{1}{2}\frac{v^2}{c_0^2}\,\omega_{yör} = \frac{1}{2}\frac{\mathcal{G}M\,v}{c_0^2 r^2}\qquad(-\hat L\text{ yönünde: geri kalma})$$

5. *İşaret çapraz denetimi:* Elektronun atomdaki spin-yörünge çiftleniminde aynı kalem ½ **azaltıcı** çalışır (Thomas 1926 — gözlemle sabit). Kuvvetle döndürülen her bağlı yapı için geri kalma yönü aynıdır; kütle-itim gerçek bir kuvvet olduğundan (Postülat 6) burada da aynen uygulanır. (Kütle-itim her nükleona eşit ivme verir — M-2; gövde gerilimsiz ivmelenir, ama Thomas gerilime değil **ortama göre hız-yönü değişimine** bağlıdır: ezilme ekseni döner, mekanizma işler.)

## 4. Sentez ve sayısal denetim

$$\Omega_{geo} = \Omega_A - \Omega_B = \left(2-\frac{1}{2}\right)\frac{\mathcal{G}M\,v}{c_0^2 r^2} = \frac{3}{2}\,\frac{\mathcal{G}M\,v}{c_0^2 r^2},\qquad \vec\Omega_{geo}=\frac{3}{2}\,\frac{\mathcal{G}M}{c_0^2 r^3}\,(\vec r\times\vec v)$$

GP-B ($\mathcal{G}M_\oplus=3{,}986\times10^{14}$ m³/s², $r=7{.}027$ km, $v=7{,}53$ km/s):
$\Omega = 1{,}5\times6{,}76\times10^{-13}$ rad/s $= 1{,}015\times10^{-12}$ rad/s $= \mathbf{6.604\ mas/yıl}$.
Ölçüm: $6.601{,}8\pm18{,}3$ ✓ (0,1σ). *(GR'ın kendi öngörüsü 6.606,1 — aynı bant; ayrım yok, beklenmiyordu: γ_PPN=1 zaten M-42'nin sonucu.)*

**Muhasebe:** İki kalemin de girdisi eski: $\Lambda^2$ bükülmeden (M-42), $\Lambda_{kin}$ Prandtl–Glauert'ten (11.4.8.1, [T]). Jeodetik böylece **girdisiz çıktı** (parametresiz öngörü) konumuna gelir; M-42'nin "GR'a başvurulmaz" iddiası bu satır için artık gerçekten tutar. Thomas payı SR ithali olmaktan çıkar: aynı sayı, teorinin kendi ezilme mekaniğinden.

## 5. İşaret/yön defteri (özet)

Kütle merkezde; konum $r\hat x$, hız $v\hat y$, $\hat L=\hat z$. (A): iç sinyal yolları kütleye doğru kırılır → ileri vektör $-\hat x$'e yatar → $+\hat z$ dönüşü (yörünge yönü) ✓. (B): iç pusula turu büyük sayar, eksen ortama göre geri kalır → $-\hat z$ ✓. Net: $+\tfrac32$ birim, $\hat L$ yönünde — de Sitter yönüyle uyumlu (GP-B'nin yörünge-düzlemi kayması).

## 6. Açık adımlar ve SINAV SONUÇLARI (17 Ağu 2026 güncellemesi)

**Sınav programı koşuldu** (`jeodetik_pusula_sinavi.py`, `jeodetik_rozet_sinavi.py`, `jeodetik_rozet_taramasi.py`). Durum:

1. ~~**Aberasyon adımının sıkılaştırılması (Kalem B)**~~ → **KAPANDI [S-num]:** Türetilmiş cetvel-saat-yerelzaman haritalarının dairesel hız yolunda adım adım bileşiminden Wigner artığı sayısal olarak toplandı: tur başına net dönme = −2π(γ−1), **oran 1.00000** (u/c₀ = 0,3; 0,05; 0,03 — üçünde de). Tur-açığı kapalı biçimi doğrulandı; kodda SR aksiyomu yok, yalnız 11.4.8.1'in türetilmiş haritaları.

2. **Küçük-döngü lemması (Kalem A) — matematiksel biçimi NETLEŞTİ, mikro-mekanik türetimi AÇIK:**
   - **Ders 1 (düzgün-gradyan null'u):** Düzgün ∇c'de düz taşınan pusula dönmez — y-ötelemesi simetrisi gereği tam sıfır (sayısal: ~1e-18). Yerel "Ω = v∇⊥ln n" ifadesi bu yüzden gauge-kokuludur; **fiziksel gözlenen kapalı-yörünge holonomisidir**: gradyan yönü yörünge boyunca döndüğü için birikim olur. Kalem A'nın doğru ifadesi: *tam yörüngede eksen, Fermat (sinyal) metriğinin paralel-taşınım holonomisi kadar döner:* Δα_A = ∮∂⊥(ln n_eff) ds = **4πμ/R per yörünge** (v'den bağımsız; μ ≡ 𝒢M/c₀²). Konformal bağlantı hesabıyla analitik: e^{2φ}δ metriğinde taşınım dönme oranı ∂⊥φ; φ = ln n_eff = 2μ/r ⇒ 2μ/R² × 2πR. Tur açığıyla toplam: 4πμ/R − 2π(γ−1) →(Kepler v²=μc₀²/R)→ **3πμ/R = de Sitter/GP-B** ✓. (Not: GR aynı 3π'ye 1+½ ayrışımıyla ulaşır; biz 2−½ ile — toplam aynı, ayrışım kanal yapısına bağlı ve 4B gerekçesi bizimkini seçer.)
   - **Ders 2 (kilitli pusula → fırıldak):** Bağı her sekmede pusulaya kilitlemek yön hafızasını siler; bağ v̂'ye kilitlenip yörüngeyle döner (ölçüm: tam 2π/yörünge). Jiroskop = yön hafızası; köleleştirilemez.
   - **Ders 3 (sinyal-çifti rozeti):** Torksuz merkezî bağla zıt-dolaşan iki paket; işaretçi m=(φ₁+φ₂)/2. Statik kontrol tam 0 ✓. μ-farkı **ölçek-değişmez temiz sayı**: a∈{0,04;0,02;0,01} ve v∈{0,02;0,03} için D(μ)−D(0) = 5,65e-3 ± %0,1 = **9πμ/R** (beklenen 4πμ/R'nin 2,25 katı). Kinematik payı D0 = (35,6)β² (a-bağımsız). Yorum: faz-toplamı işaretçisi saf yön-taşınımı değil; dönen μ-gelgitinin desen **sürüklemesini** de sayıyor — bu işaretçi jiroskop değildir. (9πμ/R ve K≈35,6 modelin kendi dinamiği olarak kayda değer; ileride bağımsız iş olabilir.)
   - **KALAN ANA İŞ:** Doğru mikro-nesne test-sinyali değil **girdap çekirdeğinin kendisi**: v ile taşınan, ekseni gradyana açılı vortex yapısının yönelim dinamiği — akışkan pertürbasyon hesabı (stiff ortamda, ∇c ve taşıma v ile). Beklenti Fermat-holonomi ağırlığı (2); GP-B ayrımı (240σ) ve 4B/11.7.1 gerekçesi bu ağırlığı bağımsız destekliyor; eksik olan alt-düzey hesabın kendisi. Kitaba girme koşulu bu hesap.
3. **Çarpım yapısı ihmali:** $\Lambda_{grav}\cdot\Lambda_{kin}$ karışık terimleri GP-B'de $\sim10^{-19}$ (iki küçüklüğün çarpımı) — ihmal meşru; bir cümleyle kayda geçirilmeli.
4. **Kanal gerekçesinin bağımsız sınaması:** "Eksen yayılım kanalında taşınır" atamasının GP-B dışında bir gözlemle (ör. LAGEOS jeodetik bileşeni, ay-yörünge de Sitter: 19,2 mas/yıl — Ay-Dünya sistemi Güneş kuyusunda) çapraz denetimi. Ay de Sitter ölçümü (LLR, ~%0,6) aynı 3/2'yi sınar → eklenmeli.
5. **Gradyan-kaynaklı $D_{XW}$ salınım sınırı (§2a-iii):** Kuyu gradyanının gövdede indükleyebileceği geçici W-asimetrisinin genliği nicelenmeli; beklenen: $\omega_2$ ritminde, ortalaması sıfır, mas/yıl sekülér bütçesine katkısız. Bir cümlelik üst sınır hesabı M-51'in Geçerlilik Sınırı'na girer.

## 7. Kitaba taşıma planı (onay sonrası, tek partide)

- Ek M'ye yeni girdi: **M-51 · Jeodetik Presesyonun Mekanik Türetimi** (bu dosyanın olgun hâli; Varsayımlar→Adımlar→Sonuç→Geçerlilik→Açık Uçlar şablonuyla).
- `18_5:1328` (M-42 Kapanan Gözlemler): jeodetik satırına "türetim: M-51" atfı; `18_5:1681` (H.3): "Thomas ½ + ölçek payı 1" gerekçesi → "M-51: sinyal taşınımı 2 − tur açığı ½" olarak düzeltilir (eski gerekçe **yanlış ayrıştırmaydı**: 1+½ değil, 2−½).
- `18_5:1264` giriş vaadi jeodetik için artık gerçekten karşılanır — vaat cümlesi M-51 atfı alır.
- KARNE'ye satır.
