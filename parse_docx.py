import zipfile
import xml.etree.ElementTree as ET
import os

extract_dir = r'C:\Users\ASUS\Desktop\EvrenAKI\KITAP3\scratch_docx'
xml_content = open(os.path.join(extract_dir, 'word', 'document.xml'), 'r', encoding='utf-8').read()
tree = ET.fromstring(xml_content)

namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
              'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
              'pic': 'http://schemas.openxmlformats.org/drawingml/2006/picture',
              'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}

# We want to extract text and image references in order.
paragraphs = tree.findall('.//w:p', namespaces)

out_text = ""
recording = False

for p in paragraphs:
    # Get text
    p_text = ''.join(node.text for node in p.findall('.//w:t', namespaces) if node.text)
    
    if "SHEYMA DENEYİ" in p_text.upper() or "ŞEYMA DENEYİ" in p_text.upper():
        recording = True
        
    if recording:
        if p_text:
            out_text += p_text + "\n"
        
        # Check for images in this paragraph
        blips = p.findall('.//a:blip', namespaces)
        for blip in blips:
            embed_id = blip.get('{%s}embed' % namespaces['r'])
            if embed_id:
                out_text += f"[IMAGE_REF: {embed_id}]\n"

with open(r'C:\Users\ASUS\Desktop\EvrenAKI\KITAP3\scratch_docx\sheyma_full.txt', 'w', encoding='utf-8') as f:
    f.write(out_text)

print("Saved to sheyma_full.txt")

# Also need to map embed_id to actual image filename
rels_content = open(os.path.join(extract_dir, 'word', '_rels', 'document.xml.rels'), 'r', encoding='utf-8').read()
rels_tree = ET.fromstring(rels_content)
rel_ns = {'rel': 'http://schemas.openxmlformats.org/package/2006/relationships'}
for rel in rels_tree.findall('.//rel:Relationship', rel_ns):
    print(f"{rel.get('Id')} -> {rel.get('Target')}")
