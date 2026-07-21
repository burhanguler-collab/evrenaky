import re

file_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

script_tag = '<script type="module" src="firebase-client.js"></script>'
if script_tag not in content:
    content = content.replace('</body>', script_tag + '\n</body>')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("index.html basariyla guncellendi.")
else:
    print("index.html zaten guncellenmis.")
