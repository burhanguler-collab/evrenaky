import re

kitapa_file = r"C:\Users\ASUS\Desktop\EvrenAKI\KITAPA\websitesi\Metin\bolum_08.md"
kitap3_file = r"C:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik\Kisim_4_Bilimin_Tekilligi\02_Evrensel_Sabitler_ve_Derivasyonlar.md"

with open(kitapa_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace Main Title
content = re.sub(r"^# Bölüm 08: (.*)", r"# 4.2 \1", content)

# 2. Replace 8.x with 4.2.x in headers
def replace_headers(match):
    header_level = match.group(1)
    number_part = match.group(2)
    rest = match.group(3)
    
    parts = number_part.split('.')
    if parts[0] == '8':
        parts[0] = '4.2'
    
    new_number = '.'.join(parts)
    return f"{header_level} {new_number} {rest}"

content = re.sub(r"^(#+)\s+(8\.[0-9.]+)\s+(.*)", replace_headers, content, flags=re.MULTILINE)

# 3. Replace in-text references
content = content.replace("Daha önceki bölümlerde (Özellikle Bölüm 6 ve Bölüm 10) detaylandırıldığı üzere", "Daha önceki kısımlarda detaylandırıldığı üzere")
content = content.replace("Animasyon 8.", "Animasyon 4.2.")
content = content.replace("Bölüm 8.", "Bölüm 4.2.")
content = content.replace("Bölüm 8'de", "Bölüm 4.2'de")
content = content.replace("Bölüm 8'in", "Bölüm 4.2'nin")

# Write to KITAP3
with open(kitap3_file, "w", encoding="utf-8") as f:
    f.write(content)

# 4. Update app.js
app_js_path = r"C:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\app.js"
with open(app_js_path, "r", encoding="utf-8") as f:
    app_content = f.read()

app_content = re.sub(
    r"title:\s*'4\.2\s+[^']+'",
    r"title: '4.2 Evrenakı\\'nın Matematiksel Modeli ve Gözlemsel Karşılıkları'",
    app_content
)

with open(app_js_path, "w", encoding="utf-8") as f:
    f.write(app_content)

print("Migration completed!")
