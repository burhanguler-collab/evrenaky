# KİTAP DÜZENLEME PLANI — Üstel Ölçek Yapısına Geçiş

> **DURUM: PLAN — HİÇBİRİ UYGULANMADI.** 17 Ağustos 2026 (Opus). Çalışma dosyası yöntemi gereği yayın metnine
> yalnız Enes "sonuçlandı" dediğinde, tek partide taşınır. Bu dosya o partinin tam listesidir.
> Dayanak: `tartısma_matematik` Tartışma #3 · `ustel_turetim_uc_yol.md` · `M52_Ustel_Olcek_Yapisi_TASLAK.md`

---

## 0. Geçişin özü (tek cümle, her düzenlemede kullanılacak formül)
Madde ölçeği **Λ = e^{−Φ/c₀²}** (tam biçim); Λ = 1 − Φ/c₀² onun **birinci mertebe kesimi**.
Basınç profili **P = P₀e^{−4Φ/c₀²}**; yayılma hızı **c_loc = c₀Λ²**; **n_eff = 1/Λ² = e^{2Φ/c₀²}**.
Yapısal ilişkilerin hiçbiri değişmiyor — yalnız Λ'nın biçimi tamamlanıyor.

---

## 1. YENİ GİRDİ — Ek M'ye M-52

**Dosya:** `Kisim_8_Ekler/` altına yeni bölüm ya da `18_5_Kuvvet_Matematigi.md` sonuna (Blok H'nin devamı).
**Kaynak:** `M52_Ustel_Olcek_Yapisi_TASLAK.md` (denetim sonucu üretildi) + `ustel_turetim_uc_yol.md`'nin üç yolu.
**Rozet önerisi:** **[T]** (türetilmiş) — üç bağımsız yol + sıfır yeni parametre; β'nın gözlemle kilitlenmesi [S] değil doğrulama.
**Şablon:** Varsayımlar → Adımlar → Sonuç → Sayısal Çapraz Kontroller → Geçerlilik Sınırı → Açık Uçlar.
**Zorunlu içerik:**
- Türetim sıralaması: (i) çarpımsal ölçek bileşimi (11.4.8.1 + M-46 Poisson lineerliği ⇒ üstel zorunlu), (ii) yerellik/Postülat 4 (sabit C gizli evrensel sabit), (iii) stiff entalpi (M-3′).
- β = 2n−1 ailesi; Merkür'ün n'yi 1,000000 ± 3,1×10⁻⁵'e kilitlemesi.
- İkinci-mertebe belirsizliğinin kalkması (β için +½ ↔ −1 ikiliği).
- Korunan gözlemler tablosu (bükülme 1,7512″, Shapiro 247,2 µs, kızıla kayma, P₀, jeodetik, Lorentz null).
- Yeni ayırt edici sınav: gölge +%4,63 (2e vs 3√3); Sgr A* 55,73 ↔ GR 53,27 µas.
- Ufuk yokluğu ve tekilliksizlik: artık iddia değil **yapısal sonuç**.
- Kazanç–kayıp muhasebesi (kitabın 11.4.8.1'deki dürüstlük usulüyle).

---

## 2. M-42'NİN YENİDEN YAZIMI (en kritik düzenleme)

**Dosya:** `Kisim_8_Ekler/18_5_Kuvvet_Matematigi.md`, M-42 bölümü (~satır 1260–1370).

| Yer | Şimdi | Olacak |
|---|---|---|
| ~1290 kutulu sonuç | `Λ ≡ 1 − Φ/c₀²` | `Λ ≡ e^{−Φ/c₀²}` + "(birinci mertebede 1 − Φ/c₀²; tam biçimin türetimi **M-52**)" |
| ~1292 kutu içindeki `c^2` | çıplak `c` | `c_0` (Parti 3 notasyon borcu D-1 ile birlikte) |
| Kapanan Gözlemler tablosu | 5 satır | **Merkür satırı EKLENİR:** "Günberi kayması (Merkür) · **42,9805″/yy** · 42,9799±0,0009 ✓ (M-52)" |
| Geçerlilik Sınırı 1. madde | "Yapı **birinci mertebedir**… β belirlenmemiştir" | **Yeniden yazılır:** yapı artık tam biçimdedir; β = 1 türetilmiştir (M-52); geçerlilik sınırı ikinci mertebeden **üçüncü** mertebeye taşınır (üstel ile GR g_tt'de U²'ye kadar özdeş, U³'te ayrışır) |
| Geçerlilik Sınırı 2. madde | "**Merkür günberi kayması hâlâ kapanmamıştır**" | **KALDIRILIR** → kapandı kaydı (~~üstü çizili~~ + M-52 atfı) |
| Açık Uçlar: "β parametresi" | "Kapanırsa Merkür'ün 43″'si de kapanır — teorinin kalan tek klasik GR sınavı" | ~~üstü çizili~~ → "**kapandı (17 Ağu 2026, M-52):** β = 1, ortamın üstel yanıtından türetildi; Merkür 42,9805″ (0,69σ)" |
| Açık Uçlar: "Ayırt edicilik" | "γ=1 ile teori 1PN'de GR ile ayrışmaz; ayrışma β'da veya ikinci mertebede aranabilir" | **Yeniden yazılır:** β=1 ile 1PN'de ayrışma tümüyle kapandı; ayrışma artık **güçlü alandadır** — gölge çapı +%4,63 (M-52, ngEHT hedefi) |
| ~1361 "Yapının türü" denetim notu | "optik-ortam kuruluşu… kütleli cisim yörüngelerini tam üretmez; Merkür'ün payı indisin dışındadır" | **Yeniden yazılır:** eksik olan hız-bağımlılığı 11.4.8.1'in Λ_kin'iyle zaten mevcuttu; tam dinamik Λ = Λ_grav·Λ_kin eyleminden çıkar ve Merkür'ü verir (M-52). *Bu paragraf en dikkatli yeniden yazımı gerektiren yerdir — eski teşhis "yapının cinsinden gelen sınır" diyordu; doğrusu "ölçek çarpanının biçimi eksikti".* |

---

## 3. M-8 / Ek B — kalibrasyon zinciri (küçük ama zorunlu)

**Dosyalar:** `10_Ek_M_Blok_B_Arka_Plan_Basinci.md` (M-8), `17_Ek_B_Arka_Plan_Basinci.md`
- Adım 5 / satır 29: "madde ölçeği Λ = 1−Φ/c₀²" → "Λ = e^{−Φ/c₀²} (birinci mertebede 1−Φ/c₀²)".
- **Zincir sayısal olarak DEĞİŞMİYOR:** ΔP_yüzey = ρₙΦ ve δc/c₀ = −2Φ/c₀² birinci mertebede aynı ⇒ P₀ = ¼ρₙc₀² korunur. Buna bir **not** düşülmeli: "kalibrasyon birinci mertebe genliğini kullandığından üstel geçişten etkilenmez".
- M-8 Geçerlilik Sınırı'na ek: "türetim zayıf-alan genliğiyle yapıldı; tam profil M-52'dedir".

## 4. Sembol Sözlüğü — `08_Sembol_Sozlugu.md`
- Satır 87 (Λ hücresi): tanım `Λ ≡ 1 − Φ/c₀²` → `Λ ≡ e^{−Φ/c₀²}`; "Dünya yüzeyi için 1 − 7×10⁻¹⁰" değeri **aynen kalır** (birinci mertebe) ama "(birinci mertebe)" ibaresi eklenir.
- Satır 88 (c_loc): `n_eff = 1/Λ²` **aynen**; `= e^{2Φ/c₀²}` eklenir.
- **S-28 güncellenir:** içindeki `Λ = 1-Φ/c_0^2` → `Λ = e^{−Φ/c₀²}` (M-52).
- `R-10` kuralı **aynen geçerli** (Λ ↔ c_loc kategori ayrımı biçimden bağımsız) — dokunulmaz.

## 5. Kısım 2 — `04_Isik_Hizi_ve_Zerre.md`
Λ tanımı kutusu (satır ~43-45): üstel biçim + "birinci mertebede" notu. Popüler anlatı korunur.

## 6. Kısım 11.4.8.1 — `04_Saturn_Halkalari_ve_Dikey_Salinim.md`
- `Λ = Λ_grav·Λ_kin` kutusu (satır ~910): **Λ_grav = 1−Φ/c₀² → Λ_grav = e^{−Φ/c₀²}**.
- **Buraya bir kazanç notu eklenir:** çarpımsal yapı yalnız bir yazım kolaylığı değil; Λ_grav'ın üstel olmasını **zorunlu kılan** yapıdır (M-52 Yol 2). Yani bu bölüm, üstel türetimin ana dayanağıdır.

## 7. Kısım 7.4 — `04_Tartisma_ve_Sonuc.md` md.14
Tümüyle yeniden yazılır: "İkinci mertebe tepki (β) — Merkür" başlığı **kapandı** kalemine dönüşür; kitabın "GR'ın klasik sınavları karşısındaki kalan tek boşluk" ifadesi **kaldırılır**; yerine "1PN tamamlandı; ayrışma güçlü alana (gölge) taşındı" muhasebesi.

## 8. Karadelik bölümü — `18_5_Kuvvet_Matematigi.md` ~1171–1180
- M_min kutusu: formül **korunur** (8,26 M☉) ama gerekçesi değişir: `R_s` girdisi yerine **teori-içi foton küresi** r_ph = 2μ (üstel indisin Fermat ekstremumu). "GR'ın R_s'i girdi alınmıştır" borcu **kapanır**.
- Anlam değişimi yazılır: eşik **ufuk eşiği değil GÖLGE eşiğidir**; altındaki cisimler "ufuksuz" değil **gölgesiz kompakt gövdelerdir**.
- Kütle boşluğu iddiası bu okumayla yeniden yazılır (LIGO GW190814/GW230529 adayları bağlamında).
- **Yeni alt bölüm:** gölge çapı öngörüsü (+%4,63) ve EHT/ngEHT sınavı.
- **Yeni açık kalem (dürüst kayıt):** yıldız-kütleli cisimlerde yüzey ışıması (1+z ≈ 1,8) — teorinin cevap adayı (kilitli kafes büyüme cephesi, enerji kafes bağlanmasına gider) ve nicelleştirme programı.

## 9. KARNE — `00_KARNE_Dogrulama_Durumu.md`
Yeni satırlar: Merkür günberi [T, sınandı ✓], β = 1 [T], gölge çapı öngörüsü [T, sınanacak], ufuk yokluğu [T].
Güncellenecek: Λ satırları, M-42 satırı, "kalan tek klasik açık" ifadeleri.

## 10. Ek C parametre envanteri — `Kisim_1_Giris/03_Evrenaki_Postulasi.md`
β satırı (varsa): serbest/aralık → **türetilmiş [T]**. Yeni parametre **eklenmiyor** — bu açıkça kaydedilmeli.

---

## Uygulama sırası önerisi
1. M-52 girdisi yazılır (her şeyin atıf hedefi).
2. M-42 yeniden yazımı (2. madde) — en dikkatli iş.
3. Sözlük + Kısım 2 + 11.4.8.1 (biçim güncellemeleri).
4. M-8/Ek B notları.
5. 7.4 md.14 + karadelik bölümü + KARNE + Ek C.
6. Parti 3 notasyon süpürgesi (çıplak c → c₀ vb.) ile birleştirilebilir — M-42 kutusuna zaten dokunuluyor.

## Uygulanmadan önce beklenen kararlar
- **A2 (M-42 muhasebesi):** Üstel geçiş bu kararı ETKİLER — β artık türetilmiş olduğundan muhasebe yeniden yazılacak; Yol 1/Yol 2 seçimi bu yeni çerçevede ele alınmalı.
- Yüzey ışıması kaleminin nasıl sunulacağı (açık kalem mi, öngörü mü).
- M-52 numarası uygun mu (M-51 jeodetik için ayrılmıştı — jeodetik M-51, üstel M-52).
