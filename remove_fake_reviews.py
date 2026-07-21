import os

path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\app.js'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    "if (chapter.id.startsWith('akademik_09') || chapter.id === 'duzeltme') {",
    "if (chapter.id === 'duzeltme') {"
)

content = content.replace(
    "if (activeChapterId && activeChapterId.startsWith('akademik_09')) {",
    "if (false) {"
)

content = content.replace(
    "if ((activeChapterId && activeChapterId.startsWith('akademik_09')) || activeChapterId === 'duzeltme') {",
    "if (activeChapterId === 'duzeltme') {"
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

path_sw = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\service-worker.js'
with open(path_sw, 'r', encoding='utf-8') as f:
    sw_js = f.read()

import re
sw_js = re.sub(r"const CACHE_NAME = 'project-cache-.*?';", "const CACHE_NAME = 'project-cache-20260719-1132';", sw_js)

with open(path_sw, 'w', encoding='utf-8') as f:
    f.write(sw_js)

print('app.js and service-worker.js updated')
