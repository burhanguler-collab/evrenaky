import os
import re
import json

app_js_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\app.js'
websitesi_dir = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi'
gorseller_dir = os.path.join(websitesi_dir, 'Gorseller')

# 1. Parse chapters from app.js
chapters_list = []
with open(app_js_path, 'r', encoding='utf-8') as f:
    content = f.read()
    # Find the chapters array roughly
    match = re.search(r'const chapters = \[(.*?)\];', content, re.DOTALL)
    if match:
        arr_str = match.group(1)
        # Find all 'file' properties
        files = re.findall(r"file:\s*['\"]([^'\"]+)['\"]", arr_str)
        chapters_list = files

print("=== YAYIN ÖNCESİ SON KONTROL RAPORU ===")
print(f"Toplam Bölüm Sayısı (app.js): {len(chapters_list)}")

missing_files = []
empty_files = []
broken_images = []

for rel_file in chapters_list:
    full_path = os.path.join(websitesi_dir, rel_file)
    if not os.path.exists(full_path):
        missing_files.append(rel_file)
        continue
    
    with open(full_path, 'r', encoding='utf-8') as f:
        file_content = f.read()
        
        # Check for placeholder text
        if "(Bu bölümün içeriği yakında eklenecektir...)" in file_content:
            empty_files.append(rel_file)
            
        # Check image links
        img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', file_content)
        md_img_srcs = re.findall(r'!\[.*?\]\((.*?)\)', file_content)
        all_srcs = img_srcs + md_img_srcs
        
        for src in all_srcs:
            if src.startswith('http') or src.startswith('data:'):
                continue # ignore external or base64
                
            # src is likely 'Gorseller/filename.png'
            img_path = os.path.join(websitesi_dir, src)
            if not os.path.exists(img_path):
                broken_images.append(f"{src} (bulunduğu dosya: {rel_file})")

if missing_files:
    print("\n[HATA] Bulunamayan Bölüm Dosyaları:")
    for m in missing_files:
        print("  -", m)
else:
    print("\n[BAŞARILI] Tüm bölüm dosyaları mevcut.")

if empty_files:
    print("\n[UYARI] İçi Boş Bırakılmış Bölümler (Yakında eklenecektir yazanlar):")
    for e in empty_files:
        print("  -", e)
else:
    print("\n[BAŞARILI] Tüm bölümler içerik dolu.")

if broken_images:
    print("\n[HATA] Kırık Görsel Linkleri:")
    for b in broken_images:
        print("  -", b)
else:
    print("\n[BAŞARILI] Tüm görseller sağlam ve yerinde.")

