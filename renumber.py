import os
import re

dir_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik\Kisim_3_Makro_Evren'
app_js_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\app.js'

# 1. Clean up old files
old_03 = os.path.join(dir_path, '03_Mikrodan_Makroya_Evrenaki.md')
old_04_placeholder = os.path.join(dir_path, '04_Kisim_3_Makro_Evren.md')
if os.path.exists(old_03): os.remove(old_03)
if os.path.exists(old_04_placeholder): os.remove(old_04_placeholder)

# 2. Read app.js
with open(app_js_path, 'r', encoding='utf-8') as f:
    app_js_content = f.read()

# Remove the old akademik_03_03 line completely
app_js_content = re.sub(r"[ \t]*\{\s*id:\s*'akademik_03_03'.*?\n", "", app_js_content)

# Update 2.4 title to reflect the move
app_js_content = re.sub(r"title:\s*'2\.4\s+Mikro ve Makro Evrenin Tekilliği'", "title: '2.4 Mikrodan Makroya Evrenakı'", app_js_content)
app_js_content = re.sub(r"title:\s*'2\.4\s+Mikro ve Makro Evren Tekilliği'", "title: '2.4 Mikrodan Makroya Evrenakı'", app_js_content)

files_to_shift = [
    '04_Kutle_Itim_Mekanizmasi.md',
    '05_Hortum_Dinamikleri.md',
    '06_Atmosferik_Hareketler.md',
    '07_Kozmolojik_Genisleme.md',
    '08_Kutlecekimsel_Dalgalar.md',
    '09_Karadelikler.md',
    '10_Ayin_Gizemleri.md',
    '11_Saturn_Halka_Dinamigi.md',
    '12_Ne_Ogrendik.md'
]

# 3. Rename files and update their internal headings, and update app.js references
for idx, filename in enumerate(files_to_shift):
    old_num = idx + 4
    new_num = old_num - 1
    
    old_prefix = f"{old_num:02d}"
    new_prefix = f"{new_num:02d}"
    
    new_filename = filename.replace(f"{old_prefix}_", f"{new_prefix}_")
    
    old_file_path = os.path.join(dir_path, filename)
    new_file_path = os.path.join(dir_path, new_filename)
    
    if os.path.exists(old_file_path):
        with open(old_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace internal headings 3.old_num -> 3.new_num
        content = re.sub(rf"(#+ )3\.{old_num}\b", rf"\g<1>3.{new_num}", content)
        content = re.sub(rf"Animasyon 3\.{old_num}\b", rf"Animasyon 3.{new_num}", content)
        
        with open(new_file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        os.remove(old_file_path)
    
    # Update app.js references for this chapter
    # First id: 'akademik_03_04' -> 'akademik_03_03'
    app_js_content = app_js_content.replace(f"akademik_03_{old_prefix}", f"akademik_03_{new_prefix}")
    # Then title: '3.4 -> 3.3
    app_js_content = app_js_content.replace(f"title: '3.{old_num} ", f"title: '3.{new_num} ")
    app_js_content = app_js_content.replace(f"title: \"3.{old_num} ", f"title: \"3.{new_num} ")
    # Then file: Kisim_3_Makro_Evren/04_ -> 03_
    app_js_content = app_js_content.replace(f"/{old_prefix}_", f"/{new_prefix}_")

# Save app.js
with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(app_js_content)

print('Renumbering complete.')
