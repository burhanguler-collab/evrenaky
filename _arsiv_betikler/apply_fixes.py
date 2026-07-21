import re

file_path = r"c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik\Kisim_3_Makro_Evren\01_Evrenin_Makine_Dairesi.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update old 29.x references to Kisim 1.4
content = content.replace("epür analizlerinde (29.1–29.7)", "epür analizlerinde (Kısım 1.4)")
content = content.replace("Epür analizinde (29.5)", "Epür analizinde (Kısım 1.4)")
content = content.replace("Bölüm 29'da kurulan Makro-Vorteks", "Bu bölümde kurulan Makro-Vorteks")
content = content.replace("29.14'te önerilen", "Bölüm 3.1.7'de önerilen")

# 2. Delete 3.1.9 to 3.1.11
# We will find the index of "### 3.1.9 Zitterbewegung'un Geometrik Sırrı" and cut everything after it (including the header).
split_marker = "### 3.1.9 Zitterbewegung'un Geometrik Sırrı"
if split_marker in content:
    content = content.split(split_marker)[0].strip() + "\n"

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Modifications applied successfully!")
