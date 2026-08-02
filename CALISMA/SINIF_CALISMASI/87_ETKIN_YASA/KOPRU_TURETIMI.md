# Basınç-destekli köprü türetimi — küresel izdüşüm lemması + Jeans köprüsü (iş 11)

**Hedef:** 6.5.4.9'un iki açık işi: **(a)** F1+F4'ün küresel simetrideki izdüşümü ("F4'ün
silindirik akı kanalı disk gerektirir; küresel sistemde karşılığı nedir?"), **(b)** dairesel
hız ↔ hız dağılımı ($v_c\leftrightarrow\sigma$) köprüsünün teori içinde kurulması. İkisi de
aşağıda kurulur; sonuç **M-48** olarak kataloğa işlenmiştir.

---

## 1. LEMMA — küresel izdüşüm: silindirik yasa, küresel sistemde aynı radyal yasayı verir

M-38'in kuvveti eksene yönelir; büyüklüğü $\sqrt{\mathcal{G}M_{kaps}a_0}/R_{sil}$
($R_{sil}=r\sin\theta$: eksene dik uzaklık). Eksene-dik birim vektörün küresel ayrışımı
$\hat R_{sil}=\sin\theta\,\hat r+\cos\theta\,\hat\theta$ olduğundan **radyal** bileşen:

$$a_r \;=\; \frac{\sqrt{\mathcal{G}M_{kaps}\,a_0}}{r\sin\theta}\cdot\sin\theta
\;=\; \boxed{\;\frac{\sqrt{\mathcal{G}M_{kaps}\,a_0}}{r}\;}\qquad\text{— her enlemde, tam disk-düzlemi değeri.}$$

$\sin\theta$'lar tam sadeleşir: **küresel sistem, diskle aynı radyal yasaya uyar** (cebirsel;
sayısal doğrulama betik çıktısında, dört enlem birebir). İki tamamlayıcı kayıt:

- **Kutup ıraksaması yoktur:** $\hat\theta$-bileşeni $\propto\cot\theta$ kutupta patlar gibi
  görünür; ama M-47 penceresi kolon içinde ($R_{sil}<\ell_\omega$) kuvveti Rankine koluna
  ($\propto R_{sil}$) döndürür — bileşen sonlu kalır. Dispersiyon-destekli sistemde kalıntı
  eksenin yönü rastgeledir (aşağıda) ve $\hat\theta$-bileşenleri yönelim ortalamasında
  sıfırlanır; kalan, yukarıdaki izotrop radyal yasadır.
- **Kaynak tarafı — kovan/izotropik bileşen neden tam besler:** 85'in $\sqrt N$ teoremi
  **dolanım korunumundan** çıkar, düzenli dönme varsaymaz: $N$ nükleonun mikro-dolanımlarının
  vektör toplamı $\sqrt N$ ölçeğinde, yönü rastgele ama büyüklüğü kütleyle belirli bir kalıntı
  bırakır. Düzenli dönme yalnız λ (kaskad tutumu) üzerinden ikinci-mertebe fark yaratır.
  **Birinci mertebede dolanım-destek kesri 1'dir** — `KAYNAK_AYRIMI.md`'nin iki bulgusunun
  (kovan-baskında tam katkı zorunlu; ılımlıda küçük bastırma izi) türetilmiş açıklaması.
  96_ETG'nin ölçülmüş başarısı (dış nokta $-0{,}003$; disklerle fark 0,013 dex — "One Law")
  de bu lemmanın verili doğrulamasıdır.

## 2. KÖPRÜ — Jeans denklemi ve $v_c=\sqrt2\,\sigma$

İzotropik, durağan sistemde Jeans: $\dfrac{d(\rho_*\sigma^2)}{dr}=-\rho_*\,g(r)$. Dış bölgede
derin rejim ($W=1$, $M_{kaps}\to M_{bar}$): $g=\sqrt{\mathcal{G}M_{bar}a_0}/r$. Sabit $\sigma$
(izotermal dış yapı) ve $\rho_*\propto r^{-\alpha}$ ile:

$$\sigma^2\cdot\alpha=\sqrt{\mathcal{G}M_{bar}a_0}
\qquad\Longrightarrow\qquad
\boxed{\;\sigma^2=\frac{\sqrt{\mathcal{G}M_{bar}\,a_0}}{\alpha}\;}$$

İzotermal kürenin öz-tutarlı üssü $\alpha=2$'dir; teoride düz kolun karesi
$v_c^2=\sqrt{\mathcal{G}M_{bar}a_0}$ olduğundan köprü kapanır:

$$\boxed{\;v_c=\sqrt2\,\sigma\;}$$

— Newtoncu izotermal bağıntının teorideki karşılığı; artık $\sigma$ ölçülen her küresel sistem
için "efektif dairesel hız" **teori içinde** kuruludur.

## 3. SONUÇ — Faber–Jackson türetimi: BTFR'nin basınç-destekli kardeşi

Köprü, BTFR'nin ($v_{flat}^4=\mathcal{G}M_{bar}a_0$) küresel eşleniğini tek satırda verir:

$$\boxed{\;\sigma^4=\frac{\mathcal{G}\,M_{bar}\,a_0}{4}\;}\qquad(\sigma=v_{flat}/\sqrt2)$$

**Biçim** gözlenen Faber–Jackson'dır ($M\propto\sigma^4$) ve sıfır noktası $a_0$ ile kilitlidir
— yeni sabit yok. Taban değerler ($a_0=7{,}67\times10^{-11}$):

| $M_{bar}$ ($M_\odot$) | $\sigma_{taban}$ | $v_c=\sqrt2\sigma$ |
|---|---|---|
| $10^{7}$ | 12,6 km/s | **17,8 km/s** |
| $10^{10}$ | 71 | 100 |
| $10^{11}$ | 126 | 179 |
| $3\times10^{11}$ | 166 | 235 |

**İki mertebe denetimi (fit yok):**
1. **Cüce küresel:** kitabın kendi Fornax kaydı "efektif hız profili $\sim18$ km/s asimptota
   oturur" (6.5.3) — köprünün $M_*\sim10^7$ için verdiği $v_c$ tam **17,8 km/s**. ($M_*$
   belirsizliği 2–4$\times10^7$ bandında 21–25 verir; dış-alan etkisi — MW alanı — değeri
   aşağı çeker, yön doğru. Kesin sınav EFE türetimini bekler, md. 5.)
2. **Eliptikler:** $L^*$ eliptiğin ($M_{bar}\sim2\times10^{11}$) tabanı $\sigma\approx150$;
   gözlenen merkezî $\sigma\approx200$–250. Doğru yönde: merkez $g\gg a_0$ rejimindedir
   ($W<1$, iç kısım saf Newton) ve Newton katkısı tabanın **üstüne** çıkarır; köprünün keskin
   öngörüsü merkez değil, **dış bölgenin düz $\sigma$'sudur** (md. 4).

## 4. Yanlışlanabilir öngörüler (G-12 olarak tabloya)

1. Dönme-destekli olmayan küresel sistemlerin dış $\sigma$-profilleri **düzleşmeli** ve düz
   değer $\sigma^4=\mathcal{G}M_{bar}a_0/4$'e oturmalı (FJ sıfır noktası $a_0$ kilidi).
2. Dış bölgesi hem $\sigma$ hem bağımsız $v_c$ (HI/X-ışını) veren sistemlerde
   $v_c/\sigma\to\sqrt2$.
3. Bu iki sınav SPARC-dışı veri ister (eliptik dış-$\sigma$ katalogları: GC/PNe/X-ışını) —
   veri-edinme kalemi.

## 5. Geçerlilik sınırı ve dürüstlük kayıtları

1. **İzotropi varsayımı:** anizotropiyle ($\beta_J$) Jeans terimi $\alpha\to\alpha-2\beta_J$
   kaydırır; köprünün $\sqrt2$'si izotrop-izotermal yapıya aittir, band $O(1)$'dir.
2. **Dış alan:** MW uydusu cüce küreseller dış-alan-baskın sistemlerdir; köprü onlara ancak
   EFE terimi türetildikten sonra *nicel* uygulanır (A5 kalemi — `EFE_PROTOKOL.md` programı).
   Fornax denetimi bu yüzden "mertebe" etiketiyle sınırlı tutuldu.
3. **λ ikinci-mertebe:** sıcak bileşenin kaskad tutumu diskten küçük olabilir (sınıf bandı
   ölçeğinde, ~0,1 dex); türetilmedi, `KAYNAK_AYRIMI.md` md. 2.2'nin hedefi olarak durur.
4. Merkez ($g\gg a_0$) parçalı rejimdedir (M-47 penceresi); köprünün kutuları dış bölge
   içindir.
5. Bu türetim Claude Fable 5 tarafından yapılmıştır; tetikleyen, KAYNAK_AYRIMI sınavının
   bıraktığı hedeflerdir. Kataloğa **M-48 [T-aday]** olarak işlenmiştir (aday: izotropi ve
   dış-$\sigma$ verisiyle ilk nicel sınav beklenir).
