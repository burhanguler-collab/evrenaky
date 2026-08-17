> ⚠️ **DENETİM NOTU (17 Ağustos 2026):** Bu dosya denetlendi — ayrıntı: `tartısma_matematik`, Tartışma #1, Bölüm F.
> **§1 (zaman genleşmesi):** matematik doğru, ancak kitapta daha sağlam hâli zaten var (Kısım 11.4.8.1, Λ_kin, [T]); esas metin odur.
> **§2 (kızıla kayma): BOZUK — kitaba taşınmasın.** Kendi öncülüyle çelişiyor (R·c_loc=sabit ⇒ R∝Λ⁻², metin R∝Λ diyor), işaret konvansiyonu karışık, M-42'nin açık kalemini (γ_ℓ mekanizması) çözülmüş gibi sunuyor.

# Evrenakı: Rölativistik Etkilerin Saf Akışkanlar Mekaniğinden Türetilmesi

Bu belge, "Zerre ve Akışkan" kurgusu dışına çıkmadan, Özel Görelilik (Zaman Genleşmesi) ve Genel Görelilik (Kızıla Kayma) sonuçlarının **saf hidrodinamik ve girdap dinamiği (vortex dynamics)** ile nasıl baştan sona (first-principles) türetilebileceğini göstermektedir. Bu yöntem, Einstein'ın geometrik varsayımlarına (ışık saati vb.) ihtiyaç duymaz.

## 1. Zaman Genleşmesinin Akışkandan Türetilmesi (Prandtl-Glauert Analojisi)

Klasik akışkanlar mekaniğinde, $c_0$ ses hızına (Zerre yayılım hızına) sahip sıkıştırılabilir bir akışkanın (Evrenakı) içinde ilerleyen stabil yapılar (örneğin atomu temsil eden Girdap Halkaları), **hidrodinamik dinamik basınca** maruz kalırlar.

Sıkıştırılabilir akışlar için potansiyel dalga denklemi şu şekildedir:
$$ (1 - M^2) \frac{\partial^2 \phi}{\partial x^2} + \frac{\partial^2 \phi}{\partial y^2} + \frac{\partial^2 \phi}{\partial z^2} = 0 $$
Burada $M = v/c_0$ cismin akışkana göre Mach hızıdır.

**Boy Kısalmasının Türetimi:**
Eğer $x' = x / \sqrt{1 - M^2}$ dönüşümünü yaparsak denklem klasik (sıkıştırılamaz) Laplace denklemine döner. Bunun mutlak fiziksel anlamı şudur: Akışkan içinde $v$ hızıyla ilerleyen herhangi bir stabil basınç yapısı (atom/girdap), hareket yönünde hidro-dinamik olarak tam olarak şu oranda ezilmek (büzülmek) ZORUNDADIR:
$$ L(v) = L_0 \sqrt{1 - \frac{v^2}{c_0^2}} = \frac{L_0}{\gamma} $$
*(Bu geometri varsayımı değil, saf akışkan dinamiğinin kaçınılmaz sonucudur).*

**Zaman Genleşmesinin (Saat Yavaşlamasının) Türetimi:**
Saatimiz, bu girdabın içinde gidip gelen bir iç sinyalden (Zerre) ibaret olsun. Girdap $v$ hızıyla ilerlerken, sinyalin kendi hızı akışkana göre daima $c_0$'dır.
- **Enine (Transvers) Tur Süresi:** Sinyal $L_0$ genişliğindeki yolda giderken akışkan da $v$ ile yana aktığı için efektif hızı $\sqrt{c_0^2 - v^2}$ olur. 
  $$ T_{enine} = \frac{2 L_0}{\sqrt{c_0^2 - v^2}} = \frac{2 L_0}{c_0 \sqrt{1 - v^2/c_0^2}} = \gamma T_0 $$
- **Boyuna (Longitudinal) Tur Süresi:** Girdap hidrodinamik olarak $L_0/\gamma$ kadar ezilmiştir! İleri ve geri tur hesabı:
  $$ T_{boyuna} = \frac{L_0/\gamma}{c_0 - v} + \frac{L_0/\gamma}{c_0 + v} = \frac{2 L_0 c_0 / \gamma}{c_0^2 - v^2} = \gamma \frac{2 L_0}{c_0} = \gamma T_0 $$

**Sonuç:** Hem enine hem boyuna yönelimde girdabın (atomun) iç sinyal çevrim süresi tam olarak $\gamma$ çarpanı kadar yavaşlamıştır. **Zaman genleşmesi ve izotropi, geometrik bir varsayım yapılmadan, doğrudan Prandtl-Glauert akışkan basınç ezilmesinden türetilmiştir. [T]**

---

## 2. Kızıla Kaymanın Akışkandan Türetilmesi (Girdap Kararlılık Denge Denklemi)

Arka plan basıncının $P(r)$ olduğu bir gradyanda (kütle-itim kuyusunda) yer alan bir girdap halkasının (atomun) enerjisi ve sirkülasyonu dış basınçla dengede olmalıdır.

Bir Rankine girdabının iç dinamik basıncı dış basınca eşittir:
$$ P_{iç} \sim \frac{1}{2} \rho_0 (\nu_{tik} R)^2 \propto P_0 $$
Kütle-İtim gradyanının içinde derinlere indikçe (basıncın düştüğü kuyuya indikçe), Zerre yayılım hızı $c_{loc}$ değişir. Evrenakı teorisinde bu değişim $c_{loc}(r) = c_0 \Lambda^2$ şeklindedir ($\Lambda = 1 - \Phi/c_0^2$).

Eğer kuyuya düşen girdabın (atomun) eylem (action) miktarı veya açısal momentumu korunuyorsa ($R \cdot c_{loc} = sabit$), yeni ortamda frekansı $\nu = c_{loc} / R$ şu şekilde ölçeklenir:
1. $c_{loc} \propto \Lambda^2$ (Hız düşer)
2. Akışkanın akustik metriğine göre girdabın denge boyutu $R \propto \Lambda$ oranında büyür.
3. Böylece frekans:
$$ \nu_{tik} \propto \frac{c_{loc}}{R} \propto \frac{\Lambda^2}{\Lambda} = \Lambda $$

**Sonuç:** Girdap atomu, basınç gradyanı içine girdiğinde kendi iç hidrodinamik dengesini (Rankine sınır koşullarını) korumak için dönme frekansını (tik hızını) tam olarak $\Lambda$ oranında düşürmek ZORUNDADIR. 
**Kızıla kayma, dışarıdan kural olarak getirilmemiş, atomun akışkanla yaptığı mekanik denge koşullarından birinci ilkeden (first-principles) türetilmiştir. [T]**
