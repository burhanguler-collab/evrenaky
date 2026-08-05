# 11.3 Kütle–Dönüş (Spin) İlişkisi: Zarf Rejimleri

Bir gök cisminin **kendi ekseni etrafındaki dönüşü** (spin) ile kütlesi arasında bir yasa var mıdır? Standart astrofizik bu soruya dört ayrı cisim sınıfı için dört ayrı ve birbirine bağlanmayan cevap verir: gezegenler için "oluşum diskinin rastlantısal türbülansı", yıldızlar için "manyetik frenleme", nötron yıldızları için "çökmede açısal momentum korunumu", karadelikler için "Kerr metriğinin geometrik sınırı". Evrenakı'da dönüşün kaynağı tektir — kütleyi oluşturan nükleonların **4B çift-dönüş deşarjı** (Kısım 3 §3.4.4) — ve dört sınıfın dört farklı görünümü tek bir değişkenden çıkar: **zarf durumu.** Bu bölüm önce dört sınıfın ölçülmüş spin verisini tek eksende toplar, sonra 4B kaynaktan $M^2$ yükleme yasasını türetir ve zarf-bağımlı matematiği kurar.

Bu bölümün konusu yalnız spindir; yörünge hareketi, kilitlenme ve uydu göçü ayrı mekanizmaların (M-37, M-43) konusudur ve burada yalnız spin'i etkiledikleri yerde (kavrama, beslenme) anılır.

> **Gözlemsel Hedef.** Dört cisim sınıfının ölçülmüş dönüşlerinde tek bir biçimin — $J=\mathcal{A}\,M^{2}$ — geçerli olduğunu, sınıflar arasındaki farkın üste değil **katsayıya** yazıldığını ve katsayının gövdenin zarf durumuyla kademelendiğini göstermek: gezegenler $\mathcal{A}\approx2\times10^{-16}$, karadelik tavanı $\mathcal{G}/c_{yerel}=2{,}2\times10^{-19}$ — aralarında **~900 kat**, ve bu 900 katın kendisi bir öngörüye dönüşür: çöken çekirdek yükünü taşıyamaz, **boşaltmak zorundadır.**

---

## 11.3.1 Soru, Ayrım ve Ölçüm Zemini

**Spin ile yörünge karıştırılmaz.** Ay'ın Dünya çevresindeki dolanımı yörüngedir; Dünya'nın 23 saat 56 dakikalık kendi dönüşü spindir. Bu bölümdeki her veri noktası ikincisidir.

Dört sınıfın spini dört farklı teknikle ölçülür ve güvenilirlikleri farklıdır:

| Sınıf | Ölçüm tekniği | Tipik hassasiyet | Veri kaynağı |
|---|---|---|---|
| Gezegenler | doğrudan dönem (yüzey/manyetosfer/sismoloji) | $10^{-4}$ ve üstü | IAU/NASA-JPL gezegen veri sayfaları |
| Yıldızlar | tayf çizgisi Doppler genişlemesi ($v\sin i$), yıldız lekesi dönemleri (Kepler/TESS) | ~%10–20 + $\sin i$ izdüşümü | Fukuda (1982); Głębocki & Gnaciński (2005) kataloğu |
| Nötron yıldızları | **pulsar zamanlaması** — atım periyodu | $10^{-15}$'e kadar; astrofiziğin en hassas ölçümü | ATNF Pulsar Kataloğu (Manchester ve ark., 2005) |
| Karadelikler | X-ışını süreklilik/Fe Kα yansıması; GW dalga biçimi | $a^*$'da ±0,05–0,3 | Reynolds (2021) derlemesi; LIGO-Virgo GWTC-3 (2021) |

Kütle tarafında gezegenler ve çift sistemler (pulsar zamanlaması + Shapiro gecikmesi; GW dalga biçimi) hassastır; tek yıldızların kütlesi tayf türünden gelir (~%10).

**Ortak para birimi.** Sınıflar kütlece 17 mertebe ayrıldığı için karşılaştırma iki türetik nicelikle yapılır:

$$j\equiv\frac{J}{M}\ \ [\mathrm{m^2/s}] \qquad\text{ve}\qquad \mathcal{A}\equiv\frac{J}{M^{2}}\ \ [\mathrm{m^2\,s^{-1}\,kg^{-1}}]$$

$\mathcal{A}$'nın seçimi keyfî değildir: hem bu bölümün türeteceği yükleme yasası ($J=\mathcal{A}_0M^2$, §11.3.7) hem de kompakt cisimlerin tavanı ($J_{max}=\mathcal{G}M^2/c_{yerel}$ — standart adıyla Kerr sınırı) **aynı $M^2$ biçimindedir.** O hâlde her sınıfın tek işareti, katsayısıdır. Boyutsuz yazımı $a^*=cJ/\mathcal{G}M^2=\mathcal{A}/(\mathcal{G}/c)$'dir; karadelik literatürünün spin parametresi budur ve kompakt olmayan cisimler için 1'i aşabilir — yarıçapları itim yarıçaplarının çok üstünde olduğundan tavan onları bağlamaz.

---

## 11.3.2 Ana Diyagram: Dört Sınıf Tek Eksende

Aşağıdaki diyagram bu bölümün bütün iddiasını tek bakışta verir. Eksenler kütle (17 mertebe) ve özgül açısal momentum (13 mertebe); noktalar dört sınıfın ölçümleri; iki kesikli doğru ise **aynı eğime (1)** sahiptir çünkü ikisi de $J\propto M^2$ yasasının $j$–$M$ düzlemindeki izidir:

<div style="background:#0b0f19;border:1px solid rgba(0,240,255,0.2);border-radius:10px;padding:12px;margin:1.2em 0;">
<svg viewBox="0 0 940 600" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Segoe UI,sans-serif" role="img" aria-label="Dort sinifta ozgul acisal momentum - kutle diyagrami">
<rect x="0" y="0" width="940" height="600" fill="#0b0f19"/>
<line x1="90.0" y1="50" x2="90.0" y2="520" stroke="#182338" stroke-width="1"/>
<line x1="134.4" y1="50" x2="134.4" y2="520" stroke="#182338" stroke-width="1"/>
<text x="134.4" y="538" fill="#8fa3c0" font-size="12" text-anchor="middle">10²⁴</text>
<line x1="178.9" y1="50" x2="178.9" y2="520" stroke="#182338" stroke-width="1"/>
<line x1="223.3" y1="50" x2="223.3" y2="520" stroke="#182338" stroke-width="1"/>
<text x="223.3" y="538" fill="#8fa3c0" font-size="12" text-anchor="middle">10²⁶</text>
<line x1="267.8" y1="50" x2="267.8" y2="520" stroke="#182338" stroke-width="1"/>
<line x1="312.2" y1="50" x2="312.2" y2="520" stroke="#182338" stroke-width="1"/>
<text x="312.2" y="538" fill="#8fa3c0" font-size="12" text-anchor="middle">10²⁸</text>
<line x1="356.7" y1="50" x2="356.7" y2="520" stroke="#182338" stroke-width="1"/>
<line x1="401.1" y1="50" x2="401.1" y2="520" stroke="#182338" stroke-width="1"/>
<text x="401.1" y="538" fill="#8fa3c0" font-size="12" text-anchor="middle">10³⁰</text>
<line x1="445.6" y1="50" x2="445.6" y2="520" stroke="#182338" stroke-width="1"/>
<line x1="490.0" y1="50" x2="490.0" y2="520" stroke="#182338" stroke-width="1"/>
<text x="490.0" y="538" fill="#8fa3c0" font-size="12" text-anchor="middle">10³²</text>
<line x1="534.4" y1="50" x2="534.4" y2="520" stroke="#182338" stroke-width="1"/>
<line x1="578.9" y1="50" x2="578.9" y2="520" stroke="#182338" stroke-width="1"/>
<text x="578.9" y="538" fill="#8fa3c0" font-size="12" text-anchor="middle">10³⁴</text>
<line x1="623.3" y1="50" x2="623.3" y2="520" stroke="#182338" stroke-width="1"/>
<line x1="667.8" y1="50" x2="667.8" y2="520" stroke="#182338" stroke-width="1"/>
<text x="667.8" y="538" fill="#8fa3c0" font-size="12" text-anchor="middle">10³⁶</text>
<line x1="712.2" y1="50" x2="712.2" y2="520" stroke="#182338" stroke-width="1"/>
<line x1="756.7" y1="50" x2="756.7" y2="520" stroke="#182338" stroke-width="1"/>
<text x="756.7" y="538" fill="#8fa3c0" font-size="12" text-anchor="middle">10³⁸</text>
<line x1="801.1" y1="50" x2="801.1" y2="520" stroke="#182338" stroke-width="1"/>
<line x1="845.6" y1="50" x2="845.6" y2="520" stroke="#182338" stroke-width="1"/>
<text x="845.6" y="538" fill="#8fa3c0" font-size="12" text-anchor="middle">10⁴⁰</text>
<line x1="890.0" y1="50" x2="890.0" y2="520" stroke="#182338" stroke-width="1"/>
<line x1="90" y1="520.0" x2="890" y2="520.0" stroke="#182338" stroke-width="1"/>
<text x="82" y="524.0" fill="#8fa3c0" font-size="12" text-anchor="end">10⁸</text>
<line x1="90" y1="486.4" x2="890" y2="486.4" stroke="#182338" stroke-width="1"/>
<line x1="90" y1="452.9" x2="890" y2="452.9" stroke="#182338" stroke-width="1"/>
<text x="82" y="456.9" fill="#8fa3c0" font-size="12" text-anchor="end">10¹⁰</text>
<line x1="90" y1="419.3" x2="890" y2="419.3" stroke="#182338" stroke-width="1"/>
<line x1="90" y1="385.7" x2="890" y2="385.7" stroke="#182338" stroke-width="1"/>
<text x="82" y="389.7" fill="#8fa3c0" font-size="12" text-anchor="end">10¹²</text>
<line x1="90" y1="352.1" x2="890" y2="352.1" stroke="#182338" stroke-width="1"/>
<line x1="90" y1="318.6" x2="890" y2="318.6" stroke="#182338" stroke-width="1"/>
<text x="82" y="322.6" fill="#8fa3c0" font-size="12" text-anchor="end">10¹⁴</text>
<line x1="90" y1="285.0" x2="890" y2="285.0" stroke="#182338" stroke-width="1"/>
<line x1="90" y1="251.4" x2="890" y2="251.4" stroke="#182338" stroke-width="1"/>
<text x="82" y="255.4" fill="#8fa3c0" font-size="12" text-anchor="end">10¹⁶</text>
<line x1="90" y1="217.9" x2="890" y2="217.9" stroke="#182338" stroke-width="1"/>
<line x1="90" y1="184.3" x2="890" y2="184.3" stroke="#182338" stroke-width="1"/>
<text x="82" y="188.3" fill="#8fa3c0" font-size="12" text-anchor="end">10¹⁸</text>
<line x1="90" y1="150.7" x2="890" y2="150.7" stroke="#182338" stroke-width="1"/>
<line x1="90" y1="117.1" x2="890" y2="117.1" stroke="#182338" stroke-width="1"/>
<text x="82" y="121.1" fill="#8fa3c0" font-size="12" text-anchor="end">10²⁰</text>
<line x1="90" y1="83.6" x2="890" y2="83.6" stroke="#182338" stroke-width="1"/>
<line x1="90" y1="50.0" x2="890" y2="50.0" stroke="#182338" stroke-width="1"/>
<text x="82" y="54.0" fill="#8fa3c0" font-size="12" text-anchor="end">10²²</text>
<rect x="90" y="50" width="800" height="470" fill="none" stroke="#8fa3c0" stroke-width="1"/>
<text x="490.0" y="560.0" fill="#8fa3c0" font-size="14" text-anchor="middle" font-weight="normal">kütle M [kg]</text>
<text x="26" y="285.0" fill="#8fa3c0" font-size="14" text-anchor="middle" transform="rotate(-90 26 285.0)">özgül açısal momentum j = J/M [m²/s]</text>
<text x="90.0" y="32.0" fill="#e6eefb" font-size="15" text-anchor="start" font-weight="500">Şekil 11.3.A — Dört sınıf tek eksende: iki paralel doğru (eğim 1), aralarında 900 kat</text>
<line x1="121.1" y1="520.0" x2="743.3" y2="50.0" stroke="#ffb84d" stroke-width="1.6" stroke-dasharray="7 5" opacity="0.9"/>
<text x="282.7" y="394.5" fill="#ffb84d" font-size="12" text-anchor="start" font-weight="normal">yükleme doğrusu  j = 𝒜₀M   (𝒜₀ ≈ 2×10⁻¹⁶)</text>
<line x1="252.3" y1="520.0" x2="874.6" y2="50.0" stroke="#ff6b6b" stroke-width="1.6" stroke-dasharray="7 5" opacity="0.9"/>
<text x="567.1" y="278.8" fill="#ff6b6b" font-size="12" text-anchor="start" font-weight="normal">tavan  j = (𝒢/c_yerel)M   (Kerr)</text>
<circle cx="125.9" cy="504.1" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="131.9" y="496.1" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Mars</text>
<circle cx="168.9" cy="486.7" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="174.9" y="500.7" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Dünya</text>
<circle cx="223.8" cy="446.7" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="215.8" y="437.7" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Neptün</text>
<circle cx="256.9" cy="415.2" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="262.9" y="429.2" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Satürn</text>
<circle cx="280.1" cy="407.3" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="270.1" y="398.3" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Jüpiter</text>
<circle cx="220.6" cy="446.7" r="5" fill="none" stroke="#ffb84d" stroke-width="1.6"/>
<text x="228.6" y="456.7" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Uranüs</text>
<circle cx="328.1" cy="393.0" r="5" fill="none" stroke="#ffb84d" stroke-width="1.6"/>
<text x="336.1" y="397.0" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">β Pic b</text>
<circle cx="485.6" cy="319.3" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="493.6" y="315.3" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">O5</text>
<circle cx="448.7" cy="333.5" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="456.7" y="343.5" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">B5</text>
<circle cx="434.9" cy="343.6" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="424.9" y="335.6" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">A0</text>
<circle cx="423.5" cy="360.0" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="431.5" y="370.0" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">F0</text>
<circle cx="414.4" cy="357.4" r="5" fill="none" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="350.4" y="361.4" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">T Tauri</text>
<circle cx="414.4" cy="419.8" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="422.4" y="429.8" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">Güneş</text>
<circle cx="420.9" cy="453.7" r="5" fill="#b58cff" stroke="#b58cff" stroke-width="1.6"/>
<text x="428.9" y="463.7" fill="#b58cff" font-size="11" text-anchor="start" font-weight="normal">Crab</text>
<circle cx="428.5" cy="418.6" r="5" fill="#b58cff" stroke="#b58cff" stroke-width="1.6"/>
<text x="436.5" y="422.6" fill="#b58cff" font-size="11" text-anchor="start" font-weight="normal">J0740</text>
<circle cx="420.9" cy="407.4" r="5" fill="#b58cff" stroke="#b58cff" stroke-width="1.6"/>
<text x="368.9" y="399.4" fill="#b58cff" font-size="11" text-anchor="start" font-weight="normal">716 Hz</text>
<circle cx="450.8" cy="401.0" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="458.8" y="411.0" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">A0620</text>
<circle cx="473.3" cy="353.2" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="411.3" y="347.2" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">Cyg X-1</text>
<path d="M 494.0 337.3 L 500.0 343.3 L 494.0 349.3 L 488.0 343.3 Z" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="502.0" y="353.3" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">GW150914</text>
<path d="M 510.0 324.1 L 516.0 330.1 L 510.0 336.1 L 504.0 330.1 Z" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="518.0" y="326.1" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">GW190521</text>
<rect x="704.2" y="180.0" width="10" height="10" fill="none" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="717.2" y="197.0" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">Sgr A*</text>
<rect x="845.5" y="64.7" width="10" height="10" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="804.5" y="61.7" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">M87*</text>
<circle cx="108.0" cy="58.0" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="120.0" y="62.0" fill="#ffb84d" font-size="12" text-anchor="start" font-weight="normal">gezegenler (içi boş: hizasız/genç)</text>
<circle cx="108.0" cy="77.0" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="120.0" y="81.0" fill="#4dd2ff" font-size="12" text-anchor="start" font-weight="normal">yıldızlar (içi boş: T Tauri)</text>
<circle cx="108.0" cy="96.0" r="5" fill="#b58cff" stroke="#b58cff" stroke-width="1.6"/>
<text x="120.0" y="100.0" fill="#b58cff" font-size="12" text-anchor="start" font-weight="normal">nötron yıldızları</text>
<circle cx="108.0" cy="115.0" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="120.0" y="119.0" fill="#ff6b6b" font-size="12" text-anchor="start" font-weight="normal">karadelikler (◆ GW, ■ SMBH)</text>
</svg>
<p style="font-size:0.9em;color:#8fa3c0;margin:10px 4px 2px;"><em>Şekil 11.3.A: Dört sınıfın ölçülmüş özgül açısal momentumu. İki kesikli doğru aynı eğime sahiptir (J ∝ M² ↔ j ∝ M): üstte gezegen kalibrasyonlu yükleme doğrusu, altta kompakt tavan. Veri: IAU/NASA-JPL; Fukuda 1982; ATNF; Reynolds 2021; GWTC-3.</em></p>
</div>

Okuma üç cümledir:

1. **Gezegenler üst doğruya oturur** — $J=\mathcal{A}_0M^2$, $\mathcal{A}_0\approx2\times10^{-16}$: 4B yüklemenin tam ifadesi (rijit zarf, kapalı kanal).
2. **Karadelikler alt doğruya yaslanır** — $J\le(\mathcal{G}/c_{yerel})M^2$: aynı biçim, ama tavanda. İki doğru paraleldir ve aralarında ~900 kat vardır.
3. **Yıldızlar ve nötron yıldızları iki doğrunun arasında, aşağı doğru kayar** — zarfları momentumu ortama geri sızdırır (yıldız: manyetize rüzgâr; NS: dipol ışıması); kayma hızını zarf türü belirler.

| Sınıf | Zarf durumu | $\mathcal{A}=J/M^2$ | $a^*$ |
|---|---|---|---|
| Gezegenler (serbest) | rijit zarf, kanal kapalı | $(1{,}2$–$4{,}6)\times10^{-16}$ | 540–2100 |
| Yıldız doğumu (T Tauri, OBA) | plazma zarf, taze | $(1$–$3)\times10^{-18}$ | 5–16 |
| Güneş (4,6 Gyr) | konvektif zarf, kanal açık | $4{,}9\times10^{-20}$ | **0,22** |
| Nötron yıldızları | zarf fırlatılmış | $(0{,}001$–$0{,}08)\times10^{-18}$ | 0,006–0,37 |
| Karadelikler | zarf yok, ufuk var | $\le2{,}2\times10^{-19}$ | 0,12–0,99 ≤ 1 |

Dikkat çekici iki ayrıntı: Güneş bugün o kadar frenlenmiştir ki katsayısı bir karadeliğin **tavanının beşte birine** düşmüştür ($a^*_\odot=0{,}22$); en hızlı nötron yıldızı bile ($a^*=0{,}37$) tavanın altındadır. Tavanı yalnız karadelikler doldurur.

---

## 11.3.3 Gezegenler: Rijit Zarf — Korunan İfade

Veri, IAU/NASA-JPL değerleridir; $L=\lambda MR^2\omega$ ile hesaplanır ($\lambda=I/MR^2$ eylemsizlik çarpanı, Dünya/Mars'ta ölçüm, devlerde model):

| Gövde | $M$ (kg) | $P_{spin}$ | $v_{ekv}$ (m/s) | $L$ (kg m²/s) | $\mathcal{A}\times10^{16}$ |
|---|---|---|---|---|---|
| Mars | $6{,}42\times10^{23}$ | 24,62 sa | 241 | $1{,}91\times10^{32}$ | 4,6 |
| Dünya | $5{,}97\times10^{24}$ | 23,93 sa | 465 | $5{,}86\times10^{33}$ | 1,6 |
| Neptün | $1{,}02\times10^{26}$ | 16,11 sa | 2.683 | $1{,}57\times10^{36}$ | 1,5 |
| Satürn | $5{,}68\times10^{26}$ | 10,56 sa | 9.960 | $7{,}51\times10^{37}$ | 2,3 |
| Jüpiter | $1{,}90\times10^{27}$ | 9,93 sa | 12.572 | $4{,}33\times10^{38}$ | 1,2 |
| *Uranüs (hizasız, $\theta=98°$)* | $8{,}68\times10^{25}$ | 17,24 sa | 2.588 | $1{,}32\times10^{36}$ | 1,8 |
| **Merkür (bastırılmış)** | $3{,}30\times10^{23}$ | 58,65 gün | 3,0 | $8{,}4\times10^{29}$ | 0,077 |
| **Venüs (bastırılmış)** | $4{,}87\times10^{24}$ | 243 gün (retro) | 1,8 | $1{,}8\times10^{31}$ | 0,0076 |

<div style="background:#0b0f19;border:1px solid rgba(0,240,255,0.2);border-radius:10px;padding:12px;margin:1.2em 0;">
<svg viewBox="0 0 940 540" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Segoe UI,sans-serif" role="img" aria-label="Gezegenlerde donme acisal momentumu - kutle iliskisi">
<rect x="0" y="0" width="940" height="540" fill="#0b0f19"/>
<line x1="90.0" y1="50" x2="90.0" y2="460" stroke="#182338" stroke-width="1"/>
<text x="90.0" y="478" fill="#8fa3c0" font-size="12" text-anchor="middle">10²³</text>
<line x1="232.9" y1="50" x2="232.9" y2="460" stroke="#182338" stroke-width="1"/>
<text x="232.9" y="478" fill="#8fa3c0" font-size="12" text-anchor="middle">10²⁴</text>
<line x1="375.7" y1="50" x2="375.7" y2="460" stroke="#182338" stroke-width="1"/>
<text x="375.7" y="478" fill="#8fa3c0" font-size="12" text-anchor="middle">10²⁵</text>
<line x1="518.6" y1="50" x2="518.6" y2="460" stroke="#182338" stroke-width="1"/>
<text x="518.6" y="478" fill="#8fa3c0" font-size="12" text-anchor="middle">10²⁶</text>
<line x1="661.4" y1="50" x2="661.4" y2="460" stroke="#182338" stroke-width="1"/>
<text x="661.4" y="478" fill="#8fa3c0" font-size="12" text-anchor="middle">10²⁷</text>
<line x1="804.3" y1="50" x2="804.3" y2="460" stroke="#182338" stroke-width="1"/>
<text x="804.3" y="478" fill="#8fa3c0" font-size="12" text-anchor="middle">10²⁸</text>
<line x1="90" y1="460.0" x2="890" y2="460.0" stroke="#182338" stroke-width="1"/>
<line x1="90" y1="425.8" x2="890" y2="425.8" stroke="#182338" stroke-width="1"/>
<text x="82" y="429.8" fill="#8fa3c0" font-size="12" text-anchor="end">10³⁰</text>
<line x1="90" y1="391.7" x2="890" y2="391.7" stroke="#182338" stroke-width="1"/>
<line x1="90" y1="357.5" x2="890" y2="357.5" stroke="#182338" stroke-width="1"/>
<text x="82" y="361.5" fill="#8fa3c0" font-size="12" text-anchor="end">10³²</text>
<line x1="90" y1="323.3" x2="890" y2="323.3" stroke="#182338" stroke-width="1"/>
<line x1="90" y1="289.2" x2="890" y2="289.2" stroke="#182338" stroke-width="1"/>
<text x="82" y="293.2" fill="#8fa3c0" font-size="12" text-anchor="end">10³⁴</text>
<line x1="90" y1="255.0" x2="890" y2="255.0" stroke="#182338" stroke-width="1"/>
<line x1="90" y1="220.8" x2="890" y2="220.8" stroke="#182338" stroke-width="1"/>
<text x="82" y="224.8" fill="#8fa3c0" font-size="12" text-anchor="end">10³⁶</text>
<line x1="90" y1="186.7" x2="890" y2="186.7" stroke="#182338" stroke-width="1"/>
<line x1="90" y1="152.5" x2="890" y2="152.5" stroke="#182338" stroke-width="1"/>
<text x="82" y="156.5" fill="#8fa3c0" font-size="12" text-anchor="end">10³⁸</text>
<line x1="90" y1="118.3" x2="890" y2="118.3" stroke="#182338" stroke-width="1"/>
<line x1="90" y1="84.2" x2="890" y2="84.2" stroke="#182338" stroke-width="1"/>
<text x="82" y="88.2" fill="#8fa3c0" font-size="12" text-anchor="end">10⁴⁰</text>
<line x1="90" y1="50.0" x2="890" y2="50.0" stroke="#182338" stroke-width="1"/>
<rect x="90" y="50" width="800" height="410" fill="none" stroke="#8fa3c0" stroke-width="1"/>
<text x="490.0" y="500.0" fill="#8fa3c0" font-size="14" text-anchor="middle" font-weight="normal">kütle M [kg]</text>
<text x="26" y="255.0" fill="#8fa3c0" font-size="14" text-anchor="middle" transform="rotate(-90 26 255.0)">dönme açısal momentumu L [kg m²/s]</text>
<text x="90.0" y="32.0" fill="#e6eefb" font-size="15" text-anchor="start" font-weight="500">Şekil 11.3.B — Serbest gezegenler tek güç yasasında (eğim 1,89) · bastırılmış ikili 300–4000 kat altta</text>
<line x1="118.6" y1="393.4" x2="875.7" y2="52.1" stroke="#ffb84d" stroke-width="1.6" stroke-dasharray="7 5" opacity="0.9"/>
<text x="668.6" y="126.1" fill="#ffb84d" font-size="12" text-anchor="start" font-weight="normal">fit: log-log eğim 1,89   (R² = 0,996)</text>
<circle cx="205.3" cy="347.9" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="213.3" y="341.9" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Mars</text>
<circle cx="343.7" cy="297.1" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="351.7" y="309.1" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Dünya</text>
<circle cx="520.0" cy="214.2" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="512.0" y="204.2" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Neptün</text>
<circle cx="626.4" cy="156.8" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="634.4" y="168.8" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Satürn</text>
<circle cx="701.2" cy="130.7" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="691.2" y="120.7" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Jüpiter</text>
<circle cx="509.8" cy="216.7" r="5" fill="none" stroke="#ffb84d" stroke-width="1.6"/>
<text x="519.8" y="228.7" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Uranüs</text>
<circle cx="855.4" cy="79.3" r="5" fill="none" stroke="#ffb84d" stroke-width="1.6"/>
<text x="737.4" y="83.3" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">β Pic b (genç)</text>
<circle cx="164.1" cy="428.4" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="174.1" y="432.4" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">Merkür</text>
<circle cx="331.0" cy="383.0" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="341.0" y="387.0" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">Venüs</text>
<text x="140.0" y="412.2" fill="#ff6b6b" font-size="12" text-anchor="start" font-weight="normal">girdap rekabetiyle bastırılmış (M-24):</text>
<text x="140.0" y="429.3" fill="#ff6b6b" font-size="12" text-anchor="start" font-weight="normal">Merkür −%97,7 · Venüs −%100,3 (retrograd)</text>
</svg>
<p style="font-size:0.9em;color:#8fa3c0;margin:10px 4px 2px;"><em>Şekil 11.3.B: Gezegenlerde dönme açısal momentumu. Serbest-hizalı beşli tek güç yasasına oturur; bastırılmış Merkür/Venüs (kırmızı) doğrunun 300–4.000 kat altında; Uranüs (hizasız) ve β Pic b (genç) içi boş.</em></p>
</div>

Beş serbest-hizalı gövdenin fiti bu bölümün girdi setiyle $L\propto M^{1{,}89}$ ($R^2=0{,}996$) ve $v_{ekv}\propto M^{0{,}54}$ ($R^2=0{,}979$) verir; Kısım 3 §3.4.4'ün girdi setiyle $L\propto M^{1{,}94}$ ($R^2=1{,}00$). Fark $\lambda$ ve dönem seçimlerinin payıdır; iki set de aynı hükme işaret eder: **üs 2'ye, katsayı $\mathcal{A}_0\approx2\times10^{-16}$'ya oturur.**

Dört dürüstlük kaydı bağlayıcıdır (tümü Kısım 3 §3.4.4'te ayrıntılıdır):
- **Saçılma tabanı ±%30'dur** ve $\mathcal{A}$ tek tek gövdelerde 1,2–4,6 arasında gezinir ($\times10^{-16}$); "tek doğru" değil "tek güç yasası eğilimi" okunmalıdır.
- **Merkür ve Venüs yasanın ihlali değil, ikinci mekanizmanın kanıtıdır:** Güneş girdabının kavraması (M-24) ifadeyi %97,7 ve %100,3 yutmuştur; doğrunun 300–4.000 kat altındadırlar ve kalıntı dönüşleri yerel girdap ritmine kilitlidir (3:2 rezonans; retrograd kayma).
- **Uranüs hizasızdır** ($\theta\approx98°$): eksen devrilmesi yükleme verimini düşürür; nokta içi boş çizilir ve fitte kullanılmaz — yine de banda yakın durması, devrilme öncesi birikimin korunmuş olmasıyla tutarlıdır.
- **β Pictoris b genç ve büzülmektedir:** ölçülen $v_{ekv}=25$ km/s (Snellen ve ark., 2014 — bir ötegezegenin ilk spin ölçümü), doğrunun öngörüsü 50 km/s'nin yarısıdır. $J$ korunumlu büzülme tamamlandığında ($R\to R_J$) hız ~34 km/s'ye çıkar ve ±%30 bandının içine girer. Genç dev ötegezegen spinleri bu doğrunun **canlı sınavıdır.**

---

## 11.3.4 Yıldızlar: Plazma Zarf — Açık Kanal ve Kraft Kırılması

Anakol yıldızlarında tayf türü başına ortalama dönme hızları (Fukuda, 1982; Głębocki & Gnaciński, 2005; $v\sin i$ izdüşüm ortalaması gerçek $v_{ekv}$'nun ~$\pi/4$'üdür):

| Tayf türü | $M$ ($M_\odot$) | $\langle v\sin i\rangle$ (km/s) |
|---|---|---|
| O5 | ~40 | ~190 |
| B0 | 16 | ~200 |
| B5 | 5,9 | ~220 |
| A0 | 2,9 | ~180 |
| A5 | 2,0 | ~150 |
| F0 | 1,6 | ~100 |
| **F5 — Kraft kırılması** | **1,3** | **~30** |
| G0 | 1,05 | ~8 |
| Güneş (G2) | 1,0 | 2,0 |
| K0–M0 | 0,85–0,5 | ~2–3 |

<div style="background:#0b0f19;border:1px solid rgba(0,240,255,0.2);border-radius:10px;padding:12px;margin:1.2em 0;">
<svg viewBox="0 0 940 540" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Segoe UI,sans-serif" role="img" aria-label="Anakol yildizlarinda ortalama donme hizi - kutle ve Kraft kirilmasi">
<rect x="0" y="0" width="940" height="540" fill="#0b0f19"/>
<line x1="128.1" y1="50" x2="128.1" y2="460" stroke="#182338"/>
<text x="128.1" y="478.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">0.5</text>
<line x1="242.4" y1="50" x2="242.4" y2="460" stroke="#182338"/>
<text x="242.4" y="478.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">1.0</text>
<line x1="356.7" y1="50" x2="356.7" y2="460" stroke="#182338"/>
<text x="356.7" y="478.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">2.0</text>
<line x1="471.0" y1="50" x2="471.0" y2="460" stroke="#182338"/>
<text x="471.0" y="478.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">4</text>
<line x1="585.2" y1="50" x2="585.2" y2="460" stroke="#182338"/>
<text x="585.2" y="478.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">8</text>
<line x1="699.5" y1="50" x2="699.5" y2="460" stroke="#182338"/>
<text x="699.5" y="478.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">16</text>
<line x1="813.8" y1="50" x2="813.8" y2="460" stroke="#182338"/>
<text x="813.8" y="478.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">32</text>
<line x1="90" y1="460.0" x2="890" y2="460.0" stroke="#182338"/>
<text x="82.0" y="464.0" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">1</text>
<line x1="90" y1="381.2" x2="890" y2="381.2" stroke="#182338"/>
<text x="82.0" y="385.2" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">3</text>
<line x1="90" y1="302.3" x2="890" y2="302.3" stroke="#182338"/>
<text x="82.0" y="306.3" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">10</text>
<line x1="90" y1="223.5" x2="890" y2="223.5" stroke="#182338"/>
<text x="82.0" y="227.5" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">32</text>
<line x1="90" y1="144.6" x2="890" y2="144.6" stroke="#182338"/>
<text x="82.0" y="148.6" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">100</text>
<line x1="90" y1="65.8" x2="890" y2="65.8" stroke="#182338"/>
<text x="82.0" y="69.8" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">316</text>
<rect x="90" y="50" width="195.8" height="410" fill="#4dd2ff" opacity="0.06"/>
<line x1="285.8" y1="50" x2="285.8" y2="460" stroke="#4dd2ff" stroke-width="1.6" stroke-dasharray="6 5"/>
<rect x="90" y="50" width="800" height="410" fill="none" stroke="#8fa3c0"/>
<text x="490.0" y="500.0" fill="#8fa3c0" font-size="14" text-anchor="middle" font-weight="normal">kütle M [M☉]</text>
<text x="26" y="255.0" fill="#8fa3c0" font-size="14" text-anchor="middle" transform="rotate(-90 26 255.0)">ortalama dönme hızı ⟨v sin i⟩ [km/s]</text>
<text x="90.0" y="32.0" fill="#e6eefb" font-size="15" text-anchor="start" font-weight="500">Şekil 11.3.C — Kraft kırılması: konvektif zarf sınırında (M ≈ 1,3 M☉) dönüş 30 kat düşer</text>
<text x="275.8" y="72.0" fill="#4dd2ff" font-size="12" text-anchor="end" font-weight="normal">konvektif zarf — kanal açık, frenli</text>
<text x="295.8" y="72.0" fill="#4dd2ff" font-size="12" text-anchor="start" font-weight="normal">radyatif zarf — kanal kapalı, hızlı</text>
<circle cx="852.7" cy="100.7" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="860.7" y="94.7" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">O5</text>
<circle cx="701.1" cy="97.1" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="709.1" y="91.1" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">B0</text>
<circle cx="536.0" cy="90.6" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="544.0" y="84.6" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">B5</text>
<circle cx="418.5" cy="104.4" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="426.5" y="98.4" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">A0</text>
<circle cx="357.1" cy="116.8" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="365.1" y="110.8" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">A5</text>
<circle cx="320.1" cy="144.6" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="328.1" y="138.6" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">F0</text>
<circle cx="285.8" cy="227.1" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="295.8" y="237.1" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">F5</text>
<circle cx="250.5" cy="317.6" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="260.5" y="327.6" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">G0</text>
<circle cx="242.4" cy="412.5" r="5" fill="none" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="252.4" y="422.5" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">Güneş</text>
<circle cx="215.5" cy="384.8" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="223.5" y="378.8" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">K0</text>
<circle cx="131.0" cy="384.8" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="139.0" y="378.8" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">M0</text>
<circle cx="242.4" cy="254.8" r="5" fill="none" stroke="#ffb84d" stroke-width="1.6"/>
<text x="251.4" y="248.8" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">T Tauri (1 Myr): genç Güneş 10 kat hızlıydı</text>
<path d="M 242.4 262.8 L 242.4 400.0" stroke="#ffb84d" stroke-width="1.2" stroke-dasharray="3 4" fill="none"/>
<text x="250.0" y="331.8" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Skumanich: ω ∝ t^(−1/2)</text>
</svg>
<p style="font-size:0.9em;color:#8fa3c0;margin:10px 4px 2px;"><em>Şekil 11.3.C: Anakol ortalama dönme hızları ve Kraft kırılması. Gölgeli bölge: konvektif zarf (açık kanal). Sınırın solunda spin yaşla, sağında doğum ifadesiyle belirlenir.</em></p>
</div>

Tablo iki olgu barındırır ve ikisi de zarf dilinde tek cümledir:

1. **Kraft kırılması** (Kraft, 1967): $M\approx1{,}3\,M_\odot$'ta ortalama dönüş **30 kat** düşer. Bu kütle, standart yıldız yapısında **dış konvektif zarfın** ortaya çıktığı sınırdır. Konvektif zarf + manyetize rüzgâr = dönme momentumunu ortama sızdıran **açık kanal**; radyatif zarflı erken türlerde (O–A) kanal kapalıdır ve doğum ifadesi korunur. Spini belirleyen kütlenin kendisi değil, kütlenin dikte ettiği **zarf türüdür** — kırılmanın keskinliği bunun kanıtıdır.
2. **Açık kanallı yıldızlarda spin yaş fonksiyonudur** (Skumanich, 1972: $\omega\propto t^{-1/2}$; açık küme jirokronolojisiyle doğrulanmış). Bu yüzden geç-tip yıldızlar kütle–spin doğrusuna oturmaz ve oturmamaları gerekir — Kısım 3 §3.4.4'ün tanım alanı kaydı ("yasa yıldızlara uygulanamaz") bu mekanizmanın ifadesidir.

Sızıntının nicel sağlaması bu bölümün en temiz sonuçlarından biridir. Güneş benzeri bir yıldızın katsayısı iki çağda ölçülebilir: T Tauri evresinde (1 Myr, $v\approx20$ km/s, konvektif $k^2\approx0{,}2$) $\mathcal{A}\approx3{,}5\times10^{-18}$; bugünkü Güneş'te (4,6 Gyr; $J_\odot=1{,}92\times10^{41}$ kg m²/s, helyosismik — Pijpers, 1998) $\mathcal{A}=4{,}9\times10^{-20}$. Oran **72**'dir; Skumanich yasasının öngörüsü $\sqrt{4600/1}=68$'dir — **%6 içinde.** Dört mertebelik zaman aralığında tek üslü sızıntı yasası tutmaktadır.

Doğum bandı da yerine oturur: kanal-kapalı erken türlerin katsayısı $(1$–$3)\times10^{-18}$, T Tauri ile aynı banttadır — yıldızlar **gezegen bandının ~100 kat altında doğar.** Bu açık, oluşumun kendisinde yaşanır: protoyıldız, momentumunun çoğunu beslenme diskine ve disk-kilitlenmesine bırakır (teori dilinde: plazma zarf, kafesle rijit kuplaj kuramaz — deplasmanın $\phi$ kanalı zayıftır). Yıldız doğumunun "açısal momentum problemi" olarak bilinen bu kalem, zarf çerçevesinde bir problem değil, plazma zarfının tanımlayıcı imzasıdır.

---

## 11.3.5 Nötron Yıldızları: Zarfını Fırlatmış Çekirdek

Kütlesi ölçülmüş pulsarlar (ATNF kataloğu; kütleler çift-sistem zamanlaması ve Shapiro gecikmesinden — NICER/Green Bank programları):

| Pulsar | $M$ ($M_\odot$) | $\nu$ (Hz) | $a^*$ | Sınıf |
|---|---|---|---|---|
| Vela | ~1,4 | 11,2 | 0,006 | genç |
| B1913+16 (Hulse–Taylor) | 1,440 | 16,9 | 0,008 | genç |
| Crab | ~1,4 | 29,9 | 0,015 | genç (doğumda ~50 Hz) |
| J0737−3039A (çift pulsar) | 1,338 | 44,1 | 0,025 | kısmen dönüştürülmüş |
| J1614−2230 | 1,908 | 317 | 0,12 | geri dönüştürülmüş |
| J0740+6620 | 2,08 | 347 | 0,11 | geri dönüştürülmüş |
| J0952−0607 | **2,35** | **707** | 0,20 | geri dönüştürülmüş |
| J1748−2446ad | (1,4 vars.) | **716** | 0,37 | geri dönüştürülmüş |

<div style="background:#0b0f19;border:1px solid rgba(0,240,255,0.2);border-radius:10px;padding:12px;margin:1.2em 0;">
<svg viewBox="0 0 940 540" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Segoe UI,sans-serif" role="img" aria-label="Kutlesi olculmus pulsarlarda donme frekansi ve kirilma tavani">
<rect x="0" y="0" width="940" height="540" fill="#0b0f19"/>
<line x1="145.2" y1="50" x2="145.2" y2="460" stroke="#182338"/>
<text x="145.2" y="478.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">1,2</text>
<line x1="255.5" y1="50" x2="255.5" y2="460" stroke="#182338"/>
<text x="255.5" y="478.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">1,4</text>
<line x1="365.9" y1="50" x2="365.9" y2="460" stroke="#182338"/>
<text x="365.9" y="478.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">1,6</text>
<line x1="476.2" y1="50" x2="476.2" y2="460" stroke="#182338"/>
<text x="476.2" y="478.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">1,8</text>
<line x1="586.6" y1="50" x2="586.6" y2="460" stroke="#182338"/>
<text x="586.6" y="478.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">2,0</text>
<line x1="696.9" y1="50" x2="696.9" y2="460" stroke="#182338"/>
<text x="696.9" y="478.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">2,2</text>
<line x1="807.2" y1="50" x2="807.2" y2="460" stroke="#182338"/>
<text x="807.2" y="478.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">2,4</text>
<line x1="90" y1="391.7" x2="890" y2="391.7" stroke="#182338"/>
<text x="82.0" y="395.7" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">10¹</text>
<line x1="90" y1="255.0" x2="890" y2="255.0" stroke="#182338"/>
<text x="82.0" y="259.0" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">10²</text>
<line x1="90" y1="118.3" x2="890" y2="118.3" stroke="#182338"/>
<text x="82.0" y="122.3" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">10³</text>
<rect x="90" y="50" width="800" height="410" fill="none" stroke="#8fa3c0"/>
<text x="490.0" y="500.0" fill="#8fa3c0" font-size="14" text-anchor="middle" font-weight="normal">kütle M [M☉]  (pulsar zamanlaması + Shapiro gecikmesi)</text>
<text x="26" y="255.0" fill="#8fa3c0" font-size="14" text-anchor="middle" transform="rotate(-90 26 255.0)">dönme frekansı ν [Hz]</text>
<text x="90.0" y="32.0" fill="#e6eefb" font-size="15" text-anchor="start" font-weight="500">Şekil 11.3.D — Nötron yıldızları: beslenme zarfı kuranlar (MSP) hem ağır hem hızlı</text>
<path d="M 90.0 95.7 L 103.6 95.1 L 117.1 94.5 L 130.7 93.8 L 144.2 93.2 L 157.8 92.6 L 171.4 92.0 L 184.9 91.4 L 198.5 90.9 L 212.0 90.3 L 225.6 89.8 L 239.2 89.2 L 252.7 88.7 L 266.3 88.2 L 279.8 87.7 L 293.4 87.2 L 306.9 86.7 L 320.5 86.2 L 334.1 85.7 L 347.6 85.2 L 361.2 84.8 L 374.7 84.3 L 388.3 83.9 L 401.9 83.4 L 415.4 83.0 L 429.0 82.6 L 442.5 82.2 L 456.1 81.7 L 469.7 81.3 L 483.2 80.9 L 496.8 80.5 L 510.3 80.1 L 523.9 79.7 L 537.5 79.4 L 551.0 79.0 L 564.6 78.6 L 578.1 78.2 L 591.7 77.9 L 605.3 77.5 L 618.8 77.2 L 632.4 76.8 L 645.9 76.5 L 659.5 76.1 L 673.1 75.8 L 686.6 75.4 L 700.2 75.1 L 713.7 74.8 L 727.3 74.4 L 740.8 74.1 L 754.4 73.8 L 768.0 73.5 L 781.5 73.2 L 795.1 72.9 L 808.6 72.6 L 822.2 72.3 L 835.8 72.0 L 849.3 71.7 L 862.9 71.4 L 876.4 71.1 L 890.0 70.8" stroke="#ff6b6b" stroke-width="1.6" stroke-dasharray="7 5" fill="none"/>
<text x="117.6" y="85.1" fill="#ff6b6b" font-size="12" text-anchor="start" font-weight="normal">kırılma tavanı ν_max = (1/2π)√(𝒢M/R³),  R = 12 km</text>
<circle cx="255.5" cy="384.9" r="5" fill="none" stroke="#b58cff" stroke-width="1.6"/>
<text x="264.5" y="388.9" fill="#b58cff" font-size="11" text-anchor="start" font-weight="normal">Vela</text>
<circle cx="277.6" cy="360.5" r="5" fill="none" stroke="#b58cff" stroke-width="1.6"/>
<text x="286.6" y="364.5" fill="#b58cff" font-size="11" text-anchor="start" font-weight="normal">B1913+16</text>
<circle cx="343.2" cy="345.4" r="5" fill="none" stroke="#b58cff" stroke-width="1.6"/>
<text x="352.2" y="349.4" fill="#b58cff" font-size="11" text-anchor="start" font-weight="normal">J0453</text>
<circle cx="255.5" cy="326.7" r="5" fill="none" stroke="#b58cff" stroke-width="1.6"/>
<text x="264.5" y="319.7" fill="#b58cff" font-size="11" text-anchor="start" font-weight="normal">Crab</text>
<circle cx="221.3" cy="303.6" r="5" fill="#b58cff" stroke="#b58cff" stroke-width="1.6"/>
<text x="230.3" y="296.6" fill="#b58cff" font-size="11" text-anchor="start" font-weight="normal">J0737A</text>
<circle cx="535.8" cy="186.5" r="5" fill="#b58cff" stroke="#b58cff" stroke-width="1.6"/>
<text x="544.8" y="190.5" fill="#b58cff" font-size="11" text-anchor="start" font-weight="normal">J1614−2230</text>
<circle cx="630.7" cy="181.3" r="5" fill="#b58cff" stroke="#b58cff" stroke-width="1.6"/>
<text x="639.7" y="185.3" fill="#b58cff" font-size="11" text-anchor="start" font-weight="normal">J0740+6620</text>
<circle cx="779.7" cy="138.9" r="5" fill="#b58cff" stroke="#b58cff" stroke-width="1.6"/>
<text x="788.7" y="142.9" fill="#b58cff" font-size="11" text-anchor="start" font-weight="normal">J0952−0607</text>
<circle cx="255.5" cy="138.2" r="5" fill="#b58cff" stroke="#b58cff" stroke-width="1.6"/>
<text x="264.5" y="131.2" fill="#b58cff" font-size="11" text-anchor="start" font-weight="normal">J1748−2446ad</text>
<path d="M 283.1 317.3 C 448.6 261.3 586.6 189.8 741.0 148.7" stroke="#ffb84d" stroke-width="1.4" stroke-dasharray="3 4" fill="none"/>
<path d="M 741.0 148.7 l -12 -1 l 7 10 z" fill="#ffb84d"/>
<text x="376.9" y="213.9" fill="#ffb84d" font-size="12" text-anchor="start" font-weight="normal">beslenme zarfı: yığışma hem kütle hem dönüş yükler</text>
<text x="586.6" y="107.5" fill="#b58cff" font-size="11" text-anchor="middle" font-weight="normal">içi boş: genç (fırlatma sonrası kalıntı dönüş)</text>
</svg>
<p style="font-size:0.9em;color:#8fa3c0;margin:10px 4px 2px;"><em>Şekil 11.3.D: Kütlesi ölçülmüş pulsarlar. İçi boş: genç (fırlatma kalıntısı, a*~0,01); dolu: beslenme zarfıyla geri dönüştürülmüş — en ağırlar en hızlıdır. Kesikli eğri: kırılma tavanı.</em></p>
</div>

Bu sınıf, zarf çerçevesinin **üç ayrı sınavını** birden taşır:

**(i) Doğumda zorunlu boşaltma.** Çöken çekirdek gezegen-bandı katsayısını taşıyamaz: $\mathcal{A}_0\approx2\times10^{-16}$, kompakt tavanın ($\mathcal{G}/c$) ~900 katıdır; hatta yıldız-bandı katsayısı bile ($\sim10^{-18}$) tavanın ~10 katıdır. Çekirdek çökerken momentumun **>%99'unu bırakmak zorundadır** — teori bunu tavanın zorlamasıyla okur; gözlem tam bunu görür: genç pulsarlar $a^*\approx0{,}01$ ile doğar (Crab'ın geri-izlenen doğum dönemi ~19 ms), ve Kepler asterosismolojisi kırmızı dev **çekirdeklerinin** daha çökme başlamadan modellerin öngördüğünden 10–100 kat yavaş döndüğünü ölçmüştür (Mosser ve ark., 2012) — standart modellerin "kayıp fren" dediği kalem, tavana yaklaşan çekirdeğin erken salımıdır.

**(ii) Çıplak fren.** Zarfsız kalıntının tek kanalı manyetik dipol ışımasıdır: $\dot\omega\propto-\omega^n$, $n\approx3$ (Crab'da ölçülen $n=2{,}5$). $n=3$ integrali $\omega\propto t^{-1/2}$ verir — **açık kanallı yıldızların Skumanich üssüyle aynıdır.** İki bambaşka cisim sınıfında aynı $t^{-1/2}$: salım kanalı hangi fizikle açılırsa açılsın, momentumun ortama tek tip sızdığının işaretidir.

**(iii) Beslenme zarfı ve geri dönüş.** Yığışma diski kuran nötron yıldızları (düşük-kütleli X-ışını çiftleri) yeniden hızlanır ve milisaniye pulsarlarına dönüşür. Tablo bunun en sert biçimini gösterir: **en hızlı dönenler en ağır olanlardır** (J0952−0607: hem 707 Hz hem $2{,}35\,M_\odot$ — bilinen en ağır nötron yıldızı). Yığışan madde hem kütleyi hem dönüşü birlikte yükler; teori dilinde beslenme diski **geçici bir zarftır** ve zarf geri gelince kuplaj geri gelir (Kısım 3 §3.4.4'ün beslenme ölçütüyle aynı kayıt). Sınıf içi kütle–spin korelasyonu böylece **pozitif** işaretle geri döner — zarf hipotezinin ters yönlü doğrulaması.

Tavan burada da görünür: en hızlı pulsar (716 Hz) kırılma frekansının %43'ünde, $a^*=0{,}37$'dedir. Denge dönemi fiziği (yığışma torku ↔ manyetosfer) pulsarları tavana varmadan doyurur; tavanı dolduran tek sınıf bir sonrakidir.

---

## 11.3.6 Karadelikler: Zarf Yok — Tavanın Kendisi

Karadelik spini iki bağımsız teknikle ölçülür: X-ışını çiftlerinde iç disk yarıçapı (süreklilik uydurması / Fe Kα yansıması; Reynolds, 2021), birleşmelerde dalga biçimi (LIGO-Virgo). Boyutsuz spin $a^*=cJ/\mathcal{G}M^2$:

| Nesne | $M$ ($M_\odot$) | $a^*$ | Yöntem |
|---|---|---|---|
| A0620−00 | 6,6 | 0,12 | X-ışını sürekliliği |
| LMC X-3 | 7,0 | 0,25 | X-ışını sürekliliği |
| GRO J1655−40 | 6,3 | 0,70 | X-ışını sürekliliği |
| LMC X-1 | 10,9 | 0,92 | X-ışını sürekliliği |
| GRS 1915+105 | 12,4 | 0,98 | X-ışını sürekliliği |
| Cyg X-1 | 21,2 | >0,99 | iki yöntem uyumlu |
| GW150914 ürünü | 62 | 0,67 | GW halka-sönümü |
| GW190521 ürünü | 142 | 0,72 | GW halka-sönümü |
| NGC 1365 | $4{,}5\times10^6$ | 0,97 | Fe Kα |
| M87* | $6{,}5\times10^9$ | ~0,9 | EHT + jet gücü |

<div style="background:#0b0f19;border:1px solid rgba(0,240,255,0.2);border-radius:10px;padding:12px;margin:1.2em 0;">
<svg viewBox="0 0 940 520" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Segoe UI,sans-serif" role="img" aria-label="Karadeliklerde boyutsuz spin - kutle">
<rect x="0" y="0" width="940" height="520" fill="#0b0f19"/>
<line x1="130.8" y1="50" x2="130.8" y2="440" stroke="#182338"/>
<text x="130.8" y="458.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">10¹</text>
<line x1="212.4" y1="50" x2="212.4" y2="440" stroke="#182338"/>
<text x="212.4" y="458.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">10²</text>
<line x1="294.1" y1="50" x2="294.1" y2="440" stroke="#182338"/>
<text x="294.1" y="458.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">10³</text>
<line x1="375.7" y1="50" x2="375.7" y2="440" stroke="#182338"/>
<text x="375.7" y="458.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">10⁴</text>
<line x1="457.3" y1="50" x2="457.3" y2="440" stroke="#182338"/>
<text x="457.3" y="458.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">10⁵</text>
<line x1="539.0" y1="50" x2="539.0" y2="440" stroke="#182338"/>
<text x="539.0" y="458.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">10⁶</text>
<line x1="620.6" y1="50" x2="620.6" y2="440" stroke="#182338"/>
<text x="620.6" y="458.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">10⁷</text>
<line x1="702.2" y1="50" x2="702.2" y2="440" stroke="#182338"/>
<text x="702.2" y="458.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">10⁸</text>
<line x1="783.9" y1="50" x2="783.9" y2="440" stroke="#182338"/>
<text x="783.9" y="458.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">10⁹</text>
<line x1="865.5" y1="50" x2="865.5" y2="440" stroke="#182338"/>
<text x="865.5" y="458.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">10¹⁰</text>
<line x1="90" y1="440.0" x2="890" y2="440.0" stroke="#182338"/>
<text x="82.0" y="444.0" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">0,0</text>
<line x1="90" y1="367.8" x2="890" y2="367.8" stroke="#182338"/>
<text x="82.0" y="371.8" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">0,2</text>
<line x1="90" y1="295.6" x2="890" y2="295.6" stroke="#182338"/>
<text x="82.0" y="299.6" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">0,4</text>
<line x1="90" y1="223.3" x2="890" y2="223.3" stroke="#182338"/>
<text x="82.0" y="227.3" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">0,6</text>
<line x1="90" y1="151.1" x2="890" y2="151.1" stroke="#182338"/>
<text x="82.0" y="155.1" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">0,8</text>
<line x1="90" y1="78.9" x2="890" y2="78.9" stroke="#182338"/>
<text x="82.0" y="82.9" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">1,0</text>
<rect x="90" y="50" width="800" height="390" fill="none" stroke="#8fa3c0"/>
<text x="490.0" y="480.0" fill="#8fa3c0" font-size="14" text-anchor="middle" font-weight="normal">kütle M [M☉]</text>
<text x="26" y="245.0" fill="#8fa3c0" font-size="14" text-anchor="middle" transform="rotate(-90 26 245.0)">boyutsuz spin  a* = cJ/𝒢M²</text>
<text x="90.0" y="32.0" fill="#e6eefb" font-size="15" text-anchor="start" font-weight="500">Şekil 11.3.E — Karadelikler tavana yaslanır: a* = 1 (girdap çekirdeği sınırı)</text>
<line x1="90" y1="78.9" x2="890" y2="78.9" stroke="#ff6b6b" stroke-width="1.8" stroke-dasharray="8 5"/>
<text x="884.0" y="70.9" fill="#ff6b6b" font-size="12" text-anchor="end" font-weight="normal">a* = 1  tavan</text>
<line x1="90" y1="79.6" x2="890" y2="79.6" stroke="#ffb84d" stroke-width="1" stroke-dasharray="2 5"/>
<text x="424.7" y="95.1" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">yığışma dengesi (Thorne 0,998)</text>
<circle cx="116.1" cy="396.7" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="124.1" y="400.7" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">A0620-00</text>
<circle cx="118.1" cy="349.7" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="126.1" y="353.7" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">LMC X-3</text>
<circle cx="127.5" cy="317.2" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="135.5" y="321.2" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">XTE J1550</text>
<circle cx="114.4" cy="187.2" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="122.4" y="201.2" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">GRO J1655</text>
<circle cx="146.7" cy="136.7" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="154.7" y="150.7" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">M33 X-7</text>
<circle cx="133.9" cy="107.8" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="49.9" y="111.8" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">LMC X-1</text>
<circle cx="138.4" cy="86.1" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="146.4" y="102.1" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">GRS 1915+105</text>
<circle cx="157.5" cy="82.5" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="165.5" y="80.5" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">Cyg X-1</text>
<path d="M 195.5 192.1 L 201.5 198.1 L 195.5 204.1 L 189.5 198.1 Z" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="203.5" y="210.1" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">GW150914</text>
<path d="M 224.9 174.0 L 230.9 180.0 L 224.9 186.0 L 218.9 180.0 Z" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="232.9" y="174.0" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">GW190521</text>
<rect x="587.3" y="84.7" width="10" height="10" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="600.3" y="83.7" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">NGC 1365</text>
<rect x="566.5" y="106.4" width="10" height="10" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="565.5" y="127.4" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">MCG−6-30-15</text>
<rect x="648.1" y="110.0" width="10" height="10" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="661.1" y="127.0" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">Mrk 335</text>
<rect x="669.7" y="110.0" width="10" height="10" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="682.7" y="109.0" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">NGC 4151</text>
<rect x="711.6" y="203.9" width="10" height="10" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="724.6" y="212.9" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">Ark 120</text>
<rect x="731.1" y="247.2" width="10" height="10" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="744.1" y="256.2" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">Fairall 9</text>
<rect x="845.2" y="110.0" width="10" height="10" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="858.2" y="119.0" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">M87*</text>
<text x="130.8" y="411.1" fill="#ff6b6b" font-size="12" text-anchor="start" font-weight="normal">● X-ışını çifti   ◆ GW birleşme ürünü   ■ AGN (Fe Kα yansıması)</text>
</svg>
<p style="font-size:0.9em;color:#8fa3c0;margin:10px 4px 2px;"><em>Şekil 11.3.E: Karadelik spinleri tavana yaslanır. X-ışını çiftleri (●), GW birleşme ürünleri (◆, ~0,7 — yörünge momentumundan), AGN (■). Kesikli çizgi a*=1; noktalı çizgi Thorne doyması 0,998.</em></p>
</div>

Üç okuma:

1. **Tavan gerçektir ve doldurulur.** 17 nesnenin hiçbiri $a^*=1$'i aşmaz; X-ışını çiftlerinin yarısı 0,9'un üstüne, yığışma dengesinin kuramsal doyma noktasına (Thorne, 1974: $a^*=0{,}998$) yaslanır. $J=\mathcal{A}M^2$ biçimi burada saf hâliyle görünür: $\mathcal{A}\to\mathcal{G}/c_{yerel}$.
2. **GW birleşme ürünleri ~0,7'de kümelenir** — bu değer spinden değil, birleşen çiftin **yörünge** momentumunun yutulmasından gelir (son yörüngenin momentumu tavanın ~0,7'sini doldurur); birleşme öncesi bireysel spinler çoğunlukla düşüktür ($\chi_{eff}\approx0$–$0{,}3$). Yörünge–spin ayrımı burada da korunur.
3. **Teorinin okuması ve ayrıştırıcı öngörü.** Standart fizikte $a^*\le1$ Kerr geometrisinin mutlak sınırıdır. Evrenakı'da bu tavan, girdap çekirdeğinin yerel dalga hızıyla ($c_{yerel}=\sqrt{P/\rho}$, Postülat 4) kurduğu sınırdır — **mutlak değil, ortama bağlıdır.** İki teori burada ilk kez ayrışır: tek bir kompakt nesnede $a^*>1$ güvenilir biçimde ölçülürse standart çerçeve çöker; Evrenakı ise bunu yerel ortam basıncının farklılaştığı bir bölge olarak okur. Bugünkü veri tavana saygılıdır; ayrım açık bir gözlemsel bahis olarak kayda geçirilir.

---

## 11.3.7 4B'den 3B'ye: Dönüşün Kaynağı ve $M^2$ Yasası

Gözlem dört sınıfta aynı biçimi verdi; şimdi biçimin kendisi türetilir.

**Kaynak.** Kısım 1 §1.4'ün sonucu: dört boyutta dönüş bir eksen etrafında değil, bir **düzlem içinde** olur ve W-eksenli bileşeni 3B kesitte dönüş olarak değil, üç dolaylı imzayla görünür. Kütleyi oluşturan her nükleon bu 4B çift-dönüşü taşır ve onu ortama **deşarj eder** (Kısım 3 §3.1.3-B, §3.2.2). Kısım 3 §3.4.4'ün motor–gösterge ayrımı buradan gelir: makro-girdabın motoru gövdenin mekanik devri değil, nükleon deşarjlarının toplamıdır; mekanik spin bu motorun ortamda bulabildiği ifadenin **göstergesidir.**

**$M^2$'nin türetimi.** İki orantı yeterlidir:

1. Girdap dolaşımı deşarj toplamıyla ölçeklenir: $\Gamma\propto N_{nükleon}\propto M$ — motor kütleyle doğrusal.
2. Bu girdabın gövdenin kendisine geri uyguladığı yükleme torku, gövdenin kavrama kesitiyle — yine deplase eden nükleon sayısıyla — ölçeklenir: $\tau\propto\Gamma\times M\propto M^2$.

Oluşum penceresi boyunca biriken dönme momentumu böylece **öz-kavrama karesi** verir:

$$\boxed{\;L_{doğum}=\mathcal{A}_0\,M^{2}\;}\qquad \mathcal{A}_0\approx2\times10^{-16}\ \mathrm{m^2\,s^{-1}\,kg^{-1}}\ \ (\text{gezegen kalibrasyonu; bant }1{,}2\text{–}4{,}6)$$

Aynı akıl yürütme ortak yönü de verir: tek 4B kaynak, sisteme tek işaretli toplam yükler (Kısım 3 §3.4.4, "ortak yön imzası"). Ve tavanla buluşma kendiliğindendir: kompakt cisimde ifadenin üst sınırı $L_{max}=\mathcal{G}M^2/c_{yerel}$ — **aynı $M^2$, başka katsayı.** Yükleme yasası ile tavan arasındaki ~900 kat, bu bölümün bütün dinamiğini kurar: zarfını koruyan gövde yükünü taşır; zarfını yitirip küçülen gövde taşıyamaz ve boşaltır.

**Üs kaydı (dürüstlük).** Ölçülen üsler tam 2 değildir: gezegenlerde 1,89–1,94. $\mathcal{A}$'nın gövdeden gövdeye ±%30 bandı ve $\lambda$ belirsizlikleri bu sapmayı örter; üssün 2'den ayrık olup olmadığı, kütle menzili genişletilerek (genç dev ötegezegenler, kahverengi cüceler) sınanacak açık kalemdir.

---

## 11.3.8 Zarf-Bağımlı Matematik: Tek Denklem, Dört Rejim

Bütün sınıflar tek yapıda toplanır:

$$\boxed{\;L(M,t)\;=\;\min\!\Bigl[\,\mathcal{A}_0\,M^{2}\,\eta_z(t)\;,\;\frac{\mathcal{G}M^{2}}{c_{yerel}}\,\Bigr]\;}$$

Burada $\eta_z(t)$ zarf ifade çarpanıdır — gövdenin zarf durumunun yükleme yasasından ne kadarını ifade edip koruyabildiği:

| Rejim | Zarf durumu | $\eta_z(t)$ | Sonuç | Sınav |
|---|---|---|---|---|
| **R1** | rijit zarf (katı/buz/dev gaz kafesi), kanal kapalı | $\eta\approx1$, sabit | $L=\mathcal{A}_0M^2$ korunur | gezegen doğrusu (Şekil 11.3.B) |
| **R2** | plazma zarf, manyetize rüzgâr = açık kanal | $\eta_i\,(1+t/\tau_z)^{-1/2}$; $\eta_i\sim10^{-2}$ (oluşum kaybı) | Skumanich $\omega\propto t^{-1/2}$; Kraft kırılması = kanal anahtarı | T Tauri→Güneş oranı 72 ↔ 68 (%6) |
| **R3** | zarf fırlatılmış (çıplak çekirdek) | çökmede tavana kırpılır; sonra dipol $(1+t/\tau_d)^{-1/2}$; beslenme zarfı kurulursa $\dot L=+\dot m\sqrt{\mathcal{G}MR_{iç}}$ | doğum $a^*\sim0{,}01$; MSP'lerde ağır=hızlı | Şekil 11.3.D |
| **R4** | zarf yok, ufuk var | $\eta=1$ **tavanda** | $a^*\to1$ doyması | Şekil 11.3.E |

Rejim ayrıntıları:

- **R1'in istisnası dış kavramadır:** rejimin kendi kanalı kapalıyken, baskın bir dış girdap ifadeyi dışarıdan yutabilir (M-24; Merkür/Venüs, $g=0{,}98/1{,}00$). Bu, $\eta_z$'nin değil, yükleme teriminin önüne gelen $(1-g)$ çarpanının işidir: $L=(1-g)\,\mathcal{A}_0M^2$.
- **R2'de iki kayıp ayrışır:** oluşumda beslenme diskine bırakılan pay ($\eta_i\sim10^{-2}$ — yıldızlar gezegen bandının ~100 kat altında doğar) ve ömür boyu rüzgâr sızıntısı ($t^{-1/2}$). İkincisi yalnız konvektif zarfta çalışır; radyatif zarflı O–A yıldızları $\eta_i$'de donar.
- **R3'ün üç fazı** aynı cismin biyografisidir: kırpılma (süpernova/disk boşaltması) → çıplak fren ($t^{-1/2}$; genç pulsarlar) → istersen yeniden yükleme (beslenme zarfı; MSP'ler). Kırmızı dev çekirdeklerinin erken yavaşlaması (Mosser ve ark., 2012), kırpılmanın çökme **öncesinde** başladığını gösterir — tavan yaklaşırken salım artar.
- **R4'te** $c_{yerel}$ kaydı geçerlidir (§11.3.6/3): tavan yerel $\sqrt{P/\rho}$ ile kurulur, evrensel bir sabitle değil.

**Yanlışlanabilir öngörüler.**

1. **İzole genç kahverengi cüceler** R1–R2 arasındadır ve $\mathcal{A}_0M^2$ uzantısının ±%30 bandına oturmalıdır (Kısım 3 §3.4.4'ün kapsam-içi sınavıyla aynı kalem; dönme istatistikleri kısmen mevcuttur).
2. **Genç dev ötegezegenler** büzülme tamamlandıkça gezegen doğrusuna yaklaşmalıdır; β Pic b'nin bugün doğrunun altında olup $J$-korunumlu büzülmeyle banda girmesi ilk örnektir — ikinci ve üçüncü spin ölçümleri (CRIRES+/ELT) doğrudan sınavdır.
3. **Tek bir kompakt nesnede $a^*>1$**: standart çerçeve için ölümcül, Evrenakı için $c_{yerel}$ değişiminin işareti — iki teoriyi ayıran en keskin gözlemsel bahis.
4. **Eksen eğikliği–dönüş korelasyonu:** hizasız gövdelerin (Uranüs benzeri) yükleme verimi düşükse, ötegezegen popülasyonunda eğiklik ile $\mathcal{A}$ arasında negatif korelasyon beklenir (Kısım 3 §3.4.4'ün hizalanma ölçütü).
5. **MSP popülasyonunda kütle–frekans pozitif eğilimi** güçlenerek sürmelidir: beslenme zarfı kütle ve momentumu birlikte taşır; kütlesi ölçülecek her yeni >500 Hz pulsarın $>1{,}8\,M_\odot$ çıkması beklenir.

---

## 11.3.9 Hüküm

| | Standart fizik | Evrenakı |
|---|---|---|
| Gezegen spini | disk türbülansı kalıntısı (rastlantı) | 4B yükleme $\mathcal{A}_0M^2$, rijit zarf korur |
| Yıldız spini | manyetik frenleme (ayrı mekanizma) | aynı yükleme, açık kanallı plazma zarf sızdırır |
| NS spini | AM korunumu + dipol (ayrı mekanizma) | aynı yükleme, tavan kırpar, çıplak fren, beslenme zarfı geri yükler |
| Karadelik spini | Kerr geometrisinin sınırı (ayrı ilke) | aynı $M^2$'nin tavan katsayısı; $c_{yerel}$ ile |
| Sınıflar arası bağ | **yok** — dört bağımsız anlatı | **tek kaynak, tek biçim, tek değişken (zarf)** |

Dürüst kapanış üç cümledir. Parçaların her biri — Skumanich yasası, dipol freni, Kerr sınırı, geri dönüştürme — standart astrofizikte tek tek bilinir ve teorinin bunları yeniden keşfetmesi bir zafer değildir. Teorinin katkısı çatıdır: dört sınıfın da $J=\mathcal{A}M^2$ biçimini paylaşması, katsayıların zarf durumuyla kademelenmesi ($2\times10^{-16}\to\mathcal{G}/c$), gezegen bandı ile kompakt tavan arasındaki ~900 katın "çöken çekirdek boşaltmak zorundadır" öngörüsüne dönüşmesi ve iki bağımsız sınıfta ($t^{-1/2}$) aynı sızıntı üssünün çıkması — bunlar standart çerçevede dört ayrı bölümün dipnotlarıdır, burada tek denklemin dört satırıdır. Ve çerçeve bahsini koymuştur: $a^*>1$ tek gözlem, kahverengi cüce bandı, MSP kütle–frekans eğilimi — üçü de önümüzdeki on yılın verisiyle sınanabilir.
