# EŞ-DÜZLEMLİLİK ve ORTAM DÖNÜŞÜ — Çözüm ve Bedel Muhasebesi

> Çalışma dosyası · 17 Ağustos 2026 (Opus) · `ortam_hiz_alani_cozumu.md` §8'in 2. kaleminin kapatılması
> Sınav: `es_duzlemlilik_sinavi.py` · Defter: Tartışma #4'ün eki

---

## 1. Soru

Ortam dolaşmıyorsa (Tartışma #4: kohezyonla tutulan statik denge, Ω ≲ 1,4×10⁻¹⁸ rad/s), kitabın **yörünge eş-düzlemliliği** ve **prograd tercih** anlatıları ayakta kalır mı?

## 2. EŞ-DÜZLEMLİLİK: ✅ hiçbir şey kaybedilmiyor — kitap zaten doğru yere koymuş

Kitabın kendi üç kaydı, eş-düzlemliliği ortam dolaşımına **hiç** bağlamıyor:

| Yer | Kitabın ifadesi |
|---|---|
| `18_5:313` | *"Eş düzlemliliğin gerçek adresi **F5'in düzlem seçimidir** (M-39, 11.4.2–11.4.4)"* |
| `11.4:1172` | *"Ayakta duran şey F5'in düzlem seçimidir — **korunumludur, sönüm gerektirmez**"* |
| KARNE s.35 | *"**Eş-düzlemlilik için mekanizma borcu yoktur.** Eğiklik korunumludur; donmuş niceliği tutmak için kuvvet gerekmez, gereken tek şey **dağıtacak kanalın olmamasıdır**. F5'in 1 AU'daki zayıflığı (1,1×10⁻¹⁵) eksiklik değil, **aranan şeydir**"* |

**F5'in kaynağı gövdenin kendi dönüşüdür**, ortam dolaşımı değil: f_yanal = −(κ₅ρv_e²/r)·sin2θ — burada v_e gövdenin **ekvator hızı**. Kararlılık analizi (θ>0 ⇒ kuvvet −θ̂; θ<0 ⇒ +θ̂) ekvatoru kararlı, kutbu kararsız denge yapıyor. **Ortam dolaşımı denklemde hiç yok.**

Üstelik kitabın mantığı daha da güçlü: eğiklik **korunumlu** bir niceliktir; onu düzlemde tutmak için sürekli bir kuvvet gerekmez — yalnız onu dağıtacak bir kanalın olmaması gerekir. Statik ortam bu koşulu **daha iyi** sağlar (dolaşan bir ortam, kesme yoluyla eğiklik dağıtan bir kanal olurdu).

**Prograd tercih ve dairesellik:** `18_5:313` bunları zaten açıkça açık kalem ilan etmiş — *"dairesellik ve prograd tercihin bu teoride şu an kanıtlanmış bir mekanizması **yoktur** — açık kalem olarak kayıtlıdır (7.4)"* (ayrıca 11.4-viii). Yani kitap prograd tercihi **hiçbir zaman** ortam dolaşımına dayandırmamış. **Kayıp yok.**

## 3. GERÇEK BEDEL: 81 çarpanı ve prograd tork kümesi

Ortam dolaşımına *fiilen* dayanan bir sonuç kümesi var ve statik çözüm onu düşürüyor:

**81 çarpanının kökeni** (`05_Oturma_Yaricapi:136–138`, DY-2, KARNE:765): Δv = |v_cisim − w|, w = 2v_yör prograd ⇒ prograd cisim için Δv = v, retrograd için Δv = 3v; sürükleme ∝ Δv⁴ ⇒ **3⁴ = 81**.

| Kurulum | prograd Δv | retrograd Δv | oran Δv⁴ |
|---|---|---|---|
| Dolaşan ortam (w = 2v_yör) | v | 3v | **81** |
| **Statik ortam (w = 0)** | v | v | **1** |

**Düşen kalemler:** Triton'un 81 katı (11.5.3) · DY-2'nin Δv = v_yör√(5−4cos i) eğiklik bağımlılığı (i=0'da 1, i=180°'de 3 verirdi; statikte her i için 1) · prograd tork ve ondan çıkan AU-kararlılığı η_E sınırı (`11.4:811`) · M-39'un R2 rejiminde "M-22 hız kaynağı" atfı (`18_5:565`).

**Hafifletici üç kayıt:**
1. **Prograd hesaplar DEĞİŞMİYOR.** Dolaşan ortamda prograd cisim için Δv = |v − 2v| = v; statikte Δv = |v − 0| = v — **aynı**. Yalnız retrograd kalemler değişiyor (81 kat zayıflıyor). Kitabın sürükleme hesaplarının neredeyse tamamı prograd cisimler için.
2. **Phoebe'nin η_E sınırı gevşiyor, sıkışmıyor.** 81 katı retrograd sürüklemeyi *güçlendiriyordu*; onun kalkması Phoebe'nin 4 Gyr hayatta kalmasını **kolaylaştırır** ⇒ η_E üst sınırı 81 kat gevşer. En sıkı sınır zaten başka kanaldan (Satürn halkası, ≲2,3×10⁻¹¹ Pa·s) geliyor, dolayısıyla defter bozulmuyor. Postülat 7'nin 10²⁸ bastırma argümanı da 81'e dayanmıyor.
3. **Kitap sınavı zaten tanımlamış.** 7.4 md.15: *"Aynı geometrili prograd/retrograd uydu çiftlerinde … **fark sıfır çıkarsa** girdap kesme katsayısının sınırı bir kademe daha düşer."* Statik çözüm tam olarak **"fark sıfır"** öngörüyor. Yani kayıp bir öngörü değil, **karara bağlanmış** bir öngörü: iki dışlayıcı seçenek, tanımlı sınav.

## 4. Ve statik resmi doğrulayan İKİNCİ bağımsız gözlem: Ay

Ortam dönüşünün gözlemsel imzası apsis sürüklenmesidir (sürüklenme hızı = Ω_ortam). Dolaşan ortam varsayımında:

| Sistem | Ω_m = 2v_yör/r | Sürüklenme periyodu | Gözlenen |
|---|---|---|---|
| Merkür (Güneş ortamı) | 1,65×10⁻⁶ rad/s | 44,0 gün | 42,98″/yy ⇒ **dışlanır (10¹²σ)** |
| **Ay (Dünya ortamı)** | 5,30×10⁻⁶ rad/s | **13,73 gün** | perigee presesyonu **8,85 yıl** ⇒ **236 kat aşım, kesin dışlanır** |
| Titan (Satürn ortamı) | 9,12×10⁻⁶ rad/s | 7,97 gün | *hesaplanmadı — açık* |

**Ay kritik çünkü Dünya'nın zarfının içinde** (60 R_⊕ < 235 R_⊕) — yani Güneş'in ortamını değil, **Dünya'nın ortamını bağımsız olarak** sınıyor. LLR'nin mm hassasiyetiyle ölçülmüş 8,85 yıllık perigee presesyonu, 13,7 günlük bir sürüklenmeyle uzlaşamaz.

**Sonuç: iki ayrı gövdenin ortamı (Güneş ve Dünya), iki bağımsız gözlemle statik ilan ediliyor.** Kohezyonla tutulan statik denge, ikisini birden açıklayan tek resim — ve dolaşımın *neden* olmadığını da açıklıyor (zorunlu değil; kohezyon yükü taşıyor).

## 5. Kitapta düzeltilecekler (eş-düzlemlilik turu)

| Yer | İşlem |
|---|---|
| `18_5:313` | **DOKUNULMAZ** — zaten doğru: eş-düzlemlilik F5'te, prograd tercih açık kalem. Yalnız "ortam dolaşımı" ima eden hiçbir şey eklenmemeli. |
| `18_5:376` | *"F5 **dolaşımı** gövdenin dönme düzlemine kilitler"* → dolaşım artık ~0; cümle "F5, **ortamın teğetsel yapısını** ve düzlem kimliğini gövdenin dönme düzlemine kilitler" gibi dolaşımdan bağımsız yazılmalı |
| `18_5:565` | M-39'un R2 rejiminde *"M-22 (R2'de hız kaynağı)"* atfı → M-22 opsiyonel dinamik durum; R2'nin hız kaynağı yeniden gerekçelendirilmeli |
| `05_Oturma_Yaricapi:136–138` | **81 çarpanı kaldırılmalı** veya "dolaşan-ortam senaryosunun öngörüsü" olarak koşullu yazılmalı; statik senaryonun öngörüsü **oran 1** eklenmeli |
| `KARNE:765` | DY-2'nin Δv = v_yör√(5−4cos i) bağıntısı → statikte Δv = v_yör (eğiklikten bağımsız) |
| `11.4:782, 786, 811` | *"ortamın siklostrofik dolaşımı… her yarıçapta prograd ve maddeden hızlı"* → koşullu/kaldırılmalı; AU-kararlılığı η_E sınırı prograd torka dayandığı için geri çekilmeli |
| `98_Ne_Ogrendik:63` | Triton'un 81 katı sorusu → *"dolaşan ortam senaryosunda 81, statik senaryoda 1; sınav 7.4 md.15"* |
| **7.4 md.15** | Sınavın öngörüsü **netleşiyor**: statik ortam ⇒ **fark sıfır**. Kalem "beklenti belirsiz"den "iki dışlayıcı senaryo, biri gözlemle seçilmiş" statüsüne yükselir |
| **KARNE, yeni satır** | **Ay perigee presesyonu = Dünya ortamının dönüş sınavı** (Merkür'ün Güneş için yaptığının Dünya karşılığı) |

## 6. Kalan açık (dürüst kayıt)

1. **Satürn ortamı sınanmadı.** Titan/Phoebe apsis presesyonlarıyla Satürn'ün ortamının dönüşü bağımsız olarak kilitlenebilir; hesap yapılmadı. Beklenti: aynı sonuç (statik).
2. **Prograd tercih ve dairesellik hâlâ açık** — ama bu, statik çözümün getirdiği bir borç değil; kitapta zaten kayıtlıydı (`18_5:313`, 11.4-viii). Statik resim bu kaleme yeni bir zorluk **eklemiyor**, ama bir aday mekanizmayı (prograd ortam torku) da **elinden alıyor** ⇒ kalemin zorluğu artıyor, dürüstçe yazılmalı.
3. **Dolaşımın tam sıfır mı, yoksa çok küçük mü olduğu** açık: Merkür Ω ≤ 1,4×10⁻¹⁸ rad/s verir, sıfır demez. Kohezyon resmi sıfırı *izinli* kılar, *zorunlu* kılmaz (açısal momentum serbest). Formasyon senaryosu neden ~0 verdiğini açıklamalı — yeni açık kalem.
4. **Kesme tabakası** (zarf sınırı, 30/220 km/s) statik resimde gerçek bir kesme tabakasıdır; yitim/tork hesabı eski açık kalem olarak duruyor.
