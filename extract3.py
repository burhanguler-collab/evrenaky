import json
import re

log_path = r'C:\Users\ASUS\.gemini\antigravity-ide\brain\f0440324-2db8-4b45-8aed-33c33a7243da\.system_generated\logs\transcript.jsonl'

with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        if 'Total Lines: 723' in line:
            print("FOUND A LINE WITH TOTAL LINES 723")
            data = json.loads(line.strip())
            
            # recursive search for strings
            def search_dict(d):
                if isinstance(d, dict):
                    for k, v in d.items():
                        if isinstance(v, str) and 'Total Lines: 723' in v:
                            print(f"Found in key: {k}")
                            if 'The following code has been modified' in v:
                                print("And it has the modified string! Length:", len(v))
                                return v
                        else:
                            res = search_dict(v)
                            if res: return res
                elif isinstance(d, list):
                    for item in d:
                        res = search_dict(item)
                        if res: return res
                return None
                
            res = search_dict(data)
            if res:
                lines = res.split('\n')
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
                print("Lines parsed:", len(output_lines))
                if len(output_lines) > 700:
                    with open(r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik\Kisim_3_Makro_Evren\03_Mikrodan_Makroya_Evrenaki.md', 'w', encoding='utf-8') as out_f:
                        out_f.write('\n'.join(output_lines) + '\n')
                    print("SUCCESS")
