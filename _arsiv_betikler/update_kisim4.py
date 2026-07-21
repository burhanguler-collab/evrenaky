import re

# Update app.js
app_js_path = r"C:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\app.js"
with open(app_js_path, "r", encoding="utf-8") as f:
    app_content = f.read()

app_replacement = """    { id: 'akademik_04_01', title: '4.1 Bilimin Tekilliği: Mikro ve Makronun Matematiksel Birleşimi', file: 'Metin/Akademik/Kisim_4_Bilimin_Tekilligi/01_Bilimin_Tekilligi.md', group: 'akademik', part: 'Kısım IV: Bilimin Tekilliği' },
    { id: 'akademik_04_02', title: '4.2 Evrenakı\\'nın Evrensel Sabitleri ve Kütle-İtim Derivasyonu', file: 'Metin/Akademik/Kisim_4_Bilimin_Tekilligi/02_Evrensel_Sabitler_ve_Derivasyonlar.md', group: 'akademik', part: 'Kısım IV: Bilimin Tekilliği' },
    { id: 'akademik_04_03', title: '4.3 Kütleçekimsel Merceklenme: Optik ve Kütlenin Tekilliği', file: 'Metin/Akademik/Kisim_4_Bilimin_Tekilligi/03_Kutlecekimsel_Merceklenme.md', group: 'akademik', part: 'Kısım IV: Bilimin Tekilliği' },
    { id: 'akademik_04_04', title: '4.4 Kısım Özeti: Ne Öğrendik?', file: 'Metin/Akademik/Kisim_4_Bilimin_Tekilligi/04_Ne_Ogrendik.md', group: 'akademik', part: 'Kısım IV: Bilimin Tekilliği' },"""

# The original block in app.js looks like:
# { id: 'akademik_04_01', ...
# { id: 'akademik_04_02', ...
# { id: 'akademik_04_03', ...

old_pattern = r"\{\s*id:\s*'akademik_04_01'.*?\n\s*\{\s*id:\s*'akademik_04_02'.*?\n\s*\{\s*id:\s*'akademik_04_03'.*?\n"
app_content = re.sub(old_pattern, app_replacement + "\n", app_content, flags=re.MULTILINE)

with open(app_js_path, "w", encoding="utf-8") as f:
    f.write(app_content)

# Update Markdown headers
file_01 = r"C:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik\Kisim_4_Bilimin_Tekilligi\01_Bilimin_Tekilligi.md"
file_03 = r"C:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik\Kisim_4_Bilimin_Tekilligi\03_Kutlecekimsel_Merceklenme.md"
file_04 = r"C:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik\Kisim_4_Bilimin_Tekilligi\04_Ne_Ogrendik.md"

def update_header(file_path, new_header):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    # Replace the first line if it's a header
    content = re.sub(r"^#.*", new_header, content, count=1)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

update_header(file_01, "# 4.1 Bilimin Tekilliği: Mikro ve Makronun Matematiksel Birleşimi")
update_header(file_03, "# 4.3 Kütleçekimsel Merceklenme: Optik ve Kütlenin Tekilliği")
update_header(file_04, "# 4.4 Kısım Özeti: Ne Öğrendik?")

print("App.js and markdown titles updated.")
