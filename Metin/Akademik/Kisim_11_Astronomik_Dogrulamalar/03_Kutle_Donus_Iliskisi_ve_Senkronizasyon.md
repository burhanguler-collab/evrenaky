# 11.3 Kütle-Dönüş İlişkisi ve Yörünge Senkronizasyonu (Kilitlenme)

Standart gök mekaniği, Ay gibi uyduların neden gezegenlerine kilitlendiğini veya gezegenlerin eksenel dönüş hızlarının neden uzayla yavaşladığını "Gelgit Sönümlemesi" veya "Dinamik Sürtünme" ile modeller. Evrenakı teorisinde bu kilitlenme (senkronizasyon) ve uydu göçü, Zerre sürtünmesinin yarattığı **artık kuplaj** ve vorteks profil dengesinin kaçınılmaz matematiksel çıktısıdır (Bkz. Ek M-37).

## 11.3.1 Vorteks Profil Teoremi

Gezegen etrafındaki dönüş vorteksinin hızı serbest değildir. Kütlenin çevresinde sürtünme zarfı yaratan Evrenakı akışkanı (Zerre Katarı), merkezkaç ivmesiyle dışarı savrulmamak için kendi radyal dengesini sağlamak zorundadır:

$$\frac{dP}{dR} = \rho\,\frac{v_\theta^2}{R} \quad\Longleftrightarrow\quad \bigl|a_{radyal}(R)\bigr| = \frac{v_\theta^2}{R}$$

Sürüklenme zarfı nedeniyle uydu bu akışkana hapsolur ($v_{y\ddot{o}r} = v_\theta$). Kepler rejiminde (radyal kütle-itim ivmesi $|a| = \frac{\mathcal{G}M}{R^2}$ alındığında) hız profili doğal olarak çözülür:

$$\boxed{\;v_\theta(R) = \sqrt{R\,\bigl|a_{radyal}(R)\bigr|} = \sqrt{\frac{\mathcal{G}M}{R}}\;}$$

Bu, klasik yörünge hız profilinin, kütleçekiminden bağımsız bir akışkan dengesi olarak yeniden türetilmesidir.

## 11.3.2 Gevşeme Zamanı ($\tau_{ret}$) ve Sürüklenme Rejimi

Uydu ile Evrenakı girdabı arasında bağıl bir hız ($\Delta v$) oluşursa, akışkan Stokes biçimli bir artık kuplaj (sürtünme kuvveti) uygular:
$$F_{s\ddot{u}r} = 6\pi\,\eta_E\,a_b\,\Delta v \;\Longrightarrow\; \frac{d(\Delta v)}{dt} = -\gamma_{s\ddot{u}r}\Delta v$$

Burada $a_b$ uydu yarıçapı, $\eta_E$ Evrenakı viskozitesi (sönüm katsayısı) ve $\gamma_{s\ddot{u}r} = \frac{6\pi\eta_E a_b}{m}$ ivmelenme çarpanıdır. Uydu kütlesi $m=\tfrac43\pi a_b^3\rho_c$ kullanılarak, yörüngenin denge düzlemine (ekvatora) gevşeme zaman ölçeği ($\tau_{ret}$) türetilir:

$$\boxed{\;\tau_{ret} = \frac{1}{\gamma_{s\ddot{u}r}} = \frac{2\,\rho_c\,a_b^{2}}{9\,\eta_E}\;}$$

Bu tek denklem, Güneş Sistemi mimarisinin neden bugünkü "gevşemiş" hâlinde olduğunu izah eder:
1. **Eş Düzlemlilik:** Yörünge eğikliği ($i \ne 0$) olan uydular, $\tau_{ret}$ süresi içinde sistemin ana ekvator düzlemine oturur.
2. **Dairesellik:** Eksantrik yörüngeler daireselliğe sönümlenir.
3. **Kilitlenme:** Cisimler sürüklenme zarfı içinde akıntıyla eş-dönüşe zorlanarak kilitlenir (Tidal Locking).

## 11.3.3 Senkron Yarıçap ve Uydu Göçü (Phobos/Triton)

Yörüngedeki kütle, yerel bir basınç çukuru (gradyan lobu) taşır. Yörünge kilitlenmesi sonrasında, uydunun kaderi (içeri düşmesi veya dışarı açılması) ana gövdenin (gezegenin) dönüş açısal hızı ($\omega_{g\ddot{o}vde}$) ile uydunun açısal hızı ($\omega_{uydu}$) arasındaki yarışa bağlıdır. Sınır çizgisi, **senkron yarıçaptır**.

- **Senkron Üstü Rejim (Ay, Deimos):** Eğer $\omega_{g\ddot{o}vde} > \omega_{uydu}$ ise, gezegenin yüzey hızı uydudan fazladır. Gelgit şişkinliği ve gradyan lobu uydunun **önüne** geçer. Lob, uyduya ileri yönde kinetik enerji aktarır. Uydu dışarı sarmal çizer (Örn. Ay yılda ~3.8 cm uzaklaşır).
- **Senkron Altı Rejim (Phobos, WASP-12b):** Eğer $\omega_{g\ddot{o}vde} < \omega_{uydu}$ ise, uydu gezegenden hızlı dolanmaktadır. Lob geride kalır ve uyduyu frenler. Yörünge bozunur, uydu içe göçer (Örn. Phobos Mars'a yaklaşır).
- **Retrograd Yörünge (Triton):** Lob daima karşı yönde kalır ve sönüm çok agresiftir. Triton sistemdeki en belirgin içe göç vakasıdır.

*(Not: Retrograd uyduların bugüne dek hayatta kalması, $\eta_E$ sönüm katsayısının inanılmaz derecede küçük olduğunu kanıtlar. Phoebe verisi $\eta_E$'nin suyun viskozitesinin otuzda biri kadar küçük olması gerektiğini gösterir.)*
