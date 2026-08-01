# 10.10 Kod Doğrulaması, Açık Kalemler ve Sonuç

## 10.10.1 Kod doğrulaması — kendi ΛCDM tarafımızın denetimi

*(Hesap: `CALISMA/kod_dogrulama.py` · kayıt: `98_KOD_DOGRULAMA/` · referans: Li ve ark. 2020, `WP50_M200.mrt`)*

Bu programdaki ΛCDM tarafının tamamı kendi implementasyonumuzdur ve "kodumuz doğru" varsayımı sınanmadan bırakılamazdı. Sınav: fitlediğimiz $M_{200}$ değerleri, SPARC ekibinin **yayınlanmış** halo fitleriyle (163 ortak galaksi) karşılaştırıldı.

![Kod doğrulama](Gorseller/k10_dogrulama.png)

| Ölçüt | Değer |
|---|---|
| Pearson $r$ (log–log) | +0,758 |
| Medyan fark | −0,12 dex |
| **Saçılma** | **0,82 dex** |
| Ölçek: yayınlanmış modeller arası fark (NFW↔Einasto) | 0,25 dex |

**Hüküm aleyhtedir ve saklanmaz: fit implementasyonumuz yayınlanmış NFW fitlerinin sadık bir yeniden üretimi değildir.** Saçılma, halo modelini komple değiştirmenin yarattığından 3–5 kat büyüktür. Sebep tespit edilmiştir: yayın MCMC + önsellerle fit eder, bizim kurulum önselsiz en küçük karelerdir; düşük kütleli cücelerde $\Upsilon_*$–$M_{200}$ dejenerasyonu önselsiz fitte tabana çöker (en büyük altı sapmanın hepsi cüce ve hepsi aynı yönde).

Bu denetimin sonuçlara etkisi sınırlıdır ama kayıt zorunludur: **öngörü karşılaştırmaları etkilenmez** (öngörü tarafında fit yoktur; $M_{200}$ abundance matching'ten gelir), fitli $\chi^2$ karşılaştırmalarında ise ΛCDM tarafımız cüce uçta yayının vereceğinden farklı davranabilir. Fitli hükümler bu çekinceyle okunmalıdır.

## 10.10.2 $\Upsilon_*$ bandı denetimi

*(Hesap: `CALISMA/upsilon_bant_nihai.py` · 169 galaksi)*

Teorinin denklemi $a_0$ küresel sabitken galaksi başına tek serbest parametre taşır: $\Upsilon_*$. O parametre fiziksel bandına hapsedilirse ne olur?

| $\Upsilon_*$ aralığı | Evrenakı ($k=1$) medyan $\chi^2_{ind}$ | ΛCDM ($k=2$) |
|---|---|---|
| Serbest (0,05–3,0) | 3,41 | 1,90 |
| **Popülasyon sentezi (0,3–0,8)** | 4,91 | 2,49 |
| **Bozulma** | **%44** | **%32** |

Serbest fitte medyan $\Upsilon_*=0{,}49$ çıkar — tam fotometrik beklentide; model $\Upsilon_*$'ı sistematik şişirmez ve bant dayatıldığında bozulma iki modelde aynı mertebededir. **Teori bu sınavda dışlanmaz.** Kalan gerçek fark uyum kalitesindedir (bant altında 4,91'e karşı 2,49) — bir parametre eksiğiyle çalışmanın bedeli. Bandın kendisi tartışılamaz: teorinin kendi $\gamma_N/m=1/\rho_n$ bağıntısı, ışık→nükleon dönüşümünü ışık→kütle dönüşümüne evrensel bir çarpanla bağlar; teori "$\Upsilon_*$ bandı bana ait değil" diyemez.

## 10.10.3 Açık kalemler — konsolide liste

Programın bütün sınavlarından geriye kalan gerçek kalemler şunlardır (her biri 7.4 madde 12'nin envanterine bağlıdır):

1. **Yoğun rejim davranışı — birincil açık.** İki bağımsız veri kümesi aynı şeyi söyler: SPARC'ın yüksek-ivme kuşaklarında ve $z\sim2$ disklerinde teori fazla itim üretir (yüksek-$z$ $f_{DM}$ artığı $+0{,}19$; radyal ivme biçim artığı $+0{,}051$ dex/dex). Eleme zinciri adresi daraltmıştır: kaynak F4'ün genliği değildir (en yoğun uçta baryonlar tek başına aşar), $\Upsilon_*$ değildir; ayakta kalan kanal ortamın/baryon tarafının yoğun-rejim davranışıdır. Gereken türetim: F1 ile F4'ün **toplanma biçimi** (şu an $a_{tam}=a_{F1}+a_{F4}$ varsayılıyor) ve yoğun paketlenmenin dolanıma etkisi.
2. **Sınıf bandı: 0,113 dex.** Gereken $a_0$ çarpanı sınıftan sınıfa ×0,65–1,53 (uçlarla ×2,7–4,4) değişir; uzaklık hatası bunun yalnız %26'sını açıklar, 14 değişkenin hiçbiri öngörmez, Sd–Im zıtlığı basit ivme etkisini dışlar. Teorinin diliyle bu, $\mathcal{G}=\alpha/\rho_n$'nin (ve $a_0$'ın) galaksiden galaksiye gerçek değişkenliğinin ölçüsü olabilir — nicelleşmesi $\rho_n(\Sigma_{bar})$ yasasını bekler.
3. **$q_n/\gamma_n$'nin türetimi.** Kalan tek galaktik serbestlik; hedef sayı bellidir ($\approx7\times10^{-14}$ m; hız oranı diliyle $u_r/v_t\approx42$). Nükleonun ortamdaki kaynak modeli yazılmadan kapanmaz.
4. **$M_{tut}$ katsayı defteri.** Ölçülen 0,84 $m_n$ ile öngörülen $m_n$ arasındaki fark, türetim katsayılarının ($2\pi$, $4\pi$, hizalanma dağılımı) defterinden kapatılmalı ya da kapanmadığı gösterilmelidir.
5. **Basınç-destekli köprü.** Eliptiklerin yıldız kinematiği ve cüce küreseller teorinin geçerlilik alanı dışındadır; F1+F4'ün küresel izdüşümü ve $v_c\leftrightarrow\sigma$ köprüsü türetilmeden oraya uzanılamaz (6.5.4.9).
6. **Bağımsız veri genişlemesi.** Lang ve ark. (2017)'nin 101 galaksilik yığılmış yüksek-$z$ eğrisi; SPARC dışı $\ell_\omega^{mikro}$ ölçümü ($a_0$'ın [S]→[T] geçişinin anahtarı); ETG kümesinin büyütülmesi; $R_f$/dış-bölge sistematiği için kenardan-görünüm kalınlık profilleri.
7. **Kod doğrulama kalemi.** Fitli ΛCDM karşılaştırmaları için önselli (MCMC) fit altyapısı.

## 10.10.4 Sonuç — bu kısımdan ne öğrendik

1. **Teorinin galaktik denklemi, galaksi başına sıfır serbest parametreyle, standart zincirin öngörüsünden daha isabetlidir:** 141 galakside dönüş eğrisi RMS'i 12,79'a karşı 14,56 km/s; öngörü yarışı 79/141; BTFR eğimi gözlenen bandın içinde (ΛCDM zinciri dışında); erken tip galaksilerin dış noktasında artık −0,008'e karşı +0,045 dex. Bunların hiçbirinde fit yoktur.
2. **Denklemin yapısal öngörüleri bağımsız ölçümlerle doğrulanmıştır:** kütle üssü 0,500 (ölçülen 0,506), $\sqrt{N}$ köprü üssü 0,500 (ölçülen 0,503), yarıçap izi sıfır (ölçülen −0,025), $\ell_\omega^{mikro}$ kütleden bağımsız (Spearman +0,03, 3,8 decade), $M_{tut}=m_n$ (ölçülen 0,84 $m_n$), $a_0$ kozmik zamanla değişmez (6/6 dışlama). Görünmez madde envanteri hiçbir yerde talep edilmemiştir.
3. **Ve teori kazanmış değildir — açıkları adresleriyle kayıtlıdır:** yoğun rejimde fazla itim (SPARC dışı sınavda niceliksel başarısızlık), sınıf bandı, ve uyum-kalitesi yarışında fit altında ΛCDM'in üstünlüğü. Program bu kalemleri gizlemek yerine eleme zinciriyle daraltmıştır; her birinin sıradaki sınavı bellidir ve çalışma dizini (`CALISMA/SINIF_CALISMASI/`) o sınavlar için açık tutulmaktadır.

> Bu kısmın bütün sayıları yeniden üretilebilir: her tablonun üreten betiği, girdi verisi ve ham çıktısı çalışma dizininde adresiyle durur. Kitap kaydı ile çalışma kaydı arasında fark bulunursa, ölçü çalışma dizinindeki hesaptır.
