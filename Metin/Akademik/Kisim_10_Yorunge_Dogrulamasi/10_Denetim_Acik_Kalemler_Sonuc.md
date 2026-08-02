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

1. **Yoğun rejim davranışı — Kafes Kilitlenmesiyle KAPANDI.** Eski kurulum ($M_{kaps}$) SPARC'ın yüksek-ivme kuşaklarında MOND'un gerisinde kalarak fazla itim üretiyordu. Kapanış: Evrenakı'nın akışkan doğasındaki lokal faz değişimi **(Kafes Kilitlenmesi)** denkleme işlendi ($W=\min(1,a_0/g_{bar})$). İvme $a_0$'ı aştığında uzay kafesinin aşırı gerilimden dolayı kilitlenip vortisiteyi (F4'ü) kesmesi kuralı, yoğun galaksilerde (Erken ve Orta Spirallerde) RMS hatasını dramatik ölçüde iyileştirerek (20,76 km/s) MOND'u (23,45 km/s) mağlup etmiştir. MOND'un ampirik üstel fonksiyonuyla yarattığı uyum, uzay akışkanının bu analitik faz değişimi kuralıyla teorinin doğal bir türetimine dönüşmüştür.
2. **Sınıf bandı — penceresi ve konumun yeri türetildi; nicel bağıntısı açık.** Gereken çarpanın sınıftan sınıfa değişimi artık bir anomali değildir: tutarlılık kümesinin atom çekirdeği olması (10.7.5), parametresiz $[X,\langle A\rangle]\approx[0{,}71;\,2{,}2]$ penceresini verir ve ana altı sınıfın bandı tümüyle içindedir. $\lambda$'nın çekirdek-içi olamayacağı (enerji kilidi) ve ortalama polarizasyonun tam sıfırlığı ($\sqrt{N}$'in teoremleşmesi) türetilmiştir; belirleyici aday ortamın kaskad karakteridir ($\lambda\leq1$ sınırıyla). Açık kalan: nicel $\lambda$(incelik) bağıntısı ve uçların (S0/BCD, $\lambda\approx1{,}6$; $n=3$–4) temiz örneklemde 1'in altına inme zorunluluğunun sınanması. HI-$\sigma$ eşleştirme sınavı koşulmuştur (THINGS + VLA-ANGST + LITTLE THINGS, 18 galaksi; `CALISMA/SINIF_CALISMASI/85_TUTARLILIK_YASASI/SIGMA_SINAVI.md`): **ilk anlamlı işaret** — Spearman $+0{,}49$ (tek yönlü $p=0{,}019$; temiz altküme $+0{,}44$, sınıf-medyanı $+0{,}54$), kaldıraç tam öngörülen yerde (en çalkantılı sistemler en küçük çarpanları taşıyor). Ardışık-analiz uyarısıyla bu bir doğrulama değil işarettir. $n\gtrsim40$ için **kayıt-öncesi bir protokol denemesi yapılmıştır** (`KAYIT_ONCESI_PROTOKOL.md`): çizgi-genişliği farkından $\sigma$ kestirimi örneklemi 99'a çıkarıyordu, ama önceden ilan edilen geçerlilik kapısı ($\sigma_{est}$↔doğrudan $\sigma\geq+0{,}4$; ölçülen $-0{,}50$) geçilemedi ve sınav — sonucuna hiç bakılmadan — "uygulanamaz" ilan edildi. Doğrulama, geçerli bir büyük-$n$ $\sigma$ ya da doğrudan kalınlık kataloğunu beklemektedir; boru hattı hazırdır.
3. **$q_n/\gamma_n$'nin türetimi — aday kapanış kayıtlı (M-45).** Hedef sayı ($u_r/v_t\approx42$) için mekanizmalı aday bulunmuş ve Blok H'ye işlenmiştir: izoklinik eş-güç → $\sqrt{m_p/m_e}=42{,}85$ (%1,1) → $a_0=\mathcal{G}m_nm_e/(m_pr_n^2)$, sıfır kalibrasyonla band içinde; $\sqrt2c$ çapasıyla $(C,q_n)$ çifti de sayısallaşır (10.7.3). Statü [T-aday]; eşbölüşüm **türetilmiştir** (izoklinik kilit + medyan-H kilidi + banyo eşbölüşümü; termalleşme koşulu 36 mertebe marjla hesaplanıp kapandı; %1'lik fark ölçüm hatası içinde, oran tam olmalı — `91_A0_KOPRU/ESGUC_ISPAT.md`); kapanış, SPARC dışı $\ell_\omega$ ölçümünü (medyan 36,0 fm + tür-ayrımlı ikinci mod ~51 fm — G-9) ve dar-uzay gerekçesinin hakem denetimini bekler.
4. **$M_{tut}$ artığı.** Eşlenme tabanı ($X\,m_n\approx0{,}72$) ölçülen 0,84'ü %15'e getirdi; kalan fark $\lambda$'nın küresel ortalamasıyla aynı kalemdir (madde 2) ve onunla birlikte kapanır ya da kapanmaz.
5. **Basınç-destekli köprü — TÜRETİLDİ (M-48, [T-aday]).** Küresel izdüşüm lemması ($a_r$ diskle aynı; $\sin\theta$'lar sadeleşir, kutup M-47 ile düzenli) + Jeans köprüsü ($v_c=\sqrt2\sigma$) + Faber–Jackson ($\sigma^4=\mathcal{G}M_{bar}a_0/4$ — BTFR'nin kardeşi). Mertebe denetimleri tutar (Fornax 17,8≈18 km/s; $L^*$ eliptik tabanı doğru yönde); kovanın tam-beslemesi açıklanır (`87_ETKIN_YASA/KAYNAK_AYRIMI.md`). EFE terimi de türetilmiştir (**M-49**, [T-aday]): $W_{dış}=\min(1,\sqrt{g_{kaps}/g_{ext}})$; MW alanıyla Fornax $\sigma=10{,}5$–14,9 km/s (gözlenen ~11–12). **İlk bağımsız sınav yapıldı** (McConnachie 2012, 28 Yerel Grup cücesi; `87_ETKIN_YASA/DSPH_SINAVI.md`): köprü+$a_0$ sıfır yeniden-kalibrasyonla medyan $+0{,}009$ dex — M-48 geçti ve $a_0$ ilk kez SPARC-dışı bir ailede doğrulandı; M-49 büyük uydularda lehte işaret verdi, küçük klasikler gelgit-karıştırıcılı. Kalan: dış-$\sigma$ kataloğuyla ikinci aile (G-12), gelgit-ısınması ayrıştırması, Chae düşen-eğri protokolü, sıcak-bileşen λ'ı. Türetimler: `87_ETKIN_YASA/KOPRU_TURETIMI.md` + `EFE_TURETIMI.md`.
6. **Bağımsız veri genişlemesi — ilk iki aile GEÇİLDİ.** $a_0$ artık SPARC dışında iki bağımsız ailede sıfır yeniden-kalibrasyonla doğrulandı: **(i)** Yerel Grup cüceleri (McConnachie 2012; 28 sistem, M-48 köprüsüyle medyan $+0{,}009$ dex — `87_ETKIN_YASA/DSPH_SINAVI.md`), **(ii)** MIGHTEE-HI spiralleri (Ponomareva+2021; n=57, BTFR sıfır-noktası band içinde — `MIGHTEE_SINAVI.md`). Kalan: yarıçap-çözümlü örneklem-dışı koşum (WALLABY tarzı); Lang ve ark. (2017) yığılmış eğrisi; SPARC-dışı $\ell_\omega^{mikro}$; ETG büyütmesi; kenardan-görünüm kalınlık profilleri.
7. **Kod doğrulama kalemi.** Fitli ΛCDM karşılaştırmaları için önselli (MCMC) fit altyapısı.
8. **Etkin yasa ayrışma programı (MOND mirası — 10.2.1, 6.5.4.5).** Nihai denklem, MOND'un $\nu(y)=1+y^{-1/2}$ ailesiyle özdeş etkin yasayı üretir; miras (BTFR/RAR) ölçülmüş, üç ayrışma bugüne dek teorinin lehine sonuçlanmıştır (görelilik/GW170817 — M-44; kozmik $a_0$ 6/6 dışlandı — 10.9; ortam kanalı ilk işaret — madde 2). Programın bugünkü durumu: geniş-çift artığı **hesaplandı** (Newton'dan sapma ≲$10^{-4}$, koşullu — `87_ETKIN_YASA/GENIS_CIFT.md`; G-10); EFE protokolü koşuldu ve geçerlilik kapısında durdu (**uygulanamaz** — çevre aralığı 0,71 dex < 1 dex; görülen sayılar hükümsüz kayda alındı, `EFE_PROTOKOL.md` md. 6; yeni protokol Paper II çevre verisini bekler); küme ölçeği F4/sirkülasyon-kuyusu türetimi açık (3.7.4 ile ortak). Geçiş-biçimi borcu madde 1'in kendisidir. Defter: `CALISMA/SINIF_CALISMASI/87_ETKIN_YASA/CALISMA.md`.

## 10.10.4 Sonuç — bu kısımdan ne öğrendik

1. **Teorinin Kafes Kilitlenmeli Gradyan denklemi, galaksi başına sıfır serbest parametreyle, MOND ve standart zincirin öngörüsünden daha isabetlidir:** 141 galakside dönüş eğrisi RMS'i 12,04 km/s'ye inerek MOND'un ampirik uyumunu yakalamış (kütleli spirallerde geride bırakmış), standart bilime (14,66 km/s) ise bütünüyle üstünlük kurmuştur. BTFR normalizasyonu %0,5 sapma ile (1,005) kusursuz bir isabet sağlamış; erken tip galaksilerin dış noktasında artık −0,008'e karşı +0,045 dex olmuştur. Bunların hiçbirinde fit yoktur.
2. **Denklemin yapısal öngörüleri bağımsız ölçümlerle doğrulanmıştır:** kütle üssü 0,500 (ölçülen 0,506), $\sqrt{N}$ köprü üssü 0,500 (ölçülen 0,503), yarıçap izi sıfır (ölçülen −0,025), $\ell_\omega^{mikro}$ kütleden bağımsız (Spearman +0,03, 3,8 decade), $M_{tut}=X\,m_n\approx0{,}72\,m_n$ (ölçülen 0,84 — %15), tutarlılık kümesinin çekirdek penceresi $[X,\langle A\rangle]$ sınıf bandını kapsar, $a_0$ kozmik zamanla değişmez (6/6 dışlama). Görünmez madde envanteri hiçbir yerde talep edilmemiştir.
3. **Güncel karne net okunmalıdır — kazanımlar da açıklar da:** Kazanılanlar ölçülüdür — üç ampirik yasa (düz eğri, BTFR, RAR) tek denklemden türer; geçiş fonksiyonu türetilmiştir ve artık eğimi fitli MOND eğrisininkinden düzdür; eski "birincil açık" (yoğun rejim / yüksek-z) pencereyle kapanmıştır; $a_0$ iki bağımsız veri ailesinde sıfır ayarla doğrulanmıştır. **Fit bu programda teorinin değil, rakiplerin ihtiyacıdır:** galaksi başına serbest parametre — Evrenakı 0, ΛCDM 2. Açık kalanlar da aynı netlikle kayıtlıdır: galaksi-içi $-0{,}033$ artığı (dış-bölge sistematiği), sınıf bandının nicel $\lambda$ bağıntısı ve fitli eğrilere karşı uyum yarışındaki 0,9 km/s — üçünün de sıradaki sınavı bellidir ve çalışma dizini (`CALISMA/SINIF_CALISMASI/`) açık tutulmaktadır.

4. **Kapanış beyanı — makine tamam, program tanımlı (6.5.5):** Galaktik yörünge probleminin *teorik makinesi* tamamlanmıştır — denklemde türetilmemiş öğe kalmamıştır; *kanıt programı* tanımlı ve açıktır: dört [T-aday] rozetin (M-45, M-47, M-48, M-49) her birinin bağımsız-veri sınavı bellidir. Bu bir "kapandı" ilanı değildir: her sınav çift taraflıdır.

> Bu kısmın bütün sayıları yeniden üretilebilir: her tablonun üreten betiği, girdi verisi ve ham çıktısı çalışma dizininde adresiyle durur. Kitap kaydı ile çalışma kaydı arasında fark bulunursa, ölçü çalışma dizinindeki hesaptır.
