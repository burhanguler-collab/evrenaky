# 6. Açık Uçlar ve Türetim Faturası

## 6.1 Bu pakette gerçekten elde edilenler

1. **[T]** Süreklilik ve Euler denklemleri, seçilen akışkan eyleminden elde edildi.
2. **[T]** Sıkışma dalgası hızı \(c_s^2=dP/d\rho\) olarak elde edildi.
3. **[T]** \(\chi\) için hiperbolik alan denklemi ve statik Poisson sınırı elde edildi.
4. **[T]** Üç boyutta küresel kaynaktan \(\chi\propto1/r\) sonucu elde edildi.
5. **[T|P]** EA-P4 ve EA-P5 kabul edildiğinde ters-kare ivme yasası türetildi.
6. **[T]** Etkin katsayı
   \[
   \mathcal G_{\rm EA}=\frac{Cq_n}{4\pi\rho_nm_n}
   \]
   olarak bulundu.
7. **[T]** Deplasman alanının enerji yoğunluğu ve enerji akısı yazıldı.

## 6.2 Henüz türetilmeyen temel girdiler

| Konu | Statü | Eksik iş |
|---|---|---|
| Hâl denklemi \(P(\rho)\) | [P/A] | zerre ölçeğinden mikro-türetim |
| \(P_{\rm tot}=P-C\chi\) | [P] | ortak eylemde yerel ve karşılıklı kuplaj |
| \(\mathbf a=-\nabla P_{\rm tot}/\rho_n\) | [P] | sonlu cismin yüzey gerilimi integralinden türetim |
| \(q_n\) | [K/A] | bağımsız fiziksel tanım ve ölçüm |
| \(C\) | [K/A] | bağımsız ölçüm; aynı veriyle doğrulama yapılmaması |
| \(\rho_n\) evrenselliği | [P/A] | bileşim ve bağlanma enerjisi hesabı |
| \(v_\chi\) | [K/A] | dinamik deneyle sınama |
| Zerre çözümü | [A] | sonlu enerjili, tekilsiz, kararlı çözüm |
| Vortisite/dönüş | [A] | Clebsch değişkenleri veya yönelim alanıyla eyleme ekleme |
| Eylemsizlik | [A] | geri-tepki çekirdeği ve düşük frekans sınırı |

## 6.3 Kritik kuramsal sorunlar

### A. Kuplajın çift sayılması

\(-C\chi\)'yi hem basınca ekleyip hem de ayrıca madde potansiyeli olarak kullanmak enerji etkileşimini iki kez sayabilir. Nihai toplam eylem bu belirsizliği gidermelidir.

### B. İşaret ve pozitif enerji

Merkez yönlü kütle-itim için kaynak, alan ve madde kuplajının işaretleri birlikte kontrol edilmelidir. Cismin yüksek basınçtan düşük basınçlı merkeze itilmesi, etkin bağlanma enerjisinin negatif olması ve serbest alan kinetik enerjisinin pozitif kalması aynı anda sağlanmalıdır.

### C. Atomik pompa–arka plan dengesinin eylemde kapatılması

Teorinin fiziksel kabulü şudur: atomik pompalar Evrenakı'yı dışa deplase ederken arka plan Evrenakı içe doğru basınç uygular; sonuç sürekli akış değil, durağan bir basınç gradyanıdır. Bu denge Dosya 2'de

\[
-\nabla P_{\rm tot}+\mathbf f_{\rm pompa}=0
\]

olarak yazılmıştır. Kütle-itim, dengedeki ortamın topluca akmasından değil, test cisminin karşı yüzlerindeki dış basınçların eşitsizliğinden doğar. Açık kalan iş mekanizmanın varlığı değil; \(\mathbf f_{\rm pompa}\)'nın ve karşı gerilmenin aynı birleşik eylemden türetilmesidir.

### D. Güçlü alan ve doğrusal olmayanlık

Poisson ve doğrusal kuplaj yalnız zayıf alan çekirdeğidir. Kuvvetli kaynaklarda \(P>0\), \(\rho>0\), sonlu enerji ve nedensel/kararlı evrim korunmalıdır.

## 6.4 Sonraki matematik çalışma sırası

1. **Birleşik madde–ortam eylemi:** atomik pompa, arka plan karşı basıncı ve durağan gradyanı aynı varyasyon ilkesinden çıkar.
2. **Sonlu zerre modeli:** noktasal delta kaynak yerine yarıçapı ve iç alanı olan kararlı çözüm kur.
3. **Etkin hacmin mikro-türetimi:** yüzey basıncı integralinden EA-P5'e geçiş Dosya 5'te gösterildi; şimdi \(V_{\rm etk}/m=1/\rho_n\) bağıntısını zerre yapısından çıkar.
4. **Eylemsizlik ve geri tepki:** ivmelenen zerrenin alan çözümünü ve etkin kütlesini hesapla.
5. **Vortisite sektörü:** dönme, makro girdap ve yönelim değişkenlerini eyleme ekle.
6. **Gözlemsel katman:** temel parametreler tek bir kalibrasyon kümesiyle sabitlendikten sonra kızıla kayma, ışık yolu, zaman gecikmesi, presesyonlar, hareket simetrisi ve dalga hızı için Evrenakı'na özgü ölçüm denklemleri çıkar.

## 6.5 Yayın dili için bağlayıcı kural

Bir denklem başka bir gözlemsel kuramın sonucuyla aynı biçimdeyse “Evrenakı'dan türetildi” denebilmesi için o denklem Evrenakı postülaları ve eyleminden çıkmalıdır. Bilinen katsayıyı hedefleyerek seçilen ansatz **[K]**, bağımsız öngörü **[Ö]**, henüz kanıtlanmamış fiziksel yorum **[P]** olarak etiketlenmelidir.
