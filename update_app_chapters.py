import re

with open('c:/Users/ASUS/Desktop/EvrenAKI/KITAP4 - Kopya (2)/websitesi/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

chapters_pattern = re.compile(r'const chapters = \[\s*(.*?)\s*\];', re.DOTALL)
new_chapters = """const chapters = [
    { id: 'akademik_01_01', title: '1.1 Giriş ve Metodoloji', file: 'Metin/Akademik/Kisim_1_Giris/01_Metodoloji_ve_Manifesto.md', group: 'akademik', part: 'Kısım I: Temeller ve Problemin Tespiti' },
    { id: 'akademik_01_02', title: '1.2 Klasik ve Modern Fiziğin Krizleri', file: 'Metin/Akademik/Kisim_1_Giris/02_Fizigin_Krizleri.md', group: 'akademik', part: 'Kısım I: Temeller ve Problemin Tespiti' },
    { id: 'akademik_01_03', title: '1.3 Evrenin Akışkan Doğası', file: 'Metin/Akademik/Kisim_1_Giris/03_Evrenaki_Postulasi.md', group: 'akademik', part: 'Kısım I: Temeller ve Problemin Tespiti' },
    { id: 'akademik_01_04', title: '1.4 Dördüncü Boyut ve İzdüşüm', file: 'Metin/Akademik/Kisim_1_Giris/04_Dorduncu_Boyut.md', group: 'akademik', part: 'Kısım I: Temeller ve Problemin Tespiti' },
    { id: 'akademik_01_05', title: '1.5 Evrenakı Gradyanları', file: 'Metin/Akademik/Kisim_1_Giris/05_Evrenaki_Gradyanlari.md', group: 'akademik', part: 'Kısım I: Temeller ve Problemin Tespiti' },
    { id: 'akademik_01_06', title: '1.6 Evrenakı Terminolojisi ve Temel Kavramlar', file: 'Metin/Akademik/Kisim_1_Giris/06_Evrenaki_Terminolojisi.md', group: 'akademik', part: 'Kısım I: Temeller ve Problemin Tespiti' },
    { id: 'akademik_01_07', title: '1.7 Kısım Özeti: Ne Öğrendik?', file: 'Metin/Akademik/Kisim_1_Giris/07_Ne_Ogrendik.md', group: 'akademik', part: 'Kısım I: Temeller ve Problemin Tespiti' },
    { id: 'akademik_02_01', title: '2.1 Mikro Evren Aktörleri', file: 'Metin/Akademik/Kisim_2_Mikro_Evren/01_Mikro_Evren.md', group: 'akademik', part: 'Kısım II: Mikro Evren' },
    { id: 'akademik_02_02', title: '2.2 Zerre ve Işığın Kinematiği', file: 'Metin/Akademik/Kisim_2_Mikro_Evren/02_Zerre_ve_Isik.md', group: 'akademik', part: 'Kısım II: Mikro Evren' },
    { id: 'akademik_02_03', title: '2.3 Işık Hızı ve Zerre', file: 'Metin/Akademik/Kisim_2_Mikro_Evren/03_Isik_Hizi_ve_Zerre.md', group: 'akademik', part: 'Kısım II: Mikro Evren' },
    { id: 'akademik_02_04', title: '2.4 Mikro ve Makro Evrenin Tekilliği', file: 'Metin/Akademik/Kisim_2_Mikro_Evren/04_Mikro_Makro_Evren_Tekilligi.md', group: 'akademik', part: 'Kısım II: Mikro Evren' },
    { id: 'akademik_02_05', title: '2.5 Işık Davranışlarında Tekillik: Yansıma, Kırılma, Soğurma ve Geçirme', file: 'Metin/Akademik/Kisim_2_Mikro_Evren/05_Isik_Yansima_Kirilma_Sogurma_Gecirme.md', group: 'akademik', part: 'Kısım II: Mikro Evren' },
    { id: 'akademik_02_06', title: '2.6 Michelson İnterferometresi ve Kayıpsız Girişim Mekanizması', file: 'Metin/Akademik/Kisim_2_Mikro_Evren/06_Michelson_Interferometresi_ve_Kayipsiz_Girisim.md', group: 'akademik', part: 'Kısım II: Mikro Evren' },
    { id: 'akademik_02_07', title: '2.7 Evrenakı Gradyanları ve Polarizasyon', file: 'Metin/Akademik/Kisim_2_Mikro_Evren/07_Evrenaki_Gradyanlari_ve_Polarizasyon.md', group: 'akademik', part: 'Kısım II: Mikro Evren' },
    { id: 'akademik_02_08', title: '2.8 Nükleon Dinamikleri ve Zitterbewegung', file: 'Metin/Akademik/Kisim_2_Mikro_Evren/08_Nukleon_ve_Zitterbewegung.md', group: 'akademik', part: 'Kısım II: Mikro Evren' },
    { id: 'akademik_02_09', title: '2.9 Kuantum Anomalilerinin Çözümü', file: 'Metin/Akademik/Kisim_2_Mikro_Evren/09_Kuantum_Anomalileri.md', group: 'akademik', part: 'Kısım II: Mikro Evren' },
    { id: 'akademik_02_10', title: '2.10 Kısım Özeti: Ne Öğrendik?', file: 'Metin/Akademik/Kisim_2_Mikro_Evren/10_Ne_Ogrendik.md', group: 'akademik', part: 'Kısım II: Mikro Evren' },
    { id: 'akademik_03_01', title: 'Kısım III: Makro Evren Dinamikleri', file: 'Metin/Akademik/Kisim_3_Makro_Evren/03_Kisim_3_Makro_Evren.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_02', title: '3.1 Makro Evreni Şekillendiren 5 Kuvvet', file: 'Metin/Akademik/Kisim_3_Makro_Evren/01_5_Hidrodinamik_Kuvvetin_Koku.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_03', title: '3.2 Mikrodan Makroya Evrenakı', file: 'Metin/Akademik/Kisim_3_Makro_Evren/02_Mikrodan_Makroya_Evrenaki.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_04', title: '3.3 Kütle-İtim (Push-Gravity) Mekanizması', file: 'Metin/Akademik/Kisim_3_Makro_Evren/03_Kutle_Itim_Mekanizmasi.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_05', title: '3.4 Hortum Dinamikleri ve Siklostrofik Denge', file: 'Metin/Akademik/Kisim_3_Makro_Evren/04_Hortum_Dinamikleri.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_06', title: '3.5 Atmosferik Hareketler ve Coriolis Etkisi', file: 'Metin/Akademik/Kisim_3_Makro_Evren/05_Atmosferik_Hareketler.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_07', title: '3.6 Kozmolojik Genişleme ve Karanlık Enerji Hipotezi', file: 'Metin/Akademik/Kisim_3_Makro_Evren/06_Kozmolojik_Genisleme.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_08', title: '3.7 Kütleçekimsel Dalgalar', file: 'Metin/Akademik/Kisim_3_Makro_Evren/07_Kutlecekimsel_Dalgalar.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_09', title: '3.8 Karadelikler', file: 'Metin/Akademik/Kisim_3_Makro_Evren/08_Karadelikler.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_10', title: '3.9 Makro Kütle Geometri Gradyanları', file: 'Metin/Akademik/Kisim_3_Makro_Evren/09_Makro_Kutle_Geometri_Gradyanlari.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_11', title: "3.10 Ay'ın Görmezden Gelinen Gizemleri", file: 'Metin/Akademik/Kisim_3_Makro_Evren/10_Ayin_Gizemleri.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_12', title: '3.11 Satürn Halka Dinamiği', file: 'Metin/Akademik/Kisim_3_Makro_Evren/11_Saturn_Halka_Dinamigi.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_03_13', title: '3.12 Kısım Özeti: Ne Öğrendik?', file: 'Metin/Akademik/Kisim_3_Makro_Evren/12_Ne_Ogrendik.md', group: 'akademik', part: 'Kısım III: Makro Evren' },
    { id: 'akademik_04_01', title: '4.1 Bilimin Tekilliği', file: 'Metin/Akademik/Kisim_4_Bilimin_Tekilligi/01_Bilimin_Tekilligi.md', group: 'akademik', part: 'Kısım IV: Bilimin Tekilliği' },
    { id: 'akademik_04_02', title: '4.2 Kütleçekimsel Merceklenme: Optik ve Kütlenin Tekilliği', file: 'Metin/Akademik/Kisim_4_Bilimin_Tekilligi/02_Kutlecekimsel_Merceklenme.md', group: 'akademik', part: 'Kısım IV: Bilimin Tekilliği' },
    { id: 'akademik_04_03', title: '4.3 Kısım Özeti: Ne Öğrendik?', file: 'Metin/Akademik/Kisim_4_Bilimin_Tekilligi/03_Ne_Ogrendik.md', group: 'akademik', part: 'Kısım IV: Bilimin Tekilliği' },
    { id: 'akademik_05', title: 'Kısım V: Deneyler ve Kanıtlar', file: 'Metin/Akademik/Kisim_5_Deneyler_ve_Kanitlar/05_Deneyler_ve_Kanitlar.md', group: 'akademik', part: 'Kısım V: Deneyler ve Kanıtlar' },
    { id: 'akademik_05_01', title: '5.1 Işığın Sabitsizliği', file: 'Metin/Akademik/Kisim_5_Deneyler_ve_Kanitlar/01_Isigin_Sabitsizligi.md', group: 'akademik', part: 'Kısım V: Deneyler ve Kanıtlar' },
    { id: 'akademik_05_02', title: '5.2 Kütle Dışı Evrenakı Gradyanları', file: 'Metin/Akademik/Kisim_5_Deneyler_ve_Kanitlar/02_Kutle_Disi_Evrenaki_Gradyanlari.md', group: 'akademik', part: 'Kısım V: Deneyler ve Kanıtlar' },
    { id: 'akademik_05_03', title: '5.3 Kütle İçi Evrenakı Gradyanları', file: 'Metin/Akademik/Kisim_5_Deneyler_ve_Kanitlar/03_Kutle_Ici_Evrenaki_Gradyanlari.md', group: 'akademik', part: 'Kısım V: Deneyler ve Kanıtlar' },
    { id: 'akademik_05_04', title: '5.4 Eksenel Kütle İtim', file: 'Metin/Akademik/Kisim_5_Deneyler_ve_Kanitlar/04_Eksenel_Kutle_Itim.md', group: 'akademik', part: 'Kısım V: Deneyler ve Kanıtlar' },
    { id: 'akademik_05_05', title: '5.5 Kısım Özeti: Ne Öğrendik?', file: 'Metin/Akademik/Kisim_5_Deneyler_ve_Kanitlar/05_Ne_Ogrendik.md', group: 'akademik', part: 'Kısım V: Deneyler ve Kanıtlar' },
    { id: 'akademik_06', title: 'Kısım VI: Tartışma ve Sonuç', file: 'Metin/Akademik/Kisim_6_Tartisma_ve_Sonuc/06_Tartisma_ve_Sonuc.md', group: 'akademik', part: 'Kısım VI: Tartışma ve Sonuç' },
    { id: 'akademik_07', title: 'Kısım VII: Ekler ve Hakem Değerlendirmeleri', file: 'Metin/Akademik/Kisim_7_Ekler_ve_Hakem_Degerlendirmeleri/07_Ekler.md', group: 'akademik', part: 'Kısım VII: Ekler ve Hakem Değerlendirmeleri' },
    { id: 'populer_01', title: '1. Uzay Boş Değil!', file: 'Metin/Populer/populer_01.md', group: 'populer' },
    { id: 'populer_02', title: '2. Elma Neden Düşer?', file: 'Metin/Populer/populer_02.md', group: 'populer' },
    { id: 'populer_03', title: '3. Işığın Gerçek Yüzü', file: 'Metin/Populer/populer_03.md', group: 'populer' },
    { id: 'populer_04', title: '4. Karanlık Madde Yanılgısı', file: 'Metin/Populer/populer_04.md', group: 'populer' },
    { id: 'populer_05', title: '5. Evreni Şekillendiren 5 Güç', file: 'Metin/Populer/populer_05.md', group: 'populer' },
    { id: 'eski_akademik_01', title: 'Eski: Akademik Bölüm 1', file: 'Metin/Eski_Surum/akademik_01.md', group: 'eski' },
    { id: 'eski_akademik_29', title: 'Eski: Akademik Bölüm 29', file: 'Metin/Eski_Surum/akademik_29.md', group: 'eski' },
    { id: 'duzeltme', title: 'Hakem Değerlendirmeleri', file: 'Metin/Eski_Surum/duzeltme.md', group: 'eski' }
];"""
js = chapters_pattern.sub(new_chapters, js)

with open('c:/Users/ASUS/Desktop/EvrenAKI/KITAP4 - Kopya (2)/websitesi/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("app.js updated successfully")
