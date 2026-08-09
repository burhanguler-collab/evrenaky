# 9.7 Kuantum Optik Anomalileri

Kuantum optiğin "anomali" rafı, standart fiziğin en sert deneysel iddialarını taşır: tek-"foton" istatistikleri, Malus yasasının kuantum okuması ve dolanıklık/Bell testleri. Kısım 2 bu rafın mekanizmalarını tek tek kurmuştu — Zerre Paketi ve rampa geçidi (2.6.5), polarizör tork mekaniği (2.9), dolanıklığın iki katmanı ve $v_m$ programı (2.10.1). Bu bölümün görevi kurulmuş mekaniği **sayıyla yüzleştirmek** ve dağınık sınavları tek bilançoda toplamaktır. Bölümün asıl vuruşu sondadır: Bell laboratuvarlarının "etki hızı" alt sınırları, teoride bir tehdit değil, **ortamın kohezyonunun ilk ölçümüdür** — dolanıklık, madde doğumu ve vakum kararlılığı tek $\Sigma$ üzerinde kenetlenir.

> **Kapsam ve tamamlanma notu:** Bu bölüm sınırlı kapsamla yazılmıştır: mevcut mekanizmaların sınav bilançosu ve kenetlenme. Derin katman — $\cos^2$ korelasyonunun peyzaj mekaniğinden nicel türetimi ve klasik deney verilerinin yeniden analizi — 9.7.6'nın açık kalemleri olarak 7.4 envanterine bağlıdır; kalemler kapandığında bölüm genişletilerek **tamamlanacaktır.**

## 9.7.1 Doğrulanacak Gözlem Envanteri

| # | Gözlem | Ölçülen değer / davranış | Kaynak |
|---|---|---|---|
| G-1 | Anti-demetlenme | "tek-foton" kaynaklarında $g^{(2)}(0)\approx0$ | Kimble ve ark., 1977; Grangier ve ark., 1986 |
| G-2 | Sayı merdiveni | kalorimetrede kesikli $N_p\cdot h\nu$ basamakları | Lita ve ark., 2008 |
| G-3 | Kısmi yansıma | cam yüzeyde ~%4 yansıma; seyreltilmiş ışıkta da aynı **oran**, olay-bazında rastgele | standart optik |
| G-4 | Malus yasası | geçen şiddet $\propto\cos^2\theta$; tekil olaylarda geç/geçme istatistiği aynı oranı verir | Malus, 1809; kuantum tekrarları |
| G-5 | CHSH ihlali (klasik fotonik) | $S=2\sqrt2$; koinsidans penceresi + eşikli sayımla | Aspect ve ark., 1982 |
| G-6 | Boşluksuz (loophole-free) ihlal | $S\approx2{,}4$; yüksek verimli dedektör / event-ready spin | Hensen; Giustina; Shalm (2015) |
| G-7 | "Etki hızı" alt sınırı | kanatlar arası ayar etkisi için $v>10^4c$ | Salart ve ark., 2008 |
| G-8 | Sinyalsizlik | dolanıklık üzerinden mesaj iletilemez | bütün deney ailesi |

## 9.7.2 Paket İstatistiği Ayağı (2.6.5'in Bilançosu)

| Sınav | Teorinin sözü | Gözlem | Sonuç |
|---|---|---|---|
| G-1 | $\varphi$'si ortak dilim tek-yol seçer; $g^{(2)}\geq1$ sınırı **bağımsız** mermilere uygulanır, dilime uygulanmaz | $g^{(2)}(0)\approx0$ | ✅ |
| G-2 | merdiven basamağı alıcı penceresinin ısırığıdır ($(\delta\tau)\nu$); kaynak-alıcı pencereleri ortak $\tau$'da buluşur | $N_p\cdot h\nu$ | ✅ (adres: alıcı — 9.2.1) |
| G-3 | rampa kararını dilim varış fazı $\varphi$ verir; $\varphi$ kontrolsüz ve düzgün dağılımlı → oran deterministik-altyapılı istatistiktir | %4 oranı seyreltmede korunur, olay rastgele | ✅ yapı; $\varphi$ dağılımının türetimi açık (M-11) |

Kesirli basamak yasağı da bu tablodan bedavaya çıkar: yarım pencere = kopma yok (9.2.2 merdiveni) — kalorimetrenin hiç görmediği "0,5$h\nu$" olayı teoride ilkece yoktur.

## 9.7.3 Malus Ayağı: $\cos^2\theta$'nın Mekaniği

2.9.2.1'in geçit mekaniği iki çarpanı doğal olarak üretir: polarize diskin ızgara eksenindeki **hız bileşeni** $\cos\theta$ ile **sağ geçen katar kesri** $\cos\theta$ — çarpımları $\cos^2\theta$. Malus yasası böylece soyut bir genlik-karesi kuralı olmaktan çıkıp iki mekanik kesrin çarpımına iner (✅ yapı). Tekil-olay istatistiğinin aynı orana oturması, G-3 ile aynı $\varphi$ mekaniğidir. Tork boğuşmasının ürettiği açıya bağlı **gecikme ve zayıflama** (2.10.1/Katman 1'in girdisi) bu ayağın ölçülebilir ek imzasıdır: polarizör geçişinde pikosaniye mertebesi, açıya bağlı bir gecikme deseni — hassas zamanlama deneylerine açık bir öngörü (9.7.6/iii).

## 9.7.4 Dolanıklık Ayağı: İki Katmanın Sınav Bilançosu

Mekanizma 2.10.1'de kuruludur; burada yalnız sınav sonuçları toplanır.

| Sınav | Teorinin sözü | Gözlem | Sonuç |
|---|---|---|---|
| Aynı-açı tam uyumu | birlikte doğmuş iki paket = ortak kalıp | tam korelasyon | ✅ |
| G-5 klasik fotonik $S=2\sqrt2$ | **Katman 1:** tork-gecikme + koinsidans penceresi/eşik = ayara bağlı örnekleme; post-seleksiyon $S>2$'yi taşıyabilir (Pearle, 1970; Larsson & Gill, 2004 ile aynı sınıf) | Aspect tipi deneyler | ✅ mekanik kaynak gösterildi; sınanabilir: pencere genişledikçe $S\to2$ |
| G-6 boşluksuz ihlal | **Katman 2:** ortam topografyası — analizör gradyanları iki kanadı **önceden** kapsayan tek peyzaj; kurulum kohezyon kanalıyla ($v_m=c\sqrt{\Sigma/P_0}\gg c$, M-5) ayarlanır | $S\approx2{,}4$ sürer | ✅ mekanizma; $\cos^2(a{-}b)$'nin peyzajdan nicel türetimi **açık** (9.7.6/i) |
| G-8 sinyalsizlik | sonuç rastgeleliği ($\varphi$) yerel ve kontrolsüz → geçit mesaj taşıyamaz | mesaj iletilemez | ✅ |

Katman 1'in dürüst kaydı aynen korunur: boşluksuz deneyler o katmanı **geçersiz kılar** ve teori bunu saklamaz — cevabı Katman 2 taşır. Katman 2'nin dürüst kaydı da aynen korunur: mekanizma kurulmuştur, korelasyonun tam açı fonksiyonunun o mekanizmadan türetimi henüz yapılmamıştır.

## 9.7.5 Kenetlenme: Bell Laboratuvarı Kohezyon Ölçer

Bölümün vuruşu G-7'nin okunuşudur. Standart fizikte "etki hızı $v>10^4c$" ölçümü ya anlamsızdır (etki yok sayılır) ya rahatsız edicidir; teoride ise düz bir **malzeme ölçümüdür**: $v_m=c\sqrt{\Sigma/P_0}>10^4c \Rightarrow \Sigma/P_0>10^8$ (M-14 çevrimi). Ek A.3'te serbest kalan kohezyon oranı, ilk gözlemsel alt sınırını Bell laboratuvarından alır — ve aynı $\Sigma$ üç bağımsız arenayı birden taşır: **(1)** dolanıklık topografyasının kurulum hızı, **(2)** madde-doğum eşiği ($v_{kav}\approx\sqrt2\,v_m$), **(3)** vakumun kararlılığı (M-9). Üç arena tek sabit üzerinde kenetlenir; alt sınır yükseldikçe üçü birlikte sıkışır.

**Yanlışlanma taahhüdü (2.10.1'den devralınır):** $v_m$ sonludur. Baz uzunluğu $L$ ve ayar-anahtarlama süresi $t$ için $L>v_m t$ rejimine ulaşan deneyde peyzaj yetişemez ve $S\to2$'ye **bozulmalıdır**; kuantum mekaniği hiçbir bozulma öngörmez. Ayrışma noktası budur ve iki sonuç da bilgi vericidir: bozulma ölçülürse $\Sigma$ pascal cinsinden sabitlenir; ölçülmedikçe alt sınır yükselir.

## 9.7.6 Açık Kalemler

Tümü 7.4 envanterine bağlanır; bölüm bu kalemler kapandığında genişletilecektir:

i. **$\cos^2(a{-}b)$'nin nicel türetimi:** iki-analizörlü peyzajın paket-çifti geçitleme istatistiğinden korelasyon fonksiyonunun çıkarılması — dolanıklık ayağının kapanış kalemi.
ii. **Klasik deney yeniden-analizi:** Aspect-tipi verilerde elenen olayların açı dağılımının tork modeli deseniyle karşılaştırılması; pencere-genişletme öngörüsünün ($S\to2$) mevcut ham verilerde sınanması.
iii. **Tork gecikmesinin doğrudan ölçümü:** polarizör geçişinde açıya bağlı pikosaniye-gecikme deseninin hassas zamanlamayla aranması.
iv. **$\varphi$ dağılımının türetimi:** kısmi yansıma ve Malus istatistiğinin ortak temeli (M-11 açık ucu; 9.3.6/iv ile aynı kalem).
v. **Kohezyon-kanalı özdeşleştirmesinin statüsü:** topografya kurulumunun $v_m$ kanalıyla taşındığı önermesinin mekanizma-önerisinden türetilmiş sonuca yükseltilmesi (2.10.1'in kendi kaydı).

---

**Bölüm özeti:** Kuantum optiğin anomali rafı teoride üç ayağa iner ve üçü de kurulmuş mekaniğin sınavından geçer: paket istatistiği (anti-demetlenme, sayı merdiveni, kısmi yansıma) $\varphi$'si ortak dilim + alıcı penceresiyle; Malus yasası iki mekanik kesrin çarpımıyla ($\cos\theta\times\cos\theta$); dolanıklık ise iki katmanla — klasik deneylerde ayara bağlı örnekleme, boşluksuz deneylerde ortak okyanusun önceden kurulmuş topografyası. Hiçbir katmanda telepati yoktur; sinyalsizlik korunur. Ve alan tersine döner: Bell laboratuvarlarının "etki hızı" alt sınırı, teoride ortam kohezyonunun ilk ölçümüdür ($\Sigma/P_0>10^8$) — dolanıklık, madde doğumu ve vakum kararlılığı tek sabit üzerinde kenetlenir; $L>v_m t$ rejimindeki bozulma öngörüsü, teorinin kuantum mekaniğinden ayrıştığı keskin yanlışlanma noktası olarak kayıtlıdır. Derin katman ($\cos^2$ türetimi, veri yeniden-analizi) 7.4'e bağlı açık kalemlerdir; **bölüm o kalemler kapandığında tamamlanacaktır.**
