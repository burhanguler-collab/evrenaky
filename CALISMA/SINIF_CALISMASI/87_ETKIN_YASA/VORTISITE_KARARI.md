# Vortisite kararı — F4 beslemesinin tek-üslü taraması ve öz-tutarlı beslemenin dışlanması (iş 5)

**Soru (kullanıcının hipotezi):** F4'ün kaynağı skaler kapsanan kütle mi ($M_{kaps}$, resmî B),
yoksa kapsanan maddenin **dolanım/vortisite** karakteri mi? Hipotez tek küresel üsle taranabilir:

$$v_{F4}^2=\sqrt{\mathcal{G}M_{kaps}\,a_0}\cdot f_{geo}^{\,\alpha/2},
\qquad f_{geo}\equiv\frac{V_{bar}^2R}{\mathcal{G}M_{kaps}}$$

$\alpha=0$: skaler kütle (B) · $\alpha=1$: tam yerel geometri/vortisite ($g_{bar}$-besleme, D) ·
ara $\alpha$: kısmi hizalanma. Ek olarak en radikal vortisite okuması sınandı — **öz-tutarlı
besleme E**: girdabı *toplam akışın* dolanımı besler, $g=g_{bar}+\sqrt{g\,a_0}$.
Hesap: `../../vortisite_taramasi.py` · **Adalet:** her $\alpha$ ve E için $a_0$, nihai kurulumun
kendi kriteriyle (dış-yarı medyan sapma $=0$) ayrı ayrı yeniden kalibre edildi.

## 1. Tarama sonucu (141 galaksi, galaksi başına fit yok)

| $\alpha$ | $k_{kal}$ | medyan RMS | RAR eğimi | sınıf bandı |
|---|---|---|---|---|
| 0,00 (B) | 1,011 | 12,76 | −0,043 | **16,1 %** |
| 0,25 | 0,986 | 12,59 | −0,042 | 16,3 % |
| 0,50 | 0,965 | 12,54 | −0,042 | 16,8 % |
| **0,75** | 0,925 | **12,41** | −0,042 | 17,2 % |
| 1,00 (D) | 0,881 | 12,54 | −0,040 | 17,6 % |
| 1,25 | 0,833 | 19,79 | −0,060 | 17,8 % |
| E (öz-tutarlı) | 0,237 | 13,51 | +0,032 | 27,1 % |

## 2. Üç bulgu

1. **Kısmi vortisite sığ biçimde yeğleniyor.** RMS minimumu $\alpha\approx0{,}75$'te (12,41), ama
   $\alpha\in[0,1]$ boyunca toplam oynama yalnız 0,35 km/s — zayıf bir tercih. $\alpha>1$ hızla
   çöker: tam-üstü ağırlık verice dışlanır.
2. **Besleme, biçim borcunun kaynağı DEĞİL.** RAR eğimi bütün $\alpha$'larda ~−0,04'te sabit;
   sınıf bandı $\alpha$ ile daralmıyor (aksine hafif geriyor — bandın mekanizması $f_{geo}$
   değil, λ/kaskad kanalı: 85'in tezini destekler). Geçiş-biçimi işi toplanma türetiminde
   kalır (7.4-12h).
3. **Öz-tutarlı besleme KESİN DIŞLANDI.** $g=g_{bar}+\sqrt{g\,a_0}$ yapısal bir taban dayatır
   ($g\geq k\,a_0=1{,}76\times10^{-11}$ m/s², kalibre değerle); gözlenen en düşük nokta
   $8{,}0\times10^{-13}$ — **22 kat ihlal.** Ayrıca RMS (13,51) ve sınıf bandı (%27) de en kötü.
   Bu, taramanın en keskin ve kalıcı sonucudur: **girdap kendi akışından beslenemez; F4'ün
   kaynağı baryonların (maddenin) dolanımıdır, sürüklenen ortam akışının kendisi değil.**
   (Kitaptaki akı gerekçesinin — dolanım $R$ içindeki maddeden doğar — verili doğrulamasıdır.)

## 3. KARAR

- **Resmî denklem B'de ($\alpha=0$, $M_{kaps}$) kalır.** Gerekçe: akı teoremi gerekçesi ayakta,
  sınıf bandında en iyi, ve $\alpha$ tercihi kanıt eşiğinin altında (0,35 km/s; galaksi-içi
  noktalar bağımsız değil).
- **Kısmi vortisite ağırlığı [aday] olarak kaydedilir:** veri $\alpha\approx0{,}5$–$0{,}75$'te
  sığ bir minimum gösteriyor. Kullanıcının vortisite sezgisi **kısmen ve kesin bir biçimde
  destekleniyor**: kaynak gerçekten dolanım-karakterli — ama (i) *baryonların* dolanımı
  (E dışlandı) ve (ii) ancak kısmi ağırlıkla ($\alpha\leq1$; tam yerel-geometri okuması bile
  sınıf bandını iyileştirmiyor).
- **Türetim hedefi güncellendi:** F4 besleme/toplanma türetimi (M-37'den) artık üç ölçülmüş
  hedefe sahiptir — (a) besleme üssü $\alpha$ (sığ 0,5–0,75), (b) beslemeden bağımsız biçim
  eğimi (rotmod −0,04 / RAR.mrt +0,05; veri-ürünü uzlaşması dahil), (c) öz-tutarlılık yasağı
  (taban çıkmamalı). Bir türetim bu üçünü birden vermek zorundadır.

## 4. Dürüstlük kayıtları

1. $\alpha$ taraması yedi noktalıdır ve tek küresel üstür — galaksi başına hiçbir şey
   fitlenmemiştir; ama $\alpha$'nın kendisi bu veriden okunmuş bir tercih olurdu, bu yüzden
   [aday] etiketiyle sınırlandı ve resmî denklem değiştirilmedi.
2. RMS farklarının anlamlılığı test edilmedi (noktalar galaksi içinde bağımlı); 0,35 km/s'lik
   fark bu belirsizlik içinde küçüktür — karar bunu "zayıf" saymaktadır.
3. E'nin dışlanması kalibrasyona dayanmaz: taban ihlali analitiktir ($g_{bar}\to0$ limitinde
   $g\to k\,a_0$) ve herhangi bir $k$ için en düşük gözlem noktalarıyla çelişir; kalibre $k$
   yalnız ihlalin büyüklüğünü (×22) sayısallaştırır.
4. Bu tarama Claude Fable 5 tarafından koşulmuş ve karar verilmiştir; hipotez kullanıcınındır.
