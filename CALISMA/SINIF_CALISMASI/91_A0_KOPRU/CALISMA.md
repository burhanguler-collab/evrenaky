# 91_A0_KOPRU — $a_0$'ın son serbestliği: **iki yol denendi** · Çalışma dosyası

Hesap: `../../a0_kopru_sinavi.py` · Görsel: [`a0_kopru.png`](a0_kopru.png)
Ön adım: [92_M_TUT](../92_M_TUT/CALISMA.md)

---

## 0. Çerçeve — bu dosyanın izni

Teorinin **matematik katmanı** (M-35, M-38, 6.5.4.x, sembol sözlüğü) yazarın kendi ifadesi
değil, önceki bir yapay zekâ türetimidir. Dolayısıyla o katmandaki bir denklem, daha iyi bir
yapıya yer açmak için **değiştirilebilir.** Bu dosya bir yerde kitabın denklemine karşı çıkar
ve gerekçesini verir.

92_M_TUT şunu bırakmıştı:

$$a_0=\frac{\mathcal{G}m_n}{\ell_\omega^{2}},\qquad \ell_\omega=\frac{q_n}{2\gamma_n}
\;\;(\text{ölçülen } 35{,}7\ \mathrm{fm})$$

Tek kalan serbestlik $q_n/\gamma_n$. İki yol denendi.

---

# YOL 1 — $q_n/\gamma_n$'yi nükleon yapısından türet

> ### ⚡ YOL 1 YENİDEN AÇILDI VE KAPANDI (1 Ağustos 2026) → [YOL1_KAPANIS.md](YOL1_KAPANIS.md) · [ESGUC_ISPAT.md](ESGUC_ISPAT.md)
>
> Aşağıda "bugün ilerletilemez" denilen ikinci denklem bulundu ve **türetildi**:
> $u_r/v_t=\sqrt{m_p/m_e}=42{,}85$ (ölçülen 42,4 — fark medyan hatası içinde) — mekanizma:
> kafes=atom (M-15/M-39) → pulsasyon kolunu $m_e$, dolanım kolunu $m_p$ taşır; **eş-güç
> türetildi** (izoklinik kilit Ek A.2'nin $\sqrt2$'sinden + banyo eşbölüşümü; termalleşme
> koşulu 36 mertebe marjla kapalı; medyan-H kilidi bileşim-kararlılığını açıklar).
> Sonuç: $a_0=\mathcal{G}m_nm_e/(m_pr_n^2)=8{,}60\times10^{-11}$ — **sıfır kalibrasyonla** beş-ölçüm
> bandının içinde; $\sqrt2c$ çapasıyla $(C,q_n)$ çifti de sayısal ($C=2{,}35$; kitapta **M-45**).
> Statü: **[T-aday]** (başka-yere-bakma: dar uzay ~2σ, geniş %40) — $a_0$ Ek C'de [S] kalır;
> kalan iki dış koşul: bağımsız $\ell_\omega$ ölçümü + hakem denetimi.

Nükleonu ortamda hem **pulse eden** hem **dönen** bir kaynak olarak yazalım:

$$q_n=4\pi r_n^2 u_r \quad(\omega_2\text{ kolu}),\qquad
\gamma_n=2\pi r_n v_t \quad(\omega_1\text{ kolu})$$

$$\Longrightarrow\quad \ell_\omega=\frac{q_n}{2\gamma_n}=r_n\cdot\frac{u_r}{v_t}$$

**Serbestlik bir uzunluk oranından bir hız oranına dönüşüyor.** Ölçülen $\ell_\omega=35{,}7$ fm
ve $r_n=0{,}841$ fm ile:

$$\boxed{\;\frac{u_r}{v_t}=42{,}4\;}$$

İki kol aynı hızda olsaydı ($u_r=v_t$) $\ell_\omega=r_n$ olurdu ve
$a_0=\mathcal{G}m_n/r_n^2=1{,}6\times10^{-7}$ m/s² çıkardı — gözlenenin **1798 katı.** Yani
bir hız oranı **kaçınılmazdır**; soru "var mı" değil, "42 nereden".

## Tıkanıklık — ve yapısal

| | |
|---|---|
| Sembol sözlüğü $q_n$ için | *"serbest (F) — $C$ ile tek kalem"* |
| Yani | $q_n$ ile $C$ **ayrılamaz**; yalnız $Cq_n$ bileşkesi $\mathcal{G}$ ile sabitlenir |
| $\gamma_n$ için bağımsız denklem | **yok** |
| Sonuç | iki bilinmeyen, bir denklem |

$u_r/v_t=42{,}4$'ü üretecek **ikinci denklem teoride yok.** Onu yazmak, nükleonun iç yapısı
için yeni bir model kurmak demektir — mevcut metnin bir okuması değil, yeni bir icat.

**Yol 1'in verdiği:** serbestliğin *yeri* netleşti (nükleonun iki kolunun hız oranı) ve
sayısal hedefi çıktı (42,4). **Vermediği:** yeni bir sınanabilir sonuç. Bugün ilerletilemez.

---

# YOL 2 — mikro/kozmik köprü

| | $a_0$ (m/s²) |
|---|---|
| mikro: $\mathcal{G}m_n/\ell_\omega^2$ (ölçülen $\ell_\omega$) | $8{,}78\times10^{-11}$ |
| ölçümün istediği ([94_YEREL_LOMEGA](../94_YEREL_LOMEGA/CALISMA.md), ×1,77) | $7{,}48\times10^{-11}$ |
| kitap: $cH_0/16{,}1$ | $4{,}22\times10^{-11}$ |
| $cH_0$ | $6{,}80\times10^{-10}$ |

$$\frac{cH_0}{a_0^{mikro}}=7{,}74
\qquad\text{(ölçümün istediğiyle } 9{,}10\text{)}\qquad
\text{kitap: }16{,}1$$

## (A) Kitabın denklemine itiraz — $\rho_n$'in üssü

Kitap şöyle yazıyor:

$$a_0=cH_0\left(\frac{\rho_0}{\rho_n}\right)^{2}=\frac{cH_0}{16}
\qquad\Longrightarrow\qquad a_0\propto\rho_n^{-2}$$

Ve kitabın **kendi açık kalemi (g)** şunu kaydediyor:

> *"Neden $(\rho_0/\rho_n)^2$, neden birinci kuvvet değil? Eşleşme post-hoc bir aramayla
> bulunmuştur… tesadüfen bir eşleşme bulma olasılığı %25 ($1{,}2\sigma$)… kitabın ilk
> yazımında ana formül olarak sunulması bir aşırı-yorumdu; **geri çekilmiştir.**"*

92_M_TUT'un türetimi aynı büyüklüğü şu hâle getiriyor:

$$a_0=\frac{C\gamma_n^{2}}{\pi\,\rho_n\,q_n}\qquad\Longrightarrow\qquad a_0\propto\rho_n^{-1}$$

> ### **Birinci kuvvet — ve türetilmiş. Kare gereksizdir.**
>
> Kitabın açıkta bıraktığı "neden kare" sorusu, soru olmaktan çıkıyor: kare hiç yoktu.
> Doğru üs birinci kuvvet ve zincirin kendisinden geliyor ($\mathcal{G}=\alpha/\rho_n$'in
> $\rho_n$'si, $\ell_\omega$'nın $\rho_n$ içermemesi).

Bu, matematik katmanına yapılan **somut bir düzeltme önerisidir** ve kitabın kendi geri
çekme kaydıyla uyumludur.

## (B) Ayırt edici — $a_0$ kozmik zamanla değişiyor mu?

| Okuma | $a_0(z)$ |
|---|---|
| kitap: $a_0\propto cH(z)$ | $H$ ile büyür |
| bizim: $a_0=\mathcal{G}m_n/\ell_\omega^2$ | üçü de mikro sabit → **değişmez** |

| $z$ | $H(z)/H_0$ | $a_0$ oranı (kitap / bizim) | $v_{düz}$ farkı |
|---|---|---|---|
| 0,5 | 1,31 | ×1,31 / ×1,00 | ×1,07 |
| 1,0 | 1,76 | ×1,76 / ×1,00 | ×1,15 |
| **2,0** | **2,97** | **×2,97 / ×1,00** | **×1,31** |
| 3,0 | 4,46 | ×4,46 / ×1,00 | ×1,45 |

**$z=2$'de iki okuma düz hızda %31 ayrışıyor** — bugünkü gözlemlerle sınanabilir bir fark.

Yüksek-$z$ disklerinin dış kolları **düşüyor** ve kinematik baryon-baskın (Genzel+2017,
Lang+2017, Übler+2018). Bu, $a_0$'ın yükseldiği okumaya karşı, **sabit kaldığı okumaya**
yakındır.

> **Uyarı:** bu bir **yön argümanıdır.** Bu çalışmada yüksek-$z$ verisi işlenmedi ve
> yüksek-$z$ disklerinin daha yoğun olması zaten (her iki okumada da) düşen eğri üretir.
> Ayrışan şey **büyüklüktür**, ve o ölçülmedi.

## (C) Bedeli — açıkça

$a_0$'ı mikro sabitlere bağlamak, teorinin **kozmoloji bağını koparır.** "$a_0\approx cH_0/16$
galaktik ölçeğin kozmolojik kaynaklı olduğunu gösterir" cümlesi düşer.

Ama bu kayıp göründüğünden küçüktür: kitap o eşleşmeyi **zaten $1{,}2\sigma$ olarak
derecelendirmiş ve ana formül statüsünden geri çekmiştir.** Yerine gelen şey daha güçlüdür —
galaktik ölçek artık **nükleonun iki kolundan** doğuyor, yani teorinin kendi motor cümlesinden
(3.8.2: *"makro girdap, nükleonların mikro dönüşlerinin toplanmasından doğar"*).

---

# Karşılaştırma

| Ölçüt | YOL 1 | YOL 2 |
|---|---|---|
| Serbestliği azaltıyor mu? | hayır — uzunluktan hıza taşıyor | hayır — ama **yerini açıklıyor** |
| Yeni sınanabilir sonuç | **yok** | **var** — $a_0(z)$ sabit mi? |
| Kitabın bir denklemini düzeltiyor mu? | hayır | **evet** — $\rho_n$ üssü: kare → birinci |
| Teoride ikinci denklem var mı? | **YOK** ($q_n \sim C$ dejenere) | gerekmiyor |
| Bugün ilerletilebilir mi? | **hayır** | **evet** |
| Bedeli | — | kozmoloji bağı düşer ($1{,}2\sigma$'lık bir bağdı) |

## Hüküm

**YOL 2 açık ara daha iyi** — ve iki somut çıktısı var:

1. **Kitabın $a_0=cH_0(\rho_0/\rho_n)^2$ denklemindeki kare kaldırılmalı.** Türetim birinci
   kuvvet veriyor ve kitabın kendi (g) maddesi kareyi zaten gerekçesiz ilan etmişti.
2. **$a_0$ sabittir, kozmik zamanla değişmez** — yanlışlanabilir bir öngörü, $z\sim2$'de
   %31 mertebesinde.

**YOL 1 kapalı** ama boş dönmedi: serbestliğin nerede olduğunu tam olarak söyledi
($u_r/v_t=42{,}4$) ve onu açmanın nükleon iç yapısı için **yeni bir model** gerektirdiğini
gösterdi. O model yazıldığında Yol 1 tekrar açılır.

---

## Dürüstlük kayıtları

1. **Bu dosya kitabın matematiğine itiraz ediyor** (Yol 2A). Gerekçesi, o katmanın yazarın
   kendi ifadesi olmaması ve kitabın kendi (g) maddesinin kareyi gerekçesiz ilan etmesidir.
   Yine de bu bir **öneridir**, uygulanmış bir değişiklik değil — kitap dosyalarına
   dokunulmadı.
2. **Yüksek-$z$ argümanı ölçüm değil.** Genzel+2017 ve devamı **okunmadı**, veri işlenmedi;
   literatürün genel yönü aktarıldı. Gerçek sınav yüksek-$z$ dönüş eğrilerini bu formülle
   koşmaktır ve **yapılmadı.**
3. **$cH_0/a_0^{mikro}=7{,}74$ ile kitabın 16,1'i arasındaki fark açıklanmadı.** Sabit okuma
   bu sayıya bir anlam yüklemez (rastlantıdır), ama "16 rastlantıysa 7,74 de rastlantıdır"
   demek gerekir — ve bu dosya bunu diyor.
4. **Yol 1'in küre+ekvator geometrisi bir seçimdir.** $q_n=4\pi r_n^2u_r$ ve
   $\gamma_n=2\pi r_n v_t$ en basit kürsel kurulumdur; başka bir geometri (halka kaynağı,
   dipol) farklı bir sayısal faktör verir. 42,4 bu geometriye bağlıdır.
5. **$r_n$ olarak proton yük yarıçapı alındı** (0,8414 fm). Teori nükleonun "ortamdaki
   etkin yarıçapı"nı tanımlamıyor; yük yarıçapı bir vekildir.
6. **Bu dosya hiçbir yeni ölçüm yapmadı.** 92_M_TUT'un $\ell_\omega=35{,}7$ fm sonucunu ve
   94_YEREL_LOMEGA'nın ×1,77'sini girdi aldı; geri kalanı cebir ve karşılaştırmadır.

## Bundan çıkan iş

| # | İş | Neden |
|---|---|---|
| **1** | **Yüksek-$z$ dönüş eğrilerini bu iki okumayla koş** | md. (B) — tek gerçek ayırt edici, ve veri var |
| 2 | Kitabın 6.5.4.5'indeki $(\rho_0/\rho_n)^2$'yi birinci kuvvete indir | md. (A) — öneri hazır, uygulanmadı |
| 3 | 6.5.4.4'teki $q_n/\gamma_n=4{,}36\times10^{20}$ m satırını düzelt | 92_M_TUT md. 5 — 34 mertebe hata |
| ~~4~~ | ~~Nükleonun ortamdaki kaynak modelini yaz~~ → [YOL1_KAPANIS.md](YOL1_KAPANIS.md) + [ESGUC_ISPAT.md](ESGUC_ISPAT.md) | ✅ **tamamlandı:** $u_r/v_t=\sqrt{m_p/m_e}$; eş-güç türetildi (izoklinik kilit + banyo eşbölüşümü, 36 mertebe marj) ve kitaba işlendi (**M-45**); kalan: bağımsız $\ell_\omega$ + hakem |
