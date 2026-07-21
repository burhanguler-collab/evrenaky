import os
import re

app_js_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\app.js'
base_dir = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi'

with open(app_js_path, 'r', encoding='utf-8') as f:
    app_js_content = f.read()

# Extract all file mappings
pattern = r"file:\s*'([^']+)'"
matches = re.finditer(pattern, app_js_content)

missing_files = []
for m in matches:
    rel_path = m.group(1)
    abs_path = os.path.join(base_dir, rel_path.replace('/', '\\'))
    if not os.path.exists(abs_path):
        missing_files.append(rel_path)

print(f"Total missing files: {len(missing_files)}")
for mf in missing_files:
    dir_path = os.path.dirname(os.path.join(base_dir, mf.replace('/', '\\')))
    if os.path.exists(dir_path):
        available = [f for f in os.listdir(dir_path) if f.endswith('.md')]
        print(f"MISSING: {mf}")
        print(f"  AVAILABLE in dir: {available}")
    else:
        print(f"MISSING DIR: {mf}")
