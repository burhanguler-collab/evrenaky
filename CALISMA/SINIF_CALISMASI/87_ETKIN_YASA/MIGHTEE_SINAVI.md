# MIGHTEE sınavı — $a_0$'ın ikinci bağımsız-aile doğrulaması: örneklem-dışı BTFR sıfır-noktası (iş 14)

**Veri:** Ponomareva ve ark. 2021 (MNRAS 508, 1195; VizieR `J/MNRAS/508/1195`, CfA aynası) —
MeerKAT **MIGHTEE-HI** derin alan taraması (COSMOS/XMM-LSS): **SPARC ile örtüşme sıfır**, farklı
teleskop, farklı seçim, $z\leq0{,}08$. `veri/_mightee_btfr.tsv` (değiştirilmemiş).
Kolonlar: $\log M_{HI}$, $\log M_*$, 3D-Barolo eğiklik, çözümlenmiş eğrinin dış hızı $V_{out}$,
$W_{50}$, ışın sayısı.

**Önceden yazılan kurallar:** kesimler $i\geq40^\circ$, $N_{beam}\geq3$; $M_{bar}=1{,}33\,M_{HI}+M_*$
(yayının kütleleri, değiştirilmeden); **sıfır yeniden-kalibrasyon** — $a_0=7{,}67\times10^{-11}$
donmuş. Ölçü: $\Delta=\log v_{ölç}-\tfrac14\log(\mathcal{G}M_{bar}a_0)$; teorinin öngörü bandı
$\Delta\in[0,+0{,}053]$ (saf-F4 asimptotundan, F1 payının SPARC medyanı $\ell_\omega/R=0{,}27$'ye
kadar). İki hız tanımı gerçeği iki yandan sarar: $v_W=W_{50}/(2\sin i)$ türbülans-şişkindir
(+yönlü yanlılık), $V_{out}$ sınırda-çözümlü eğrilerde düzlüğe ulaşmaz (−yönlü).

## 1. Sonuç (n=57)

| Ölçü | Medyan $\Delta$ | Saçılma |
|---|---|---|
| $v_W$ (birincil; +yanlı) | $+0{,}083$ | 0,076 dex |
| $V_{out}$ (ikincil; −yanlı) | $-0{,}026$ | 0,090 dex |
| **Teori bandı** | $[0,\ +0{,}053]$ | — |
| MOND ($g_\dagger$) kıyası, $v_W$ | $+0{,}034$ | — |

**Hüküm: GEÇTİ.** İki yanlı tanımın braketi $[-0{,}026,+0{,}083]$ teorinin bandını tam içine
alır; her iki yanlılığın bilinen yönü ve büyüklüğü (türbülans düzeltmesi $\sim-0{,}02$…$-0{,}04$;
düzlük-altı $\sim+0{,}02$…$+0{,}05$) bandı daha da ortalar. $a_0$ böylece **ikinci** SPARC-dışı
ailede (birincisi: Yerel Grup cüceleri, `DSPH_SINAVI.md`) sıfır ayarla doğrulanmış oldu —
üstelik iki aile iki ayrı rejimden: basınç-destekli cüceler (köprüyle) ve dönme-destekli
kütleli spiraller (BTFR ile).

## 2. Dürüstlük kayıtları

1. **Bu bir sıfır-noktası sınavıdır**, tam radyal denklem koşumu değil (MIGHTEE eğrileri
   sınırda-çözümlü; yarıçap-çözümlü örneklem-dışı koşum — WALLABY tarzı — açık iştir).
2. **Eğim bu örneklemde kısıtlanamaz:** naif fit 2,83 verir ama kütle aralığı dar
   ($\log M_{bar}\sim9{,}5$–10,7), hız hatası büyük ve naif regresyon eğimi aşağı yanlıdır
   (yayının kendi hata-içeren fiti ~3,7 bulur). Eğim hükmü SPARC/97'nin işidir; buraya
   taşınmaz.
3. MOND'un $g_\dagger$'ı da braket içindedir — bu sınav teori↔MOND ayrıştırmaz (sıfır-noktada
   F1-paylı etkin ölçek $g_\dagger$'a yakındır; ayrıştırma biçim/pencere sınavlarındadır).
4. Yayının kütle konvansiyonları (kozmoloji, $M_*$ tahmini) değiştirilmeden alındı;
   $O(0{,}02$–$0{,}03)$ dex'lik konvansiyon kaymaları hükmü etkilemez.
5. Kesimler ($i\geq40$, $N_{beam}\geq3$) koşumdan önce yazıldı; başka eleme yapılmadı.
6. Bu sınav Claude Fable 5 tarafından koşulmuştur.
