# 12.0 Temel Sözleşme: Tanımlar, Hükümler ve Statü Envanteri

Kısım 12, bu kitabın matematik temelidir: sonraki her türetim buradaki tanımlara ve hükümlere dayanacak, önceki kısımların matematiği de elden geçirilirken bu sözleşmeye hizalanacaktır. Bu bölüm o sözleşmeyi tek yerde toplar. Burada yeni fizik yoktur; burada olan şey, dağınık kaldığında pahalıya mal olan **tanım ve statü kararlarının** tek tek sabitlenmesidir.

---

## 12.0.1 Kanonik Gösterim: İki Açısal Hızın Sözlüğü

4B çift dönüşün iki açısal hızı bu kitapta **değişmez düzlem hızları** olarak tanımlıdır:

| Sembol | Tanım | 3B kesitte görünümü |
|---|---|---|
| $\omega_1$ | Kesitimizin içindeki değişmez düzlemin açısal hızı | Doğrudan dönme (dolanım) |
| $\omega_2$ | $W$ eksenini içeren değişmez düzlemin açısal hızı | Pulsasyon (boyutsal salınım) |

**İzoklinik dönüş ölçütü:** $\omega_1 = \omega_2$.

Bu sözlük kanoniktir. Rijit cisim (Euler açıları) diliyle çalışan bölümlerde çeviri şudur: duruş hızları $\dot\phi$ (görünür dönme) ve $\dot\psi$ (öz-dönme) ile değişmez düzlem hızları

$$\Omega_\pm = \frac{\dot\phi \mp \dot\psi}{2}$$

bağıntısıyla ilişkilidir. Kısım 1.4'ün $\varepsilon\cos\theta$ bağıntısı bu çeviriyle okunur: oradaki oran $\dot\psi/\dot\phi$ oranıdır ve $\varepsilon\to0$ limitinde $\dot\psi\to0$, yani $\Omega_+=\Omega_-$ — izoklinik dönüş. İki sözlük aynı fiziği anlatır; **"$\omega_2$" adı yalnız düzlem-hızı anlamında kullanılır.** Önceki kısımlarda bu adın öz-dönme anlamında geçtiği yerler, geriye dönük düzenlemede bu sözlüğe çevrilecektir.

**Sembol ayrımları:** Kısım 12'de $\varepsilon$, Kut'un 4B yarıçap ölçeğidir; Kısım 1.4'te aynı harf dinamik eliptiklik $(C-A)/C$ için kullanılıyordu — geriye dönük düzenlemede eliptiklik ayrı bir simgeye ($e_d$) taşınacaktır. Dolanım ölçeği SI'da boyutludur: $K_{\mathrm{SI}}=\Gamma/2\pi=\sqrt2\,c_0r_e$ (m²/s); simülasyonun boyutsuz $K=\sqrt2$'si bunun model-birim değeridir.

---

## 12.0.2 Hız Hükümleri

**Hüküm 1 — $c_0$ tavan değildir.** $c_0$, ortamın ses (basınç-iletim) hızıdır; Postülat 4 gereği evrensel bir sınır değildir. Ortamda $c_0$'ı aşan hızlar vardır ve bu kısım onları hesaplar.

**Hüküm 2 — üst hız $v_{\text{kav}}$'dır ve biçimi şudur:**

> **Sürekli Evrenakı akışında $|v| \le v_{\text{kav}}$. Eşitlikte ortam yırtılır:** akış sürekli olmaktan çıkar, faz değiştirir ve Kut doğar (12.1.2). $v > v_{\text{kav}}$ değerine sahip **sürekli akış durumu yoktur.**

Bu bir yasak değil, sürekli çözümün **var olmama** koşuludur; Ek A'nın "eşiği aşmak yasak değildir — ortam yırtılır, madde doğar" hükmüyle aynı içeriğin kesin yazımıdır. İki ifade geriye dönük düzenlemede bu biçimde birleştirilecektir.

**Hüküm 3 — $M_{\text{kav}}$ şimdilik alt sınırdır.** $\Sigma/P_0 \gtrsim 1{,}9\times10^9$ bir alt sınır olduğu sürece

$$M_{\text{kav}} \gtrsim 6{,}164\times10^4$$

yazılır; kesin değer $\Sigma$ kesinleşince belirlenir. Evren içindeki bütün hızlar bu üst hızın alt ölçekli türevleridir.

---

## 12.0.3 Kavitasyon Ölçütünün Tanımı

$$\boxed{\;\tfrac12\rho_0 v^2 \;>\; P_0 + \Sigma \;\Longrightarrow\; \text{yırtılma}\;}$$

$\Sigma$, ortamın **çekme (kohezyon) dayanımıdır** ve taban girdidir. $v_{\text{kav}} = \sqrt2\,c_0\sqrt{1+\Sigma/P_0}$ ile $R_{\text{cep}} = r_e/\sqrt{1+\Sigma/P_0}$ bu tanımın doğrudan sonuçlarıdır.

**Ayrım beyanı:** yoğunluk profili $\rho=\rho_0e^{-(r_e/R)^2}$, sıkıştırılabilir Bernoulli'den ($v^2/2 + c_0^2\ln\rho = \text{sabit}$) gelir ve hâl denklemiyle tam tutarlıdır. Yırtılma ölçütü ise akışın değil **malzemenin** özelliğidir (dayanım) ve ayrı bir yasadır. İkisi karıştırılmamalıdır: profil akışı, $\Sigma$ kopmayı anlatır. $R_{\text{cep}}(\Sigma)$ bağıntısı bu tanıma bağlıdır; tanım değişirse bağıntı da değişir — bu yüzden tanım burada sabitlenmiştir.

---

## 12.0.4 Küresel Faz Hükmü

Bjerknes bağ kanalı (12.3.2) yalnız **eş fazlı** pulsasyon için çekicidir. Aynı frekans tek başına aynı fazı garanti etmez: $\phi_i(t)=\omega_2t+\phi_{i0}$ yazımında başlangıç fazları $\phi_{i0}$ serbest kalabilirdi. Teorinin hükmü bu boşluğu kapatır ve açıkça beyan edilir:

> **Kutlar bağımsız osilatörler değildir; hepsi tek bir küresel 4B dönüşün yerel kesitleridir.** Ortak olan yalnız $\omega_2$ değil, dönüşün kendisidir — dolayısıyla faz da ortaktır: $\phi_{i0}$ diye bağımsız bir serbestlik yoktur.

Bu, kurucu bir hükümdür (postülat statüsünde) ve bağ mekanizmasının önkoşuludur. Sınanabilir sonucu vardır: faz uyumu bozulmuş bir Kut topluluğu bağ kuramazdı; kümeleşmenin evrenselliği (12.3.6) bu hükmün dolaylı sınavıdır.

---

## 12.0.5 Statü Envanteri

Her büyüklüğün ve yasanın statüsü — neyin aksiyom, neyin girdi, neyin türetilmiş, neyin açık olduğu:

| Kalem | Statü |
|---|---|
| $P = c_0^2\rho$ hâl denklemi | **Aksiyom** (postülatlardan; Zel'dovich'ten yalnız matematiksel biçim — 12.1.1) |
| Tek küresel 4B çift dönüş + $w=0$ kesit okuması | **Aksiyom** (küresel faz hükmü dahil — 12.0.4) |
| $\Sigma$ kohezyon dayanımının varlığı ve ölçütü | **Aksiyom + ölçülen girdi** (12.0.3; değeri alt sınır) |
| İdeal akışkan / Kelvin çerçevesi | **Aksiyom** (makro akışkan mekaniğinin devri — 12.5.1); Kelvin ayrıca birleşik eylemin Noether sonucudur (Ek M-50) |
| Birleşik eylem iskeleti (girdap + çift dönüş + kohezyon) | **Kuruldu (yapı)** — Ek M-50: profil, Euler, Kelvin, nokta-girdap korunumları eylemden; çift dönüş = 4B vortisitenin Darboux ayrışımı; pertürbatif kanal türetimleri açık |
| $\rho_0$, $P_0$, $\Sigma/P_0$ | **Ölçülen girdi** (taban tablo — 12.1.1) |
| Yoğunluk profili, $R_{\text{cep}}$, $v_{\text{kav}}$, hız merdiveni | **Türetilmiş** (12.1) |
| Üç imza ve tamlığı | **Türetilmiş** (üreteç sayımı — 12.2.3) |
| Bağ dinamiği, $d_{\text{denge}}$, işaret yapısı | **Katmanlı:** indirgenmiş skaler yasa ölçülmüş/kalibre edilmiştir; temel kapanış, aynı gecikmeli Green çekirdeğinden çıkan $(\mathcal R,\mathcal T,F_L)$ ile iki bağlı Green–Magnus denklemidir ve nicel çözümü açıktır (12.3) |
| $\Omega_N$, $\Omega_{\text{yörünge}}$, impuls aktarımı | **Türetilmiş** (12.4; nokta girdap dinamiği kesin) |
| Ölçek değişmezliği $d\propto N$, $r_e(\text{Kutam})=|\sum g|r_e$ | $r_e(\text{Kutam})$ **türetilmiş + ölçülmüş**; $d\propto N$ indirgenmiş modelde tamdır, temel çekirdekte $q_N$ ve kaynak-genliği öz-benzerlik koşullarını bekler (12.3.7, 12.5) |
| $\kappa$ | **Türetildi (kapalı biçim):** $\kappa_{\mathrm{SI}}=\rho_0\omega_2^2\Delta V^2/2\pi$ (12.3.2); kalan iş $\varepsilon$, $A_w$, $\omega_2$ özdeşleştirmesidir |
| Kuvvet–hareket köprüsü | **Boyutça kapalı, nicel çekirdek açık:** Magnus yasası radyal ve teğetsel Bjerknes bileşenlerini $(\Omega_{\text{orb}},\dot d)$'ye bağlar. $\mathcal R$, $\mathcal T$ ve $F_L$ aynı gecikmeli Green çözümünden türetilecektir; bunlar yeni sabit değildir. $M_K=1$ yalnız çıplak dolaşım sonucudur, gerçek $M_{\text{orb}}$ bağlı denklemden çıkar (12.3.4). |
| $\vec\omega_1\parallel\vec\omega_2$ hizalanması (koordinat-çifti biçimi) | **Varsayım** — kanonik biçimin seçilme gerekçesi ayrı türetim bekler (12.2.1) |
| Terslenme–kaybolma kilidi ($A_w=\varepsilon$, faz 0) | **Model varsayımı**; kırık kilit ayrı bir gözlenebilir sunar (12.2.3) |
| Kuadrupol yanıtı $F_L$ | **Düşük-Mach özel sınırı hesaplandı:** $C_L^{(0)}=8\pi^2$, $C^{(0)}=1$. İşletme noktasındaki $F_L(M_{\text{orb}},\ldots)$, $\mathcal R$ ve $\mathcal T$ ile birlikte tam çekirdekten çıkacaktır (12.3.3–12.3.4). |
| İlk dönmenin kaynağı | **Bilinmiyor, beyan edildi** (12.1.5) |
| $\Gamma$'nın nicemlenip nicemlenmediği | **Açık** (12.4.8) |

Bu tablo, geriye dönük düzenlemenin yol haritasıdır: önceki kısımlarda bu statülerle çelişen her ifade, bu sözleşmeye çevrilecektir.
