import os

root_dir = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik'

print("--- KITAP 3 İÇERİK DURUMU ---")
for root, dirs, files in os.walk(root_dir):
    # Sort for readability
    dirs.sort()
    files.sort()
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, root_dir)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = len(content.splitlines())
                words = len(content.split())
            print(f"{rel_path:<60} | Satır: {lines:<4} | Kelime: {words:<5}")
