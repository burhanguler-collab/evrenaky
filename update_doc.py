import os
import re

path_app = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\app.js'
with open(path_app, 'r', encoding='utf-8') as f:
    app_js = f.read()

# Replace file path and title
app_js = app_js.replace('01_Prof_Riza_Demirbilek_Degerlendirmesi.md', '01_Doc_Dr_Riza_Demirbilek_Degerlendirmesi.md')
app_js = app_js.replace('9.1 Prof. Dr. Rıza Demirbilek Değerlendirmesi', '9.1 Doç. Dr. Rıza Demirbilek Değerlendirmesi')

with open(path_app, 'w', encoding='utf-8') as f:
    f.write(app_js)

path_sw = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\service-worker.js'
with open(path_sw, 'r', encoding='utf-8') as f:
    sw_js = f.read()

sw_js = re.sub(r"const CACHE_NAME = 'project-cache-.*?';", "const CACHE_NAME = 'project-cache-20260719-1426';", sw_js)

with open(path_sw, 'w', encoding='utf-8') as f:
    f.write(sw_js)

print('app.js and service-worker.js updated')
