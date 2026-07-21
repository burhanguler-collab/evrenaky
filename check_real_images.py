import os
import re

websitesi_dir = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi'
gorseller_dir = os.path.join(websitesi_dir, 'Gorseller')
available_images = os.listdir(gorseller_dir)

print(f"Total images in Gorseller: {len(available_images)}")

def check_files():
    broken = []
    for root, dirs, files in os.walk(websitesi_dir):
        for f in files:
            if f.endswith('.md'):
                file_path = os.path.join(root, f)
                content = open(file_path, 'r', encoding='utf-8').read()
                
                # find all src="XXX"
                srcs = re.findall(r'src=["\']([^"\']+)["\']', content)
                for src in srcs:
                    if src.startswith('http') or src.startswith('data:'): continue
                    
                    basename = os.path.basename(src)
                    if basename not in available_images:
                        broken.append(f"{f} -> {src}")
    return broken

b = check_files()
if b:
    print("REALLY MISSING IMAGES (Not even in Gorseller folder):")
    for x in b:
        print(x)
else:
    print("ALL images referenced exist in the Gorseller folder, just path issues.")
