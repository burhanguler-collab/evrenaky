import os
import re

websitesi_dir = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi'

count = 0
for root, dirs, files in os.walk(websitesi_dir):
    for f in files:
        if f.endswith('.md'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
                
            new_content = content
            # Fix image paths
            new_content = new_content.replace('../Gorseller/', 'Gorseller/')
            new_content = new_content.replace('../../Gorseller/', 'Gorseller/')
            new_content = new_content.replace('../../../Gorseller/', 'Gorseller/')
            
            # Fix iframe simulasyon paths
            new_content = new_content.replace('../../../Simulasyon/', 'Simulasyon/')
            new_content = new_content.replace('../../Simulasyon/', 'Simulasyon/')
            new_content = new_content.replace('../Simulasyon/', 'Simulasyon/')
            
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                count += 1

print(f"Fixed paths in {count} markdown files.")
