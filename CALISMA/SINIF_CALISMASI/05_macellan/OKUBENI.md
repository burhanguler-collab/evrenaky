# Sınıf: Sdm – Sm

SPARC Hubble tipi **T = 8, 9**. Kalite ve eğiklik süzgeçlerini geçen galaksiler.

## Sayılar

| | |
|---|---|
| Galaksi sayısı | **28** |
| Toplam ölçüm noktası | 423 |
| Nokta / galaksi | 7 – 34 (medyan 12) |
| İçerdiği Hubble tipleri | Sdm (T=8, n=9), Sm (T=9, n=19) |
| Kalite | Q=1 yuksek: 19 · Q=2 orta: 9 |
| Eğiklik | 30° – 90° (medyan 56°) |

## Neden bu sınıf ayrı tutuluyor

Morfolojik tip, dönüş eğrisi biçimini belirleyen fiziksel özelliklerle (kovan oranı, yüzey
parlaklığı, gaz kesri, disk kalınlığı) güçlü biçimde ilişkilidir. Sınıfları karıştırmak, blok
ortalamasının içinde ters yönlü davranışları görünmez kılar. Bu nedenle her sınıf ayrı
çalışılır ve **sonuçlar sınıf sınıf raporlanır, blok ortalaması yalnız yanında verilir.**

## Bu klasördeki dosyalar

- `veri/*_rotmod.dat` — **ölçülen** dönüş eğrileri. SPARC `Rotmod_LTG` dosyaları, **değiştirilmemiş kopyalar.**
  Sütunlar: `Rad(kpc)  Vobs(km/s)  errV(km/s)  Vgas  Vdisk  Vbul  SBdisk  SBbul`
  `Vdisk` ve `Vbul`, $\Upsilon_*=1$ için verilir; ölçekleme kullanıcıya bırakılmıştır.
- `KATALOG.csv` — bu sınıfın galaksileri için **yayınlanmış** katalog büyüklükleri.

## Kaynak ve provenans

Bütün sayılar **Lelli, McGaugh & Schombert (2016), AJ 152, 157**, Tablo 1'den birebir alınmıştır.
Bu çalışmada **hiçbiri yeniden hesaplanmamıştır.** Ölçüm yöntemleri o yayında belgelidir:

| Sütun | Ne | Nasıl ölçüldü |
|---|---|---|
| `T` | Hubble tipi | 0=S0, 1=Sa … 7=Sd, 8=Sdm, 9=Sm, 10=Im, 11=BCD |
| `D_Mpc`, `eD_Mpc`, `fD` | uzaklık ve yöntemi | 1=Hubble akışı · 2=TRGB · 3=Cepheid · 4=UMa üyeliği · 5=Süpernova |
| `Inc_deg`, `eInc_deg` | eğiklik | HI hız alanı ve/veya optik eksen oranından |
| `L36_1e9Lsun` | 3,6 μm toplam ışıma | *Spitzer* IRAC fotometrisi |
| `Reff_kpc`, `SBeff` | etkin yarıçap / yüzey parlaklığı | 3,6 μm profilinden |
| `Rdisk_kpc`, `SBdisk` | disk ölçek uzunluğu / merkezî yüzey parlaklığı | 3,6 μm diske eksponansiyel uydurma |
| `MHI_1e9Msun`, `RHI_kpc` | HI kütlesi / yarıçapı | 21 cm; $R_{HI}$ = 1 M☉/pc² konturu |
| `Vflat_kms`, `eVflat_kms` | asimptotik düz hız | dönüş eğrisinin dış düz kısmına uydurma |
| `Q` | kalite bayrağı | 1=yüksek, 2=orta, 3=düşük |
| `Kaynak` | HI/Hα verisinin kaynağı | yayın kısaltması (ana katalogun Not 4'ü) |
| `N_nokta` | eğri noktası sayısı | `veri/` dosyasının satır sayısı (tek türetilmiş alan) |

### Okuma uyarıları

- **`Vflat_kms = 0.0` "hız sıfır" demek değildir.** SPARC'ın kuralı: dönüş eğrisinde ölçülebilir
  bir düz (asimptotik) kısım yoksa alan sıfır bırakılır. Bu galaksilerde $V_{flat}$ **tanımsızdır**;
  sıfır olarak hesaba katılmamalıdır. Aynı şey `RHI_kpc = 0.0` için de geçerlidir.
- **`Vdisk`, `Vbul` sütunları $\Upsilon_*=1$ içindir.** Gerçek katkı $\sqrt{\Upsilon_*}\,V_{disk}$'tir.
- **`Kaynak` alanı virgül içerebilir** (birden çok yayın); CSV'de tırnaklanmıştır.
- Uzaklık hatası tüm eğriyi birlikte ölçekler, eğiklik hatası tüm hızları birlikte ölçekler —
  bunlar **korelasyonlu sistematiklerdir**, nokta başına bağımsız hata değil.

**Atıf zorunludur:** Lelli F., McGaugh S. S., Schombert J. M., 2016, AJ, 152, 157 (SPARC).
