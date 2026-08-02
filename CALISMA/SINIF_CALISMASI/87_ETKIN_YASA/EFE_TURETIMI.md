# EFE teriminin türetimi — egemenlik yarıçapı ve sonlu-kolon uzak alanı (iş 12)

**Hedef:** dış alan etkisinin (EFE) teori içindeki nicel biçimi — A5'in mekanizmasını nicelleştirir,
cüce küresellere nicel uzanımın (M-48'in şerhi) anahtarını verir. Sonuç **M-49 [T-aday]**.

---

## 1. Türetim — M-47'nin ayna simetriği

**Okuma:** M-47'nin penceresi, koherent kolonun **iç** sınırıdır: $\ell_\omega=\sqrt{\mathcal{G}M_{kaps}/a_0}$,
yani kolon, öz alanın $a_0$'a düştüğü yüzeye kadar uzanır; içeride ($g_{kaps}>a_0$) Rankine kolu.

**Dış alan bunun aynasını koyar.** Ev sahibi sistemin alanı $g_{ext}$, alt sistemin öz alanını
aştığı bölgede ortamın örgütlenmesi ev sahibine aittir — alt sistemin koherent kolonu ancak
**egemenlik yarıçapına** kadar kurulabilir:

$$r_e=\sqrt{\frac{\mathcal{G}M_{kaps}}{g_{ext}}}\qquad(\text{öz alan}=g_{ext}\ \text{yüzeyi})$$

**Sonlu kolonun uzak alanı üssü türetir:** silindirik $1/R$ yasası sonsuz kolon içindir; boyu
$\sim r_e$ ile sınırlanan kolon, $r>r_e$'de kompakt kaynak gibi görünür ve alanı $1/r^2$'ye
döner. Göreli bastırma bu geometrik geçişin kendisidir:

$$\boxed{\;W_{dış}=\min\!\Big(1,\ \frac{r_e}{r}\Big)=\min\!\Big(1,\ \sqrt{\frac{g_{kaps}}{g_{ext}}}\Big)\;}$$

— üs (1) seçilmedi; $1/R\to1/r^2$ geçişinden çıktı. **Birleşik F4:**

$$v_{F4}^2=\sqrt{\mathcal{G}M_{kaps}\,a_0}\cdot
\underbrace{\min\!\Big(1,\frac{a_0}{g_{kaps}}\Big)}_{W_{iç}\ (\text{M-47})}\cdot
\underbrace{\min\!\Big(1,\sqrt{\frac{g_{kaps}}{g_{ext}}}\Big)}_{W_{dış}\ (\text{M-49})}$$

Tam ifade bandı: $g_{ext}<g_{kaps}<a_0$ — kolon, iki organizasyon ölçeğinin arasında yaşar.

## 2. Limitler ve türetilmiş sonuçlar

1. **Yalıtık sistem** ($g_{ext}\to0$): $W_{dış}=1$ — bütün önceki sonuçlar dokunulmadan kalır.
2. **Tam-baskın limit** ($g_{kaps}\ll g_{ext}$): $g=g_{bar}\big(1+\sqrt{a_0/g_{ext}}\big)$ —
   iç dinamik **yarı-Newton'dur**, etkin katsayı
   $\boxed{\mathcal{G}_{etkin}=\mathcal{G}\big(1+\sqrt{a_0/g_{ext}}\big)}$
   ($g_{ext}=a_0$: ×2 · $0{,}1a_0$: ×4,2). Güçlü eşdeğerlik ilkesinin ihlali burada
   **türetilmiş** bir sonuçtur: iç dinamik dış alana bağlıdır, çünkü kolonun boyu dış alana
   bağlıdır. (MOND bunu varsayımla taşır; bizde geometriden çıkar — ve bağımlılık biçimi
   farklıdır: bizde $\sqrt{a_0/g_{ext}}$, MOND'da $\nu$-ailesi. Ayrıştırıcı sınav budur.)
3. **Disk dış eğrisi düşüşü (Chae imzası):** $g_{kaps}<g_{ext}$ olan dış bölgede
   $v_{F4}^2\propto\sqrt{\mathcal{G}M a_0}\,r_e/R$ — düz kol düşüşe geçer. Chae ve ark.
   (2020)'nin istatistiksel tespiti tam bu biçimdir; A5'in yeni kayıt-öncesi protokolü artık
   **nicel** öngörüyle yazılabilir.
4. **SPARC'ta neden süptil:** tipik SPARC çevresi $e_{env}\approx0{,}033$ →
   $g_{ext}\approx4\times10^{-12}$ m/s² $=122$ (km/s)²/kpc; çoğu galaksinin son ölçüm
   noktasında $g_{kaps}$ bunun üstündedir → $W_{dış}=1$. Etki ortalamada görünmez, kuyrukta
   (en seyrek dış bölgeler, en yoğun çevreler) görünür — Chae'nin 153-galaksi istatistiği
   gerektirmesinin türetilmiş açıklaması; bizim EFE protokolünün 0,71-dex kapı dersiyle tutarlı.

## 3. Mertebe denetimi — Fornax (M-48 köprüsü + M-49 birlikte)

MW alanı ($V\approx220$, $D\approx140$ kpc): $g_{ext}=346$ (km/s)²/kpc $=1{,}1\times10^{-11}$ m/s².
Fornax $r_h=0{,}7$ kpc; Jeans ($\alpha=2$) ile $\sigma^2=r_h\,[g_{bar}+g_{F4}W_{dış}]/2$:

| $M_*$ ($M_\odot$) | $r_e$ (kpc) | $\sigma$ (yalıtık) | $\sigma$ (EFE'li) |
|---|---|---|---|
| $10^7$ | 0,35 | 13,8 | **10,5** |
| $2\times10^7$ | 0,50 | 16,9 | **14,9** |

Gözlenen $\sigma_{Fornax}\approx11$–12 km/s: EFE terimi yalıtık öngörüyü **gözleme doğru çeker**
ve $M_*\sim10^7$ bandında oturur. (Mertebe denetimidir: $M_*$, $\alpha$, anizotropi ve MW alanı
belirsizlikleri $O(1)$; fit yok.)

## 4. Yanlışlanabilir öngörüler (G-13)

1. Dış-alan-baskın sistemlerde iç dinamik yarı-Newton'dur ve tek evrensel çarpan taşır:
   $\mathcal{G}_{etkin}/\mathcal{G}=1+\sqrt{a_0/g_{ext}}$ — aynı $g_{ext}$'teki bütün sistemlerde
   aynı olmalı.
2. Disklerde eğri düşüşü tam $g_{kaps}=g_{ext}$ yarıçapında başlamalı; düşüş bölgesinde
   $v^2-V_{bar}^2\propto1/R$.
3. İzole cüce küreseller (düşük $g_{ext}$) sistematik olarak baskın-alan eşleniklerinden
   yüksek $\sigma$ taşımalı (aynı $M_*$'da).

## 5. Dürüstlük kayıtları

1. $g_{ext}$, ev sahibinin **gözlenen toplam alanıdır** ($V_{host}^2/D$) — ölçülebilir;
   teorik ayrıştırması (F1+F4 payları) gerekmez, kolon kesilmesi toplam örgütlenmeye bakar.
   Bu bir okumadır ve kayıt altındadır.
2. $\min$-eklemeleri Rankine tarzı büklümlüdür (M-47'deki gibi); yumuşak geçiş türetilmeden
   eklenmeyecektir.
3. Gel-git (tidal) etkisi ayrı ve klasiktir (M-36); M-49 yalnız **F4 kanalının** dış-alan
   tepkisidir — ikisi karıştırılmamalıdır.
4. Statü **[T-aday]**: üs geometriden türetildi ama doğrudan veri sınavı henüz yok; sınav
   adresleri — Chae+2020 düşen-eğri altkümesi (nicel biçimle yeni kayıt-öncesi protokol),
   izole↔baskın dSph karşılaştırması, geniş-çift kesinleşmesi (G-10'un $g_{ext}$'i MW alanıdır:
   $W_{dış}=\min(1,\sqrt{g_{iç}/g_{ext}})$ — 10⁴ AU'da $g_{iç}\sim1{,}6a_0>g_{ext}\approx0{,}9a_0$
   → bastırma yok; GENIS_CIFT hükmü değişmez).
5. Bu türetim Claude Fable 5 tarafından yapılmıştır; M-47'nin ayna-simetri okuması türetimin
   çekirdeğidir ve M-49 olarak kataloğa işlenmiştir.
