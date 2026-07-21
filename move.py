import os
import re

file_3_3 = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik\Kisim_3_Makro_Evren\03_Mikrodan_Makroya_Evrenaki.md'
file_2_4 = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik\Kisim_2_Mikro_Evren\04_Mikro_Makro_Evren_Tekilligi.md'

with open(file_3_3, 'r', encoding='utf-8') as f:
    content_3_3 = f.read()

split_marker = '# Bölüm 26:'
if split_marker in content_3_3:
    part_3_3, part_leftover = content_3_3.split(split_marker, 1)
    part_leftover = split_marker + part_leftover
else:
    part_3_3 = content_3_3
    part_leftover = ''

# Renumber part_3_3
part_3_3 = part_3_3.replace('# 3.3 Mikrodan Makroya Evrenakı', '# 2.4 Mikrodan Makroya Evrenakı')
part_3_3 = part_3_3.replace('## 3.3.1 Makro Kütle Evrenakı Merkezcil Gradyanları', '## 2.4.1 Makro Kütle Evrenakı Merkezcil Gradyanları')
part_3_3 = part_3_3.replace('## 3.3.4 Makro Kütle Işık Davranışları', '## 2.4.2 Makro Kütle Işık Davranışları')
part_3_3 = part_3_3.replace('### 3.3.4.1 Makro Kütle Evrenakı Gradyanları', '### 2.4.2.1 Makro Kütle Evrenakı Gradyanları')
part_3_3 = part_3_3.replace('Animasyon 3.3.1', 'Animasyon 2.4.1a') # avoid clash with existing 2.4.1

with open(file_2_4, 'r', encoding='utf-8') as f:
    content_2_4 = f.read()

# Renumber existing 2.4
content_2_4 = content_2_4.replace('# 2.4 Mikro ve Makro Evren Tekilliği', '## 2.4.3 Mikro ve Makro Evren Tekilliği')
content_2_4 = content_2_4.replace('## 2.4.1', '### 2.4.3.1')
content_2_4 = content_2_4.replace('Animasyon 2.4.1', 'Animasyon 2.4.3.1')

combined = part_3_3.strip() + '\n\n\n' + content_2_4.strip() + '\n'

with open(file_2_4, 'w', encoding='utf-8') as f:
    f.write(combined)

with open(file_3_3, 'w', encoding='utf-8') as f:
    f.write(part_leftover.strip() + '\n')

print('Move successful.')
