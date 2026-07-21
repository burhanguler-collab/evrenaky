import zipfile
import xml.etree.ElementTree as ET
import os

docx_path = r'C:\Users\ASUS\Desktop\EvrenAKI\KITAP2\5_Arsiv\CFS-makale1.docx'
extract_dir = r'C:\Users\ASUS\Desktop\EvrenAKI\KITAP3\scratch_docx'

if not os.path.exists(extract_dir):
    os.makedirs(extract_dir)

with zipfile.ZipFile(docx_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

xml_content = open(os.path.join(extract_dir, 'word', 'document.xml'), 'r', encoding='utf-8').read()
tree = ET.fromstring(xml_content)

# Extract text
namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
paragraphs = tree.findall('.//w:p', namespaces)
texts = []
for p in paragraphs:
    texts.append(''.join(node.text for node in p.findall('.//w:t', namespaces) if node.text))

# Find the section for Sheyma Deneyi
sheyma_text = ""
recording = False
for t in texts:
    if "SHEYMA DENEYİ" in t.upper() or "ŞEYMA DENEYİ" in t.upper():
        recording = True
    if recording:
        sheyma_text += t + "\n"

print("--- TEXT EXTRACTED ---")
print(sheyma_text[:4000]) # print first 4000 chars

# List images
media_dir = os.path.join(extract_dir, 'word', 'media')
if os.path.exists(media_dir):
    print("\n--- IMAGES FOUND ---")
    print(os.listdir(media_dir))
