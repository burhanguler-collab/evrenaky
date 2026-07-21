import os
import re
import json

dir_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik\Kisim_3_Makro_Evren'
app_js_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\app.js'
file_2_4 = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik\Kisim_2_Mikro_Evren\04_Mikro_Makro_Evren_Tekilligi.md'

# 1. Revert 04_Mikro_Makro_Evren_Tekilligi.md
with open(file_2_4, 'r', encoding='utf-8') as f:
    content_2_4 = f.read()

split_marker = '## 2.4.3 Mikro ve Makro Evren Tekilliği'
if split_marker in content_2_4:
    _, orig_2_4 = content_2_4.split(split_marker, 1)
    orig_2_4 = split_marker + orig_2_4
    
    orig_2_4 = orig_2_4.replace('## 2.4.3 Mikro ve Makro Evren Tekilliği', '# 2.4 Mikro ve Makro Evren Tekilliği')
    orig_2_4 = orig_2_4.replace('### 2.4.3.1', '## 2.4.1')
    orig_2_4 = orig_2_4.replace('Animasyon 2.4.3.1', 'Animasyon 2.4.1')
    
    with open(file_2_4, 'w', encoding='utf-8') as f:
        f.write(orig_2_4.strip() + '\n')

# 2. Revert Kisim 3 files
files_to_revert = [
    '11_Ne_Ogrendik.md',
    '10_Saturn_Halka_Dinamigi.md',
    '09_Ayin_Gizemleri.md',
    '08_Karadelikler.md',
    '07_Kutlecekimsel_Dalgalar.md',
    '06_Kozmolojik_Genisleme.md',
    '05_Atmosferik_Hareketler.md',
    '04_Hortum_Dinamikleri.md',
    '03_Kutle_Itim_Mekanizmasi.md'
]

for filename in files_to_revert:
    current_num = int(filename[:2])
    old_num = current_num + 1
    
    old_prefix = f"{current_num:02d}"
    new_prefix = f"{old_num:02d}"
    
    new_filename = filename.replace(f"{old_prefix}_", f"{new_prefix}_")
    
    current_path = os.path.join(dir_path, filename)
    new_path = os.path.join(dir_path, new_filename)
    
    if os.path.exists(current_path):
        with open(current_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = re.sub(rf"(#+ )3\.{current_num}\b", rf"\g<1>3.{old_num}", content)
        content = re.sub(rf"Animasyon 3\.{current_num}\b", rf"Animasyon 3.{old_num}", content)
        
        with open(new_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        os.remove(current_path)

# 3. Revert app.js
with open(app_js_path, 'r', encoding='utf-8') as f:
    app_js_content = f.read()

for current_num in range(11, 2, -1):
    old_num = current_num + 1
    old_prefix = f"{current_num:02d}"
    new_prefix = f"{old_num:02d}"
    
    app_js_content = app_js_content.replace(f"akademik_03_{old_prefix}", f"akademik_03_{new_prefix}")
    app_js_content = app_js_content.replace(f"title: '3.{current_num} ", f"title: '3.{old_num} ")
    app_js_content = app_js_content.replace(f"title: \"3.{current_num} ", f"title: \"3.{old_num} ")
    app_js_content = app_js_content.replace(f"/{old_prefix}_", f"/{new_prefix}_")

insert_idx = app_js_content.find("akademik_03_04")
if insert_idx != -1:
    line_start = app_js_content.rfind('\n', 0, insert_idx)
    new_line = "    { id: 'akademik_03_03', title: '3.3 Mikrodan Makroya Evrenakı', file: 'Metin/Akademik/Kisim_3_Makro_Evren/03_Mikrodan_Makroya_Evrenaki.md', group: 'akademik', part: 'Kısım III: Makro Evren' },\n"
    app_js_content = app_js_content[:line_start+1] + new_line + app_js_content[line_start+1:]

app_js_content = re.sub(r"title:\s*'2\.4\s+Mikrodan Makroya Evrenakı'", "title: '2.4 Mikro ve Makro Evrenin Tekilliği'", app_js_content)

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(app_js_content)

# 4. Recover 03_Mikrodan_Makroya_Evrenaki.md from transcript
log_path = r'C:\Users\ASUS\.gemini\antigravity-ide\brain\f0440324-2db8-4b45-8aed-33c33a7243da\.system_generated\logs\transcript.jsonl'
file_03_03 = os.path.join(dir_path, '03_Mikrodan_Makroya_Evrenaki.md')
recovered = False

with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        if '03_Mikrodan_Makroya_Evrenaki.md' in line and 'Total Lines: 723' in line and 'The following code has been modified' in line:
            data = json.loads(line)
            content = data.get('content') or data.get('output', '')
            if 'output' in data: # sometimes it is nested inside tool_results
                 content = data['output']
            if not content and 'tool_calls' in data: # search nested
                 continue # It's in the next step usually
            
            # Use regex to find the content block if it's deeply nested
            match = re.search(r'The following code has been modified.*?(?=\n\w|\Z)', content, re.DOTALL)
            if not match: 
                 match = re.search(r'The following code has been modified.*', content, re.DOTALL)
            
            if match:
                 text_block = match.group(0)
                 lines = text_block.split('\n')
                 output_lines = []
                 for l in lines[1:]: # skip the "The following..." line
                     if l.startswith('The above content shows'):
                         break
                     m = re.match(r'^\d+:\s?(.*)$', l)
                     if m:
                         output_lines.append(m.group(1))
                 
                 if len(output_lines) > 700:
                     with open(file_03_03, 'w', encoding='utf-8') as out_f:
                         out_f.write('\n'.join(output_lines) + '\n')
                     recovered = True
                     break

print('Revert successful. Recovered 03_:', recovered)
