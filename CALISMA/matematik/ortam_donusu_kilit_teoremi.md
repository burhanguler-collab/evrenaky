# ORTAM DÖNÜŞÜ KİLİT TEOREMİ — Satürn ve ötesi

> Çalışma dosyası · 17 Ağustos 2026 (Opus) · `ortam_hiz_alani_cozumu.md` §8 kalem 1'in kapatılması
> Sınav: `saturn_ortami_sinavi.py` · Önceki: `ortam_dolasimi_mp.py`, `es_duzlemlilik_sinavi.py`

---

## 1. Genel teorem (Satürn'ü hesaplarken çıktı — beklenenden çok daha güçlü)

Siklostrofik ortam dolaşımı w(r) = 2v_yör(r) = 2√(𝒢M/r) alınırsa, apsis sürüklenme hızı:

$$\Omega_m = \frac{w}{r} = \frac{2\sqrt{\mathcal{G}M/r}}{r} = 2\sqrt{\frac{\mathcal{G}M}{r^3}} = \boxed{2n}$$

**Ortamın açısal hızı, tam olarak yörüngenin ortalama hareketinin iki katıdır** — kütleden ve yarıçaptan bağımsız. Sayısal denetim (Merkür, Ay, Titan, Mimas): oran **2,0000000000** dört sistemde de.

### Bunun anlamı kategorik, nicel değil
Ω_m = 2n ise apsis çizgisi, **her radyal periyotta tam iki tur** atar. Yani yörüngeler kapalı elips **olmaz** — hızla dönen bir rozet olur. Kepler elipsleri var olamaz.

> **Gözlenen kapalı elipslerin varlığı, tek başına, ortamın dolaşmadığının kanıtıdır.**

Bu, hassasiyet tartışmasına açık bir sınav değil: model tümüyle çöker. Ölçüm hassasiyeti yalnız **kalan** dönüşün üst sınırını belirler.

## 2. Satürn ortamı kilitlendi

J₂-hâkim apsidal presesyon (ω̇ = 1,5·n·J₂·(R_S/a)²/(1−e²)²) ile karşılaştırma:

| Uydu | a (km) | P_yör (gün) | Gözlenen apsis periyodu | Dolaşan ortamın vereceği | **Dışlama** |
|---|---|---|---|---|---|
| Mimas | 185.539 | 0,944 | **1,0 yıl** | 11,3 saat | **776×** |
| Enceladus | 237.948 | 1,371 | 2,4 yıl | 16,5 saat | 1.276× |
| Tethys | 294.619 | 1,888 | 5,1 yıl | 22,7 saat | 1.956× |
| Dione | 377.396 | 2,738 | 12,0 yıl | 1,4 gün | 3.209× |
| Rhea | 527.108 | 4,519 | 38,7 yıl | 2,3 gün | 6.261× |
| **Titan** | 1.221.870 | 15,948 | **733 yıl** | **8,0 gün** | **3,36×10⁴** |
| Iapetus* | 3.560.820 | 79,340 | ~31.000 yıl (J₂) | 39,7 gün | 2,85×10⁵ |

\*Iapetus'ta Güneş pertürbasyonu J₂'yi aşar; J₂-yalnız kestirimi gerçek gözleneni temsil etmez — **sağlam sınır Titan'dır.**

**Titan tek başına yeter:** apsisi 733 yılda bir tur atıyor; dolaşan ortam **8 günde** bir tur döndürürdü. Cassini-öncesi astrometri bile bunu görürdü.

**Phoebe (retrograd, 12,95×10⁶ km):** dolaşan ortamda apsisi 4 Gyr'de **5,3×10⁹ tur** atardı.

## 3. Kaç bağımsız ortam kilitlendi

| # | Ortam | Sınayan gözlem | Dışlama | Kalan dönüş üst sınırı |
|---|---|---|---|---|
| 1 | **Güneş** | Merkür günberi (Park+2017: 575,3100 ± 0,0015 ″/yy) | 1,87×10⁶ | **≤ 2,3×10⁻¹⁸ rad/s** |
| 2 | **Dünya** | Ay perigee 8,85 yıl (LLR) | 237× | ≤ ~2×10⁻¹⁶ rad/s |
| 2b | Dünya | LAGEOS-2 düğüm/apsis (J₂ hâkim) | 4.489× | — |
| 3 | **Satürn** | Titan apsisi 733 yıl | 3,36×10⁴ | ≤ ~2,7×10⁻¹⁵ rad/s |
| 4 | **Jüpiter** | Io apsisi (J₂ hâkim) | 3.158× | — |

**Dört ayrı gövdenin ortamı, dört bağımsız gözlem ailesiyle statik ilan ediliyor.** Kohezyonla tutulan statik denge (τ_rr = ρₙΦ/2, Σ'nın 14–15 mertebe altında) dördünü birden açıklayan tek resim.

## 4. Σ'nın statüsü yükseldi — bu bölümün en önemli sonucu

Teorem kategorik olduğu için, **statik ortam bir seçenek değil zorunluluktur**: Kepler elipslerinin varlığı ortamın dolaşmamasını dayatıyor. Ve teorinin elinde kuyuyu dolaşmadan tutacak **tek** mekanizma kohezyondur (M-4'ün Σ'sı, M-5'in kesme kanalı).

Dolayısıyla Σ'nın rolü değişiyor:
- **Önce:** Bell/Salart deneylerinden alttan sınırlanmış, başka hiçbir yere yük taşımayan bir parametre (Ek C'de serbest kalem).
- **Şimdi:** **Kepler yörüngelerinin var olabilmesinin yapısal koşulu.** Kohezyon olmasa ortam dolaşmak zorunda kalır, dolaşırsa kapalı elips kalmaz.

Bu, Σ için **Bell deneylerinden tamamen bağımsız, ikinci bir gerekçe** ve teorideki en eski "yalnız alttan sınırlı" kalemlerden birine yapısal bir görev verir. *(Nicel olarak yeni bir alt sınır vermiyor — gereken τ = ρₙΦ/2 çok küçük olduğundan Σ'nın mevcut alt sınırı bol bol yetiyor. Kazanç kavramsal ve yapısal.)*

## 5. Kitaba yazılacaklar

| Yer | İşlem |
|---|---|
| **Yeni türetim** (M-9'un ekine ya da yeni katalog girdisi) | **Ortam Dönüşü Kilit Teoremi:** siklostrofik dolaşım ⇒ Ω_m = 2n ⇒ apsis yörünge başına iki tur ⇒ kapalı elips olamaz. Dört sistemde dışlama tablosu. |
| **M-9 Geçerlilik Sınırı** | *"madde düşer, ortam dolaşır"* → **"madde düşer, ortam gerilir"**; Euler'in kohezyonsuz limit olduğu + kilit teoremi atfı |
| **M-4 / M-5 (Σ)** | Σ'nın yeni yapısal görevi: kuyuyu dolaşmadan tutan kanal; Kepler elipslerinin varlık koşulu. Bell'den bağımsız ikinci gerekçe. |
| **M-37** | v_θ = 2v_yör → **kohezyonsuz üst sınır**; gözlemle dışlandığı kaydı (dört sistem) |
| **M-22** | Varsayım 2 (*"dönen ortam merkezkaç gereksinimini basınç gradyanıyla karşılar"*) → opsiyonel dinamik durum; gezegen ölçeğinde gözlemle dışlanmış |
| **KARNE** | Yeni sınav satırları: Merkür (Güneş ortamı) · Ay + LAGEOS (Dünya) · Titan (Satürn) · Io (Jüpiter). Statü: **Sınandı ✓** (dolaşım dışlandı, statik doğrulandı) |
| **81 çarpanı kalemleri** | `05_Oturma:136-138`, `KARNE:765`, `11.4:782,786,811`, `98_Ne_Ogrendik:63` → koşullu yazım veya geri çekme (bkz. `es_duzlemlilik_cozumu.md` §5) |

## 6. Kalan açık (dürüst kayıt)

1. **Dolaşımın neden ~0 olduğunun formasyon gerekçesi.** Kohezyon sıfırı *izinli* kılıyor, *zorunlu* kılmıyor (açısal momentum serbest bir başlangıç koşulu). Gözlem sıfır diyor; teorinin *neden* sıfır olduğunu söylemesi gerekir. **Yeni açık kalem.**
2. **Galaktik ölçekte durum.** Kilit teoremi yörünge apsisleri üzerinden çalışıyor; galaktik ölçekte apsis ölçümü yok. Galaktik ortamın dolaşıp dolaşmadığı **açık** — ve M-37'nin madde kolonu (dönüş eğrisi) buna bağlı olmadığı için (Tartışma #4) serbest kalabilir. Ama tutarlılık için bir hüküm gerekir: aynı kohezyon galaktik kuyuyu da tutabiliyor (τ/Σ = 8,9×10⁻¹⁵).
3. **Iapetus kanalı** Güneş pertürbasyonu hâkim olduğu için tam kullanılmadı; gerçek efemerid artıklarıyla çalışılırsa Satürn sınırı ~10⁻¹⁷'ye inebilir.
4. **Kesme tabakası** (zarf sınırı) yitim/tork hesabı — eski açık kalem, değişmedi.
