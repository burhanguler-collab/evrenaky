import json
import re

try:
    with open('log_line.json', 'r', encoding='utf-16') as f:
        line = f.read().strip()
            
    data = json.loads(line)
    
    content = ""
    if "content" in data:
        content = data["content"]
        
    lines = content.split('\n')
    output_lines = []
    start = False
    for l in lines:
        if 'The following code has been modified' in l:
            start = True
            continue
        if start:
            if l.startswith('The above content shows'):
                break
            m = re.match(r'^\d+:\s?(.*)$', l)
            if m:
                output_lines.append(m.group(1))
                
    if len(output_lines) > 700:
        with open(r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik\Kisim_3_Makro_Evren\03_Mikrodan_Makroya_Evrenaki.md', 'w', encoding='utf-8') as out_f:
            out_f.write('\n'.join(output_lines) + '\n')
        print("Successfully recovered 03_")
    else:
        print("Not enough lines:", len(output_lines))
        
except Exception as e:
    print("Error:", e)
