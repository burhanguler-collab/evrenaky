import sys

target_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik\Kisim_3_Makro_Evren\03_Mikrodan_Makroya_Evrenaki.md'

with open(target_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Line 712 in 1-based is index 711. Line 1239 in 1-based is index 1238.
# We want to remove from index 711 to index 1237 (inclusive).
start_idx = 711
end_idx = 1238 # Exclusive, so it deletes up to line 1238 in 1-based, leaving line 1239 intact.

if lines[start_idx].startswith('## 3.3.3') and lines[end_idx].startswith('## 3.3.4'):
    new_lines = lines[:start_idx] + lines[end_idx:]
    with open(target_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"Successfully deleted {end_idx - start_idx} lines.")
else:
    print(f"Error: Indices do not match expected headings.")
    print(f"Line {start_idx + 1}: {lines[start_idx].strip()}")
    print(f"Line {end_idx + 1}: {lines[end_idx].strip()}")
