## HÜKÜM: ÜSTEL YAPI ZAYIF-ALAN KARNESİNİ HİÇBİR KALEMDE KIRMIYOR — 8/8 GEÇER

Betik: `C:\Users\ASUS\AppData\Local\Temp\claude\C--Users-ASUS-Desktop-EvrenAKI-KITAP3\af8a4f91-3ca3-4d3f-8118-deaefaba8858\scratchpad\zayif_alan_denetimi.py` + `ek_kontroller.py` (mpmath, 60 hane; ışın integralleri boyutsuzlaştırılıp $s=b/r$ ile tam çözüldü, seri açılımı kullanılmadı).

---

### (a) IŞIK BÜKÜLMESİ — Güneş kenarı, $b=R_\odot$, $\Phi/c_0^2=2{,}1225\times10^{-6}$

| | $\delta$ (as) | 2. mertebe katsayısı ($\delta=4x+Kx^2$) | GR'dan sapma |
|---|---|---|---|
| birinci mertebe $4\mu/b$ | 1,7511903 | — | — |
| **ÜSTEL** $n=e^{2\mu/r}$ | **1,7512020** | $K=4\pi$ | **+0,730 µas** |
| LİNEER $n=(1-\mu/r)^{-2}$ | 1,7512049 | $K=5\pi$ | +3,649 µas |
| LİNEER-kesim $n=1{+}2\mu/r$ | 1,7511962 | $K=2\pi$ | −2,190 µas |
| GR (Schwarzschild) | 1,7512013 | $K=15\pi/4$ | 0 |

- Mevcut kayıt: **1,7512″** (ölçüm 1,7510″). Üstel: **1,7512020″** — dördüncü haneye kadar **aynı**.
- İkinci mertebe payının büyüklüğü: üstel−lineer $=-2{,}92$ µas; üstel−GR $=+0{,}73$ µas.
- Cassini $\gamma$ bandı ($2{,}3\times10^{-5}$) bükülmede $\pm20{,}14$ µas'a karşılık gelir → **üstel sapma 0,036σ**, lineer 0,18σ. Üstel yapı GR'a **5 kat daha yakın**.
- **KIRILIYOR MU: HAYIR.** Kalibrasyon (M-42 Kısıt 2) da bozulmuyor: $\ln(c_{loc}/c_0)=-2\Phi/c_0^2$ üstel yapıda **tam** (ε=0,1'de bile 20 hane doğrulandı), yani $\gamma_c=-2$ artık birinci mertebe okuma değil özdeşlik.

### (b) SHAPIRO GECİKMESİ — Dünya–Mars teğet, gidiş-dönüş

| | değer |
|---|---|
| kitabın kapalı formu $\frac{4GM}{c^3}\ln\frac{4r_1r_2}{b^2}$ | 247,2440412 µs |
| **ÜSTEL indis (tam integral)** | **247,244019817 µs** |
| LİNEER indis | 247,244085343 µs |
| LİNEER-kesim | 247,243888765 µs |

- Fark: **−65,53 ps** (üstel daha küçük); bağıl $-2{,}65\times10^{-7}$. Analitik pay $2\pi\mu^2/(cb)=65{,}69$ ps ile örtüşüyor.
- Ölçüm kısıtı $2{,}3\times10^{-5}$ bağıl → pay 1σ'nın **%1,2**'si. Mevcut kayıt "≈247 µs" değişmiyor.
- **KIRILIYOR MU: HAYIR.**

### (c) KÜTLEÇEKİMSEL KIZILA KAYMA — GPS + Pound–Rebka

Kapalı biçim türetildi: iki yazımın farkı **tam olarak $(\varepsilon_1^2-\varepsilon_2^2)/2$**.

| | değer |
|---|---|
| $\varepsilon_{yer}=6{,}9613\times10^{-10}$, $\varepsilon_{yör}=1{,}6698\times10^{-10}$, $\Delta=5{,}2915\times10^{-10}$ | |
| birinci mertebe | 45,718213 µs/gün |
| **ÜSTEL** | 45,7182127949 µs/gün |
| LİNEER | 45,7182128147 µs/gün |
| **fark** | $2{,}284\times10^{-19}$ kesirsel = **19,73 fs/gün** |
| üstelin kendi 2. mertebe payı $\Delta^2/2$ | $1{,}400\times10^{-19}$ = 12,10 fs/gün |

- GPS saat kararlılığı $\sim10^{-14}$/gün → pay hassasiyetin **$2{,}3\times10^{-5}$** katı (4–5 mertebe altı).
- Pound–Rebka (h=22,5 m): fark $1{,}71\times10^{-24}$, %1 hassasiyet $2{,}46\times10^{-17}$ → oran $7\times10^{-8}$.
- En iyi optik saat (h=1 m, $8\times10^{-19}$ hassasiyet): fark $7{,}6\times10^{-26}$ → oran $9{,}5\times10^{-8}$.
- Güneş yüzeyi çizgi kayması: mutlak pay $2{,}25\times10^{-12}$, etkinin $1{,}06\times10^{-6}$'sı; ölçüm hassasiyeti ~%1.
- **KIRILIYOR MU: HAYIR** — hiçbir mevcut ya da öngörülen saat deneyinde görünmez. M-42 Kısıt 1 de ayakta: $\delta f/f = e^{-\varepsilon}-1$, birinci mertebe katsayısı $-1$ (oran 0,99999999965).

### (d) JEODETİK PRESESYON (GP-B) — 2 ve −½ paylarının denetimi

Holonomi integrali yeniden hesaplandı: $\oint\partial_\perp(\ln n_{eff})\,ds = |d(\ln n_{eff})/dr|\cdot2\pi r$.

- **ÜSTEL:** $\ln n_{eff}=2\mu/r$ **tam doğrusal** ⟹ taşınım payı $=4\pi\mu/r$, **ikinci mertebe terimi YOK**. "+2" payı birinci-mertebe okuma olmaktan çıkıp **özdeşlik** oluyor.
- **LİNEER:** $\ln n_{eff}=-2\ln(1-\mu/r)$ ⟹ $4\pi(\mu/r)/(1-\mu/r)$, yani $+4\pi\mu^2/r^2$ fazlası var.
- **Tur açığı ($-\tfrac12$) hiç değişmiyor** — $\Lambda_{kin}$/$\gamma$ kalemi, potansiyel kolunun biçimine bağlı değil. Toplam $3\pi\mu/r$ **aynen korunuyor**.

| $r$ | ÜSTEL | LİNEER | fark |
|---|---|---|---|
| 7026,5 km | 6605,991195 mas/yıl | 6605,991201 | $5{,}56\times10^{-6}$ mas/yıl |

- GP-B: $6601{,}8\pm18{,}3$ → fark **$3{,}0\times10^{-7}\sigma$**. **KIRILIYOR MU: HAYIR** (2−½ ayrışımı korunuyor, hatta (i) payı tamlaşıyor).
- *Denetim sırasında düşen ilgisiz kalem:* M-42 tablosundaki 6606 mas/yıl ancak $r=7026{,}5$ km ile çıkıyor; M-40 Adım 5 ise $r=R_\oplus+642=7013$ km kullanıyor ve o yarıçapta jeodetik 6637,8 mas/yıl olur. Üstel öneriyle **ilgisiz**, mevcut bir iç tutarsızlık (`18_5_Kuvvet_Matematigi.md:1057` ↔ `:1327`).

### (e) $\xi$, LAGEOS DÜĞÜM KAYMASI, GP-B ÇERÇEVE SÜRÜKLENMESİ

| $|\delta c_{loc}/c_0|$ okuması | değer |
|---|---|
| LİNEER $2\Phi/c_0^2$ | $1{,}392254917318\times10^{-9}$ |
| ÜSTEL, doğrusal kesir $1-e^{-2\varepsilon}$ | $1{,}392254916349\times10^{-9}$ |
| **ÜSTEL, log okuma $|\ln(c_{loc}/c_0)|$ (TAM)** | $1{,}392254917318\times10^{-9}$ — **birebir aynı** |

- $\xi$: $4{,}60418701157\times10^{-10}$ → $4{,}60418700837\times10^{-10}$; bağıl değişim $-6{,}96\times10^{-10}$ (kitabın $4{,}605\times10^{-10}$ yazımı **dokunulmaz**).
- LAGEOS-1 30,6 → $2{,}13\times10^{-8}$ mas/yıl değişim; LAGEOS-2 31,4 → $2{,}19\times10^{-8}$; GP-B 41,0 → $2{,}85\times10^{-8}$. Gözlem hassasiyeti ~%10 (≈3 mas/yıl) → $7\times10^{-9}\sigma$.
- M-40'ın "$\Phi/c_0^2$ ikinci ölçümü" tablosu ($6{,}3\pm1{,}2$ vs $7{,}0\times10^{-10}$, 0,55σ) **değişmiyor**.
- **KIRILIYOR MU: HAYIR.** Üstel yapı $\xi$'nin doğal okumasını (log ölçü) **tam** yapıyor.

### (f) YEREL LORENTZ NULL ($10^{-18}$) — KANIT

$$\frac{c_{loc}}{\ell_{loc}f_{loc}} = \frac{c_0\Lambda^2}{(\ell\Lambda)(f\Lambda)} = \frac{c_0}{\ell f}\qquad\text{— her } \Lambda \text{ için, } \Lambda\text{'nın biçiminden bağımsız}$$

İptal, $\Lambda$'nın **fonksiyonel biçimine değil üs üçlüsüne** ($\ell{:}1$, $f{:}1$, $c{:}2$) bağlıdır; üstel yazım bu üçlüyü aynen taşır. 60 haneli aritmetikte $\Lambda=e^{-\varepsilon}$, $1-\varepsilon$, $0{,}5$, $0{,}01$ için sapma **tam olarak 0,0**. Null **bütün mertebelerde** korunur.

**Ek kazanç (geçerlilik alanı genişliyor):** $\Lambda_{lin}=1-\Phi/c_0^2$, $\Phi\ge c_0^2$'de $\le0$ olur ve yapı çöker; $\Lambda_{üst}=e^{-\Phi/c_0^2}>0$ her zaman. Null artık yalnız zayıf alanda değil **her alan şiddetinde** ayakta.

**KIRILIYOR MU: HAYIR — korunuyor, kanıt yukarıda.**

### (g) M-8'in $P_0$ KALİBRASYONU

Üstel yapıda üsteldeki katsayı zincirden çıkıyor: $C\chi/P_0 = \alpha M/(P_0r) = \mathcal{G}\rho_nM/(P_0r) = N\,\Phi/c_0^2$, $N\equiv\rho_nc_0^2/P_0$. Kavrama Yasası'nın log-diferansiyeli:
$$\tfrac{1-k}{2}\,\bigl|\ln(P/P_0)\bigr| = \tfrac{1-k}{2}N\frac{\Phi}{c_0^2} \;\stackrel{!}{=}\; \frac{2\Phi}{c_0^2}\;\Longrightarrow\; N=\frac{4}{1-k}\;\Longrightarrow\; \boxed{P_0=\frac{1-k}{4}\rho_nc_0^2}$$

| | mevcut kayıt | üstel |
|---|---|---|
| $P_0$ ($k=0$) | $6{,}07\times10^{33}$ Pa | $6{,}0666\times10^{33}$ Pa — **aynı** |
| $\rho_0$ | $\rho_n/4=6{,}8\times10^{16}$ | $6{,}75\times10^{16}=\rho_n/4$ — **aynı** |
| $\Delta P_{yüzey}$ | $\rho_n\Phi=1{,}68925002803\times10^{25}$ Pa | $P_0(1-e^{-4\varepsilon})=1{,}68925002568\times10^{25}$ Pa |

- $\Delta P_{yüzey}$ farkı: bağıl $-1{,}392\times10^{-9}$ ($=-2\Phi/c_0^2$), mutlak $2{,}35\times10^{16}$ Pa $= 3{,}9\times10^{-18}\,P_0$. M-8 Varsayım 4 birinci-mertebe kalıyor — hâlihazırdaki statüsü bu.
- **Zincir artık TAM:** $\tfrac12\ln(P/P_0)=\ln(c/c_0)=-2\Phi/c_0^2$ özdeşliği $\varepsilon=6{,}96\times10^{-10}$, $2{,}12\times10^{-6}$ **ve $\varepsilon=0{,}1$**'de 20 hane doğrulandı. Kalibrasyon "birinci mertebe zincir" olmaktan çıkıp cebirsel özdeşlik oluyor.
- **KIRILIYOR MU: HAYIR — güçleniyor.**

> **ZORUNLU NOTASYON DÜZELTMESİ (kırılma değil, tanım çatalı).** Üstel yapıda $\Phi$'nin iki okuması ikinci mertebede ayrılıyor:
> - $\Phi_{log}\equiv-\tfrac{c_0^2}{4}\ln(P/P_0)$ → **tam olarak $\mathcal{G}M/r$**; $\Lambda=e^{-\Phi/c_0^2}=(P/P_0)^{1/4}$ ve $c_{loc}=\sqrt{P/\rho_0}$ **tam** olur (Kavrama Yasası, $k=0$).
> - $\Phi_{def}\equiv(P_0-P)/\rho_n$ (Ek D · S-28'in mevcut tanımı).
> Fark bağıl $-2\Phi/c_0^2$: Dünya yüzeyi $62\,564\,815{,}853$ ↔ $62\,564\,815{,}766$ J/kg ($1{,}39\times10^{-9}$); Güneş kenarı $4{,}245\times10^{-6}$. **S-28 log biçimle yazılmalı**, birinci mertebe indirgemesi $(P_0-P)/\rho_n$ olarak not düşülmeli. 17 Ağustos 2026 işaret kararı (kuyu derinliği, pozitif) **etkilenmiyor**.

### (h) MERKÜR — AÇIK KALEM KAPANIYOR

| | presesyon ölçeği $\tfrac{2+2\gamma-\beta}{3}$ | Merkür | sapma |
|---|---|---|---|
| **ÜSTEL** ($\kappa=1$, $\beta=1$) | **1** (tam GR) | **42,9805″/yy** | **0,67–0,69σ ✓** |
| LİNEER ($\kappa=0$, $\beta=\tfrac12$) | $7/6$ | 50,1439″/yy | **7960σ ✗** |

Ölçüm $42{,}9799\pm0{,}0009$. Kitabın kayıtlı **son klasik açığı kapanıyor**; mevcut yazımın kendisi (lineer $\Lambda$) 7960σ ile **dışlanıyor**.

---

## GÜNCELLENECEK SATIRLAR

**`C:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik\Kisim_8_Ekler\18_5_Kuvvet_Matematigi.md`**
- `:52` — blok parametre tablosu, $\Lambda$ satırı: $1-\Phi/c_0^2$ → $e^{-\Phi/c_0^2}$
- `:1292` — **M-42 Sonuç kutusu** (asıl hedef): $\Lambda\equiv1-\Phi/c^2$ → $\Lambda\equiv e^{-\Phi/c_0^2}$; lineer biçim "birinci mertebe kesimi" olarak not
- `:1300` — $n_{eff}=1/\Lambda^2=1+2\Phi/c_0^2$ → $n_{eff}=e^{+2\Phi/c_0^2}$ (birinci mertebede $1+2\Phi/c_0^2$)
- `:1317` — M-19 simetri paragrafı, kapanış cümlesi ($1/\gamma\approx1-v^2/2c^2 \leftrightarrow \Lambda=1-\Phi/c_0^2$)
- `:1323` — "PPN dilinde $\gamma_{PPN}=1$ ... tüm **birinci mertebe** sınavları" → $\gamma=1$ **ve** $\beta=1$; "birinci mertebe" kaydı kalkar
- `:1327` (Kapanan Gözlemler tablosu) — bükülme 1,7512″ ✓ kalır; jeodetik 6606 kalır (yarıçap notu ayrı kalem); **yeni satır: Merkür 42,98″/yy ✓**
- `:1334` — taşınım payı (i): holonominin $4\pi\mu/r$ olduğu artık **tam** (ln $n_{eff}$ doğrusal); "birinci mertebe" kaydı düşer
- `:1348–1352` — $P_0$ bölümü: zincirin **log biçimde tam** olduğu eklenir; sayı ($6{,}07\times10^{33}$) değişmez
- `:1356` — **"Yapı birinci mertebedir ... $\beta$ belirlenmemiştir"** → SİLİNMELİ/tersine çevrilmeli ($\beta=1$ türetildi)
- `:1357` — **"Merkür günberi kayması hâlâ kapanmamıştır"** → SİLİNMELİ (kapandı, 0,69σ)
- `:1362` — Açık Uçlar, "$\beta$ parametresi" kalemi → **KAPANDI** olarak yeniden yazılmalı
- `:1365` — "Ayırt edicilik: ... ayrışma ancak $\beta$'da veya ikinci mertebede aranabilir" → $\beta=1$ de GR ile aynı; ayrışma **güçlü alana** taşınır (gölge $+\%4{,}63$, ufuk yok, sonlu $z$)
- `:1367–1371` — "Yapının türü ve $\beta$'nın neden ayrı iş olduğu (28 Tem 2026 denetim notu)" — "optik analoji kütleli yörüngeyi vermez" hükmü **yanlışlandı**; blok yeniden yazılmalı
- `:1611` — H.1 tablosu M-42 satırı: $\Lambda=1-\Phi/c_0^2$ → üstel
- `:1651` — H.2 satır **1′** ($P(\Phi)\Rightarrow\beta$, öncelik 1) → **kapandı**, listeden düşer
- `:1693` — H.3 karne son satırı: *Merkür ... "Türetilemiyor"* → **"Sınandı ✓ 0,69σ"**; ayrıca $\gamma=1$ satırına $\beta=1$ eklenir

**`...\Kisim_8_Ekler\10_Ek_M_Blok_B_Arka_Plan_Basinci.md`** — `:55` (Varsayım 5, $\Lambda$ biçimi), `:60` (Adım 2, log biçim), `:63` civarı (Adım 3 — $\Delta P_{yüzey}=\rho_n\Phi$'nin birinci-mertebe statüsü açıkça yazılmalı)

**`...\Kisim_8_Ekler\13_Ek_M_Blok_E_Doppler_Kizila_Kayma.md`** — `:68` (M-20 Varsayım 4), `:91` ("Birinci mertebede $\Lambda=1-\Phi/c_0^2$..." — bu satır zaten doğru kalıyor, yalnız üstelin tam biçimi eklenir), `:124` (M-21 Varsayım 3), `:134` (**M-21 Sonuç kutusu** $\Lambda\equiv1-\Phi/c^2$)

**`...\Kisim_8_Ekler\17_Ek_B_Arka_Plan_Basinci.md`** — `:29` (Ek B.3, $\Lambda$ biçimi + zincirin tamlığı)

**`...\Kisim_8_Ekler\08_Sembol_Sozlugu.md`** — `:15` (R-10 ölçek ayrımı), `:130` ($\Phi$ girdisi — **log tanım zorunlu**), `:217` (**S-28** — $\Phi\equiv-\tfrac{c_0^2}{4}\ln(P/P_0)$, birinci mertebede $(P_0-P)/\rho_n$)

**`...\Kisim_8_Ekler\07_Matematiksel_Ekler.md`** — `:16` (Blok H özeti, $\Lambda=1-\Phi/c_0^2$)

**Gövde metni (aynı ifadeyi taşıyan yerler):**
- `...\Kisim_1_Giris\06_Evrenaki_Terminolojisi.md:55`, `:81`
- `...\Kisim_4_Bilimin_Tekilligi\02_Evrensel_Sabitler_4_Sinirlar_ve_Itirazlar.md:55`, `:63` (Merkür çekincesi kalkar), `:99` (Merkür'ün "en büyük matematiksel sınav" listesinden çıkması)
- `...\Kisim_4_Bilimin_Tekilligi\03_Kutlecekimsel_Merceklenme.md:19`
- `...\Kisim_6_Kanitlar\02_Kutlecekimsel_Kizila_Kayma_Sentezi.md:79`
- `...\Kisim_6_Kanitlar\03_Ekvatoral_Vorteks_ve_Yorunge_Anomalileri.md:174`, **`:178`** ("Karşı Kayıt — kalan kalem: $\Lambda$ yalnız birinci mertebeyi verir ... $\beta$ henüz türetilmemiştir" → tamamen geçersiz)
- `...\Kisim_6_Kanitlar\98_Ne_Ogrendik.md:11`
- `...\Kisim_7_Tartisma_ve_Sonuc\04_Tartisma_ve_Sonuc.md:127`, **`:165`** (md.14 — $\beta$/Merkür açık kalemi kapanır)
- `...\00_KARNE_Dogrulama_Durumu.md:93` ("Diğer açıklar: md.14 ($\beta$/Merkür 43″)" → düşer), `:135` (öncelik tablosunda md.14)

---

**ÖZET:** Sekiz kalemin hiçbiri kırılmıyor. İkinci mertebe payları sırasıyla 0,73 µas (bükülme, hassasiyetin %3,6'sı), 66 ps (Shapiro, %1,2'si), $2{,}3\times10^{-19}$ (kızıla kayma, $10^{-5}$'i), $5{,}6\times10^{-6}$ mas/yıl (jeodetik, $3\times10^{-7}\sigma$), $2{,}9\times10^{-8}$ mas/yıl ($\xi$ kanalı) — **hepsi ölçüm hassasiyetinin 2–8 mertebe altında**. Buna karşılık üstel yazım beş yerde birinci-mertebe bağıntıyı **özdeşliğe** çeviriyor ($P_0$ zinciri, $\gamma_c=-2$, jeodetik taşınım payı, $\xi$'nin log ölçüsü, Lorentz null'un alanı) ve Merkür'ü kapatıyor. Tek gerçek iş kalemi **kırılma değil notasyon**: S-28'in $\Phi$ tanımı log biçime alınmalı.