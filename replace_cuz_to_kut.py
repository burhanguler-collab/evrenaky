import os
import re

base_dir = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi'

replacements = {
    "Cüz'lerden": "Kut'lardan",
    "cüz'lerden": "kut'lardan",
    "CÜZ'LERDEN": "KUT'LARDAN",
    "Cüzlerden": "Kutlardan",
    "cüzlerden": "kutlardan",
    "CÜZLERDEN": "KUTLARDAN",
    "Cüz'lerin": "Kut'ların",
    "cüz'lerin": "kut'ların",
    "CÜZ'LERİN": "KUT'LARIN",
    "Cüzlerin": "Kutların",
    "cüzlerin": "kutların",
    "CÜZLERİN": "KUTLARIN",
    "Cüz'lerde": "Kut'larda",
    "cüz'lerde": "kut'larda",
    "CÜZ'LERDE": "KUT'LARDA",
    "Cüzlerde": "Kutlarda",
    "cüzlerde": "kutlarda",
    "CÜZLERDE": "KUTLARDA",
    "Cüz'den": "Kut'tan",
    "cüz'den": "kut'tan",
    "CÜZ'DEN": "KUT'TAN",
    "Cüzden": "Kuttan",
    "cüzden": "kuttan",
    "CÜZDEN": "KUTTAN",
    "Cüz'de": "Kut'ta",
    "cüz'de": "kut'ta",
    "CÜZ'DE": "KUT'TA",
    "Cüzde": "Kutta",
    "cüzde": "kutta",
    "CÜZDE": "KUTTA",
    "Cüz'ün": "Kut'un",
    "cüz'ün": "kut'un",
    "CÜZ'ÜN": "KUT'UN",
    "Cüzün": "Kutun",
    "cüzün": "kutun",
    "CÜZÜN": "KUTUN",
    "Cüz'lük": "Kut'luk",
    "cüz'lük": "kut'luk",
    "CÜZ'LÜK": "KUT'LUK",
    "Cüzlük": "Kutluk",
    "cüzlük": "kutluk",
    "CÜZLÜK": "KUTLUK",
    "Cüz'e": "Kut'a",
    "cüz'e": "kut'a",
    "CÜZ'E": "KUT'A",
    "Cüze": "Kuta",
    "cüze": "kuta",
    "CÜZE": "KUTA",
    "Cüz'ü": "Kut'u",
    "cüz'ü": "kut'u",
    "CÜZ'Ü": "KUT'U",
    "Cüzü": "Kutu",
    "cüzü": "kutu",
    "CÜZÜ": "KUTU",
    "Cüzler": "Kutlar",
    "cüzler": "kutlar",
    "CÜZLER": "KUTLAR",
    "Cüz'ler": "Kut'lar",
    "cüz'ler": "kut'lar",
    "CÜZ'LER": "KUT'LAR",
    "Cüz": "Kut",
    "cüz": "kut",
    "CÜZ": "KUT"
}

ext_to_check = {'.md', '.js', '.html', '.txt'}

# To ensure whole word replacement, we will use regex word boundaries,
# but since Turkish has suffixes and apostrophes, we need to be careful.
# Actually, the dictionary includes all expected suffixes. 
# We can search for \b(key)\b but in regex \b might not work perfectly with '.
# Let's use negative lookaheads/lookbehinds to ensure it's a standalone word.

def replace_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    for old, new in replacements.items():
        # Match old string only if not preceded or followed by alphanumeric chars.
        # \B doesn't work well with non-english letters.
        # So we use regex with lookaround, treating non-word boundaries appropriately.
        # Because we replace longest strings first (ordered in dict? Dict in python 3.7+ preserves insertion order, which is length-based roughly here).
        # Let's sort the replacements dict by length of key descending.
        
        pass # we will process sorted below

    keys = sorted(replacements.keys(), key=len, reverse=True)
    
    modified = False
    for k in keys:
        # Regex to match 'k' exactly as a whole word-like sequence.
        # We ensure no a-z, A-Z, ğüşıöçĞÜŞİÖÇ directly before or after.
        escaped_k = re.escape(k)
        pattern = r'(?<![a-zA-ZğüşıöçĞÜŞİÖÇ])' + escaped_k + r'(?![a-zA-ZğüşıöçĞÜŞİÖÇ])'
        
        if re.search(pattern, new_content):
            new_content = re.sub(pattern, replacements[k], new_content)
            modified = True
            
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {file_path}")

for root, dirs, files in os.walk(base_dir):
    for f in files:
        if any(f.endswith(ext) for ext in ext_to_check):
            # Skip node_modules etc if they exist
            if 'node_modules' in root or '.git' in root or '_arsiv' in root:
                continue
            full_path = os.path.join(root, f)
            try:
                replace_in_file(full_path)
            except Exception as e:
                print(f"Error reading {full_path}: {e}")

print("Done.")
