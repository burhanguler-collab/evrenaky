import os
import re

base_dir = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi'

replacements = {
    "Kut'dür": "Kut'tur",
    "kut'dür": "kut'tur",
    "KUT'DÜR": "KUT'TUR",
    "Kutdür": "Kuttur",
    "kutdür": "kuttur",
    "KUTDÜR": "KUTTUR"
}

ext_to_check = {'.md', '.js', '.html', '.txt'}

def replace_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return
    
    new_content = content
    modified = False
    for old, new in replacements.items():
        if old in new_content:
            new_content = new_content.replace(old, new)
            modified = True
            
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed: {file_path}")

for root, dirs, files in os.walk(base_dir):
    for f in files:
        if any(f.endswith(ext) for ext in ext_to_check):
            if 'node_modules' in root or '.git' in root or '_arsiv' in root:
                continue
            full_path = os.path.join(root, f)
            replace_in_file(full_path)

print("Fixes Done.")
