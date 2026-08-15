# 3. Durgun Küresel Çözüm ve Kütle-İtim Yasası

## 3.1 Noktasal kaynak

Merkezde \(N\) nükleondan oluşan durağan bir kaynak için

\[
n(\mathbf x)=N\delta^{(3)}(\mathbf x).
\]

EA-4:

\[
\nabla^2\chi=-Nq_n\delta^{(3)}(\mathbf x)
\]

olur. Üç boyutta

\[
\nabla^2\left(\frac1r\right)=-4\pi\delta^{(3)}(\mathbf x)
\]

özdeşliği kullanılırsa, \(\chi(\infty)=0\) sınır koşuluyla

\[
\boxed{\chi(r)=\frac{Nq_n}{4\pi r}}
\tag{EA-9}
\]

elde edilir.

## 3.2 Basınç kuyusu

Arka plan yoğunluğu yaklaşık sabit ve akışkanın yerel basıncı \(P_0\) ise EA-7:

\[
P_{\rm tot}(r)=P_0-\frac{CNq_n}{4\pi r}
\tag{EA-10}
\]

sonucunu verir. Böylece

\[
\nabla P_{\rm tot}=\frac{CNq_n}{4\pi r^2}\,\hat{\mathbf r}.
\]

Basınç merkezden dışarı doğru artar; EA-P5'teki eksi işareti test cismini merkeze ivmelendirir:

\[
\boxed{
\mathbf a(r)=-\frac{Cq_nN}{4\pi\rho_n r^2}\hat{\mathbf r}
}
\tag{EA-11}
\]

Kaynak kütlesi \(M=Nm_n\) ise

\[
\boxed{
\mathbf a(r)=-\mathcal G_{\rm EA}\frac{M}{r^2}\hat{\mathbf r},
\qquad
\mathcal G_{\rm EA}=\frac{Cq_n}{4\pi\rho_n m_n}
}
\tag{EA-12}
\]

elde edilir.

EA-12'de ters-kare biçim üç uzaysal boyut, yerel ikinci-mertebe alan denklemi ve küresel simetrinin sonucudur. \(\mathcal G_{\rm EA}\), **etkin kütle-itim katsayısıdır**. Sayısal değeri \(Cq_n/\rho_n\) bileşimine ait bir kalibrasyondur; bu aşamada ilk ilkelerden türetilmiş değildir. Eksi işaret bir çekme etkileşimini değil, dış taraftaki daha yüksek Evrenakı basıncının cismi düşük basınçlı merkeze itmesini gösterir.

## 3.3 Genişletilmiş küresel kaynak

Küresel simetrili \(n(r)\) için

\[
\frac1{r^2}\frac{d}{dr}\left(r^2\frac{d\chi}{dr}\right)=-q_n n(r).
\]

\[
N(<r)=4\pi\int_0^r n(s)s^2ds
\]

tanımıyla

\[
\frac{d\chi}{dr}=-\frac{q_nN(<r)}{4\pi r^2}
\]

Bu işaret EA-4 ve noktasal çözüm EA-9 ile uyumludur. Doğrudan EA-9'un türevi \(d\chi/dr=-Nq_n/(4\pi r^2)\)'dir; dolayısıyla

\[
\frac{dP_{\rm tot}}{dr}=\frac{Cq_nN(<r)}{4\pi r^2}.
\]

Sonuç:

\[
\boxed{
\mathbf a(r)=-\mathcal G_{\rm EA}\frac{M(<r)}{r^2}\hat{\mathbf r}
}
\tag{EA-13}
\]

olur.

## 3.4 Süperpozisyonun sınırı

EA-3 doğrusal olduğu için \(\chi\) kaynakları zayıf-alan rejiminde süperpoze olur. Fakat \(P(\rho)\), \(C\), \(q_n\) veya \(\rho_n\) alana bağlıysa fizik doğrusal değildir. Galaksi ölçeğinde farklı davranış elde etmek istenirse bu bağımlılık açık bir kurucu bağıntıdan gelmeli; sisteme özel ek çarpan olarak eklenmemelidir.
