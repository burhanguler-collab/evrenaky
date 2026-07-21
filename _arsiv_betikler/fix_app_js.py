import re

app_js_path = r"C:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\app.js"
with open(app_js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# We will replace the block from 'akademik_02_08' to 'akademik_03_13' with the newly ordered block.
new_block = """    { id: 'akademik_02_08', title: '2.8 Evrenakı Gradyanları ve Polarizasyon', file: 'Metin/Akademik/Kisim_2_Mikro_Evren/08_Evrenaki_Gradyanlari_ve_Polarizasyon.md', group: 'akademik', part: 'Kısım II: Mikro Evren' },
    { id: 'akademik_02_09', title: '2.9 Kuantum Anomalilerinin Çözümü', file: 'Metin/Akademik/Kisim_2_Mikro_Evren/09_Kuantum_Anomalileri.md', group: 'akademik', part: 'Kısım II: Mikro Evren' },
    { id: 'akademik_02_10', title: '2.10 Kısım Özeti: Ne Öğrendik?', file: 'Metin/Akademik/Kisim_2_Mikro_Evren/10_Ne_Ogrendik.md', group: 'akademik', part: 'Kısım II: Mikro Evren' },
    { id: 'akademik_03_01', title: '3.1 Nükleon Dinamikleri ve Zitterbewegung', file: 'Metin/Akademik/Kisim_3_Makro_Evren/01_Nukleon_ve_Zitterbewegung.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_02', title: '3.2 Makro Evreni Şekillendiren 5 Kuvvet', file: 'Metin/Akademik/Kisim_3_Makro_Evren/02_5_Hidrodinamik_Kuvvetin_Koku.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_03', title: '3.3 Mikrodan Makroya Evrenakı', file: 'Metin/Akademik/Kisim_3_Makro_Evren/03_Mikrodan_Makroya_Evrenaki.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_04', title: '3.4 Kütle-İtim (Push-Gravity) Mekanizması', file: 'Metin/Akademik/Kisim_3_Makro_Evren/04_Kutle_Itim_Mekanizmasi.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_05', title: '3.5 Hortum Dinamikleri ve Siklostrofik Denge', file: 'Metin/Akademik/Kisim_3_Makro_Evren/05_Hortum_Dinamikleri.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_06', title: '3.6 Atmosferik Hareketler ve Coriolis Etkisi', file: 'Metin/Akademik/Kisim_3_Makro_Evren/06_Atmosferik_Hareketler.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_07', title: '3.7 Kozmolojik Genişleme ve Karanlık Enerji Hipotezi', file: 'Metin/Akademik/Kisim_3_Makro_Evren/07_Kozmolojik_Genisleme.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_08', title: '3.8 Kütleçekimsel Dalgalar', file: 'Metin/Akademik/Kisim_3_Makro_Evren/08_Kutlecekimsel_Dalgalar.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_09', title: '3.9 Karadelikler', file: 'Metin/Akademik/Kisim_3_Makro_Evren/09_Karadelikler.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_10', title: '3.10 Makro Kütle Geometri Gradyanları', file: 'Metin/Akademik/Kisim_3_Makro_Evren/10_Makro_Kutle_Geometri_Gradyanlari.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_11', title: "3.11 Ay'ın Görmezden Gelinen Gizemleri", file: 'Metin/Akademik/Kisim_3_Makro_Evren/11_Ayin_Gizemleri.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_12', title: '3.12 Satürn Halka Dinamiği', file: 'Metin/Akademik/Kisim_3_Makro_Evren/12_Saturn_Halka_Dinamigi.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_13', title: '3.13 Kısım Özeti: Ne Öğrendik?', file: 'Metin/Akademik/Kisim_3_Makro_Evren/13_Ne_Ogrendik.md', group: 'akademik', part: 'Kısım III: Makro Evren' }"""

pattern = re.compile(r"\{\s*id:\s*'akademik_02_08'.*?\{\s*id:\s*'akademik_03_13'.*?\},", re.DOTALL)
js = pattern.sub(new_block + ',', js)

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("app.js successfully updated with new Kisim 2 and Kisim 3 structures.")
