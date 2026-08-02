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
| [`85_TUTARLILIK_YASASI`](85_TUTARLILIK_YASASI/CALISMA.md) | **Sınıf bandının mekanizması** — [$N_c$ türetildi](85_TUTARLILIK_YASASI/NC_TURETIM.md): **kafes = atom çekirdeği**, pencere $[X,\langle A\rangle]$ parametresiz, band içinde; $M_{tut}\approx X m_n$ %15. [$\lambda$ denemesi](85_TUTARLILIK_YASASI/LAMBDA_TURETIM.md): $\sqrt{N}$ **teoremleşti** (polarizasyon $<3\times10^{-35}$), aday: kaskad karakteri; S0/BCD'ye $\lambda<1$ çağrısı. [σ sınavı](85_TUTARLILIK_YASASI/SIGMA_SINAVI.md): $n=18$'de **ilk anlamlı işaret** $+0{,}49$ ($p=0{,}02$); [kayıt-öncesi $n=99$ denemesi](85_TUTARLILIK_YASASI/KAYIT_ONCESI_PROTOKOL.md) geçerlilik kapısında durdu (W-farkı kestiricisi geçersiz) | 148 galaksi · 8 grup | fit yok |
| [`86_NIHAI`](86_NIHAI/CALISMA.md) | ⚡ **NİHAİ KURULUM KARARI** — yerel $\ell_\omega$ + $a_0$; **PENCERELİ resmî denklem (M-47):** $a_0=7{,}67\times10^{-11}$, RMS **12,48** < ΛCDM 14,56 (penceresiz 12,79) | 9 ölçüt · 4 kurulum | — |
| [`87_ETKIN_YASA`](87_ETKIN_YASA/CALISMA.md) | **MOND mirasının eritilmesi** — kimlik: nihai denklem $g=g_{bar}+\sqrt{g_{bar}a_0}$, Milgrom ailesinin *mekanizmalı* üyesi ($\nu=1+y^{-1/2}$ F1+F4'ten çıkar); miras defteri ölçüldü (BTFR eğim 3,734 band içi + norm 0,984 ✅, RAR medyan −0,003 ✅); devralınamayan tek parça: **geçiş biçimi** (+0,051 kalıntı → F1+F4 toplanma türetimi); ayrışma karnesi A1–A7 (görelilik ✅ M-44 · kozmik $a_0$ 6/6 dışlandı ✅ · ortam kanalı ilk işaret ✅; geniş-çift hesabı ✅ ≲$10^{-4}$ koşullu · EFE sınavı kapıda durdu (uygulanamaz) ⛔ · küme ⏳); [besleme sınavı](87_ETKIN_YASA/BESLEME_SINAVI.md): $M_{kaps}$↔$g_{bar}$ okumaları diskte ayrışıyor — 6.5.4.4'e şerh; [vortisite kararı](87_ETKIN_YASA/VORTISITE_KARARI.md): kısmi ağırlık sığ aday, öz-tutarlı besleme ×22 taban ihlaliyle **kesin dışlandı** — F4'ün kaynağı maddenin dolanımı; [toplanma türetimi](87_ETKIN_YASA/TOPLANMA_TURETIMI.md): basit toplam lineerlikten **türetildi** [T-koşullu], kayma hipotezi reddedildi; [sınıf-içi sınav](87_ETKIN_YASA/SINIF_ICI_SURUKLENME.md): sürüklenme galaksi-İÇİ ($-0{,}074$), sınıflar-arası $\approx0$ — λ aklandı; [pencere türetimi](87_ETKIN_YASA/PENCERE_TURETIMI.md): Rankine iç kolu + $r_0=\ell_\omega$ → $W=\min(1,a_0/g_{kaps})$ **[T-aday]** — sürüklenme $\approx0$, RMS 12,48; **RESMİLEŞTİ (M-47)** — defter 12,48; RAR eğimi ≈0; yüksek-z 5/6; λ/σ ayakta; [basınç-destekli köprü](87_ETKIN_YASA/KOPRU_TURETIMI.md) **TÜRETİLDİ (M-48)**: küresel sistemler diskle aynı yasada, $v_c=\sqrt2\sigma$, Faber–Jackson $\sigma^4=\mathcal{G}M_{bar}a_0/4$ — Fornax 17,8≈18 km/s; [EFE terimi](87_ETKIN_YASA/EFE_TURETIMI.md) **TÜRETİLDİ (M-49)**: $W_{dış}=\min(1,\sqrt{g_{kaps}/g_{ext}})$, tam-baskında $\mathcal{G}_{etkin}=\mathcal{G}(1+\sqrt{a_0/g_{ext}})$ — EFE'li Fornax 10,5–14,9 (gzl ~11–12); [dSph sınavı](87_ETKIN_YASA/DSPH_SINAVI.md): **M-48+$a_0$ örneklem-dışı GEÇTİ** (Yerel Grup, 28 sistem, medyan $+0{,}009$, sıfır kalibrasyon), M-49 büyük uydularda lehte işaret; [MIGHTEE](87_ETKIN_YASA/MIGHTEE_SINAVI.md): **ikinci bağımsız aile GEÇTİ** (n=57, sıfır-nokta band içinde, sıfır kalibrasyon); [gradyan denemesi](87_ETKIN_YASA/GRADYAN_DENEMESI.md): kazanımlar gerçek ama temel değil (RMS-optimalde eşitlik; $f_{geo}$ imzası yok) — P resmî, G1 ölçülmüş-alternatif; [eliptik dış-σ](87_ETKIN_YASA/ELIPTIK_SIGMA.md): **üçüncü bağımsız aile GEÇTİ** (SLUGGS n=22, medyan +0,051/−0,004 dex, sıfır kalibrasyon) — M-48 [T] koşulu sağlandı | tespit + analitik $\nu$ tablosu | fit yok |
| [`88_TARAMA`](88_TARAMA/CALISMA.md) | Galaksi başına açığı ne öngörüyor? — 14 değişken tarandı, **NULL SONUÇ** | 141 / 38 galaksi | fit yok |
| [`89_KAFES`](89_KAFES/CALISMA.md) | **Kafes yasası, yoğun rejimde** — yazarın iddiası ölçüldü; 2,6 kat bastırma, ölçülen yönde | 2728 nokta, 137 galaksi | fit yok |
| [`90_YUKSEK_Z`](90_YUKSEK_Z/CALISMA.md) | **Teorinin ilk SPARC dışı sınavı** — $a_0$ kozmik zamanla değişiyor mu? Kozmik okuma 6/6 dışlandı; **pencereli yeniden koşum (M-47): 5/6 bant içi**, yoğun-rejim açığı kapandı | 6 galaksi, $z=0{,}85$–$2{,}38$ (Genzel+2017) | **fit yok, kalibrasyon yok** |
| [`91_A0_KOPRU`](91_A0_KOPRU/CALISMA.md) | $a_0$'ın son serbestliği — iki yol; [Yol 1 aday kapanışı](91_A0_KOPRU/YOL1_KAPANIS.md): $u_r/v_t=\sqrt{m_p/m_e}$ → $a_0=\mathcal{G}m_nm_e/(m_pr_n^2)$, %1 isabet, **[T-aday]** — Blok H'ye işlendi (**M-45**; $(C,q_n)$ sayısallaştı); [eş-güç TÜRETİLDİ](91_A0_KOPRU/ESGUC_ISPAT.md) (36 mertebe marj); [C↔M-1 köprüsü](91_A0_KOPRU/C_HAL_KOPRUSU.md): $C\ell_\omega/\rho_0c=4{,}2\times10^{-39}$; **χ-yayılım terimi yazıldı (M-46)** — kütle-itim eylemden çıkar, $C=-(\partial P/\partial\chi)_\rho$; kalan: $C$'nin değerinin mikro türetimi + bağımsız $\ell_\omega$ + hakem | cebir + türetim | — |
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
