# Ek M — Merkezî Türetim Kataloğu · Blok H: Beş Hidrodinamik Kuvvetin Matematiği

Şablon ve rozet sistemi için bkz. Blok A (M-1..M-6) girişi.

**Blokun kapsamı.** Postülat 9'un beş hidrodinamik kuvvetinin nicel altyapısı (M-35..M-39) ve dönme sürüklenmesinin iki gözlemlenebiliri: jiroskop spini (M-40) ile yörünge düzlemi (M-41). Bölüm 3.2 bu kuvvetleri mekanizma düzeyinde kurar ve $\omega_1/\omega_2$ köken haritasını verir; bu blok her birinin uzaklık yasasını, kapalı biçimini ve geçerlilik penceresini türetir. Beşinin tamamı iki köke ve — göreceğimiz üzere — yalnız üç serbest kaleme iner. Blok iki kuvvet-olmayan girdiyle kapanır: kuvvetlerin ölçüm çerçevesini sabitleyen **M-42** (ölçek yapısı $\Lambda$) ve sürükleme hesaplarının rejimini sabitleyen **M-43** (altkritik bastırma). M-42 için: potansiyelin cetvel, saat ve yayılma hızını hangi üslerle ölçeklediği belirlenmeden hiçbir uzaklık yasası gözlemle karşılaştırılamaz.

---

## H.0 Blok Ortak Çerçevesi

### Köken haritası (Bölüm 3.2 ile ortak)

| Bileşen | 3B'ye yansıması | Doğurduğu kuvvetler |
|---|---|---|
| $\omega_2$ — W eksenli bileşen | **Pompa** (Boyutsal Salınım / pulsasyon) | **M-35** Radyal kütle-itimi · **M-36** Diferansiyel sıkıştırma (gelgit) · *(alanın ölçek yapısı:* **M-42***)* |
| $\omega_1$ — 3B-içi bileşen | **Dönüş** (görünür spin, makro-vorteks) | **M-37** Vorteks sürüklenmesi · **M-38** Eksenel itim · **M-39** Yanal itim · **M-40** Dönme sürüklenme kesri |

### Bu blokta tanımlanan parametreler

| Sembol | Anlam | Birim | Statü |
|---|---|---|---|
| $q_n$ | Nükleon başına pulsasyon hacim debisi ($\omega_2$ kaynak şiddeti) | m³·s⁻¹ | **F** |
| $C$ | Ortamın deplasman→basınç direnç katsayısı | kg·m⁻³·s⁻¹ | **F** |
| $\kappa_5$ | Yanal itim deplasman kapanış katsayısı | boyutsuz | **F**, $\lesssim0{,}1$ (Dünya basıklığından, M-39) |
| $\phi$ | Deplasman hacim kesri $=1-1/n^2$; **iç kavrama kesri** $\mathcal{R}=\phi$ | boyutsuz | **T** (M-15/M-16) — serbest değil |
| $r_0$ | $1/R^2 \to 1/R$ rejim geçiş yarıçapı (Rankine) | m | **F** (Ek C P1 ile bağlı) |
| $\Lambda$ | Yerel madde ölçek çarpanı, $1-\Phi/c^2$ ($\ell,f\propto\Lambda$; $c_{loc}\propto\Lambda^2$) | boyutsuz | **T** (M-42) — serbest değil |
| $n$ | Altkritik bastırma üssü, $F\propto(v/v_{kav})^{n}$ | boyutsuz | **S** (M-43); $n\simeq3$, Phoebe'den |

> $C$ ve $q_n$ bağımsız değildir; gözleme yalnız **$Cq_n$ çarpımı** bağlanır. Ek C'de tek kalem olarak sayılmalıdır.

Notasyon: Anayasa R-4 (kuyu konvansiyonu, $dP/dr>0$, kuvvet $-\nabla P$), R-6 ($\rho_n=2{,}7\times10^{17}$ kg/m³), S-14 ($r$ küresel yarıçap, $R$ eksene dik uzaklık).

---

## M-35 · Radyal (Merkezcil) Kütle-İtimi: $\alpha$'nın Ayrıştırılması · **[T (yapı) / F ($Cq_n$)]**

**Kullanıldığı bölümler:** 3.2.1 (Kuvvet 1), 1.5, 3.4.1, 4.2.4. Bağlı katalog: M-2, M-28, M-29.

### Varsayımlar

1. **Küresel akı geometrisi:** Pulsasyon kaynağı izotropiktir; deplasman akısı $4\pi r^2$ üzerinde seyrelir (M-29 ile aynı argüman).
2. **Doğrusal ortam tepkisi:** Yerel akı yoğunluğu ile basınç gradyanı doğru orantılıdır; katsayı $C$.
3. **Toplanabilirlik:** $N$ nükleonun debisi toplanır ($Q=Nq_n$), kütle $M=Nm_n$.
4. **Kutup yalıtımı:** Dönme ekseni üzerinde M-38 simetriden, M-39 ise $\sin2\theta|_{90°}=0$'dan sıfırdır. Kutup, bu kuvveti yalıtan tek temiz noktadır.

### Adımlar

1. Akı yoğunluğu:
$$\Phi_q(r) = \frac{N q_n}{4\pi r^2}$$

2. Ortam tepkisi (kuyu konvansiyonu — basınç merkezden uzaklaştıkça **artar**):
$$\frac{dP}{dr} = +\,C\,\Phi_q(r) = \frac{C\,N q_n}{4\pi r^2} \;>\;0$$

3. İntegral M-28'in profilini verir: $P(r) = P_0 - \dfrac{CNq_n}{4\pi r}$ ✓

4. Kütle-itim yasası (M-2) uygulanır ve $N=M/m_n$ konur:
$$a_r = -\frac{1}{\rho_n}\frac{dP}{dr} = -\frac{C\,N q_n}{4\pi \rho_n r^2}$$

### Sonuç

$$\boxed{\;a_r = -\left(\frac{C\,q_n}{4\pi\,\rho_n\,m_n}\right)\frac{M}{r^2}\;}$$

M-28 zaten $P(r)=P_0-\alpha M/r$ ve $\mathcal{G}=\alpha/\rho_n$ vermişti; $\alpha$ orada **[S]** statüsündeydi. Bu türetim onu ayrıştırır:

$$\boxed{\;\alpha = \frac{C\,q_n}{4\pi\,m_n}\;,\qquad \mathcal{G} = \frac{\alpha}{\rho_n} = \frac{C\,q_n}{4\pi\,\rho_n\,m_n}\;}$$

**Boyut denetimi** (Ek D, $\alpha$ için $[\mathrm{s^{-2}}]$):

$$[\alpha] = \frac{[\mathrm{kg\,m^{-3}s^{-1}}]\cdot[\mathrm{m^3 s^{-1}}]}{[\mathrm{kg}]} = \mathrm{s^{-2}}\;\checkmark \qquad [\mathcal{G}] = \frac{\mathrm{s^{-2}}}{\mathrm{kg\,m^{-3}}} = \mathrm{m^3 kg^{-1}s^{-2}}\;\checkmark$$

İki bağımsız yoldan gelen boyutların birebir tutması, ayrıştırmanın temel desteğidir. **Kazanç:** $\alpha$ artık fenomenolojik bir katsayı değil, nükleon-ölçeği bir debinin makro izdüşümüdür — M-28'in açık ucunun cevabı.

### Geçerlilik Sınırı

- İzotropik kaynak varsayımı gereği **küresel simetrik** kütleler için birebir; asimetrik geometride $\nabla P_r$'nin açısal yapısı devreye girer (1.5, 3.3).
- $C$'nin basınçtan bağımsız olduğu zayıf sıkışma rejimi ($k\ll1$; M-1, Yön Kuralı).
- Gözlem $GM$ *çarpımlarını* on haneye kadar sabitler; belirsiz olan yalnız $G$ ile $M$ arasındaki bölüşümdür. Model $GM$'leri değiştirmez, yorumlar.

### Açık Uçlar

- $q_n$'nin $\omega_2$ frekansı ve nükleon deplasman hacminden hesabı → $\alpha$ tamamen türetilmiş olur. *(Aday kapanış M-45'tedir: $q_n=4\pi r_n^2\sqrt2c\sqrt{m_p/m_e}=1{,}62\times10^{-19}$ m³/s.)*
- ~~$C$ ile M-1'in hâl katsayısı $A$ arasındaki ilişki~~ → **kimlik kuruldu**: $A=P_0/\rho_0=c^2$ (dalga kanalının sertliği) ve iki kanalın empedans oranı kapalı biçimde $\dfrac{C\,\ell_\omega}{\rho_0c}=2\sqrt2\,\dfrac{\mathcal{G}m_n/c^2}{r_n}=4{,}2\times10^{-39}$'dur — kütle-itimin zayıflık hiyerarşisi tek boyutsuz sayıda. $\chi$-yayılım terimi **M-46'da yazılmıştır** — profil ve kütle-itim artık eylemden çıkar, $C$'nin kimliği hâl denkleminin ikinci katsayısıdır ($-(\partial P/\partial\chi)_\rho$); kalan iş yalnız $C$'nin **değerinin** mikro türetimidir ($\mathcal{G}$'nin — dolayısıyla yerel ölçülen $G$ değerinin — türetimine eşdeğer). *(Tuzak kaydı: $C\approx3{,}8\rho_nH_0$ görünümü $a_0\sim cH_0$ rastlantısının aynısıdır; yüksek-$z$ sınavı kozmik okumayı dışlamıştır — $C$, $H_0$'a bağlanamaz.)*

---

## M-36 · Gelgit Tensörü ve Denge Gelgiti · **[T]**

**Kullanıldığı bölümler:** 3.2.1 (Kuvvet 2), 3.9.2–3.9.2.2, **11.1** (tam türetim ve ayırt edici sınav). Bağlı katalog: M-26 (hidrostatik tepki tarafı), M-35, M-43 (kayma açısının rejimi).

**Kilit tez:** Kuvvet 2 bağımsız bir kuvvet değildir; **M-35'in uzaysal türevidir.** Gelgit hiçbir yeni parametre gerektirmez.

### Varsayımlar

1. M-35'in alanı geçerlidir: $P(r)=P_0-\alpha M/r$, dolayısıyla $a_r=-\mathcal{G}M/r^2$.
2. Test cismi noktasal değil, yarıçapı $b\ll r$ olan uzanımlı gövdedir.
3. **Akı korunumu:** Kaynaktan uzakta deplasman akısı ne yaratılır ne yok edilir. *(Düzeltme kaydı, 3 Ağustos 2026: bu varsayımın önceki sürümü doğrudan "$\nabla^2P=0$" yazıyordu ve izsizlik girdi olarak kullanılıyordu; aşağıda hem türetiliyor hem bağımsız olarak doğrulanıyor.)*
4. **Ortak taşınmanın çıkarılması:** Kuvvet 1, $\rho_n$ evrensel olduğu için gövdenin her nükleonuna aynı ivmeyi verir; alanın ortak bileşeni gövdeyi bir bütün olarak taşır, deforme etmez.

### Adımlar

**Adım 0 — akı korunumu $\nabla^2P=0$'ı verir.** M-35'in ortam tepkisi $dP/dr=CNq_n/4\pi r^2$ ile, kaynağı çevreleyen herhangi bir küre üzerinden akı yarıçaptan bağımsızdır:
$$\oint_S \nabla P\cdot d\vec A = \frac{CNq_n}{4\pi r^2}\cdot4\pi r^2 = CNq_n=\text{sabit} \;\Longrightarrow\; \int_V\nabla^2P\,dV=0 \;\Longrightarrow\; \nabla^2P=0$$
Fiziksel okuma: kaynaktan çıkan deplasman akısı yolda ne çoğalır ne eksilir. Bu sonuç aşağıda **kullanılmayacak**; tensör ondan bağımsız kurulup iki yolun çakıştığı gösterilecektir.

**Adım 1 — çerçeve.** Gövde merkezi $r$'de, gövde üzerindeki nokta merkezden $\vec\xi$ kadar uzakta olsun. Ortak ivme (Varsayım 4) çıkarıldığında geriye artık kalır:

$$\Delta a_i(\vec\xi) = \frac{\partial a_i}{\partial x_j}\xi_j + O(\xi^2),\qquad T_{ij}\equiv\frac{\partial a_i}{\partial x_j} = -\frac{1}{\rho_n}\partial_i\partial_j P$$

Gelgit tensörü, basınç alanının **ikinci** türevidir. $\mathsf{T}$ simetrik olduğundan eksenin iki ucundaki artık ivmeler zıt yönlüdür — ikisi de merkezden dışa: **çift şişkinlik ek varsayım gerektirmez.**

**(a) Eksenel bileşen:**
$$T_\parallel = \frac{da_r}{dr} = \frac{d}{dr}\left(-\frac{\mathcal{G}M}{r^2}\right) = +\frac{2\mathcal{G}M}{r^3} \;\Longrightarrow\; \Delta a_\parallel = +\frac{2\mathcal{G}M}{r^3}\xi_\parallel$$
Pozitif: uzak uç da yakın uç da merkezden **dışa** kaçar → gelgit ekseni boyunca iki taraflı kabarma ✓

**(b) Yanal bileşen — iz varsayımı kullanılmadan, saf geometriden.** Merkezden $\xi_\perp$ kadar yana kaymış noktada ivme yine kaynağa doğrudur ($r'=\sqrt{r^2+\xi_\perp^2}\simeq r$), fakat doğrultusu merkez hattından $\xi_\perp/r$ kadar sapar:
$$a_\perp = -\frac{\mathcal{G}M}{r'^2}\cdot\frac{\xi_\perp}{r'} \simeq -\frac{\mathcal{G}M}{r^3}\xi_\perp \;\Longrightarrow\; T_\perp = -\frac{\mathcal{G}M}{r^3}$$
Negatif: yanal doğrultularda hareket merkez hattına doğru → **sıkıştırma** ✓ Bu, $1/r^2$ alanının **yakınsama geometrisidir.**

Hesapta $\xi_\perp$'nin hangi yanal doğrultu olduğu hiçbir yere girmedi: eksene dik bütün doğrultular kaynağa aynı uzaklıkta ve aynı açıyla baktığı için $-1$ özdeğeri **iki katlı dejeneredir.** Sıkıştırma tek yönden gelen bir kıstırma değil, gelgit eksenini saran **eşit basınçlı bir kuşaktır** — çembersel sıkıştırma. *(Kuşak gelgit eksenine diktir; gövdenin dönme eksenine veya ekvatoruna değil — bkz. 11.1.3 uyarısı.)*

**(c) İz artık bir sonuçtur:**
$$\mathrm{tr}\,\mathsf{T} = T_\parallel+2T_\perp = \frac{2\mathcal{G}M}{r^3}-\frac{2\mathcal{G}M}{r^3}=0$$
Üç bileşen de bağımsız kuruldu ve iz kendiliğinden sıfır çıktı. $\mathrm{tr}\,\mathsf{T}=-\frac{1}{\rho_n}\nabla^2P$ olduğundan bu, Adım 0'ın akı korunumuyla **birebir aynı ifadedir** — iki bağımsız yol aynı sıfırı verir.

### Sonuç

$$\boxed{\;\left(T_\parallel,\;T_\perp,\;T_\perp\right) = \frac{\mathcal{G}M}{r^3}\,(+2,\,-1,\,-1)\;,\qquad \textstyle\sum\lambda_i = 0\;}$$

### Teori açısından anlamı — iz sıfırlığı bir muhasebe ifadesidir

$(+2,-1,-1)$ yapısı, 3.2.1'deki gelgit anlatısının birebir matematiksel karşılığıdır:

| Özdeğer | Doğrultu | Fiziksel okuma |
|---|---|---|
| $-1$ (×2, **dejenere**) | gelgit eksenine dik **her** yön | **Neden:** Evrenakı, ekseni saran eşit basınçlı bir kuşakla çepeçevre sıkıştırır |
| $+2$ | eksenel | **Sonuç:** sıkışan madde eksen boyunca iki yöne kabarır |

İz sıfırlığı ($\nabla^2P=0$) tam olarak şunu söyler: **Evrenakı yaratılmaz, yok edilmez; yalnızca yer değiştirir.** Yandan sıkıştırılan hacim, eksende kabaran hacimle tam muhasebeleşir. Standart fizikte "gelgit tensörünün izsizliği" soyut bir özellik olarak kaydedilir; burada **korunum yasasının kendisidir**.

Hem $1/r^3$ yasası hem $(+2,-1,-1)$ oranı M-35'in $\nabla^2P=0$ varsayımından türedi — $C$, $q_n$, $\alpha$ dışında hiçbir girdi yok. Kilit tez kanıtlanmıştır.

### Sayısal doğrulama: Güneş/Ay oranı

$$\frac{T_\odot}{T_{Ay}} = \frac{M_\odot}{M_{Ay}}\left(\frac{r_{Ay}}{r_\odot}\right)^3 = \frac{2{,}709\times10^{7}}{(389{,}2)^3} = 0{,}460$$

**%46** ✓ M-26'nın değeriyle birebir. Karşılaştırma için toplam kuvvet oranı $= 179$: Güneş toplam itimde Ay'ın 179 katı, gelgitte yarısından az. $1/r^2$ ile $1/r^3$ arasındaki farkın tüm gücü buradadır.

### Nicel öngörü: denge gelgiti genliği

Gelgit potansiyeli, ortak taşınma çıkarıldıktan sonra kalan ikinci mertebe terimdir ve teorinin kendi sembolüyle yazılır:

$$\Psi_T(\xi,\psi)=-\tfrac12\left(T_\parallel\xi_\parallel^2+T_\perp\xi_\perp^2\right)=-\frac{\mathcal{G}M\,\xi^2}{2r^3}\left(3\cos^2\psi-1\right)$$

*(Notasyon kaydı, 3 Ağustos 2026: önceki sürüm $GM$ yazıyordu — Anayasa R-1/S-20 gereği teorinin kendi denkleminde $\mathcal{G}$ olmalıdır.)*

Artık **basınç** alanı $P_T=\rho_n\Psi_T$'dir ve gövde yüzeyinde ($\xi=b$) gelgit ekseninde $-\rho_n\mathcal{G}Mb^2/r^3$ (açık), kuşakta $+\rho_n\mathcal{G}Mb^2/2r^3$ (fazla) verir — oran tam $2{:}1$. Akışkan $-\nabla P$ yönünde, kuşaktan eksene akar: **sıkıştırma neden, kabarma sonuçtur.**

Serbest yüzey koşulu $g\,\zeta+\Psi_T=$ sabit ile ($g=\mathcal{G}M_\oplus/b^2$), ve sabit **hacim korunumundan** sıfırlanarak ($\langle3\cos^2\psi-1\rangle=0$, Legendre $P_2$):

$$\zeta(\psi)=\frac{1}{2}\frac{M}{M_\oplus}\left(\frac{b}{r}\right)^3 b\left(3\cos^2\psi-1\right) \;\Longrightarrow\; \boxed{\;\Delta\zeta = \frac{3}{2}\,\frac{M}{M_\oplus}\left(\frac{b}{r}\right)^{3} b\;}$$

$\mathcal{G}$ sadeleşir: sonuç **sıfır parametrelidir.** Ve $3/2$ katsayısı etiketi belirler — $\Delta\zeta$ bir *yükseklik değil*, **tepe–çukur tam genliğidir** (tepe $+A$, çukur $-A/2$). *(Notasyon kaydı: eski yazım $\Delta h$ Anayasa S-4'e aykırıydı; $\zeta$ **S-27** olarak kayıtlıdır.)*

| Kaynak | $M/M_\oplus$ | $(b/r)^3$ | tepe $+A$ | çukur $-A/2$ | genlik $\Delta\zeta$ |
|---|---|---|---|---|---|
| Ay | $1{,}229\times10^{-2}$ | $4{,}553\times10^{-6}$ | $+0{,}357$ m | $-0{,}178$ m | **0,535 m** |
| Güneş | $3{,}331\times10^{5}$ | $7{,}724\times10^{-14}$ | $+0{,}164$ m | $-0{,}082$ m | **0,246 m** |

Büyük gelgit (hizalı) $0{,}781$ m · küçük gelgit (dik) $0{,}289$ m · oran $2{,}70$. Açık okyanusta ölçülen denge gelgiti genliği ~0,5 m mertebesindedir ✓ (kıyıdaki metrelerce genlik havza rezonansının yerel büyütmesidir, modele ait değildir). Ay/Güneş oranı burada da 0,46 ✓ — üç ayrı yoldan aynı sayı. *(Dürüstlük kaydı: genlikteki uyum bir **mertebe ve yapı** doğrulamasıdır; hassas olan boyutsuz oranlardır — 0,460 ve 2,70.)*

### Geçerlilik Sınırı

- $b\ll r$ birinci mertebe açılımı; $O(\xi^2)$ ihmal edildi (Ay için $b/r\approx0{,}017$, hata ~%2).
- İz sıfırlığı yalnız **kaynaksız** bölgede geçerlidir; gövde içinde $\nabla^2P\ne0$ ve tensör iz kazanır.
- Denge gelgiti *statik* tepkidir; gerçek gelgit gecikmeli ve dinamiktir (şişkinlik kayması ~3°, kaynağı **atomik sürtünme** — Açık Uçlar'a bkz.).
- Yukarıdaki $(+2,-1,-1)$ yapısı **kilitli kaynak** içindir ($\omega_1$ kapalı). Hızlı dönen kaynakta F4/F5 katkıları tensörün yapısını değiştirir (11.1.8).

### Açık Uçlar

- ~~Şişkinlik kaymasının ($\sim3°$) $\eta_E$ ile bağı~~ → **kapandı (11.1.9):** kaymanın kaynağı **atomik (malzeme) sürtünmesidir**, ortam değil. Üç gerekçe: (i) gevşeme zamanları $\tau_E/\tau_{madde}\approx1{,}8\times10^{16}$ — 12,4 saatlik zorlamaya 16 mertebe yavaş kanal faz kazandıramaz; (ii) M-43'ün altkritik bastırması; (iii) ölçülen ~3,7 TW yitimin ezici çoğunluğu sığ deniz taban sürtünmesindedir. Kayma açısı Ay'ın uzaklaşmasından geri çözülür: $k_2\sin2\varepsilon=0{,}0256$ ⟹ $\varepsilon\approx2^\circ\!-\!3{,}5^\circ$, $Q\approx8\!-\!14$ ✓. Ortamın artık katkısı $\sim2\times10^{-16}$ derecedir — sıfır değil, ölçülemez.
- ~~Gövde içi ($r<b$) rejimde tensör izinin $q_n$ kaynak yoğunluğuyla ilişkisi~~ → **kapandı:** akı gövde içinde kapsanan nükleon sayısıyla büyür, $\nabla^2P=Cq_n\rho_{madde}/m_n$, ve $\mathcal{G}=Cq_n/4\pi\rho_nm_n$ konduğunda
  $$\mathrm{tr}\,\mathsf{T}\big|_{i\varsigma}=-4\pi\mathcal{G}\rho_{madde}$$
  Teori gövde içinde **Poisson denkleminin tam karşılığını** üretir — yeni parametre girmeden, doğru katsayıyla. Öngörü değil, **tutarlılık kapanışı:** dışarıda sıfır, içeride $-4\pi\mathcal{G}\rho$.
- **Yeni:** Kaynak dönüyorsa ($\omega_1$ açık) F4'ün silindirik ve F5'in meridyenel katkıları tensöre girer; yanal dejenerasyon kırılır ve boşlukta iz sıfır olmaktan çıkar. Kilitli kaynak (Ay) ile dönen kaynak (Güneş) arasındaki bu yapı farkı, bölümün ayırt edici sınavıdır (11.1.8). Genlikleri öngörülmemiştir ($\kappa_5$ serbest, $\beta$ apsidal presesyondan $\lesssim10^{-9}$).

---

## M-37 · Vorteks Profil Teoremi, $\tau_{ret}$ ve $\eta_E$ Üst Sınırı · **[T (profil) / A ($\eta_E$)]**

**Kullanıldığı bölümler:** 3.2.2 (Kuvvet 3), 3.1.3-B, 3.4.4, 3.6.1. Bağlı katalog: M-22, M-25, M-27, M-30.

Kuvvet 3'ün iki mertebesi karıştırılmamalıdır:
- **Sıfırıncı mertebe (zarf):** Gövdeyi saran sürüklenme zarfı içinde bağıl hız sıfıra iner ve klasik $F_d\propto\rho v_{bağıl}^2$ sürüklemesi kaybolur — Michelson–Morley null'unun kaynağı budur. Bu bir **taşıma mekanizması değildir:** yörünge hareketini sağlayan şey zarf değil, maddenin basınç gradyanında **serbest düşmesidir** ($v_{madde}=\sqrt{\mathcal{G}M/R}$, M-2). Ortamın kendi dolaşımı bundan ayrıdır ve $\sqrt{\rho_n/\rho_0}=2$ kat hızlıdır (**M-9**: *"madde düşer, ortam dolaşır"*; M-22, M-25); zarf sınırında bir kayma tabakası kalır. *(Düzeltme kaydı, 3 Ağustos 2026: bu satırın önceki sürümü "Cisim ortamla gider ($v_{bağıl}=0$)… yörünge hareketinin kendisini sağlar" diyordu. O yazım M-9'un Geçerlilik Sınırı ile doğrudan çelişiyor ve literal alındığında gezegenleri $2v_{Kepler}$'e koyuyordu; gözlem onu dışlar. Zarfın rolü sürüklemeyi bastırmaktır, yörüngeyi üretmek değil. Birinci mertebe ve bu girdinin bütün sayısal sonuçları etkilenmez.)*
- **Birinci mertebe (artık kuplaj):** Bağıl hız varsa ortam cismi eş-dönüşe **gevşetir**. Asıl "sürüklenme kuvveti" budur.

### Varsayımlar

1. **Postülat 7 (sürüklenme zarfı):** Zarf içinde $v_{bağıl}\approx0$; klasik $F_d\propto\rho v_{bağıl}^2$ sürüklemesi kaybolur (3.4.5).
2. **Ortamın kendi radyal dengesi:** Dönen ortam merkezkaç gereksinimini basınç gradyanıyla karşılar (M-22).
3. **Doğrusal tepki:** Artık kuplaj $\Delta v$ ile doğrusaldır; katsayısı Stokes biçiminde $\eta_E$ ile parametrize edilir (M-27'nin ansatzıyla **aynı** varsayım).

### Adımlar A — Profil teoremi: $v_\theta(R)$ serbest değildir

1. Ortamın radyal dengesi (M-22, kuyu konvansiyonu):
$$\frac{dP}{dR} = \rho\,\frac{v_\theta^2}{R} \quad\Longleftrightarrow\quad \bigl|a_{radyal}(R)\bigr| = \frac{v_\theta^2}{R}$$

2. Sürüklenme zarfı gereği cisim ortamla eş hızlıdır: $v_{yör}=v_\theta$.

3. Birleştirince profil çözülür:

$$\boxed{\;v_\theta(R) = \sqrt{R\,\bigl|a_{radyal}(R)\bigr|}\;}$$

**Ortamın teğetsel profili, radyal itim yasasının sonucudur** — bağımsız bir girdi değildir. Üç rejim tek satırdan çıkar:

| Radyal rejim | $\lvert a_{radyal}\rvert$ | Çıkan profil | Gözlem | Katalog |
|---|---|---|---|---|
| Rankine iç çekirdek | $\propto R$ | $v_\theta \propto R$ (katı-cisim) | yükselen iç kol | M-30 |
| Kepler (küresel akı, M-35) | $\mathcal{G}M/R^2$ | $v_\theta=\sqrt{\mathcal{G}M/R}\propto R^{-1/2}$ | Kepler yörüngeleri | **M-25** ✓ |
| Logaritmik kuyu (silindirik akı, M-38) | $v_0^2/R$ | $v_\theta = v_0$ (sabit) | **düz dönüş eğrisi** | **M-30** ✓ |

Sayısal kontrol: Dünya yörüngesi için $\sqrt{R\lvert a\rvert} = 29{,}79$ km/s, gözlenen $29{,}78$ km/s ✓

**Sonuç:** Kuvvet 3 ile Kuvvet 4 aynı vorteksin teğetsel ve eksenel bileşenleridir; ikisi de tek bir $a_{radyal}(R)$ tarafından yönetilir. Serbest kalan profil fonksiyonu değil, yalnız **geçiş yarıçapı $r_0$**'dır (Ek C P1 buna göre daraltılmalıdır).

> Düz dönüş eğrisi burada karanlık madde varsayımı olmadan, yalnız üç bağımsız gerekçeli öğeden çıkar: *silindirik akı geometrisi + ortamın kendi radyal dengesi + sürüklenme zarfı.*

### Adımlar B — Artık kuplaj ve gevşeme yasası

Küresel cisim için Stokes biçimi:

$$F_{sür} = 6\pi\,\eta_E\,a_b\,\Delta v \;\Longrightarrow\; \frac{d(\Delta v)}{dt} = -\gamma_{sür}\Delta v,\qquad \gamma_{sür} = \frac{6\pi\eta_E a_b}{m}$$

$m=\tfrac43\pi a_b^3\rho_c$ konularak:

$$\boxed{\;\tau_{ret} = \frac{1}{\gamma_{sür}} = \frac{2\,\rho_c\,a_b^{2}}{9\,\eta_E}\;}$$

**Bu, Bölüm 3.6.1'de adı konup formülü verilmeyen $\tau_{ret}$'in kapalı biçimidir.**

$\gamma_{sür}=6\pi\eta_E a_b/m$ ifadesi, M-27'deki halka sönüm terimi $\gamma_{ortam}\sim6\pi\eta_E r_t/m$ ile **birebir aynı formüldür** — aynı $\eta_E$, aynı Stokes kuplajı, biri halka taneciğinde biri gezegen uydusunda. 3.10.4.2'nin çapraz-doğrulama çağrısının karşılığıdır.

**$e$ ve $i$ bağımlılığı — önemli incelik.** Doğrusal rejimde gevşeme oranı $\Delta v$'den bağımsızdır; $\tau_{ret}$ yalnız cismin kendi özelliklerine ($\rho_c$, $a_b$) ve $\eta_E$'ye bağlıdır:

$$\tau_{ret} \ne f(r,e,i)\quad\text{(doğrusal rejimde)}$$

Yörünge geometrisi yalnız **başlangıç** $\Delta v$'sini belirler ($i$ için $\Delta v=2v_{yör}\sin(i/2)$; retrograd $i=180°$ için $2v_{yör}$; basıklık için $\sim e\,v_{yör}$), gevşeme *hızını* değil. Gözlem $e$ veya $i$ bağımlılığı gösterirse kuplaj doğrusal değildir — **yanlışlanabilir ayrım.**

### Sonuç: Güneş Sistemi mimarisi gevşemiş bir durumdur

1. **Eş düzlemlilik:** $i\ne0$ yörüngeler $\tau_{ret}$ ölçeğinde ortam düzlemine oturur → ekliptik.
2. **Prograd tercih:** Retrograd yörüngeler maksimum $\Delta v$ ile en hızlı sönümlenir → kalıcı retrograd cisimler nadir ve yalnız $\tau_{ret}$'i büyük (iri/yoğun) olanlar.
3. **Dairesellik:** $e$ sönümlenir.

Aynı kuplajın dönme karşılığı 3.4.4'ün **kavrama klifi** $g(R)$'sidir: orada ortamın gövde *spinine*, burada *yörüngesine* tutunması ölçülür.

### $\eta_E$ için ilk sayısal üst sınır

$\tau_{ret}$'in kapalı biçimi, Ek C satır 14'ün "değersiz F" kaydını sayıya çevirir. Mantık: *bugün hâlâ retrograd yörüngede duran cisim, $\tau_{ret}$'i Güneş Sistemi yaşından büyük olduğu için oradadır.*

$$\tau_{ret} > t_{GS} \quad\Longrightarrow\quad \boxed{\;\eta_E < \frac{2\,\rho_c\,a_b^{2}}{9\,t_{GS}}\;}$$

$t_{GS}\approx4{,}0$ Gyr $=1{,}26\times10^{17}$ s ile:

| Retrograd cisim | $\rho_c$ (kg/m³) | $a_b$ (m) | Çıkan sınır |
|---|---|---|---|
| Triton (Neptün) | 2061 | $1{,}353\times10^{6}$ | $\eta_E < 6{,}6\times10^{-3}$ Pa·s |
| **Phoebe (Satürn)** | 1638 | $1{,}065\times10^{5}$ | $\boldsymbol{\eta_E < 3{,}3\times10^{-5}}$ **Pa·s** |

Sınır $a_b^2$ ile ölçeklendiğinden **en küçük kalıcı retrograd cisim en güçlü sınırı verir.** Phoebe'nin değeri suyun viskozitesinin (~$10^{-3}$ Pa·s) otuzda biri mertebesindedir; km-altı retrograd ko-orbital cisimler doğrulanırsa sınır $10^{-9}$ Pa·s mertebesine iner.

Statü **[A]**'dır (üst sınır), [S] değil — ama 3.1'in "Parametrik Bir Davet"ine ve 3.10.4.2'nin "Dürüst tespit #2"sine ilk sayısal cevaptır.

### Geçerlilik Sınırı

- **Doğrusal tepki ansatzı merkezî varsayımdır ve bu bloğun en kırılgan halkasıdır.** Klasik akışkanda Stokes düşük Reynolds gerektirir; burada gerekçe farklıdır: sürüklenme zarfı bulk akışı zaten sıfırladığı için geriye *yalnız* artık kuplaj kalır ve onun doğrusal alınması M-27'nin ansatzıyla aynı statüdedir. Ansatz düşerse Adımlar B ve $\eta_E$ sınırı birlikte düşer.

- **Zarfın bastırma yükünün niceliği (28 Temmuz 2026'da eklendi).** Yukarıdaki gerekçe niteliksel bırakılmıştı; sayısı hesaplanınca yükün büyüklüğü görünür olur. Phoebe zarfsız olsaydı, yani $v_{bağıl}\approx3{,}4$ km/s ile $\rho_0=6{,}8\times10^{16}$ kg/m³ içinde klasik eylemsizlik sürüklemesine ($F=\tfrac12C_D\rho_0v^2\pi a_b^2$) maruz kalsaydı:
$$a_{sürükleme}\approx\frac{7{,}0\times10^{33}\ \text{N}}{8{,}29\times10^{18}\ \text{kg}} \approx 8\times10^{14}\ \text{m/s}^2$$
  Oysa Phoebe'nin 4 Gyr boyunca retrograd kalması $a \lesssim v/t \approx 2{,}7\times10^{-14}$ m/s² gerektirir. Yani **sürüklenme zarfı artık kuplajı ~$10^{28}$ çarpanıyla bastırmak zorundadır.** Bu, teoriyi çürüten bir sayı değildir — Postülat 7 zarfı zaten *tam* sürüklenme olarak kurar ve $v_{bağıl}\approx0$ demek tam olarak bu bastırmayı ilan etmektir. Ama iki sonucu vardır ve ikisi de dürüstçe kaydedilmelidir:
  1. $\eta_E$ bir **akışkan viskozitesi gibi okunamaz.** Sayısal değeri $\rho_0$ ile birlikte klasik bir sürükleme yasasına konulursa sonuç 28 mertebe yanlış çıkar. $\eta_E$, zarf sonrası *artık* kuplajın fenomenolojik katsayısıdır; $\rho_0$ ile arasındaki bağ **türetilmemiştir**.
  2. Akış rejimi Stokes değildir ($\mathrm{Re}\approx8\times10^{29}$) ama klasik türbülans da değildir: Mach sayısı $v/c\approx10^{-5}$ ile derin **sıkıştırılamaz** rejimdedir ve ortam bir süper-akışkandır. Süper-akışkanlarda sürükleme, viskozlukla değil **kritik hız / vorteks dökülmesi** eşiğiyle yönetilir — teorinin kendi $v_{kav}$ eşiği (M-4) bunun doğal adresidir.

  > **Bu kalem çözülmüştür: bkz. Ek M-43.** Artık kuplaj $v_{kav}$ çerçevesinde yeniden kuruldu: $F=\tfrac12C_D\rho_0v^2A\,(v/v_{kav})^n$ ile $n\simeq3$. Sistem derin altkritik olduğundan ($v/v_{kav}\approx8\times10^{-10}$) 29 mertebelik bastırma **rejimden** çıkar, ortamın bir özelliğinden değil. Sonuçları: $\eta_E$ boyutlu serbest parametre olmaktan çıkar ve $\eta_E^{etkin}\propto a_b v^4/v_{kav}^3$ olur (evrensel sabit **değildir**); $\rho_0$ ile bağ kurulur; ve $\Sigma/P_0\gtrsim6{,}4\times10^8$ öngörüsü doğar. Aşağıdaki $\tau_{ret}$ öngörülerinin **hız-bağımsızlık** kolu bu çerçevede geçersizdir — M-43'ün ayırt edici tablosuna bakınız.
- Adımlar A'nın 2. adımı ($v_{yör}=v_\theta$) **tam** sürüklenme varsayar; kısmi sürüklenmede profil ile yörünge hızı ayrışır ve teorem yalnız ortam için geçerli kalır.
- $\tau_{ret}$ küresel cisim varsayar; düzensiz cisimlerde $a_b$ etkin yarıçapla değişir.

### Açık Uçlar

- $\tau_{ret}$'in gelgit sönümünden ayrıştırılması: Triton'un gözlenen içe kayması standart gelgit modeliyle açıklanıyor; $\eta_E$ katkısı bu bütçenin **içinde** kalmalıdır — daha sıkı sınır buradan çıkar.
- Yörünge kuplajı ile 3.4.4'ün spin kavraması $g(R)$'nin ortak katsayıya indirgenmesi.
- Doğrusal ↔ doğrusal-olmayan kuplaj ayrımının gözlemsel testi.

---

## M-38 · Eksenel İtim: Silindirik Akı ve $1/R$ Rejimi · **[T (geometri) / A (büyüklük)]**

**Kullanıldığı bölümler:** 3.2.2 (Kuvvet 4), 3.8.6, 4.2.13. Bağlı katalog: M-30, M-37.

### Varsayımlar

1. Ekvator kuşağı, maksimum çizgisel hız nedeniyle Evrenakı'yı düzlem boyunca dışa deplase eder.
2. Deplasman akısı, $h$ kalınlıklı bir **silindir yanağından** geçer (küreden değil).
3. **$h$ yarıçaptan bağımsızdır: $h(R)=$ sabit.** *(28 Temmuz 2026'da açıkça yazıldı — daha önce sessiz varsayımdı.)* Bu koşul zorunludur: akı korunumu akı yoğunluğunu $\propto1/(2\pi Rh)$ verdiğinden, $1/R$ yasası **yalnız $h$ sabitse** çıkar. Yayılan (flaring) bir akı tüpünde $h\propto R$ olsa yasa $1/R^2$'ye döner ve küresel durumdan **hiçbir ayrım kalmaz** — yani bu bloğun galaktik ayağının tamamı bu tek koşula dayanır.
4. Ortam kaynaksızdır; akı korunur.

### Adımlar — geometrik akı argümanı

Kritik ayrım, akının hangi yüzeyden geçtiğidir:

| Kaynak | Akı yüzeyi | Alan | Akı yoğunluğu |
|---|---|---|---|
| **Küresel** (pulsasyon, M-35) | küre | $4\pi r^2$ | $\propto 1/r^2$ |
| **Silindirik** (ekvator deplasmanı) | silindir yanağı | $2\pi R h$ | $\propto 1/R$ |

$$\boxed{\;a_{eksenel}(R)\;\propto\;\frac{1}{R}\qquad (r_{kaynak}\ll R\ll R_{kesim})\;}$$

**Basınç karşılığı — logaritmik kuyu.** $a=-\rho^{-1}dP/dR$ ile $a\propto1/R$ birleşince:

$$\frac{dP}{dR}\propto\frac{\rho}{R} \;\Longrightarrow\; P(R) = P_{ref} + \rho v_0^2\ln\frac{R}{r_0}$$

Bu **M-30**'un galaktik profilidir ve orada düz dönüş eğrisini verir: $a=v_0^2/R$ ile $v^2/R=a$ ⟹ $v=v_0=$ sabit ✓ (M-37'nin profil teoremiyle aynı sonuç.)

> **Türetim zinciri burada tamamlanır — ve düz eğri *varsayılmaz*, çıkar:**
> $$\underbrace{h=\text{sabit}}_{\text{Varsayım 3}}\;\Rightarrow\;\underbrace{a\propto1/R}_{\text{akı geometrisi}}\;\Rightarrow\;\underbrace{v_\theta=\sqrt{R|a|}=\text{sabit}}_{\text{M-37 profil teoremi}}$$
> M-30, aynı sonuca Rankine profilini *girdi alarak* ulaşır; bu zincir ise onu **türetir**. Düz dönüş eğrisinin teoride öngörü statüsü kazanması bu yola bağlıdır (bkz. M-30'un düzeltme kaydı).
>
> **Yayılma (flaring) öngörüsü.** Gerçek galaktik diskler dışa doğru kalınlaşır. $h$ artmaya başladığı yarıçapta $a$, $1/R$'den daha hızlı düşer ve dönüş eğrisi **düzlükten sapıp inmeye başlar.** Bu, varsayımın bedava getirdiği yanlışlanabilir sonuçtur: disk kalınlık profili ($h(R)$, 21 cm gözlemlerinden bilinir) ile dönüş eğrisinin dış kolu **birlikte** fit edilmelidir. Kalınlaşan diskte düz eğrinin sürmesi modeli çürütür.

### Geçerlilik Sınırı — zorunlu düzenleme

$1/R$ yasası her yerde geçerli **değildir** ve bu, teorinin lehinedir:

- **İç sınır ($R\to0$):** Eksende $1/R$ ıraksar; oysa simetri gereği eksende net eksenel kuvvet **sıfırdır**. Rankine iç çekirdeği ($v_\theta=\omega R$, $a\propto R$) ıraksamayı düzenler.
- **Dış sınır ($R\gg$ kaynak diskinin yarıçapı):** Akı düzleme hapsedilemez, küresel yayılıma döner, yasa yeniden $1/R^2$'ye evrilir.
- **Sonuç:** $1/R$ bir **ara pencere**dir; sınırlarını $r_0$ ve kesim yarıçapı belirler. 4.2.13'ün rejim tablosu tam budur.

### Dünya–Ay sistemi: $1/R$ payının gözlemsel üst sınırı

Yakın bir sistemde $1/R$ teriminin ne kadar zayıf kalmak zorunda olduğu, Ay'ın yörünge dinamiğinden doğrudan okunur. Karışık kuvvet yasası ve karışım oranı:

$$a(r) = \underbrace{\frac{A}{r^2}}_{\text{M-35}} + \underbrace{\frac{B}{r}}_{\text{M-38}},\qquad \varepsilon \equiv \left.\frac{B/r}{A/r^2}\right|_{r=r_{Ay}}$$

İki yöntem sınır verir; ikincisi beş kat sıkıdır.

**(a) İvme muhasebesi.** Ay'ın gerektirdiği bağıl ivme $v^2/r = 2{,}717\times10^{-3}$ m/s²'dir. Bu yolla anlamlı bir sınır kurmak için hesaba **girmesi zorunlu** terimler ve her birinin mertebesi:

| Hesaba girmesi zorunlu terim | Mertebe (m/s²) |
|---|---|
| Ay'ın kendi kütlesi — iki-cisim: $G(M_\oplus{+}M_{Ay})/r^2$ | $3{,}32\times10^{-5}$ |
| Kutup ivmesinin $J_2$ düzeltmesi: $g_{kutup}=9{,}832$ yerine $GM/R_p^2=9{,}8642$ | $0{,}88\times10^{-5}$ |
| Yarı-büyük eksen ($384.748$ km) ile ortalama uzaklık ($384.400$ km) ayrımı | $1{,}35\times10^{-5}$ |

Üçü de $10^{-5}$ mertebesindedir — yani **herhangi birinin atlanması, toplam ivmenin ~%1'i büyüklüğünde sahte bir artık üretir.** Üçü birlikte hesaba katıldığında standart iki-cisim bağıntısı $n^2a^3 = G(M{+}m)$ %0,01 hassasiyetle kapanır. Bu, yöntemin duyarlılık tabanıdır:

$$\varepsilon_{Ay} \;<\; 1\times10^{-4} \qquad \text{(ivme muhasebesi)}$$

**(b) Apsidal presesyon — asıl kısıt.** Karışık yasanın etkin üssü ve apsis açısı:

$$n_{ef} = \frac{2+\varepsilon}{1+\varepsilon},\qquad \Phi = \frac{\pi}{\sqrt{3-n_{ef}}},\qquad \Delta\varpi_{\text{yörünge}} = 2\Phi-2\pi \simeq -\pi\varepsilon$$

Ay'ın apsidal presesyonu $+40{,}7°$/yıl'dır (8,85 yıllık çevrim, 3.9.6) ve Güneş pertürbasyonuyla yüksek hassasiyetle modellenir. Muhafazakâr %0,1 modelleme hassasiyeti alındığında yörünge başına artık $\lvert\Delta\varpi\rvert < 5{,}3\times10^{-5}$ rad olur ve $\lvert\Delta\varpi\rvert=\pi\varepsilon$ ilişkisinden:

$$\boxed{\;\varepsilon_{Ay} = \left.\frac{a_{1/R}}{a_{1/R^2}}\right|_{r=384.400\text{ km}} \;<\; 2\times10^{-5}\;}$$

Duyarlılık ölçeği için: $\varepsilon = 10^{-2}$ mertebesinde bir pay, yörünge başına $-1{,}9°$ (yılda $-25°$) ek presesyon üretirdi — gözlenen değerin %62'si. Yöntem bu yüzden çok keskindir; Ay verisi, yakın sistemlerde $1/R$ payını **yüz binde iki**nin altına hapseder.

**Ek kısıt — etki-tepki.** Kilitlenmiş bir uydunun gövdeye uyguladığı kuvvet neredeyse saf M-35 iken gövdenin uyguladığı M-35+M-38 ise, asimetri doğar. Ortam momentum taşıdığı için katı 3. yasa zorunlu değildir; ancak dengesizlik barisentre seküler ivme verir ve barisentrin Güneş yörüngesi bunu aynı mertebede sınırlar.

### Ölçek ataması: $1/R$ galaktik vortekse aittir

Yukarıdaki sınır, karanlık madde argümanını zayıflatmaz; ona ölçeğini verir:

- $1/R$ rejimi her gezegenin kendi ekvatoruna değil, **galaktik ölçekli kolektif vortekse** aittir.
- Geçiş yarıçapı $r_0$ (kpc mertebesi) Güneş Sistemi'ni Kepler rejiminde tutar (4.2.13).
- Yerel galaktik alan ($v_0\approx220$ km/s, $R\approx8$ kpc → $a=v_0^2/R\approx2{,}0\times10^{-10}$ m/s²) tüm Güneş Sistemi'ne **ortak-mod** etki eder; Dünya–Ay *bağıl* dinamiğinde görünmez. Çelişki bu yüzden doğmaz.

### Açık Uçlar

- $r_0$'ın gövde/disk parametrelerinden (dönüş hızı, kalınlık $h$) türetimi — bu bloğun kalan tek yapısal boşluğu.
- Silindirik akı katsayısının ($h$) nükleon deplasman debisi $q_n$ ile bağı — M-35 ve M-38'i ortak kaynağa indirger.
- Bağımsız M-numarası hakkı: bu girdi şu an M-30'un yeniden okumasıdır; $r_0$ türetimi eklenince tam bağımsız statü kazanır.

---

## M-39 · Yanal İtim: $\sin 2\theta$ Yasası · **[T (yapı) / F ($\kappa_5$)]**

**Kullanıldığı bölümler:** 3.2.2 (Kuvvet 5), 3.5.1, 3.10. Bağlı katalog: M-27, M-37.

### Geometri ve kuvvet yönleri

<div style="text-align:center; margin:22px 0;">
<svg width="100%" viewBox="0 0 760 440" xmlns="http://www.w3.org/2000/svg" font-family="system-ui, -apple-system, Segoe UI, sans-serif">
  <defs>
    <marker id="hF1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#ff7b72"/></marker>
    <marker id="hF4" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#ffa657"/></marker>
    <marker id="hF5" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#7ee787"/></marker>
    <marker id="hDimP" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#d2a8ff"/></marker>
    <marker id="hDimB" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#a5d6ff"/></marker>
    <marker id="hSpin" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#58a6ff"/></marker>
  </defs>

  <rect x="0" y="0" width="760" height="440" rx="12" fill="#0d1117"/>

  <line x1="340" y1="48" x2="340" y2="350" stroke="#484f58" stroke-width="1.5" stroke-dasharray="6,6"/>
  <text x="328" y="60" fill="#8b949e" font-size="13" text-anchor="end">z — dönme ekseni (ω₁)</text>

  <line x1="95" y1="260" x2="700" y2="260" stroke="#484f58" stroke-width="1.5" stroke-dasharray="6,6"/>
  <text x="612" y="281" fill="#8b949e" font-size="13">Ekvator düzlemi</text>

  <circle cx="340" cy="260" r="72" fill="#1f6feb" fill-opacity="0.20" stroke="#58a6ff" stroke-width="2"/>
  <ellipse cx="340" cy="260" rx="72" ry="17" fill="none" stroke="#58a6ff" stroke-width="1.2" stroke-dasharray="3,3" opacity="0.65"/>
  <path d="M 280 269 Q 340 282 400 269" fill="none" stroke="#58a6ff" stroke-width="2" opacity="0.85" marker-end="url(#hSpin)"/>
  <circle cx="340" cy="260" r="3.5" fill="#ffffff"/>
  <text x="349" y="288" fill="#c9d1d9" font-size="15" font-style="italic">M</text>

  <line x1="340" y1="260" x2="520" y2="109" stroke="#58a6ff" stroke-width="2"/>
  <text x="440" y="199" fill="#58a6ff" font-size="16" font-style="italic">r</text>

  <path d="M 396 260 A 56 56 0 0 0 383 224" fill="none" stroke="#c9d1d9" stroke-width="1.5"/>
  <text x="400" y="241" fill="#c9d1d9" font-size="15" font-style="italic">θ</text>

  <circle cx="340" cy="109" r="3" fill="#6e7681"/>
  <circle cx="520" cy="260" r="3" fill="#6e7681"/>

  <line x1="340" y1="105" x2="340" y2="66" stroke="#6e7681" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="520" y1="105" x2="520" y2="66" stroke="#6e7681" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="340" y1="74" x2="520" y2="74" stroke="#d2a8ff" stroke-width="1.5" marker-start="url(#hDimP)" marker-end="url(#hDimP)"/>
  <text x="430" y="64" fill="#d2a8ff" font-size="14" text-anchor="middle">R = r·cos θ</text>

  <line x1="524" y1="260" x2="612" y2="260" stroke="#6e7681" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="524" y1="109" x2="612" y2="109" stroke="#6e7681" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="598" y1="109" x2="598" y2="260" stroke="#a5d6ff" stroke-width="1.5" marker-start="url(#hDimB)" marker-end="url(#hDimB)"/>
  <text x="610" y="190" fill="#a5d6ff" font-size="14">z = r·sin θ</text>

  <circle cx="520" cy="109" r="5.5" fill="#f0f6fc"/>
  <text x="529" y="99" fill="#f0f6fc" font-size="15" font-weight="600">P</text>

  <line x1="520" y1="109" x2="465" y2="155" stroke="#ff7b72" stroke-width="3.5" marker-end="url(#hF1)"/>
  <text x="462" y="139" fill="#ff7b72" font-size="15" font-weight="600" text-anchor="end">F₁</text>

  <line x1="520" y1="109" x2="448" y2="109" stroke="#ffa657" stroke-width="3.5" marker-end="url(#hF4)"/>
  <text x="452" y="99" fill="#ffa657" font-size="15" font-weight="600" text-anchor="middle">F₄</text>

  <line x1="520" y1="109" x2="566" y2="164" stroke="#7ee787" stroke-width="3.5" marker-end="url(#hF5)"/>
  <text x="572" y="178" fill="#7ee787" font-size="15" font-weight="600">F₅</text>

  <line x1="100" y1="368" x2="130" y2="368" stroke="#ff7b72" stroke-width="3.5"/>
  <text x="140" y="373" fill="#c9d1d9" font-size="13">F₁ — Radyal kütle-itimi (ω₂): merkeze doğru, ∝ 1/r²   [M-35]</text>
  <line x1="100" y1="392" x2="130" y2="392" stroke="#ffa657" stroke-width="3.5"/>
  <text x="140" y="397" fill="#c9d1d9" font-size="13">F₄ — Eksenel itim (ω₁): dönme eksenine doğru, ∝ 1/R   [M-38]</text>
  <line x1="100" y1="416" x2="130" y2="416" stroke="#7ee787" stroke-width="3.5"/>
  <text x="140" y="421" fill="#c9d1d9" font-size="13">F₅ — Yanal itim (ω₁): ekvator düzlemine doğru, ∝ sin 2θ   [M-39]</text>
</svg>
</div>

*Şekil M-39.1: P noktasındaki üç kuvvetin yönleri ve epür ölçülendirmesi. $\theta$ ekvatordan ölçülen enlem açısıdır; $R=r\cos\theta$, $z=r\sin\theta$. F₁ radyal ($-\hat r$), F₄ eksene dik ($-\hat R$), F₅ teğetsel ($-\hat\theta$) yönlüdür; F₁ ile F₅ karşılıklı diktir.*

### Varsayımlar

1. **Geometri:** $R=r\cos\theta$, $z=r\sin\theta$.
2. **Hız profili:** Sürüklenen ortamın hızı $v(\theta)=v_e\cos\theta$; kutupta sıfır, ekvatorda maksimum. $v_e$ ortamın yüzeydeki ekvatoral hızıdır. **Profilin biçimi eş-dönüşü şart koşar:** $v=\Omega_{ortam}\,r\cos\theta$ ancak ortam gövdeyle aynı *açısal* hızda taşınıyorsa geçerlidir, yani $v_e=\Omega_{ortam}R$.
   > *Düzeltme kaydı (28 Temmuz 2026): bu varsayımın önceki sürümü "3.2.2 gereği ortam gövdeden çok daha hızlı döner" diyordu. İfade kaldırıldı — kitapta dayanağı bulunamadı, kullanılan $\cos\theta$ profiliyle (ki eş-dönüşü şart koşar) ve M-40'ın $\xi$'siyle çelişiyordu.*

4. **Kavrama kesri deplasman kesridir ($\mathcal{R}=\phi$).** Ortam gövdeyle *tam* dönmez; kafesin deplase ettiği kesir kadar taşınır. Bu kesir teoride zaten türetilmiştir — **M-16**'nın Fizeau muhasebesi tam olarak bunu söyler: deplase edilen $\phi$ kesri maddeyle birlikte taşınır, arka plan $(1-\phi)$ taşınmaz. Dolayısıyla
$$v_e = \phi\,\omega R\,,\qquad \phi = 1-\frac{1}{n^2}$$
   $\phi$ yeni bir parametre **değildir**; kırılma indisinden okunur ve akan sudaki ışık sürüklenmesiyle ($f=0{,}434\pm0{,}020$) ölçülmüş büyüklüğün aynısıdır.

   > **Deplasman kafesi nükleon değil, atomdur.** Su için $\phi=0{,}437$ iken $\rho_{su}/\rho_n=3{,}7\times10^{-15}$'tir — 14 mertebe fark. Atomun elektron kabuğu *kütlesel* olarak boştur ama Evrenakı açısından **doludur**: bağlı yapı orayı da deplase eder. Kavramanın kütleyle değil **yer** (hacim) ile ölçeklendiğini Fizeau deneyi doğrudan ölçmüştür — kütle ölçeklemesi olsaydı akan su ışığı hiç sürüklemezdi.
   >
   > Bunun üç sonucu vardır ve üçü de gözlemle uyumludur:
   > - **Bağlı ↔ iyonize uçurumu belirleyicidir.** Atom çözülünce bağlı kafes kalmaz ve $\phi$ çöker: gaz devleri yoğun *maddedir* (moleküler/metalik hidrojen, $\phi\sim0{,}6$), Güneş ise tam iyonize plazmadır ($\phi\to\rho/\rho_n\sim10^{-15}$). **Yanal itim gaz devlerinde güçlü, Güneş'te yoktur.**
   > - **Atom ↔ nötron farkı ılımlıdır.** Nötron maddesinde iç boşluk yoktur ve cepler sıkı paketlenir, $\phi\approx0{,}7$–$0{,}9$; ama nötronun kendi iç yapısı olduğu için $\phi<1$ kalır. Doygunluk **asimptotiktir**, tam değil.
   > - **Karadelikte doygunluk 1'e yaklaşır, 1'e eşit olmaz.**
3. **Deplasman kapanışı:** Hızlı akan kuşağın bıraktığı basınç açığı kinetik ölçeklemeyle alınır:
$$\Delta P(\theta) = -\,\kappa_5\,\rho\,v(\theta)^2$$
$\kappa_5=\tfrac12$ seçimi Bernoulli biçimini verir.

> **Neden Bernoulli değil, deplasman?** Akım çizgileri *arası* Bernoulli yalnız dönüsüz (irrotasyonel) akışta geçerlidir. Yüzeye yakın bölge sürüklenme zarfı nedeniyle katı-cisim benzeri (rotasyonel) davranırsa denge $P=P_c+\tfrac12\rho\Omega^2R^2$ olur — **ekvatorda basınç yüksek** çıkar ve kuvvetin işareti ters döner (basık değil, uzun gövde). Gözlem (basıklık, halkalar, diskler) ters işareti dışladığı için gerekçe, rejime bağımlı Bernoulli yerine **teorinin kendi deplasman muhasebesine** dayandırılır. Cebirsel biçim aynı kalır; değişen gerekçe ve katsayının statüsüdür.

### Adımlar

Enleme bağlı yüzey basıncı:
$$P(\theta) = P_{kutup} - \kappa_5\,\rho\,v_e^2\cos^2\theta$$

Küresel yüzeyde açısal gradyan $\nabla_\theta P=\frac1r\frac{dP}{d\theta}$; türev:
$$\frac{d}{d\theta}(\cos^2\theta) = -2\cos\theta\sin\theta = -\sin2\theta \;\Longrightarrow\; \frac{dP}{d\theta} = \kappa_5\rho v_e^2\sin2\theta$$

Birim hacme düşen kuvvet $f=-\nabla P$ olduğundan:

### Sonuç

$$\boxed{\;f_{yanal}(\theta) = -\frac{\kappa_5\,\rho\,v_e^{2}}{r}\,\sin 2\theta\qquad [\mathrm{N/m^3}]\;}$$

$\kappa_5=\tfrac12$ için $f_{yanal}=-\dfrac{\rho v_e^2}{2r}\sin2\theta$.

**Boyut denetimi:** $\rho v_e^2/r = \mathrm{Pa/m} = \mathrm{N/m^3}$ ✓ — kuvvet değil **kuvvet yoğunluğu**; bu nedenle $f$ (küçük harf) kullanılır.

**İşaret okuması:** Eksi işaret $-\hat\theta$, yani **ekvatora doğru**yu gösterir ✓

### Merkezkaça Oranı Cisimden Bağımsızdır

$v_e=\phi\,\omega R$ konup ivmeye geçilince ($a=-\rho_n^{-1}\nabla P$, M-2) $\omega$ ve $R$ **sadeleşir**:

$$\frac{a_{yanal}}{a_{merkezkaç}} = \kappa_5\left(\frac{\rho_0}{\rho_n}\right)\phi^{2}\cdot 2\sin\theta$$

Bu, bloğun en kısıtlayıcı yapısal sonucudur: yanal itim her cisim için merkezkaçın **aynı kesridir**, yalnız $\phi$ ile ölçeklenir. İki okuması var ve ikisi de gereklidir:

- **Mutlak büyüklük cisimden cisme çok değişir.** Jüpiter'in yüzey hızı Dünya'nın 27 katı ($12.570$ ↔ $465$ m/s), dolayısıyla $a_{yanal}$ 730 kat büyüktür. Gaz devlerinin basıklığının ($f_J=0{,}065$, $f_S=0{,}098$ ↔ $f_\oplus=0{,}0034$) çok büyük olması bu tarafla tutarlıdır.
- **Oransal büyüklük sabittir.** Bu yüzden yanal itim, basıklık–dönüş ilişkisini *bozmaz*; yalnız $(1+\kappa_5(\rho_0/\rho_n)\phi^2)$ çarpanıyla yeniden ölçekler. Hidrostatik uyum bu çarpanı içine emer.

### İmza $J_2$'de Değil, $J_4$'tedir

Yukarıdaki sonuç, uzun süre kayıtlı olan "$J_2$ katalogundan tek $\kappa_5$" sınavının **yanlış harmoniğe baktığını** gösterir. İki kuvvetin enlem profilleri farklıdır:

| Kuvvet | Enlem profili | Yön |
|---|---|---|
| Merkezkaç | $\propto\cos\theta$ — ekvatorda maksimum, kutupta sıfır | eksene dik |
| **Yanal itim** | $\propto\sin2\theta$ — **45°'de maksimum; ekvatorda VE kutupta sıfır** | ekvator düzlemine |

Merkezkaç bu deseni taklit edemez. Dolayısıyla yanal itim $J_2$'yi yeniden ölçekler (içine emilir, görünmez) ama **$J_4$ ve $J_6$'ya kendi imzasını bırakır.** Gereken veri yüksek hassasiyette mevcuttur:

| Cisim | $J_4$ (ölçülen) | Kaynak |
|---|---|---|
| Dünya | $-1{,}62\times10^{-6}$ | uydu jeodezisi |
| Jüpiter | $-5{,}87\times10^{-4}$ | **Juno** |
| Satürn | $-9{,}35\times10^{-4}$ | **Cassini Grand Finale** |

**$\kappa_5$ üzerindeki ilk sayısal sınır.** Dünya'nın ölçülen basıklığı standart hidrostatik öngörüyle ~%0,5 içinde uyuşur (kalan fark manto konveksiyonu ve buzul geri sıçramasına atfedilir). $\phi_\oplus\approx0{,}6$ ve $\rho_0/\rho_n=\tfrac18$ ($k=\tfrac12$ öngörüsü, M-44) ile 45°'de oran $0{,}088\,\kappa_5$ çıkar; %0,5 tolerans:

$$\boxed{\;\kappa_5 \lesssim 0{,}1\;}$$

Yani $\kappa_5=\tfrac12$ çalışma değeri **beş kat fazladır** ve düşürülmelidir. Bu, $\kappa_5$'in ilk gözlemsel kısıtıdır.

### Enlem profili ve kararlılık

<div style="text-align:center; margin:22px 0;">
<svg width="100%" viewBox="0 0 640 285" xmlns="http://www.w3.org/2000/svg" font-family="system-ui, -apple-system, Segoe UI, sans-serif">
  <rect x="0" y="0" width="640" height="285" rx="12" fill="#0d1117"/>
  <text x="320" y="30" fill="#c9d1d9" font-size="14" text-anchor="middle">Yanal itim şiddetinin enlem profili:  |f| ∝ sin 2θ</text>
  <line x1="80" y1="215" x2="580" y2="215" stroke="#8b949e" stroke-width="1.5"/>
  <line x1="80" y1="215" x2="80" y2="48" stroke="#8b949e" stroke-width="1.5"/>
  <line x1="74" y1="60" x2="86" y2="60" stroke="#8b949e" stroke-width="1.2"/>
  <text x="68" y="65" fill="#8b949e" font-size="11" text-anchor="end">1</text>
  <text x="68" y="219" fill="#8b949e" font-size="11" text-anchor="end">0</text>
  <line x1="320" y1="215" x2="320" y2="60" stroke="#7ee787" stroke-width="1.2" stroke-dasharray="4,4" opacity="0.55"/>
  <polyline fill="none" stroke="#7ee787" stroke-width="3"
    points="80,215 120,175 160,138 200,105 240,81 280,65 320,60 360,65 400,81 440,105 480,138 520,175 560,215"/>
  <circle cx="320" cy="60" r="5" fill="#7ee787"/>
  <circle cx="80" cy="215" r="5" fill="#ff7b72"/>
  <circle cx="560" cy="215" r="5" fill="#ff7b72"/>
  <text x="332" y="52" fill="#7ee787" font-size="12">maksimum ezme: θ = 45°</text>
  <text x="96" y="196" fill="#ff7b72" font-size="11">kararlı denge</text>
  <text x="546" y="196" fill="#ff7b72" font-size="11" text-anchor="end">kararsız denge</text>
  <line x1="80" y1="215" x2="80" y2="221" stroke="#8b949e"/>
  <line x1="240" y1="215" x2="240" y2="221" stroke="#8b949e"/>
  <line x1="320" y1="215" x2="320" y2="221" stroke="#8b949e"/>
  <line x1="400" y1="215" x2="400" y2="221" stroke="#8b949e"/>
  <line x1="560" y1="215" x2="560" y2="221" stroke="#8b949e"/>
  <text x="80" y="236" fill="#8b949e" font-size="11" text-anchor="middle">0°</text>
  <text x="240" y="236" fill="#8b949e" font-size="11" text-anchor="middle">30°</text>
  <text x="320" y="236" fill="#8b949e" font-size="11" text-anchor="middle">45°</text>
  <text x="400" y="236" fill="#8b949e" font-size="11" text-anchor="middle">60°</text>
  <text x="560" y="236" fill="#8b949e" font-size="11" text-anchor="middle">90°</text>
  <text x="80" y="258" fill="#8b949e" font-size="12" text-anchor="start">ekvator</text>
  <text x="560" y="258" fill="#8b949e" font-size="12" text-anchor="end">kutup</text>
  <text x="320" y="276" fill="#6e7681" font-size="11" text-anchor="middle">θ — ekvatordan ölçülen enlem</text>
</svg>
</div>

*Şekil M-39.2: Kuvvet hem ekvatorda hem kutupta sıfırlanır; şiddeti 45° orta enlemlerde maksimumdur.*

**Kararlılık analizi:**

- $\theta>0$ için $\sin2\theta>0 \Rightarrow f<0$: kuvvet $-\hat\theta$ = **ekvatora doğru**
- $\theta<0$ için $\sin2\theta<0 \Rightarrow f>0$: kuvvet $+\hat\theta$ = yine **ekvatora doğru**

⟹ **Ekvator kararlı, kutup kararsız dengedir.** Kutupta kuvvet sıfırdır ama en küçük sapma maddeyi ekvatora savurur; madde kutupta birikemez.

Satürn halkalarının, gezegen halka sistemlerinin ve galaktik disklerin neden ekvator düzleminde jilet inceliğinde toplandığının mekanik cevabı budur: **ekvator, yanal itim alanının tek kararlı çekim noktasıdır.**

### Geçerlilik Sınırı

- Türetim **sabit $r$** üzerinde teğetsel bileşeni verir; formüldeki $1/r$ metrik çarpandır, uzak-alan sönümü değildir. Radyal yapı M-37'nin profil teoreminden gelir: Kepler rejiminde $v_e^2=GM/r$ konularak $f_{yanal}\propto\rho\,GM\sin2\theta/r^2$.
- $v(\theta)=v_e\cos\theta$ profili, ortamın gövdeyle aynı **açısal** hızda (genliği $\phi$ kesriyle) sürüklendiği yüzey kuşağı için geçerlidir; serbest-vorteks bölgesinde ($v\propto1/R$) profil değişir.
- $\kappa_5$ serbesttir; işaret ve enlem yapısı $\kappa_5$'ten bağımsızdır, yalnız genlik ona bağlıdır. Yeni üst sınır: $\kappa_5\lesssim0{,}1$.
- **$\phi$'nin opak ve metalik fazlarda okunması doğrudan değildir (dürüst kayıt).** $\phi=1-1/n^2$ bağıntısı saydam ortamlar için türetildi (M-15). Dünya için kullandığım $\phi\approx0{,}6$ mantoya dayanır (silikat, $n\approx1{,}6$; hacimce ~%84); demir çekirdek ve Jüpiter'in metalik hidrojeni için $n$ karmaşıktır ve $\phi$ ayrı bir argüman gerektirir. Sayısal sonuçlar bu belirsizliği taşır.
- **İyonizasyon geçişi türetilmemiştir.** Güneş için verilen $\phi\to\rho/\rho_n\sim10^{-15}$ bir mertebe tahminidir; bağlı kafesin iyonizasyon derecesiyle *sürekli* mi yoksa *eşikli* mi çözüldüğü modellenmemiştir.
- **İç kavrama ile dış sürüklenme ayrı büyüklüklerdir.** Buradaki $\phi$ kafesin *içindeki* ortamı yönetir; gövdenin *dışındaki* dipolar alanı M-40'ın $\xi$'si yönetir ve ikisinin sınırda eşleşmesi gerekmez — sınır tam olarak kafesin bittiği yerdir (M-40, "İki kavrama kanalı").

### Açık Uçlar

1. **$\kappa_5$'in $J_4$'ten kalibrasyonu (öncelikli iş).** Sınav $J_2$ değil $J_4$ üzerinden kurulmalıdır: her cisim için $\Delta_4\equiv(J_4^{gözlenen}-J_4^{hidrostatik})/J_4^{hidrostatik}$ hesaplanır ve
$$\Delta_4 \;\propto\; \kappa_5\left(\frac{\rho_0}{\rho_n}\right)\phi^2$$
   ile karşılaştırılır. $\phi$ her cisim için bağımsızca (kırılma indisi / kompozisyon) bilindiğinden **dört cisim tek $\kappa_5$ vermek zorundadır**: Dünya, Jüpiter, Satürn, Güneş. Uyuşmazsa model yanlışlanır. Güneş özel önemdedir: $\phi\approx0$ olduğundan $\Delta_4^{Güneş}\approx0$ öngörülür — kompozisyon ekseninin doğrudan sınavı. *(Önceki sürüm bu sınavı $J_2$ üzerinden kuruyordu; $J_2$ katkısı yeniden-ölçekleme olarak emildiği için sınav ayırt edici değildi.)*
2. **45° imzası:** Kuvvetin orta enlemlerde maksimum olması, atmosferik/manto ölçeğinde 45° dolaylarında ayırt edici gerilme veya akış deseni öngörür — $\sin2\theta$'nın doğrudan sınanabilir tek imzası.
3. **Halka kalınlığı:** Ekvatordaki kararlı denge çevresinde küçük salınım frekansı, $f_{yanal}$'ın $\theta$ türevinden çıkar ve M-27'nin dikey salınımıyla karşılaştırılabilir — iki bağımsız yoldan aynı kalınlık çıkmalıdır.

---

## M-40 · Dönme Sürüklenme Kesri ve Çerçeve Sürüklenmesi (GP-B) · **[T]**

**Kullanıldığı bölümler:** Postülat 7 (1.3), 6.3.3, 3.10.6, 4.2.16, Ek C satır 19. Bağlı katalog: M-8 ($\Phi/c^2$ girdisi), M-37 (aynı entrainment kuplajı), M-39.

Bu girdi, M-37'nin sürüklenme kavramını **dönme** eksenine taşır ve teorinin öteleme/dönme ayrımını nicelleştirir.

### Varsayımlar

1. **Öteleme sürüklenmesi tamdır** (Postülat 7): $\vec v_{bağıl}\approx0$ — Michelson–Morley'in sıfır sonucu bunu ölçer.
2. **Dönme sürüklenmesi patinajlıdır:** Rijit kafes yavaş döner, atomik boşluklardan sızan akışkan kafese tutunmaz (3.2.2). Kuplaj bir kesirle yazılır: $\vec\Omega_{ortam}=\xi\,\vec\omega_{gövde}$, $\xi\ll1$. **Bu, patinaj ilkesinin dönme eksenine uygulanmasıdır — ek varsayım değil, teorinin öngörüsü.**
3. **Akış çözümünün biçimi — simetriden, viskozlukten değil.** Alanın $r^{-3}$ dipolar biçimi, dönen kaynağın **simetrisinden** çıkar: $\vec\omega$'da doğrusal, diverjanssız, sonsuzda sönen ve eksenel simetrik bir hız alanının baş terimi tek bir biçimdir,
$$\vec v \propto \frac{\vec\omega\times\vec r}{r^3}\,,\qquad \nabla\cdot\!\left(\frac{\vec\omega\times\vec r}{r^3}\right)=0$$
   (manyetik dipolün $r^{-3}$'ünü veren argümanın birebir aynısı). Biçim bu yüzden **düşük-Reynolds koşulu gerektirmez**.
   > *Düzeltme kaydı (28 Temmuz 2026):* Bu varsayımın önceki sürümü "viskoz ortamda dönen küre için **Stokes rotleti** geçerlidir" diyordu. Denetimde bu gerekçe **geçersiz** bulundu: Stokes rejimi $\mathrm{Re}\ll1$ ister, oysa buradaki değerlerle $\mathrm{Re}=\rho_0 vL/\eta_E \approx 3\times10^{21}$'dir (21 mertebe ihlal). Alanın biçimi Stokes'a **borçlu değildir** — yukarıdaki simetri argümanı onu bağımsız olarak verir ve genliği zaten $\xi$ ile gözlemden sabitlenir. Türetimin sonucu değişmez; yalnız yanlış dayanak kaldırılmıştır.
4. **Jiroskop kinematiği:** Bir jiroskop, taşındığı akışkanın vortisitesiyle değil **rotasyon hızıyla** devinir: $\vec\Omega_{rot}=\tfrac12\nabla\times\vec v$ (hız gradyan tensörünün antisimetrik kısmı).
   > **İki kuplajın karıştırılmaması (zorunlu ayrım).** Bu türetimde iki farklı bağ vardır ve **aynı türden değildir**; aksi hâlde "$\xi\approx5\times10^{-10}$ ile neredeyse hiç kuplaj yok" ile "jiroskop ortamı tam izliyor" aynı cümlede çelişik görünür:
   > - **Gövde → ortam: dinamik ve patinajlı.** Dünya'nın dönüşünün ortama aktarılması bir *momentum aktarımıdır* ve kesirle olur ($\xi$, Varsayım 2).
   > - **Ortam → jiroskop: kinematik ve tam.** Serbest bir jiroskop, ortama tork uyguladığı için değil, **ortam yerel eylemsizlik çerçevesini tanımladığı** için onun rotasyonunu izler (Postülat 7'nin çerçeve yorumu). Burada bir kuplaj katsayısı yoktur; olsaydı sonuç $\xi^2$ mertebesine düşer ve gözlemin $10^{10}$ katı altına inerdi.
   >
   > Bu ayrım teoriye eklenen bir varsayım değil, öteleme kolunda zaten kullanılan yapının dönme koluna taşınmasıdır: Michelson–Morley'de de ortam *tam* taşır (kinematik), ama gövde ortamı sürüklemez.

### Adımlar

1. **Akış alanı** (Stokes rotleti, kısmi sürüklenmeyle):
$$\vec v = \xi\,\frac{R^3}{r^3}\left(\vec\omega_{gövde}\times\vec r\right)$$

2. **Curl'ü dipolardır** — manyetik dipol yapısının birebir aynısı:
$$\nabla\times\vec v = \xi R^3\,\frac{3(\vec\omega_{gövde}\cdot\hat r)\hat r - \vec\omega_{gövde}}{r^3}$$

3. **Yerel rotasyon hızı** (Varsayım 4):
$$\vec\Omega_{rot} = \tfrac12\nabla\times\vec v = \frac{\xi R^3}{2r^3}\left[3(\vec\omega_{gövde}\cdot\hat r)\hat r - \vec\omega_{gövde}\right]$$

Bu, Lense–Thirring'in açısal biçimiyle **yapısal olarak özdeştir**; $\xi R^3/2 \leftrightarrow GI/c^2$ eşlemesiyle GR'ın $\vec\Omega_{LT}=\frac{G}{c^2r^3}[3(\vec J\cdot\hat r)\hat r-\vec J]$ ifadesine geçer.

4. **Kutupsal yörünge ortalaması — kesin geometrik çarpan.** Ölçülen büyüklük yerel hız değil, yörünge boyunca ortalanmış presesyondur. $\hat r=\cos\theta\,\hat z+\sin\theta\,\hat\rho$ yazılıp ortalanınca $\langle\cos^2\theta\rangle=\tfrac12$, $\langle\cos\theta\sin\theta\rangle=0$ olduğundan:
$$\bigl\langle 3(\hat\omega\cdot\hat r)\hat r - \hat\omega \bigr\rangle = \left(3\cdot\tfrac12 - 1\right)\hat\omega = \tfrac12\,\hat\omega$$
$$\Longrightarrow\quad \langle\Omega\rangle^{\text{kutupsal}} = \frac{\xi R^3\omega_{gövde}}{4r^3} = \tfrac12\,\Omega_{yerel}$$

> **İki ayrı $\tfrac12$ vardır ve ikisi de gereklidir:** biri *kinematik* (rotasyon vektörü = vortisitenin yarısı, Adım 3), diğeri *geometrik* (kutupsal yörünge ortalaması, Adım 4). Yalnız birinin uygulanması sonucu tam iki kat şişirir.

5. **Sayısal değerlendirme (Dünya / GP-B).** $I=0{,}3307\,M_\oplus R_\oplus^2 = 8{,}02\times10^{37}$ kg·m², $\omega_\oplus=7{,}292\times10^{-5}$ rad/s, dolayısıyla $J_\oplus=5{,}85\times10^{33}$ kg·m²/s; $r=R_\oplus+642\ \text{km}=7013$ km:

$$\Omega_{yerel} = \frac{GJ_\oplus}{c^2r^3} = 1{,}26\times10^{-14}\ \text{rad/s} = 81{,}9\ \text{mas/yıl}$$
$$\langle\Omega\rangle^{\text{kutupsal}} = \tfrac12\times81{,}9 = 41{,}0\ \text{mas/yıl}$$

### Sonuç

$$\boxed{\;\langle\Omega\rangle^{\text{kutupsal}} = \frac{\xi R^3\omega_{gövde}}{4r^3} = 41{,}0\ \text{mas/yıl}\;;\qquad \xi_{\text{GP-B}} = (4{,}2\pm0{,}8)\times10^{-10}\;}$$

| Büyüklük | Değer | Sapma |
|---|---|---|
| GP-B ölçümü | $37{,}2\pm7{,}2$ mas/yıl | 1σ: 30,0–44,4 |
| **Bu türetim** | **41,0** | **0,52σ** ✓ |
| Genel Görelilik | 39,2 | %4,5 |

Kalan %4-5, nokta-dipol yaklaşımının payıdır (GP-B'nin yayımlanmış değeri Dünya'nın tam çekim modelini, yörünge basıklığını ve yüksek çokkutupluları içerir).

### $\xi$'nin Türetimi — Kavrama Kanalı *(28 Temmuz 2026'da eklendi; girdiyi [S]'den [T]'ye taşır)*

$\xi$ uzun süre gözlemle sabitlenmiş bir kesir olarak kaldı ve yapısal biçimi Adım 3'ün Genel Görelilik'e eşlenmesinden alındı. Bu bölüm onu teori-içi büyüklüklerden türetir; **GR'a başvurulmaz.**

**Hangi eşik?** Teorinin hız merdiveni (M-6) iki ayrı eşik taşır ve karıştırılmamalıdır:

| Eşik | Fiziksel olay | Yönettiği |
|---|---|---|
| $c=\sqrt{P/\rho}$ | **kavrama/patinaj** (sonik sınır, M-1) | dönme sürüklenme kesri $\xi$ |
| $v_{kav}=\sqrt2c\sqrt{1+\Sigma/P_0}$ | **kavitasyon/yırtılma** (kohezyon, M-4) | öteleme artık sürüklemesi (M-43) |

$\xi$'yi $v_{kav}$'a bağlama girişimi başarısızdır ve nedeni yapısaldır: $\xi$ bir yırtılma değil bir **patinaj** büyüklüğüdür — adı da bunu söyler. Doğru eşik $c$'dir.

**Adım 1 — Kavramanın yerel ölçüsü.** Ortam bir cismi ancak kavrama hızının o bölgede *bozulduğu* ölçüde tutar; bozulma yoksa ($\delta c=0$) tutamaç da yoktur. Bozulmanın kesri M-42'den doğrudan gelir — yüzeyde
$$\left|\frac{\delta c_{loc}}{c}\right|_{yüzey} = \frac{2\Phi}{c^2}$$
(2 çarpanı **ışık bükülmesinden** sabitlenmiştir, M-42; GP-B'den değil).

**Adım 2 — Dönmenin geometrik ağırlığı.** Öteleme kütleyi düz toplarken dönme onu $r^2$ ile ağırlıklandırır; kesre giren geometrik çarpan bu yüzden atalet momenti oranıdır, $I/MR^2$.

**Adım 3 — Kavrama kesri.** $\xi$ boyutsuzdur ve cismin ortamdaki tutamacını ölçer; ortamı niteleyen tek yerel boyutsuz büyüklük $\delta c/c$, cismi niteleyen tek geometrik oran $I/MR^2$'dir. Serbest sayısal katsayı yoktur:

$$\boxed{\;\xi \;=\; \frac{I}{MR^{2}}\left|\frac{\delta c_{loc}}{c}\right| \;=\; \frac{I}{MR^{2}}\cdot\frac{2\Phi}{c^{2}} \;=\; \frac{I}{MR^{2}}\left(\frac{v_{kaç}}{c}\right)^{2}\;}$$

Dünya için: $0{,}3307\times1{,}392\times10^{-9} = \mathbf{4{,}605\times10^{-10}}$.

**Bu, Adım 3'ün GR eşlemesinin verdiği değerin birebir aynısıdır** ($\xi=2GI/c^2R^3$). İki yol bağımsızdır — biri Lense–Thirring'den, diğeri bükülmeyle sabitlenmiş $\delta c/c$'den — ve aynı sayıda buluşur. Teorinin kendi makinesi GR'ın gravitomanyetik katsayısını yeniden üretmiştir.

**Sonucu: GP-B artık öngörüdür.** Zincir tümüyle teori-içidir — ışık bükülmesi → M-42'nin $c_{loc}=c\Lambda^2$'si → $\delta c/c=2\Phi/c^2$ → $\xi$ → 41,0 mas/yıl. GP-B'nin $37{,}2\pm7{,}2$ ölçümü bu zincire **girdi değil**, sınavdır (0,52σ ✓). Girdinin rozeti bu nedenle [T (yapı) / S ($\xi$)]'den **[T]**'ye yükselmiştir.

**Sınır kontrolleri.** $\Phi\to0$ (uzak, sığ kuyu): $\xi\to0$, ortam hiç dönmez ✓. Kompaktlık arttıkça $\xi$ büyür (aşağıdaki tablo); ancak bağıntı birinci mertebedir ve $\xi\to1$ yaklaşırken doğrusal biçim geçerliliğini yitirir.

### Aynı Sonucun Kalibrasyon Okuması: $\Phi/c^2$'nin İkinci Ölçümü

Adım 3'ün eşlemesi $\xi R^3/2 = GI/c^2$ çözülünce kesrin yapısı çıkar:

$$\boxed{\;\xi = \frac{2GI}{c^2R^3} = 2\left(\frac{I}{MR^2}\right)\frac{GM}{c^2R} = 2\left(\frac{I}{MR^2}\right)\frac{\Phi}{c^2}\;}$$

Sağdaki $\Phi/c^2$, **M-8'in arka plan basıncını sabitlemek için kullandığı gözlemsel girdinin aynısıdır** (GPS 38 µs/gün + Pound–Rebka). Teori böylece atom saati kaymasıyla jiroskop sürüklenmesini tek sayıya bağlar; sınandığında:

| $\Phi/c^2$ kaynağı | Değer |
|---|---|
| GPS + Pound–Rebka (M-8 girdisi) | $7{,}0\times10^{-10}$ |
| GP-B jiroskobundan (bu türetimle) | $(6{,}3\pm1{,}2)\times10^{-10}$ |
| Sapma | **0,55σ** ✓ |

İki bağımsız deney sınıfı — yörüngedeki jiroskop ve yerdeki atom saatleri — teorinin makinesinden geçirildiğinde aynı sayıda buluşur.

> **Bu buluşmanın statüsü.** Bir önceki sürümde buraya şu çekince konmuştu: *"Veri bağımsızdır ama köprü türetilmemiş, GR'ın Lense–Thirring ifadesine eşlenmiştir; dolayısıyla bu bir tutarlılık sınavıdır, parametresiz öngörü değildir."* **Bu çekince artık geçerli değildir** — yukarıdaki "$\xi$'nin Türetimi" bölümü köprüyü teori-içi kurar: $\xi=(I/MR^2)|\delta c_{loc}/c|$, ve $|\delta c_{loc}/c|=2\Phi/c^2$ M-42'de **ışık bükülmesinden** sabitlenmiştir. GR'a başvurulmaz.
>
> Dolayısıyla bu bölüm iki ayrı şeyi birden söyler: (i) $\Phi/c^2$, jiroskop ve atom saati gibi ortak sistematiği olmayan iki deney sınıfından aynı sayıyla okunur — gerçek bir çapraz ölçüm; (ii) $\xi$'nin GR eşlemesiyle bulunan biçimi ile kavrama kanalından türetilen biçimi **birebir aynıdır**, yani teori GR'ın gravitomanyetik katsayısını bağımsızca yeniden üretir. Çekincenin kaldırılmasıyla girdinin rozeti **[T]** olmuştur ve M-8'in $P_0$ kalibrasyonu için ikinci dayanak olma değeri artık çekincesizdir.

### Kompaktlık Ölçeklemesi ve Ergosfer

$\xi\propto\Phi/c^2$ olduğundan dönme sürüklenmesi kompaktlıkla ölçeklenir:

| Cisim | $\Phi/c^2 = GM/c^2R$ | $\xi$ |
|---|---|---|
| Dünya | $7{,}0\times10^{-10}$ | $4{,}6\times10^{-10}$ |
| Güneş | $2{,}1\times10^{-6}$ | $1{,}4\times10^{-6}$ |
| Nötron yıldızı (1,4 M☉, 12 km) | $0{,}17$ | $\approx0{,}11$ |
| Karadelik ufku | $\to O(1)$ | $\to O(1)$, 1'e **yaklaşır** |

$\xi\to O(1)$, ortamın neredeyse tam eş-dönüşe geçmesi — hiçbir cismin durağan kalamaması — demektir; bu, ergosferin tanımıdır. Teori ergosfere mekanik bir okuma verir: **dönme sürüklenmesinin doyduğu yüzey.**

> **Doygunluk asimptotiktir, tam değildir.** Önceki sürüm "$\xi\to1$" yazıyordu. Doygunluğu belirleyen şey iç kavrama kesridir ($\phi$, aşağıdaki bölüm) ve nötron maddesinde bile $\phi<1$ kalır: cepler sıkı paketlenir ama **nötronun kendi iç yapısı vardır**. Dolayısıyla $\xi$ 1'e yaklaşır, ona eşit olmaz.

### İki Kavrama Kanalı: İçeride Kafes, Dışarıda Alan

$\xi$ ile M-39'un $\phi$'si **aynı büyüklüğün iki değeri değil, iki ayrı alandır** ve karıştırılmaları teorinin görünürdeki en sert iç çelişkisini üretir ($\xi\approx5\times10^{-10}$ ↔ $\phi\approx0{,}6$). Ayrım:

| | Nerede | Neyle kavranır | Büyüklük |
|---|---|---|---|
| **İç kavrama** | kafesin *içinde*, atomlar arasında | **maddeyle** — deplasman kafesi | $\mathcal{R}=\phi=1-1/n^2$ (M-16) |
| **Dış sürüklenme** | yüzeyin *dışında*, boşlukta | **alanla** — kavrama hızı bozulması | $\xi=(I/MR^2)\,\lvert\delta c_{loc}/c\rvert$ |

İçeride kafes var ve ortamı mekanik olarak tutar. Dışarıda kafes **yok**, dolayısıyla o kanal orada mevcut değildir; kalan tek tutamaç $\delta c/c$ bozulmasıdır. **İkisinin sınırda eşleşmesi gerekmez** — sınır tam olarak kafesin bittiği yerdir ve kafes sürekli bir alan değil, bir malzeme yapısıdır. Kalınlığı da kafes aralığıdır; ayrı bir uzunluk ölçeği gerekmez.

Bu, iki formülün **neden yapısal olarak farklı** olduğunu da açıklar: iç kavrama malzeme büyüklüğü taşır ($n$, dolayısıyla $\phi$), dış sürüklenme yalnız alan büyüklükleri ($\Phi$, $I/MR^2$). Birinin diğerinin limiti olması beklenmemelidir.

**Kafes sınıfları (M-39'un kompozisyon ekseni).** İç kavrama, kafesin *bağlı* olup olmamasına duyarlıdır:

| Sınıf | Kafes durumu | $\phi$ |
|---|---|---|
| Kayaç gezegen | atom kafesi, sıkı paketli | ~0,6 |
| Gaz devi | moleküler/metalik hidrojen — **yoğun madde, plazma değil** | ~0,5–0,7 |
| Yıldız | **tam iyonize plazma → bağlı kafes yok** | $\sim10^{-15}$ |
| Nötron yıldızı | iç boşluk yok, cepler paketli | ~0,7–0,9 |
| Karadelik | kilitli | 1'e yaklaşır |

### Minimum Karadelik Kütlesi — Kilitli Kafesin Bedava Öngörüsü

Karadelik, kafesi kilitlenene kadar sıkışmış maddeyse (dönen bir cismin açısal momentumunu taşıyan bir yapı olmak zorundadır), yarıçapı $R_\rho=(3M/4\pi\rho_n)^{1/3}\propto M^{1/3}$ ile sınırlıdır. Schwarzschild yarıçapı ise $\propto M$'dir; ikisi tek bir kütlede kesişir:

$$\boxed{\;M_{\min}=\frac{1}{G}\sqrt{\frac{3c^6}{32\pi G\rho_n}} \approx 8{,}3\,M_\odot\;}$$

Altında $R_\rho>R_s$ — sıkışmış cisim ufkunun dışında kalır, karadelik oluşamaz. Nötron yıldızları $\rho_n$'i zaten ~1,4 kat aştığından ($\bar\rho\approx3{,}9\times10^{17}$ kg/m³) tavan yukarı alınırsa $M_{\min}$ **4–8 $M_\odot$** bandına iner.

Gözlemsel karşılık: yıldız-kütleli karadeliklerin ölçülen alt kenarı ~5 $M_\odot$'dir ve nötron yıldızı üst sınırı (~2,2 $M_\odot$) ile arasındaki **kütle boşluğu** tam bu banda düşer. Teori boşluğu bir seçim etkisi değil, **yapısal bir eşik** olarak okur. *(Rozet: $\rho_n$'in gerçek sıkışma tavanı olup olmadığı türetilmediğinden mertebe öngörüsüdür, kesin sayı değil.)*

### Geçerlilik Sınırı

- **Ayırt edici değildir.** Sonuç GR ile yapısal olarak özdeştir; kazanç, sayının akışkan denklemlerinden ek serbest parametre üretmeden çıkması ve $\xi$'nin Ek C'de *eksilen* bir kalem ([S]) olmasıdır. Aynı dürüstlük M-27'nin dikey salınım kaydında da geçerlidir.
- Stokes rotleti düşük-Reynolds/kararlı akış çözümüdür; kısmi sürüklenme ($\xi\ll1$) rejiminde doğrusal ölçekleme varsayılır.
- Nokta-dipol yaklaşımı; gövdenin çokkutupluları %4-5 düzeyinde katkı verir.
- $\xi\to1$ rejiminde doğrusal ölçekleme geçerliliğini yitirir; kompaktlık tablosunun son iki satırı ekstrapolasyondur.

### Açık Uçlar

- ~~$\xi\propto\Phi/c^2$ ilişkisinin türetilmesi~~ → **çözüldü** (yukarıda, "$\xi$'nin Türetimi"): kavrama kanalından $\xi=(I/MR^2)|\delta c_{loc}/c|$; GP-B tutarlılık denetiminden **öngörüye** dönmüştür. Geriye kalan: bağıntının $\omega_1$ deşarj mekanizmasıyla mikroskobik eşlenmesi ve $\xi\to1$ rejiminde doğrusal biçimin ötesine geçilmesi.
- Nötron yıldızı rejiminde $\xi\approx0{,}11$'in gözlemsel sonuçları: PSR B1828-11 devinimi ve pulsar glitch programıyla (3.1.8, $\kappa_d$) bağlanması.
- LAGEOS-1'in 31 mas/yıl'lık düğüm sapmasının aynı $\xi$ ile bağımsız yeniden üretimi (eğik yörünge için geometrik çarpan farklıdır).

---

## M-41 · Yörünge Düzlemi Sürüklenmesi: LAGEOS Düğüm Kayması · **[T]**

**Kullanıldığı bölümler:** 6.3.3 (LAGEOS), Postülat 7. Bağlı katalog: M-23 (aynı Coriolis yapısı), M-40 (aynı $\xi$ ve aynı alan).

M-40 jiroskop **spininin** sürüklenmesini verdi. LAGEOS'ta ölçülen ise farklı bir gözlemlenebilirdir: **yörünge düzleminin** kendisinin sürüklenmesi (düğüm kayması). İkisi aynı alandan çıkar ama farklı mekanizmayla — biri paralel taşıma, diğeri **kuvvet**.

### Varsayımlar

1. Ortamın dönme alanı M-40'tan alınır: $\vec\Omega_{rot} = \dfrac{G}{c^2r^3}\left[3(\vec J\cdot\hat r)\hat r - \vec J\right]$ (aynı $\xi$, yeni parametre yok).
2. **Uydu, yerel olarak dönen ortam içinde hareket eder ve Coriolis ivmesi duyar** — M-23'ün atmosferik dolaşım için türettiği $-2\vec\Omega\times\vec v$ yapısının birebir aynısı, bu kez yörünge ölçeğinde:
$$\vec a_{pert} = -2\,\vec\Omega_{rot}\times\vec v$$
3. Pertürbasyon küçüktür; Gauss yörünge denklemleri geçerlidir.

### Adımlar

**1. Geometri.** Yörünge normali $\hat n$, eğiklik $i$; düğüm doğrusu $\hat e_1$, $\hat e_2=\hat n\times\hat e_1$; konum $\hat r = \cos u\,\hat e_1+\sin u\,\hat e_2$; hız $\vec v = v(-\sin u\,\hat e_1+\cos u\,\hat e_2)$. Buradan $\hat z = \cos i\,\hat n + \sin i\,\hat e_2$ ve $\cos\theta = \hat z\cdot\hat r = \sin i\sin u$.

**2. Düzlem-dışı (normal) bileşen.** İki çapraz çarpımın $\hat n$ izdüşümleri: $(\hat r\times\vec v)\cdot\hat n = v$ ve $(\hat z\times\vec v)\cdot\hat n = v\sin i\sin u$. Dolayısıyla:

$$W \equiv \vec a_{pert}\cdot\hat n = -2\frac{GJ}{c^2a^3}\Bigl[\,3\sin i\sin u\cdot v \;-\; v\sin i\sin u\,\Bigr] = -\frac{4\,GJ\,v\,\sin i\,\sin u}{c^2a^3}$$

**3. Gauss düğüm denklemi** (dairesel yörünge, $r=a$, $v=na$):

$$\frac{d\Omega_{düğüm}}{dt} = \frac{a\sin u}{n a^2 \sin i}\,W = -\frac{4\,GJ\,\sin^2 u}{c^2 a^3}$$

**4. Yörünge ortalaması** ($\langle\sin^2u\rangle = \tfrac12$):

### Sonuç

$$\boxed{\;\left|\frac{d\Omega_{düğüm}}{dt}\right| = \frac{2\,G J}{c^2 a^3\,(1-e^2)^{3/2}}\;}$$

Yön, merkez cismin dönüş yönüyle aynıdır (prograd sürükleme) — gözlenen yön budur.

| Uydu | $a$ | $e$ | **Bu türetim** | Gözlem |
|---|---|---|---|---|
| LAGEOS-1 | 12.270 km | 0,0045 | **30,6 mas/yıl** | ~31 mas/yıl (Ciufolini & Pavlis, 2004) |
| LAGEOS-2 | 12.163 km | 0,0135 | **31,4 mas/yıl** | aynı program |

**Önemli yapısal sonuç:** Formülde eğiklik $i$ **yoktur** — düğüm sürüklenme hızı eğiklikten bağımsızdır. Eğiklik yalnızca bu etkinin Newtonyen $J_2$ düğüm gerilemesinden (LAGEOS için ~126°/yıl, yani $10^7$ kat büyük) *ayrıştırılmasında* rol oynar; iki LAGEOS'un farklı eğiklikte olması, $J_2$ belirsizliğini birleşik analizde eleyebilmek içindir. Etkinin *büyüklüğünü* eğiklik belirlemez.

### Neden M-40'tan farklı bir çarpan çıkıyor

İki gözlemlenebilir aynı alandan beslenir ama farklı fizikle ölçülür:

| | Mekanizma | Geometrik işlem | Sonuç |
|---|---|---|---|
| **M-40** (jiroskop spini) | paralel taşıma: $\tfrac12\nabla\times\vec v$ | kutupsal yörünge ortalaması $\times\tfrac12$ | $\tfrac12\,GJ/c^2r^3$ |
| **M-41** (yörünge düzlemi) | **kuvvet:** Coriolis $-2\vec\Omega\times\vec v$ | Gauss düğüm denklemi + ortalama | $2\,GJ/c^2a^3$ |

Oran 4'tür ve tamamen mekanizma farkından gelir — aynı $\xi$, aynı alan, iki farklı ölçüm. Bu, M-40'ın bağımsız bir doğrulamasıdır: tek kalibrasyon iki ayrı deneyi birden karşılar.

### Geçerlilik Sınırı

- Türetim dairesel yörünge içindir; $e$ bağımlılığı $(1-e^2)^{-3/2}$ olarak standart Gauss açılımından eklenmiştir (LAGEOS'un $e\lesssim0{,}014$'ünde etki %0,03'ün altında).
- Nokta-dipol yaklaşımı; gövdenin yüksek çokkutupluları ihmal edilmiştir.
- Gözlemsel ayrıştırma bu türetimin dışındadır: $J_2$ düğüm gerilemesi bu etkinin $10^7$ katıdır ve ayrıştırma yer çekim alanı modelinin (GRACE/GOCE) hassasiyetine bağlıdır.

### Açık Uçlar

- Aynı Coriolis yolunun günberi (perigee) kaymasına uygulanması — bağımsız bir üçüncü sınav verir.
- Kutupsal olmayan yörüngeler için jiroskop spin presesyonunun eğiklik bağımlılığı (M-40'ın $\tfrac12$'si kutupsal yörüngeye özgüdür).

---

## M-42 · Ölçek Yapısı $\Lambda$: Cetvel, Saat ve Işık Hızının Ortak Çarpanı · **[T]**

**Kullanıldığı bölümler:** 2.4.2 (Yön Kuralı), 4.2.15 (İtiraz 3), 6.2.3, 6.2.5–6.2.6, 6.3.3. Bağlı katalog: M-1, M-8, M-19, M-21, M-40.

Bu girdi, teorinin uzun süre açık kalan **2 çarpanı** sorununu çözer: ışık bükülmesinin neden 0,876″ değil 1,751″ olduğu, jeodetik presesyonun neden $\tfrac32$ katsayısıyla geldiği ve Lorentz testlerinin neden hiçbir şey görmediği tek bir yapıdan çıkar.

### Sorunun kurulumu

$\epsilon \equiv \Phi/c^2$ tanımlayıp üç yerel büyüklüğün arka plana göre ölçeklenmesini bilinmeyen üslerle yazalım:

$$c_{loc} = c\,(1+\gamma_c\,\epsilon),\qquad \ell_{loc} = \ell\,(1+\gamma_\ell\,\epsilon),\qquad f_{loc} = f\,(1+\gamma_f\,\epsilon)$$

Burada $c_{loc}$ Zerre'nin arka plan (düz) uzayda ölçülen yayılma hızı, $\ell_{loc}$ maddeden yapılmış bir cetvelin uzunluğu, $f_{loc}$ yerel bir saatin tik hızıdır. Teorinin önceki sürümü örtük olarak $\gamma_c=\gamma_f=-1$ ve $\gamma_\ell=0$ alıyordu; aşağıda bunun bükülmeyi yarım verdiği görülecektir.

### Adımlar — üç kısıt, üç üs

**Kısıt 1 — Kütleçekimsel kızıla kayma (ölçülmüş).** GPS'in günde 38 µs'si ve Pound–Rebka genliği, saat hızının potansiyelle nasıl değiştiğini doğrudan verir:
$$\frac{\delta f}{f} = -\frac{\Phi}{c^2} \quad\Longrightarrow\quad \boxed{\gamma_f = -1}$$

**Kısıt 2 — Işık bükülmesi (ölçülmüş).** Teorinin ontolojisinde uzay düzdür; bükülme, düz arka planda değişken yayılma hızının Fermat ilkesiyle ürettiği kırılmadır. Uzak saatle ölçülen uçuş süresi
$$T = \int\frac{ds}{c_{loc}} = \frac1c\int\left(1-\gamma_c\epsilon\right)ds \quad\Longrightarrow\quad n_{eff} = 1-\gamma_c\,\epsilon$$
Bükülme açısı $\delta = 2(-\gamma_c)\,GM/c^2b$ olduğundan, Güneş kenarı için ölçülen $1{,}751''$:
$$\boxed{\gamma_c = -2}$$
($\gamma_c=-1$ seçimi $0{,}876''$ verir — Soldner/Newton değeri, gözlemin tam yarısı.)

**Kısıt 3 — Yerel $c$ değişmezliği (ölçülmüş).** Yerel bir gözlemci ışık hızını kendi cetveli ve saatiyle ölçer; ölçtüğü sayı $c_{loc}/(\ell_{loc}f_{loc})$'dur. Dönen rezonatör ve optik saat deneyleri bu sayının $10^{-18}$ düzeyinde sabit olduğunu göstermiştir:
$$\gamma_c = \gamma_\ell + \gamma_f \quad\Longrightarrow\quad -2 = \gamma_\ell - 1 \quad\Longrightarrow\quad \boxed{\gamma_\ell = -1}$$

### Sonuç — tek ölçek çarpanı

Üç üs tek bir çarpana iner. **Madde ölçeği** tanımlanır:

$$\boxed{\;\Lambda \equiv 1 - \frac{\Phi}{c^2}\;;\qquad \ell_{loc} \propto \Lambda,\qquad f_{loc}\propto\Lambda,\qquad c_{loc}\propto\Lambda^{2}\;}$$

Yapı kendi içinde kapanır:

| Bağıntı | Kontrol |
|---|---|
| Işık-saati: $f = c_{loc}/\ell_{loc} \propto \Lambda^2/\Lambda = \Lambda$ | ✓ gözlenen kızıla kayma |
| Yerel ölçüm: $c_{loc}/(\ell_{loc}f_{loc}) \propto \Lambda^2/\Lambda^2 = 1$ | ✓ Lorentz testleri null |
| Optik yol: $n_{eff} = 1/\Lambda^2 = 1+2\Phi/c^2$ | ✓ $1{,}7512''$ |

**Kritik notasyon ayrımı.** Teorinin "yerel ışık hızı" dediği iki farklı büyüklük vardır ve karıştırılmamalıdır:
- **$\Lambda$** — madde ölçeği; saatleri, cetvelleri ve atomik geçiş frekanslarını yönetir. Kızıla kayma ve Zerre-Saati formüllerinde geçen budur (M-20, M-21).
- **$c_{loc} = c\Lambda^2$** — Zerre'nin arka plandaki yayılma hızı. Bükülme, Shapiro gecikmesi ve $n_{eff}$'te geçen budur.

Önceki sürüm ikisini tek büyüklük sayıyordu; 2 çarpanının kökeni tam olarak bu birleştirmeydi.

### M-19 ile Yapısal Simetri

Bu çözüm teoriye yabancı bir hamle değildir; teorinin **hareket** için zaten yaptığının potansiyele uzatılmasıdır:

| | Cetvel | Saat | Yayılım | Yerel ölçüm $\dfrac{c_{yay}}{\ell f}$ |
|---|---|---|---|---|
| **Hareket** (M-19) | $\ell/\gamma$ | $f/\gamma$ | $c/\gamma^{2}$ *(paralel kolda yol uzaması)* | $\dfrac{c/\gamma^2}{(\ell/\gamma)(f/\gamma)}=\dfrac{c}{\ell f}$ ✓ M&M null |
| **Kütle-itim** (M-42) | $\ell\Lambda$ | $f\Lambda$ | $c\Lambda^{2}$ | $\dfrac{c\Lambda^2}{(\ell\Lambda)(f\Lambda)}=\dfrac{c}{\ell f}$ ✓ Lorentz null |

**Simetrinin tam ifadesi.** Cetvel ile saatin aynı çarpanla ölçeklenmesi, ortamı yerel ölçümden gizlemek için **tek başına yeterli değildir**: $\ell$ ve $f$ birlikte çarpanın *karesini* üretir, dolayısıyla yayılım teriminin de aynı kareyi taşıması gerekir. İki durumda da tam olarak bu olur — ve mekanizmaları farklıdır: harekette kare, hareket yönündeki gidiş-dönüş yolunun $\gamma^2$ uzamasından gelir (M-19 Adım 2'nin boy kısalması tartışması); kütle-itimde ise doğrudan $c_{loc}=c\Lambda^2$ ölçeklemesinden. Değişen yalnız çarpanın kaynağıdır: $1/\gamma \approx 1-v^2/2c^2$ ↔ $\Lambda = 1-\Phi/c^2$.

Bu, $\gamma_\ell = \gamma_f$ eşitliğinin neden doğal olduğunu da açıklar: teori hareket kolunda cetvel ve saati zaten tek ortak çarpana bağlamıştı; potansiyel kolunda aynı yapının tekrarlanması yeni bir varsayım değil, mevcut yapının uzatılmasıdır.

### Kapanan Gözlemler

$\Lambda$ yapısı, PPN dilinde $\gamma_{PPN}=1$ vermeye denktir; $\gamma$'ya bağlı tüm birinci mertebe sınavları birden karşılar:

| Gözlem | Bu yapıyla | Ölçüm |
|---|---|---|
| Işık bükülmesi (Güneş kenarı) | **1,7512″** | 1,7510″ ✓ |
| Jeodetik presesyon (GP-B) | **~6.606 mas/yıl** | 6.601,8 ± 18,3 ✓ |
| Shapiro gecikmesi (Dünya–Mars, teğet) | **≈247 µs** (aşağıda hesaplandı) | ≈250 µs ✓ |
| Kütleçekimsel kızıla kayma | $-\Phi/c^2$ | GPS, Pound–Rebka ✓ |
| Lorentz ihlali sınırları | yapısal olarak null | $10^{-18}$ ✓ |

**Shapiro gecikmesinin hesabı.** Aynı $n_{eff}$ Fermat integraline sokulur; ek varsayım yoktur:
$$\Delta t = \frac1c\int (n_{eff}-1)\,ds = \frac{2GM}{c^3}\int\frac{ds}{r} \quad\Longrightarrow\quad \Delta t_{gidiş-dönüş} = \frac{4GM}{c^3}\,\ln\!\frac{4r_1r_2}{b^2}$$
Güneş kenarına teğet geçen Dünya–Mars sinyali için ($r_1=1$ AU, $r_2=1{,}524$ AU, $b=R_\odot$): $4GM_\odot/c^3 = 1{,}97\times10^{-5}$ s ve $\ln(2{,}82\times10^{5}) = 12{,}55$, dolayısıyla
$$\Delta t \approx 247\ \mu\text{s}$$
Ölçülen değer ≈250 µs'dir (Shapiro, 1964; Viking: Reasenberg ve ark., 1979). **Yarım indis ($n=1+\Phi/c^2$) bu sayının tam yarısını (≈124 µs) verir ve gözlemle kesin olarak çelişir** — yani Shapiro, 2 çarpanının bükülmeden bağımsız **üçüncü** doğrulamasıdır. Cassini'nin daha keskin ölçümü PPN $\gamma$'yı $1+(2{,}1\pm2{,}3)\times10^{-5}$ olarak sabitler (Bertotti ve ark., 2003); yapının verdiği $\gamma=1$ bu bantla uyumludur.

**Muhasebe:** İki gözlem girdi olarak kullanılır (bükülme → $\gamma_c$; yerel değişmezlik → $\gamma_\ell$); üç gözlem çıktı olarak öngörülür (kızıla kayma, jeodetik presesyon, Shapiro). Net kazanç bir öngörüdür — ve daha önemlisi, kızıla kayma artık *kalibrasyon* değil *öngörü* konumuna geçer.

### $P_0$ Üzerindeki Sonucu

M-8, $P_0$'ı kızıla kayma genliğinden sabitlerken $\delta c/c = \delta f/f$ eşitliğini kullanıyordu. $\Lambda$ yapısında bu eşitlik geçersizdir ($\delta c/c = 2\,\delta f/f$), dolayısıyla zincir yeniden çalışır:

$$\frac{1-k}{2}\cdot\frac{-\rho_n\Phi}{P_0} = -\frac{2\Phi}{c^2} \quad\Longrightarrow\quad \boxed{P_0 = \frac{1-k}{4}\,\rho_n c^2\;,\qquad \rho_0 = \frac{1-k}{4}\,\rho_n}$$

$k=0$ için $P_0 \approx 6{,}1\times10^{33}$ Pa ve $\rho_0\approx\rho_n/4 \approx 6{,}8\times10^{16}$ kg/m³. Mertebe değişmez; M-7'nin alt sınırı ($1{,}6\times10^{25}$ Pa) hâlâ sekiz-dokuz mertebe aşılır. Monizm ifadesi "madde, okyanusun ~4 kat sıkışmış fazıdır" biçimini alır. **Ayrıca $P_0$ artık kızıla kaymadan değil bükülmeden sabitlenir** — kızıla kayma serbest kalıp öngörüye dönüştüğü için.

### Geçerlilik Sınırı

- Yapı **birinci mertebedir** ($O(\Phi/c^2)$). PPN dilinde yalnız $\gamma=1$'i verir; $\beta$ parametresi (ortamın doğrusal-olmayan tepkisi, $O(\Phi^2/c^4)$) belirlenmemiştir.
- Bu nedenle **Merkür günberi kayması hâlâ kapanmamıştır:** presesyon $\frac{2+2\gamma-\beta}{3}$ ile ölçeklenir; $\gamma=1$ sağlandı, $\beta=1$ gerekiyor. $\beta$ olmadan öngörü $\frac{4-\beta}{3}\times43''$/yüzyıldır.
- $\Lambda$ yapısı **ortak-mod** bir etkidir: bölgedeki hem ortamı hem ölçüm aletlerinin maddesini birlikte ölçekler. Maddi ortamdaki (cam, su, fiber) kırılma ise **diferansiyeldir** — yalnız ışığın yolunu değiştirir, gözlemcinin cetvelini değiştirmez. Bu yüzden $1/n^2=1-\phi$ (M-15) ve $f=\phi=1-1/n^2$ (M-16) türetimleri bu yapıdan **etkilenmez** ve maddi ortamda ışığın yavaşlaması yerel olarak ölçülebilir kalır.

### Açık Uçlar

- **$\beta$ parametresi:** Ortamın $O(\Phi^2)$ tepkisinin $P(\Phi)$ hâl ilişkisinden türetilmesi. Kapanırsa Merkür'ün 43″'si de kapanır — teorinin kalan tek klasik GR sınavı.
- **$\gamma_\ell=-1$'in mekanizması:** Cetvellerin neden tam $\Lambda$ ile büzüldüğü, atomun/nükleonun ortam içindeki denge boyutundan birinci-ilkelerle türetilmelidir. Şu an yerel değişmezlik gözleminden sabitlenmiştir (M-19'un boy kısalmasının kendi mekanik türetiminin de açık olması gibi).
- **Ayırt edicilik:** $\gamma=1$ ile teori 1PN düzeyinde GR ile gözlemsel olarak ayrışmaz. Ayrışma ancak $\beta$'da veya ikinci mertebede aranabilir.

- **Yapının türü ve $\beta$'nın neden ayrı iş olduğu (denetim notu, 28 Temmuz 2026).** Bu türetim biçimsel olarak bir **optik-ortam** (etkin kırılma indisi) kuruluşudur: düz arka plan + konuma bağlı $c_{loc}$ + Fermat ilkesi. Bu sınıfın bilinen bir kapsamı ve bilinen bir sınırı vardır ve teorinin durumu tam olarak o sınıra oturur:
  - **Kapsam:** Işık yolu gözlemleri — bükülme, Shapiro gecikmesi, merceklenme, $\gamma$'ya bağlı her şey. Bunları tek indisle, ek varsayım olmadan verir. ✓
  - **Sınır:** Kütleli cisim yörüngeleri. Bir skaler indis, $n$'nin hıza bağlı olmadığı sürece kütleli parçacıkların hareketini tam üretmez; günberi kaymasının ikinci mertebe payı bu yüzden indisin *dışındadır*.

  Yani Merkür'ün açık kalması rastlantı ya da eksik hesap değil, **kullanılan yapının cinsinden gelen bir sınırdır.** Kapanması için ortamın hâl ilişkisinin ($P(\Phi)$) ikinci mertebe terimi gerekir — yani optik analojiden çıkıp ortamın dinamiğine geçmek gerekir. Bu, $\beta$'yı "hesaplanmayı bekleyen bir sayı" olmaktan çıkarıp **yapısal bir sonraki adım** hâline getirir; 7.4 md.12 bu çerçevede okunmalıdır.

---

## M-43 · Altkritik Bastırma: Artık Kuplajın Süper-Akışkan Çerçevesi · **[T (yapı) / S ($n$)]**

**Kullanıldığı bölümler:** 3.4.5 (sürüklenme zarfı), 3.10.5 (halka sönümü), 7.4 md.13. Bağlı katalog: M-4 ($v_{kav}$), M-5 ($v_m$), M-37 ($\tau_{ret}$, $\eta_E$), M-40 ($\xi$).

Bu girdi, M-37'nin Geçerlilik Sınırı'nda nicelenen **sürükleme felaketini** çözer ve $\eta_E$'yi serbest boyutlu parametre olmaktan çıkarır.

### Sorunun kurulumu

Ortam yoğunluğu $\rho_0=6{,}8\times10^{16}$ kg/m³'tür. Klasik eylemsizlik sürüklemesi bu yoğunlukla yazılırsa Phoebe için
$$a_{klasik}=\frac{\tfrac12 C_D\rho_0 v_{bağıl}^2\,\pi a_b^2}{m} \approx \frac{7{,}0\times10^{33}\ \text{N}}{8{,}29\times10^{18}\ \text{kg}} \approx 8{,}4\times10^{14}\ \text{m/s}^2$$
çıkar; oysa 4 Gyr retrograd hayatta kalma $a\lesssim v/t_{GS}\approx2{,}7\times10^{-14}$ m/s² gerektirir. Gereken bastırma
$$S_{gerekli} = \frac{2{,}7\times10^{-14}}{8{,}4\times10^{14}} \approx 3{,}2\times10^{-29}$$
Bu 29 mertebe, M-37'de $\eta_E$ adlı **boyutlu ve serbest** bir katsayıya yüklenmişti; $\rho_0$ ile bağı yoktu.

### Varsayımlar

1. Ortam kohezyonlu bir **süper-akışkandır** (Postülat 1, M-4). Süper-akışkanlarda momentum kaybı viskozlukla sürekli değildir; bir **kritik hız** eşiğinin altında yapısal olarak bastırılır (Landau ölçütünün teorideki karşılığı).
2. Teorinin kritik hızı zaten tanımlıdır ve yeni bir parametre değildir: $v_{kav}=\sqrt2\,c\sqrt{1+\Sigma/P_0}$ (M-4). Eşiğin üstünde ortam yırtılır (kavitasyon → vorteks dökülmesi), altında dökülme yoktur.
3. Artık kuplaj, klasik sürüklemenin altkritik orana bağlı bir kesridir; kesir $v_{bağıl}/v_{kav}\to0$ limitinde **sıfıra gitmek zorundadır** (ideal süper-akışkan limiti).

### Adımlar

**1. Altkritik oranın hesabı.** Güneş Sistemi'ndeki bağıl hızlar kritik hızın neresinde? Bell alt sınırıyla ($\Sigma/P_0>10^8$) $v_{kav}>4{,}2\times10^{12}$ m/s'dir; Phoebe'nin retrograd bağıl hızı $v_{bağıl}\approx3{,}4\times10^3$ m/s:
$$\frac{v_{bağıl}}{v_{kav}} \approx 8\times10^{-10}$$
Sistem **derin altkritik** rejimdedir. Sorunun kökü buradadır: 29 mertebelik bastırma, ortamın bir özelliği değil, **rejimin** özelliğidir.

**2. Bastırma yasasının biçimi.** Varsayım 3 gereği kuplaj, oranın pozitif bir kuvvetiyle bastırılır:
$$F_{artık} = \underbrace{\tfrac12 C_D\,\rho_0\,v_{bağıl}^2\,A}_{\text{klasik}}\;\times\;\underbrace{\left(\frac{v_{bağıl}}{v_{kav}}\right)^{n}}_{\text{altkritik bastırma}}$$

**3. Üssün sabitlenmesi.** $S_{gerekli}=3{,}2\times10^{-29}$ ile $v_{bağıl}/v_{kav}=8\times10^{-10}$ eşitlenir:
$$n = \frac{\ln(3{,}2\times10^{-29})}{\ln(8\times10^{-10})} = \frac{-65{,}6}{-20{,}9} = 3{,}1$$
En yakın tam sayı **$n=3$**'tür. $n=3$ alınırsa eşitlik $v_{kav}\ge1{,}07\times10^{13}$ m/s gerektirir, yani:
$$\frac{\Sigma}{P_0} \gtrsim 6{,}4\times10^{8}\,,\qquad v_m \gtrsim 2{,}5\times10^{4}\,c$$
Bu, Bell'in verdiği alt sınırı ($\Sigma/P_0>10^8$, $v_m>10^4c$) **2,5 kat sıkıştırır** ve onunla çelişmez.

**4. $\eta_E$'nin statüsünün çözülmesi.** M-37'nin doğrusal ansatzı ($F=6\pi\eta_E a_b v$) bastırılmış sürüklemeye eşitlenir:
$$\eta_{E}^{etkin} = \frac{C_D\,\rho_0\,a_b\,v_{bağıl}^{\,1+n}}{12\,v_{kav}^{\,n}} \;\overset{n=3}{=}\; \frac{C_D\,\rho_0\,a_b\,v_{bağıl}^{4}}{12\,v_{kav}^{3}}$$
Phoebe değerleriyle $\eta_E^{etkin}=3{,}3\times10^{-5}$ Pa·s — M-37'nin bağımsız olarak bulduğu üst sınırın **tam olarak kendisi.** (Aynı gözlemden geldiği için bu bir doğrulama değil, tutarlılık kontrolüdür; değeri, iki yazımın birbirine çevrilebilir olduğunu göstermesindedir.)

### Sonuç

$$\boxed{\;F_{artık}=\tfrac12 C_D\rho_0 v_{bağıl}^2 A\left(\frac{v_{bağıl}}{v_{kav}}\right)^{n}\;,\qquad n\simeq3\;,\qquad \eta_E^{etkin}=\frac{C_D\rho_0 a_b v_{bağıl}^{1+n}}{12\,v_{kav}^{n}}\;}$$

Üç kazanç:

| | Önce (M-37) | Sonra (M-43) |
|---|---|---|
| Serbest kalem | $\eta_E$ — **boyutlu** (Pa·s), üst sınırlı | $n$ — **boyutsuz**, tam sayı adayı |
| $\rho_0$ ile bağ | **yok** | $F\propto\rho_0$ açıkça; 29 mertebe rejimden gelir |
| $\Sigma$ ile bağ | yok | $\Sigma/P_0\gtrsim6{,}4\times10^8$ **öngörüsü** |

Ve $\eta_E$ artık **evrensel bir akışkan sabiti değildir**: cisim boyutuyla ve bağıl hızla değişir ($\propto a_b v^4$). Bu, iki yazımı gözlemsel olarak ayırır.

### Ayırt Edici Öngörüler — iki çerçeve gözlemsel olarak ayrışır

Sönüm zamanı $\tau\equiv v/|\dot v|$ iki yazımda farklı ölçeklenir:

| | Stokes yazımı (M-37) | Altkritik yazım (M-43, $n=3$) |
|---|---|---|
| Hız bağımlılığı | $\tau_{ret}$ **bağımsız** | $\tau_{ret}\propto v_{bağıl}^{-(1+n)}=v_{bağıl}^{-4}$ |
| Boyut bağımlılığı | $\tau_{ret}\propto \rho_c a_b^{2}$ | $\tau_{ret}\propto \rho_c a_b$ |

İki bağımsız ayırt edici vardır ve ikisi de mevcut veriyle sınanabilir: retrograd cisim popülasyonu farklı $v_{bağıl}$ ve $a_b$ değerlerine sahiptir. **M-37'nin "$\tau_{ret}$, $e$ ve $i$'den bağımsızdır" öngörüsü bu çerçevede yanlışlanır** — bağımlılık bulunması artık teorinin *beklentisidir*. Üstelik $n$, tek bir cisim yerine popülasyondan **aşırı-belirlenir**: iki farklı cisim $n$'yi ayrı ayrı verir; uyuşmazsa çerçeve düşer.

### Geçerlilik Sınırı

- **$n$ tek gözlemden sabitlenmiştir** (Phoebe) — bu yüzden rozet [S], [T] değil. Türetilmiş değil, *ölçülmüştür*; ilk-ilke değeri vorteks dökülme eşiğinin mikro-modelinden gelmelidir.
- Bastırmanın **kuvvet yasası** biçiminde olduğu varsayılmıştır. Süper-akışkanlarda eşik altı bastırma üstel de olabilir ($e^{-E/E_0}$); üstel biçim aynı tek veriyi de tutturur ve popülasyon testi ikisini ayırır (kuvvet yasası: log-log doğru; üstel: eğri).
- Türetim **öteleme** kanalı içindir ve yalnız orada geçerlidir. M-40'ın dönme kesri $\xi$ bu çerçeveden çıkmaz — ve **çıkmaması gerekir**: $\xi=(v/v_{kav})^1$ eşlemesi denendiğinde ~10 kat tutmaz ve Bell sınırıyla çelişir. Nedeni yapısaldır: $\xi$ bir yırtılma değil **patinaj** büyüklüğüdür, dolayısıyla eşiği $v_{kav}$ değil $c$'dir. Dönme kolu M-40'ın "$\xi$'nin Türetimi" bölümünde kavrama kanalından ayrıca çözülmüştür ($\xi=(I/MR^2)|\delta c_{loc}/c|$). **İki kanal iki eşiğe bağlıdır; birleştirilmeleri beklenmemelidir** (H.1'in kapanış tablosu).
- $C_D$ mertebe-1 alınmıştır; $n$'nin çıkarımı $C_D$'ye logaritmik duyarlıdır (10 kat $C_D$ değişimi $n$'yi ~%5 kaydırır), dolayısıyla sonuç sağlamdır.

### Açık Uçlar

- **$n$'nin ilk-ilkelerden türetimi:** ortamın vorteks dökülme eşiğinin altında momentum aktarımının mikro-mekanizması. $n=3$ tam sayı çıkarsa geometrik bir kökeni olması beklenir.
- **Kuvvet yasası ↔ üstel ayrımı:** retrograd popülasyonun log-log grafiği.
- ~~Dönme kolunun bağlanması~~ → **çözüldü** (M-40, "$\xi$'nin Türetimi"): $\xi$ $v_{kav}$'a değil kavrama eşiği $c$'ye bağlanır; M-40'ın kalibrasyonu öngörüye dönmüştür.
- **Halka sönümüne uygulama:** M-27'nin $\gamma_{Evrenakı}$ terimi bu çerçevede yeniden yazılmalı; Satürn halkalarındaki $v_{bağıl}$ çok küçük olduğu için bastırma daha da güçlüdür — halka ömrü sorununa katkısı hesaplanmalıdır.

---

## M-45 · İki Kolun Güç Eşbölüşümü: $q_n/\gamma_n$ Oranı ve $a_0$'ın Aday Kapanışı · **[T (yapı) / T-aday (eşbölüşüm)]**

**Kullanıldığı bölümler:** 6.5.4.3 (Adım 6–7), 6.5.4.5 (a₀'ın değeri), Kısım X 10.7. Bağlı katalog: M-15/M-39 (kafes=atom), M-35 (açık ucu), Ek A.2 ($\sqrt2c$).

M-35'in açık ucu şuydu: *"$q_n$'nin $\omega_2$ frekansı ve nükleon deplasman hacminden hesabı → $\alpha$ tamamen türetilmiş olur."* Bu türetim o ucu, iki kolun oranı üzerinden **aday** düzeyinde kapatır.

### Varsayımlar

1. **Tek kaynak, iki izdüşüm** (H.0 köken haritası): $\gamma_n$ ($\omega_1$, 3B-içi dönüş) ve $q_n$ ($\omega_2$, W-eksenli pulsasyon), nükleonun tek 4B çift dönüşünün iki düzlem izdüşümüdür.
2. **İzoklinik eş-güç — türetilmiştir**: **(2a)** Ek A.2'nin $\sqrt2c$'si izoklinik kilidin doğrudan ifadesidir — kararlılık her iki değişmez düzlemi ayrı ayrı kavrama sınırında ($c$) doyurur, $\sqrt{c^2+c^2}=\sqrt2c$; iki kanal **tek ortak frekansta** sürülür ve çekirdeğin düzlem enerjileri eşit kilitlenir. **(2b)** Dejenere iki mod, ortak Zerre banyosuyla sürekli alışverişte olduğundan kararlı hâlde mod başına ortalama enerji eşitlenir (eşbölüşüm; değiş-tokuş/vuru yoluyla da aynı sonuç). **(2c)** Eşbölüşümün geçerlilik koşulu hesaplanmış ve kapanmıştır: kanal enerjisi $E=m_pc^2$, sızıntı gücü (alan-kurma işi, üst sınır) $\Delta P\cdot q_n=5{,}8\times10^{-24}$ W → boşalma süresi $\sim0{,}8$ milyon yıl; banyo teması dönüş periyodu ölçeğindedir ($10^{-23}$ s) — $t_{term}/t_{sızıntı}\lesssim10^{-30}$, **36 mertebe marj.** Aynı hesap bir düzeltme de getirir: ışıma düzeltmesi $10^{-30}$ mertebesindedir, dolayısıyla ölçülen %1'lik fark (42,4'e karşı 42,85) fiziksel bir açık değil, medyanın kendi ölçüm hatasının (%3,5) içidir — **oran, ölçüm hassasiyeti neye izin veriyorsa o kadar tam $\sqrt{m_p/m_e}$ olmalıdır** (keskinleşen öngörü; G-9).
3. **Taşıyıcı ayrımı:** dolanım kolunun süredurumunu nükleon özü taşır ($m_p$, yarıçap $r_n$); pulsasyon kolu **deplasman kafesinin** nefesidir ve kafes atomun tamamıdır (M-15/M-39) — kafesin oynak süredurumunu zarfın en hafif bileşeni, elektron kütlesi ($m_e$) taşır. Tür-ayrımlı genel hâl $u_r/v_t=\sqrt{Am_p/(Zm_e)}$'dir (H: 42,85 · He/metaller: 60,6); nükleonların yarıdan fazlası hidrojen olduğundan ($X>0{,}5$) **medyan her ortamda H değerine kilitlenir** — $\ell_\omega$ medyanının bileşimden etkilenmemesini (kütleyle korelasyon $+0{,}03$) bu kilit açıklar ve tür-ayrımlı ikinci bir mod ($\ell\approx51$ fm) öngörür.
4. **Kürsel kaynak yazımı:** $q_n=4\pi r_n^2 u_r$, $\gamma_n=2\pi r_n v_t$ ($u_r$: radyal pulsasyon hızı, $v_t$: teğetsel dolanım hızı).

### Adımlar

1. Eş enerji (Varsayım 2+3): $\tfrac12 m_e u_r^2=\tfrac12 m_p v_t^2 \Rightarrow u_r/v_t=\sqrt{m_p/m_e}=42{,}85$.
2. Vortisite uzunluğu: $\ell_\omega=\dfrac{q_n}{2\gamma_n}=r_n\dfrac{u_r}{v_t}=r_n\sqrt{\dfrac{m_p}{m_e}}=36{,}05$ fm.
3. İvme ölçeği (6.5.4.3 Adım 6 ile): $a_0=\dfrac{\mathcal{G}m_n}{\ell_\omega^2}=\dfrac{\mathcal{G}\,m_n\,m_e}{m_p\,r_n^{2}}=8{,}60\times10^{-11}$ m/s².
4. **Mutlak debiler** (Ek A.2 çapasıyla — kararlı vakum-cepli girdap duvarını $\sqrt2c$'de döndürür → $v_t=\sqrt2c$):
$$\gamma_n=2\pi r_n\sqrt2c=2{,}24\times10^{-6}\ \mathrm{m^2/s},\qquad
q_n=4\pi r_n^2\sqrt2c\sqrt{m_p/m_e}=1{,}62\times10^{-19}\ \mathrm{m^3/s}$$
$u_r\approx61c$'dir — çelişki değildir: pulsasyon cephesi kohezyon kanalında taşınır ($v_m>10^4c$; Ek A.3) ve $c$ mutlak sınır değildir (Postülat 4).
5. $C$–$q_n$ dejenerasyonu kırılır: $C=\dfrac{4\pi \mathcal{G}\rho_n m_n}{q_n}=2{,}35$ kg·m⁻³·s⁻¹ (denetim: $\alpha=Cq_n/4\pi m_n=1{,}80\times10^{7}$ s⁻², $\mathcal{G}=\alpha/\rho_n$ birebir geri çıkar ✓).

### Sonuç

$$\boxed{\;\frac{u_r}{v_t}=\sqrt{\frac{m_p}{m_e}}\;\Longrightarrow\;
\ell_\omega=r_n\sqrt{\frac{m_p}{m_e}}\;\Longrightarrow\;
a_0=\frac{\mathcal{G}\,m_n\,m_e}{m_p\,r_n^{2}}\;}$$

**Gözlemle karşılaştırma:** $u_r/v_t$ ölçülen 42,4 (öngörü 42,85 — %1,1); $\ell_\omega$ ölçülen 35,7 fm (öngörü 36,05 — %1,0; medyanın kendi hatası %3,5); $a_0$ öngörüsü, galaktik beş bağımsız ölçümün bandının ($6{,}8$–$9{,}3\times10^{-11}$) içinde — **sıfır kalibrasyonla.** Blok H'nin "tek serbest çift" dediği $(C,q_n)$ kalemi, bu türetimle **iki ayrı sayıya** çözülür.

### Geçerlilik Sınırı

- **Türetimin iç zinciri tamamlanmıştır** (izoklinik kilit + banyo eşbölüşümü + 36 mertebelik marj hesabı); kalan yapısal vekiller: $m_e$ ataması kafes-atomu okumasına bağlıdır, $r_n$ olarak proton yük yarıçapı vekildir. Başka-yere-bakma hesabı dar aday uzayında ~$2\sigma$, geniş uzayda %40 verir — bu yüzden **bağımsız $\ell_\omega$ ölçümü ve hakem denetimi gelene dek** Ek C'de $a_0$'ın rozeti **[S] kalır**, buradaki kapanış **[T-aday]** olarak kayıtlıdır.
- Yanlışlanabilir sonuçları G-9'dadır: bağımsız $\ell_\omega$ ölçümü 36,0 fm'e yakınsamalı; oran $r_p$ revizyonlarını izlemeli; $a_0^{etkin}$ hiçbir ortamda $X\cdot a_0^{M45}\approx6{,}3\times10^{-11}$ tabanının altına inmemeli.

### Açık Uçlar

- **Mutlak çapa seçimi:** $v_t$ bileşke duvar hızı mı ($\sqrt2c$ — burada kullanılan) düzlem-başına hız mı ($c$)? Oranı ve $a_0$'ı etkilemez; $(\gamma_n,q_n,C)$ mutlakları ortak $\sqrt2$ çarpanıyla oynar. Ek C satır 8'in ekvator-hızı bütçesiyle birlikte çözülmelidir.
- **Banyo temas kesrinin ($\eta$) ilk-ilkelerden hesabı:** eşbölüşüm koşulu $\eta$'nın her fiziksel değerinde sağlanır (2c'nin 36 mertebelik marjı); yine de $\eta$'nın kendisi Zerre-çarpışma modelinden hesaplanırsa marj bir ölçüme döner.
- ~~$C=2{,}35$'in M-1'in hâl katsayısı $A$ ile ilişkisi~~ → **kimlik kuruldu** (M-35 Açık Uçlar): $C\ell_\omega/\rho_0c=2\sqrt2(\mathcal{G}m_n/c^2)/r_n=4{,}2\times10^{-39}$; $\chi$-yayılım terimi M-46'da yazıldı (kütle-itim eylemden çıkar; $C=-(\partial P/\partial\chi)_\rho$); kalan: $C$'nin değerinin mikro türetimi — yapılırsa $\mathcal{G}$ (dolayısıyla yerel ölçülen $G$ değeri) türetilmiş olur.
- $u_r$ taşınımının M-4/M-43 eşik yapısıyla tam tutarlılık hesabı; tür-ayrımlı ikinci modun ($\ell\approx51$ fm) galaksi-içi ince yapıda aranması; kalıcı bir yüzde-düzeyi oran sapması bulunursa $m_e$-etkin süredurumu / $r_n$ vekili hesabı.

---

## M-47 · F4 Penceresi — "Kafes Kilitlenmesi": Rankine İç Kolunun Galaktik Denklemdeki İfadesi · **[T-aday]**

**Kullanıldığı bölümler:** 6.5.4.4 (resmî denklem), 10.2.1, 10.9. Bağlı katalog: M-30 (Rankine yapısı), M-38 (silindirik akı penceresi), Adım 6 ($\ell_\omega$ yasası).

**Kilit tez:** Galaktik denklemin F4 terimi her yarıçapta açık değildir; M-30'un türetilmiş Rankine yapısı (içte katı-cisim, kuvvet $\propto R$; dışta $1/R$) denkleme uygulandığında **parametresiz** bir pencere çıkar.

### Varsayımlar
1. M-30'un bileşik girdap yapısı: $r<r_0$'da katı-cisim ($a\propto R$), $r>r_0$'da düz kol ($a\propto1/R$); iki kol $r_0$'da sürekli eklenir.
2. Geçiş yarıçapı özdeşleştirmesi (6.5.4.4): $r_0=\ell_\omega^{etkin}(R)=\sqrt{\mathcal{G}M_{kaps}(R)/a_0}$ — koherent kolonun kendi uzunluğu.
3. Yerel yasa (Adım 6): $M_{kaps}$ ve $\ell_\omega$ yereldir.

### Adımlar
1. Dış kolda F4 ivmesi $\sqrt{\mathcal{G}M_{kaps}a_0}/R$'dir (6.5.4.4). İç kolda kuvvet $\propto R$ olduğundan, $1/R$ biçimine göre çarpan $(R/r_0)^2$'dir; $R=r_0$'da süreklilik Rankine eklemesinin kendisidir.
2. $r_0=\ell_\omega$ konur: $(R/\ell_\omega)^2=R^2a_0/(\mathcal{G}M_{kaps})=a_0/g_{kaps}$, $g_{kaps}\equiv\mathcal{G}M_{kaps}/R^2$.

### Sonuç
$$\boxed{\;v_{F4}^2=\sqrt{\mathcal{G}M_{kaps}\,a_0}\cdot W,\qquad W=\min\!\Big(1,\;\frac{a_0}{g_{kaps}}\Big)\;}$$

İvme dilinde etkin aile parçalıdır: $\nu(y)=1+y^{-1/2}$ ($y\leq1$), $\nu(y)=1+y^{-3/2}$ ($y>1$) — yüksek ivmede türetilmiş, daha dik sönüm. **Kanal-arası okuma:** $g_{kaps}>a_0$ bölgesi kolonun *içidir*; silindirik uzak-alan yasası orada kurulmamıştır.

**Sayısal sınavlar** (141 galaksi, adil kalibrasyon): radyal ivme biçim sürüklenmesi $-0{,}043\to-0{,}002$ (rotmod) ve $+0{,}051\to+0{,}0002$ (Lelli+2017, 2693 nokta); galaksi-içi eğim $-0{,}074\to-0{,}033$; medyan RMS $12{,}76\to12{,}48$; yüksek-$z$ $f_{DM}$ açığı kapanır (5/6 bant içi); sınıf bandı ve BTFR dokunulmaz. Üs-1 kontrolü daha kötüdür — biçim veriden ayarlanmamıştır.

### Geçerlilik Sınırı
- Koherent disk taşıyıcısı olan sistemler (galaktik diskler); basınç-destekli sistemlere uzanmaz (6.5.4.9).
- Rankine eklemesi $R=\ell_\omega$'da büklümlüdür (türev süreksiz) — M-30'un kendi yapısı; yumuşak geçiş biçimi türetilmeden **eklenmeyecektir**.
- $a_0$'ın pencereli kalibrasyonu $7{,}67\times10^{-11}$ m/s² verir ($\ell_\omega$ eşleniği 38,2 fm — ölçülen 35,7 fm'e penceresizden daha yakın).

### Açık Uçlar
- Galaksi-içi artık eğimi $-0{,}033$'te durur (aday adres: dış-bölge sistematiği, 6.5.4.6).
- $r_0=\ell_\omega^{etkin}$ özdeşleştirmesinin bağımsız türetimi (bugün: tek-galaksi ölçümüyle desteklenen tespit) — [T-aday]→[T] geçişinin koşulu.
- Sdm-Sm sınıfının $+0{,}07$'lik aykırı sınıf-içi eğimi pencere sonrası yeniden ölçülmeli.

---

## M-48 · Basınç-Destekli Köprü: Küresel İzdüşüm Lemması ve $v_c=\sqrt2\,\sigma$ · **[T]**

**Kullanıldığı bölümler:** 6.5.4.9 (kapsam kaydının kapanışı), 6.5.3 (eliptik/cüce küresel), 10.10.3 md. 5. Bağlı katalog: M-37/M-38 (silindirik akı), M-47 (pencere), Adım 6–7 ($\sqrt N$/λ).

**Kilit tez:** Silindirik F4 yasası küresel sistemlerde de aynı radyal yasayı verir; Jeans denklemiyle $v_c\leftrightarrow\sigma$ köprüsü kurulur ve Faber–Jackson ($M\propto\sigma^4$) BTFR'nin kardeşi olarak türer.

### Varsayımlar
1. M-38'in ekseneselevkli kuvveti: büyüklük $\sqrt{\mathcal{G}M_{kaps}a_0}/R_{sil}$, yön $-\hat R_{sil}$; M-47 penceresi kolon içinde geçerli.
2. Dispersiyon-destekli sistemde koherent kolon, $\sqrt N$ teoreminin **rastgele-yönlü kalıntı dolanımıdır** (85; düzenli dönme gerekmez — dolanım korunumu yeter).
3. Köprü için: izotropik, durağan sistem; dış bölgede izotermal yapı ($\rho_*\propto r^{-2}$).

### Adımlar
1. **İzdüşüm lemması:** $\hat R_{sil}=\sin\theta\,\hat r+\cos\theta\,\hat\theta$ → radyal bileşen $\dfrac{\sqrt{\mathcal{G}M_{kaps}a_0}}{r\sin\theta}\sin\theta=\dfrac{\sqrt{\mathcal{G}M_{kaps}a_0}}{r}$ — **enlemden bağımsız.** $\hat\theta$-bileşeni kutupta M-47'nin Rankine koluyla sonlu kalır; rastgele-eksen ortalamasında sıfırlanır.
2. **Jeans:** $d(\rho_*\sigma^2)/dr=-\rho_*g$; derin rejimde $g=\sqrt{\mathcal{G}M_{bar}a_0}/r$ → $\sigma^2=\sqrt{\mathcal{G}M_{bar}a_0}/\alpha$; izotermal $\alpha=2$.

### Sonuç
$$\boxed{\;a_r^{küresel}=\frac{\sqrt{\mathcal{G}M_{kaps}a_0}}{r}\;(\text{diskle aynı});\qquad v_c=\sqrt2\,\sigma;\qquad \sigma^4=\frac{\mathcal{G}M_{bar}a_0}{4}\;}$$

Mertebe denetimleri (fit yok): Fornax $M_*\sim10^7$ için $v_c=17{,}8$ km/s — kitabın kendi $\sim18$ km/s kaydı (6.5.3); $L^*$ eliptik tabanı $\sigma\approx150$, gözlenen merkez 200–250 — merkez Newton rejimi tabana ekler, yön doğru. Kovanın F4'ü birinci mertebede TAM beslemesi bu lemmanın sonucudur; 96_ETG'nin dış-nokta başarısı ($-0{,}003$) verili doğrulamadır.

### Geçerlilik Sınırı
- İzotropi: anizotropi $\alpha\to\alpha-2\beta_J$ kaydırır ($O(1)$ bandı).
- **Dış-alan-baskın cüce küreseller** (MW uyduları) nicel kapsam dışıdır — EFE terimi türetilene dek (87 A5).
- Merkez ($g_{kaps}>a_0$) M-47'nin parçalı rejimindedir; kutular dış bölge içindir.

### Açık Uçlar
- ~~İlk bağımsız-aile sınavı~~ → **GEÇİLDİ** (McConnachie 2012, 28 Yerel Grup cücesi; sıfır yeniden-kalibrasyonla medyan $+0{,}009$ dex).
- ~~İkinci aile: dış-$\sigma$ katalogları (G-12)~~ → **GEÇİLDİ** (Forbes+2017 SLUGGS küresel-küme kinematiği, 22 eliptik/merceksi; medyan $+0{,}051$ dex, kovan konvansiyonuyla $-0{,}004$; 2–10 $R_{eff}$ yarıçapta düz) → **rozet [T]'ye yükseldi.** Kayıt: en kötü tekil küme-merkezlisi M87 ($-0{,}195$) — küme ortamı kapsam dışı (7.4/A7).
- Sıcak bileşenin λ'ının (kaskad tutumu) türetimi — ikinci-mertebe kovan düzeltmesi.
- EFE teriminin türetimi (cüce küresellere nicel uzanımın anahtarı).

---

## M-49 · Dış Alan Etkisi (EFE): Egemenlik Yarıçapı ve Sonlu-Kolon Uzak Alanı · **[T-aday]**

**Kullanıldığı bölümler:** 6.5.4.9 (cüce küresellerin nicel uzanımı), 87 A5 programı. Bağlı katalog: M-47 (iç pencere — ayna simetriği), M-48 (Jeans köprüsü), M-38.

**Kilit tez:** Ev sahibi alanı $g_{ext}$, alt sistemin koherent kolonunu **egemenlik yarıçapında** keser; sonlu kolonun uzak alanı $1/R\to1/r^2$'ye döndüğünden bastırma üssü geometriden çıkar.

### Varsayımlar
1. M-47 okuması: kolon, öz alanın $a_0$'a düştüğü yüzeye kadar uzanır (iç sınır).
2. $g_{kaps}<g_{ext}$ bölgesinde ortamın örgütlenmesi ev sahibine aittir; alt sistemin kolonu orada kurulamaz.
3. $g_{ext}$: ev sahibinin gözlenen toplam alanı ($V_{host}^2/D$) — ölçülebilir girdi.

### Adımlar
1. Egemenlik yarıçapı: $\mathcal{G}M_{kaps}/r_e^2=g_{ext}$ → $r_e=\sqrt{\mathcal{G}M_{kaps}/g_{ext}}$.
2. Boyu $\sim r_e$ olan kolonun silindirik $1/R$ yasası $r>r_e$'de kompakt-kaynak $1/r^2$'sine döner → göreli bastırma $r_e/r$.

### Sonuç
$$\boxed{\;W_{dış}=\min\!\Big(1,\ \sqrt{g_{kaps}/g_{ext}}\Big);\qquad
v_{F4}^2=\sqrt{\mathcal{G}M_{kaps}a_0}\cdot W_{iç}\cdot W_{dış}\;}$$

Tam-baskın limitte $g=g_{bar}(1+\sqrt{a_0/g_{ext}})$ — **yarı-Newton**, $\mathcal{G}_{etkin}=\mathcal{G}(1+\sqrt{a_0/g_{ext}})$: güçlü eşdeğerlik ilkesinin ihlali türetilmiş sonuçtur (MOND'da varsayım; bizde geometri — ve bağımlılık biçimi farklı: $\sqrt{a_0/g_{ext}}$, ayırıştırıcı sınav). Disklerde $g_{kaps}<g_{ext}$ dış bölgesinde eğri düşüşü (Chae ve ark. 2020'nin imzası). Mertebe denetimi: MW alanındaki Fornax için $\sigma=10{,}5$–14,9 km/s (gözlenen ~11–12; yalıtık değer 13,8–16,9'dan gözleme doğru çeker). SPARC'ta süptillik türer: tipik $g_{ext}\approx4\times10^{-12}$ son noktaların çoğunda $W_{dış}=1$ bırakır.

### Geçerlilik Sınırı
- Gel-git etkisi ayrıdır (M-36, klasik); M-49 yalnız F4 kanalının dış-alan tepkisidir.
- $\min$-eklemesi Rankine tarzı büklümlüdür; yumuşak geçiş türetilmeden eklenmez.
- Geniş çiftlerde $g_{iç}>g_{ext}$ olduğundan bastırma doğmaz — G-10 hükmü değişmez.

### Açık Uçlar
- Doğrudan veri sınavı ([T-aday]→[T]): Chae+2020 düşen-eğri altkümesiyle nicel kayıt-öncesi protokol. dSph ilk sınavı yapıldı (G-13): büyük uydularda **lehte işaret** ($+0{,}109\to+0{,}042$), küçük klasiklerde gelgit-karıştırıcılı aşırı-bastırma — ayrıştırma gelgit-ısınması hesabını bekler.
- $g_{ext}$'in bileşen ayrıştırması (toplam-alan okumasının türetimi).

---

## H.1 Blok Özeti: Ölçek Haritası ve Bağımlılık Zinciri

| No | Kuvvet | Köken | Akı geometrisi | Uzaklık yasası | Baskın ölçek | Statü |
|---|---|---|---|---|---|---|
| M-35 | Radyal kütle-itimi | $\omega_2$ | küresel, $4\pi r^2$ | $1/r^2$ | her ölçek; Güneş Sistemi'nde tekil hâkim | [T]/[F] |
| M-36 | Diferansiyel sıkıştırma | $\omega_2$ | **M-35'in türevi** | $\frac{\mathcal{G}M}{r^3}(+2,-1,-1)$ | yakın çiftler | **[T]** — yeni parametre yok |
| M-37 | Vorteks sürüklenmesi | $\omega_1$ | teğetsel akış | $v_\theta=\sqrt{R\lvert a_{radyal}\rvert}$ — **türetilmiş** | yörünge düzlemi | [T]/[A] |
| M-38 | Eksenel itim | $\omega_1$ | silindirik, $2\pi Rh$ | $1/R$ (yalnız $r_0<R<R_{kesim}$) | galaktik disk | [T]/[A] |
| M-39 | Yanal itim | $\omega_1$ | enlem gradyanı | $\sin2\theta$; oran $=\kappa_5\frac{\rho_0}{\rho_n}\phi^2$ **cisimden bağımsız** | gövde yüzeyi, disk oluşumu; imza $J_4$'te | [T]/[F], $\kappa_5\lesssim0{,}1$ |
| M-40 | Dönme sürüklenmesi — jiroskop spini | $\omega_1$ | dipolar (simetriden) | $\xi R^3\omega/4r^3$, $\xi=\frac{I}{MR^2}\frac{2\Phi}{c^2}$ | jiroskop ölçekleri; kompaktlıkla doyar | **[T]** — $\xi$ türetildi |
| M-41 | Dönme sürüklenmesi — yörünge düzlemi | $\omega_1$ | aynı alan, Coriolis kuvveti | $2GJ/c^2a^3$ | uydu yörüngeleri | **[T]** — yeni parametre yok |
| M-42 | *(kuvvet değil)* ölçek yapısı $\Lambda$ | $\omega_2$ potansiyeli | — (skaler ölçekleme) | $\Lambda=1-\Phi/c^2$; $c_{loc}\propto\Lambda^2$ | tüm ışık yolu gözlemleri | **[T]** — yeni parametre yok |
| M-43 | *(kuvvet değil)* artık kuplajın rejimi | — (ortam tepkisi) | altkritik bastırma | $F\propto\rho_0v^2A\,(v/v_{kav})^{3}$ | tüm sürükleme/sönüm hesapları | [T (yapı)]/**[S ($n$)]** — $\eta_E$'yi kaldırır |
| M-49 | *(kuvvet değil)* dış alan etkisi (EFE) | — | egemenlik yarıçapı + sonlu kolon | $W_{dış}=\min(1,\sqrt{g_{kaps}/g_{ext}})$; tam-baskında $\mathcal{G}_{etkin}=\mathcal{G}(1+\sqrt{a_0/g_{ext}})$ | uydu cüceler, yoğun çevre dış bölgeleri | **[T-aday]** — Chae altkümesi/dSph sınavı bekler |
| M-48 | *(kuvvet değil)* basınç-destekli köprü | — | küresel izdüşüm + Jeans | $a_r$ diskle aynı; $v_c=\sqrt2\sigma$; $\sigma^4=\mathcal{G}M_{bar}a_0/4$ | eliptik/cüce küresel dış bölgesi | **[T]** — iki bağımsız aile geçildi (dSph $+0{,}009$; SLUGGS $+0{,}051$/$-0{,}004$) |
| M-47 | *(kuvvet değil)* F4 penceresi | $\omega_1$ | Rankine iç kolu (M-30) | $W=\min(1,a_0/g_{kaps})$ — **parametresiz** | iç bölgeler ($g_{kaps}>a_0$) | **[T-aday]** — biçim türetildi, sürüklenme sıfırlandı |
| M-45 | *(kuvvet değil)* iki kolun eş-gücü | $\omega_1\!\leftrightarrow\!\omega_2$ | — (kaynak simetrisi) | $u_r/v_t=\sqrt{m_p/m_e}$ → $a_0=\mathcal{G}m_nm_e/(m_pr_n^2)$ | galaktik ivme ölçeği; $(C,q_n)$ çifti çözülür | **[T-aday]** — eş-güç ispatı açık |

M-42 bir kuvvet türetmez; diğer altısının **ölçüm çerçevesini** sabitler. Bu yüzden tablodaki her uzaklık yasası ona bağımlıdır: $\Phi$'nin cetvel ve saatle birlikte nasıl ölçeklendiği bilinmeden hiçbirinin sayısal büyüklüğü gözlemle karşılaştırılamaz.

**Rejim kuralı.** Bir ölçekte hangi kuvvetin baskın olduğunu akı geometrisi belirler. Küresel geometri $1/r^2$, silindirik geometri $1/R$ verir; oranları $\propto R$ olduğundan **geçiş yarıçapı $r_0$ bu bloğun en kritik tek parametresidir** — Güneş Sistemi'nin Kepler'de kalmasını da, galaksilerin düz dönüş eğrisini de aynı sayı belirler.

**Bağımlılık zinciri.** Beş kuvvet iki köke iner ve bağlar tek yönlüdür:

$$\underbrace{q_n,\;C}_{\text{tek serbest çift}} \Rightarrow \alpha \Rightarrow \underbrace{\text{M-35}}_{1/r^2} \Rightarrow \underbrace{\text{M-36}}_{\partial(\text{M-35})} \qquad\qquad \underbrace{a_{radyal}}_{\text{M-35}+\text{M-38}} \Rightarrow \underbrace{v_\theta(R)}_{\text{M-37}} \Rightarrow \underbrace{v_e}_{\text{M-39}}$$

M-36 tamamen M-35'e, M-37 ve M-39 radyal yasaya **bağımlıdır**. Bağımsız serbest kalemler yalnız üçtür: $(Cq_n)$, $r_0$, $\kappa_5$ — artı M-43'ün altkritik bastırma üssü $n$ (boyutsuz, tek gözlemden). $(Cq_n)$ çifti için M-45'in aday kapanışı kayıtlıdır: eş-güç türetilmiştir (izoklinik kilit + banyo eşbölüşümü, termalleşme koşulu 36 mertebe marjla kapalı) ve $\sqrt2c$ çapasıyla $q_n=1{,}62\times10^{-19}$ m³/s, $C=2{,}35$ kg·m⁻³·s⁻¹ — **[T-aday]**; bağımsız $\ell_\omega$ ölçümü ve hakem denetimi gelene dek çift Ek C'de [F] sayılmaya devam eder. M-40'ın $\xi$'si ise artık **türetilmiştir** ([T]): $\xi=(I/MR^2)\,|\delta c_{loc}/c| = (I/MR^2)(2\Phi/c^2)$, ve $|\delta c_{loc}/c|$ M-42'de ışık bükülmesinden sabitlenmiştir — yani bloğa parametre eklemez, **çıkarır.** $\eta_E$ de M-43 ile boyutlu serbest parametre olmaktan çıkmıştır.

**İki eşik, iki kanal (blokun kapanış ilkesi).** Ortamın $c$'yi aşan iki tepki kanalı ayrı eşiklere bağlıdır ve karıştırılmamalıdır:

| Kanal | Eşik | Yönettiği | Katalog |
|---|---|---|---|
| **Kavrama / patinaj** | $c=\sqrt{P/\rho}$ | dönme sürüklenme kesri $\xi$ | M-40 (+M-42) |
| **Kavitasyon / yırtılma** | $v_{kav}=\sqrt2c\sqrt{1+\Sigma/P_0}$ | öteleme artık sürüklemesi, $\tau_{ret}$ | M-43 (+M-4) |

Bu ayrım, $\xi$'yi $v_{kav}$'a bağlama girişiminin neden başarısız olduğunu açıklar (sayısal olarak ~10 kat tutmaz ve Bell sınırıyla çelişir): yanlış eşik denenmiştir. Doğru eşleme yapıldığında iki kanal da kapanır.

**Öteleme ↔ dönme ayrımı.** Sürüklenme iki eksende çok farklı davranır ve sınavları da ayrıdır:

| | Kuplaj | Gözlemsel sınav |
|---|---|---|
| **Öteleme** | tam ($\vec v_{bağıl}\approx0$, Postülat 7) | Michelson–Morley sıfır sonucu |
| **Dönme** | neredeyse tam patinaj ($\xi\approx4\times10^{-10}$) | GP-B'nin mas/yıl mertebesindeki küçük sapması |

Bu ayrım teorinin patinaj ilkesinin (2.4.2) dönme eksenine uygulanmasıdır; ek varsayım değildir. Ortam gövdeyle eş-dönseydi GP-B ölçülenin $10^{10}$ katı presesyon görürdü.

## H.2 Blok Açık Uçları (öncelik sırasıyla)

| Öncelik | İş | Kazanç |
|---|---|---|
| **1** | ~~$r_0$'ın türetimi~~ → **büyük ölçüde kapandı (M-47)**: $r_0=\ell_\omega^{etkin}$ ile pencere parametresizce yazıldı ve sınavlardan geçti; kalan, özdeşleştirmenin bağımsız türetimi | Ay sınırı ve galaktik eğri tek yapıyla kapandı; [T-aday]→[T] için bağımsız türetim |
| **1′** | $P(\Phi)$ hâl ilişkisinin $O(\Phi^2/c^4)$ terimi ⟹ $\beta$ (M-42 Açık Uçlar) | Merkür'ün 43″/yüzyıl'ını kapatır; GR'dan ayrışmanın aranacağı tek yer |
| **2** | $q_n$'nin $\omega_2$ frekansı ve nükleon deplasman hacminden hesabı | $\alpha$, dolayısıyla $\mathcal{G}$ **ve** M-36'nın tamamı türetilmiş olur |
| **3** | $\kappa_5$'in **$J_4$**'ten kalibrasyonu (Juno, Cassini, jeodezi, Güneş) — $\phi$ girdisiyle | Çok-gözlemli, tek-parametreli yanlışlama sınavı; kompozisyon eksenini ($\phi$) de sınar |
| **4** | $n$'nin retrograd popülasyondan **aşırı-belirlenmesi** (M-43) ve kuvvet-yasası ↔ üstel ayrımı | Tek gözlemden sabitlenmiş $n$'yi öngörüye çevirir; çerçeveyi yanlışlayabilir |
| **5** | M-37'nin yörünge kuplajı ile 3.4.4'ün spin kavraması $g(R)$'nin ortak katsayıya indirgenmesi | İki fenomenoloji tek parametreye iner |
| **6** | $C$ ile M-1'in $A$ katsayısı arasındaki ilişki | $(Cq_n)$ çiftini tek kaleme indirir |

## H.3 Bloğun Yanlışlanabilir Öngörüleri

| Öngörü | Ölçüm | Durum |
|---|---|---|
| Ay mesafesinde $1/R$ payı $\varepsilon<2\times10^{-5}$ | Apsidal presesyon (8,85 yıl), LLR | **Sınır aktif** — teori uymak zorunda |
| $\eta_E^{etkin}=3{,}3\times10^{-5}$ Pa·s *(evrensel sabit değil: $\propto a_b v^4/v_{kav}^3$)* | Phoebe'nin retrograd yörüngesinin 4 Gyr ayakta kalması | M-43 ile yeniden yorumlandı |
| **$\tau_{ret}\propto \rho_c a_b\,v_{bağıl}^{-4}$** | Retrograd cisim popülasyonu (farklı $v_{bağıl}$, $a_b$) | **Ayırt edici** — Stokes yazımı $\rho_c a_b^2 v^0$ der (M-43) |
| **$\Sigma/P_0\gtrsim6{,}4\times10^{8}$** ($v_m\gtrsim2{,}5\times10^4c$) | Bell hız sınırı ($>10^8$) ile uyumlu, 2,5 kat sıkı | M-43'ün $n=3$ sonucundan; bağımsız $\Sigma$ ölçümü sınayacak |
| Denge gelgiti 0,53 m (Ay) + 0,25 m (Güneş) | Açık okyanus gelgit genliği | Mertebe ✓, hassas karşılaştırma bekliyor |
| Gelgit tensörü oranı tam $(+2,-1,-1)$ | Gelgit ivmesinin yanal/eksenel ölçümü | Sapma $\nabla^2P=0$'ı çürütür |
| ~~$\tau_{ret}$, $e$ ve $i$'den bağımsız~~ → **bağımlıdır**: $\tau_{ret}\propto v_{bağıl}^{-4}$ | Farklı basıklık/eğimdeki retrograd cisimlerin sönüm süreleri | **M-43 ile ters çevrildi** — bağımlılık artık öngörüdür; iki yazımı ayıran sınav budur |
| ~~Tüm gezegenler için tek $\kappa_5$, $J_2$'den~~ → **$J_4$'ten** | Juno (Jüpiter), Cassini (Satürn), uydu jeodezisi (Dünya), Güneş | **Harmonik düzeltildi (M-39):** $J_2$ katkısı yeniden-ölçekleme olarak emilir; imza $\sin2\theta$ profilinden $J_4$'e düşer |
| **$\kappa_5\lesssim0{,}1$** | Dünya basıklığının hidrostatik uyumu (~%0,5) | $\kappa_5$'in ilk sayısal sınırı; $\tfrac12$ çalışma değeri 5 kat fazla |
| **Yanal itim gaz devlerinde güçlü, Güneş'te yok** | $\Delta_4$ karşılaştırması: Jüpiter/Satürn ≫ Güneş ≈ 0 | Kompozisyon ekseninin sınavı ($\phi$: bağlı kafes ↔ iyonize plazma) |
| **$\mathcal{R}=\phi=1-1/n^2$ — Fizeau ile aynı büyüklük** | Akan su $f=0{,}434$ ↔ gezegen $J_4$ | Çapraz-ölçek iddiası; kavrama kütleyle değil hacimle ölçeklenir |
| Minimum karadelik kütlesi 4–8 $M_\odot$ | Yıldız-kütleli karadelik dağılımının alt kenarı (~5 $M_\odot$) | Kütle boşluğu seçim etkisi değil, yapısal eşik (M-40) |
| **Sıkışma dalgası hızı tam $c$** (stiff hâl denklemi) | GW170817: kütleçekim dalgası ↔ ışık, $10^{-15}$ | **Sınandı ✓** — Ek M-44; ortam Zel'dovich tipi akışkandır |
| $P_0=\tfrac14\rho_nc^2$ kesin ($k=0$ türetildi) | SN 1987A gecikme bütçesi ile bağımsız doğrulama | Ek M-44; $k$ serbest parametre olmaktan çıktı ($6\to5$) |
| Yanal itim maksimumu 45° enlemde | Orta enlem gerilme/akış deseni | Henüz aranmadı |
| Halka kalınlığı: $f_{yanal}$ salınımı = M-27 dikey salınımı | Cassini/Voyager halka profilleri | Henüz karşılaştırılmadı |
| **Çerçeve sürüklenmesi 41,0 mas/yıl** | GP-B (Everitt ve ark., 2011) | **Sınandı: 0,52σ ✓** — artık *öngörü*: $\xi$ türetildi, GP-B girdi değil |
| **$\xi = (I/MR^2)\,\lvert\delta c_{loc}/c\rvert$** | Farklı $I/MR^2$ ve kompaktlıktaki cisimler | Serbest katsayısı yok; sapma kavrama orantısını çürütür |
| **$\Phi/c^2$: jiroskop ↔ atom saati aynı sayı** | GP-B vs GPS/Pound–Rebka | **Sınandı: 0,55σ ✓** |
| Nötron yıldızında $\xi\approx0{,}11$ | PSR B1828-11 devinimi, glitch istatistiği | Henüz aranmadı |
| **LAGEOS düğüm kayması 30,6 / 31,4 mas/yıl** | LAGEOS-1/2 lazer telemetrisi (~31 mas/yıl) | **Sınandı ✓** (M-41; aynı $\xi$, yeni parametre yok) |
| Düğüm kayması eğiklikten bağımsız | Farklı eğiklikteki uydu çiftleri | Formülde $i$ yok — yapısal öngörü |
| **Jeodetik presesyon 6.606 mas/yıl** | GP-B (±%0,28) | **Sınandı ✓** (M-42; Thomas $\tfrac12$ + ölçek payı 1) |
| **Işık bükülmesi 1,7512″** | Güneş kenarı, VLBI (1,7510″) | **Sınandı ✓** (M-42; $n_{eff}=1+2\Phi/c^2$) |
| **Shapiro gecikmesi ≈247 µs** | Viking, Dünya–Mars teğet (≈250 µs) | **Sınandı ✓** (M-42; yarım indis 124 µs verirdi) |
| PPN $\gamma=1$ | Cassini: $1+(2{,}1\pm2{,}3)\times10^{-5}$ | **Sınandı ✓** — yapı $\gamma$'yı serbest bırakmaz |
| **Yerel $c$ ölçümü tam değişmez** | Lorentz ihlali testleri ($10^{-18}$) | **Sınandı ✓** — $\ell$ ve $f$ aynı $\Lambda$ ile ölçeklenir |
| Kızıla kayma $\delta f/f=-\Phi/c^2$ *(artık öngörü)* | GPS, Pound–Rebka | **Sınandı ✓** — kalibrasyon bükülmeye taşındığından bağımsız sınav oldu |
| *Merkür günberi kayması 43″/yüzyıl* | *Radar telemetrisi* | **Türetilemiyor** — ikinci mertebe $\beta$ (7.4 md.12) |

## H.4 Ek C İçin Gerekli Güncellemeler

- **Satır 14 ($\eta_E$):** "değersiz F" → **[A], $<3{,}3\times10^{-5}$ Pa·s** (M-37).
- **P1 (profil fonksiyonu):** Serbest *fonksiyon* değil, serbest tek *sayı* $r_0$ (M-37 profil teoremi).
- **Yeni satır adayları:** $(Cq_n)$ [F], $r_0$ [F], $\kappa_5$ [F].
- **Satır 12 ($\alpha$):** [S] statüsü korunur, ancak ayrıştırması kaydedilir: $\alpha=Cq_n/4\pi m_n$ (M-35).
