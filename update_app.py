import os

path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\app.js'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    "{ id: 'akademik_08', title: 'Kısım VIII: Ekler ve Hakem Değerlendirmeleri', file: 'Metin/Akademik/Kisim_8_Ekler_ve_Hakem_Degerlendirmeleri/07_Ekler.md', group: 'akademik', part: 'Kısım VIII: Ekler ve Hakem Değerlendirmeleri' },",
    "{ id: 'akademik_08', title: 'Kısım VIII: Matematiksel Ekler', file: 'Metin/Akademik/Kisim_8_Ekler/07_Matematiksel_Ekler.md', group: 'akademik', part: 'Kısım VIII: Matematiksel Ekler' },\n    { id: 'akademik_09', title: '9.1 Prof. Dr. Rıza Demirbilek Değerlendirmesi', file: 'Metin/Akademik/Kisim_9_Hakem_Degerlendirmeleri/01_Prof_Riza_Demirbilek_Degerlendirmesi.md', group: 'akademik', part: 'Kısım IX: Hakem Değerlendirmeleri ve Tartışmalar' },\n    { id: 'akademik_09_02', title: '9.2 Önceki Değerlendirmeler ve Tartışmalar', file: 'Metin/Akademik/Kisim_9_Hakem_Degerlendirmeleri/08_Hakem_Degerlendirmeleri.md', group: 'akademik', part: 'Kısım IX: Hakem Değerlendirmeleri ve Tartışmalar' },"
)

content = content.replace(
    "if (chapter.id === 'akademik_08' || chapter.id === 'duzeltme') {",
    "if (chapter.id.startsWith('akademik_09') || chapter.id === 'duzeltme') {"
)

content = content.replace(
    "if (activeChapterId === 'akademik_08') {",
    "if (activeChapterId && activeChapterId.startsWith('akademik_09')) {"
)

content = content.replace(
    "if (activeChapterId === 'akademik_08' || activeChapterId === 'duzeltme') {",
    "if ((activeChapterId && activeChapterId.startsWith('akademik_09')) || activeChapterId === 'duzeltme') {"
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('app.js updated')
