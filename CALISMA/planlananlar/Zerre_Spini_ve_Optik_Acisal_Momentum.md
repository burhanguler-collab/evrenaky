# ÇALIŞMA DOSYASI — ZERRE SPİNİ ↔ OPTİK AÇISAL MOMENTUM AÇIĞI (K-8)

> ⚠️ **BU DOSYA YAYIN METNİ DEĞİLDİR.** `app.js`'e kayıtlı değildir, sitede görünmez.
> Amacı: E1 kararının (${v_{cev}=\sqrt2\,c}$) ortaya çıkardığı yeni bir nicel sınavı tek yerde tutmak.
> Kapandığında ya da yayına taşındığında bu dosya silinir.
>
> **Açılış:** 10 Ağustos 2026 · **Durum:** AÇIK — hiçbir yayın dosyası değiştirilmedi.
> **Bağlam:** `Temel_Donus_ve_Temel_Parcacik_Plani.md` §19.15'ten türeyen kalem.

---

## 0. TEK CÜMLELİK HÜKÜM

Zerre'nin öz açısal momentumu, $\hbar$'ın **14 milyarda biri** çıkıyor; bir "foton eşdeğeri" boyunca toplandığında bile gözlenen optik açısal momentumun yalnız **milyonda birini** karşılıyor. Teorinin polarizasyon kanalı (disk yönelimi + basınç torku) bu açığı kapatmak zorundadır, yoksa açık kalır.

---

## 1. HESAP NEDEN ŞİMDİ YAPILABİLDİ

$L = k_a\,m_z\,v_{cev}\,r_z$ üç girdi ister. Üçü de ancak 10 Ağustos 2026 kararlarıyla sabitlendi:

| Girdi | Değer | Kaynak |
|---|---|---|
| $k_a$ | $1/2$ (basık/disk gövde) | §19 (T-5b çözümü); önce yanlışlıkla $2/5$ |
| $v_{cev}$ | $\sqrt2\,c = 4{,}243\times10^8$ m/s | §11.3 / E1 (M-3 duvar hızı yasası); önce **"belirlenmemiş"** |
| $r_z$ | $2{,}35\times10^{-18}$ m | Postülat 4 ($m_z/\rho_n$'den; eşdeğer küre yarıçapı) |

Yani bu sınav, $v_{cev}$ belirsiz olduğu sürece **yapılamıyordu.** E1'in yan ürünü.

---

## 2. SAYILAR

**Zerre'nin öz açısal momentumu:**
$$L_z = \tfrac12 \times (1{,}47\times10^{-35}) \times (4{,}243\times10^{8}) \times (2{,}35\times10^{-18}) = 7{,}33\times10^{-45}\ \text{J·s}$$

$$\frac{\hbar}{L_z} = \frac{1{,}055\times10^{-34}}{7{,}33\times10^{-45}} = \mathbf{1{,}44\times10^{10}}$$

**Bir "foton eşdeğeri" boyunca toplam** (600 nm ışık; $\nu = 5{,}00\times10^{14}$ Hz, $\tau = 7{,}7$ ps):

| Nicelik | Değer |
|---|---|
| Pencere içindeki Zerre sayısı $N=\nu\tau$ | $3{,}85\times10^{3}$ |
| Taşınan toplam spin $N L_z$ | $2{,}82\times10^{-41}$ J·s |
| Ölçülen (foton başına) | $\hbar = 1{,}055\times10^{-34}$ J·s |
| **Açık** | **$3{,}7\times10^{6}$ kat** |

**Karşı ölçüm:** Beth (1936) — dairesel polarize ışığın yarım-dalga plakasına uyguladığı tork, foton başına $\hbar$ ile uyumlu. Bu ölçüm eski ama sağlam ve çok kez yenilendi; teori bu mertebeyi vermek zorundadır.

---

## 3. AÇIĞI KAPATABİLECEK ADAYLAR

### 3.1 ⭐ Süpürülen disk yarıçapı ($r_z$ değil, $R_{disk}$)
Teori elektron için bunu **zaten** söylüyor (2.1): *"kavitasyonu çok küçük ama süpürdüğü Disk yarıçapı EN GENİŞ."* Aynı ayrım Zerre için de geçerliyse, açısal momentumu belirleyen $r_z$ (kavitasyon çekirdeği) değil, diskin süpürdüğü yarıçaptır.

Gereken değer: $N L = \hbar$ için Zerre başına $L = \hbar/N = 2{,}74\times10^{-38}$ J·s, yani

$$R_{disk} = \frac{L}{k_a m_z v_{cev}} = \frac{2{,}74\times10^{-38}}{3{,}12\times10^{-27}} \approx 8{,}8\times10^{-12}\ \text{m} \;(\approx 8{,}8\ \text{pm})$$

**Denetim kalemleri:**
- $R_{disk}/r_z = 3{,}7\times10^{6}$ — elektronun disk/kavitasyon oranıyla kıyaslanmalı; aynı mertebede mi?
- 600 nm ışıkta Zerre Aralığı 600 nm; 8,8 pm disk buna rahat sığar ($1/6{,}7\times10^4$). ✔
- **Sorun adayı:** X-ışını (0,1 nm = 100 pm) hâlâ diskten büyük ✔, ama **gama ışınında** ($\lambda \lesssim 1$ pm) Zerre Aralığı diskten **küçük** kalır — katar iç içe geçer. Bunun ne anlama geldiği ayrıca düşünülmeli.
- 9.8'in disk-tork mekaniği bu yarıçapla yeniden hesaplanmalı (Malus yasası bozulmamalı).
- $\lambda_C(e) = 2{,}43$ pm ile 8,8 pm arasındaki $\approx3{,}6$ katlık ilişki tesadüf mü, yoksa bir bağ mı — kontrol edilmeli. *(Dikkat: buradan bir çarpan uydurulmamalı — Madde 21.)*

### 3.2 Açısal momentum spinden değil, **disk-tork kanalından** taşınıyor
9.8'e göre polarizasyonun taşıyıcısı Zerre'nin spini değil, **diskin yönelimi ve ona etki eden basınç torkudur.** O hâlde §2'nin hesabı yanlış kanalı ölçmüş olur.
**Ama bedava değil:** o kanalın $\hbar$ mertebesini verdiği **gösterilmek zorunda.** "Başka kanaldan gelir" demek, hesap yapılmadıkça açığı kapatmaz — yalnız adresini değiştirir.

### 3.3 $\tau$ daha büyük (dolayısıyla $N$ daha büyük)
$N L_z = \hbar$ için $N = 1{,}44\times10^{10}$ gerekir → $\tau = N/\nu = 2{,}9\times10^{-5}$ s = 29 µs.
**Elenir:** 29 µs, fotoelektriğin ölçülmüş nanosaniye-altı "gecikmesiz" emisyonuyla (Lawrence & Beams, 1927) doğrudan çelişir. Bu yol kapalı.

### 3.4 $v_{cev}$ daha büyük
$L=\hbar/N$ için $v = 1{,}59\times10^{15}$ m/s $= 5{,}3\times10^{6}\,c$ gerekir.
**Elenir (bu düzeyde):** duvar hızı yasası (M-3) $\sqrt2c$ diyor ve o yasa E1'in temeli. Ayrıca $5{,}3\times10^{6}c$, kavitasyon eşiğinin ($\approx1{,}4\times10^{4}c$) ~380 katı — yani Kut düzeyine ait bir hız olurdu, ki Kut hiçbir hesaba girmez (Anayasa Madde 30). Bu yol da kapalı.

**Sonuç: ayakta kalan iki aday 3.1 ve 3.2'dir ve ikisi birbirini dışlamaz** — süpürülen disk yarıçapı büyükse tork kolu da büyür.

---

## 4. NE **YAPILMAMALI**

- $R_{disk}$'e 8,8 pm değeri **atanmamalı.** O sayı, açığı kapatmak için *gereken* değerdir — bağımsız bir gerekçeden gelmedikçe yazılırsa tam olarak Anayasa Madde 21'in yasakladığı yama parametre olur. §19.15'te $\tau$ için verdiğimiz kararla aynı ilke.
- Açık, "başka kanaldan gelir" denip kapatılmamalı (bkz. 3.2 uyarısı).
- Bu kalem 7.4'e **nicel hesap kalemi** olarak yazılır (Anayasa Madde 19); "açıklayamıyoruz" dili kullanılmaz.

---

## 5. YAPILACAK İŞ SIRASI

1. **9.8'in disk-tork bütçesini hesapla:** gradyan torkunun bir Zerre diskine aktardığı açısal momentum, mevcut geometriyle kaç J·s? $\hbar$ mertebesine ne kadar yakın?
2. Elektronun disk/kavitasyon yarıçap oranını çıkar; Zerre için gereken $3{,}7\times10^{6}$ oranıyla aynı mertebede mi?
3. Gama ışını rejiminde (Zerre Aralığı < disk çapı) katarın ne olduğunu tanımla.
4. Sonuç ne olursa olsun 7.4'e kalem olarak yaz; Malus yasası ve 9.8 sayıları bozulmadıysa kaydet.

---

## 6. DURUM KAYDI

| Kalem | Durum | Tarih |
|---|---|---|
| $L_z$ hesabı | ✅ yapıldı — $7{,}33\times10^{-45}$ J·s | 10 Ağu 2026 |
| Açığın büyüklüğü | ✅ tespit — $3{,}7\times10^{6}$ kat | 10 Ağu 2026 |
| Aday 3.3 ($\tau$) | ✅ elendi (29 µs, Lawrence & Beams ile çelişir) | 10 Ağu 2026 |
| Aday 3.4 ($v_{cev}$) | ✅ elendi (M-3 ve Madde 30 ile çelişir) | 10 Ağu 2026 |
| Aday 3.1 (süpürülen disk yarıçapı) | ⬜ açık — denetim kalemleri §3.1'de | — |
| Aday 3.2 (disk-tork kanalı bütçesi) | ⬜ açık — **öncelikli iş** (§5 md.1) | — |
| 7.4'e kalem yazımı | ⬜ yapılmadı | — |
