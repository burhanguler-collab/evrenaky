# 5.4 Eksenel Kütle İtimi

Şimdiye kadarki deneylerimizde ışık hızını kullanarak kütlenin durağan haldeyken yarattığı basınç farklılıklarını gözlemledik. Bu bölümde ise tamamen farklı bir fenomene; **dönen bir kütlenin Evrenakı akışkanı içerisinde yarattığı eksenel itme kuvvetine** odaklanacağız.

> **Kanıt durumu notu:** Bu bölümde aktarılan sayısal değerler, yazarın rapor ettiği ilk ölçüm bulgularıdır; ham veri setleri ve hata analizleri manüskriptin ilerleyen sürümlerinde yayımlanacaktır. Bulgular, bağımsız tekrar öncesinde "rapor edilen sonuç" statüsündedir.

## Deney 1: Eksenel Kütle İtimi

### 5.4.1 Deneyin Amacı ve Hipotez
Modern fizik, kütleler arasındaki etkileşimleri yalnızca kütleçekim kuvvetiyle açıklar. Ancak Evrenakı teorimize göre, evrensel bir akışkanın içinde dönen bir kütle, çevresindeki Evrenakı dokusunu hareketlendirerek eksenel yönlerde olağanüstü büyüklükte itici/çekici kuvvetler yaratmalıdır. Jiroskopların kütle-itime meydan okuyan hareketleri veya sarmal galaksilerin yörünge anomalileri (Rubin & Ford, 1970) de bu fenomenin sonuçlarıdır. Bu deneyin amacı, laboratuvar koşullarında dönen bir diskin yakınına yerleştirilmiş bir kütleyi, hesaplanan kütleçekim kuvvetinden çok daha büyük bir kuvvetle, tamamen Evrenakı rüzgarları aracılığıyla ittiğini kanıtlamaktır.

### 5.4.2 Deney Düzeneği
Deneysel donanımımız son derece hassas bir şekilde tasarlanmıştır:
- **Dönen Disk:** 200 gram ağırlığında, 60 mm çapında manyetik olmayan alüminyum malzemeden üretilmiştir.
- **Hedef Kütle:** Poliüretan akrilat malzemeden (organik) üretilmiş, 6 gram ağırlığında özel bir kütle.
- **Motor:** 0 ile 30.000 RPM (devir/dakika) arasında ayarlanabilir hıza sahip elektrik motoru.
- **Kuvvet Ölçer:** Hedef kütleye binen nano-kuvvetleri tespit edebilen çok hassas bir sensör mekanizması.

Dönen disk ile 6 gramlık kütle arasındaki mesafe tam 1 mm olarak ayarlanmış ve her türlü hava/rüzgar etkisini elemine etmek için tüm sistem bir **Vakum Kabini** içerisine yerleştirilmiştir. Manyetik bir etki olmaması adına alüminyum ve organik kütleler tercih edilmiştir.

<div style="text-align: center; margin: 30px 0;">
    <img src="Gorseller/eksenel_itim_sema.png" alt="Eksenel Kütle İtimi Şeması" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--border-color);">
    <p style="font-size: 0.9em; color: var(--text-muted); margin-top: 10px;"><em>Şekil 5.9: Eksenel Kütle İtim Deneyi Temel Düzeneği.</em></p>
</div>

<div style="display: flex; justify-content: center; gap: 20px; margin: 30px 0; flex-wrap: wrap;">
    <div style="text-align: center; flex: 1; min-width: 300px;">
        <img src="Gorseller/eksenel_itim_vakum1.png" alt="Vakum Kabini 1" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--border-color);">
    </div>
    <div style="text-align: center; flex: 1; min-width: 300px;">
        <img src="Gorseller/eksenel_itim_vakum2.png" alt="Vakum Kabini 2" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--border-color);">
    </div>
</div>
<p style="text-align: center; font-size: 0.9em; color: var(--text-muted);"><em>Şekil 5.10: Deneyin gerçekleştirildiği gerçek vakum kabini ve cihaz düzenekleri.</em></p>

### 5.4.3 Yöntem ve Uygulama
Deneyin güvenirliğini test etmek için ilk etapta sistem normal hava ortamında çalıştırılmıştır. Hedef kütleye küçük bir "kanatçık" eklenmiş, disk döndüğünde hava moleküllerinin kanatçığa çarparak kütleyi uzaklaştırdığı ve kuvvet sensöründe negatif değerler okunduğu doğrulanmıştır. 

Asıl deney ise sistemdeki tüm hava boşaltılıp **tam vakum ortamı** sağlandıktan sonra gerçekleştirilmiştir. Vakum sayesinde hava sürtünmesi veya rüzgar etkisi tamamen ortadan kalkmış, içeride sadece Evrenakı kalmıştır. Motor yavaş yavaş hızlandırılmış ve 30.000 devre kadar çıkarılmıştır.

### 5.4.4 Gözlem ve Bulgular
Modern fiziğin Newton çekim yasalarına göre (Newton, 1687), 200 gramlık bir disk ile 1 mm uzağındaki 6 gramlık bir kütle arasında yalnızca **0,00000008 N** (Newton) değerinde mikroskobik bir çekim kuvveti olmalıdır.
Ancak vakum ortamında motor hızlanmaya başladığı an, hedef kütlenin (beklenenin aksine) diske doğru çekilmediği, inanılmaz bir güçle itildiği görülmüştür. Motor 30.000 devre ulaştığında ölçülen itme kuvveti tam **0,00981 N** olarak kaydedilmiştir!

<div style="text-align: center; margin: 30px 0;">
    <img src="Gorseller/eksenel_itim_grafik.png" alt="Eksenel İtim Kuvvet Grafiği" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--border-color);">
    <p style="font-size: 0.9em; color: var(--text-muted); margin-top: 10px;"><em>Şekil 5.11: Motorun devir hızına (RPM) bağlı olarak artan eksenel itim kuvvetinin (Newton) grafiği.</em></p>
</div>

### 5.4.5 Sonuç ve Değerlendirme
Ölçülen 0,00981 Newton'luk itim kuvveti, modern fiziğin hesapladığı kütleçekim kuvvetinden yüz binlerce kat daha büyüktür. Manyetizma yok, hava (rüzgar) yok, ölçülebilir bir mekanik sürtünme yok; dolayısıyla bu kuvveti yaratan yegâne unsur, dönen diskin **Evrenakı akışkanı içerisinde yarattığı devasa eksenel basınç (itim) dalgasıdır**. 

Bu kusursuz deney;
1. Modern fiziğin iddia ettiği "boş uzay" kavramının yanlış olduğunu, uzayın Evrenakı (cosmofluid) adını verdiğimiz bir akışkanla dolu olduğunu,
2. Dönen astronomik cisimlerin (örneğin galaksilerin, karadeliklerin veya jiroskopların) etraflarında yalnızca kütle-itim değil, Evrenakı girdapları aracılığıyla çok güçlü eksenel itici ve çekici alanlar yarattığı hipotezini güçlü biçimde desteklemektedir.
