import os
import shutil
import re

source_md = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\bolum_16.md'
old_dest_md = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP4\websitesi\Metin\Akademik\Kisim_4_Bilimin_Tekilligi\04_Mevcut_Fizik_Teorileriyle_Iliski.md'
new_dest_md = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP4\websitesi\Metin\Akademik\Kisim_4_Bilimin_Tekilligi\04_Michelson_Interferometresi_ve_Kayipsiz_Girisim.md'

img_src_dir = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Gorseller'
img_dest_dir = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP4\websitesi\Gorseller'

os.makedirs(img_dest_dir, exist_ok=True)

with open(source_md, 'r', encoding='utf-8') as f:
    content = f.read()

images = re.findall(r'\.\./Gorseller/([^\"\'\)]+)', content)
for img in images:
    src = os.path.join(img_src_dir, img)
    dst = os.path.join(img_dest_dir, img)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f'Copied {img}')
    else:
        print(f'Warning: {src} not found')

content = content.replace('# Bölüm 16: Michelson', '# 4.4 Michelson')
content = content.replace('## 16.', '## 4.4.')
content = content.replace('### 16.', '### 4.4.')
content = content.replace('Animasyon 16.', 'Animasyon 4.4.')
content = content.replace('Şekil 16.', 'Şekil 4.4.')

with open(new_dest_md, 'w', encoding='utf-8') as f:
    f.write(content)

if os.path.exists(old_dest_md):
    os.remove(old_dest_md)

app_update_script = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP4\websitesi\update_app_chapters.py'
with open(app_update_script, 'r', encoding='utf-8') as f:
    app_code = f.read()

app_code = app_code.replace(
    "{ id: 'akademik_04_04', title: '4.4 Mevcut Fizik Teorileriyle Epistemolojik İlişki', file: 'Metin/Akademik/Kisim_4_Bilimin_Tekilligi/04_Mevcut_Fizik_Teorileriyle_Iliski.md', group: 'akademik', part: 'Kısım IV: Bilimin Tekilliği' },",
    "{ id: 'akademik_04_04', title: '4.4 Michelson İnterferometresi ve Kayıpsız Girişim Mekanizması', file: 'Metin/Akademik/Kisim_4_Bilimin_Tekilligi/04_Michelson_Interferometresi_ve_Kayipsiz_Girisim.md', group: 'akademik', part: 'Kısım IV: Bilimin Tekilliği' },"
)

with open(app_update_script, 'w', encoding='utf-8') as f:
    f.write(app_code)

print('Markdown and script updated.')
