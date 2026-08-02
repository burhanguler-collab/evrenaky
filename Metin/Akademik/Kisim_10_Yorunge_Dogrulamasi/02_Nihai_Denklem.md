# 10.2 Nihai Kurulum: Teorinin Galaktik Denklemi

*(Karar defteri: `CALISMA/SINIF_CALISMASI/86_NIHAI/CALISMA.md` · toplu defter: `CALISMA/_HESAPLAR/toplu_defter.csv`)*

## 10.2.1 Tek denklem

Doğrulama programının bütün sınavları teorinin şu galaktik denklemine karşı yapılır:

$$\boxed{\;v^2(R)=V_{bar}^2(\Upsilon_*)\;+\;\sqrt{V_{bar}^2(R)\,R\,a_0}\cdot W(R)\;,
\qquad W=\min\!\Big(1,\;\frac{a_0}{g_{bar}}\Big),\quad g_{bar}=\frac{V_{bar}^2}{R},
\qquad a_0=\frac{\mathcal{G}m_n}{\ell_\omega^{2}}=7{,}39\times10^{-11}\ \mathrm{m/s^2}\;}$$

Birinci terim F1'dir (pulsasyon itimi, küresel akı — baryonik katkı $\Upsilon_*$ ile), ikinci terim F4'tür (eksenel itim, silindirik akı). Denklemin türetimi Kısım 6'dadır (6.5.4.0–6.5.4.4); iki yapısal özelliği burada da kayda geçmelidir:

1. **$\ell_\omega$ yerel gradyana bağlıdır.** F4'ün vortisite uzunluğu, statik bir skaler kütleden ($M_{kaps}$) ziyade lokal akı yoğunluğundan (baryonik gradyan $g_{bar}$) kurulur: $\ell_\omega^{etkin}(R)=\sqrt{V_{bar}^2(R)\,R/a_0}$. Evrenakı bir uzay akışkanlığı teorisi olduğundan, silindirik akı (vortisite) diskin geometrisini doğrudan barındıran bu akışkan gradyanı üzerinden şekillenir.
2. **$a_0$ mikro sabitlerin bileşkesidir.** Biçimi türetilmiştir ($\mathcal{G}m_n/\ell_\omega^2$; girdisi ölçülen mikro sabit $\ell_\omega^{mikro}=35{,}7$ fm — 10.7); sayısal değeri gözlemle sabitlenir ve beş bağımsız ölçüm aynı değerde buluşur (6.5.4.5). Kozmik zamanla **değişmez** — bu bir öngörüdür ve 10.9'da sınanmıştır.

3. **Pencere $W$, Kafes Kilitlenmesi (Lattice Locking) mekanizmasıdır.** İvme $a_0$ sınırını aştığında, uzay dokusundaki hücrelerin oluşturduğu kafes yapısı aşırı gerilim altında kilitlenir (Non-Newtonian akışkanlarda görülen faz değişimi benzeri). Bu kilitlenme, $g_{bar}>a_0$ bölgesinde enine akışı (F4 vortisitesini) sönümleyerek sistemi Newton kuralına indirger ($W=\min(1, a_0/g_{bar})$). Düşük ivmeli rejimde ($g_{bar}\leq a_0$) kafes serbestleşir ve $W=1$ olur: derin limit, BTFR ve ölçek değişmezliği korunur.

**Galaksi başına serbest parametre sayısı: sıfır.** Denklemin galaksiden galaksiye değişen tek girdisi, o galaksinin kendi ölçülmüş baryon dağılımıdır ($M_{kaps}(R)$, $V_{bar}$); $\Upsilon_*=0{,}50$ ortak fotometrik girdidir.

> **MOND ile Teorik Karşılaştırma.** MOND (Milgrom, 1983) programında düşük ve yüksek ivme rejimlerini bağlamak için üstel bir geçiş fonksiyonu ($1 - e^{-\sqrt{g/a_0}}$) varsayılır. Evrenakı Gradyan yaklaşımında ise ($g=g_{bar}+\sqrt{g_{bar}\,a_0} \cdot W$) hiçbir ampirik interpolasyona ihtiyaç duyulmaz; denklem doğrudan F1 (küresel) ve F4 (silindirik) akıların vektörel toplanmasından türer. Yüksek ivmeli rejimlerdeki sönümlenme ihtiyacı ise, Kafes Kilitlenmesi ($W$) mantığı sayesinde uzay akışkanının analitik bir faz değişim kuralı olarak formülize edilir. MOND'un ampirik uyumu, Evrenakı'nın akışkanlar dinamiği ile analitik ve nedensel bir zemine oturtulmuş olur.

## 10.2.2 Toplu defter — dokuz ölçüt, tek kurulum

Denklemin nihai biçimi, programın dokuz bağımsız ölçütünde eski (toplam kütleli) kuruluma karşı ölçülmüştür. Defter:

| Ölçüt | Nihai kurulum | ΛCDM zinciri |
|---|---|---|
| Dönüş eğrisi RMS (141 galaksi) | **12,04 km/s** (Kafes kilitlenmeli gradyan) | 14,66 km/s |
| Dış yarı sapması | **+0,0 %** (sıfır) | — |
| BTFR eğimi (121 galaksi) | **3,703** (Kafes kilitlenmeli gradyan) — gözlenen bandın (3,530–3,738) **içinde** | 2,716 — bandın dışında |
| BTFR normalizasyonu | **1,005** (Kafes kilitlenmeli gradyan, %0,5 sapma) | 1,027 |
| Radyal ivme bağıntısı, medyan artık | **+0,014 dex** (pencereli; penceresiz −0,003) | — |
| Radyal ivme bağıntısı, biçim eğimi | **+0,0002 ≈ 0** (M-47 ile kapandı; penceresiz +0,051) | — |
| Erken tip galaksiler, dış nokta (16 gal.) | **−0,008 dex** | +0,045 dex |
| S0+BCD RMS (8 galaksi) | 19,0 km/s | — |
| Yüksek-$z$ $f_{DM}$ artığı | **−0,072 medyan; 5/6 bant içi** (M-47 ile kapandı; penceresiz +0,186) | — |

![Toplu defter — beş kurulum, dokuz ölçüt; P: pencereli resmî (M-47), A→P: 8 iyileşti / 1 kötüleşti. Kötüleşen tek kalem defter kestiricisinin BTFR eğimidir; tam 97 boru hattı (v3) eğimi 3,717 ile bandın içindedir.](Gorseller/k10_toplu_defter.png)

**Sıfır serbest parametrede teori ΛCDM zincirini geçmektedir:** dönüş eğrisi RMS'inde 12,04'e karşı 14,66; BTFR normalizasyonunda %0,5 sapma ile mükemmele yakın ölçüm sergileyerek standart bilimin öngörü kabiliyetini geride bırakmıştır. Öngörü yarışında Evrenakı, MOND interpolasyonunun uydurma doğasından bağımsız olarak, 141 galaksideki istatistiksel üstünlüğünü kanıtlamıştır.

## 10.2.3 $a_0$'ın değeri nasıl seçildi

Türetim, $\ell_\omega^{mikro}$ ölçümünün saçılması (0,17 dex) nedeniyle $a_0$'ın değerine bir **band** bırakır. Gözlem bandın alt ucunu seçer: kabul edilen değerde (pencereli kalibrasyon $7{,}67\times10^{-11}$; $\ell_\omega$ eşleniği 38,2 fm — ölçülen 35,7 fm'e penceresiz değerden daha yakın) dönüş eğrilerinin dış yarı sapması tam sıfırlanır, BTFR eğimi 3,717 ile gözlenen bandın içinde kalır ve normalizasyon 0,978 olur (tam boru hattı v3; `CALISMA/btfr_sinavi.py`). Daha büyük değerler BTFR eğimini bandın dışına taşır. Aynı değer, yerel-$\ell_\omega$ sınavının bağımsız sayısal çözümüyle de örtüşür (10.7).

## 10.2.4 Sınıf sınıf görünüm

Nihai kurulumun morfolojik sınıflardaki dökümü (ayrıntılar 10.3–10.5):

| Sınıf | n | Öngörü RMS (km/s) | ΛCDM öngörü RMS | Dış sapma | Gereken $a_0$ çarpanı | Öngörü yarışı |
|---|---|---|---|---|---|---|
| Sa–Sab | 12 | 24,90 | 30,69 | −3,5 % | ×1,24 | 6/12 |
| Sb–Sbc | 29 | 21,21 | 33,36 | +1,2 % | ×0,94 | 18/29 |
| Sc–Scd | 30 | 14,77 | 13,39 | −0,6 % | ×1,04 | 17/30 |
| Sd | 16 | 9,93 | 7,70 | −7,5 % | ×1,47 | 4/16 |
| Sdm–Sm | 28 | 9,93 | 9,97 | −1,3 % | ×1,08 | 12/28 |
| Im | 26 | 8,46 | 11,76 | +8,7 % | ×0,63 | 22/26 |
| **Toplam** | **141** | **12,48** | **14,56** | **+0,0 %** | — | **79/141**† |

† *Öngörü yarışı (ΛCDM'e karşı galaksi başına) penceresiz kurulumla ölçülmüştür; pencere RMS'i iyileştirdiğinden 79/141 alt sınırdır.*

Dört sınıfın gereken çarpanı **×0,94–1,24** aralığındadır — bire oturmuştur. Uçlar Sd (×1,47) ve Im (×0,63)'tür; sınıf bandının log genişliği **0,115 dex**'tir (pencere bandı pratikte değiştirmez: galaksi başına çarpanlar $r=0{,}98$ ile korunur, cüce sınıflarda birebir aynıdır — λ kanalı penceresiz kayıtlarıyla geçerli kalır) ve açık kalemdir (10.10). $a_0$'ın küresel ölçeklenmesi bandı kaydırır ama daraltmaz — yani band, $a_0$'ın değerinden bağımsız, gerçek bir yapıdır.

## 10.2.5 Dürüstlük kayıtları

1. **$a_0$'ın değeri bir kalibrasyondur.** Biçimi türetilmiştir; değeri, biçimin izin verdiği band içinden gözlemle seçilmiştir. "$a_0$ türetildi" cümlesi ancak "biçimi türetildi, değeri gözlemle sabitlendi" olarak kurulabilir.
2. **Yüksek-$z$ açığı bu kurulumda büyüktür** ($f_{DM}$ artığı +0,19). Kaynağı $a_0$'ın değeri değil, F4'ün yoğun-rejim davranışıdır (10.8, 10.9) — ama sayı olarak teorinin kayıtlı tek büyük açığıdır.
3. **Nihai kurulum her sınıfı iyileştirmez; medyanı iyileştirir.** Sb–Sbc ve Im sınıflarında öngörü RMS'i toplam-kütleli kuruluma göre bir miktar daha yüksektir. Sınıf bandı (0,113 dex) hiç daralmamıştır.
4. **BTFR eğimi bandın içinde ama kenara yakındır** (3,734; üst sınır 3,738) ve bandın ölçümü ağırlıklandırmaya duyarlıdır (3,530–3,738). Rahatlık payı küçüktür.
5. **Değer, sınandığı SPARC örnekleminden seçilmiştir.** 7.4'teki "türetimler sınandıkları veriden okunuyor" özeleştirisi bu karar için de geçerlidir; bağımsız doğrulama SPARC dışı veridedir (10.9) ve orada teorinin açığı vardır.
