import sys

target_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik\Kisim_3_Makro_Evren\03_Mikrodan_Makroya_Evrenaki.md'

with open(target_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '3.10.2' in line:
        print(f"Line {i+1}: {line.strip()}")
        # Let's print the next 20 lines to see what's going on
        for j in range(1, 21):
            if i+j < len(lines):
                print(f"Line {i+j+1}: {lines[i+j].strip()}")
        break
