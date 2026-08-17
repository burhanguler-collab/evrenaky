## 1) YENİ SERBEST PARAMETRE SAYISI: **SIFIR** — envanter satır satır doğrulandı

Üstel biçimin kullandığı her nicelik Ek C'de zaten kayıtlıdır ve **hiçbirinin rozeti veya değeri değişmez**:

| Nicelik | Ek C konumu | Üstelde rolü | Değişim |
|---|---|---|---|
| $C$ | Satır yok; Blok H'de $(Cq_n)$ **tek kalem [F]** (Ek C.1-(0), KARNE s.56) | $dP/d\chi=-C(P/P_0)$; $P=P_0$'da tam olarak eski $-C$ | **Yok** — aynı türev, aynı arka plan noktası |
| $q_n$ | Ek C.1 s.391: türetilmiş, $1{,}616\times10^{-19}$ m³/s, sıfır serbest parametre | $\nabla^2\chi=-q_nn_m$ **aynen** | Yok |
| $P_0$ | Satır 4, **[S]**, $\tfrac14\rho_nc_0^2=6{,}07\times10^{33}$ Pa | Üstelin ölçeği | Yok — kalibrasyon zinciri korunur |
| $\rho_0$ | Satır 5, **[S]**, $\rho_n/4$ | $c_{loc}=\sqrt{P/\rho_0}$ | Yok |
| $k$ | Satır 3, **[T]**, $k=0$ | Üstel **ancak** $k=0$ ile yazılabilir (yoğunluk korunur, basınç düşer) | Yok — güçlenir |
| $c_0$, $\rho_n$, $\alpha/\mathcal G$ | Satır 6 [T], 2 [G], 12 [S] | değişmez | Yok |

**Kanıt (cebirsel kapanış, yeni girdi yok):** M-46'nın kendi zincir denetimi $C\chi/P_0 = 4\Phi/c_0^2$ (19_Ek_M_Blok_I:268, %0,24) ⟹ $C\chi=\rho_n\Phi$ (= M-8'in $\Delta P_{yüzey}$'i). Üstelin üssü bu yüzden **hesaplanan** bir niceliktir: $-C\chi/P_0=-4\Phi/c_0^2$. Ayarlanabilir üs **yok**; $dP/d\chi=-C(P/P_0)^s$ yazılsaydı $s$ yeni parametre olurdu, ama $s=1$ **stiff hâl denkleminden zorunludur** ($K=\rho c^2=P$, çünkü $c^2=P/\rho$ — Kavrama Yasası, M-1). Yani $s$ ölçülmedi, **türetildi**.

**Envanter net olarak DARALIR:** 7.4 md.14 bugün *"$\beta$ türetilmeden öngörü $\frac{4-\beta}{3}\times43''$ olarak **belirsiz** kalır"* der — yani $\beta$ Ek C'de satırı olmayan ama fiilen belirlenmemiş bir kalemdi. Üstel onu $\beta=1$ olarak kapatır. **Bilanço: +0 / −1.**

Ek olarak M-46'nın **kendi Geçerlilik Sınırı** (19_Ek_M_Blok_I:225) *"Doğrusallaştırılmış rejim… güçlü-alan davranışı **yazılmamıştır**"* der: üstel yeni bir boşluk açmıyor, kitabın ilan ettiği boşluğu dolduruyor.

## 2) EK C ROZET DEĞİŞİMLERİ: **HİÇBİRİ**

Denetim sonucu — soruda varsayılan iki değişim de **gerçekleşmiyor, çünkü o satırlar yok**:

- **$\beta$'nın Ek C'de satırı yoktur** (grep doğrulandı). "F/A → T" geçişi uygulanamaz; $\beta$ yalnız 7.4 md.14 ve M-42 Geçerlilik Sınırı/Açık Uçlar'da yaşıyor. Rozet değişimi **M-42 kataloğunda** olur, envanterde olmaz.
- **$\Lambda$'nın da satırı yoktur.** KARNE:266'nın *"$\Lambda$ envanterde zaten [T]"* cümlesi gevşektir — $\Lambda$ yalnız satır 6 ($c_0$) ve satır 19 ($\xi$) metinlerinin içinde geçer.
- Satır 4/5/6/19 ve $(Cq_n)$: **rozet ve değer aynen kalır**; yalnız satır 6'nın formül metnine $\Lambda=e^{-\Phi/c_0^2}$ yazılır.
- Ek C.1'in **"5 skaler + 2 profil"** sayımı değişmez. *(Ayrı kayıt: bu sayım hâlâ $\tau$ ve $\delta$'yı serbest sayıyor; KARNE s.60 ikisini 10 Ağu'da [T] yapmıştı — üstelle ilgisiz, önceden var olan bayatlık.)*

**Gerçek rozet değişimleri (Ek C dışında):** M-42 Geçerlilik Sınırı "birinci mertebedir" → yapı tam; M-42 Açık Uçlar "$\beta$ parametresi" → **kapandı, $\beta_{PPN}=1$ [T]**; H.2 kalem 1′ → kapandı; H.3 son satır "Türetilemiyor" → **Sınandı ✓ 0,69σ**; M-46 → [T (yapı) / F ($C$ değeri)] **aynen** (üstel $C$'nin değerini gerektirmez).

## 3) 7.4 md.14 — **TAM KAPANIR**, ama silinmez: kapanış kaydına + yeni kaleme dönüşür

`Kisim_7_Tartisma_ve_Sonuc/04_Tartisma_ve_Sonuc.md`

- **s.165 (1. paragraf): AYNEN KALIR** — birinci mertebe muhasebesi ($\gamma=1$, bükülme/jeodetik/Shapiro/Cassini) değişmiyor.
- **s.167: TAMAMI YENİDEN YAZILIR.** Düşecek dört cümle:
 1. *"Geriye **ikinci mertebe** kalır."*
 2. *"…ortamın doğrusal-olmayan tepkisi, yani $P(\Phi)$ hâl ilişkisinin $O(\Phi^2/c_0^4)$ terimi gereklidir."* → terim **ek** değil: stiff ortamda tepki **çarpımsaldır**.
 3. *"$\beta$ türetilmeden öngörü $\frac{4-\beta}{3}\times43''$ olarak belirsiz kalır."* → $\beta=1$; **42,9805 as/yy ↔ 42,9799 ± 0,0009 (0,69σ)**.
 4. ⚠ *"**Bu, teorinin Genel Görelilik'in klasik sınavları karşısındaki kalan tek boşluğudur** ve aynı zamanda **ayırt edicilik için en umut verici yerdir**"* → **kitaptaki en yüksek görünürlüklü düşen cümle.** İkinci yarısı yalnız düşmez, **tersine döner**.
- **s.169: "ilk ikisi kapanmıştır" → "üçü de kapanmıştır."**
- **Yerine açılacak kalem (md.14′):** üstel biçimin M-50 birleşik eyleminden **türetilmesi** ($K=P$ argümanı stiff EoS'tan geliyor, ama biçimin tekliği eylem düzeyinde gösterilmedi) + güçlü-alan muhasebesinin yeniden kurulması (aşağıda). md.16 ile aynı arazidedir.

## 4) KARNE — güncellenecek ve girecek satırlar

**Güncellenecek:** `00_KARNE_Dogrulama_Durumu.md`
- **s.25–27** §0: *"Geçilmiş ayırt edici sınav: SIFIR"* **doğru kalır** (Merkür klasik GR sınavıdır, ayırt edici değil). Eklenecek: son klasik GR açığı kapandı; 1PN **ve** $\beta$ mertebesi artık GR ile tam dejenere.
- **s.46** S-5 (Minimum karadelik kütlesi, ⚠ Gerilim/GW230529) → **🔄 yeniden okunmalı**: ufuk yoksa eşik "oluşamaz" değil "gölge vermez"dir; iddia **zayıflar**, gerilim biçim değiştirir.
- **s.93** "Diğer açıklar" listesinden **md.14 çıkar**.
- **s.135** Önerilen sıra, öncelik 7'den **md.14 çıkar**.
- **s.264** $\Lambda_{grav}=1-\Phi/c_0^2$ → $e^{-\Phi/c_0^2}$.
- **s.292–295** ⚠ 11.4-iv: *"M→1 … teorinin Lorentz'den ayrıldığı **tek** yer, dolayısıyla **kalan tek ayırt edici arena**"* → **"tek" düşer**; güçlü-alan $\Lambda_{grav}$ ikinci ve gözlemsel olarak canlı arena.
- **s.70** §3 Kapananlar'a md.14 eklenir.

**Yeni satırlar:**
- **§1 sınav tablosuna (s.48'den sonra) S-12 — Karadelik gölge çapı.** $b_{krit}=2e\mu=5{,}4366\mu$ ↔ GR $3\sqrt3\mu=5{,}1962\mu$ (**+%4,63**), $r_{ph}=2\mu$. Parametresiz. Veri hazır (EHT; kaynak kitapta zaten: `Kisim_3_Makro_Evren/99_Kaynakca.md:27`). **Dürüstlük şartı:** bugünkü EHT halka-çapı sistematiği (~%10, M87\*) %4,6'yı ayırmaz ⟹ statü *"kuruldu, koşulabilir; bugünkü duyarlılıkta ayırt etmez"*. Aksi hâlde aşırı iddia olur.
- **§1'e S-13 — Ufuk yokluğu / sonlu kızıla kayma.** $\Lambda=e^{-\mu/r}$ hiçbir sonlu $r$'de sıfırlanmaz; $r=2\mu$'de $1+z=1{,}65$, $r=0{,}1\mu$'de $2{,}2\times10^4$. GR $z\to\infty$ der ⟹ **kategorik** ayrım. Ölçüm yolu tanımlanmadı.
- **§4 (geri alınanlar tablosuna, s.122'den sonra) iki satır:** (a) *"Merkür'ün açık kalması kullanılan yapının cinsinden gelen bir sınırdır"* (M-42:1371) → ❌ sınır doğrusallaştırmadandı; (b) *"kalan tek boşluk"* → ❌ boşluk yok, ve bedeli 1PN dejenerasyonu.
- **§6 günlüğe** (s.830 üstüne) 17 Ağustos 2026 kaydı + s.279/11.4.8.1 kalıbında **muhasebe kutusu**.

## 5) GÜNCELLENECEK DOSYA:SATIR LİSTESİ

**A. Çekirdek (M-42 / 7.4 / M-46)**
- `Kisim_7_Tartisma_ve_Sonuc/04_Tartisma_ve_Sonuc.md`:**165, 167, 169**
- `Kisim_8_Ekler/18_5_Kuvvet_Matematigi.md`:**1292** (kutulu $\Lambda\equiv1-\Phi/c^2$), **1300** ($n_{eff}$), **1317**, **1348–1352** ($P_0$ zinciri: birinci mertebe kesimi notu), **1356** (Geçerlilik Sınırı md.1), **1357** ("hâlâ kapanmamıştır" — silinir), **1362** (Açık Uçlar $\beta$ → kapandı), **1365** (Ayırt edicilik), **1367–1371** (28 Tem denetim notu → geri alma kaydı), **1651** (H.2 kalem 1′), **1693** (H.3 son satır)
- `Kisim_8_Ekler/19_Ek_M_Blok_I_Eylem_Ilkesi.md`:**204** (Varsayım 3: türev arka planda), **211** (Adım 2: $P=P_0e^{-C\chi/P_0}$; doğrusal = birinci mertebe kesimi), **225** (güçlü-alan artık yazılı), **268** (zincir denetimi artık yapısal)
- `Kisim_6_Kanitlar/03_Ekvatoral_Vorteks_ve_Yorunge_Anomalileri.md`:**178** ("Karşı Kayıt — kalan kalem" kutusu tamamı)
- `Kisim_4_Bilimin_Tekilligi/02_Evrensel_Sabitler_4_Sinirlar_ve_Itirazlar.md`:**55–57** ($\Lambda$ biçimi), **63** (parantez içi "Kalan kalem")
- `Kisim_1_Giris/03_Evrenaki_Postulasi.md`:**359** (Ek C satır 6 metni), **308** (Postülat 7 kutusu: "karadelik ufkunda 1'e yaklaşır"), **391/393** (Ek C.1'e $\beta_{PPN}$ [T] kaydı)
- `Kisim_11_Astronomik_Dogrulamalar/04_Saturn_Halkalari_ve_Dikey_Salinim.md`:**920, 922, 935, 937** (11.4.8.1: $\Lambda_{grav}$ biçimi + "geriye ne kalıyor" listesine güçlü alan)
- `00_KARNE_Dogrulama_Durumu.md`: yukarıdaki satırlar

**B. Ufuk bağımlı makine (en büyük yan hasar — üstelde ufuk YOK)**
- `Kisim_8_Ekler/18_5_Kuvvet_Matematigi.md`:**1171–1179** (M_min türetimi $R_\rho=R_s$ → $R_\rho=r_{ph}=2\mu$; **sayı aynı: 8,26 ↔ kitaptaki 8,3**, anlam "ufuk eşiği" → **"gölge eşiği"**), **1673** (H.3 satırı), **1133** (kompaktlık tablosu "Karadelik ufku"), **1161**
- `Kisim_6_Kanitlar/03_...md`:**158** (aynı tablo)
- `Kisim_11_Astronomik_Dogrulamalar/03_Kutle_Spin_Iliskisi_ve_Zarf_Rejimleri.md`:**200, 1006** ($L(M,t)$'nin "ufuk tavanı" $\mathcal GM^2/c$ terimi), **1014** ("çökmüş gövdede ufuk olarak görünür"), **1021–1022** (R3/R4), **1856, 1858** ($a^*=1$ ufuk tavanı), **459, 1268, 1694** (şekil etiketleri)
 *Hafifletici:* s.1014 iki tavanın 1,8 kat içinde çakıştığını zaten yazıyor ⟹ $r_{ph}$ tabanına taşıma **ucuz**, ama **yapılmadan yayına girmemeli**.

**C. Bedava toplanacak iki önceden var olan bozukluk**
- **Atıf hatası: "7.4 md.12" → "md.14"** (md.12 galaktik kalemdir): `18_5:1371`, `18_5:1693`, `Kisim_6/03:178`, `Kisim_4/02:63`.
- **Sembol çakışması — $\beta$ beş anlamda:** $v/c_0$ (resmî: `Kisim_8_Ekler/08_Sembol_Sozlugu.md:101` ve **S-22:211**), Prandtl–Glauert $\sqrt{1-M^2}$ (11.4.8.1:892–906), F4 payı $Br/\mathcal GM$ (11.1:371), donmuş kesir (11.7:461–463), ve **PPN $\beta$** (sözlükte **kayıtlı değil**). $\beta$ "belirsiz kalem"den **[T] sonuç**a yükselince çok daha sık anılacak ⟹ **$\beta_{PPN}$ olarak ayrı sembol** ve S-29 kaydı zorunlu.

**D. ⚠ Tanımsal zorunluluk — 17 Ağustos 2026 $\Phi$ kararına dokunur**
`Kisim_8_Ekler/08_Sembol_Sozlugu.md`:**130** ve **217 (S-28)**: $\Phi=(P_0-P)/\rho_n\ge0$ **ile** $\Phi=\mathcal GM/r$ üstelde **ikisi birden tam olamaz**. Tam olan: $\Phi\equiv\mathcal GM/r$ ($\chi$'den, M-46) ve $P=P_0e^{-4\Phi/c_0^2}$; dolayısıyla $(P_0-P)/\rho_n=\Phi$ **birinci mertebe okumasına** iner (tam tersi: $\Phi=\tfrac{c_0^2}{4}\ln(P_0/P)=-c_0^2\ln\Lambda$). Yazar kararı gerekir. `Kisim_11/01_Denge_Gelgiti...md:23` ($\Phi_{it}$) aynı turda hizalanır.

## 6) KAZANÇ–KAYIP MUHASEBESİ (11.4.8.1 kalıbında)

**Kazanılan (dört kalem):**
1. **Merkür kapandı** — 42,9805 as/yy ↔ 42,9799 ± 0,0009, **0,69σ**; sıfır yeni parametre. Kitabın klasik GR sınav kümesi (bükülme · Shapiro · kızıla kayma · jeodetik · çerçeve sürüklenmesi · LAGEOS · günberi) **tamamlandı**.
2. **$\beta_{PPN}$: belirsiz → [T] = 1** (sayısal 0,999933). $(2+2\gamma-\beta)/3=(7-\kappa)/6$ ile üstel $\kappa=1\Rightarrow1$.
3. **M-46'nın ilan ettiği güçlü-alan boşluğu doldu** (19:225).
4. **İç tutarlılık yükseldi:** kütle-itim $a=-(1/\rho_n)dP/dr$ ile etkin yapının statik ivmesi **1,0000000000** (4 yarıçapta). Doğrusal yazımda bu yalnız birinci mertebede tutar ⟹ M-2 ↔ M-42 artık **tam** uyumlu.
5. **Bonus epistemik kazanç:** Merkür artık "boşluk" değil **seçici sınav** — doğrusal yazım 50,1439 as/yy ile **7960σ dışlanır**. Gözlem iki aday hâl ilişkisi arasında **seçim yaptı**.

**Kaybedilen (iki kalem):**
1. ⚠ **Teorinin ilan ettiği en umut verici ayırt edicilik kanalı yok oldu.** 7.4 md.14 aynen şöyle diyor: *"aynı zamanda ayırt edicilik için en umut verici yerdir… ayrışma ancak $\beta$'da veya daha yüksek mertebede aranabilir"*; H.2 kalem 1′ ise *"GR'dan ayrışmanın aranacağı **tek yer**"*. $\beta=1$ ile teori **1PN'de VE $\beta$ mertebesinde** GR'dan ayrışmaz. Zayıf alanda kalan tek yol $\ge$2PN'dir ve hesaplanmamıştır. **Bu, 11.4.8.1'in $\Lambda_{kin}$ turuyla aynı türden ikinci kayıptır: teori bir arenada daha Einstein fenomenolojisini birebir üretir hâle geldi.**
2. **Ufuk makinesi tabansız kaldı.** Kazanç ($\Lambda$ sonlu $r$'de sıfırlanmaz ⟹ ufuk yok, tekillik yok) aynı zamanda bedeldir: 11.3'ün $L(M,t)$ yasasındaki **"ufuk tavanı" $\mathcal GM^2/c$**, R4 rejimi (*"zarf yok, ufuk var"*), $a^*=1$ tavanı (2.527 nesne, Şekil 11.3.D), M-40'ın ergosfer okuması ve M_min'in $R_\rho=R_s$ kesişimi — **hepsi Schwarzschild ufkuna dayanıyor.** Yeniden temellendirme $r_{ph}=2\mu$ ile mümkün ve ucuz (s.1014 çakışmayı 1,8 kat içinde zaten yazıyor), ama **yapılmamış iştir**. M_min'in iddiası da zayıflar: "karadelik oluşamaz" → "gölge oluşmaz" (S-5/GW230529 gerilimi bu yüzden yeniden okunmalı).

**Doğan yeni ayırt ediciler (iki):**
- **S-12 · Gölge çapı +%4,63** ($2e\mu$ ↔ $3\sqrt3\mu$) — parametresiz, veri ve kaynak hazır. **Ama bugünkü EHT sistematiği (~%10) bunu ayırmaz** ⟹ "koşulabilir ama bugün karar vermez"; ngEHT/uzay-VLBI sınıfı duyarlılıkla belirleyici olur. *(Bu kaydı düşmeden yayına girmemeli — yoksa kayıp bir ayırt ediciyi ölçülemez bir ayırt ediciyle örtmüş oluruz.)*
- **S-13 · Ufuk yokluğu / sonlu kızıla kayma** ($r=2\mu$'de $1+z=1{,}65$ ↔ GR $\infty$) — **kategorik** ve teorinin şimdiye kadarki en sert GR ayrımı; ölçüm yolu tanımlanmadı.

**Tek cümlelik hüküm:** Üstel yapı **sıfır serbest parametre ekleyerek** kitabın son klasik GR açığını kapatır ve envanterin hiçbir rozetini oynatmaz; bedeli, teorinin zayıf alanda ilan ettiği son ayrışma umudunun ölmesi ve ufka dayanan 11.3/M-40 makinesinin foton küresine yeniden temellendirilmesi gereğidir — ayrım arenası artık zayıf alandan **güçlü alana** taşınmıştır.