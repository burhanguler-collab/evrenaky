# 10.9 SPARC Dışı Sınav — Yüksek Kırmızıya Kayma Diskleri

*(Hesap: `CALISMA/yuksek_z_sinavi.py` · veri: `CALISMA/veri/_genzel2017_tablo1.csv` — Genzel ve ark. 2017, Nature 543, 397'nin Tablo 1'inden elle aktarılmış · kayıt: `90_YUKSEK_Z/`)*

## 10.9.1 Bu sınav neden özel

Programın bütün diğer sonuçları tek bir veri ailesinden okunur: SPARC ve türevleri. Kitabın kendi en ağır özeleştirisi de budur (7.4 madde 12: türetimler sınandıkları veriden okunuyor; öngörü statüsü kazanılmadı). Genzel ve ark. (2017)'nin altı büyük yıldız-oluşturan diski ($0{,}85<z<2{,}38$) bu programa **hiç girmemiştir**: kalibrasyon yok, fit yok, ayar yok. Teori ne diyorsa o.

Üstelik sınav bir **ayırt edicidir.** $a_0$'ın iki okuması yüksek kırmızıya kaymada kesin ayrışır, çünkü $H(z{=}2)\approx3H_0$:

| Okuma | $a_0(z)$ |
|---|---|
| **Kozmik** ($a_0\propto cH(z)$) | $H$ ile büyür — $z=2$'de üç kat |
| **Sabit/mikro** ($a_0=\mathcal{G}m_n/\ell_\omega^2$) | değişmez |

## 10.9.2 Yöntem — kütle modeli gerekmez

Evrenakı'da karanlık madde yoktur; Genzel'in ölçtüğü "karanlık madde payı" teoride **F4'ün payıdır**: $f_{DM}=v_{F4}^2/v_c^2$. Nihai denklemin yerel biçimi kapalı çözüm verir — girdi olarak yalnız ölçülmüş $v_c$ ve $R$ gerekir; kütle modeli, $\Upsilon_*$, disk geometrisi, eğiklik girmez.

İki denetim önceden yapılmıştır: (1) tablo doğru okunmuş mu — Genzel'in kendi sayıları iki bağımsız yoldan çapraz tutarlıdır (medyan oran 1,07; küresel yaklaşımın beklenen payı); (2) **yerel çapa** — aynı formül, aynı $a_0$, SPARC'ın 140 galaksisinde eğrinin orta yarıçapında öngörülen ile ölçülen $f_{DM}$ arasında yalnız $+0{,}05$ fark verir. Formül $z\approx0$'da doğru mertebeyi tutturur; yüksek-$z$'de görülen her sapma evrimden ya da yüksek-$z$'ye özgü fizikten gelir.

## 10.9.3 Sonuç

| Galaksi | $z$ | gözlenen $f_{DM}$ | SABİT okuma | KOZMİK okuma |
|---|---|---|---|---|
| COS4 01351 | 0,854 | 0,21 (0,11–0,31) | 0,40 | 0,47 |
| D3a 6397 | 1,500 | 0,17 (<0,38) | 0,36 | 0,50 |
| GS4 43501 | 1,613 | 0,19 (0,10–0,28) | 0,36 | 0,50 |
| zC 406690 | 2,196 | 0,00 (<0,08) | 0,33 | 0,51 |
| zC 400569 | 2,242 | 0,00 (<0,07) | 0,23 | 0,37 |
| D3a 15504 | 2,383 | 0,12 (<0,26) | 0,35 | 0,54 |

![Yüksek kırmızıya kayma sınavı](Gorseller/k10_yuksek_z.png)

| Okuma | Yayının üst sınırını aşan | Ortalama sapma |
|---|---|---|
| **Kozmik** | **6/6** | $6{,}1\sigma$ |
| **Sabit** | 5/6 | $3{,}3\sigma$ |

## 10.9.4 Hüküm — iki parça, biri lehte biri aleyhte

**(a) Ayırt edici çalıştı: kozmik okuma dışlandı.** $a_0\propto cH(z)$ yazımı altı galaksinin altısında yayının üst sınırını aşar ve her galakside sabit okumadan kötüdür. **$a_0$ kozmik zamanla değişmez** — 10.7'nin mikro-bileşke sonucunun bağımsız veriyle doğrulanmasıdır; $cH_0$ ile bugünkü sayısal örtüşme rastlantıdır.

**(b) Ama sabit okuma da ortalamada fazla öngörür — ve bu ciddidir.** Kazanan okumada nihai kurulumun $f_{DM}$ artığı $+0{,}19$ dex'tir; yerel çapanın payı düşüldüğünde bile gerçek bir yüksek-$z$ açığı kalır. **Teorinin ilk SPARC dışı sınavı niceliksel olarak başarısızdır** — bu satır yumuşatılmaz; sonucun yarısı budur. Fiziksel adresi 10.8'in bulgusuyla örtüşür: bu sıkı, yoğun, çalkantılı disklerde ($v/\sigma\sim3$–5) teori gereğinden çok F4 üretir — açık $a_0$'ın değerinde değil, **yoğun rejimin davranışındadır** ve teorinin kayıtlı tek büyük açığıdır.

## 10.9.5 Dürüstlük kayıtları

1. **Genzel'in $f_{DM}$'si model bağımlıdır** (NFW + disk + kovan fitinin çıktısı); öngörümüz yalnız $v_c$ ve $R$ kullanır ama karşılaştırıldığı sayı onların kütle modelinden gelir.
2. **Altı galaksi seçilmiştir** — en kütleli, en iyi gözlenen, yüksek yüzey yoğunluklu uç; bu, teorinin aşımını abartıyor olabilir. Lang ve ark. (2017)'nin 101 galaksilik yığılmış eğrisi bu yanlılığı kırar ve **işlenmemiştir** (açık iş).
3. **Basınç desteği ciddidir** ($v/\sigma\sim3$–5); Genzel'in $v_c$'si düzeltmeyi içerir, ama M-37 dairesel yörünge için kuruludur — düzeltilmiş $v_c$'yi ona vermek bir varsayımdır.
4. **Üst sınırlı dört galakside** artık üst sınıra göre hesaplanmıştır — teoriye en elverişli okuma; gerçek $f_{DM}$ daha küçükse aşım daha büyüktür.
5. **$H(z)$ için ΛCDM genişleme geçmişi kullanılmıştır**; sabit okuma bundan etkilenmez ($H$ hiç girmez), kozmik okumanın eğrisi Evrenakı'nın kendi genişleme geçmişiyle değişebilir.
6. **Tablo elle aktarılmıştır**; iç tutarlılık denetimi geçilmiştir ama ikinci bir göz denetlememiştir.
