# Hesaplar — bu çalışmanın kendi çıktıları

Sınıf klasörleri **girdi**dir: yalnız ölçülen eğriler ve yayınlanmış katalog büyüklükleri.
Bu klasör **çıktı**dır: bu çalışmada hesaplanan her şey.

## Kural

Her hesap kendi alt klasörüne konur ve şu üçü birlikte bulunur:

1. `SONUC.csv` — galaksi başına sayısal çıktı
2. `YONTEM.md` — hangi denklem, hangi parametreler serbest, hangi sınırlar, hangi ölçüt
3. `betik` — üreten betiğin adı ve sürüm tarihi

Bir hesap bu üçü olmadan buraya girmez. Gerekçe: bu çalışmanın bütün geçmişinde en pahalı
hatalar, bir sayının nasıl üretildiğinin kaydının tutulmamasından çıktı.

## Dışarıdan alınan ilişkiler — ve statüleri

Aşağıdaki büyüklükler bu çalışmada hesaplanmamış, literatürden alınmıştır. Kullanıldıkları her
yerde atıf zorunludur:

| İlişki | Kaynak | Ne veriyor | Statü |
|---|---|---|---|
| NFW yoğunluk profili | Navarro, Frenk & White 1996 | halo profil biçimi | N-cisim çıktısına **uydurulmuş formül** (analitik türetim değil) |
| $c_{200}$–$M_{200}$ | Dutton & Macciò 2014 | konsantrasyon–kütle, 0,11 dex saçılma | N-cisim simülasyonlarına **fitlenmiş** iki katsayı |
| Abundance matching | Moster ve ark. 2013 | $M_* \leftrightarrow M_{halo}$ | gözlemsel kütle fonksiyonuna **fitlenmiş** |
| Popülasyon sentezi $\Upsilon_*$ | 3,6 μm literatürü | $\Upsilon_*\approx0{,}3$–$0{,}8$ | IMF varsayımına bağlı **bant**, tek sayı değil |

**Uyarı:** bu dördü de "türetilmiş" değil, "kalibre edilmiş"tir. Karşılaştırmalarda bu böyle
sunulmalıdır.
