import os

base_dir = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP4\websitesi\Metin\Akademik'
chapters_to_create = [
    (r'Kisim_1_Giris\07_Ne_Ogrendik.md', '# 1.7 Kısım Özeti: Ne Öğrendik?\n\n(Bu bölümün içeriği yakında eklenecektir...)'),
    (r'Kisim_2_Mikro_Evren\07_Ne_Ogrendik.md', '# 2.6 Kısım Özeti: Ne Öğrendik?\n\n(Bu bölümün içeriği yakında eklenecektir...)'),
    (r'Kisim_3_Makro_Evren\12_Ne_Ogrendik.md', '# 3.12 Kısım Özeti: Ne Öğrendik?\n\n(Bu bölümün içeriği yakında eklenecektir...)'),
    (r'Kisim_4_Bilimin_Tekilligi\07_Ne_Ogrendik.md', '# 4.7 Kısım Özeti: Ne Öğrendik?\n\n(Bu bölümün içeriği yakında eklenecektir...)'),
    (r'Kisim_5_Deneyler_ve_Kanitlar\05_Ne_Ogrendik.md', '# 5.5 Kısım Özeti: Ne Öğrendik?\n\n(Bu bölümün içeriği yakında eklenecektir...)')
]

for path, content in chapters_to_create:
    full_path = os.path.join(base_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Created {full_path}')

app_script_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP4\websitesi\update_app_chapters.py'
with open(app_script_path, 'r', encoding='utf-8') as f:
    app_code = f.read()

app_code = app_code.replace(
    "{ id: 'akademik_01_06', title: '1.6 Evrenakı Terminolojisi ve Temel Kavramlar', file: 'Metin/Akademik/Kisim_1_Giris/06_Evrenaki_Terminolojisi.md', group: 'akademik', part: 'Kısım I: Temeller ve Problemin Tespiti' },",
    "{ id: 'akademik_01_06', title: '1.6 Evrenakı Terminolojisi ve Temel Kavramlar', file: 'Metin/Akademik/Kisim_1_Giris/06_Evrenaki_Terminolojisi.md', group: 'akademik', part: 'Kısım I: Temeller ve Problemin Tespiti' },\n    { id: 'akademik_01_07', title: '1.7 Kısım Özeti: Ne Öğrendik?', file: 'Metin/Akademik/Kisim_1_Giris/07_Ne_Ogrendik.md', group: 'akademik', part: 'Kısım I: Temeller ve Problemin Tespiti' },"
)

app_code = app_code.replace(
    "{ id: 'akademik_02_06', title: '2.5 Kuantum Anomalilerinin Çözümü', file: 'Metin/Akademik/Kisim_2_Mikro_Evren/06_Kuantum_Anomalileri.md', group: 'akademik', part: 'Kısım II: Mikro Evren' },",
    "{ id: 'akademik_02_06', title: '2.5 Kuantum Anomalilerinin Çözümü', file: 'Metin/Akademik/Kisim_2_Mikro_Evren/06_Kuantum_Anomalileri.md', group: 'akademik', part: 'Kısım II: Mikro Evren' },\n    { id: 'akademik_02_07', title: '2.6 Kısım Özeti: Ne Öğrendik?', file: 'Metin/Akademik/Kisim_2_Mikro_Evren/07_Ne_Ogrendik.md', group: 'akademik', part: 'Kısım II: Mikro Evren' },"
)

app_code = app_code.replace(
    "{ id: 'akademik_03_12', title: '3.11 Satürn Halka Dinamiği', file: 'Metin/Akademik/Kisim_3_Makro_Evren/11_Saturn_Halka_Dinamigi.md', group: 'akademik', part: 'Kısım III: Makro Evren' },",
    "{ id: 'akademik_03_12', title: '3.11 Satürn Halka Dinamiği', file: 'Metin/Akademik/Kisim_3_Makro_Evren/11_Saturn_Halka_Dinamigi.md', group: 'akademik', part: 'Kısım III: Makro Evren' },\n    { id: 'akademik_03_13', title: '3.12 Kısım Özeti: Ne Öğrendik?', file: 'Metin/Akademik/Kisim_3_Makro_Evren/12_Ne_Ogrendik.md', group: 'akademik', part: 'Kısım III: Makro Evren' },"
)

app_code = app_code.replace(
    "{ id: 'akademik_04_06', title: '4.6 Kütleçekimsel Merceklenme: Optik ve Kütlenin Tekilliği', file: 'Metin/Akademik/Kisim_4_Bilimin_Tekilligi/06_Kutlecekimsel_Merceklenme.md', group: 'akademik', part: 'Kısım IV: Bilimin Tekilliği' },",
    "{ id: 'akademik_04_06', title: '4.6 Kütleçekimsel Merceklenme: Optik ve Kütlenin Tekilliği', file: 'Metin/Akademik/Kisim_4_Bilimin_Tekilligi/06_Kutlecekimsel_Merceklenme.md', group: 'akademik', part: 'Kısım IV: Bilimin Tekilliği' },\n    { id: 'akademik_04_07', title: '4.7 Kısım Özeti: Ne Öğrendik?', file: 'Metin/Akademik/Kisim_4_Bilimin_Tekilligi/07_Ne_Ogrendik.md', group: 'akademik', part: 'Kısım IV: Bilimin Tekilliği' },"
)

app_code = app_code.replace(
    "{ id: 'akademik_05_04', title: '5.4 Eksenel Kütle İtim', file: 'Metin/Akademik/Kisim_5_Deneyler_ve_Kanitlar/04_Eksenel_Kutle_Itim.md', group: 'akademik', part: 'Kısım V: Deneyler ve Kanıtlar' },",
    "{ id: 'akademik_05_04', title: '5.4 Eksenel Kütle İtim', file: 'Metin/Akademik/Kisim_5_Deneyler_ve_Kanitlar/04_Eksenel_Kutle_Itim.md', group: 'akademik', part: 'Kısım V: Deneyler ve Kanıtlar' },\n    { id: 'akademik_05_05', title: '5.5 Kısım Özeti: Ne Öğrendik?', file: 'Metin/Akademik/Kisim_5_Deneyler_ve_Kanitlar/05_Ne_Ogrendik.md', group: 'akademik', part: 'Kısım V: Deneyler ve Kanıtlar' },"
)

with open(app_script_path, 'w', encoding='utf-8') as f:
    f.write(app_code)

print('Updated update_app_chapters.py successfully.')
