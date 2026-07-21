import os
import re
import shutil

base_dir = r"c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik"
kisim2_dir = os.path.join(base_dir, "Kisim_2_Mikro_Evren")
kisim3_dir = os.path.join(base_dir, "Kisim_3_Makro_Evren")

def update_headers(filepath, old_num, new_num, prefix):
    # prefix can be '2' or '3'
    # updates # 3.x to # 3.y
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update main headers like `# 3.2` or `## 3.2.1` or `### 3.2.1`
    # Replace `<prefix>.<old_num>` with `<prefix>.<new_num>`
    # Using regex to ensure we only replace numbers that represent sections
    pattern = r"(#+\s+" + prefix + r"\.)" + str(old_num) + r"(\b)"
    new_content = re.sub(pattern, r"\g<1>" + str(new_num) + r"\g<2>", content)
    
    # Update HTML tags like `<h4>Animasyon 3.2.1...`
    pattern2 = r"(" + prefix + r"\.)" + str(old_num) + r"(\.\d+:)"
    new_content = re.sub(pattern2, r"\g<1>" + str(new_num) + r"\g<2>", new_content)

    # Note: Kisim_3_Makro_Evren index file is "03_Kisim_3_Makro_Evren.md", wait, it was originally 03.
    # Let's just blindly update the prefix numbers and see. It's safe since old_num and new_num are exact matches.
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("--- Processing Kisim 3 (Shifting +1) ---")
# List files in Kisim 3 that start with two digits
k3_files = [f for f in os.listdir(kisim3_dir) if re.match(r"^\d{2}_", f)]
k3_files.sort(reverse=True) # highest to lowest to avoid overwrite

for f in k3_files:
    match = re.match(r"^(\d{2})_(.*)$", f)
    if match:
        old_idx = int(match.group(1))
        new_idx = old_idx + 1
        new_filename = f"{new_idx:02d}_{match.group(2)}"
        
        old_path = os.path.join(kisim3_dir, f)
        new_path = os.path.join(kisim3_dir, new_filename)
        
        print(f"Renaming {f} -> {new_filename}")
        os.rename(old_path, new_path)
        update_headers(new_path, old_idx, new_idx, '3')

print("--- Moving 09 from Kisim 2 to Kisim 3 ---")
old_zitter_path = os.path.join(kisim2_dir, "09_Nukleon_ve_Zitterbewegung.md")
new_zitter_path = os.path.join(kisim3_dir, "01_Nukleon_ve_Zitterbewegung.md")
print("Moving 09_Nukleon_ve_Zitterbewegung.md -> 01_Nukleon_ve_Zitterbewegung.md")
shutil.move(old_zitter_path, new_zitter_path)
# Update headers in the moved file from 2.9 to 3.1
with open(new_zitter_path, 'r', encoding='utf-8') as f:
    content = f.read()
content = re.sub(r"(#+\s+)2\.9", r"\g<1>3.1", content)
content = re.sub(r"2\.9(\.\d+:?)", r"3.1\g<1>", content)
with open(new_zitter_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("--- Processing Kisim 2 (Shifting -1 for 10 and 11) ---")
k2_files = [f for f in os.listdir(kisim2_dir) if re.match(r"^\d{2}_", f)]
k2_files.sort() # lowest to highest for downshifting
for f in k2_files:
    match = re.match(r"^(\d{2})_(.*)$", f)
    if match:
        old_idx = int(match.group(1))
        if old_idx >= 10:
            new_idx = old_idx - 1
            new_filename = f"{new_idx:02d}_{match.group(2)}"
            old_path = os.path.join(kisim2_dir, f)
            new_path = os.path.join(kisim2_dir, new_filename)
            print(f"Renaming {f} -> {new_filename}")
            os.rename(old_path, new_path)
            update_headers(new_path, old_idx, new_idx, '2')

print("Done.")
