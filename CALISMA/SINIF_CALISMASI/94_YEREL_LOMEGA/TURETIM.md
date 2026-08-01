# Adım 2 — $\ell_\omega(R)$ M-38'den türetilebilir mi? · Türetim denetimi

**Cevap: hayır — ama gerekçesi türetimin kendisinde ve bulunduğu yer tam olarak
belirlenmiştir.** Bu dosya 6.5.4.3'ün zincirini satır satır denetler, üç aday kurulumu
teoriye karşı sınar, ve açığın nerede olduğunu tek bir cümleye indirger.

İlgili: [`CALISMA.md`](CALISMA.md) md. 6.1 · kaynak metin
`Metin/Akademik/Kisim_6_Kanitlar/07_Galaktik_Yorungeler.md` §6.5.4.3 (satır 1178–1206)

---

## 1. Türetimin zinciri — olduğu gibi

| Adım | İçerik | Kullanılan kütle |
|---|---|---|
| **1** | Nükleon başına dolanım debisi $\gamma_n$ (m²s⁻¹), $q_n$'nin $\omega_1$ kardeşi | — |
| **2** | **Stokes:** $\Gamma(R)=\dfrac{\gamma_n}{m_n}M_{kaps}(R)$ | $M_{kaps}(R)$ |
| **3** | Silindirik akı: $Q_{sil}=\Gamma(R)h$, yoğunluk $Q_{sil}/(2\pi Rh)$ — $h$ sadeleşir | $M_{kaps}(R)$ |
| **4** | Ortam tepkisi: $a_{F4}=\dfrac{C}{\rho_n}\cdot\dfrac{\gamma_n M_{kaps}(R)}{2\pi m_n R}$ | $M_{kaps}(R)$ |
| **5** | $\mathcal{G}=Cq_n/4\pi\rho_n m_n$ ile: $a_{F4}=\dfrac{\mathcal{G}M_{kaps}(R)}{\ell_\omega R}$, $\ell_\omega\equiv\dfrac{q_n}{2\gamma_n}$ | $M_{kaps}(R)$ |

> ### Birinci tespit: türetimin hiçbir adımında $M_{bar}$ **yoktur**
>
> Zincirin beş adımının beşinde de kütle $M_{kaps}(R)$'dir. Toplam baryonik kütle
> 6.5.4.3'te **bir kez bile geçmez.** $M_{bar}$ yalnız 6.5.4.5'in *kalibre edilmiş*
> yasasıyla ($\ell_\omega=\sqrt{\mathcal{G}M_{bar}/a_0}$) içeri girer.
>
> Yani mevcut kurulum (A), türetilmiş bir ifadenin ($a_{F4}=\mathcal{G}M_{kaps}/\ell_\omega R$)
> içine, kalibre bir yasadan gelen bir başka kütleyi koyuyor. **Bu bir türetim sonucu
> değildir.**

## 2. İkinci tespit: Adım 5 $\ell_\omega$'yı **mikro sabit** yapar

$\ell_\omega = q_n/(2\gamma_n)$ — tek bir nükleonun iki debisinin oranı. İçinde ne yarıçap
var, ne kütle. Türetim, olduğu gibi okunduğunda **$\ell_\omega$ evrensel bir sabittir.**

Teori bunu zaten biliyor ve 6.5.4.3'ün kutusunda kaydediyor:

> *"$\ell_\omega$ evrensel bir sabit değildir ve teori öyle olduğunu iddia etmez… galaktik
> ölçekte ölçülen büyüklük tek nükleonun oranı değil, **ortamın o galakside kurduğu net
> dolanımın** karşılığıdır. Ölçümde 0,22 kpc ile $2\times10^4$ kpc arasında değişir."*

**Ama o "net dolanım" hiçbir yerde hesaplanmamıştır.** Beş kuvvetin katalogunda, Adım 2'nin
Stokes toplamı **birebir tutarlı** (coherent) varsayılır: $\Gamma\propto M$. Ortamın neden
bunu tam olarak kuramadığı, ve ne kadar kuramadığı, **açık bırakılmıştır.** Açık tam olarak
buradadır.

---

## 3. Üç aday kurulum — teoriye karşı

| | $\ell_\omega$ | Adım 2'ye uyar mı ($M_{kaps}$)? | Adım 5'e uyar mı (sabit)? |
|---|---|---|---|
| **A** mevcut | $\sqrt{\mathcal{G}M_{bar}/a_0}$ | ❌ $M_{bar}$ türetimde yok | ✅ galaksi başına sabit |
| **B** yerel | $\sqrt{\mathcal{G}M_{kaps}(R)/a_0}$ | ✅ | ❌ $R$ ile değişir |
| **C** örtülü | $\mathcal{G}M_{kaps}(\ell_\omega)/\ell_\omega^2=a_0$ | ✅ | ✅ galaksi başına sabit |

C, **iki koşulu da sağlayan tek kurulumdur** ve 6.5.4.3'ün "bedava sonuç 1"inden çıkar:
$\ell_\omega=r_0$, yani F1 ile F4'ün eşitlendiği yarıçap. Orada ivme $a_0$'a eşitse
$\ell_\omega$ örtülü olarak belirlenir. Bu, aday olarak en güçlüsüydü — o yüzden sınandı.

### C sınandı ve **yapısal olarak çöktü**

| | sonuç |
|---|---|
| Çözülebilen galaksi | **63/141** |
| Çözülemeyenler | 78 galakside $\mathcal{G}M_{kaps}(r)/r^2$ **hiçbir yerde** $a_0$'ı aşmıyor → kesişim yok |
| Çözülen 63'te RMS | 21,54 (A: 22,00 · B: 22,96) |

**Kesişim yoksa $\ell_\omega$ tanımsızdır ve teori o galaksi için F4 öngörüsü üretemez.**
Örneklemin %55'i düşük yüzey parlaklıklı sistemlerdir — yani teorinin en iyi çalıştığı
galaksiler. C, onları tümüyle dışarıda bırakır. Sayısal başarısı (63'te marjinal) bunu
kurtarmaz.

> **Kayıt:** C'nin ilk kodlaması yanlıştı. `np.interp` merkezde kütleyi kırpıyor ve
> $r\to0$'da sahte bir iç kök üretiyordu; ilk koşuda $\ell_\omega$ medyanı 0,09 kpc çıktı
> (doğrusu 11,8 kpc) ve RMS 92,9 oldu. Kök arama dış dala alındı, sonuç yukarıdaki.

---

## 4. Öyleyse B ne demek? — kapalı biçimi

B'nin $\ell_\omega$'sı yarıçapla değişir, yani Adım 5'i ihlal eder. Ama B'nin **eşdeğer**
bir yazılışı vardır ve o yazılışta $\ell_\omega$ hiç geçmez:

$$v_{F4}^2=\sqrt{\mathcal{G}M_{kaps}(R)\,a_0}
\quad\Longleftrightarrow\quad
\boxed{\;a_{F4}=\sqrt{a_{F1}\cdot a_0}\;}$$

**Eksenel itim, radyal itim ile kozmik deşarj ölçeğinin geometrik ortalamasıdır.**

Bu biçim yereldir, toplam kütle içermez, ve tek bir cümleyle söylenebilir. Türetilmesi
gereken şey artık "hangi kütle" değil, **bu doyum yasasıdır.**

### Ve bu, Adım 2'nin varsayımına doğrudan bağlanıyor

Adım 4'ü tersine çevirip B'nin gerektirdiği dolanımı çıkaralım:

$$\Gamma_{etkin}(R)\;\propto\;\sqrt{M_{kaps}(R)}
\qquad\text{oysa Adım 2}\qquad \Gamma(R)\;\propto\;M_{kaps}(R)$$

| | Toplanma | $\Gamma$ | Sonuç |
|---|---|---|---|
| **Adım 2 (varsayılan)** | birebir tutarlı (coherent) | $\propto N$ | $a_{F4}\propto M/R$ |
| **B'nin gerektirdiği** | **tutarsız / rastgele yürüyüş** | $\propto\sqrt{N}$ | $a_{F4}\propto\sqrt{M}/R$ |

> ### Üçüncü tespit — ve bu dosyanın asıl kazancı
>
> **B ⟺ nükleonların mikro dolanımları birebir değil, $\sqrt{N}$ ile toplanır.**
>
> Adım 2 tutarlı toplanmayı **varsayar** ve bu varsayım 6.5.4'ün kendi açık kalemleri
> arasında zaten kayıtlıdır ("F4'ün $\Gamma(R)$ türetimindeki tutarlı hizalanma varsayımı
> gerekçelendirilmemiştir"). Veri o varsayımı **reddediyor** ve yerine $\sqrt{N}$
> koyuyor — üstelik $\ell_\omega$'nın yarıçap izini $+0{,}56$'dan $-0{,}025$'e indirerek.
>
> Bu, "$a_0$'ı kalibre et" sorusunu **"ortamın dolanım tutarlılık ölçeği nedir"** sorusuna
> çeviriyor. İkincisi bir akışkan kuramının cevaplayabileceği bir sorudur; birincisi değildi.

### Tutarlılık kütlesi

$\Gamma_{etkin}=\dfrac{\gamma_n}{m_n}\sqrt{M_{kaps}\,M_{tut}}$ yazılırsa, Adım 4–5 zinciri
$B$'yi verir ve

$$M_{tut}=\frac{\pi\,\rho_n\,a_0\,q_n\,m_n}{C\,\gamma_n^{2}}
\qquad\text{eşdeğer olarak}\qquad
\ell_\omega^{mikro}=\frac{q_n}{2\gamma_n}=\sqrt{\frac{\mathcal{G}M_{tut}}{a_0}}$$

$M_{tut}$ — **tutarlılık kütlesi** — mikro dolanımların birebir toplanmayı bıraktığı
ölçektir. $M_{kaps}=M_{tut}$ olduğunda $\Gamma_{etkin}=\Gamma_{coherent}$, yani Adım 2
tam olarak geçerli.

> ### ✅ SONRAKI ADIMDA TÜRETİLDİ → [92_M_TUT](../92_M_TUT/CALISMA.md)
>
> $\Gamma_{etkin}=\gamma_n\sqrt{N}$ (saf rastgele yürüyüş) konursa **$M_{tut}=m_n$** çıkar —
> serbest parametre yok. Ölçülen $0{,}48\,m_n$; $\ell_\omega^{mikro}=35{,}7$ fm ve kütleyle
> Spearman $+0{,}029$ (3,8 decade), yani gerçekten bir **mikro sabit.**

**Bu satır bir türetim değil, bir yeniden yazımdı.** $a_0$'ı $M_{tut}$ cinsinden ifade eder;
$M_{tut}$'u türetmez. Ama hedefi değiştirir: artık aranan şey bir ivme kalibrasyonu değil,
ortamın **dolanım tutarlılık ölçeğidir** — ve o, 4.2.4'ün $\gamma_N/m=1/\rho_n$
evrenselliğiyle aynı dilde yazılmış bir büyüklüktür.

---

## 5. Sonuç — üç cümle

1. **$M_{bar}$'ın $\ell_\omega$'da olması türetimden gelmiyor.** 6.5.4.3'ün beş adımının
   beşi de $M_{kaps}(R)$ kullanır; $M_{bar}$ yalnız 6.5.4.5'in kalibre yasasından girer.
   Bu yönüyle **B, A'dan daha sadıktır.**
2. **Ama B de türetilmiş değildir:** Adım 5 $\ell_\omega$'yı mikro sabit yapar, B onu
   yarıçapa bağlar. İki koşulu birden sağlayan tek aday (C) örneklemin %55'inde
   **tanımsızdır** ve elenmiştir.
3. **Açık tek bir cümleye indi:** Adım 2'nin *tutarlı toplanma* varsayımı yanlıştır; veri
   $\sqrt{N}$ diyor. Türetilecek şey $a_0$ değil, **tutarlılık kütlesi $M_{tut}$'tur.**

## 6. Dürüstlük kayıtları

1. **Bu dosya bir türetim üretmedi.** Nerede duracağını buldu. B hâlâ ölçümle desteklenen
   bir kurulumdur, teoremle değil.
2. **$\sqrt{N}$ yorumu tek olası yorum değildir.** $\Gamma_{etkin}\propto\sqrt{M}$ başka
   mekanizmalarla da doğabilir (örneğin dolanımın bir üst sınıra doyması, ya da
   $\gamma_n$'nin ortam yoğunluğuna bağlı olması). Rastgele yürüyüş **en basit** olandır,
   kanıtlanmış olan değil.
3. **$M_{tut}$ ifadesi bir tanımdır, bir sonuç değil.** Sağ tarafındaki $\rho_n$, $q_n$,
   $\gamma_n$, $C$ nicelikleri bağımsız ölçülmedikçe $M_{tut}$ sayısal bir değer taşımaz.
4. **C'nin elenmesi sayısal başarısızlığına değil, tanımsızlığına dayanıyor.** Çözülen 63
   galakside C aslında en iyi RMS'i veriyordu (21,54). Eleme gerekçesi budur ve
   tartışmaya açıktır: kesişimi olmayan galaksiler için $\ell_\omega$'yı $M_{bar}$
   limitine (yani A'ya) düşüren melez bir kurulum denenebilirdi. **Denenmedi.**
