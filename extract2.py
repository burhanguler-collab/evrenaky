import json
import re

log_path = r'C:\Users\ASUS\.gemini\antigravity-ide\brain\f0440324-2db8-4b45-8aed-33c33a7243da\.system_generated\logs\transcript.jsonl'

best_content = []
with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        if '03_Mikrodan_Makroya_Evrenaki.md' in line:
            try:
                data = json.loads(line.strip())
            except:
                continue
                
            content = data.get("content", "")
            if not content:
                content = data.get("output", "")
                
            if 'The following code has been modified' in content:
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
                            
                if len(output_lines) > len(best_content):
                    best_content = output_lines

if len(best_content) > 700:
    with open(r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik\Kisim_3_Makro_Evren\03_Mikrodan_Makroya_Evrenaki.md', 'w', encoding='utf-8') as out_f:
        out_f.write('\n'.join(best_content) + '\n')
    print("Recovered:", len(best_content))
else:
    print("Could not recover, max lines found:", len(best_content))
