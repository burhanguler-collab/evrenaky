import os
import glob

base_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik'
kisimlar = ['Kisim_1_Giris', 'Kisim_2_Mikro_Evren', 'Kisim_3_Makro_Evren', 'Kisim_4_Bilimin_Tekilligi']

for kisim in kisimlar:
    print(f"\n=== {kisim} ===")
    files = sorted(glob.glob(os.path.join(base_path, kisim, '*.md')))
    for file in files:
        filename = os.path.basename(file)
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        title = "No Title"
        for line in lines:
            if line.startswith('#'):
                title = line.strip()
                break
        print(f"{filename}: {title}")
