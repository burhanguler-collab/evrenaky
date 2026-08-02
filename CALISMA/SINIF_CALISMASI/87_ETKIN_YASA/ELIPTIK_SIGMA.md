# Eliptik dış-σ sınavı (G-12) — M-48 ikinci bağımsız ailede GEÇTİ (iş 16)

**Veri:** Forbes+ 2017 (AJ 153, 114; CDS `J/AJ/153/114`, erratum-düzeltmeli table5) —
SLUGGS: 27 erken-tip galakside 3573 küresel-küme (GC) radyal hızı.
`veri/_sluggs_gal.dat`, `veri/_sluggs_gc.dat` — değiştirilmemiş.
**SPARC'tan bağımsız ÜÇÜNCÜ veri ailesi** (dSph ve MIGHTEE'den sonra).
Hesap: `../../eliptik_sigma_sinavi.py` (okuma kuralları betik başlığında, veriye bakılmadan).
Çıktı: [`SONUC_ELIPTIK_SIGMA.csv`](SONUC_ELIPTIK_SIGMA.csv).

Örnek: dış bölgede ($R>2R_{eff}$) $n_{GC}\geq15$ olan **22 galaksi** ($\log M_*$ 10,13–11,62).
Öngörü: M-48 köprüsü ($\alpha=2$; dSph betiğiyle birebir aynı biçim) + M-47 penceresi;
iç-kütle Hernquist profili; $a_0$ ve bütün sabitler **SPARC değerlerinde donmuş —
sıfır yeniden-kalibrasyon.**

## 1. SONUÇ — köprü üçüncü ailede de bire oturdu

$$\text{ANA (22 galaksi): medyan }\log(\sigma_{öng}/\sigma_{ölç})=+0{,}051\ \text{dex},\quad
\text{saçılma }0{,}092\ \text{dex}$$

- **Konvansiyon bandı sıfırı kapsar:** katalog $\Upsilon\!\approx\!1$ ile $+0{,}051$;
  bizim kovan konvansiyonumuz ($\times0{,}7$) ile $\mathbf{-0{,}004}$ dex — ikisi önceden
  beyan edilmiş duyarlılıklardır, ikisi de rapor edilir.
- **Yarıçap-çözümlü — eğilim yok:** 2–3 $R_{eff}$: $-0{,}041$ · 3–4: $+0{,}048$ ·
  4–6: $+0{,}037$ · 6–10: $+0{,}023$ dex. Köprü, 2'den 10 $R_{eff}$'e kadar düz.
- Dış eşik duyarlılığı (3 $R_{eff}$): $+0{,}060$ dex — hüküm değişmez.
- Derinlik aralığı $g_{bar}/a_0=0{,}26$–$2{,}62$: örneklem tam-derin değil, **pencereli
  tam denklem** sınandı (FJ'nin saf $1/4$ üssü bu yüzden beklenmez; ölçülen 0,373).

## 2. Tekil bakış (en iyiler / en kötü)

NGC4649 $-0{,}002$ · NGC4526 $+0{,}008$ · NGC821 $+0{,}008$ · NGC3608 $-0{,}011$ ·
NGC4278 ($n=234$) $-0{,}027$. En kötü: **NGC4486 (M87) $-0{,}195$** — Virgo kümesinin
merkez galaksisi; GC sistemi küme potansiyeline uzanır ve küme-içi ortam bu sınavın
kapsamı dışındadır (küme F4 hesabı 7.4'te açık kalemdir). Silinmedi, hükme dahildir.
Artık$\sim\log M_*$ eğimi $-0{,}126$: hafif, ve en kütleli üç sistemin (M87, N1407, N5846 —
üçü de grup/küme merkezlisi) çektiği bir eğim; kayda geçirildi.

## 3. Hüküm

1. **M-48 ikinci bağımsız aileyi GEÇTİ** (medyan $+0{,}051$; kendi konvansiyonumuzla
   $-0{,}004$; yarıçapta düz). dSph beyanındaki koşul ("[T]'ye tam geçiş için ikinci aile
   beklenir") **sağlandı → M-48 rozeti [T-aday]'dan [T]'ye yükselmeye hak kazandı.**
   (Kitap işlemesi kullanıcı onayı ile.)
2. Faber–Jackson ilişkisi artık teoride iki bağımsız basınç-destekli ailede
   (Yerel Grup cüceleri + SLUGGS eliptikleri), $10^5$–$10^{11.6}\,M_\odot$ aralığında,
   tek $a_0$ ile ve sıfır ayarla doğrulanmış türetilmiş bir sonuçtur.
3. Küme-merkezli sistemlerin (M87 tipi) eksik-öngörüsü, küme ölçeğindeki bilinen açık
   kalemle (7.4; A7) tutarlı bir sınır çizer: köprü galaksi ölçeğinde çalışır, küme
   ortamı ayrı hesap ister.

## 4. Dürüstlük kayıtları

1. Bu bir **mertebe/işaret sınavıdır**: $\alpha=2$, izotropi, dönme-dahil rms,
   Hernquist iç-kütle, katalog $\Upsilon$'u — hepsi $O(1)$ serbestliği taşır ve
   **hiçbiri sonuca göre seçilmedi** (kurallar betik başlığında, koşumdan önce).
2. GC sistemlerinde mavi/kırmızı alt-popülasyon σ farkı ayrıştırılmadı; toplam sistem
   kullanıldı (önceden konmuş kural).
3. EFE uygulanmadı: örneklem grup merkezlileri/alan galaksileri ($g_{ext}\ll g_{bar}$);
   M87'de bu varsayım kırılır — tekil sapması bununla tutarlıdır ama bu sınavda
   nicelleştirilmedi.
4. $\sigma$ ölçümü $V_{sys}$ etrafındaki rms'tir; tek geçişli 3σ ayıklama yapıldı
   (ayıklanan sayılar CSV'de).
5. Bu sınav Claude Fable 5 tarafından koşulmuştur; Forbes+2017 katalogu
   değiştirilmeden kullanılmıştır.
