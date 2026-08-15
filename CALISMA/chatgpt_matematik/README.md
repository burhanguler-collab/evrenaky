# Evrenakı Temel Matematik Programı

Bu dizin, Evrenakı teorisinin GR/SR denklemlerini başlangıç noktası yapmadan kurulacak temel matematik çekirdeğini içerir. Amaç gözlemlerden kaçınmak değil; gözlemsel sonuçlara Evrenakı'nın kendi alanları, etkileşimleri ve hareket yasaları üzerinden ulaşabilecek kapalı bir başlangıç sistemi kurmaktır.

## Dosyalar

1. `01_Kurucu_Ilkeler_ve_Semboller.md` — alanlar, boyutlar, varsayımlar ve statü dili.
2. `02_Eylem_ve_Temel_Alan_Denklemleri.md` — eylem, varyasyon ve temel denklemler.
3. `03_Durgun_Kuresel_Cozum_ve_Kutle_Itim.md` — noktasal/küresel kaynak çözümü ve etkin kütle-itim katsayısı.
4. `04_Dalga_Sektoru_ve_Kararlilik.md` — küçük bozuntular, yayılma hızları ve kararlılık koşulları.
5. `05_Madde_Hareketi_Enerji_ve_Korunum.md` — test cismi hareketi, enerji ve momentum muhasebesi.
6. `06_Acik_Uclar_ve_Turetim_Faturasi.md` — henüz türetilmeyen parçalar ve sonraki çalışma sırası.

## Güncel durum

Temel statik çekirdek ve doğrusal dalga sektörü yazılmıştır. Denklem numaraları dosyalar boyunca EA-1–EA-25 aralığında tekildir. Akışkan varyasyonundaki Bernoulli işareti ile \(\chi\) alanının yerel enerji alışverişi işareti, tanımlanan eylemlerle tutarlı olacak biçimde denetlenmiştir.

Paket henüz tam geri-tepkili dinamik teori değildir. Sıradaki ana çalışma, atomik pompa etkisini, arka plan karşı basıncını ve madde geri tepkisini tek bir birleşik eylem altında kapatmaktır. Bu yapılıncaya kadar statik ters-kare sonuç kullanılabilir; fakat dinamik enerji kaybı, yörünge sönümü veya tam enerji-momentum korunumu bağımsız türetim olarak sunulmamalıdır.

## Statü işaretleri

- **[P] Postüla:** Teoriyi tanımlayan başlangıç kabulü.
- **[T] Türetim:** Belirtilen postülalardan matematiksel olarak çıkar.
- **[K] Kalibrasyon:** Değeri deney/gözlemle belirlenen bağımsız katsayı.
- **[Ö] Öngörü:** Kalibrasyonda kullanılmamış ölçülebilir sonuç.
- **[A] Açık:** Henüz kapanmamış kuramsal problem.

Bu sürüm temel katmandır. Geleneksel literatürde “kütleçekimsel kızıla kayma” ve “kütleçekim dalgası” diye adlandırılan gözlemlerle birlikte ışık bükülmesi, Shapiro gecikmesi, jeodetik presesyon, çerçeve sürüklenmesi ve Lorentz-simetrisi deneyleri daha sonra **gözlemsel sınama katmanı** olarak ele alınacaktır. Bu adlar yalnız gözlemsel literatürle eşleştirme içindir; GR/SR açıklamaları burada postüla veya türetim girdisi değildir. Evrenakı'nın merkezcil kuvvet mekanizmasının adı **kütle-itim**dir.
