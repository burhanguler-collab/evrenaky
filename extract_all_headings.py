import os
import glob
import re

base_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik'
kisimlar = ['Kisim_1_Giris', 'Kisim_2_Mikro_Evren', 'Kisim_3_Makro_Evren', 'Kisim_4_Bilimin_Tekilligi', 'Kisim_5_Felsefe', 'Kisim_6_Biyoloji', 'Kisim_7_Ekler_ve_Hakem_Degerlendirmeleri']

for kisim in kisimlar:
    kisim_path = os.path.join(base_path, kisim)
    if not os.path.exists(kisim_path):
        continue
    print(f"\n=== {kisim} ===")
    files = sorted(glob.glob(os.path.join(kisim_path, '*.md')))
    for file in files:
        filename = os.path.basename(file)
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        has_heading = False
        for i, line in enumerate(lines):
            if line.startswith('#'):
                # Extract the heading level and text
                level = len(line) - len(line.lstrip('#'))
                text = line.strip()
                # Check if it has a number pattern like 1.2 or 3.4.1
                print(f"[{filename}] {text}")
                has_heading = True
        
        if not has_heading:
            print(f"[{filename}] (No headings found)")
