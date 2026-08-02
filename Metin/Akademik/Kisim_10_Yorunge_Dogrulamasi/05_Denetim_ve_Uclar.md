# 10.5 Galaktik Doğrulama: Uç Sınıflar ve Karışık Sistemler

## 10.5.1 Karmaşık küme neden var — seçim etkisi denetimi

32 galaksi (örneklemin %18'i) dört dışlama ölçütünden en az birine takılarak sınıf dışı bırakılmıştır. Bu küme sessizce bir kenara konamaz; konursa seçim etkisi doğar. Sorulan soru "modeller bu kümede nasıl" değildir — **"dışlanan galaksiler hükmü değiştirir miydi?"** sorusudur.

Tip dağılımı: Im 12 · Sm 8 · BCD 5 · S0 3 · Sc 2 · Sab 1 · Sbc 1. Gerekçeler: $Q=3$ düşük kalite (12), eğiklik $i<30°$ (12), $N<6$ nokta (10), tipinde 5'ten az galaksi (8; örtüşmeler var).

<p style="margin:20px 0;padding:16px;border:1px solid #22c55e;border-radius:10px;background:rgba(34,197,94,0.07)"><a href="Simulasyon/kisim10/panel_99_KARMASIK.html" target="_blank" rel="noopener" style="display:inline-block;padding:12px 22px;background:#166534;color:#ffffff;border-radius:8px;font-weight:700;text-decoration:none;font-size:1.05em">&#9654;&#65039; ETKİLEŞİMLİ ANİMASYONU AÇ — Karmaşık küme (denetim) (32 galaksi)</a><br><span style="color:#a1a1aa;font-size:0.9em;display:inline-block;margin-top:8px">Tarayıcıda ayrı sayfada, tam ekran açılır. Galaksi galaksi gezinme (ok tuşları), &#9654; Oynat ile sıralı animasyon ve katman açma/kapatma düğmeleri sayfanın içindedir.</span></p>

![Karmaşık küme — öngörü mü, fit mi (32 galaksi)](Gorseller/k10_ongoru_99_KARMASIK.png)

| Ölçüt | Değer |
|---|---|
| Evrenakı öngörü RMS (medyan) | 19,00 km/s |
| ΛCDM öngörü RMS (medyan) | **18,27 km/s** |
| Dış yarı sapması | +2,5 % |
| Öngörü yarışı | 16/32 — tam beraberlik |

**Toplamda dışlama hükmü değiştirmiyor** (16/32 — tam beraberlik). Ama gerekçeye göre kırılım, ölçütlerin **yansız olmadığını** gösterir ve bu açıkça kaydedilir:

- **$Q=3$ dışlaması teorinin aleyhine işlemiştir:** o altkümede teori 9/12 kazanır ($+1{,}7\sigma$). Düşük kaliteli veri dışlanırken teorinin kazandığı bir altküme de dışlanmıştır.
- **Eğiklik dışlaması teorinin lehine işlemiştir:** $i<30°$ altkümesinde teori 5/12 ile hafif geridedir.

İki ölçüt de fiziksel gerekçeyle ve sonuç bilinmeden seçilmiştir ($Q=3$ SPARC'ın kendi bayrağıdır; yüz-üstü diskte $V=V_{los}/\sin i$ kötü belirlenir); denetim, ikisinin ters yönlerde çalışıp toplamda dengelendiğini göstermiştir. Ayrıca bu kümede fitlerin çok iyi çıkması ($\chi^2_{ind}\approx1$) bir başarı değil, dışlama gerekçesinin doğrulamasıdır: hata çubuğu büyük ve nokta sayısı az olduğunda iki parametreli her model kolayca uyar — bu galaksiler ayırt edici değildir.

## 10.5.2 Uçlar: S0 (mercek) ve BCD (mavi tıkız cüce)

Karmaşık kümenin içinden, tip sayısı 5'in altında kaldığı için sınıf açılamayan iki uç ayrıca okunmuştur: 3 S0 + 5 BCD. Bu sekiz galaksi örneklemin iki ucudur — S0'lar kovan baskın ve yüksek ivmeli, BCD'ler gaz baskın ve en düşük ivmeli. Yeni fit yapılmamıştır; tek yeni hesap, gereken $a_0$ çarpanının sayısal çözümüdür.

![S0 ve BCD — sekiz galaksi](Gorseller/k10_s0_bcd.png)

| Küme | n | Örneklem kalitesi | Medyan RMS (Evr.) | Gereken $a_0$ çarpanı |
|---|---|---|---|---|
| S0 | 3 | temiz (ikisi $Q=1$) | 34,9 km/s | **×2,61** |
| BCD | 5 | 4/5 kirli ($Q=3$ / $N=4$) | — | **×4,21** |

**Sonuç teorinin aleyhinedir ve yumuşatılmaz: uçlarda sınıf bandı genişler.** Ana altı sınıfın çarpan bandı ×0,63–1,47 iken S0 ×2,61, BCD ×4,21 ister. Üç kayıt yanında durmalıdır: (1) $n=3$ ve $n=5$ — hiçbiri tek başına hüküm taşımaz; (2) BCD'lerin beşte dördü SPARC'ın kendi düşük-kalite bayrağını taşır, ama temiz olan tek BCD (NGC2915) çarpanı **düşürmez, yükseltir** — temizlik BCD sonucunu kurtarmıyor; (3) S0 tarafı temizdir ve yine de ×2,61 ister — bu satır savunulamaz ve açık kalemdir.

Öngörü yarışı bu sekiz galakside 3/8'dir (fit yok, iki tarafta da sıfır serbest parametre).

## 10.5.3 Bu bölümün okunması

1. **Dışlama ölçütleri toplamda hükmü değiştirmemiştir** — ve iki ölçütün ters yönlü yanlılığı ölçülüp kayda geçmiştir. Program kendi eleğini de sınamıştır.
2. **Uçlar, sınıf bandının gerçek olduğunun en sert kanıtıdır:** band ana sınıflarda 0,115 dex iken uçlarla birlikte büyür. Bunun hangi kısmının ölçüm bütçesi, hangi kısmının fizik olduğu 10.8 ve 10.10'da ele alınır.
3. **Karmaşık kümenin sayıları model karşılaştırması olarak alıntılanmamalıdır** — bu galaksiler güvenilir sınav vermedikleri için dışlanmıştır; buradaki işlevleri denetimdir.
