import sys

source_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik\Kisim_7_Ekler_ve_Hakem_Degerlendirmeleri\10_Makro_Kutle_Geometri_Gradyanlari.md'
target_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik\Kisim_3_Makro_Evren\03_Mikrodan_Makroya_Evrenaki.md'

with open(source_path, 'r', encoding='utf-8') as f:
    source_content = f.read()

# Change the heading to 3.3.2
source_content = source_content.replace('# 3.10 Makro Kütle Geometri Gradyanları', '## 3.3.2 Makro Kütle Geometri Gradyanları', 1)

with open(target_path, 'r', encoding='utf-8') as f:
    target_content = f.read()

# Find the insertion point (</script>\n</div>)
insert_marker = "</script>\n</div>"
parts = target_content.split(insert_marker)

if len(parts) >= 2:
    # We want to insert after the first occurrence of the marker (which is the end of Animasyon 3.3.1)
    new_content = parts[0] + insert_marker + "\n\n" + source_content + "\n" + insert_marker.join(parts[1:])
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Content successfully inserted into Kisim 3.")
    
    # Empty the source file to indicate it's been moved (or we could just leave it)
    with open(source_path, 'w', encoding='utf-8') as f:
        f.write("> Bu dosyanın içeriği 'Kısım 3: Mikrodan Makroya Evrenakı' bölümüne (Animasyon 3.3.1 sonrası) taşınmıştır.\n")
    print("Source file replaced with a forwarding note.")
else:
    print("Error: Could not find insertion marker.")

