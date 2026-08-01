r"""ADIM 3 — a_0'IN SON SERBESTLIGI: IKI YOL DENENDI, KARSILASTIRILDI.

92_M_TUT sunu birakti:   a_0 = G m_n / l_om^2 ,  l_om = q_n/(2 gamma_n)
Tek kalan serbestlik q_n/gamma_n. Iki yol var; ikisi de burada kuruluyor.

  YOL 1 — q_n/gamma_n'yi NUKLEON YAPISINDAN turet.
  YOL 2 — MIKRO/KOZMIK kopruyu ele al: G m_n/l_om^2 =? c H_0/16,1

NOT — bu betigin cercevesi: teorinin matematik katmani (M-35/M-38/6.5.4.x) yazarin
kendi ifadesi degil, onceki bir yapay zeka turetimidir. Dolayisiyla o katmandaki
bir ifade, daha iyi bir yapiya yer acmak icin DEGISTIRILEBILIR. Asagida bir yerde
kitabin denklemine karsi cikilir ve gerekcesi verilir.

Cikti: SINIF_CALISMASI/91_A0_KOPRU/ -> a0_kopru.png
"""

import os
import sys
import warnings

import numpy as np
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
plt.style.use('dark_background')

CIK = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   'SINIF_CALISMASI', '91_A0_KOPRU')
os.makedirs(CIK, exist_ok=True)

G = 6.67430e-11
M_N = 1.67492749804e-27
C = 2.99792458e8
H0 = 70e3 / 3.0857e22
R_N = 0.8414e-15                 # proton yuk yaricapi (CODATA)
LOM = 3.568e-14                  # 92_M_TUT olcumu (35,7 fm)
A0_KITAP = C * H0 / 16.1
A0_MIKRO = G * M_N / LOM ** 2
A0_B = A0_KITAP * 1.77           # 94_YEREL_LOMEGA'nin gerektirdigi

print('=' * 100)
print('YOL 1 — q_n/gamma_n NUKLEON YAPISINDAN TURETILEBILIR MI?')
print('=' * 100)
print("""
  Nukleonu ortamda hem PULSE EDEN hem DONEN bir kaynak olarak yazalim:
      q_n     = 4 pi r_n^2 u_r      (kuresel pulsasyon debisi — omega_2 kolu)
      gamma_n = 2 pi r_n v_t        (ekvator dolanimi        — omega_1 kolu)
  Oran:
      l_om = q_n/(2 gamma_n) = r_n * (u_r/v_t)
""")
print('  Olculen l_om = %.2f fm · proton yaricapi r_n = %.3f fm' % (LOM * 1e15, R_N * 1e15))
print('  => GEREKEN HIZ ORANI  u_r/v_t = %.1f' % (LOM / R_N))
print('\n  Iki kol AYNI hizda olsaydi (u_r = v_t) l_om = r_n olurdu:')
print('    a_0 = G m_n/r_n^2 = %.2e m/s^2  — gozlenenin %.0f KATI.'
      % (G * M_N / R_N ** 2, (G * M_N / R_N ** 2) / A0_MIKRO))
print('  Yani hiz orani kacinilmazdir; soru "var mi" degil, "42 nereden".')
print("""
  TIKANIKLIK — ve yapisal:
    Sembol sozlugu q_n'yi "serbest (F) — C ile tek kalem" diye listeler. Yani
    teoride q_n ile C AYRILAMAZ; yalniz Cq_n bileskesi G ile sabitlenir.
    gamma_n icin de bagimsiz bir denklem yoktur. Iki bilinmeyen, bir denklem.
    u_r/v_t = 42,4'u uretecek IKINCI denklem teoride YOKTUR.
  Bu yol, serbestligi bir uzunluk oranindan bir HIZ oranina tasir. Yeni bir
  sinanabilir sonuc uretmez.
""")

print('=' * 100)
print('YOL 2 — MIKRO/KOZMIK KOPRU')
print('=' * 100)
print('  a_0 (mikro, olculen l_om)   = %.3e m/s^2' % A0_MIKRO)
print('  a_0 (kitap, cH_0/16,1)      = %.3e m/s^2' % A0_KITAP)
print('  a_0 (94_YEREL_LOMEGA x1,77) = %.3e m/s^2' % A0_B)
print('  cH_0                        = %.3e m/s^2' % (C * H0))
print('  cH_0/a_0^mikro = %.2f   ·   cH_0/a_0^(B) = %.2f   ·   kitap: 16,1'
      % (C * H0 / A0_MIKRO, C * H0 / A0_B))

print("""
  (A) KITABIN DENKLEMINE ITIRAZ — rho_n'in USSU
      Kitap: a_0 = c H_0 (rho_0/rho_n)^2      -> a_0 ~ rho_n^(-2)
      Kitabin kendi acik kalemi (g): "neden KARE, neden birinci kuvvet degil?
      Esleme post-hoc bir aramayla bulundu; tesaduf olasiligi %25 (1,2 sigma).
      Kitabin ilk yaziminda ana formul olarak sunulmasi bir asiri-yorumdu;
      GERI CEKILMISTIR."
      92_M_TUT'un turetimi ayni buyuklugu su hale getirir:
          a_0 = C gamma_n^2 / (pi rho_n q_n)  -> a_0 ~ rho_n^(-1)
      BIRINCI kuvvet, ve TURETILMIS. Kare gereksizdir.
""")

print('  (B) AYIRT EDICI: a_0 kozmik zamanla degisiyor mu?')
print('      kitap okumasi : a_0 ~ c H(z)  -> H ile buyur')
print('      bizim okuma   : a_0 = G m_n/l_om^2 -> hepsi mikro sabit -> DEGISMEZ')
print('      %-6s %10s %14s %16s' % ('z', 'H(z)/H_0', 'a_0 orani', 'v_duz farki'))
ZZ = [0, 0.5, 1, 2, 3]
VV = []
for z in ZZ:
    hz = np.sqrt(0.3 * (1 + z) ** 3 + 0.7)
    VV.append(hz ** 0.25)
    print('      %-6.1f %10.2f %14s %16.2f' % (z, hz, 'x%.2f / x1,00' % hz, hz ** 0.25))
print("""
      z=2'de iki okuma duz hizda %31 ayrisiyor — bugunku gozlemlerle
      SINANABILIR bir fark. Yuksek-z disklerinin dis kollari DUSER
      (Genzel+2017, Lang+2017, Ubler+2018) ve baryon-baskindir; bu, a_0'in
      YUKSELDIGI okumaya karsi, SABIT kaldigi okumaya yakindir.
      Uyari: bu bir yon argumanidir — bu calismada yuksek-z verisi ISLENMEDI.
""")

print('=' * 100)
print('KARSILASTIRMA')
print('=' * 100)
OL = [('Serbestligi azaltiyor mu?', 'HAYIR — uzunluktan hiza tasiyor', 'HAYIR — ama yerini aciklyor'),
      ('Yeni sinanabilir sonuc?', 'yok', 'EVET — a_0(z) sabit mi degisken mi'),
      ('Kitabin bir denklemini duzeltir mi?', 'hayir', 'EVET — rho_n ussu: kare -> birinci'),
      ('Teori icinde ikinci denklem var mi?', 'YOK (q_n ~ C ile dejenere)', 'gerekmiyor'),
      ('Bugun ilerletebilir miyiz?', 'hayir', 'evet')]
print('  %-38s %-32s %s' % ('olcut', 'YOL 1', 'YOL 2'))
for a, b, c_ in OL:
    print('  %-38s %-32s %s' % (a, b, c_))

# ------------------------------------------------------------------ grafik
fig, ax = plt.subplots(1, 3, figsize=(16.4, 5.4), facecolor='#121212')
for a in ax:
    a.set_facecolor('#121212'); a.grid(alpha=.13)

a = ax[0]
et = ['$r_n$\nproton\nyarıçapı', '$\\ell_\\omega$\nölçülen', 'gereken\n$u_r/v_t$']
vv = [R_N * 1e15, LOM * 1e15, LOM / R_N]
cl = ['#7c3aed', '#16a34a', '#ffcc00']
a.bar(range(3), vv, .6, color=cl)
for i, v in enumerate(vv):
    a.text(i, v * 1.25, ('%.2f' % v if v < 5 else '%.0f' % v).replace('.', ','),
           ha='center', fontsize=11, color=cl[i], fontweight='bold')
a.set_yscale('log'); a.set_ylim(0.3, 900)
a.set_xticks(range(3)); a.set_xticklabels(et, fontsize=8.8)
a.set_ylabel('fm  ·  (son sütun boyutsuz)', fontsize=10)
a.set_title('YOL 1 — nükleon yapısı', fontsize=12.4, color='white', pad=8)
a.text(.5, .95, ('$\\ell_\\omega=r_n\\,(u_r/v_t)$\n\niki kol aynı hızda olsaydı\n'
                 '$a_0$ %.0f kat büyük olurdu' % ((G * M_N / R_N ** 2) / A0_MIKRO)),
       transform=a.transAxes, ha='right', va='top', fontsize=8.8, color='#a1a1aa')

a = ax[1]
et2 = ['mikro\n$\\mathcal{G}m_n/\\ell_\\omega^2$', 'ölçümün\nistediği (B)',
       'kitap\n$cH_0/16{,}1$', '$cH_0$']
vv2 = [A0_MIKRO, A0_B, A0_KITAP, C * H0]
cl2 = ['#16a34a', '#ffcc00', '#7c3aed', '#f87171']
a.bar(range(4), vv2, .6, color=cl2)
for i, v in enumerate(vv2):
    a.text(i, v * 1.15, '%.1f' % (v * 1e11), ha='center', fontsize=10.4,
           color=cl2[i], fontweight='bold')
a.set_yscale('log')
a.set_xticks(range(4)); a.set_xticklabels(et2, fontsize=8.6)
a.set_ylabel('$a_0$   ($10^{-11}$ m/s², etiketler)', fontsize=10)
a.set_title('YOL 2 — $a_0$ okumaları', fontsize=12.4, color='white', pad=8)
a.text(.5, .90, ('$cH_0/a_0^{mikro}=%.2f$ · kitap 16,1' % (C * H0 / A0_MIKRO)).replace('.', ','),
       transform=a.transAxes, ha='center', fontsize=9.2, color='#fbbf24')

a = ax[2]
zz = np.linspace(0, 3, 60)
hz = np.sqrt(0.3 * (1 + zz) ** 3 + 0.7)
a.plot(zz, hz ** 0.25, '-', color='#7c3aed', lw=2.6, label='kitap: $a_0\\propto cH(z)$')
a.plot(zz, np.ones_like(zz), '-', color='#16a34a', lw=2.6,
       label='bizim: $a_0=\\mathcal{G}m_n/\\ell_\\omega^2$ sabit')
a.fill_between(zz, 1, hz ** 0.25, color='#ffcc00', alpha=.14)
a.annotate('$z=2$\'de\n%31 fark', (2, (np.sqrt(0.3 * 27 + 0.7)) ** 0.25),
           xytext=(1.15, 1.24), fontsize=9.6, color='#fbbf24',
           arrowprops=dict(arrowstyle='->', color='#fbbf24'))
a.set_xlabel('kırmızıya kayma $z$', fontsize=10.5)
a.set_ylabel('$v_{düz}$ oranı (aynı $M_{bar}$)', fontsize=10.5)
a.set_title('AYIRT EDİCİ — yüksek $z$ dönüş eğrileri', fontsize=12.4, color='white', pad=8)
a.legend(fontsize=9, framealpha=.3, loc='upper left')

fig.suptitle('$a_0$\'ın son serbestliği — iki yol denendi', fontsize=14.6,
             color='white', y=.975)
fig.text(.5, .035, 'YOL 1 serbestliği uzunluk oranından hız oranına taşır ($u_r/v_t=42{,}4$) '
                   'ama teoride ikinci denklem yok ($q_n$ ile $C$ dejenere) — TIKALI.',
         ha='center', fontsize=9.4, color='#a1a1aa')
fig.text(.5, .008, 'YOL 2 kitabın $\\rho_n$ üssünü düzeltir (kare → birinci kuvvet, türetilmiş) '
                   've yanlışlanabilir bir öngörü doğurur: $a_0$ kozmik zamanla değişmez.',
         ha='center', fontsize=9.4, color='#a1a1aa')
fig.subplots_adjust(left=.055, right=.986, top=.855, bottom=.185, wspace=.26)
plt.savefig(os.path.join(CIK, 'a0_kopru.png'), dpi=140,
            facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print('\n-> 91_A0_KOPRU/  a0_kopru.png')
