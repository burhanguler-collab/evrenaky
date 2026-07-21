import os
import re

base_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik'

# Fix 1: Kisim 2 - 05
f1_path = os.path.join(base_path, 'Kisim_2_Mikro_Evren', '05_Isik_Yansima_Kirilma_Sogurma_Gecirme.md')
with open(f1_path, 'r', encoding='utf-8') as f:
    text = f.read()
text = re.sub(r'# Bölüm 2\.5: Işık Davranışları \(Yansıma, Kırılma, Geçirme\)', r'# 2.5 Işık Davranışları (Yansıma, Kırılma, Geçirme)', text)
with open(f1_path, 'w', encoding='utf-8') as f:
    f.write(text)

# Fix 2: Kisim 3 - 02
f2_path = os.path.join(base_path, 'Kisim_3_Makro_Evren', '02_5_Hidrodinamik_Kuvvetin_Koku.md')
with open(f2_path, 'r', encoding='utf-8') as f:
    text = f.read()
text = re.sub(r'# Kısım III: Makro Evren Dinamikleri', r'# 3.2 5. Hidrodinamik Kuvvetin Kökü', text)
with open(f2_path, 'w', encoding='utf-8') as f:
    f.write(text)

# Fix 3: Kisim 3 - 03
f3_path = os.path.join(base_path, 'Kisim_3_Makro_Evren', '03_Mikrodan_Makroya_Evrenaki.md')
with open(f3_path, 'r', encoding='utf-8') as f:
    text = f.read()
if not text.startswith('# 3.3'):
    text = "# 3.3 Mikrodan Makroya Evrenakı (Kütle ve Gradyan İlişkisi)\n\n" + text
with open(f3_path, 'w', encoding='utf-8') as f:
    f.write(text)

# Fix 4: Kisim 3 - 10
f4_path = os.path.join(base_path, 'Kisim_3_Makro_Evren', '10_Ayin_Gizemleri.md')
with open(f4_path, 'r', encoding='utf-8') as f:
    text = f.read()
text = re.sub(r'# 3\.11 Ay\'ın Gizemleri', r'# 3.10 Ay\'ın Gizemleri', text)
text = re.sub(r'(#+) 3\.11\.', r'\1 3.10.', text)
with open(f4_path, 'w', encoding='utf-8') as f:
    f.write(text)

# Fix 5: Kisim 3 - 11
f5_path = os.path.join(base_path, 'Kisim_3_Makro_Evren', '11_Saturn_Halka_Dinamigi.md')
with open(f5_path, 'r', encoding='utf-8') as f:
    text = f.read()
text = re.sub(r'# 3\.12 EVRENAKI TEORİSİ ÇERÇEVESİNDE SATÜRN HALKA DİNAMİĞİ:', r'# 3.11 EVRENAKI TEORİSİ ÇERÇEVESİNDE SATÜRN HALKA DİNAMİĞİ:', text)
with open(f5_path, 'w', encoding='utf-8') as f:
    f.write(text)

# Fix 6: Kisim 3 - 12
f6_path = os.path.join(base_path, 'Kisim_3_Makro_Evren', '12_Ne_Ogrendik.md')
with open(f6_path, 'r', encoding='utf-8') as f:
    text = f.read()
text = re.sub(r'# 3\.13 Kısım Özeti: Ne Öğrendik\?', r'# 3.12 Kısım Özeti: Ne Öğrendik?', text)
with open(f6_path, 'w', encoding='utf-8') as f:
    f.write(text)

# Fix 7: Kisim 4 - 03
f7_path = os.path.join(base_path, 'Kisim_4_Bilimin_Tekilligi', '03_Kutlecekimsel_Merceklenme.md')
with open(f7_path, 'r', encoding='utf-8') as f:
    text = f.read()
text = re.sub(r'### 4\.6\.(\d+)', r'## 4.3.\1', text)
with open(f7_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("All fixes applied successfully.")
