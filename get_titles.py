import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

matches = re.findall(r"title:\s*['\"](.*?)['\"]", content)
for i, m in enumerate(matches):
    print(f"{i+1}. {m}")
