# 1. Kurucu İlkeler ve Semboller

## 1.1 Amaç ve kapsam

Evrenakı, üç uzaysal boyut ve ortak zaman parametresi üzerinde tanımlanan sürekli bir fiziksel ortam modeli olarak ele alınır. Bu başlangıç, uzay-zaman eğriliği veya Lorentz dönüşümlerini varsaymaz. Buna karşılık teori; kendi içinde iyi tanımlı başlangıç-değer problemi, boyutsal tutarlılık, kararlılık ve enerji-momentum muhasebesi sağlamak zorundadır.

## 1.2 Temel alanlar

| Sembol | Tanım | SI boyutu |
|---|---|---|
| \(\rho(\mathbf x,t)\) | Evrenakı kütle/eylemsizlik yoğunluğu | kg m\(^{-3}\) |
| \(\mathbf u(\mathbf x,t)\) | ortam hızı | m s\(^{-1}\) |
| \(P(\rho)\) | izotropik mekanik basınç | Pa |
| \(\chi(\mathbf x,t)\) | madde kaynaklı deplasman potansiyeli | m\(^2\) s\(^{-1}\) |
| \(n(\mathbf x,t)\) | nükleon sayı yoğunluğu | m\(^{-3}\) |
| \(q_n\) | tek nükleonun \(\chi\)-kaynak şiddeti | m\(^3\) s\(^{-1}\) |
| \(C\) | \(\chi\)–basınç kuplajı | kg m\(^{-3}\) s\(^{-1}\) |
| \(v_\chi\) | deplasman alanının karakteristik yayılma hızı | m s\(^{-1}\) |
| \(\rho_n\) | maddenin etkin basınç-tepki yoğunluğu | kg m\(^{-3}\) |

\(\chi\)'nin boyutu, \(\nabla^2\chi=-q_n n\) seçimiyle sabitlenmiştir. Böylece \(C\chi\) basınç boyutundadır.

## 1.3 Asgari postülalar

**EA-P1 [P] — Sürekli ortam.** Evrenakı'nın yerel durumu en az \((\rho,\mathbf u)\) alanlarıyla tanımlanır.

**EA-P2 [P] — Yerel barotropik tepki.** İzotropik ortam basıncı, temel sürümde \(P=P(\rho)\) bağıntısına uyar. Küçük bozuntular için

\[
c_s^2(\rho)=\frac{dP}{d\rho}>0.
\]

Bu koşul mekanik kararlılık için gereklidir. \(c_s^2=P/\rho\) genel bir özdeşlik değildir; yalnız seçilen hâl denklemi bunu ayrıca sağlarsa kullanılabilir.

**EA-P3 [P] — Madde kaynak alanı.** Madde, \(\chi\) alanına \(q_n n\) ile kaynaklık eder.

**EA-P4 [P] — Atomik pompa ve basınç kuyusu.** Maddenin atomik/nükleonik pompaları Evrenakı'yı dışa deplase eder; arka plan Evrenakı ise içe doğru karşı basınç uygular. Durağan denge sürekli radyal akış değil, uzaysal bir basınç profili üretir. Zayıf deplasman rejiminde bu profil

\[
P_{\rm tot}=P(\rho)-C\chi
\]

olarak tanımlanır. Bu eşitlik bir termodinamik hâl denklemi değil, atomik pompa alanı ile arka plan basıncı arasındaki mekanik denge bağıntısıdır.

**EA-P5 [P] — Kütle-itim.** Evrenakı basıncı cismin bütün yüzeyine normal yönde etkir. Dış basınç iç taraftan daha büyük olduğunda yüzey kuvvetlerinin toplamı düşük basınçlı merkeze yönelir. Küçük ve yapı değişimine uğramayan bir test cisminin ivmesi

\[
\mathbf a=-\frac{1}{\rho_n}\nabla P_{\rm tot}
\]

ile tanımlanır. Bu mekanizma çekme değil, yüksek basınç tarafından düşük basınca doğru **kütle-itim**dir. Yasanın yüzey basıncı integralinden geçişi Dosya 5'te gösterilmiştir; etkin hacmin mikro-türetimi açık iştir.

## 1.4 Bağımsızlık ve gözlemsel dürüstlük

Bu çekirdekte \(G\), Lorentz çarpanı, metrik, eğrilik tensörü veya Einstein alan denklemleri başlangıç girdisi değildir. Newton tipi ters-kare davranış da postüla değildir; \(\chi\) alan denkleminin üç boyutlu statik Green fonksiyonundan çıkacaktır.

Öte yandan \(q_n,C,\rho_n,v_\chi\) değerlerinin gözlemle belirlenmesi mümkündür. Bir katsayının kalibre edilmesi kusur değildir; aynı verinin hem kalibrasyon hem bağımsız doğrulama olarak kullanılması kusurdur.
