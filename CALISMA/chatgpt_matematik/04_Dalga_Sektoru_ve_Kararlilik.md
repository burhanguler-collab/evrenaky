# 4. Dalga Sektörü ve Kararlılık

## 4.1 Akışkanın küçük bozuntuları

Durgun ve homojen arka plan çevresinde

\[
\rho=\rho_0+\delta\rho,
\qquad
\mathbf u=\delta\mathbf u,
\qquad
|\delta\rho|\ll\rho_0
\]

yazılsın. EA-1 ve EA-2'nin doğrusal biçimleri:

\[
\partial_t\delta\rho+\rho_0\nabla\cdot\delta\mathbf u=0,
\]

\[
\partial_t\delta\mathbf u=-\frac{c_s^2}{\rho_0}\nabla\delta\rho,
\qquad
c_s^2=\left.\frac{dP}{d\rho}\right|_{\rho_0}.
\]

Birleştirildiğinde

\[
\boxed{
\partial_t^2\delta\rho-c_s^2\nabla^2\delta\rho=0
}
\tag{EA-14}
\]

ve düzlem dalga için

\[
\boxed{\omega^2=c_s^2k^2}
\tag{EA-15}
\]

elde edilir.

Bu sonuçta temel hız \(c_s^2=dP/d\rho\)'dur. \(P/\rho\) oranı ancak özel hâl denkleminde buna eşittir.

## 4.2 Deplasman alanı dalgaları

Kaynak dışındaki EA-3 için

\[
\boxed{\omega^2=v_\chi^2k^2}
\tag{EA-16}
\]

olur. Dolayısıyla temel model iki farklı karakteristik hıza izin verir:

- \(c_s\): ortamın sıkışma kanalı,
- \(v_\chi\): madde kaynaklı deplasman alanı kanalı.

Bunların eşit veya farklı olması türetim değil, teorinin dinamik yapısına ilişkin bir seçimdir. Her seçim daha sonra deneysel olarak sınanmalıdır.

## 4.3 Kararlılık koşulları

Doğrusal gradyan kararlılığı için

\[
\rho_0>0,\qquad \rho_\chi>0,\qquad c_s^2>0,\qquad v_\chi^2>0
\tag{EA-17}
\]

gereklidir. Bunlardan biri negatifse üstel büyüyen mod veya negatif kinetik enerji ortaya çıkar.

## 4.4 Sınırlar

EA-14–EA-16 ışığın ne olduğunu henüz göstermez. Bir Evrenakı modunu elektromanyetik ışıkla özdeşleştirmek için en az şu özellikler ayrıca türetilmelidir:

- iki enine polarizasyon veya gözlenen polarizasyon yapısı,
- yüklerle/maddeyle kuplaj,
- frekans–enerji ilişkisi,
- çok düşük vakum dağılımı,
- hareketli kaynak ve gözlemci için ölçüm protokolü.

Bu nedenle \(c_s=c\) sayısal eşitlemesi bir kalibrasyon olabilir; “ışık türetildi” sonucu değildir.
