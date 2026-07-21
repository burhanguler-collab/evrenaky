import os
import re

app_js_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\app.js'
base_dir = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi'

with open(app_js_path, 'r', encoding='utf-8') as f:
    app_js_content = f.read()

pattern = r"file:\s*'([^']+)'"
matches = list(re.finditer(pattern, app_js_content))

fixes = 0
for m in matches:
    rel_path = m.group(1)
    abs_path = os.path.join(base_dir, rel_path.replace('/', '\\'))
    
    if not os.path.exists(abs_path):
        dir_rel_path = os.path.dirname(rel_path)
        filename = os.path.basename(rel_path)
        
        dir_abs_path = os.path.dirname(abs_path)
        
        if os.path.exists(dir_abs_path):
            available_files = [f for f in os.listdir(dir_abs_path) if f.endswith('.md')]
            
            # Remove leading numbers and underscores
            suffix = re.sub(r'^\d+_', '', filename)
            
            best_match = None
            for af in available_files:
                af_suffix = re.sub(r'^\d+_', '', af)
                if af_suffix == suffix:
                    best_match = af
                    break
            
            if best_match:
                new_rel_path = f"{dir_rel_path}/{best_match}"
                # Safely replace in app_js_content
                app_js_content = app_js_content.replace(f"file: '{rel_path}'", f"file: '{new_rel_path}'")
                print(f"FIXED: {rel_path} -> {new_rel_path}")
                fixes += 1
            else:
                print(f"COULD NOT FIX: {rel_path}")

if fixes > 0:
    with open(app_js_path, 'w', encoding='utf-8') as f:
        f.write(app_js_content)
    print(f"Updated app.js with {fixes} fixes.")
else:
    print("No fixes made.")
