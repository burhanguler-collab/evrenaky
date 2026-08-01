# KAYIT-ÖNCESİ PROTOKOL — λ–soğukluk sınavının $n\gtrsim40$ doğrulaması

**Bu dosya, hesap koşulmadan ÖNCE yazılmış ve kilitlenmiştir.** Aşağıdaki reçete tek seferde uygulanacak; kip, eşik ve istatistik sonuca bakılarak değiştirilmeyecektir. (Önceki iki turun ardışık-analiz çekincesini kaldırmanın tek yolu budur; SIGMA_SINAVI.md md. "sıradaki iş".)

## Hipotez (LAMBDA_TURETIM.md'den, veri görülmeden)

Gereken çarpan $k$ (pencere-içi konum $\lambda$'nın monoton vekili), diskin dinamik soğukluğu $v/\sigma$ ile **artar**: Spearman$[\log k,\ \log(v/\sigma)]>0$.

## Veri ve örneklem (önceden ilan)

- $\sigma$ tahmini: Lelli ve ark. 2019 BTFR kataloğunun (`veri/_BTFR_Lelli2019.mrt` — diskte, bu sınav için hiç kullanılmamış kolonlar) çizgi genişliklerinden, Gauss-kenar bağıntısıyla:
  $$\sigma_{est}=\frac{W_{P20}-W_{M50}}{2\left(\sqrt{2\ln5}-\sqrt{2\ln2}\right)}=\frac{W_{P20}-W_{M50}}{1{,}2334}$$
  (Kenar yumuşaması izotropiktir; $\sin i$ düzeltmesi gerekmez. Spearman sıra-tabanlı olduğundan sabitin değeri sonucu etkilemez; yalnız monotonluk gerekir.)
- $v$: dönüş eğrisinin dış-yarı medyan hızı (rotmod, SPARC; v2 ile aynı tanım).
- $k$: dış-yarı sapmasını sıfırlayan çarpan, sayısal çözüm (85'in tanımı), yalnız `ok` çözümler.
- Dahil olma koşulları: $W_{P20}>0$, $W_{M50}>0$, $W_{P20}-W_{M50}\geq5$ km/s (altı gürültü-baskın).
- **Birincil örneklem:** altı ana morfolojik sınıfın üyeleri. **İkincil (ayrı satır, karara girmez):** S0/BCD uçları ve 99 üyeleri.

## İstatistik ve karar kuralı (önceden ilan)

- TEK istatistik: Spearman$[\log k,\ \log(v/\sigma_{est})]$, birincil örneklemde.
- $p$: tek yönlü permütasyon, 20.000 permütasyon, tohum 42.
- **Karar:** $p<0{,}05$ → işaret bu veri türünde doğrulanmış sayılır; $p\geq0{,}05$ → desteklenmemiş sayılır ve öyle yazılır.

## Geçerlilik kapısı (karara girmez, sınavı açar/kapar)

$\sigma_{est}$'in işe yaraması için doğrudan ölçümle monoton olması gerekir: SIGMA_SINAVI'nın 18 doğrudan-$\sigma$ galaksisiyle örtüşen altkümede Spearman$[\sigma_{est},\sigma_{doğrudan}]\geq0{,}4$ olmalıdır. Altında kalırsa sınav **"uygulanamaz"** ilan edilir (desteklenmedi DEĞİL) ve sonuç raporlanmaz.

## Bilinen sınırlar (önceden kabul)

1. $W_{P20}$ tepe akının, $W_{M50}$ ortalama akının yüzdesidir (Lelli+2019'un tanımları) — karışık tanım $\sigma_{est}$'e galaksi-profiline bağlı sistematik katar; geçerlilik kapısı bunun için vardır.
2. Çift-boynuz/tek-tepe profil farkı ve $e_W$ gürültüsü saçılma katar; bunlar $p$'yi zayıflatır, sahte pozitif üretmez (permütasyon altında).
3. $k$ ile $\sigma_{est}$ tümüyle bağımsız ölçümlerdir (dönüş eğrisi vs entegre çizgi profili); dairesellik yoktur.

*Protokol tarihi: 1 Ağustos 2026. Yazan: Claude Fable 5 (yazar onayıyla koşulacak). Bu satırın altına sonuç, hesap koşulduktan sonra tek sefer eklenecektir.*

---

## SONUÇ (tek sefer, 1 Ağustos 2026 — `kayit_oncesi_vsigma.py`)

**Geçerlilik kapısı GEÇİLEMEDİ → sınav UYGULANAMAZ.**

- Örneklem kuruldu: birincil $n=99$ (altı ana sınıf; $k$ çözümü + $W$ koşulları), ikincil $n=2$.
- Kapı ölçümü: Spearman$[\sigma_{est},\sigma_{doğrudan}]=\mathbf{-0{,}500}$ ($n=8$ örtüşme; eşik $\geq+0{,}4$).
- Teşhis: $W_{P20}$ (tepe akının %20'si) ile $W_{M50}$ (ortalama akının %50'si) **farklı normalizasyon** taşır; farkları kenar yumuşamasını (türbülansı) değil profil biçimini (çift-boynuz derinliğini) izliyor. Gauss-kenar bağıntısı bu tanım çiftine uygulanamaz.
- Protokol gereği birincil istatistik **raporlanmaz** (hesaplanmış olsa da karar değeri yoktur); hüküm "desteklenmedi" DEĞİL, "**bu σ kaynağıyla sınanamaz**"dır.

**Kazanç:** (i) kayıt-öncesi kip ilk uygulamasında işledi — geçersiz bir kestiricinin sonucu (hangi yönde çıkarsa çıksın) literatüre/kitaba sızmadı; (ii) altyapı hazır: 99 galaksilik $k$ + eşleşme boru hattı duruyor, geçerli bir $\sigma$ kaynağı takıldığı anda sınav aynı protokolle koşulur. Geçerli kaynak adayları: MHONGOOSE/Apertif ikinci-moment kataloğu, THINGS-türü süper-profil ölçümlerinin genişletilmesi, ya da kenardan-görünüm kalınlık katalogları (σ yerine doğrudan incelik).
