import os

source_file = r"c:\Users\ASUS\Desktop\EvrenAKI\KITAPA\websitesi\Metin\bolum_29.md"
target_file = r"c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik\Kisim_3_Makro_Evren\01_Nukleon_ve_Zitterbewegung.md"
app_js_file = r"c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\app.js"

with open(source_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if "Mikrodan Makroya Geçiş: Sorunun Cevabı" in line or "Mikrodan Makroya Ge" in line and "Sorunun" in line:
        start_idx = i
    if "## Kaynakça" in line or "## Kaynak" in line:
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    extracted_lines = lines[start_idx:end_idx]
    extracted_text = "".join(extracted_lines)
    
    with open(target_file, 'r', encoding='utf-8') as f:
        target_content = f.read()
    
    # Remove the old title from target
    # Old title was probably `# 3.1 Nükleon Dinamikleri ve Zitterbewegung`
    import re
    # Strip the very first line if it's the title
    target_lines = target_content.split('\n')
    if target_lines[0].startswith('# '):
        target_lines = target_lines[1:]
    rest_of_target = "\n".join(target_lines).strip()
    
    new_title = "# 3.1 Evrenin Makine Dairesi: Nükleon ve Zitterbewegung\n\n"
    
    # Wait, the extracted text already has a section title "## Mikrodan Makroya Geçi..."
    # The user said "bölümün başına koyalım", so maybe:
    # 1. New Title
    # 2. Extracted text
    # 3. Old content
    
    # We should also replace standard markdown headers inside the extracted text to match the depth if needed, 
    # but let's just insert it raw first.
    
    final_content = new_title + extracted_text + "\n\n---\n\n" + rest_of_target
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(final_content)
        
    print("Content successfully copied and prepended.")
    
    # Also update app.js title
    with open(app_js_file, 'r', encoding='utf-8') as f:
        app_js = f.read()
    
    app_js = re.sub(r"title:\s*'3\.1 Nükleon Dinamikleri ve Zitterbewegung'", "title: '3.1 Evrenin Makine Dairesi: Nükleon ve Zitterbewegung'", app_js)
    with open(app_js_file, 'w', encoding='utf-8') as f:
        f.write(app_js)
        
    print("app.js updated.")
else:
    print(f"Could not find boundaries. start: {start_idx}, end: {end_idx}")
