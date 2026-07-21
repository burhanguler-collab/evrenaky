import os

path_app = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\app.js'
with open(path_app, 'r', encoding='utf-8') as f:
    app_js = f.read()

# Fix the parts in app.js
app_js = app_js.replace(
    "part: 'Kısım VIII: Matematiksel Ekler'",
    "part: 'Kısım VIII: Ekler'"
).replace(
    "title: 'Kısım VIII: Matematiksel Ekler'",
    "title: 'Kısım VIII: Ekler'"
).replace(
    "part: 'Kısım IX: Hakem Değerlendirmeleri ve Tartışmalar'",
    "part: 'Kısım IX: Hakem Değerlendirmeleri'"
)

with open(path_app, 'w', encoding='utf-8') as f:
    f.write(app_js)

# Update service worker cache
path_sw = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\service-worker.js'
with open(path_sw, 'r', encoding='utf-8') as f:
    sw_js = f.read()

import re
sw_js = re.sub(r"const CACHE_NAME = 'project-cache-.*?';", "const CACHE_NAME = 'project-cache-20260719-1118';", sw_js)

with open(path_sw, 'w', encoding='utf-8') as f:
    f.write(sw_js)

print("Updated app.js and service-worker.js")
