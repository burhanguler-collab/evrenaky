# 2. Eylem ve Temel Alan Denklemleri

## 2.1 Neden eylem ilkesi?

Eylem ilkesi, alan denklemlerinin birbirinden bağımsız olarak seçilmesini önler ve enerji-momentum hesabı için ortak bir başlangıç sağlar. Aşağıdaki eylem nihai mikro-kuram değil, sınanabilir en küçük etkili alan modelidir.

## 2.2 Akışkan sektörü

Dönüsüz akış için \(\mathbf u=\nabla\theta\) yazılsın. Akışkan eylem yoğunluğu

\[
\mathcal L_f=-\rho\left(\partial_t\theta+\frac12|\nabla\theta|^2\right)-\varepsilon(\rho)
\]

seçilir. Burada \(\varepsilon(\rho)\) iç enerji yoğunluğudur ve basınç

\[
P(\rho)=\rho\varepsilon'(\rho)-\varepsilon(\rho)
\]

ile tanımlanır.

\(\theta\)'ya göre varyasyon:

\[
\boxed{\partial_t\rho+\nabla\cdot(\rho\mathbf u)=0}
\tag{EA-1}
\]

sonucunu verir. \(\rho\)'ya göre varyasyon ise Bernoulli bağıntısını verir:

\[
\partial_t\theta+\frac12|\mathbf u|^2+h(\rho)=0,
\qquad h(\rho)=\varepsilon'(\rho),
\qquad h'(\rho)=\frac{P'(\rho)}{\rho}.
\]

Gradyan alınırsa Euler denklemi elde edilir:

\[
\boxed{\partial_t\mathbf u+(\mathbf u\cdot\nabla)\mathbf u
=-\frac1\rho\nabla P}
\tag{EA-2}
\]

Buradaki artı işareti, \(\mathbf u=\nabla\theta\) tanımı ve yukarıdaki \(\mathcal L_f\) seçimiyle sabittir; gradyan alındığında EA-2'deki basınç kuvvetinin eksi işareti elde edilir.

## 2.3 Deplasman alanı sektörü

Boyutsal olarak eksiksiz alan eylemi

\[
S_\chi=\int dt\,d^3x\;\rho_\chi
\left[
\frac{1}{2v_\chi^2}(\partial_t\chi)^2
-\frac12|\nabla\chi|^2
+q_n n\chi
\right]
\]

olarak alınsın. \(\rho_\chi\) sabit pozitif bir normalizasyon yoğunluğudur. Sabit olduğunda alan denkleminden sadeleşir; fakat enerji hesabında korunmalıdır.

\(\chi\)'ye göre Euler–Lagrange denklemi:

\[
\boxed{
\frac{1}{v_\chi^2}\partial_t^2\chi-\nabla^2\chi=q_n n
}
\tag{EA-3}
\]

olur. Durağan sınırda:

\[
\boxed{\nabla^2\chi=-q_n n.}
\tag{EA-4}
\]

İşaret EA-P4 ile birlikte merkez yönlü ivme verecek biçimde seçilmiştir.

## 2.4 Atomik pompa–arka plan dengesi

Atomik pompa etkisi \(\chi\) alanıyla temsil edilir. Evrenakı'nın momentum dengesi genel olarak

\[
\rho\frac{D\mathbf u}{Dt}=-\nabla P_{\rm tot}+\mathbf f_{\rm pompa}
\tag{EA-5}
\]

biçimindedir. Durağan durumda \(\mathbf u=0\) ve

\[
-\nabla P_{\rm tot}+\mathbf f_{\rm pompa}=0
\tag{EA-6}
\]

olur. Teorinin fiziksel kabulüne göre atomik pompalar Evrenakı'yı dışa deplase ederken arka plan Evrenakı içe doğru karşı basınç uygular. Bu denge sürekli radyal akış değil, uzaysal bir basınç gradyanı üretir. Zayıf deplasman rejiminde denge profili

\[
\boxed{P_{\rm tot}=P(\rho)-C\chi}
\tag{EA-7}
\]

olarak yazılır. Bu bağıntı termodinamik hâl denklemi değil, pompa alanı ile arka planın mekanik denge bağıntısıdır. Karşı kuvvet eşdeğer olarak bir pompa/kohezyon gerilmesiyle

\[
\mathbf f_{\rm pompa}=\nabla\cdot\boldsymbol\sigma_{\rm pompa}
\]

biçiminde temsil edilebilir. \(C\)'nin işareti, EA-7'nin basınç kuyusu oluşturması ve EA-6'nın dengelenmesi birlikte gözetilerek sabitlenmelidir.

Homojen arka planda \(\nabla P(\rho_0)=0\) olduğundan EA-7 ve EA-6 birlikte

\[
\boxed{\mathbf f_{\rm pompa}=\nabla P_{\rm tot}=-C\nabla\chi}
\]

verir. Küresel kaynakta \(\chi\propto1/r\) ve \(\nabla\chi\) merkeze yöneldiği için \(-C\nabla\chi\) dışa yönlü atomik pompa etkisidir; \(-\nabla P_{\rm tot}\) ise içe yönlü arka plan karşı kuvvetidir. Durağanlık bu iki terimin eşitliğidir.

EA-7'yi yalnız Euler denklemine elle eklemek toplam enerji alışverişini kapatmaz. Tam birleşik kuramda atomik pompa, arka plan ve madde geri tepkisi aynı eylemde bulunmalıdır. Bu nedenle iki seviye ayrılır:

1. **Statik kütle-itim seviyesi:** EA-3, EA-4, EA-7 ve EA-P5 birlikte kullanılır.
2. **Geri-tepkili dinamik seviye:** madde serbestlik dereceleri ve kuplajı aynı toplam eylemde yazılmadan tamamlanmış sayılmaz.

Bu ayrım, statik ters-kare kütle-itim sonucunun kullanılmasını; fakat dinamik enerji kaybı veya yörünge sönümünün henüz iddia edilmemesini sağlar.

## 2.5 Genel hâl denklemi

En basit doğrusal arka plan modeli

\[
P(\rho)=P_0+c_0^2(\rho-\rho_0)
\tag{EA-8}
\]

olabilir. Burada

\[
\left.\frac{dP}{d\rho}\right|_{\rho_0}=c_0^2.
\]

EA-8 yerel bir yaklaşım olup \(P_0=\rho_0c_0^2\) sonucunu zorunlu kılmaz. Bu eşitlik isteniyorsa ayrıca sınır koşulu veya daha özel \(P=c_0^2\rho\) hâl denklemi kabul edilmelidir.
