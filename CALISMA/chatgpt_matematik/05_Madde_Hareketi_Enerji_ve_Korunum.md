# 5. Madde Hareketi, Enerji ve Korunum

## 5.1 Yüzey basıncından kütle-itim

Evrenakı basıncının sonlu bir cisme uyguladığı net kuvvet, yüzey kuvvetlerinin toplamıdır:

\[
\boxed{\mathbf F_{\rm Kİ}=-\oint_{\partial V}P_{\rm dış}(\mathbf x)\,\mathbf n\,dA.}
\tag{EA-18}
\]

Diverjans teoremiyle

\[
\mathbf F_{\rm Kİ}=-\int_V\nabla P_{\rm dış}\,dV
\]

olur. Basınç gradyanı cismin boyutuna göre yavaş değişiyorsa

\[
\boxed{\mathbf F_{\rm Kİ}\simeq-V_{\rm etk}\nabla P_{\rm dış}.}
\tag{EA-19}
\]

Bu, kaldırma kuvvetiyle aynı yüzey-basıncı matematiğidir; fakat Evrenakı teorisinde basınç gradyanı önceden kabul edilmiş bir merkezcil kuvvet alanından değil, atomik pompa–arka plan dengesinden doğar. Ortamın kendi pompa–arka plan kuvvetleri dengede olabilirken test cisminin karşı yüzlerindeki **dış** basınçlar eşit olmadığı için cisim düşük basınçlı merkeze itilir.

## 5.2 Test cismi potansiyeli

Statik kaynak alanında test cisminin ivmesi EA-P5 ve EA-7 ile

\[
\mathbf a=-\frac1{\rho_n}\nabla P_{\rm tot}
=\frac{C}{\rho_n}\nabla\chi-\frac1{\rho_n}\nabla P(\rho)
\]

olur. Homojen arka planda ikinci terim sıfırdır. Birim kütle başına etkin potansiyel

\[
\boxed{\Phi_{\rm EA}=-\frac{C}{\rho_n}\chi}
\tag{EA-20}
\]

seçilirse

\[
\mathbf a=-\nabla\Phi_{\rm EA}
\]

elde edilir. Noktasal kaynak için

\[
\Phi_{\rm EA}(r)=-\mathcal G_{\rm EA}\frac{M}{r}.
\]

Bu, zayıf ve statik rejimde yörünge enerjisinin

\[
E_{\rm test}=\frac12m|\mathbf v|^2+m\Phi_{\rm EA}
\]

olarak korunmasını sağlar.

## 5.3 Alan enerjisi

Deplasman alanının enerji yoğunluğu

\[
\boxed{
\mathcal E_\chi=\rho_\chi\left[
\frac{1}{2v_\chi^2}(\partial_t\chi)^2+
\frac12|\nabla\chi|^2
\right]
}
\tag{EA-21}
\]

ve enerji akısı

\[
\boxed{
\mathbf S_\chi=-\rho_\chi(\partial_t\chi)\nabla\chi
}
\tag{EA-22}
\]

olarak bulunur. Kaynak varken

\[
\partial_t\mathcal E_\chi+\nabla\cdot\mathbf S_\chi
=\rho_\chi q_n n\,\partial_t\chi.
\tag{EA-23}
\]

Bu artı işareti, EA-3'ün \(\rho_\chi\partial_t\chi\) ile çarpılmasıyla doğrudan elde edilir. Sağ taraf alan ile madde arasındaki enerji alışverişidir. Maddenin eyleminde bunun ters işaretli karşılığı bulunmadan toplam enerji korunumu tamamlanmış olmaz.

## 5.4 Eşit düşme ve etkin kütle

EA-P5'in cisimden bağımsız ivme vermesi için bütün sıradan maddede etkin hacim/kütle oranının aynı olması gerekir:

\[
\frac{V_{\rm etk}}{m}=\frac1{\rho_n}.
\tag{EA-24}
\]

Bu oran nükleon sayımıyla varsayılabilir; fakat bağlanma enerjisi, elektron katkısı, farklı çekirdek bileşimleri ve iç gerilmeler hesaba katıldığında tam evrensellik otomatik değildir. Zerre mikro-modelinin EA-24'ü türetmesi gerekir.

## 5.5 Eylemsizlik

Statik basınç kuvveti eylemsizliğin kökenini tek başına açıklamaz. Evrenakı'nın ivmelenen maddeye geri tepkisi genel olarak

\[
\mathbf F_{\rm geri}(t)=
-m_{\rm ortam}\mathbf a(t)
-\int_{-\infty}^{t}K(t-t')\mathbf a(t')dt'
+\mathbf F_{\rm yayınım}
\tag{EA-25}
\]

biçiminde olabilir. Düşük frekans sınırında gözlenen eylemsizlik için

\[
\mathbf F_{\rm geri}\simeq-m_i\mathbf a
\]

elde edilmelidir. \(m_i\)'nin EA-P5'teki pasif tepki kütlesiyle neden aynı olduğu henüz açık problemdir.

## 5.6 Korunum iddiasının sınırı

EA-20 ile tanımlanan statik test-cismi potansiyeli konservatiftir. Fakat zaman bağımlı iki-cisim sistemi için aşağıdakiler tamamlanmadan “enerji ve momentum korunur” denemez:

1. maddenin dinamik eylemi,
2. madde–\(\chi\) karşılıklı kuplajı,
3. ortamın geri tepkisi,
4. sınırdan taşınan alan enerjisi,
5. vortisiteli sektör varsa onun gerilim ve enerji terimleri.

Bu dosyanın sonucu statik çekirdeğin enerji hesabıdır; tam dinamik kuram değildir.
