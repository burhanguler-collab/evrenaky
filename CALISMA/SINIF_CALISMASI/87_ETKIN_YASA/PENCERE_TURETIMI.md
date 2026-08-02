# Pencere türetimi — Rankine yapısı galaktik denkleme uygulandı; sürüklenme sıfırlandı (iş 8)

**Hedef** (`SINIF_ICI_SURUKLENME.md` md. 2.3): geçiş penceresinin türetimi; ölçüsü, galaksi-içi
artık eğimini $-0{,}07$'den sıfıra çekmek. **Yasaklar:** biçim fit edilmeyecek (MOND'un $\nu$'süne
düşmemek), taban doğmayacak, derin limit/BTFR korunacak.

---

## 1. Türetim — yeni hiçbir şey icat edilmedi, kitaptaki iki parça birleştirildi

1. **M-30 (Rankine, türetilmiş):** girdabın iç çekirdeği katı-cisimdir; kuvvet içte $\propto R$,
   dışta $\propto1/R$; iki kol $r_0$'da sürekli eklenir. Bu yapı kitapta vardır ama **galaktik
   denkleme hiç uygulanmamıştı** — resmî denklem $\sqrt{\mathcal{G}M_{kaps}a_0}$'ı her yarıçapta
   açık sayar.
2. **Kitabın kendi özdeşleştirmesi (6.5.4.4 tablosu):** $r_0=\ell_\omega^{etkin}$; yerel yasayla
   $\ell_\omega(R)=\sqrt{\mathcal{G}M_{kaps}(R)/a_0}$.

İkisinin birleşimi, F4 genliğine **parametresiz** bir pencere verir (içte Rankine'in $\propto R$
kolu, $1/R$ biçimine göre $(R/r_0)^2$ çarpanıdır; süreklilik $R=\ell_\omega$'da):

$$\boxed{\;v_{F4}^2=\sqrt{\mathcal{G}M_{kaps}a_0}\cdot W,\qquad
W=\min\!\Big(1,\;(R/\ell_\omega)^2\Big)=\min\!\Big(1,\;\frac{a_0}{g_{kaps}}\Big),
\quad g_{kaps}\equiv\frac{\mathcal{G}M_{kaps}}{R^2}\;}$$

**Fiziksel okunuşu:** $R<\ell_\omega$ iken akı yüzeyi koherent kolonun *içindedir* — silindirik
uzak-alan yasası henüz kurulmamıştır, cisim katı-cisim çekirdeğin basınç yapısını duyar. İkinci
eşitlik pencerenin *kanal-arası bastırma* okunuşudur: $g_{kaps}>a_0$ bölgesinde F4,
$(a_0/g_{kaps})$ ile bastırılır — `TOPLANMA_TURETIMI.md` md. 3'ün aday (i)'si aranan biçimiyle
kendiliğinden çıkmıştır.

## 2. Sonuçlar (141 galaksi; adil kalibrasyon; galaksi başına fit yok)

| Model | $k_{kal}$ | medyan RMS | küresel RAR eğimi | **galaksi-içi eğim** | sınıf bandı |
|---|---|---|---|---|---|
| B (resmî, penceresiz) | 1,011 | 12,76 | −0,043 | −0,074 | 16,1 % |
| **P (Rankine penceresi)** | 1,038 | **12,48** | **−0,002 ≈ 0** | **−0,033** | 16,2 % |
| kontrol: üs 1 | 1,038 | 12,48 | −0,015 | −0,045 | — |
| MOND (fitli $g_\dagger$) | — | 11,59 | +0,027 | −0,021 | — |

Kuşak artıkları: B'nin tekdüze sürüklenmesi (+0,02 → −0,09) P'de düzleşir (tümü $\pm0{,}035$
içinde; en yüksek kuşak $+0{,}001$). Galaksi başına: P, 141'in **84**'ünde B'den iyi.

**Denetim listesi:** taban yok ✓ ($W\leq1$) · derin limit ve BTFR dokunulmadı ✓ ($g_{kaps}\leq a_0$'da
$W=1$) · ölçek değişmezliği korunur ✓ · sınıf bandı değişmedi ✓ (pencere sürüklenmeyi taşır,
bandı λ taşır — `SINIF_ICI_SURUKLENME.md` ayrışmasının bağımsız teyidi) · Güneş Sistemi daha da
güvenli ✓ (iç bastırma $\varepsilon^2$; G-5'in $\varepsilon$ üst sınırı a fortiori sağlanır) ·
$a_0$ kalibrasyonu yalnız %3,8 oynar ($7{,}67\times10^{-11}$ — beş-ölçüm bandının içinde).

**Üs kontrolü:** üs 1 alınsaydı eğimler daha kötü kalırdı (−0,015 / −0,045) — üs veriden
seçilmedi; Rankine'in kendi üssü (2) kazandı. Küresel biçimde P, **fitli MOND'dan bile düzdür**
(−0,002'ye karşı +0,027).

## 3. Hüküm ve statü

- **Pencerenin biçimi türetilmiştir** (M-30 + $r_0=\ell_\omega$ özdeşleştirmesi; sıfır yeni
  parametre) ve üç ölçülmüş hedefin ikisini kapatmıştır: küresel sürüklenme ≈ 0, RMS iyileşti;
  galaksi-içi eğim yarıya indi (−0,074 → −0,033) ama sıfırlanmadı.
- **Statü: [T-aday].** Biçim kitaptaki türetilmiş yapılardan geliyor; ama doğrulaması aynı SPARC
  verisindedir ve $r_0=\ell_\omega^{etkin}$ özdeşleştirmesi kitapta ölçümle (tek galaksi)
  desteklenen bir tespittir, bağımsız türetim değildir. Hakem-öncesi dilde: *resmî denklemin
  eksik uygulanmış kendi yapısı tamamlandı.*
- **Resmî denkleme alınması ayrı karardır** (10.2.1 ve 6.5.4.4'ün kutulu denklemi değişir; bütün
  aşağı-akış sınavları yeniden koşulmalıdır: toplu defter, BTFR, sınıf defterleri, yüksek-z).
  Bu dosya öneriyi kaydeder; onay kullanıcıya sunulmuştur.

## 4. Kalan işler ve dürüstlük kayıtları

1. **Galaksi-içi −0,033 duruyor.** Adaylar: dış-bölge sistematiği ($R_f$/warp kalemi, 6.5.4.6)
   ve Rankine eklemesinin keskin büklümü (gerçek profil yumuşak olabilir — ama yumuşatma biçimi
   türetilmeden **eklenmeyecek**). Sdm-Sm'nin $+0{,}07$'lik aykırı sınıf-içi eğimi pencereden
   sonra yeniden ölçülmelidir.
2. Pencere $\ell_\omega$'nın **yerel** tanımıyla kuruludur (nihai kurulumla tutarlı); toplam-kütle
   tanımı denenmedi (yerel yasa 94'te ölçülmüşken gerekçesiz olurdu).
3. Eğimler EKK/tanımlayıcıdır (nokta bağımlılığı); dört ölçünün **birlikte** iyileşmesi hükmün
   dayanağıdır, tek bir eğim değil.
4. MOND satırı fitli $g_\dagger$ iledir; RMS'te hâlâ önde (11,59) — kaydedilir, gizlenmez.
5. Bu türetim ve sınav Claude Fable 5 tarafından yapılmıştır; hesap bu dosyanın md. 2 çıktısını
   üreten oturum betiğidir (üçlü karşılaştırma `../../` altında betikleştirilecekse
   `pencere_sinavi.py` adıyla eklenmelidir — resmîleşme onayıyla birlikte).
