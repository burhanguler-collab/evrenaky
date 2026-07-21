import re

app_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\app.js'
with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_toc = '''    { id: 'akademik_05', title: 'Kısım V: Deneyler ve Kanıtlar', file: 'Metin/Akademik/Kisim_5_Deneyler_ve_Kanitlar/05_Deneyler_ve_Kanitlar.md', group: 'akademik', part: 'Kısım V: Deneyler ve Kanıtlar' },
    { id: 'akademik_05_01', title: '5.1 Işığın Sabitsizliği', file: 'Metin/Akademik/Kisim_5_Deneyler_ve_Kanitlar/01_Isigin_Sabitsizligi.md', group: 'akademik', part: 'Kısım V: Deneyler ve Kanıtlar' },
    { id: 'akademik_05_02', title: '5.2 Kütle Dışı Evrenakı Gradyanları', file: 'Metin/Akademik/Kisim_5_Deneyler_ve_Kanitlar/02_Kutle_Disi_Evrenaki_Gradyanlari.md', group: 'akademik', part: 'Kısım V: Deneyler ve Kanıtlar' },
    { id: 'akademik_05_03', title: '5.3 Kütle İçi Evrenakı Gradyanları', file: 'Metin/Akademik/Kisim_5_Deneyler_ve_Kanitlar/03_Kutle_Ici_Evrenaki_Gradyanlari.md', group: 'akademik', part: 'Kısım V: Deneyler ve Kanıtlar' },
    { id: 'akademik_05_04', title: '5.4 Eksenel Kütle İtim', file: 'Metin/Akademik/Kisim_5_Deneyler_ve_Kanitlar/04_Eksenel_Kutle_Itim.md', group: 'akademik', part: 'Kısım V: Deneyler ve Kanıtlar' },
    { id: 'akademik_05_05', title: '5.5 Kısım Özeti: Ne Öğrendik?', file: 'Metin/Akademik/Kisim_5_Deneyler_ve_Kanitlar/05_Ne_Ogrendik.md', group: 'akademik', part: 'Kısım V: Deneyler ve Kanıtlar' },
    { id: 'akademik_06', title: 'Kısım VI: Tartışma ve Sonuç', file: 'Metin/Akademik/Kisim_6_Tartisma_ve_Sonuc/06_Tartisma_ve_Sonuc.md', group: 'akademik', part: 'Kısım VI: Tartışma ve Sonuç' },
    { id: 'akademik_07', title: 'Kısım VII: Ekler ve Hakem Değerlendirmeleri', file: 'Metin/Akademik/Kisim_7_Ekler_ve_Hakem_Degerlendirmeleri/07_Ekler.md', group: 'akademik', part: 'Kısım VII: Ekler ve Hakem Değerlendirmeleri' },'''

new_toc = '''    { id: 'akademik_05', title: 'Kısım V: Deneyler', file: 'Metin/Akademik/Kisim_5_Deneyler/05_Deneyler_ve_Kanitlar.md', group: 'akademik', part: 'Kısım V: Deneyler' },
    { id: 'akademik_05_01', title: '5.1 Işığın Sabitsizliği', file: 'Metin/Akademik/Kisim_5_Deneyler/01_Isigin_Sabitsizligi.md', group: 'akademik', part: 'Kısım V: Deneyler' },
    { id: 'akademik_05_02', title: '5.2 Kütle Dışı Evrenakı Gradyanları', file: 'Metin/Akademik/Kisim_5_Deneyler/02_Kutle_Disi_Evrenaki_Gradyanlari.md', group: 'akademik', part: 'Kısım V: Deneyler' },
    { id: 'akademik_05_03', title: '5.3 Kütle İçi Evrenakı Gradyanları', file: 'Metin/Akademik/Kisim_5_Deneyler/03_Kutle_Ici_Evrenaki_Gradyanlari.md', group: 'akademik', part: 'Kısım V: Deneyler' },
    { id: 'akademik_05_04', title: '5.4 Eksenel Kütle İtim', file: 'Metin/Akademik/Kisim_5_Deneyler/04_Eksenel_Kutle_Itim.md', group: 'akademik', part: 'Kısım V: Deneyler' },
    { id: 'akademik_05_05', title: '5.5 Kısım Özeti: Ne Öğrendik?', file: 'Metin/Akademik/Kisim_5_Deneyler/05_Ne_Ogrendik.md', group: 'akademik', part: 'Kısım V: Deneyler' },
    { id: 'akademik_06', title: 'Kısım VI: Kanıtlar', file: 'Metin/Akademik/Kisim_6_Kanitlar/06_Kanitlar.md', group: 'akademik', part: 'Kısım VI: Kanıtlar' },
    { id: 'akademik_07', title: 'Kısım VII: Tartışma ve Sonuç', file: 'Metin/Akademik/Kisim_7_Tartisma_ve_Sonuc/06_Tartisma_ve_Sonuc.md', group: 'akademik', part: 'Kısım VII: Tartışma ve Sonuç' },
    { id: 'akademik_08', title: 'Kısım VIII: Ekler ve Hakem Değerlendirmeleri', file: 'Metin/Akademik/Kisim_8_Ekler_ve_Hakem_Degerlendirmeleri/07_Ekler.md', group: 'akademik', part: 'Kısım VIII: Ekler ve Hakem Değerlendirmeleri' },'''

content = content.replace(old_toc, new_toc)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("TOC updated successfully in app.js")
