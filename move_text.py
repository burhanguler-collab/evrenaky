import sys

source_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik\Kisim_3_Makro_Evren\03_Mikrodan_Makroya_Evrenaki.md'
target_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik\Kisim_2_Mikro_Evren\04_Mikro_Makro_Evren_Tekilligi.md'

with open(source_path, 'r', encoding='utf-8') as f:
    source_lines = f.readlines()

# Extract lines 0 to 14 (which is 1 to 15 in 1-based)
extracted_lines = source_lines[:15]
remaining_source_lines = source_lines[15:]

# Add an extra newline for separation if needed
if extracted_lines[-1].strip() != '':
    extracted_lines.append('\n\n')

with open(target_path, 'r', encoding='utf-8') as f:
    target_content = f.read()

# Prepend the extracted lines to target content
new_target_content = "".join(extracted_lines) + "\n" + target_content

with open(source_path, 'w', encoding='utf-8') as f:
    f.writelines(remaining_source_lines)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(new_target_content)

print("Successfully moved the text block from Kisim 3 to the beginning of Kisim 2 chapter 4.")
