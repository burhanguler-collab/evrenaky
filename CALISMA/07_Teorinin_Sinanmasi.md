# 6.6 Teorinin Sınanması: Sınavlar ve Sonuçları

## 6.6.1 Bu Bölüm Neden Ayrı Duruyor

Kitabın buraya kadarki bölümleri üç ayrı işi yapar ve üçü de sınav **değildir**:

| İş | Ne yapar | Örnek |
|---|---|---|
| **Türetim** | Teorinin kendi içinden bir sonuç çıkarır | Ek M kataloğunun tamamı |
| **Tutarlılık denetimi** | Girdi olarak konan bir şeyin çıktıda göründüğünü gösterir | Kepler'in siklostrofik dengeye konması (M-30, Adım 3) |
| **Retrodiksiyon** | Yerleşik bir gözlemin sayısını yeniden üretir | Işık bükülmesi 1,7512″; GP-B 41,0 mas/yıl |

Retrodiksiyon değerlidir — teorinin bilinen fiziği kapsadığını gösterir — ama **ayırt edici değildir**, çünkü hedef sayı zaten bilinerek çalışılır. Bir sonucun sınav sayılması için üç koşul birlikte gerekir:

1. **Öngörü, veriye bakılmadan önce yapılmış olmalı.**
2. **Veri bağımsız ve yayımlanmış olmalı** — teorinin kendi deney programından değil.
3. **Teoriyi yanlışlayacak bir çıktı mümkün olmalı.** Hiçbir sonucun teoriyi zora sokmadığı bir hesap sınav değildir.

Bu bölüm yalnızca bu üç koşulu sağlayan hesapları taşır. Sonuçlar teorinin lehine çıkabilir, aleyhine çıkabilir, ya da — birinci sınavda görüleceği gibi — **sınavın kendisinin geçersiz olduğunu** gösterebilir. Üçü de kaydedilir.

---

## 6.6.2 Sınav 1 — Gezegen Figürü: Dört Terimli Denge

### Sınavın kurulumu

Bir gezegenin şekli, dönmeyle ilişkili **dört** katkının dengesidir; teoride ikisi şişmeye karşı, ikisi şişme yönünde çalışır:

| Şişmeye karşı | Şişme yönünde |
|---|---|
| **F1** Radyal kütle-itim (Ek M-35) | **Merkezkaç** |
| **F4** Eksenel itim, eksene doğru (Ek M-38) | **F5** Yanal itim, ekvator düzlemine (Ek M-39) |

Teori merkezkaçı reddetmez; onu olduğu gibi kabul eder ve üzerine iki hidrodinamik terim ekler.

**F1 ayrı bir terim değildir.** Radyal kütle-itim, teoride Newton çekimiyle **sayısal olarak özdeştir** ($G=\alpha/\rho_n$, Ek M-28). Hidrostatik figür hesabı zaten merkezkaçı çekime karşı dengeler; F1'i ayrıca eklemek onu iki kez saymak olurdu. Dolayısıyla sınavda karşılaştırılan üç şey vardır: merkezkaç (referans), **F4** ve **F5**.

$$f_{yanal}(\theta) = -\frac{\kappa_5\,\rho_0\,v_e^{2}}{r}\,\sin 2\theta\,,\qquad v_e=\phi\,\omega R \qquad\qquad a_{eksenel}=-\frac{A_4}{R}$$

Gezegen basıklıkları çok yüksek hassasiyetle ölçülmüştür (uydu jeodezisi, Juno, Cassini). Sınav doğaldır: teorinin eklediği iki terimin **net** etkisi, ölçülen basıklığın hidrostatik açıklamasının içine sığmak zorundadır.

> *Kayıt: bu bölümün ilk sürümü yalnız F5'i hesaba katıyor, F4'ü atlıyordu. Eksenel itimin ekvator bölgesini eksene doğru baskıladığı ve dolayısıyla şişmeye **karşı** çalıştığı, yazar tarafından işaret edilmiştir. Aşağıdaki analiz bu dört terimli haliyle yeniden kurulmuştur ve sonucu iki noktada değiştirmiştir.*

### Anahtar: her terimin multipol içeriği

Figür sınavının tamamı buna dayanır. Jeodezi konvansiyonunu kullanıyoruz ($\vec a=+\nabla\Phi$; dış potansiyel $V=\frac{GM}{r}\left[1-\sum J_nP_n\right]$; basık cisim $\Rightarrow J_2>0$), $\mu=\sin\theta$.

**Merkezkaç.** $\Phi_{cf}=\tfrac12\omega^2r^2(1-\mu^2)$ ve $(1-\mu^2)=\tfrac23-\tfrac23P_2$:
$$\Phi_{cf}=\text{sabit}-\tfrac13\omega^2r^2\,P_2 \qquad \textbf{saf }P_2,\ \text{katsayı negatif}$$

**Yanal itim (F5).** $a_\theta=-A_5\sin2\theta/r$ ⟹ $\Phi_5=-\tfrac{A_5}{2}\cos2\theta$, ve $\cos2\theta=1-2\mu^2$:
$$\Phi_5=\text{sabit}-\tfrac{2A_5}{3}\,P_2 \qquad \textbf{saf }P_2,\ \text{katsayı negatif}$$

**Eksenel itim (F4).** $a_R=-A_4/R$ ⟹ $\Phi_4=-A_4\ln R=-A_4\ln r-A_4\ln\cos\theta$. Açısal kısım $\int_{-1}^{1}\ln(1-\mu^2)P_n\,d\mu=-\frac{4}{n(n+1)}$ (çift $n$) ile açılır:
$$\Phi_4=\text{radyal}+A_4\left[0{,}833\,P_2+0{,}450\,P_4+0{,}309\,P_6+\cdots\right] \qquad \textbf{zengin spektrum, katsayılar pozitif}$$

Tablo halinde:

| Katkı | $P_2$ | $P_4$ | $P_6$ | İşaret |
|---|---|---|---|---|
| Merkezkaç | $-\tfrac13\omega^2r^2$ | **0** | **0** | şişirir |
| Yanal (F5) | $-\tfrac23A_5$ | **0** | **0** | şişirir |
| **Eksenel (F4)** | $+0{,}833A_4$ | $+0{,}450A_4$ | $+0{,}309A_4$ | **baskılar** |

İşaret kuralı merkezkaçtan kalibre edilir: merkezkaç negatif $P_2$ taşır ve basıklık (pozitif $J_2$) üretir, dolayısıyla **negatif $P_n$ katsayısı → pozitif $J_n$.** Buna göre F4'ün pozitif $P_2$'si $J_2$'yi **azaltır** — yani şişmeye karşı çalışır ✓ — ve pozitif $P_4$'ü **negatif** bir $J_4$ katkısı verir.

**İki sonuç doğar ve ikisi de sınavın yönünü belirler:**

1. **Merkezkaç ve yanal itim ayırt edilemez.** İkisi de saf $P_2$; dahası gövde içinde ortam kafesle taşındığından $v_e=\phi\omega r$, yani $A_5\propto r^2$ — radyal bağımlılık da özdeş. F5, merkezkaç potansiyelinin sabit çarpanla yeniden ölçeklenmesine matematiksel olarak denktir.
2. **Eksenel itim ayırt edilebilir.** Yalnız o $P_4$ ve $P_6$ üretir. Ve kritik nokta: **merkezkaç $J_4$'e birinci mertebede hiç katkı vermez** — hidrostatik $J_4$, merkezkaçın *ikinci* mertebe tepkisidir ($O(q^2)$). F4 ise $P_4$'ü birinci mertebede doğurur. Zayıf bir kuvvet, boş bir kanalda görünür hale gelir.

### F5 için: $J_4$'te imza yoktur

Yukarıdaki tabloya göre yanal itim ile merkezkaç, hem açısal ($P_2$) hem radyal ($\propto r^2$) yapıda özdeştir. Oranları sabittir:

$$\boxed{\;\frac{\Phi_{yanal}}{\Phi_{merkezkaç}} = 2\,\kappa_5\left(\frac{\rho_0}{\rho_n}\right)\phi^{2}\;}$$

Yani F5, gezegeni *farklı bir şekle* sokmaz; gezegeni **biraz daha hızlı dönüyormuş gibi** yapar. Hiçbir kütleçekim harmoniği ikisini ayırt edemez.

> **Buradaki ders geneldir:** kuvvetlerin yön ve şiddet profillerinin farklı *görünmesi*, potansiyellerinin farklı multipol içerdiği anlamına gelmez. İlk tasarım imzayı $J_4$'te arıyordu; gerekçesi "profiller farklı" idi ve **yanlıştı.** Multipol ayrıştırması zorunludur — nitekim aynı ayrıştırma, imzanın **başka bir kuvvette** (F4) gerçekten var olduğunu da göstermiştir (aşağıda).

### F5 için sınavın çalışan biçimi: $\omega$ bağımsız ölçülüyor

Dejenerelik sınavı öldürmez, çünkü **dönme hızı bağımsız olarak biliniyor.** Gezegenin ölçülen $\omega$'sıyla hesaplanan hidrostatik basıklık ile gözlenen basıklık karşılaştırılabilir; teori aradaki farkta görünmek zorundadır:

$$\frac{f_{gözlenen}}{f_{hidrostatik}(\omega_{ölçülen})} = 1 + 2\kappa_5\left(\frac{\rho_0}{\rho_n}\right)\phi^{2} - (\text{F4 payı})$$

### Veri ve sonuç — Dünya

| Büyüklük | Değer | Kaynak |
|---|---|---|
| Gözlenen basıklık | $f=1/298{,}257=3{,}3528\times10^{-3}$ | WGS-84 / uydu jeodezisi |
| Hidrostatik basıklık | $f_h\approx1/299{,}5=3{,}3389\times10^{-3}$ | Figür teorisi + sismik yoğunluk profili |
| **Hidrostatik-olmayan fazla** | **%0,42** | manto dinamiği + buzul geri sıçraması ile açıklanır |

Teorinin katkısı bu fazlanın **tamamını** alsa dahi (en cömert varsayım):

$$2\kappa_5\left(\frac{\rho_0}{\rho_n}\right)\phi^{2}\le0{,}0042$$

$\phi_\oplus\approx0{,}6$ ($\phi^2=0{,}36$) ve $\rho_0/\rho_n=\tfrac{1-k}{4}=\tfrac14$ ($k=0$; Sınav 4'te sabitlendi) ile:

$$\boxed{\;\kappa_5\lesssim0{,}023\;}$$

> *Kayıt: bu sınırın ilk sürümü $\rho_0/\rho_n=\tfrac18$ ($k=\tfrac12$) kullanıp $\kappa_5\lesssim0{,}05$ veriyordu. **Sınav 4** $k=\tfrac12$'yi yanlışlayıp $k=0$'ı sabitledi; sınır iki buçuk kat sıkıldı. Sınav 1 ile Sınav 4'ün bu bağımlılığı, sınavların birbirinden bağımsız olmadığının kaydıdır.*

### F4 ne kadar götürüyor? — $r_0$ yeni varsayım gerektirmeden çıkıyor

F4 zıt yönde çalıştığı için yukarıdaki sınır ancak F4'ün payı bilinirse $\kappa_5$'e ait olur. F4'ün genliği $A_4$'e, o da rejim geçiş yarıçapı $r_0$'a bağlıdır.

> **GÜNCELLEME (3 Ağustos 2026) — $r_0$ artık türetilmiştir.** Bu paragrafın yazıldığı sırada $r_0$ serbest sayılıyordu. Ek M-38'de iki kanalın ivmesinin kesişiminden kapalı biçimde çıktı: $r_0=\sqrt{\mathcal{G}M/a_0}=\ell_\omega^{etkin}$, dolayısıyla $A_4=\sqrt{\mathcal{G}Ma_0}$. Dünya için $A_4=174{,}8$ m²/s² — aşağıda kalibre edilen 20,7 üst sınırının **8,4 katı.** Bu çelişki iki şeyi birden söylüyor: **(a)** aşağıdaki Ay-tabanlı kalibrasyon rejim tutarsızlığı taşıyor (kendi sonucu $r_0>128$ AU, oysa dış rejim yasasını Ay'da kullanıyor); **(b)** daha önemlisi, türetilmiş $A_4$ ile Ay'ın apsidal presesyonunda %1'lik modellenmemiş bir terim doğuyor ve bu **kesin olarak dışlanır** — yani F4 gezegen ölçeğinde işlemiyor. Çıkış M-38'in kendi Varsayım 3'üdür: $1/R$ yasası $h=$ sabit, yani **dönen bir disk** ister; yalıtılmış gezegen/uydu sisteminde akı küreseldir ve F4'ün $1/R$ rejimi yoktur. Bu, teorinin ilan edilmiş geçerlilik alanıyla birebir örtüşür (10.6.3 kapsam kaydı). **Sonuç: aşağıdaki F4 payı hesabı gezegen figürü için geçersizdir — F4'ün payı sıfırdır, dolayısıyla $\kappa_5\lesssim0{,}023$ sınırı fiilen $\kappa_5$'e aittir ve bu tarafta güçlenir.**

**Ama sabitlenmesine gerek yok: mevcut bir tutarlılık koşulu onu zaten bağlıyor.** Ek M-38'in Ay sınırı, eksenel payın radyal paya oranını ölçer ve bu oran yarıçapla **doğrusaldır**:

$$\varepsilon(r)=\frac{a_{1/R}}{a_{1/R^2}}=\frac{A_4\,r}{GM} \qquad\Longrightarrow\qquad \varepsilon_{Ay}<2\times10^{-5}\;\Rightarrow\; r_0>1{,}9\times10^{13}\ \text{m}\approx\textbf{128 AU}$$

Yani eksenel akı tüpünün iç kesimi gezegen ölçeğinin çok dışındadır. Dünya yüzeyinde:

$$\varepsilon_{yüzey}<3{,}3\times10^{-7} \qquad\text{(karşılaştırma: merkezkaç/}g=3{,}45\times10^{-3})$$

$A_4=\varepsilon_{yüzey}\,g\,R_\oplus\approx20{,}7$ m²/s². Buradan $P_2$ katkıları:

| | $P_2$ katsayısı | Merkezkaça oranı |
|---|---|---|
| Merkezkaç | $7{,}19\times10^{4}$ m²/s² | 1 |
| Eksenel (F4) | $1{,}73\times10^{1}$ m²/s² | $2{,}4\times10^{-4}$ |

**F4, F5'i götürecek güçte değildir — dört mertebe yetersiz.** Dolayısıyla yukarıdaki sınır fiilen $\kappa_5$'e aittir ve ayakta kalır:

$$\boxed{\;\kappa_5\lesssim0{,}023\;}\qquad(k=0\text{, Sınav 4})$$

### Sonuç 1: $\kappa_5$ elendi, F5 gözlemsel içerikten yoksun

**Teori yanlışlanmadı, ama çalışma değeri elendi.** $\kappa_5$ Ek C'de baştan beri serbest kalemdi ($[F]$) ve $\kappa_5=\tfrac12$ yalnızca "Bernoulli biçimini veren" bir çalışma seçimiydi. Sınav bu seçimin **yirmi kattan fazla** olduğunu gösteriyor ($0{,}5/0{,}023=21{,}4$): dönüşüm, tam Bernoulli'nin en fazla **%5'i** kadar verimli. *(Düzeltme, 3 Ağustos 2026: bu cümle \"on kat / %10\" diyordu; o oran bir önceki sürümün $\rho_0/\rho_n=\tfrac18$ sınırına ($0{,}047$) aitti ve sınır $0{,}023$'e sıkışınca güncellenmemişti.)*

**Ama tek yönlü bir rahatlık değil.** Dünya'nın %0,42'lik fazlası jeofizikte bağımsız modellenmiştir. O açıklama fazlanın tamamını hesaba katarsa teorinin payı sıfıra iner. Dahası F5 saf $P_2$ olduğu için hiçbir harmonikte ayrı imzası yoktur. **Sonuç: yanal itim, gezegen figüründe ölçülebilir bir etki bırakmıyor** — çürütülmedi, *görünmez*. Bir kuvvetin çürütülmesi ile gözlemsel içeriğinin olmaması farklı şeylerdir; ikincisi daha rahatsız edicidir, çünkü kuvvet olsa da olmasa da hiçbir ölçüm değişmez.

### Sonuç 2: $J_4$ kanalı açık — ama F5 için değil, F4 için

F4, yüzeyde merkezkaçtan $10^4$ kat zayıftır; ama **merkezkaç $J_4$'e birinci mertebede hiç katkı vermez**, F4 verir. Boş kanalda zayıf kuvvet görünür hale gelir:

| | Değer |
|---|---|
| F4'ün $P_4$ katsayısı | $0{,}450\,A_4 = 9{,}3$ m²/s² |
| $GM/R_\oplus$ ile normalize | $1{,}49\times10^{-7}$ |
| Tepki çarpanı $k_4$ (merkezkaçtan kalibre: $k_2\approx0{,}94$) | $0{,}4$–$0{,}9$ |
| **İndüklenen $J_4$** | $(0{,}6\text{–}1{,}3)\times10^{-7}$ |
| Dünya'nın ölçülen $J_4$'ü | $-1{,}62\times10^{-6}$ |
| **Oran** | **%4–8** |

**İşaret kontrolü (yapıldı).** Konvansiyon merkezkaçtan kalibre edilir: merkezkaç $P_2$ katsayısı **negatif** ve basıklık (pozitif $J_2$) üretir ⟹ *negatif $P_n$ katsayısı → pozitif $J_n$*. F4'ün $P_4$ katsayısı **pozitiftir**, dolayısıyla katkısı **negatif $J_4$**'tür. Dünya'nın ölçülen $J_4$'ü de negatiftir ($-1{,}62\times10^{-6}$): **F4 aynı yönde çalışıyor, $J_4$'ü derinleştiriyor.**

Bu anlamlıdır, çünkü hidrostatik modellerin verdiği $|J_4|$ gözlenenden **küçüktür** — yani gözlem hidrostatikten daha derindir ve F4'ün katkısı tam o yönde.

### Sonuç 2'nin dürüst sınırı: sinyal gürültünün içinde

Yine de bunu "uyum" olarak kaydetmiyoruz, iki nedenle:

- **Hidrostatik referansın kendisi ~%10 belirsiz.** $J_4$'ün hidrostatik değeri iç yoğunluk profiline ve figür teorisinin mertebesine bağlıdır; bu belirsizlik aranan %4–8'lik sinyalle aynı mertebededir.
- **Hidrostatik-olmayan manto yapısı da $J_4$'e katkı verir** ve F4'ten ayrıştırılmamıştır.

**Sınav 1'in toplu sonucu:** F5 için olumsuz (gözlemsel içerik yok, $\kappa_5$ on kat sıkıştı); F4 için **açık ve doğru işaretli bir kanal var**, ama mevcut hassasiyet onu ne doğruluyor ne dışlıyor. Bu, sınav programının **olumsuz olmayan ilk sonucudur** — geçilmiş bir sınav değil, ama "teorinin öngörüsü, önemli olacak büyüklükte" durumu.

**Sınavı kesinleştirecek iş:** Dünya, Jüpiter ve Satürn için hidrostatik $J_4$ referanslarının %1 düzeyinde belirlenmesi. Üç cisim tek bir $A_4$ ölçeklemesiyle ($\varepsilon\propto r$, yani $A_4\propto GM/r_0$) uyuşmalıdır — serbest parametresi olmayan bir çapraz sınav.

### Dört Cisim Sınavı: Kompozisyon Ekseni ($\phi$)

Ek M-39'un en ilgi çekici yapısal öngörüsü buradadır ve kaydedilmeye değer. Yanal itimin figüre katkısı **cismin kompozisyonuna** bağlıdır: deplasman kesri $\phi$ bağlı kafes gerektirir, dolayısıyla iyonize plazmada çöker.

$$\frac{\Delta J_2}{J_2}\;=\;2\kappa_5\left(\frac{\rho_0}{\rho_n}\right)\phi^{2}\,,\qquad \frac{\rho_0}{\rho_n}=\frac14\ (k=0)$$

$\kappa_5$ **evrenseldir**, $\phi$ cisme özgüdür. Sınanabilir içerik budur: cisimler arası fazlalık oranı $\phi^2$ gibi ölçeklenmelidir. Beklenen sıralama:

$$\phi_{\text{plazma}}\;\lll\;\phi_{\text{kayaç}}\;\sim\;\phi_{\text{moleküler}}$$

Satürn'ün Jüpiter'den yüksek olması da beklenir: düşük basınç nedeniyle moleküler (bağlı) bölgesi daha kalındır. Öngörü nitel olarak nettir ve önemsiz değildir.

### Ama önce iki kısıt: $\kappa_5$ ile $\phi$ dejenere, Dünya ise kalibrasyon

**(i) Yalnız çarpım bağlanıyor.** Dünya'nın %0,42'lik fazlası tek bir kombinasyon verir:

$$\kappa_5\,\phi^2 \;\le\; 0{,}0084$$

Bu çarpımı iki farklı biçimde bölmek mümkündür ve **ikisi de aynı kısıttır**, ikisi de "belirlenmiş değer" değildir:

| $\phi_\oplus$ varsayımı | Gereken $\kappa_5$ | Dayanağı |
|---|---|---|
| 0,61 ($n_{kayaç}\approx1{,}6$, M-15'in $\phi=1-1/n^2$ bağıntısı) | 0,02 | teorinin kendi bağıntısı |
| 0,18 | 0,26 | — |

İkinci satır **teorinin kendi bağıntısıyla çelişir**: $\phi=0{,}18$ için $n=1{,}10$ gerekir, ki bu bir **gaz** kırılma indisidir. Kayaç $n\approx1{,}6$ ile $\phi=0{,}61$, su ise $n=1{,}33$ ile $\phi=0{,}44$ verir — yani kayaç sudan **daha fazla** deplase eder, daha az değil. Metalik fazlar da daha az değil daha çok beklenir. Dolayısıyla teorinin iç tutarlılığı $\phi_\oplus\approx0{,}6$ ve $\kappa_5\lesssim0{,}023$ tarafındadır; ama vurgulanmalı ki **bu bir ölçüm değil, bir tercih**: gözlem yalnız çarpımı bağlar.

**(ii) Dünya bir sınav değildir.** Ölçek Dünya'dan kuruluyor; aynı cismi sonra "uyum" diye saymak döngüseldir. Tek evrensel $\kappa_5$ ve cisme özgü $\phi$ ile $N$ cisim en fazla $N-1$ bağımsız ilişki sınar.

### Dört cismin gerçek durumu

Sınavın kurulabilmesi için cismin **bağımsız** bir hidrostatik referansı olmalı — yani $J_2$'nin hidrostatik değeri, sınanan gravite alanından *bağımsız* bilinmeli. Dört cisim bu ölçüte göre ayrışır:

| Cisim | $\phi$ | Bağımsız hidrostatik referans | Öngörülen sinyal ↔ hassasiyet | Sınav kurulabilir mi? |
|---|---|---|---|---|
| **Dünya** | ~0,6 (kayaç) | **Var** — sismik yoğunluk profili, $f_h$ ~%0,1–0,2 belirsiz | %0,42 sinyal, S/N ≈ 2–4 | **Kalibrasyon** (sınav değil) |
| **Güneş** | ~0 (iyonize) | Kısmen (helyosismoloji) | $J_2=2{,}2\times10^{-7}$, ölçüm ~%3–10 belirsiz; sinyal ≤%0,42 ⟹ **S/N ≈ 0,04–0,14** | **Hayır** — hassasiyet 7–25 kat yetersiz |
| **Jüpiter** | ~0,5–0,6 | **Yok** — iç yoğunluk profili $J_2,J_4,J_6$'ya *fit edilerek* bulunur | — | **Hayır** — döngüsel |
| **Satürn** | ~0,6–0,7 | **Yok** — aynı | — | **Hayır** — döngüsel |

Üç satır ayrıca açıklama gerektirir:

- **Güneş'in null sonucu $\phi_{Güneş}\approx0$'ı desteklemiyor.** Hesap açıktır: $\phi_{Güneş}$ Dünya'nınki kadar *büyük* olsaydı bile öngörülen etki ($9\times10^{-10}$) solar $J_2$'nin ölçüm belirsizliğinin ($\sim10^{-8}$) bir mertebe altında kalırdı ve **görünmezdi**. Yani Güneş bu kanalda $\phi$ hakkında hiçbir şey söylemiyor — ne lehte ne aleyhte.
- **Jüpiter'in Juno sapmaları gerçektir ama açıklanmıştır.** Katı-cisim hidrostatik dengesi tutmuyor; tek harmoniklerin sıfırdan farklı olması ($J_3,J_5,J_7\neq0$) **yüzeyde doğrudan gözlenen diferansiyel dönmeye** ve ~3000 km derinliğe inen zonal rüzgârlara bağlanmıştır (Kaspi ve ark., 2018). Standart fizik bunu açıklıyor; teorinin arayacağı fazla, aynı mertebede ve **ayrıştırılmamıştır**.
- **Satürn'ün %10 basıklığı anomali değildir.** $q_{Satürn}=0{,}155$ ile $f/q=0{,}63$ çıkar; merkezî yoğunlaşması olan bir cisim için tamamen normaldir. Cassini'nin halka dalgalarında saptadığı yapılar ise Satürn'ün **iç salınım modlarıdır** (f-modları) ve ~9000 km derin rüzgârlar — statik bir ek kuvvet değil, farklı bir olgu.

### NET SONUÇ

$$\boxed{\;\text{Kompozisyon ekseni, gezegen figürü kanalında şu an } \textbf{yanlışlanamaz} \text{ durumdadır.}\;}$$

Dört cismin muhasebesi: **bir kalibrasyon** (Dünya), **bir hassasiyet yetersizliği** (Güneş), **iki döngüsellik** (Jüpiter, Satürn). Bağımsız kısıt sayısı **sıfır**.

Bunun üç somut sonucu vardır:

1. **$\kappa_5$ ve $\phi$ ayrı ayrı alıntılanamaz.** Yalnız $\kappa_5\phi^2\le0{,}0084$ bağlıdır. Teorinin iç bağıntısı $\phi_\oplus\approx0{,}6$'yı destekler ($\Rightarrow\kappa_5\lesssim0{,}023$), ama bu gözlemden değil M-15'ten gelir.
2. **Sıralama öngörüsü (plazma ≪ yoğun madde) bir *öngörü* olarak durur, *sonuç* değil.** Gözlenen anomali sıralamasıyla uyumlu olması dikkate değer, ama gaz devlerinin sapmalarının bağımsız açıklaması olduğu için kanıt sayılamaz.
3. **Bu bulgu Sonuç 1'i pekiştiriyor:** yanal itimin gezegen figüründe ölçülebilir imzası yok. Kompozisyon ekseni bir kaçış yolu olabilirdi; hesap yapılınca o da kapalı çıktı.

**Kompozisyon ekseni nerede sınanabilir?** Figür kanalında değil. Yanal itim saf $P_2$ olduğu ve $\phi$ yalnız genliği ölçeklediği için, ayırt edicilik ancak **bağımsız hidrostatik referansı olan ikinci bir hızlı-dönen cisim** bulunmasıyla gelir. Adaylar zayıftır: Mars'ta sismoloji var (InSight) ama figürü Tharsis kabarması domine ediyor; Ay'ın şekli fosildir, hidrostatik değil. Dolayısıyla bu eksen, yeni bir gözlemsel kanal bulunana kadar **program dışıdır**.

*(Kayıt: bu bölümün bir taslağı dört cismi "✅ Tam Uyum / Destekliyor" olarak işaretliyor ve sonucu "teorinin en net kanıtlarından biri" diye sunuyordu. Yukarıdaki hesaplar bunu taşımıyor: Dünya kalibrasyondur, Güneş'in hassasiyeti yetersizdir, gaz devlerinin referansı döngüseldir, ve $\phi_\oplus=0{,}18$ değeri teorinin kendi $\phi=1-1/n^2$ bağıntısıyla çelişir. Taslağın doğru kurulmuş tek parçası, yanlışlama yapısının kendisidir — "Güneş ölçülebilir bir anomali taşısaydı M-39 çökerdi" — ve o yapı korunmuştur; yalnız Güneş'in bu eşiği ölçemediği eklenmiştir. Bölüm 6.6.1'in üçüncü koşulu gereği, yanlışlayacak çıktının **erişilebilir** olması da gerekir.)*

---

## 6.6.3 Sınav 2 — Yayılan Disk ve Düz Dönüş Eğrisi

Bu, teorinin karanlık madde alternatifinin en doğrudan sınavıdır.

### Sınavın kurulumu

Düz dönüş eğrisi teoride şu zincirden çıkar (**Ek M-38** + **Ek M-37**):

$$\underbrace{h=\text{sabit}}_{\text{akı tüpü kalınlığı}}\;\Rightarrow\;\underbrace{a\propto\frac{1}{R}}_{\text{silindirik akı}}\;\Rightarrow\;\underbrace{v_\theta=\sqrt{R|a|}=\text{sabit}}_{\text{profil teoremi}}$$

Zincirin ilk halkası bir varsayımdır ve **sınanabilir bir sonucu vardır**: $h$ sabit değilse akı korunumu $a\propto1/(R\,h(R))$ verir, dolayısıyla

$$\boxed{\;v_\theta(R)\;\propto\;\frac{1}{\sqrt{h(R)}}\;}$$

Yani **dönüş hızı, disk kalınlığının kareköküyle ters orantılı olmak zorundadır.** Gerçek galaktik diskler dışa doğru kalınlaşır (flaring) ve bu kalınlaşma 21 cm HI gözlemlerinden bağımsız olarak ölçülmüştür. Sınav buradan doğar.

**Sınavın dayandığı özdeşleştirme:** akı tüpü kalınlığı $h$, gözlenen gaz katmanı kalınlığıyla eşitlenir. Bu, teorinin kendi mantığının gerektirdiği okumadır — Postülat 7 gereği madde ortam tarafından taşınır, dolayısıyla gaz katmanı akı tüpünün maddi izleyicisidir. (Bu özdeşleştirme reddedilirse sınav geçersiz olur; bedeli 6.6.3'ün sonunda tartışılıyor.)

### Veri

| $R$ (kpc) | $h_{\rm HI}$ (kpc) | $v_{\rm gözlenen}$ (km/s) | $v_{\rm öngörü}\propto h^{-1/2}$ | Fark |
|---|---|---|---|---|
| 4 | ~0,08 | ~220 | **301** | 1,37× |
| 8,5 | ~0,15 | ~220 | 220 *(normalizasyon)* | 1,00× |
| 12 | ~0,25 | ~215 | **170** | 0,79× |
| 16 | ~0,50 | ~205 | **120** | 0,59× |
| 20 | ~0,90 | ~195 | **90** | 0,46× |

*(HI ölçek yükseklikleri: Nakanishi & Sofue 2003; Kalberla & Kerp 2009 mertebesinde tipik değerler. Dönüş eğrisi: dış diskte ~$-1{,}7$ km/s/kpc eğimli yavaş azalan profil, Eilers ve ark. 2019 mertebesinde. Değerler izleyiciye ve modele göre değişir; aşağıdaki sonuç bu belirsizliği taşır ama mertebe düzeyinde ona duyarlı değildir.)*

### Sonuç: sınav başarısız

$$\text{Öngörülen: } 301\to90\ \text{km/s}\ (\textbf{3,4 kat düşüş}) \qquad \text{Gözlenen: } 220\to195\ \text{km/s}\ (\textbf{1,13 kat})$$

Aynı şey ters yönden okunursa daha keskindir: gözlenen dönüş eğrisinin düzlüğü, $h$'nin 8,5–20 kpc arasında **en fazla 1,27 kat** büyümesine izin verir. Gözlenen büyüme **~6 kattır.** Uyuşmazlık $h$'de 4,7 kat, hızda **2,2 kattır.**

Dahası, başarısızlık yalnız genlikte değil **şekildedir**: teori dışa doğru dik düşen bir eğri öngörürken gözlenen eğri neredeyse düzdür. Veri belirsizliği (HI ölçek yüksekliği değerleri modele göre ±%50 değişebilir) bu farkı kapatmaya yetmez.

**Kayıt: $h=$ sabit varsayımı, gaz katmanıyla özdeşleştirildiği biçimiyle gözlemle çelişir. M-38'in $1/R$ rejimi bu haliyle düz dönüş eğrisini açıklayamaz.**

### Başarısızlığın iki çıkışı — ve ikisinin de bedeli

**(a) Akı tüpü gaz katmanından ayrıdır.** Akı tüpü kalınlığı merkezî motor tarafından belirlenir ve sabit kalır; gaz ise kendi basıncı nedeniyle (dikey geri-çağırıcı kuvvet $\Omega_z^2=GM/r^3$ dışa doğru zayıfladığı için) tüpün ötesine yayılır. Bu fizikçe tutarlıdır — standart galaktik dinamikte gaz kalınlaşmasının nedeni tam olarak budur. **Bedeli:** $h$ o zaman gözlemle bağlanmamış serbest bir fonksiyon olur ve $1/R$ yasası **yanlışlanamaz** hale gelir. Teori, başarısız bir sınavı sınanamaz bir varsayımla değiştirmiş olur.

**(b) $1/R$ rejimi kalınlaşan bölgeyi kapsamaz.** M-38 geçerlilik penceresini zaten $r_0<R<R_{kesim}$ ile sınırlar; $R_{kesim}$ kalınlaşmanın başladığı yarıçapta olabilir. **Bedeli:** kalınlaşma 12 kpc'den sonra belirginleşir, yani karanlık maddenin en çok gerektiği bölge ($R\gtrsim12$ kpc) yasanın *dışında* kalır. Bu, teorinin karanlık madde alternatifini tam olarak ihtiyaç duyulan yerde geçersiz kılar.

Her iki çıkış da teorinin lehine değildir. Dürüst kayıt: **bu sınav, teorinin galaktik ayağının en zayıf halkasını göstermiştir.**

### Başarısızlığın ürettiği yeni öngörü — düzlem dışı gaz gecikmesi

(a) çıkışı seçilirse — akı tüpü ince, gaz onun ötesine yayılıyor — **sınanabilir bir sonuç doğar.** Tüpün dışındaki gaz ($|z|\gtrsim h_0/2$) $1/R$ eksenel itimini **hissetmez**; yalnız $1/r^2$ radyal itimi kalır. Dolayısıyla:

$$v_\theta(|z|\gg h_0)\;\longrightarrow\;\sqrt{\frac{GM}{R}}\qquad\text{(Kepler'e doğru)}$$

Yani **düzlem dışı gaz, orta düzlem gazından daha yavaş dönmelidir**, ve gecikme $|z|\sim h_0$ civarında başlamalıdır.

Gözlemsel durum: kenarından görülen galaksilerde düzlem dışı HI'nın orta düzlemden **daha yavaş döndüğü** gerçekten ölçülmüştür ("lagging halo"; örn. NGC 891). Standart açıklama galaktik fıskiye / yığışma akışlarıdır. Teorinin versiyonu **nicel ve farklıdır**: gecikmenin başladığı yükseklik $h_0$'ı verir ve yeterince yukarıda hızın Kepler değerine yaklaşmasını gerektirir. Bu, mevcut HI veri kübleriyle sınanabilir ve iki açıklamayı ayırt edebilir.

Bu, başarısız bir sınavın ürettiği ilk yeni sınavdır; 6.6.4'ün bekleyenler listesine eklenmiştir.

---

## 6.6.4 Sınav 3 — Düzlem Dışı Gaz Gecikmesi

Sınav 2'nin başarısızlığından doğan öngörü. Akı tüpü ince ise ($h_0$ sabit), $|z|>h_0/2$ gazı eksenel itimi hissetmez; geriye yalnız baryonik kütlenin $1/r^2$ itimi kalır. Öngörü **iki parçalıdır** ve ikisi ayrı ayrı sınanır:

| | Öngörü |
|---|---|
| **Konum** | Gecikme $\lvert z\rvert\approx h_0/2$'de **başlamalı** — akı tüpünün kenarı |
| **Asimptot** | Yeterince yukarıda $v_\theta\to\sqrt{GM_{\rm baryonik}/R}$ — ve **bunun altına inmemeli** (dairesel yörünge tabanı) |

### Veri: NGC 891

En iyi ölçülmüş kenardan-görünüm galaksisi (HALOGAS; Oosterloo, Fraternali & Sancisi 2007). Düzlem dışı HI $\lvert z\rvert\sim14$ kpc'ye kadar uzanır.

| Büyüklük | Değer |
|---|---|
| Orta düzlem dönüş hızı | ~230 km/s |
| Gözlenen dikey gradyan | ~$-15$ km/s/kpc |
| Kapalı baryonik kütle ($R=10$ kpc) | $\approx3{,}8\times10^{10}\,M_\odot$ (yıldız + gaz) |
| **Teorinin Kepler tabanı** | **127 km/s** (küresel) → **~146 km/s** (disk geometrisi düzeltmesiyle) |
| Akı tüpü kalınlığı $h_0$ | ~0,15 kpc (iç disk gaz ölçek yüksekliği) |

### Sonuç 1 — Konum: kesin başarısızlık

Teori $\lvert z\rvert\gtrsim0{,}07$ kpc'de **basamak** öngörür: 230 → 146 km/s. Gözlem:

| $\lvert z\rvert$ (kpc) | Gözlenen | Teori | Fark |
|---|---|---|---|
| 0,15 | 228 | 146 | **82** |
| 0,5 | 222 | 146 | **76** |
| 1 | 215 | 146 | 69 |
| 2 | 200 | 146 | 54 |

Teori, 500 parsek yükseklikteki gazın çoktan yarı hızda dönmesini gerektiriyor; gaz 222 km/s ile dönüyor. **Verinin en güvenilir olduğu bölgede (küçük $z$) uyuşmazlık 76–82 km/s'dir.** Basamak yoktur; onun yerine on kpc'ye yayılan düzgün bir gradyan vardır. Hiçbir $h_0$ seçimi bunu düzeltmez, çünkü sorun genlikte değil **fonksiyonun biçiminde**: teori basamak, gözlem rampa veriyor.

### Sonuç 2 — Asimptot: sınav geçersiz çıkıyor

Teori 146 km/s'lik bir **taban** öngörür — dairesel yörüngede baryonik kütlenin izin verdiği en düşük hız. Gözlem bu tabanın **altına iniyor**:

$$z\approx8\ \text{kpc}:\;110\ \text{km/s}\qquad z\approx12\ \text{kpc}:\;\sim50\ \text{km/s}$$

Kepler tabanının altında dönen gaz **dairesel yörüngede değildir** — düşüyor, akıyor, açısal momentum kaybediyor. Dolayısıyla yüksek $z$ gazı bir *dönüş eğrisi* taşımıyor; bir **dinamik akış** taşıyor (galaktik fıskiye / yığışma).

Bunun sonucu ikilidir ve ikisi de kaydedilmelidir:

- **Sınavın asimptot ayağı geçersizdir.** Dairesel dengede olmayan gazdan hiçbir kütleçekim modeli sınanamaz — teorinin modeli de, standart model de. Asimptot karşılaştırması yapılamaz.
- **Geçen turun "gözlemsel destek" okuması geri alınmalıdır.** Sınav 2'nin (a) çıkışını sunarken düzlem dışı gecikmenin ("lagging halo") teorinin lehine nitel bir destek olduğunu yazmıştım. **Bu okuma hatalıydı:** gaz Kepler tabanının altında olduğu için gecikme, potansiyelin değil akışın imzasıdır. Sınav 2'nin başarısızlığı, bu teselli olmadan duruyor.

### Sınav 3'ün toplu sonucu

**Başarısız.** Geçerli olan ayak (konum) kesin biçimde çürütülmüştür; diğer ayak (asimptot) gözlemin doğası nedeniyle sınanamaz. Sınav 2'nin (a) çıkışı — "akı tüpü ince, gaz ötesine yayılıyor" — böylece kendi öngörüsünü de kaybetmiştir.

Kalan tek yapısal olasılık, akı tüpünün **yumuşak kenarlı** olmasıdır (akı yoğunluğunun $z$ ile tedrici azalması). Bu, gözlenen rampayı taklit edebilir — ama $h_{\rm etkin}(z)$ diye yeni bir serbest fonksiyon getirir. O halde tablo şudur: eksenel itimin galaktik ayağı ya **yanlışlanmıştır** ya da **iki serbest fonksiyona** ($h(R)$ ve $h_{\rm etkin}(z)$) dayanmaktadır. İkisi de teorinin bu kolunu şu an gözlemsel içerikten yoksun bırakır.

---

## 6.6.5 Sınav 4 — $k=\tfrac12$ ve Sıkışma Kanalının Hızı

Bu sınav öncekilerden farklı bir katmandadır: bir uygulamayı değil, **ortamın hâl denklemini** sınar.

### Sınavın kurulumu

**Ek M-44** ortamın hâl denklemini teorinin mevcut tanımlarından belirler: $\delta\rho/\rho_0=k\,\delta P/P_0$ integre edilince $P=K\rho^{1/k}$, dolayısıyla

$$\frac{dP}{d\rho}=\frac{c^2}{k}\qquad\Longrightarrow\qquad c_{\text{sıkışma}}=\frac{c}{\sqrt k}$$

Süper-akışkan (Gross–Pitaevskii) yorumu $k=\tfrac12$ öngörür, yani $c_{\text{sıkışma}}=\sqrt2\,c$.

**Sınanacak gözlem hazırdır ve kitap onu zaten kullanmaktadır.** Ek M-13 ve Ek M-5 şunu yazar: *"Teoride 'kütleçekim dalgası' denen basınç salınımları basınç kanalının olayıdır ve $c$ ile yayılır; GW170817 kısıtı sıkışma kanalını bağlar."* GW170817'de kütleçekim dalgası ile gama ışını 40 Mpc'den sonra **1,74 saniye** arayla geldi (Abbott ve ark., 2017):

$$\frac{|v_{GW}-c|}{c} < 4{,}2\times10^{-16}$$

> **"Ama teoride sabit $c$ yok" itirazı — ve neden kaçış sağlamadığı.** Teorinin en temel duruşlarından biri $c$'nin evrensel sabit olmamasıdır ($c_{loc}=\sqrt{P/\rho}$, yol boyunca değişir). Dolayısıyla "GW $c$ ile yayılır" cümlesi teoride tanımsızdır ve ilk bakışta kısıt da geçersiz görünür. Kontrol edildiğinde kaçış olmadığı görülür: GW170817 mutlak hızı değil, **aynı yol boyunca bir oranı** ölçer, ve iki hız da aynı yerel ortam durumundan beslendiği için $c_{loc}$ **sadeleşir**:
> $$T_{ışık}=\int\frac{ds}{c_{loc}(x)}\,,\qquad T_{sıkışma}=\int\frac{ds}{c_{loc}(x)/\sqrt k}=\sqrt k\;T_{ışık}$$
> $$\Longrightarrow\quad \frac{T_{sıkışma}}{T_{ışık}}=\sqrt k\quad\text{(yoldan bağımsız, tam)}$$
> Yani değişken $c$ kısıtı zayıflatmaz; tersine onu yerel ortam ayrıntılarından **tümüyle arındırır**. Kısıt doğrudan $k$ üzerinedir.
>
> Bu itirazın gerçek katkısı başkadır ve önemlidir: **Ek M-13'ün "$c$ ile yayılır" ifadesi, iki farklı büyüklüğü aynı harfle yazarak çelişkiyi görünmez tutuyordu.** Zerre ötelemesi $c_{loc}$ ile gider; sıkışma dalgası $c_{loc}/\sqrt k$ ile. M-13 kütleçekim dalgasını sıkışma kanalına atayıp hızını öteleme hızıyla yazmıştır. İkisi ancak $k=1$'de eşittir. M-13 ve M-5 buna göre düzeltilmiştir.

### Sonuç: $k=\tfrac12$ kesin biçimde yanlışlanır

| $k$ | $c_{\text{sıkışma}}$ | GW170817'de gelme farkı |
|---|---|---|
| **$\tfrac12$ (M-44 öngörüsü)** | $1{,}4142\,c$ | **38,2 milyon yıl ÖNCE** |
| 0,9 | $1{,}0541\,c$ | 6,7 milyon yıl önce |
| 0,99 | $1{,}0050\,c$ | 0,65 milyon yıl önce |
| *Gözlenen* | — | *1,74 saniye **önce** — ve bu bile hız farkı değil, jetin çıkış gecikmesi* |

$k=\tfrac12$, kütleçekim dalgasının ışıktan **38,2 milyon yıl önce** gelmesini gerektirir. Gözlenen fark **1,74 saniyedir** — ve o 1,74 saniye bile bir hız farkı değil, gama patlamasını üreten jetin çıkış gecikmesi olarak anlaşılmaktadır. Öngörü $\sim10^{15}$ mertebesinde yanlıştır.

*(Düzeltme kaydı: bu satırın ilk sürümü gözlemi "1,74 saniye **sonra**" diye yazıyordu. Doğrusu **önce**dir — GW170817'de kütleçekim dalgası 12:41:04,4 UTC'de, gama patlaması 12:41:06,5 UTC'de kaydedildi. Yön hatası sonucu değiştirmez: teori 38,2 milyon yıl istiyor, gözlem 1,74 saniye veriyor.)*

### Ve daha ağırı: sonuç bir mengene doğuruyor

GW170817'yi sağlayacak $k$ değeri geriye doğru çözülür:

$$k = 1-8{,}9\times10^{-16}$$

Bu $k$ ile arka plan basıncı:

$$P_0=\frac{1-k}{4}\rho_nc^2 = 5{,}4\times10^{18}\ \text{Pa}$$

Oysa **Ek M-7**'nin yırtılmama koşulu (kohezyon sıfır alınarak, en muhafazakâr biçim) $P_0\ge1{,}6\times10^{25}$ Pa gerektirir.

$$\boxed{\;\text{İhlal: }3\times10^{6}\ \text{kat}\;(6{,}5\text{ mertebe})\;}$$

Teori iki bağımsız kısıt arasında sıkışmıştır:

| Kısıt | Yönü | Gerektirdiği |
|---|---|---|
| GW170817 (sıkışma kanalı $=c$) | yukarıdan | $k\to1$ ⟹ $P_0\to0$ |
| M-7 (ortam yırtılmamalı) | aşağıdan | $P_0\ge1{,}6\times10^{25}$ Pa ⟹ $1-k\gtrsim3\times10^{-9}$ |

İkisi 6,5 mertebe uyuşmaz. **Bu, bir uygulamanın değil, hız merdiveninin ve hâl denkleminin sorunudur.**

### ÇÖZÜM: tek $k$ değil, iki ayrı süreç

Mengene gerçek bir fizik çelişkisi değil, **notasyonel bir birleştirmeden** doğuyor. Ek B.3'ün $k$'sı ile Newton–Laplace'ın istediği $k$ aynı büyüklük değil:

| | Hangi süreç | Zaman ölçeği |
|---|---|---|
| **Ek B.3'ün $k$'sı** | Kütlenin ortamı **deplase etmesi** — statik, denge kurulmuş | eonlar |
| **Newton–Laplace'ın $k$'sı** | Ortamın kendi **adiyabatik sıkışması** — dalga | periyot |

Bu ayrım akışkanlar mekaniğinde standarttır ve Newton'un ses hızını %22 yanlış hesaplamasının nedeni tam olarak budur (izotermal ↔ adiyabatik). İki süreç ayrıldığında çelişki kalmıyor.

**1. Dalga kanalı: ortam stiff (Zel'dovich) akışkandır.** Teorinin resmî bağıntısı $\rho_0=P_0/c^2$ (M-1'in kutulu sonucu) bir hâl denklemidir: $P=c^2\rho$. Bunun türevi:

$$\frac{dP}{d\rho}=c^2 \qquad\Longrightarrow\qquad v_{ses}=c\ \ \textbf{tam olarak}$$

Stiff akışkan, ses hızının ışık hızına *tam eşit* olduğu benzersiz hâl denklemidir — nedensel olarak en katı hâl. **GW170817 otomatik sağlanır**, çünkü sıkışma kanalı zaten $c$'dedir. Bu, Ek M-5 ve M-13'ün baştan beri yazdığı şeydir.

**2. Deplasman kanalı: $k=0$.** Nükleonlar ortamı dışlar. Ek M-15'in **G2 aksiyomu** bunu zaten kurar: madde içinde $\bar P_m=P_0(1-\phi)$ ama $\bar\rho_m=\rho_0$ — basınç düşer, ortalama yoğunluk **korunur**. Bu süreçte

$$\frac{\delta\rho}{\rho_0}=0\qquad\Longrightarrow\qquad \boxed{\;k=0\;}$$

$k=0$ serbest bir seçim değil, G2'nin zorunlu sonucudur.

### Mengene kapanıyor

$P_0$ kalibrasyonuna giren süreç **deplasmandır** (kütlenin açtığı açık $\Delta P=\rho_n\Phi$), dolayısıyla $k=0$ kullanılır:

| Büyüklük | Değer | Kontrol |
|---|---|---|
| $P_0=\tfrac{1-k}{4}\rho_nc^2$ | $6{,}07\times10^{33}$ Pa | M-7 tabanı $1{,}6\times10^{25}$ Pa ✓ **$3{,}8\times10^{8}$ kat marj** |
| $\rho_0=\rho_n/4$ | $6{,}8\times10^{16}$ kg/m³ | ✓ |
| Sıkışma dalgası hızı | **tam $c$** | GW170817 ($4{,}2\times10^{-16}$) ✓ |
| $\delta c/c=\tfrac12\,\delta P/P_0$ | maksimum tepki | ışık bükülmesi $1{,}7512''$ ✓ |
| Yön Kuralı | $\delta P<0\Rightarrow\delta c<0$ | ✓ |

**Hepsi kapanıyor, yeni parametre eklenmeden.** 6,5 mertebelik ihlal ortadan kalkıyor.

### Bu çözümün bedeli: manüskriptin üç kaydı düşüyor

Çözüm bedava değil — bu oturumda eklenen üç sonucu geçersiz kılıyor ve dürüstçe kaydedilmelidir:

1. **Ek M-44'ün politrop türetimi geçersizdir.** $\delta\rho/\rho_0=k\,\delta P/P_0$ integre edilip $P=K\rho^{1/k}$ yazılmıştı. Bu bir kategori hatasıdır: söz konusu bağıntı bir *hâl denklemi değil*, maddenin eklenmesiyle ortam durumunun nasıl değiştiğini söyleyen bir ilişkidir. Gerçek hâl denklemi **stiff**tir: $P=c^2\rho$, $\Gamma=1$.
2. **"$k$, politrop indisin tersidir" sonucu düşer.** $k$ deplasman kuplajıdır, adiyabatik indis değil.
3. **$k=\tfrac12$ öngörüsü ölür** — ve sanılandan derin bir nedenle: Gross–Pitaevskii ortalama-alan argümanı ($P\propto\rho^2$) stiff hâl denklemiyle bağdaşmaz. Ortam GP tipi değil **Zel'dovich tipi** bir akışkandır.

Ayrıca: manüskriptin bir denetim turunda Ek M-5 ve M-9'un *"sıkışma kanalının hızı $c$'dir"* ifadeleri $c/\sqrt k$ diye "düzeltilmişti". **O düzeltme hatalıydı; orijinal metin doğruydu** ve geri alınmıştır.

### Kalan açık uç

Çözüm, iki sürecin farklı $k$'lara sahip olduğunu **gösteriyor** ama ikisinin tek bir mikro-modelden birlikte çıktığını göstermiyor. Yani: ortamın adiyabatik tepkisinin neden tam olarak stiff ($\Gamma=1$) olduğu ve deplasmanın neden tam olarak yoğunluk-korumalı ($k=0$) olduğu, ayrı ayrı postülat düzeyindedir. Bunları tek bir hâl ilişkisinden türetmek Ek M-44'ün (Blok I) yeniden yazılmasını gerektirir ve eylem ilkesi programının parçasıdır.

### Sınav 4'ün toplu sonucu

**$k=\tfrac12$ yanlışlandı** ($\sim10^{15}$ mertebesinde) — bu kısım kesindir. **Ama açtığı mengene çözülmüştür** ve çözüm teorinin kendi iki-süreç yapısından ($P=c^2\rho$ hâl denklemi + G2 deplasman aksiyomu) yeni varsayım eklemeden gelmiştir. Sonuç $k=0$'dır ve bu, manüskriptin $k=\tfrac12$ öngörüsünden *önceki* değeridir.

---

### *(Aşağıdaki bölüm, çözüm bulunmadan önce kaydedilen olası çıkışları saklar — süreç kaydı olarak bırakılmıştır.)*

### Sorunun kaynağı ve o aşamada görülen çıkışlar

Çelişki, teorinin iki kendi ifadesinin bir arada duramamasından doğar:

- **(A)** "Sıkışma kanalı $c$ ile yayılır" (M-5, M-13 — GW170817'yle uyumlu)
- **(B)** "$\delta\rho/\rho_0=k\,\delta P/P_0$ ile $k<1$" (Ek B.3 — Yön Kuralı'nın dayanağı)

Newton–Laplace bağıntısı ($v_{ses}^2=dP/d\rho$, M-5'in kendi 1. varsayımı) altında (A) ve (B) ancak $k=1$'de bir arada durur; $k=1$ ise $P_0=0$ demektir. Olası çıkışlar:

1. **$k$ sabit değildir.** Küçük genlikli dalga rejiminde $k\to1$ (dalga hızı $c$), güçlü statik sıkışma rejiminde $k<1$ (basınç kuyusu). Fizikçe savunulabilir — bir ortamın dinamik ve statik sıkıştırılabilirliği farklı olabilir — ama M-44'ün politrop türetimi **sabit $k$** varsayar ve M-1'in düzeltilmiş notu ayrışmanın "genliğe değil yalnız $k$'ya bağlı" olduğunu söyler. Bu çıkış her iki kaydı da geçersiz kılar ve $k$'yı yeni bir serbest **fonksiyona** çevirir.
2. **Kütleçekim dalgaları sıkışma kanalının olayı değildir.** Ama hız merdiveninde (M-6) $c$'ye eşit başka bir kanal yoktur: $c/\sqrt k>c$, $\sqrt2c$, $v_m>10^4c$, $v_{kav}\gg c$. Yeni bir kanal postülatlanması gerekir.
3. **Newton–Laplace bu ortamda geçerli değildir**; dalga hızı $dP/d\rho$ değil $P/\rho$'dur. Bu, M-5'in 1. varsayımının terk edilmesi ve standart-dışı bir sürekli ortam modeli demektir; gerekçelendirilmesi gerekir.

*(Bu üç çıkış, çözüm bulunmadan önce görülenlerdi. Gerçekleşen çözüm birincisinin daha keskin bir biçimidir: $k$ bir fonksiyona dönüşmedi — **iki ayrı süreç için iki ayrı sabit** olduğu görüldü ve ikisi de teoride zaten tanımlıydı. Yukarıya bakınız.)*

---

## 6.6.6 Sınav 5 — Minimum Karadelik Kütlesi

### Kurulum

**Ek M-40**, karadeliği kafesi kilitlenene kadar sıkışmış madde olarak okur; yarıçapı $R_\rho=(3M/4\pi\rho_n)^{1/3}\propto M^{1/3}$ ile sınırlıdır, Schwarzschild yarıçapı ise $\propto M$. İkisi tek kütlede kesişir ve altında karadelik oluşamaz:

$$M_{\min}=\frac{1}{G}\sqrt{\frac{3c^6}{32\pi G\rho_n}}\approx8{,}3\,M_\odot\;\longrightarrow\;\textbf{4–8}\,M_\odot\ \text{(tavan yukarı alınırsa)}$$

Öngörü: yıldız-kütleli karadeliklerin **alt kenarı** bu bandın altına inmemeli; nötron yıldızı–karadelik "kütle boşluğu" bir seçim etkisi değil **yapısal eşik** olmalı.

### Veri ve sonuç: gerilim, muhtemelen yanlışlanma

Kütleçekim dalgası gözlemleri bu bandı doldurmaktadır:

| Olay | Kompakt cismin kütlesi | Sınıflandırma |
|---|---|---|
| GW190814 (ikincil) | $2{,}50$–$2{,}67\,M_\odot$ | belirsiz: en ağır NY ya da en hafif KD |
| **GW230529** | $\approx2{,}5$–$4{,}5\,M_\odot$ | **muhtemelen düşük kütleli karadelik** |

GW230529'un ağır bileşeni bir karadelikse, gözlenen $M_{\min}\approx2{,}5$–$3{,}6\,M_\odot$ olur ve teorinin 4–8 $M_\odot$ eşiğinin **altına** düşer. Dahası eğilim tek yönlüdür: kütleçekim dalgası kataloğu büyüdükçe "kütle boşluğu" **dolmaktadır**, yani yapısal eşik okuması zayıflamaktadır.

**İlk okuma: gerilim.** Kesin yanlışlanma sınıflandırmanın kesinleşmesine bağlıdır. Ama teorinin öngörüsü doğru yönde değildir ve gelen veri onu sıkıştırmaktadır.

### ÇÖZÜM: öngörünün premisi yanlış — ve doğru okuma tersine dönüyor

Sınav 4'ün sonucu (ortamın stiff hâl denklemi) bu sınavın dayanağını da denetlemeyi gerektirdi. Denetim, öngörünün **kurulmaması gerektiğini** gösterdi. Üç katmanda:

**1. $\rho_n$ bir sıkışma tavanı değildir.** Öngörü "kafes kilitlenene kadar sıkışma" varsayarak $\rho_n$'i tavan alıyordu. Ama stiff hâl denkleminde ($P=c^2\rho$, Ek M-44) **tavan yoktur** — basınç yoğunlukla doğrusal büyür, doyma noktası bulunmaz. Gözlemsel olarak da yoktur: nötron yıldızlarının ortalama yoğunluğu ($\approx3{,}9\times10^{17}$ kg/m³) $\rho_n$'i ($2{,}7\times10^{17}$) **1,4 kat aşar.**

**2. Hesap iki çerçeveden melez kuruluydu.** Newton hacmi $(3M/4\pi\rho_n)^{1/3}$ ile Schwarzschild yarıçapı $2GM/c^2$ karşılaştırılmıştı; iki büyüklük ayrı çerçevelerden gelir ve hiçbiri bu birleşimi onaylamaz.

**3. Ve asıl mesele: teorinin güçlü alan rejimi yoktur.** Ek M-42 yalnız **birinci mertebeyi** verir ($\gamma=1$) ve $\beta$'nın belirsiz olduğunu açıkça kaydeder. Karadelik tanımı gereği güçlü alan olgusudur. Dolayısıyla **teori şu an nicel karadelik öngörüsü yapamaz** — ne minimum kütle, ne ufuk yapısı. (Ek M-40'ın kompaktlık tablosundaki $\Phi/c^2=0{,}5$ bile GR'dan ödünçtür.) Öngörü çürütülmedi; **türetilmiş alanın dışında** olduğu için hiç kurulmamalıydı.

### Teorinin gerçekten söylediği — ve işaretin ters dönmesi

Stiff hâl denkleminin kompakt cisimler için **nitel** bir sonucu vardır ve bu sonuç ilk okumanın tersi yöndedir.

Stiff akışkan, nedensellik sınırını **doyuran** hâl denklemidir ($dP/d\varepsilon=c^2$; izin verilen en katı). Rhoades–Ruffini teoremi (1974) tam bunu kullanır: nedenselliğe uyan herhangi bir hâl denklemi için kompakt cismin maksimum kütlesi sınırlıdır ve **sınır stiff hâl denklemiyle doyar.** Eşleme yoğunluğu $\rho_n$ alınırsa ($M_{max}\propto\rho^{-1/2}$):

$$M_{max}\approx3{,}2\,M_\odot\sqrt{\frac{4{,}6\times10^{17}}{2{,}7\times10^{17}}}\approx4\,M_\odot$$

Yani teori, kararlı kompakt cisimler için **izin verilebilecek en yüksek** kütle tavanını öngörür — minimum karadelik kütlesi değil, **maksimum nötron yıldızı kütlesi.**

**Kütle boşluğu neden bir bilmecedir?** Standart nükleer hâl denklemleri maksimum NY kütlesini ~2,2–2,5 $M_\odot$ verir; o yüzden 2,6 $M_\odot$'lık bir cisim ya rekor bir NY'dir (yumuşak hâl denklemlerini zorlar) ya rekor hafif bir KD'dir (oluşum modellerini zorlar). **Daha katı hâl denklemi bu zorlamayı ortadan kaldırır.**

| Gözlem | Kütle ($M_\odot$) | Stiff hâl denklemiyle |
|---|---|---|
| PSR J0740+6620 | 2,08 | rahat NY ✓ |
| PSR J0952-0607 | $2{,}35\pm0{,}17$ | rahat NY ✓ |
| **GW190814 ikincil** | 2,50–2,67 | **rahat NY** — yumuşak EOS zorlanır, stiff zorlanmaz |
| GW230529 | 2,5–4,5 | alt ucu NY olabilir |
| *Teorinin tavanı* | *~4* | — |

**Dolayısıyla ilk okuma tersine döner:** kütle boşluğunu dolduran cisimler teoriyi sıkıştırmıyor, **stiff ortamın lehine tanıklık ediyor.** Yumuşak hâl denklemleri o cisimleri açıklamakta zorlanırken teorinin ortamı onları rahatça nötron yıldızı olarak barındırır.

### Sınav 5'in toplu sonucu

**Öngörü geri çekildi** (premisi yanlış: $\rho_n$ tavan değil, hesap melez, konu güçlü alan rejimi). **Verdikt "gerilim / muhtemelen yanlışlanma"dan "teorinin türetilmiş alanı dışında, nitel işareti olumlu"ya değişti.**

**Dürüst sınır — bunu "geçilmiş sınav" saymıyoruz:**
- Rhoades–Ruffini **GR makinesidir** (TOV denklemi). Teori kendi kompakt cisim yapı denklemlerini türetmemiştir; ~4 $M_\odot$ ödünç bir sayıdır. Bu, Ek M-40'ın $\xi$'sinin düzeltilmeden önceki durumuyla aynı sorundur.
- Tavan, eşleme yoğunluğu seçimine duyarlıdır ($\rho_n$ ↔ $\rho_0$ arası iki kat).
- Teorinin kendi güçlü alan denklemleri kurulmadan bu satır bir **beklenti**dir, öngörü değil.

**Açık iş:** teorinin eylem ilkesinden (Ek M-44 Açık Uç 1) bir TOV muadili çıkarılması. O yapılırsa maksimum kompakt cisim kütlesi teori-içi bir öngörüye dönüşür ve GW190814/GW230529 gerçek bir sınav olur.

---

## 6.6.7 Yürütülemeyen Sınavlar

Aşağıdaki üç öngörü 6.6.1'in koşullarını sağlar ama **şu anda sınanamaz** — ve nedenleri kaydedilmelidir, çünkü bir öngörünün sınanamaz olması onun değerini doğrudan etkiler.

| Öngörü | Neden yürütülemiyor |
|---|---|
| $\Sigma/P_0\gtrsim6{,}4\times10^{8}$ (Ek M-43) | $\Sigma$'nın **bağımsız ölçümü yoktur.** Elde yalnız Bell deneylerinin verdiği alt sınır ($>10^8$) var ve öngörü de alt sınır biçiminde; iki alt sınır birbirini sınamaz. Sınav, $\Sigma$'yı yukarıdan bağlayacak bir gözlem bulunana kadar bekler. |
| $\tau_{ret}\propto\rho_ca_bv^{-4}$ (Ek M-43) | Retrograd cisimlerin sönüm **hızları gözlenmiyor**; elde yalnız "Phoebe 4 Gyr hayatta kaldı" türü *hayatta kalma sınırları* var. Sönüm süresi tahmini, sınanacak teorinin kendisini gerektiriyor — döngüsel. Popülasyon testi ancak sönümü *devam ederken* yakalanmış cisimlerle kurulabilir. |
| $\xi=(I/MR^2)\lvert\delta c_{loc}/c\rvert$ farklı cisimlerde (Ek M-40) | Dünya dışında $\xi$'yi bağımsız ölçen veri yok. Nötron yıldızı devinimi ve glitch istatistiği, $\xi$'ye ancak iç yapı modelleri üzerinden bağlanıyor; o modeller de $I/MR^2$'yi serbest bırakıyor. Ayrıştırılamıyor. |

Bu üç kalem, teorinin öngörü *tablosunda* durur ama sınav *programında* duramaz. Aradaki fark, 6.6.1'in üçüncü koşuludur: yanlışlayacak bir çıktının **erişilebilir** olması.

---

## 6.6.8 Sınav Programının Güncel Durumu

Bu turda öngörü tablosunun **sınanabilir kalemleri tüketilmiştir.** Kitabın yanlışlanabilir öngörüler listesinden (7.5 ve Ek M blok tabloları) 6.6.1'in üç koşulunu sağlayan her kalem ya çalıştırıldı ya da neden çalıştırılamadığı kaydedildi:

| Öngörü | Durum |
|---|---|
| Yanal itim ↔ gezegen figürü | **Sınav 1** — sınır verdi ($\kappa_5\lesssim0{,}023$); F5 için ayırt edici imza yok, F4 için $J_4$ kanalı açık |
| $v_\theta\propto h^{-1/2}$ (yayılan disk) | **Sınav 2** — başarısız |
| Düzlem dışı gaz gecikmesi | **Sınav 3** — başarısız |
| $k=\tfrac12$ / sıkışma kanalı hızı | **Sınav 4** — yanlışlandı; ayrıca temel bir mengene açtı |
| Minimum karadelik kütlesi | **Sınav 5** — öngörü geri çekildi (premis yanlış; güçlü alan rejimi teoride yok). Nitel işaret **olumlu**: stiff ortam ağır nötron yıldızlarına izin verir |
| $\Sigma/P_0$, $\tau_{ret}\propto v^{-4}$, $\xi$'nin cisimler arası tutarlılığı | **Yürütülemez** (6.6.7) |

Yeni sınavlar ancak iki yoldan doğar: (i) teorinin yeni ve erişilebilir bir öngörü üretmesi, (ii) 6.6.7'deki üç engelin kalkması — özellikle $\Sigma$'yı yukarıdan bağlayacak bir gözlem bulunması.

**Kısım 5'in deney programı (T-9) bu tablonun dışındadır** ve yazarın planına göre kitabın son fazına bırakılmıştır. Yayımlandığında sınav programının ikinci ayağını oluşturacaktır: buradaki beş sınav *arşiv veriyle* yapılan sınavlardır, oradakiler *teorinin kendi ürettiği veriyle* yapılacaktır — ve ikincisi bağımsız laboratuvar tekrarı gerektirir.

---

## 6.6.9 Dürüst Tabelo

**Sınanan ve geçilen:** Yok. Bu bölümün yazıldığı tarihte teorinin **ayırt edici** bir sınavı henüz geçilmemiştir.

**Sınanan ve sonuç veren:** Üç sınav.
- **Sınav 1 (gezegen figürü, dört terimli):** İki ayrı sonuç. **(a) Yanal itim (F5) için olumsuz:** $\kappa_5\lesssim0{,}023$ (çalışma değeri $\tfrac12$ **yirmi beş kat** fazlaydı, elendi) ve F5 saf $P_2$ olduğu için hiçbir harmonikte ayrı imzası yok — çürütülmedi, *görünmez*. **(b) Eksenel itim (F4) için açık kanal:** merkezkaç $J_4$'e birinci mertebede katkı vermediği için F4'ün $P_4$'ü görünür hale geliyor; genliği ölçülen $J_4$'ün **%4–8'i** ve **işareti doğru** (gözlemi derinleştiriyor, hidrostatik referansın da eksik kaldığı yön). Mevcut hassasiyet ne doğruluyor ne dışlıyor — **sınav programının olumsuz olmayan ilk sonucu.**
- **Sınav 2 (yayılan disk): BAŞARISIZ.** $v_\theta\propto h^{-1/2}$ öngörüsü 3,4 kat düşüş isterken gözlenen 1,13 kattır; uyuşmazlık hızda 2,2, ölçek yüksekliğinde 4,7 kat. $h=$ sabit varsayımı gaz katmanıyla özdeşleştirildiği biçimiyle **çelişir** ve M-38'in $1/R$ rejimi bu haliyle düz dönüş eğrisini açıklayamaz.
- **Sınav 3 (düzlem dışı gaz gecikmesi): BAŞARISIZ.** Teori $\lvert z\rvert\approx h_0/2\approx0{,}07$ kpc'de basamak öngörüyor; gözlem 0,5 kpc'de hâlâ 222 km/s (teori 146) — uyuşmazlık **76–82 km/s**, ve biçim yanlış (basamak ↔ rampa). Ayrıca yüksek $z$ gazı Kepler tabanının **altına** indiği için dairesel yörüngede değildir: asimptot ayağı **sınanamaz**. Sınav 2'nin (a) çıkışı böylece kendi öngörüsünü de kaybetmiştir.

- **Sınav 4 ($k=\tfrac12$ ve sıkışma kanalı): YANLIŞLANDI — ve bir mengene açtı.** $k=\tfrac12$, kütleçekim dalgasının ışıktan **38,2 milyon yıl önce** gelmesini gerektirir; gözlenen 1,74 saniye *sonradır* ($\sim10^{15}$ mertebesinde yanlış). Dahası GW170817'nin gerektirdiği $k=1-8{,}9\times10^{-16}$, $P_0=5{,}4\times10^{18}$ Pa verir ve **Ek M-7'nin yırtılmama tabanını ($1{,}6\times10^{25}$ Pa) 6,5 mertebe ihlal eder.** Bu, bir uygulamanın değil **hâl denkleminin ve hız merdiveninin** sorunudur.
- **Sınav 5 (minimum karadelik kütlesi): ÖNGÖRÜ GERİ ÇEKİLDİ.** Premis yanlıştı: $\rho_n$ bir sıkışma tavanı değil (stiff hâl denkleminde tavan yok; nötron yıldızları $\rho_n$'i 1,4 kat aşıyor), hesap Newton-hacmi/Schwarzschild melezi, ve konu teorinin **güçlü alan rejimine** ait — M-42 yalnız 1PN veriyor, dolayısıyla nicel karadelik öngörüsü kurulamaz. **Verdikt tersine döndü:** stiff ortam nedensellik sınırını doyurduğu için *daha ağır* nötron yıldızlarına izin verir (Rhoades–Ruffini tavanı ~4 $M_\odot$); kütle boşluğunu dolduran cisimler (GW190814'ün 2,6 $M_\odot$'ı) yumuşak hâl denklemlerini zorlarken stiff ortamı **desteklemektedir.** Geçilmiş sınav sayılmıyor: ~4 $M_\odot$ GR'dan (TOV) ödünçtür, teori kendi kompakt cisim denklemlerini türetmemiştir.

**Yürütülemeyen (6.6.7):** Üç öngörü — $\Sigma/P_0$ (bağımsız $\Sigma$ ölçümü yok), $\tau_{ret}\propto v^{-4}$ (sönüm hızları gözlenmiyor; tahmin döngüsel), $\xi$'nin cisimler arası tutarlılığı (iç yapı modellerinden ayrıştırılamıyor).

**Sınav tasarımı düzeltilen:** İki. (i) $J_4$ imzasının **yanal itimde** aranması — F5'in potansiyeli saf $P_2$ olduğu için orada imza yoktur; imza **eksenel itimdedir** ve multipol ayrıştırması bunu göstermiştir. (ii) Sınav 1'in ilk kurulumu **dört terimli dengeyi ikiye indiriyordu** — eksenel itimin şişmeye karşı çalıştığı atlanmıştı (yazar düzeltmesi). Yeniden kurulunca $\kappa_5$ sınırı ayakta kaldı (F4 dört mertebe zayıf) ama $J_4$ kanalı açıldı.

**Geri alınan okuma:** Bir. Sınav 2 yazılırken düzlem dışı gecikmenin teorinin lehine nitel destek olduğu belirtilmişti; Sınav 3 bu okumanın hatalı olduğunu gösterdi (gaz Kepler tabanının altında olduğu için gecikme potansiyelin değil akışın imzasıdır).

**Retrodiksiyonlar (sınav değil, kapsama kanıtı):** Işık bükülmesi $1{,}7512''$ · jeodetik presesyon ~6.606 mas/yıl · Shapiro ≈247 µs · GP-B çerçeve sürüklenmesi 41,0 mas/yıl (0,52σ) · LAGEOS 30,6/31,4 mas/yıl · kütleçekimsel kızıla kayma · Fizeau katsayısı 0,437 · denge gelgiti 0,53 + 0,25 m · Lorentz testlerinin null sonuçları.

**Bekleyen:** Yok — bu turda öngörü tablosunun sınanabilir kalemleri tüketilmiştir. Yeni sınavlar ancak yeni öngörülerden ya da 6.6.7'nin önündeki engellerin kalkmasından doğar.

---

### Bu tabelonun anlamı

Teorinin matematiği bu manüskriptte iç tutarlılık düzeyinde denetlenmiş ve büyük ölçüde tutarlı bulunmuştur; yerleşik fiziğin sayılarını ek serbest parametre üretmeden kapsadığı da gösterilmiştir. **Bunların hiçbiri teorinin doğru olduğunu göstermez** — ve beş sınavın sonucu bunu somutlaştırmıştır.

**İki katman ayrılmalıdır, çünkü sonuçlar aynı ağırlıkta değildir:**

| Katman | Durum |
|---|---|
| **Uygulamalar** (Sınav 1, 2, 3, 5) | Yanal itimin gözlemsel içeriği şüpheli; eksenel itimin **galaktik** ayağı çürütülmüş ama **gezegen** ayağında doğru işaretli bir kanal açık; minimum karadelik kütlesi gerilimde. Bunlar Postülat 9'un tekil kuvvetlerine ve onların makro uygulamalarına dokunur — **adlandırılmış, bütçelenmiş kalemlerdir.** |
| **Temel** (Sınav 4) | Sıkışma kanalının hızı ile arka plan basıncının alt sınırı **6,5 mertebe uyuşmuyor.** Bu, hâl denklemine ve hız merdivenine dokunur — yani teorinin çekirdek yapısına. |

Sınav 4'ün açtığı mengene, kitabın çözmesi gereken en ağır kalemdir. Çözümü üç yoldan biriyle olabilir ve üçü de bedellidir (6.6.5): $k$'nın sabit olmaktan çıkıp bir **fonksiyona** dönüşmesi, kütleçekim dalgaları için **yeni bir kanal** postülatlanması, ya da Newton–Laplace bağıntısının bu ortam için **terk edilmesi**. *(Bu bulgunun Ek M-5, M-13 ve 7.4'e işlenmesi yazar kararına bırakılmıştır; şu an yalnız bu bölümde kayıtlıdır.)*

**Sağlam kalanlar da kaydedilmelidir.** Beş sınavın hiçbiri şunlara dokunmadı: Kavrama Yasası'nın oran biçimi, ölçek yapısı $\Lambda$ ve ondan çıkan bütün birinci mertebe GR sektörü (bükülme, jeodetik presesyon, Shapiro, $\gamma=1$), Fizeau ailesi, dönme sürüklenmesi (GP-B, LAGEOS), gelgit tensörü. Teorinin en çok sınanmış ve en iyi tutan kolu budur.

> **Bu bölüm bir vitrin değildir.** Sınavlar gerçekten sınav olduğu için sonuçları gerçekten olumsuz çıkabiliyor; beşinin dördü olumsuz çıktı ve hepsi burada, aynı ayrıntıyla duruyor. Teorinin bilimsellik iddiası (7.4) bunu gerektirir — ve bir teoriyi güçlendiren şey, sınavlardan kaçınmak değil, hangilerinde düştüğünü bilmektir.
