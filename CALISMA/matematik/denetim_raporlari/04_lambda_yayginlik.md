# ÇEKİRDEK KANON DENETİMİ — Blok A / B / I · Üstel Yanıt

Denetlenen dosyalar (tam okundu):
- **[A]** `C:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik\Kisim_8_Ekler\09_Ek_M_Blok_A_Temel_Yasalar.md` (305 satır)
- **[B]** `C:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik\Kisim_8_Ekler\10_Ek_M_Blok_B_Arka_Plan_Basinci.md` (126 satır)
- **[I]** `C:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik\Kisim_8_Ekler\19_Ek_M_Blok_I_Eylem_Ilkesi.md` (368 satır)

Doğrulama betiği: `C:\Users\ASUS\AppData\Local\Temp\claude\C--Users-ASUS-Desktop-EvrenAKI-KITAP3\af8a4f91-3ca3-4d3f-8118-deaefaba8858\scratchpad\chk.py`

**GENEL HÜKÜM: Blok A/B/I ile ÇELİŞKİ YOK.** 7 maddeden 0'ı çelişki, 3'ü *lineer yazımın* daha önce görülmemiş iç tutarsızlığını ortaya çıkarıyor (üstel bunları kapatıyor), 4'ü nötr/kazanç. 5 kalem **zorunlu metin düzenlemesi** (fizik değil ifade), 3 kalem **yeni açık uç**.

---

## 0. ÖN BULGU — ÇARPIMSAL YAPI TEOREMİ (denetimin çekirdeği; 7 maddenin hepsi buna dayanıyor)

Kitap dalga kanalının eğimini **iki kez** yazıyor ve ikinci yazım birincisinden daha güçlü:

> `[A]:240` — "| **Sıkışma (dalga)** | $\chi$ sabit — adiyabatik | $(\partial P/\partial\rho)_\chi=c_0^2$ | **yerel $c_0=\sqrt{P/\rho}$** (stiff/Zel'dovich hâl denklemi) |"

Bu satır $(\partial P/\partial\rho)_\chi = P/\rho$ **yerel olarak** demektir. Bu bir kısmi diferansiyel denklemdir ve tek çözümü vardır:

$$(\partial P/\partial\rho)_\chi = P/\rho \iff \boxed{P(\rho,\chi) = \rho\,a(\chi)}$$

**Üç sonuç:**

1. **Hâl denklemi $\rho$'da birinci dereceden homojen olmak ZORUNDADIR.** Kitabın kendi satırı bunu dayatıyor.
2. **$\chi$-bağımlılığı $a(\chi)$ içinde TAMAMEN SERBESTTİR.** Dalga kanalı ve GW170817, $\chi$-bağlaşımının biçimi hakkında *hiçbir şey* söylemez — ne lineeri seçer, ne üsteli dışlar. Bu, Soru 1'in kesin cevabıdır.
3. **Buna karşılık TOPLAMSAL yazım — $P = c_0^2\rho - C\chi$ — koşulu İHLAL EDER:** o yazımda $(\partial P/\partial\rho)_\chi = c_0^2$ = arka plan sabiti olur, kuyu içinde $P/\rho$'ya eşit olmaz. Yani `[A]:240`'ın "yerel $\sqrt{P/\rho}$" ifadesi bozulur.

**Lineer↔üstel ayrımı nerede yapılıyor?** Çarpımsal aile içinde:
- Lineer: $a(\chi) = c_0^2(1 - C\chi/P_0)$ — **sonlu $\chi$'de sıfırlanır ve negatife geçer.**
- Üstel: $a(\chi) = c_0^2 e^{-C\chi/P_0}$ — $\forall\chi\ge0$ için $a>0$.

**Üstel, çarpımsal ailenin (i) her $\chi$ için pozitif kalan ve (ii) sabit *oransal* tepki hızına sahip ($a'/a=$ sbt) TEK üyesidir.** $a'/a = -C/P_0$ koşulu tam olarak "hacim modülü basıncın kendisidir" ($K=\rho c^2 = P$, M-1 oran biçiminin doğrudan sonucu) demektir. Türetim tektir, keyfî değil.

---

## SORU 1 — M-44'ün iki değişkenli yapısı, dalga kanalı, GW170817

**CEVAP: Dalga kanalı BOZULMUYOR. GW170817 hâlâ otomatik — ve üstelde LİNEERDEN DAHA GÜÇLÜ biçimde otomatik.**

**Kanıt (yapısal):** Üstel yanıt $P = \rho\,c_0^2e^{-C\chi/P_0}$ biçimindedir; $\chi$ sabitken $P$, $\rho$'da doğrusaldır ⟹
$$\left(\frac{\partial P}{\partial\rho}\right)_\chi = c_0^2e^{-C\chi/P_0} = \frac{P}{\rho} \equiv c_{loc}^2 \quad\text{(her noktada, TAM)}$$
Işığın yerel hızı da $c_{loc}=\sqrt{P/\rho_0}$'dır (M-1). İkisi **özdeş nicelik**; fark sıfır, ayar yok, parametre yok.

**KANIT (birebir alıntı):**
> `[A]:246` — "**Ve GW170817 böylece yapısal olarak geçilir:** ışık da sıkışma dalgası da **aynı yerel** $\sqrt{P/\rho}$ ile gider — ölçülen eşitlik açıklanacak bir tesadüf değil, aynı niceliğin iki kez okunmasıdır. Ayar yok, yeni parametre yok."

Üstel bu cümleyi **birebir korur**. Ayrıca kritik nokta: kitap stiff bağıntıyı yalnız arka planda denetlemiş:
> `[A]:244` — "Denetim: $P_0=\tfrac14\rho_nc^2$ ve $\rho_0=\rho_n/4$ ⟹ $P_0/\rho_0=c_0^2$ **tam** — stiff bağıntı **arka planda** birebir sağlanıyor."

Üstel, bu denetimi arka plandan **kuyunun her noktasına** taşır (betik: `P0/rho0/c0^2 = 1.000000000000`).

**Ek bulgu — GW170817'nin ölçüldüğü yer güçlü alandır.** Kaynak bir nötron yıldızı birleşmesidir; toplamsal lineer yazımda kaynak civarında $|c_{dalga}-c_{ışık}|/c \simeq 2\Phi/c_0^2$ ayrışması doğardı (yapısal, gözlemsel olarak yol boyunca küçük olsa da "aynı niceliğin iki kez okunması" argümanını kırar). Üstelde ayrışma **kimliksel sıfırdır**.

**ÇELİŞKİ VAR MI: HAYIR.** Aksine: `[A]:240`+`[A]:246` üstel/çarpımsal yapıyı **talep ediyor**, toplamsal yazımı dışlıyor.

**Zorunlu ifade düzenlemesi:** `[I]:40`'ın kutulu sonucu — "$P=c_0^2\rho \Rightarrow (\partial P/\partial\rho)_\chi=c_0^2 \Rightarrow \boxed{v_{ses}=c_0\ \text{tam olarak}}$" — buradaki $c_0$'ın **yerel** olduğu açıkça yazılmalı ($v_{ses}=c_{loc}$ tam olarak). Kitap zaten `[A]:240`'da bunu yapıyor; `[I]:40` Postülat 4'e göre eksik yazımdır (üstel öneri olmadan da eksikti).

---

## SORU 2 — $k=0$ taahhüdü ve Yön Kuralı

**CEVAP: $k=0$ AYNEN KORUNUYOR. Üstel, $k$'ya hiç dokunmuyor — üs $\chi$'de, $\rho$'da değil. Yön Kuralı ise GÜÇLENİYOR.**

$k$ yalnız deplasman kanalının parametresidir ve tanımı $\delta\rho/\rho_0 = k\,\delta P/P_0$'dır. Üstel yanıt, $\delta P$'nin $\chi$'ye bağımlılığının *biçimini* değiştirir; $\delta\rho=0$ ifadesine değmez.

**KANIT:**
> `[I]:204` — "**Hâl denkleminin doğrusallaştırılması** (M-44'ün iki kanalı): $\delta P=\left(\frac{\partial P}{\partial\rho}\right)_\chi\delta\rho+\left(\frac{\partial P}{\partial\chi}\right)_\rho\delta\chi$; deplasman kanalında $\delta\rho=0$ ($k=0$, M-44)"
> `[I]:53` — "$\frac{\delta\rho}{\rho_0}=0 \Longrightarrow \boxed{k=0}$"
> `[A]:241` — "| **Deplasman** | madde ortamı dışlar | $dP/d\rho=c_0^2/k$, $k=0$ | **hız değil** — statik tepki; yoğunluk basınca eşlik etmez |"

**$c^2 = P/\rho_0$ nasıl davranıyor?** $\rho=\rho_0$ sabit, $P=P_0e^{-4\Phi/c_0^2}$ ⟹ $c_{loc}=c_0e^{-2\Phi/c_0^2}$. Hiçbir sonlu $r$'de sıfırlanmaz, hiçbir yerde negatif/hayali olmaz.

**Yön Kuralı ile uyum — KATSAYI TAM $\tfrac12$ KALIYOR:**
> `[I]:59-61` — "$\frac{\delta c}{c}=\frac{1}{2}\left(\frac{\delta P}{P_0}-\frac{\delta\rho}{\rho_0}\right)=\frac{1}{2}\,\frac{\delta P}{P_0}$ … Kütleye yaklaşırken $\delta P<0$ olduğundan $\delta c<0$: ışık zorunlu olarak yavaşlar ✓, ve katsayı olabilecek **en büyük** değerdedir ($\tfrac12$)."

Üstelin tam biçimi: $d\ln c = \tfrac12 d\ln P$ — bu, $c^2=P/\rho_0$'ın $\rho$ sabitken logaritmik türevidir ve **her genlikte** geçerlidir. Lineer yazımda $\tfrac12$ katsayısı yalnız $\delta P\ll P_0$ iken geçerliydi; üstelde **tüm genliklerde tam.** $\delta c<0$ monotondur, sıfır geçişi yoktur.

**ÇELİŞKİ VAR MI: HAYIR.** Kazanç: Yön Kuralı'nın "en büyük katsayı $\tfrac12$" hükmü doğrusallaştırılmış bir ifadeden **tam bir özdeşliğe** yükseliyor.

**Ek kayıt (Soru 3 ile bağlı):** $k=0$ sadece korunmuyor — Soru 3'te görüleceği gibi **Poisson denklemini koruyan şeyin kendisi $k=0$'dır.**

---

## SORU 3 — M-46'nın $\chi$ Poisson denklemi ve varyasyonel tutarlılık

**CEVAP: $\nabla^2\chi=-q_nn_m$ DEĞİŞMİYOR — ama bu OTOMATİK DEĞİL, bir koşulun sonucu; ve o koşulu üstel/çarpımsal yazım sağlıyor, TOPLAMSAL lineer yazım İHLAL EDİYOR.**

**Eylemde nasıl yazılır (açık formül):** Kitap $u(\rho,\chi)$'nin $\chi$-bağımlılığını hiç yazmamış —
> `[I]:67` — "**6. Akışkan eylemi.** Stiff hâl denklemiyle ($u(\rho)=\tfrac12 c_0^2\rho$ mertebesinde, **sabit $\chi$'de**) eylem:"
> `[I]:298` — "$U(\rho)=c_0^2\,\rho\,\ln\frac{\rho}{\rho_0} \Longrightarrow P=\rho\,U'-U=c_0^2\rho\ \checkmark$"

M-50'nin $U$'sunun asgari $\chi$-genişletmesi:
$$\boxed{\;U(\rho,\chi) = c_0^2\,e^{-C\chi/P_0}\;\rho\,\ln\frac{\rho}{\rho_0}\;}$$

Denetim (sympy, betikte): $\rho U_\rho - U = c_0^2\rho\,e^{-C\chi/P_0}$ ✓ (istenen $P$), ve $\chi=0$'da M-50'nin $U$'suna birebir iner ✓.

**Varyasyonel tutarlılık — kritik hesap.** Durağan $\chi$ varyasyonu tüm eylemden:
$$\rho_\chi\big(\nabla^2\chi + q_nn_m\big) - \frac{\partial U}{\partial\chi} = 0 \;\Longrightarrow\; \nabla^2\chi = -q_nn_m + \frac{1}{\rho_\chi}\frac{\partial U}{\partial\chi}$$
Yukarıdaki $U$ ile: $\partial U/\partial\chi = -\frac{C}{P_0}\,P\,\ln(\rho/\rho_0)$. Deplasman kanalında $\rho=\rho_0$ ⟹ $\ln(\rho/\rho_0)=0$ ⟹ **geri-tepki KİMLİKSEL SIFIR** (sympy: `dU/dchi at rho=rho0: 0`).

$$\Longrightarrow \nabla^2\chi = -q_nn_m \quad\text{TAM OLARAK KORUNUR}$$

**Yani M-46'nın Poisson denklemini koruyan mekanizma, $k=0$'ın kendisidir.** İki taahhüt birbirini kilitliyor.

**Buna karşılık TOPLAMSAL lineer yazım varyasyonel olarak BOZUKTUR.** $U = c_0^2\rho\ln(\rho/\rho_0) + C\chi$ da $P=c_0^2\rho-C\chi$ verir ✓, ama $\partial U/\partial\chi = C$ = **sıfırlanmayan sabit** ⟹
$$\nabla^2\chi = -q_nn_m + C/\rho_\chi \;\Longrightarrow\; \chi_{fazla}=\tfrac{C}{6\rho_\chi}r^2 \;\Longrightarrow\; \vec a_{fazla}\propto +r\,\hat r$$
Bu, M-46'nın **kendi dokuz-yol tablosunda ölü ilan edilmiş** başarısızlık kipidir:
> `[I]:249` — "| $-\rho\,(v_{arka}\!\cdot\!\nabla\chi)$ (çapraz) | **ışınsal $\propto r$ ister = genleşme**; $\mathcal G\propto H$ | LLR $10^{3}$ |"

Yani: toplamsal lineer bağlaşım, eylem düzeyinde yazıldığında LLR'nin $10^3$ marjla dışladığı bir terim üretir. Çarpımsal yazım (lineer *ve* üstel) üretmez.

**Bir gauge serbestliği açıkça kayda geçmeli:** $U \to U + b(\chi)\rho$ eklemek $P$'yi değiştirmez ama $\partial U/\partial\chi|_{\rho_0} = b'\rho_0$ verir. Poisson'un tamlığı **$b'(\chi)=0$ koşuluna eşdeğerdir**; yani $\chi$-bağımlılığının *yalnız stiff katsayı $a(\chi)$ üzerinden* girmesi. Bu bir varsayım değil, M-46'nın kendi sonucunun gerektirdiği bir kısıttır — ama **yazılmalıdır.**

**Yalnız $P(\chi)$ bağlaşımı mı değişiyor? EVET.** $\chi$-sektörü aynen kalıyor:
> `[I]:202` — "$\Delta S=\int dt\,d^3x\left[\frac{1}{2v_m^2}(\partial_t\chi)^2-\frac{1}{2}(\nabla\chi)^2+\chi\,q_n\,n_m\right]$"
> `[I]:208` — "**Statik alan denklemi** ($\delta\Delta S/\delta\chi=0$, durağan): $\nabla^2\chi=-q_n n_m$ — Poisson."

Bu üç terimde $P$ hiç geçmiyor; $\chi(r)=Nq_n/4\pi r$ ve $\mathcal G$'nin $1/r^2$'si aynen çıkıyor.

**M-44 Sonuç 2 (korunumluluk ölçütü) da yapısal olarak AYNEN korunuyor.** Çarpımsal $P=\rho a(\chi)$ ile:
$$\nabla\times\left(-\frac{\nabla P}{\rho}\right)=\frac{a'(\chi)}{\rho}\nabla\rho\times\nabla\chi = \frac{1}{\rho^2}\left(\frac{\partial P}{\partial\chi}\right)_{\!\rho}\nabla\rho\times\nabla\chi$$
— `[I]:113-115`'in kutulu formülünün **birebir aynısı**; yalnız katsayı $-C \to -(C/P_0)P$ olur. Tablonun 4 satırı (`[I]:124-127`) ve `[I]:134`'ün sağlamlık notu **hiç etkilenmez** (ölçüt $\nabla\rho\times\nabla\chi$; katsayının değeri değil işareti/sıfırlığı belirleyicidir).

**ÇELİŞKİ VAR MI: HAYIR — ama önerinin lehine bir KEŞİF var:** M-46'nın lineer bağlaşımı, eylemde toplamsal yazılırsa kendi tablosundaki LLR-dışlanmış terimi üretir. Üstel (çarpımsal) yazım varyasyonel olarak temiz olan tek tamamlamadır.

---

## SORU 4 — M-9 (ağırlıksızlık) ve Jeans kararlılığı: $(\partial P/\partial\rho)_\chi>0$

**CEVAP: KORUNUYOR — ve burada LİNEER YAZIM AÇIKÇA BAŞARISIZ.**

Üstel: $(\partial P/\partial\rho)_\chi = c_0^2e^{-4\Phi/c_0^2} > 0$, **her $r$'de, her derinlikte.** $r\to0$'da sıfıra yaklaşır ama asla ulaşmaz/geçmez.

Lineer (çarpımsal okumada): $(\partial P/\partial\rho)_\chi = c_0^2(1-4\mu/r)$ ⟹ **$r<4\mu$ için NEGATİF** ⟹ hayali ses hızı ⟹ dinamik kararsızlık. Bu, M-9'un boyun eğdiği koşulun doğrudan ihlalidir:

**KANIT:**
> `[B]:102-103` — "$\left(\frac{\partial P}{\partial\rho}\right)_{\chi} = c_0^2 \;>\; 0 \Longrightarrow c_{pürüz}=c_0$ … **Sıkıştırılabilirlik her koşulda pozitif olduğundan kararsızlık penceresi hiçbir rejimde açılmaz;** homojen durum yalnızca izinli değil, ortamın **tek doğal taban durumudur.**"
> `[B]:119` — "…$(\partial P/\partial\rho)_\chi = c_0^2$ türetimi (Ek M-44) $k$'dan bağımsız olduğu için **$k$'nın izinli tüm aralığında ve her sıkışma genliğinde** geçerlidir"
> `[B]:120` — "Kanıtlanan şey, **çöküşe karşı kararlılıktır** (Jeans tipi geri-besleme yok, $dP/d\rho>0$)."

`[B]:103`'ün "hiçbir rejimde" ve `[B]:119`'un "her sıkışma genliğinde" ifadeleri **yalnız üstelde doğrudur.** Lineer yazımda $r<4\mu$ bir kararsızlık penceresidir.

**Ağırlıksızlık teoremi ($\nabla P_0=0$):** arka planda $\chi=0$ ⟹ $P=P_0$, $\rho=\rho_0$ — üstel arka plana **hiç dokunmaz.** `[B]:113`'ün kutulu sonucu aynen geçerli.

**M-9 3. adımı (kendiliğinden madde doğumu yok) — üstelde GÜÇLENİYOR.** Yerel kavitasyon eşiği $v_{kav}^2 = 2(P+\Sigma)/\rho_0$; $P\to0$ iken $v_{kav}\to\sqrt{2\Sigma/\rho_0} = \sqrt2\,v_m > 1{,}4\times10^4c_0$ — **taban değeri M-6 merdiveninin son basamağıdır ve derinlikten bağımsızdır.** Lineerde ise $P<-\Sigma$ olduğunda $v_{kav}$ hayali olur (ortam zaten yırtılmıştır).

**Merdiven sıralaması (M-6) denetimi:** $c_{loc}<\sqrt2c_{loc}<v_m<v_{kav}$; $\Sigma,\rho_0$ sabitse $v_m$ sabit, $c_{loc}$ derinlikle düşer ⟹ **basamak aralıkları AÇILIR, sıralama hiçbir derinlikte bozulmaz.** `[A]:301` ("Basamak aralıkları çok geniştir, dolayısıyla sıralama teoremi tanım ayrıntılarına duyarsızdır") aynen geçerli.

**YENİ VE BAĞIMSIZ BULGU — SİKLOSTROFİK DENGE (M-9 Geçerlilik Sınırı).** Kitap kütle çevresindeki ortamın davranışını şöyle yazıyor:
> `[B]:116-118` — "gradyan, dolaşımın merkezcil ivmesiyle siklostrofik dengede taşınır, $$\frac{\nabla P}{\rho_0} = \frac{v_\theta^2}{r}$$ … **Madde düşer, ortam dolaşır.**"

Bu denklemi iki profille çözdüm ($u\equiv4\mu/r$; betikte doğrulandı):

| $u=4\mu/r$ | ÜSTEL $v_\theta/c_0$ | ÜSTEL $c_{loc}/c_0$ | ÜSTEL Mach | LİNEER $v_\theta/c_0$ | LİNEER $c_{loc}/c_0$ |
|---|---|---|---|---|---|
| 0,25 | 0,4412 | 0,8825 | 0,500 | 0,5000 | 0,8660 |
| 0,50 | 0,5507 | 0,7788 | 0,707 | 0,7071 | 0,7071 |
| **1,00** ($r=4\mu$) | **0,6065** | **0,6065** | **1,000** | **1,0000** | **0 (P=0!)** |
| 2,00 | 0,5203 | 0,3679 | 1,414 | 1,4142 | hayali |
| 10,0 | 0,0213 | 0,0067 | 3,162 | 3,1623 | hayali |

- **ÜSTEL:** $v_\theta^2 = c_0^2\,u\,e^{-u}$ ⟹ **üstten sınırlı**: $v_{\theta,max}=c_0/\sqrt e = 0{,}6065\,c_0$ ($r=4\mu$'de). Ortamın dolaşımı hiçbir derinlikte $c_0$'ı, $\sqrt2c_0$'ı (M-3′ e-katlanma) veya $v_{kav}$'ı **geçmez** ⟹ M-9 3. adımı her derinlikte sağlanır. Yerel Mach $=\sqrt{4\mu/r}$ — yavaş büyür, sonlu $r$'de ışımaz.
- **LİNEER:** $v_\theta = c_0\sqrt u \to \infty$; $u=1$'de ($r=4\mu$) ortam **tam olarak $P=0$ noktasında $v_\theta=c_0$** ile dönmek zorunda — vakum ile sonik noktanın çakışması. $u\gtrsim10^8$'de $v_\theta \to v_m$ ⟹ **ortam kendiliğinden kavitasyona girer ve madde üretir** ⟹ M-9 3. adımının ihlali.

**ÇELİŞKİ VAR MI: HAYIR.** Üstel M-9'un üç adımını da (ağırlıksızlık, Jeans, doğurgan-değillik) her derinlikte korur. Lineer yazım M-9'un 2. ve 3. adımını $r\lesssim4\mu$'de ihlal eder. Bu, ana oturumun Merkür sonucundan **bağımsız, ikinci bir eleme.**

---

## SORU 5 — M-7 yırtılmama koşulu ve M-4 kohezyonu: kazanç mı, yeni sorun mu?

**CEVAP: NET KAZANÇ — ve kitabın M-3′/M-4'te ZATEN VERDİĞİ hükmün $\chi$-kanalına taşınmasıdır. Tek maliyet: M-7'nin *mantıksal rolü* değişiyor (sayısal sonucu değişmiyor).**

**Lineer profil gerçek bir yırtılma yüzeyi üretir.** $P=P_0(1-4\mu/r) = 0$ at $r_c=4\mu$; kohezyonla genel koşul $P+\Sigma>0$ ⟹ $r_c^{koh}=4\mu/(1+\Sigma/P_0)\approx4\mu\times10^{-8}$ — **hâlâ sonlu**, sadece $10^8$ kat küçük. Yani lineer profil, hem M-7'yi hem M-4'ü sonlu bir yarıçapta ihlal eder.

**Üstel profil $P$'yi hiçbir yerde sıfırlamaz** ($e^{-4\mu/r}>0\;\forall r>0$) ⟹ yırtılma yüzeyi **kimliksel olarak yoktur.**

**KANIT — bu argüman kitabın kendisidir, birebir:**
> `[A]:218` (M-4 Geçerlilik Sınırı) — "düzgün sıkıştırılabilir akışta $P(v)=P_0\,e^{-v^2/2c^2}>0$ olduğundan **$-\Sigma$ eşiğine akım çizgisi boyunca hiç erişilemez.**"
> `[A]:117` (M-3 Geçerlilik Sınırı) — "**Vakum cebi hiçbir sonlu hızda oluşmaz.** $P\to0$ için $\rho\to0$, o da $v\to\infty$ gerektirir. **Stiff bir akışkanda düzgün seyrelmeyle vakum cebi açılamaz.**"
> `[A]:139` (M-3′ Sonuç 1) — "Yoğunluk merkeze doğru **üstel olarak** azalır ve **hiçbir sonlu yarıçapta sıfırlanmaz.** 'Cep duvarı' diye keskin bir yüzey yoktur."

Kitap $\rho$-kanalında **tam olarak bu hükmü** vermiş: stiff ortamda düzgün bir süreç $P$'yi sonlu parametrede sıfıra indiremez, çünkü stiff yapı üsteldir. Üstel öneri, aynı hükmü $\chi$-kanalına uygular. Lineer profilin $r_c=4\mu$'deki $P=0$ yüzeyi, `[A]:117`'nin "olamaz" dediği nesnenin ta kendisidir — **yani lineer profil M-3/M-3′ ile çelişiyordu, üstel çelişkiyi kaldırıyor.**

**M-3′ Sonuç 5 ile birebir yapısal koşutluk:**
> `[A]:182` — "~%18, bir düzeltme bütçesi de, rejim ihlalinin işareti de değil — **keskin duvar varsayımının yarattığı yapay bir problemdi ve varsayım kaldırılınca ortadan kalktı.**"

Aynı hamle: $r_c=4\mu$'deki "yırtılma yüzeyi", **lineer bağlaşım varsayımının yarattığı yapay bir problemdi**; varsayım kaldırılınca (ve buna paralel olarak ufuk/tekillik de) ortadan kalkıyor.

**MALİYET — M-7'nin statüsü (dürüstçe kaydedilmeli).**
> `[B]:24` — "**Yırtılmama koşulu.** Merkezde mutlak basınç $P_0 - \Delta P$'dir; kohezyonsuz akışkanın yırtılmaması için $P_0 > \Delta P$ gerekir."

Üstelde merkez basıncı $P_0-\Delta P$ değil $P_0e^{-4\Phi/c_0^2}$'dir ve $P_0>\Delta P$ eşitsizliği **hiçbir $\Phi$ için ihlal edilemez.** Dolayısıyla M-7'nin "yırtılmama koşulu $P_0$'a alttan sınır koyar" iddiası mantıksal gücünü yitirir.

**Ama sayısal olarak hiçbir şey kırılmıyor:**
- $\Delta P_{üstel} = P_0(1-e^{-4\Phi/c_0^2})$, ve $4\Phi/c_0^2 = 2{,}784\times10^{-9}$ (Dünya yüzeyi) ⟹ lineerden **bağıl sapma $3{,}9\times10^{-18}$** (betikte doğrulandı). M-7'nin $\Delta P\approx0{,}83\times10^{25}$ Pa hesabı, iç gradyan profili (`[B]:21`), $\rho_n g$ yüzey gradyanı (`[B]:18`) — hepsi **birebir aynı.**
- M-7'nin sonucu ($P_0\ge1{,}6\times10^{25}$ Pa) M-8'in değerinin 8-9 mertebe altında olduğu için hiçbir gözlem M-7'ye bağlı değil (`[B]:73`).

**Öneri:** M-7'nin Geçerlilik Sınırı'na bir satır: *"Koşul, $\chi$-bağlaşımının doğrusallaştırılmış okumasında bir alt sınırdır. Tam (üstel) bağlaşımda $P>0$ özdeşliktir ve koşul ihlal edilemez; M-7'nin sayıları $\Delta P/P_0\sim10^{-9}$ genliğinde $10^{-18}$ doğrulukla geçerli bir muhasebe olarak kalır, ama $P_0$'ı büyük olmaya *zorlayan* argüman artık M-8'dir."* Ayrıca `[B]:39`'un açık ucu (iki kat emniyet payının gerekçelendirilmesi) **hükümsüz kalır** — envanterden düşer.

**M-4/$\Sigma$ ile ilişki:** $\Sigma$ ve $v_{kav}$, M-3′'ün zaten kaydettiği role çekilir:
> `[A]:169` — "$\Sigma$ ve $v_{kav}$ başka işler için (kohezyon kanalı $v_m$, M-7'nin yırtılmama koşulu) anlamlı kalır, ama **nükleon çekirdeğini açmak için gerekmezler.**"

Üstelde bu cümlenin ikinci yarısı da genişler: $\Sigma$ artık *kütle kuyusunu* kurtarmak için de gerekmez. Kohezyon, kuyuda bir emniyet payı olmaktan çıkıp yalnız $v_m$ kanalının ve keskin gradyan katmanlarının (M-50 §5) niceliği olur — **daha temiz bir iş bölümü.**

**ÇELİŞKİ VAR MI: HAYIR. KAZANÇ.** Tek gerçek maliyet M-7'nin bir alt sınır *türetimi* olma statüsüdür; sayısal içeriği ve tüm ara adımları $10^{-18}$ doğrulukla korunuyor.

---

## SORU 6 — M-1'in oran biçimi ↔ diferansiyel biçim ($k$ ile $1/k$) ayrımı

**CEVAP: Ayrım ETKİLENMİYOR. Üstel, ayrımın *hangi kanala ait olduğunu* netleştiriyor ve oran biçiminin "resmî" ilan edilmesini eylem düzeyinde haklı çıkarıyor.**

**KANIT:**
> `[A]:30-33` — "**Oran biçimi ($c_0^2 = P/\rho$) resmî biçimdir** ve kitap boyunca kullanılır. Diferansiyel biçim yalnızca kararlılık argümanlarında (M-9) geçer ve **oran biçiminden türetilir, ona eşit değildir.** … $\frac{dP}{d\rho} = \frac{1}{k}\cdot\frac{P}{\rho} = \frac{c^2}{k}$ … **İki biçim yalnız $k=1$'de özdeştir** ($P\propto\rho$); $k<1$ olduğu sürece diferansiyel biçim daima **$1/k$ kat büyüktür.** Bu ayrışma genliğe değil yalnız $k$'ya bağlıdır"

M-1'in $1/k$'lı diferansiyel biçimi **deplasman yolunun** eğimidir ($\delta\rho/\rho_0=k\,\delta P/P_0$'ın integrali), dalga yolunun değil. Kitap bunu kendi tablosunda iki kez teyit ediyor:
> `[A]:236` — "Karıştırma, sıkışma kanalına $\sqrt{dP/d\rho}=c_0/\sqrt k$ hızı atfetmek biçiminde ortaya çıkar ve $k=0$ ile sonsuz hız verir; **bu okuma geçersizdir.**"
> `[A]:244` — "⟹ $c_0/\sqrt k$ **bir dalga hızı değil, deplasman yolunun eğimidir**"

**Üstelin bu ayrıma etkisi:** Üstel, yalnız $a(\chi)$'yi — yani deplasman yolunun *profilini* — değiştirir. $k$ tanımına, $k=0$ değerine, $dP/d\rho=c_0^2/k$ etiketine ve o etiketin "hız değil" hükmüne dokunmaz. **Etkisi sıfırdır.**

**Ama bir *lehte* sonucu var.** `[A]:30`'un "oran biçimi resmîdir" hükmü, dalga kanalında oran ve diferansiyel biçimin **çakışmasını** gerektirir (yani dalga yolu boyunca etkin $k=1$: $P\propto\rho$). Bu, Bulgu 0'daki çarpımsal yapıdır ($P=\rho a(\chi)$) ve `[A]:240`'ın "yerel $\sqrt{P/\rho}$" satırıyla aynı şeydir.

- **Çarpımsal (lineer veya üstel):** oran biçimi ile dalga eğimi kuyunun **her noktasında** özdeş ⟹ `[A]:30` güçlü alanda da geçerli.
- **Toplamsal ($P=c_0^2\rho-C\chi$):** kuyu içinde oran biçimi $c_0^2(1-4\mu/r)$, diferansiyel biçim $c_0^2$ ⟹ **ikisi ayrışır**, `[A]:30`'un "resmî biçim" hükmü kuyuda kırılır.

**ÇELİŞKİ VAR MI: HAYIR.** Üstel, M-1'in $k\!\leftrightarrow\!1/k$ ayrımını aynen bırakır; ek olarak "oran biçimi resmîdir" hükmünü doğrusallaştırılmış bir seçim olmaktan çıkarıp çarpımsal hâl denkleminin bir teoremi hâline getirir.

---

## SORU 7 — "Hacim modülü = $P$" argümanının kitaptaki KARŞILIĞI (öneri teoriye yabancı mı?)

**CEVAP: YABANCI DEĞİL. Argümanın hem MANTIĞI hem MATEMATİĞİ hem SAYISI kitapta zaten yazılı — üç bağımsız yerde. Üstel öneri yeni bir varsayım getirmiyor; kitabın $\rho$-kanalında yaptığı hamleyi $\chi$-kanalında tekrarlıyor.**

### Dayanak 1 — $K=P$ doğrudan M-1'in resmî biçiminden çıkar
> `[A]:30` — "**Oran biçimi ($c_0^2 = P/\rho$) resmî biçimdir**"

$K \equiv \rho\,c^2 = \rho\cdot(P/\rho) = P$. Yani "hacim modülü basıncın kendisidir" bir yeni postülat değil, **M-1'in resmî biçiminin cebirsel yeniden yazımıdır.** Sabit *mutlak* tepki oranı ($dP/d\chi=-C$) ise modülün dışsal ve sabit bir sayı ($P_0$) olduğunu varsayar — bu, M-1'in yerelliğini ve **Postülat 4'ü** ihlal eder. Sabit *oransal* tepki ($dP/d\chi = -CP/P_0$) modülü yerel yapar; integrali üsteldir. Türetim gerekçesi budur ve tamamen kitap-içidir.

### Dayanak 2 — Kitap $\chi$-bağlaşımının şiddetini ZATEN $\rho_0c^2$ (yani $P$) olarak hesaplamış
> `[I]:259` — "Dışlanan-hacim modeli ($P=P(\rho/(1-f))$, $f=n_mV_{cep}$) bu ailenin en güçlüsüdür ve **$(\partial P/\partial f)_\rho=\rho_0c^2=6{,}07\times10^{33}$ Pa** gibi doğru mertebede bir sayı verir"

Bu, önerinin **tam kalbidir.** $\rho_0c^2$ *yerel olarak* $P$'nin kendisidir (çünkü $\rho=\rho_0$ sabit ve $c^2=P/\rho_0$). Kitap bu türevi arka planda değerlendirdiği için $\rho_0c_0^2=P_0$ görünüyor; **yerel okunduğunda $(\partial P/\partial f)_\rho = P$ olur** ve $dP/df=-P$ ⟹ $P=P_0e^{-f}$ — üstel. Yani kitap üstel yapının türetim gerekçesini zaten yazmış, sadece arka plan noktasında dondurmuş.

### Dayanak 3 — Üs, kitabın kendi zincir denetiminin ta kendisi
> `[I]:268` — "**Zincir denetimi (bağımsız).** $C\chi/P_0$ ile $4\Phi/c_0^2$ aynı olmalıdır ve Dünya yüzeyinde $2{,}7777\times10^{-9}$ ile $2{,}7844\times10^{-9}$ çıkar — **%0,24.**"

$P=P_0\exp(-C\chi/P_0)=P_0\exp(-4\Phi/c_0^2)$ — **üstelin üssü, kitabın zaten özdeşlediği iki niceliktir.** Yeni bir sayı, yeni bir kalibrasyon, yeni bir parametre yok. (Betik: $4\Phi/c_0^2 = 2{,}784\times10^{-9}$ ✓; $\rho_n c_0^2/P_0 = 4{,}0$ tam ✓.)

### Dayanak 4 — Üstel/logaritmik yapı kitabın barotropik potansiyelinin kendisi
> `[A]:110` — "Stiff hâl denklemiyle kararlı akış enerji denklemi ($\tfrac12v^2+h=$ sbt, **$h=c_0^2\ln\rho$**)"
> `[A]:131` — "$\boxed{\;v^2 = 2c^2\ln\frac{\rho_0}{\rho}\;}$"
> `[A]:137` — "$\rho(r)=\rho_0\exp\!\left(-\frac{v(r)^2}{2c^2}\right)$"
> `[I]:298` — "$U(\rho)=c_0^2\,\rho\,\ln\frac{\rho}{\rho_0}$"
> `[I]:302` — "$\rho=\rho_0\,e^{-v^2/2c_0^2} \Longrightarrow \boxed{\;\rho=\rho_0\,e^{-(r_e/R)^2}\;}$"

Stiff ortamın *tanımlayıcı* özelliği entalpinin logaritmik, profillerin üstel olmasıdır. Kitap bunu $\rho$-kanalında dört yerde kullanıyor. Öneri, $\chi$-kanalında aynı yapıyı istiyor — **teorinin dilinin dışına çıkmıyor, dilin kendisini kullanıyor.**

### Dayanak 5 — Kitap güçlü alanı AÇIKÇA YAZILMAMIŞ ilan ediyor
> `[I]:225` — "Doğrusallaştırılmış rejim ($\delta P\ll P_0$): galaktik ve Güneş Sistemi alanları için $\delta P/P_0\lesssim10^{-9}$ — bol marj; **güçlü-alan davranışı yazılmamıştır.**"
> `[I]:204` — "**Hâl denkleminin doğrusallaştırılması** (M-44'ün iki kanalı)"
> `[I]:67` — "$u(\rho)=\tfrac12 c_0^2\rho$ **mertebesinde, sabit $\chi$'de**"

**Bu üç satır denetimin hukuki temelidir:** M-46 lineer profili bir *taahhüt* olarak değil, kendi ilan ettiği doğrusallaştırma olarak yazıyor; $u$'nun $\chi$-bağımlılığı hiç yazılmamış. Üstel öneri **yazılı bir taahhüdü devirmiyor — ilan edilmiş bir boşluğu ilk kez dolduruyor.**

**ÇELİŞKİ VAR MI: HAYIR.** Öneri, "teoriye yabancı değil" iddiasını beş bağımsız kitap-içi dayanakla karşılıyor; ikisi (`[I]:259`, `[I]:268`) doğrudan sayısal, ikisi (`[A]:110-137`, `[I]:298-302`) doğrudan matematiksel, biri (`[A]:30`) doğrudan yasal.

---

## SENTEZ — LİNEER ↔ ÜSTEL AYRIMINI HANGİ KANON MADDESİ YAPIYOR?

| Kanon maddesi | Ayrım yapıyor mu? | Hüküm |
|---|---|---|
| M-44 dalga kanalı / GW170817 (`[A]:240,246`) | Kısmen | **Toplamsal yazımı dışlar**; çarpımsal lineer ile üsteli ayırmaz |
| $k=0$ taahhüdü (`[I]:53`) | Hayır | İkisi de korur; $k=0$ Poisson'u koruyan mekanizma |
| $\nabla^2\chi=-q_nn_m$ (`[I]:208`) | Kısmen | **Toplamsal yazımı LLR ile dışlar** (`[I]:249`) |
| **M-9 Jeans, $(\partial P/\partial\rho)_\chi>0$** (`[B]:102-103,119`) | **EVET** | Lineer $r<4\mu$'de negatif ⟹ **dışlanır** |
| **M-9 siklostrofik denge + 3. adım** (`[B]:116-118,110`) | **EVET** | Lineer $v_\theta\to\infty$, kendiliğinden kavitasyon ⟹ **dışlanır** |
| **M-3/M-3′/M-4 "stiff ortam sonlu parametrede yırtılmaz"** (`[A]:117,139,218`) | **EVET** | Lineerin $r_c=4\mu$ yüzeyi bu hükmü ihlal ⟹ **dışlanır** |
| M-1 oran/diferansiyel ayrımı (`[A]:30`) | Kısmen | Üstelde her noktada tam; lineerde de çarpımsal yazılırsa tam |
| M-7 yırtılmama tabanı (`[B]:24`) | Hayır | Üstelde koşul özdeşlik olur (M-7'nin *rolü* değişir) |
| M-8 kalibrasyonu (`[B]:59-63`) | Hayır | İkisi de $P_0=\tfrac14\rho_nc_0^2$ verir ($10^{-18}$ doğrulukla) |
| Merkür 43″ (ana oturum) | **EVET** | Lineer 7960σ ⟹ **dışlanır** |

**Çekirdek kanon, ana oturumun Merkür sonucundan tamamen bağımsız olarak lineer yazımı ÜÇ AYRI YERDEN dışlıyor** (Jeans pozitifliği, siklostrofik sınırlılık, stiff yırtılmazlık). Üstel bu üçünü de aynı tek satırla ($a(\chi)>0$) geçiyor.

---

## ZORUNLU METİN DÜZENLEMELERİ (fizik değil, ifade — 5 kalem)

1. **`[I]:40` ve `[I]:80` (M-44 kutulu sonuç):** "$v_{ses}=c_0$ tam olarak" → "$v_{ses}=c_{loc}=\sqrt{P/\rho}$ tam olarak (yerel)". `[A]:240` zaten böyle yazıyor; `[I]` Postülat 4'e göre eksik. *(Üstel öneriden bağımsız olarak da düzeltilmesi gereken bir tutarsızlık.)*
2. **`[I]:220` (M-46 Sonuç):** "$A=(\partial P/\partial\rho)_\chi=c_0^2$ (dalga sertliği), $C=-(\partial P/\partial\chi)_\rho$ (deplasman direnci)" → iki *sabit* değil, tek fonksiyon + bir oran: $A(\chi)=c_0^2e^{-C_0\chi/P_0}$, $C(\chi)=(C_0/P_0)P$. "İki tepki katsayısı" yerine "bir stiff katsayı fonksiyonu ve onun logaritmik $\chi$-hızı". Empedans oranı ($4{,}2\times10^{-39}$) ve $\varepsilon=6{,}88\times10^{-41}$ **arka plan değerleri** olarak etiketlenmeli (`[I]:264-266`, Ek C).
3. **`[I]:67` + `[I]:298` (iç enerji):** $U$'nun $\chi$-bağımlılığı açıkça yazılmalı: $U(\rho,\chi)=c_0^2e^{-C\chi/P_0}\rho\ln(\rho/\rho_0)$; ve $U\to U+b(\chi)\rho$ serbestliğinin $b'=0$ ile sabitlendiği (Poisson'un tamlığının koşulu) kayda geçmeli.
4. **`[I]:211` (M-46 2. adım):** $P(r)=P_0-CNq_n/4\pi r$ "doğrusallaştırılmış profil ($\delta P\ll P_0$)" olarak etiketlenmeli; tam profil $P=P_0e^{-CNq_n/4\pi P_0 r}$ olarak yanına yazılmalı. **`[I]:211`'in "M-28/M-35'in profili birebir"** ifadesi, M-28/M-35'in de aynı etiketi alması gerektiğini gösteriyor — **bu iki girdi bu denetimin kapsamı dışında ve ayrıca denetlenmeli.**
5. **`[B]:24` + `[B]:34-40` (M-7):** yırtılmama koşulunun statüsü "alt sınır türetimi"nden "doğrusal rejim muhasebesi"ne çevrilmeli; `[B]:39`'un "iki kat emniyet payı" açık ucu envanterden düşer.

## YENİ AÇIK UÇLAR (3 kalem — hiçbiri çelişki değil)

1. **$\Sigma$ (ve $\Lambda_\Sigma$) yerel mi, evrensel mi?** `[I]:328`'in kohezyon terimi $c_0^2\Lambda_\Sigma^2$ önçarpanı taşıyor. Postülat 4'ün yerelliği tutarlı uygulanırsa $c_0^2\to a(\chi)$ olmalı ⟹ $\Sigma\propto P$ ⟹ $\Sigma/P$ derinlikten bağımsız sabit, $v_m\propto c_{loc}$. $\Sigma$ evrensel sabit sayılırsa $\Sigma/P$ derinlikle büyür ve ortam **daha** kohezif olur. **İki okuma da yırtılmayı engelliyor**, ama `[I]:202`'nin $1/2v_m^2$ zaman terimini ve M-6 merdiveninin derin-kuyu okumasını farklı etkiliyorlar. Karar verilmeli.
2. **Derin rejimde ($r\to0$) hâl denkleminin geçerliliği.** M-3′ kendi çekincesini yazmış: `[A]:186` — "**Derin seyrelme rejiminde hâl denklemi en az sınanmış yerdedir.** $P=c_0^2\rho$'nun $\rho\to0$'a kadar geçerli olduğu varsayılmıştır". Üstelin ufuk-yok/tekillik-yok sonuçları ($r\to0$'da $P\to0$, $\rho=\rho_0$) **aynı çekinceyi miras alır** ve bu açıkça yazılmalı. Kuyu tabanı $\rho$ sabit ama $P\to0$ — M-3′'ün $\rho\to0,P\to0$ rejiminden farklı bir köşe; ayrıca sınanmamış.
3. **M-44 Geçerlilik Sınırı md. 4 KAPANMIYOR.** `[I]:167` — "**$\Lambda$ ölçeklemesi çıkmaz.** Cetvellerin ve saatlerin neden tam $\Lambda$ ile ölçeklendiği (M-42'nin $\gamma_\ell=-1$'i) maddenin ortam içindeki bağlı yapısının modelini gerektirir." Üstel öneri $c_{loc}=c_0\Lambda^2$'yi ($\Lambda\equiv e^{-\Phi/c_0^2}$ tanımıyla) eylemden verir, ama **cetvel/saat tarafını ($\ell,f\propto\Lambda$) vermez** — md. 4 aynen açık kalır. Aynı şekilde `[I]:165` (iki kısmi türevin mikro-modeli) ve `[I]:158/178` (zaman-bağımlı korunumsuzluğun $10^9$ bastırması) **etkilenmiyor, kapanmıyor.**

## SAYISAL DENETİM ÖZETİ (betikle doğrulandı)

| Kalem | Sonuç |
|---|---|
| $P_0/\rho_0/c_0^2$ | $1{,}000000000000$ ✓ (M-8/M-5 stiff arka plan denetimi) |
| $\rho_n c_0^2/P_0$ | $4{,}0$ tam ⟹ üs $=4\Phi/c_0^2$ ✓ (M-8 ile birebir) |
| Dünya yüzeyi üssü | $2{,}784\times10^{-9}$ ✓ (`[I]:268` ile birebir) |
| Lineer↔üstel $P$ sapması (yüzey) | $3{,}9\times10^{-18}$ — tüm zayıf-alan kalibrasyon zinciri korunur |
| Lineer↔üstel $\Lambda$ sapması | $2{,}4\times10^{-19}$ |
| Kütle-itim iç tutarlılığı | $a=-(1/\rho_n)dP/dr = -(GM/r^2)e^{-4\mu/r}$ — analitik TAM eşleşme ✓ |
| $U$'dan $P$ geri kazanımı | $\rho U_\rho-U = c_0^2\rho e^{-C\chi/P_0}$ ✓ (sympy) |
| $\partial U/\partial\chi\vert_{\rho=\rho_0}$ | $0$ ✓ ⟹ Poisson TAM korunur (sympy) |
| $v_{\theta,max}$ (siklostrofik) | $c_0/\sqrt e=0{,}6065\,c_0$ at $r=4\mu$ (üstel) ↔ $\infty$ (lineer) |
| $M_{min}$ ($r_{ph}=2\mu=R_\rho$) | $8{,}261\,M_\odot$ ✓ (kitabın 8,3 formülüyle sayısal aynı) |
| $b_{krit}/\mu$ | üstel $2e=5{,}4366$ ↔ GR $3\sqrt3=5{,}1962$ ⟹ %4,63 |
| PPN | üstel $\beta=1{,}000$, presesyon ölçeği $1{,}000000$ ↔ lineer $\beta=0{,}500$, $7/6=1{,}166667$ |