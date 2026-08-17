# Kısım 8 Tam Denetim Raporu ve Uygulama Planı

EvrenAKI Kısım 8 (Matematiksel Ekler) dosyaları üzerinde "Ontolojik Uygunluk ve GR/SR Kalıntı Denetimi" tamamlanmıştır. Teori omurganız olan "c yerel değişkendir, zaman mutlak/saatler yereldir, kütleçekim yoktur" prensiplerine uymayan, standart fizikten bulaşmış matematiksel ifadeler tespit edilmiştir.

Bu plan, tespit edilen kalıntıları temizlemek ve sistemi EvrenAKI tabanına oturtmak için önerilen değişiklikleri içerir.

## User Review Required

> [!IMPORTANT]
> Aşağıdaki müdahaleler, teorinin matematiğini temelden arındıracaktır. Lütfen özellikle **Schwarzschild karadelik** tanımının ve **c² yerine c_0²** kullanımının her yerde (örneğin $\xi$ türetiminde) değiştirilmesini onaylayın.

## Open Questions

> [!WARNING]
> **Soru 1:** `18_5_Kuvvet_Matematigi.md` içinde jeodezik presesyon (Thomas yarısı) mekanik olarak türetilecek mi, yoksa şimdilik sadece "bu bir GR kalıntısıdır, mekanik açıklaması açık uçtur" notuyla mı bırakılacak? (Mevcut metinde "Adım 3'ün GR eşlemesi" ifadesi var, bu doğrudan dışlanmalı).
> 
> **Soru 2:** Karadelik sınırını Schwarzschild ($R \propto M$) yerine kavitasyon/yırtılma eşiği ($v_{kav}$) üzerinden mi tanımlamalıyız? 

## Proposed Changes

### Matematiksel Sembol ve Terim Arınması (Parti 3)

Matematikte "çıplak c" (c) ve "çıplak G" (G) kalıntıları mevcuttur. Bunlar teoriye "evrensel sabitleri" gizlice geri sokar. Bütün denklemlerde EvrenAKI versiyonlarıyla değiştirilecekler.

#### [MODIFY] 18_5_Kuvvet_Matematigi.md
- **$\xi$ (Çerçeve Sürüklenmesi) Türetimindeki Çıplak c²:** 
  - Mevcut: $\xi = \frac{2GI}{c^2R^3}$
  - Yeni: $\xi = \frac{2\mathcal{G}I}{c_0^2R^3}$
- **Schwarzschild Karadelik Sınırı:**
  - Mevcut (Satır 1173): "Schwarzschild yarıçapı ise $\propto M$'dir; ikisi tek bir kütlede kesişir:"
  - Yeni: Çıplak c'ye dayanan Schwarzschild sınırı kaldırılarak, teorinin kendi mutlak sınırı olan **Kavitasyon Eşiği ($v_{kav}$)** veya **Kafes Kilidi** vurgulanacak.
- **Jeodezik Presesyon (Adım 3 GR Eşlemesi):**
  - Mevcut: "Bu, Adım 3'ün GR eşlemesinin verdiği değerin birebir aynısıdır"
  - Yeni: Adım 3'teki rölativistik kinematik atfı (Thomas yarısı vb.) teori içine alınacak veya dışarıdan alındığı açık bir uyarı (Açık Uç) ile belirtilecek.
- **Zaman / Kızıla Kayma Kavramı:**
  - $\frac{\delta f}{f} = -\frac{\Phi}{c_0^2}$ denklemi civarındaki "Zaman Genleşmesi" çağrışımları temizlenecek (Zaman mutlak, yavaşlayan lokal saat mekanizmasıdır vurgusu artırılacak).

#### [MODIFY] 19_Ek_M_Blok_I_Eylem_Ilkesi.md
- Çıplak `c^2` kullanımı temizlenecek: $P_0=\frac{1-k}{4}\rho_n c^2 \to P_0=\frac{1-k}{4}\rho_n c_0^2$

#### [MODIFY] 17_Ek_B_Arka_Plan_Basinci.md
- Çıplak `c^2` kullanımı temizlenecek: $\rho_0 = P_0/c^2 \to \rho_0 = P_0/c_0^2$

#### [MODIFY] 13_Ek_M_Blok_E_Doppler_Kizila_Kayma.md
- Çıplak `c^2` kullanımı: $\Lambda \equiv 1 - \Phi/c^2 \to \Lambda \equiv 1 - \Phi/c_0^2$
- "Kütleçekimsel kızıla kayma" isminin sadece **standart fiziğin gözlem adı** olduğu, teorideki karşılığının **kütle-itim yoğunluk gradyanı** üzerinden saat yavaşlaması (mekanik yavaşlama) olduğu güçlü şekilde vurgulanacak.

#### [MODIFY] 12_Ek_M_Blok_D_Optik_Fizeau.md
- Denklemdeki çıplak `c` temizlenecek: $\delta(\Delta\varphi)=-\frac{2\omega}{c^2}\,(L_1-L_2)\,\delta c \to \delta(\Delta\varphi)=-\frac{2\omega}{c_0^2}\,(L_1-L_2)\,\delta c_{loc}$

#### [MODIFY] 09_Ek_M_Blok_A_Temel_Yasalar.md
- Bernoulli formülündeki $v^2 = 2c^2\ln\frac{\rho_0}{\rho}$ denklemi $v^2 = 2c_0^2\ln\frac{\rho_0}{\rho}$ olarak (veya $c_{loc}$ kullanılarak) düzeltilecek.

## Verification Plan

### Manual Verification
- Kısım 8 dosyalarında `c^2` araması yapılarak sonuç sayısının (standart fizik referansları hariç) sıfıra inip inmediği kontrol edilecek.
- `G ` ve `G/` araması yapılarak teorik denklemlerde $\mathcal{G}$'nin kullanıldığı doğrulanacak.
- GR ve "uzay-zaman" ifadelerinin sadece standart fizikle karşılaştırma kısımlarında yer alıp almadığı (ontolojik bağlamdan yalıtıldığı) kontrol edilecek.
