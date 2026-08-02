# Chae düşen-eğri kayıt-öncesi protokolü — M-49'un disk imzası (iş 17)

**Statü: PROTOKOL — kestiriciler koşulmadan önce yazıldı.** Bu, `EFE_PROTOKOL.md`'nin
"bundan çıkan iş" maddesindeki **yeni** protokoldür; oradan taşınan iki ders uygulanmıştır:
(i) aralık/kaldıraç eşiği mutlak dex olarak değil, **ölçüm hatasına göreli güç kapısı** olarak
konur; (ii) ayrıştırıcı ikincil imza tasarımı korunur. Eski `veri_chae2021_tablo2.txt`
(Paper I erratum) bu sınavda **kullanılmaz** — o kümeye "en fazla işaret" damgası vurulmuştu.

**Şeffaflık kaydı:** Paper II kaynağının (arXiv 2109.04745) tab:env tablosunun ilk ~18 satırı,
çıkarım kodunun biçim tasarımı için görülmüştür (kaçınılmaz); hiçbir kestirici veya eşik bu
satırlara göre seçilmemiştir — kapılar aşağıda görecelidir ve koşumdan önce kilitlenmiştir.

---

## 1. Hipotezler (önceden ilan; türetim: `EFE_TURETIMI.md`, M-49)

Teorinin denklemi: $v^2=V_{bar}^2+\sqrt{\mathcal{G}M_{kaps}a_0}\,W_{iç}W_{dış}$;
$W_{iç}=\min(1,a_0/g_{kaps})$ [M-47], $W_{dış}=\min(1,\sqrt{g_{kaps}/g_{ext}})$ [M-49].

M-49 **keskindir**: bastırma yalnız $g_{kaps}<g_{ext}$ bölgesinde başlar. MOND-AQUAL'da ise
EFE, $\nu$ fonksiyonunun içinden **yumuşak** girer ve $g_{bar}\gg g_{ext}$'te bile dış eğimi
aşındırır. Buradan iki zıt öngörü:

- **H1 (teori):** SPARC dış bölgelerinde $g_{kaps}\gg g_{ext}$ olduğu sürece çevrenin ölçülebilir
  imzası YOKTUR; gözlenen dış-eğim artığı ($s_{obs}-s_P$; $s_P$ = pencereli resmî denklemin
  öngördüğü eğim) çevre alanı $e_{N,env}$ ile **korelasyonsuzdur** ($\rho\approx0$).
- **H1′ (MOND-AQUAL):** aynı artık $e_{N,env}$ ile **negatif** korelidir (güçlü çevre → daha
  düşük dış eğim).
- **H2 (teori, ikincil — Chae imzasının yeniden-yorumu):** Chae'nin galaksiden galaksiye
  fitlediği $\tilde e_{fit}$ (dış düşüşün şiddeti), teoride **pencereden (W_iç) türeyen** düşüşü
  ölçmektedir; dolayısıyla $\rho_s[\tilde e_{fit},\,-s_P]>0$ (tek yönlü) olmalıdır — yani
  "EFE" diye fitlenen şey, teorinin **çevresiz** öngördüğü eğimle birlikte hareket etmelidir.

## 2. Veri ve eşleştirme

- **$e_{N,env}$ (bağımsız çevre alanı):** Chae ve ark. (2021b, ApJ 921, 104 — Paper II),
  tab:env — SDSS ayak izindeki 109 SPARC galaksisi için büyük-ölçek yapıdan (NSA +
  Karachentsev + MCXC) hesaplanmış $\log e_{N,env}$; "max clustering" ana, "no clustering"
  duyarlılık. Dönüş eğrisinden türetilmemiştir (Kapı 1 bunun metin doğrulamasıdır).
  Birim: $g_{ext}=e_N\times1{,}2\times10^{-10}$ m/s² (yayının kendi $a_0$ normalizasyonu).
- **$\tilde e_{fit}$ (H2 için):** Paper II tab:fit — yayının kendi eğri-fiti; yalnız H2'de,
  "gözlem tarafı" olarak.
- **$s_{obs}$ (dış eğim):** rotmod verisinden doğrudan: dış üçte-birlik noktalarında
  $\log V_{obs}$–$\log R$ ağırlıklı EKK eğimi; hatası EKK'den. **Hiçbir MOND/teori fiti girmez.**
- **$s_P$, $s_{PE}$:** aynı yarıçaplarda pencereli resmî denklemin (P) ve P+M-49'lu denklemin
  öngördüğü eğimler; bütün sabitler donmuş (resmî $a_0=7{,}67\times10^{-11}$, $\Upsilon_*$ 0,50/0,70).
- Eşleştirme SPARC adıyla birebir; el düzeltmesi tek tek gerekçelenir.

## 3. Geçerlilik kapıları (koşulmadan denetlenir)

1. **Bağımsızlık:** $e_{N,env}$ LSS kataloglarından; RC'ye bakmaz (yayın metni §3) — beklenen ✓.
2. **Örneklem:** eşleşen ve dış bölgede $\geq4$ noktalı $n\geq40$; altında "işaret" statüsü.
3. **Güç kapısı (göreli):** MOND-AQUAL'ın öngördüğü eğim-etkisi
   $\Delta s_{MOND}=s_{AQUAL}(e_{N,env})-s_{AQUAL}(0)$ hesaplanır (ν-ailesi, $e_N$'li standart
   biçim). $\mathrm{medyan}|\Delta s_{MOND}| \geq \mathrm{medyan}\,\sigma_{s,obs}$ değilse iki
   hipotez bu veriyle ayrışamaz → **birincil sınav uygulanamaz** (H2 yine koşulur; H2 çevre
   verisi kullanmaz).

## 4. Kestirici ve karar kuralları (önceden kilitli)

- **Birincil:** Spearman $\rho_s[s_{obs}-s_P,\ \log e_{N,env}^{max}]$; iki yönlü permütasyon
  $p$ (10 000, tohum 42). Karar: anlamlı **negatif** ($p<0{,}05$) → **M-49 aleyhine, MOND-tipi
  yumuşak EFE lehine kayıt** (gizlenmez, 7.4'e); anlamsız ($p\geq0{,}05$) **ve** güç kapısı
  geçilmişken → **H1 doğrulandı** (çevre imzası yok — M-49'un keskinliği ayakta); anlamlı
  pozitif → yönsüz anomali, hüküm yok, kayda geçer.
- **İkincil (H2):** $\rho_s[\tilde e_{fit},\,-s_P]$, tek yönlü pozitif, permütasyon $p<0{,}05$
  → "Chae'nin düşen-eğri imzası teoride pencereden türer" doğrulanır.
- **Betimleyici (hüküm dışı):** medyan $(s_{obs}-s_P)$ ve $(s_{obs}-s_{PE})$; $W_{dış}<1$ olan
  galaksi sayısı (teorinin "etki bekleme" listesi).
- Bu dosya yazıldıktan sonra kestirici/kapı değiştirilemez; zorunlu değişiklik sonuca
  bakılmadan gerekçesiyle eklenir.

## 5. Bilinen karıştırıcılar (önceden kayıt)

- Dış eğim, eğiklik ve mesafe hatasına duyarlıdır; bunlar $e_{N,env}$'den bağımsızdır —
  gürültü korelasyonu sıfıra çeker, sahte sinyal üretmez.
- $\tilde e_{fit}$ ile $s_P$ aynı fiziksel eğriden türetildiği için H2'de pozitiflik kısmen
  yapısaldır; bu yüzden H2 tek başına doğrulama değil, H1 ile **birlikte** okunur (H2'nin asıl
  gücü, H1'de çevre korelasyonu yokken düşüşlerin yine de açıklanmış olmasıdır).
- Kümeleme modeli belirsizliği: iki model ("max"/"no") arasında ~0,9 dex fark vardır; birincil
  "max" ile koşulur, "no" duyarlılıkta rapor edilir (ikisi de önceden ilan).

## 6. SONUÇ — **BİRİNCİL SINAV UYGULANAMAZ (Kapı 3 — güç); işaretler ve dersler kayıtlı**

**Veri edinildi:** Paper II kaynak tex'inden (arXiv 2109.04745) tab:env (109 galaksi,
bağımsız $\log e_{N,env}$) ve tab:fit (162 galaksi, $\tilde e_{fit}$) çıkarıldı →
`veri/_chae2021b_env.tsv`, `_chae2021b_fit.tsv`. Hesap: `../../chae_dusen_sinavi.py`;
birleşik veri: [`SONUC_CHAE_DUSEN.csv`](SONUC_CHAE_DUSEN.csv). Eşleşen örnek $n=61$.

**Kapı denetimleri:**

| Kapı | Ölçüm | Hüküm |
|---|---|---|
| 1 — bağımsızlık | $e_{N,env}$ NSA+Karachentsev+MCXC kataloglarından (yayın §3); RC'ye bakmaz | GEÇTİ |
| 2 — örneklem | $n=61\geq40$ | GEÇTİ |
| 3 — güç | medyan $\vert\Delta s_{MOND}\vert=0{,}080$ < medyan $\sigma_{s,obs}=0{,}138$ | **KALDI** |

**Hüküm:** MOND-AQUAL'ın kendi öngördüğü çevre-etkisi bile tekil dış-eğim hatasının altında
kalıyor → iki hipotez (keskin M-49 ↔ yumuşak AQUAL) bu veriyle galaksi-başına ayrışamaz;
**birincil sınav uygulanamaz.** (Eski protokolün 1-dex mutlak eşiği yerine göreli güç kapısı
kondu ve o da aynı hükmü verdi — bu kez gerekçe ölçülmüştür.)

**Süreç kayıtları (gizlenmez):** (i) Betik kapıları ve kestiricileri yine tek koşuda bastı —
EFE_PROTOKOL'dekiyle aynı süreç lekesi. (ii) İlk koşumda güç kapısı kaba $\nu(y{+}e)$ ile
hesaplanmıştı (0,015); protokolün "e_N'li standart biçim" ifadesine uygun düzeltme (Paper II
eq. 2) sonuçlar görülmüş hâldeyken yapıldı (0,080) — kapı hükmü iki biçimde de aynıdır, ama
sıra bozukluğu kayıttır.

**İşaret düzeyinde okumalar (hüküm değil):**
1. Birincil korelasyon her iki kümeleme modelinde sıfırla uyumlu: $\rho_s=-0{,}113$
   ($p=0{,}39$; "no clustering" $-0{,}097$, $p=0{,}46$) — yön H1 (teori: çevre imzası yok)
   ile uyumlu, kanıt değeri düşük.
2. **Teorinin kendi beyanı nettir ve kayda geçer:** eşleşen 61 galaksinin **hiçbirinde**
   $W_{dış}<1$ değil — M-49, SPARC dış bölgelerinde çevresel bastırma **öngörmez**
   (medyan $\tilde e_{env}=0{,}071$ ≪ iç alanlar). Bu, gelecekte daha derin veriyle
   (örn. en dış HI halkaları $g_{kaps}\to g_{ext}$'e yaklaşan sistemler) yanlışlanabilir
   duran keskin bir farktır.
3. **H2 kestiricisi vekilliğini kaybetti:** $\rho_s[\tilde e_{fit},-s_P]=-0{,}109$
   ($p=0{,}79$, desteklenmedi) — ama post-hoc denetim $\tilde e_{fit}$'in bu altkümede
   **gözlenen** dış eğimle bile korelasyonsuz olduğunu gösterdi ($\rho_s[\tilde e_{fit},
   -s_{obs}]=+0{,}009$). $\tilde e_{fit}$ dış eğimin değil, tüm-eğri fitinin (mesafe/eğiklik
   serbestlikleriyle) bir parametresidir; H2'nin "düşüş şiddeti vekili" varsayımı ampirik
   olarak çürüktür → H2'nin desteklenmemesi ne lehte ne aleyhte bilgi taşır. Tasarım dersi
   kayıtlıdır.
4. Ölçek uyumu: $\tilde e_{fit}$ medyanı 0,042, $\tilde e_{env}$ medyanı 0,071 — aynı mertebe
   (Paper II'nin uyum iddiası bu altkümede de görünür). Teorinin bu sayıya yorumu: bu uyum
   nedensellik kanıtı değildir; güç kapısı düşükken fit parametresi önseline/çevre medyanına
   çekilir.
5. medyan $(s_{obs}-s_P)=-0{,}048$: P dış eğimi hafif fazla-öngörür — galaksi-içi $-0{,}033$
   kalemiyle aynı aile (bilinen açık kalem, yeni bilgi değil).

**Bundan çıkan iş:** tekil eğim yerine **çevre-kutulu yığma** (stacking) protokolü — düşük/yüksek
$e_{N,env}$ kutularında yığılmış dış-eğri karşılaştırması güç kazandırabilir; ve/veya
$g_{kaps}$'ı $g_{ext}$'e gerçekten yaklaşan en-dış HI verisi (WALLABY tarzı yarıçap-çözümlü).
İkisi de yeni kayıt-öncesi protokol ister.

Bu protokol ve koşum Claude Fable 5 tarafından yapılmıştır (85/EFE_PROTOKOL şablonu;
kayıt-öncesi kip). md. 1–5 koşumdan sonra değiştirilmemiştir.
