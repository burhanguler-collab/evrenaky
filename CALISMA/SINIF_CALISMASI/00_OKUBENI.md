# Sınıf Çalışması — kuruluş ve kurallar

Bu klasör, galaktik dönüş eğrisi çalışmasını **morfolojik sınıf sınıf** yürütmek için kurulmuştur.
Yapıyı üreten betik: `kur_sinif_calismasi.py` (bu klasörün bir üstünde). Betik yeniden koşulduğunda
yapı sıfırdan kurulur, yani **kuruluş tekrarlanabilirdir.**

## Neden sınıf sınıf

Örneklem bloğu hâlinde bakıldığında ters yönlü davranışlar birbirini götürüyor. Ölçüldü: aynı
büyüklük (fitlenen $\Upsilon_*$'ın fotometrik bandın dışında kalma oranı) spiral sınıfında %44,
Macellan sınıfında %91 çıkıyor. Blok ortalaması ikisini de gizler. Bu nedenle **hiçbir sonuç blok
hâlinde verilmez;** sınıf sınıf verilir, blok ortalaması yalnız yanında özet olarak durur.

## Sınıflar

| Klasör | Tip | SPARC T | Galaksi | Ölçüm noktası |
|---|---|---|---|---|
| `01_erken_spiral` | Sa – Sab | T=1,2 | **12** | 632 |
| `02_orta_spiral` | Sb – Sbc | T=3,4 | **29** | 640 |
| `03_gec_spiral` | Sc – Scd | T=5,6 | **30** | 730 |
| `04_cok_gec_spiral` | Sd | T=7 | **16** | 300 |
| `05_macellan` | Sdm – Sm | T=8,9 | **28** | 423 |
| `06_duzensiz` | Im | T=10 | **26** | 272 |
| `99_KARMASIK` | ayrım yapılamayanlar | — | **32** | 348 |
| ↳ [`07_S0_BCD`](07_S0_BCD/CALISMA.md) | S0 · BCD | T=0,11 | **8** | *99_KARMASIK içinden ayrıştırıldı* |

### Sınıf dışı sınavlar

Aşağıdakiler morfolojik sınıf değil, **ayrı veri kümeleri** üzerinde kurulmuş sınavlardır:

| Klasör | Ne | Veri | Fit |
|---|---|---|---|
| [`86_NIHAI`](86_NIHAI/CALISMA.md) | ⚡ **NİHAİ KURULUM KARARI** — yerel $\ell_\omega$ + $a_0=1{,}75\times cH_0/16{,}1$; toplu defter: **8 iyileşti / 1 kötüleşti**, RMS 12,79 < ΛCDM 14,56 | 9 ölçüt · 4 kurulum | — |
| [`88_TARAMA`](88_TARAMA/CALISMA.md) | Galaksi başına açığı ne öngörüyor? — 14 değişken tarandı, **NULL SONUÇ** | 141 / 38 galaksi | fit yok |
| [`89_KAFES`](89_KAFES/CALISMA.md) | **Kafes yasası, yoğun rejimde** — yazarın iddiası ölçüldü; 2,6 kat bastırma, ölçülen yönde | 2728 nokta, 137 galaksi | fit yok |
| [`90_YUKSEK_Z`](90_YUKSEK_Z/CALISMA.md) | **Teorinin ilk SPARC dışı sınavı** — $a_0$ kozmik zamanla değişiyor mu? | 6 galaksi, $z=0{,}85$–$2{,}38$ (Genzel+2017) | **fit yok, kalibrasyon yok** |
| [`91_A0_KOPRU`](91_A0_KOPRU/CALISMA.md) | $a_0$'ın son serbestliği — iki yol denendi ve karşılaştırıldı | cebir + türetim | — |
| [`92_M_TUT`](92_M_TUT/CALISMA.md) | **Tutarlılık kütlesi türetildi** — $M_{tut}=m_n$; $\ell_\omega$ mikro sabit olarak ölçüldü (35,7 fm) | 133 galaksi | **sıfır serbest parametre** |
| [`93_G_YEREL`](93_G_YEREL/CALISMA.md) | **$\mathcal{G}$ yerel mi?** — teorinin değişkenlik iddiasının sınavı | 737 nokta, 110 galaksi | fit yok |
| [`94_YEREL_LOMEGA`](94_YEREL_LOMEGA/CALISMA.md) | **$\ell_\omega$ yerel kütleden kurulmalı** — kurulum tutarsızlığı | 141 galaksi | **yeni parametre yok** |
| [`07_S0_BCD`](07_S0_BCD/CALISMA.md) | mercek ve tıkız cüce — örneklemin iki ucu | 8 galaksi (99_KARMASIK'ın kaydı) | **yeni fit yok** |
| [`95_RAR`](95_RAR/CALISMA.md) | radyal ivme bağıntısı — teorinin **biçimi** sınanıyor | 2693 nokta, 3,9 decade (Lelli+2017) | yapılmadı |
| [`96_ETG`](96_ETG/CALISMA.md) | erken tip galaksiler — radyal ivme düzlemi | 16 galaksi, 32 ivme noktası (Lelli+2017) | **yapılamaz** (2 nokta/galaksi) |
| [`97_BTFR`](97_BTFR/CALISMA.md) | baryonik Tully-Fisher | 121 galaksi (Lelli+2019) | yapılmadı |
| `98_KOD_DOGRULAMA` | betiklerin kendi denetimi | — | — |

## Ölçütler

Bir galaksi, aşağıdakilerden **en az biri** geçerliyse `99_KARMASIK`'a konur:

1. Dönüş eğrisinde $N<6$ nokta
2. SPARC kalite bayrağı $Q=3$ (düşük)
3. Eğiklik $i<30°$ (yüz-üstü — $V_{obs}=V\sin i$ kötü belirlenir)
4. Kendi Hubble tipi sınıfında $N<5$ galaksi kalıyor (S0, BCD)

Her karmaşık galaksinin hangi ölçütten düştüğü `99_KARMASIK/GEREKCE.csv`'de yazılıdır.

## Veri türü ayrımı — bu klasörün en önemli kuralı

| Klasörde ne VAR | Klasörde ne YOK |
|---|---|
| **Ölçülen** dönüş eğrileri (SPARC Rotmod_LTG, değiştirilmemiş) | Bu çalışmanın fit sonuçları |
| **Yayınlanmış** katalog büyüklükleri (Lelli+2016 Tablo 1) | Türetilmiş model parametreleri ($\Upsilon_*$, $M_{200}$, $b$, $R_f$ …) |
| Her sütunun nasıl ölçüldüğü (`OKUBENI.md`) | $\chi^2$, AIC, BIC gibi uyum ölçütleri |

**Gerekçe:** sınıf klasörleri **girdi** klasörleridir. Buradaki her sayının kaynağı bir yayındır ve
ölçüm yöntemi o yayında belgelidir. Bizim hesapladığımız hiçbir şey buraya karışmaz — karışırsa
girdi ile çıktı ayrımı kaybolur ve sonuçlar denetlenemez hâle gelir.

Bu çalışmanın kendi hesapları `_HESAPLAR/` altında, her biri kendi klasöründe ve üreten betiğin
adıyla birlikte tutulur.

## Tek dosyada tüm sınıflama

`00_SINIFLAMA.csv` — **173** galaksinin tamamı (yerel `Rotmod_LTG` kümesinin tamamı), hangi
sınıfa girdiği ve neden. Sütunlar:
`Galaksi, Tip_T, Tip_ad, Sinif, N_nokta, Q, Inc_deg, D_Mpc, Vflat_kms`

## Kaynak

Lelli F., McGaugh S. S., Schombert J. M., 2016, **AJ 152, 157** — *SPARC: Mass Models for 175 Disk
Galaxies with Spitzer Photometry and Accurate Rotation Curves.* Ana katalog: `veri/_sparc.mrt`.
Dönüş eğrileri: `Rotmod_LTG`.
