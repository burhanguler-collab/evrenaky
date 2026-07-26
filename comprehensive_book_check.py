import os
import re
import sys

# Ensure UTF-8 output encoding for Windows terminal
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

base_dir = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi'
app_js_path = os.path.join(base_dir, 'app.js')
metin_dir = os.path.join(base_dir, 'Metin')
gorseller_dir = os.path.join(base_dir, 'Gorseller')
simulasyon_dir = os.path.join(base_dir, 'Simulasyon')

print("==================================================")
print("       TÜM KİTAP KAPSAMLI DENETİM RAPORU          ")
print("==================================================")

# 1. Read app.js chapters
chapters = []
if os.path.exists(app_js_path):
    with open(app_js_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
        match = re.search(r'const chapters = \[(.*?)\];', content, re.DOTALL)
        if match:
            arr_str = match.group(1)
            files = re.findall(r"file:\s*['\"]([^'\"]+)['\"]", arr_str)
            chapters = files

print(f"\n[1] App.js İçindeki Bölüm Sayısı: {len(chapters)}")

# 2. Collect all markdown files under Metin
all_md_files = []
for root, dirs, files in os.walk(metin_dir):
    if "Eski_Surum" in root:
        continue
    for file in files:
        if file.endswith('.md'):
            rel_path = os.path.relpath(os.path.join(root, file), base_dir).replace('\\', '/')
            all_md_files.append(rel_path)

print(f"[2] Metin Klasöründeki Toplam Aktif Markdown Dosyası Sayısı: {len(all_md_files)}")

# Check chapters in app.js vs filesystem
missing_in_fs = []
for c in chapters:
    full_p = os.path.join(base_dir, c.replace('/', os.sep))
    if not os.path.exists(full_p):
        missing_in_fs.append(c)

orphaned_md = []
chapters_set = set(chapters)
for md in all_md_files:
    # Exclude Populer chapters and editor notes from orphan warnings if intentional
    if md not in chapters_set and not md.startswith('Metin/Populer'):
        orphaned_md.append(md)

if missing_in_fs:
    print(f"  [HATA] app.js'de tanımlı ama diskte bulunamayan dosyalar ({len(missing_in_fs)}):")
    for m in missing_in_fs:
        print(f"     - {m}")
else:
    print("  [OK] app.js'deki tüm bölüm dosyaları diskte mevcut.")

if orphaned_md:
    print(f"  [BİLGİ] app.js'e kayıtlı olmayan Akademik dosyalar ({len(orphaned_md)}):")
    for om in orphaned_md:
        print(f"     - {om}")
else:
    print("  [OK] Yetim akademik markdown dosyası yok.")

# 3. Content Analysis of all Markdown files
print("\n[3] İçerik, LaTeX, HTML ve Karakter Kodlama Denetimi")

mojibake_patterns = [r'Ã¼', r'Ã§', r'Ã¶', r'ÄŸ', r'ÅŸ', r'Ä±', r'Ã‡', r'Ã–', r'Ãœ', r'Äž', r'Åž', r'Ä°', r'ï»¿', r'â€™', r'â€œ', r'â€']
mojibake_regex = re.compile('|'.join(mojibake_patterns))

image_refs_in_md = set()
sim_refs_in_md = set()
broken_img_refs = []
broken_sim_refs = []
latex_warnings = []
mojibake_warnings = []
empty_section_warnings = []

for md_rel in all_md_files:
    md_full = os.path.join(base_dir, md_rel.replace('/', os.sep))
    with open(md_full, 'r', encoding='utf-8', errors='replace') as f:
        text = f.read()

    # Check UTF-8 BOM or Mojibake
    if text.startswith('\ufeff'):
        mojibake_warnings.append(f"{md_rel}: Dosya UTF-8 BOM ile başlıyor.")
    m_matches = mojibake_regex.findall(text)
    if m_matches:
        mojibake_warnings.append(f"{md_rel}: Bozuk karakter (Mojibake) tespit edildi: {set(m_matches)}")

    # Check empty section placeholder
    if "(Bu bölümün içeriği yakında eklenecektir...)" in text or len(text.strip()) < 50:
        empty_section_warnings.append(f"{md_rel}: Bölüm boş veya placeholder içeriyor.")

    # Remove <script>...</script> blocks before checking LaTeX formulas
    text_no_script = re.sub(r'<script.*?>.*?</script>', '', text, flags=re.DOTALL | re.IGNORECASE)
    # Remove JS template strings ${...}
    text_math_only = re.sub(r'\$\{[^}]*\}', '', text_no_script)

    # Check LaTeX math equation markers ($ and $$)
    # Match double dollars $$
    double_dollars = len(re.findall(r'(?<!\\)\$\$', text_math_only))
    # Remove $$ blocks to inspect single $
    text_single_math = re.sub(r'(?<!\\)\$\$.*?(?<!\\)\$\$', '', text_math_only, flags=re.DOTALL)
    single_dollars = len(re.findall(r'(?<!\\)\$', text_single_math))

    if double_dollars % 2 != 0:
        latex_warnings.append(f"{md_rel}: Çiftli '$$' formül bloğu kapanmamış (Sayı: {double_dollars})")
    if single_dollars % 2 != 0:
        latex_warnings.append(f"{md_rel}: Tekli '$' satır içi formül işareti kapanmamış (Sayı: {single_dollars})")

    # LaTeX \( \) and \[ \] check
    slash_open_paren = text_math_only.count(r'\(')
    slash_close_paren = text_math_only.count(r'\)')
    if slash_open_paren != slash_close_paren:
        latex_warnings.append(f"{md_rel}: \\( ve \\) sayıları eşit değil ({slash_open_paren} vs {slash_close_paren})")

    slash_open_bracket = text_math_only.count(r'\[')
    slash_close_bracket = text_math_only.count(r'\]')
    if slash_open_bracket != slash_close_bracket:
        latex_warnings.append(f"{md_rel}: \\[ ve \\] sayıları eşit değil ({slash_open_bracket} vs {slash_close_bracket})")

    # Extract Image references
    img_html = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', text)
    img_md = re.findall(r'!\[.*?\]\((.*?)\)', text)
    all_imgs = img_html + img_md
    for img in all_imgs:
        img_clean = img.strip().split('?')[0].split('#')[0]
        if img_clean.startswith('http') or img_clean.startswith('data:'):
            continue
        image_refs_in_md.add(img_clean)
        img_full = os.path.join(base_dir, img_clean.replace('/', os.sep))
        if not os.path.exists(img_full):
            broken_img_refs.append(f"{md_rel} -> Görsel bulunamadı: {img_clean}")

    # Extract Simulation references (iframes or links to html files)
    iframes = re.findall(r'<iframe[^>]+src=["\']([^"\']+)["\']', text)
    links = re.findall(r'href=["\']([^"\']+\.html[^"\']*)["\']', text)
    md_links = re.findall(r'\[.*?\]\((.*?\.html.*?)\)', text)
    all_sims = iframes + links + md_links
    for sim in all_sims:
        sim_clean = sim.strip().split('?')[0].split('#')[0]
        if sim_clean.startswith('http'):
            continue
        sim_refs_in_md.add(sim_clean)
        sim_full = os.path.join(base_dir, sim_clean.replace('/', os.sep))
        if not os.path.exists(sim_full):
            broken_sim_refs.append(f"{md_rel} -> Simülasyon/HTML bulunamadı: {sim_clean}")

# Report Content Results
if empty_section_warnings:
    print(f"  [UYARI] Boş / Placeholder Bölümler ({len(empty_section_warnings)}):")
    for w in empty_section_warnings:
        print(f"     - {w}")
else:
    print("  [OK] Tüm bölümlerde içerik dolu ve tamamlanmış.")

if mojibake_warnings:
    print(f"  [HATA] Bozuk Karakter / Kodlama Uyarıları ({len(mojibake_warnings)}):")
    for w in mojibake_warnings:
        print(f"     - {w}")
else:
    print("  [OK] Karakter kodlamaları düzgün (Mojibake yok).")

if latex_warnings:
    print(f"  [UYARI] LaTeX Formül Uyarıları ({len(latex_warnings)}):")
    for w in latex_warnings:
        print(f"     - {w}")
else:
    print("  [OK] LaTeX formül sembolleri tam ve dengeli.")

if broken_img_refs:
    print(f"  [HATA] Kırık Görsel Bağlantıları ({len(broken_img_refs)}):")
    for w in broken_img_refs:
        print(f"     - {w}")
else:
    print("  [OK] Markdown dosyalarındaki tüm görsel bağlantıları geçerli.")

if broken_sim_refs:
    print(f"  [HATA] Kırık Simülasyon / HTML Bağlantıları ({len(broken_sim_refs)}):")
    for w in broken_sim_refs:
        print(f"     - {w}")
else:
    print("  [OK] Markdown dosyalarındaki tüm simülasyon/HTML bağlantıları geçerli.")

# 4. Check Görseller Folder Integrity
print("\n[4] Görseller Klasörü ve Kullanılmayan Görsel Denetimi")
all_gorsel_files = []
if os.path.exists(gorseller_dir):
    for root, dirs, files in os.walk(gorseller_dir):
        for file in files:
            rel_p = os.path.relpath(os.path.join(root, file), base_dir).replace('\\', '/')
            all_gorsel_files.append(rel_p)

print(f"  - Gorseller klasöründeki toplam dosya sayısı: {len(all_gorsel_files)}")

other_files = [app_js_path, os.path.join(base_dir, 'index.html'), os.path.join(base_dir, 'index.css'), os.path.join(base_dir, 'blgr.html')]
all_referenced_images = set(image_refs_in_md)

for of in other_files:
    if os.path.exists(of):
        with open(of, 'r', encoding='utf-8', errors='replace') as f:
            c = f.read()
            imgs = re.findall(r'Gorseller/[a-zA-Z0-9_\-\.]+\.(?:png|jpg|jpeg|gif|svg|webp)', c, re.IGNORECASE)
            for img in imgs:
                all_referenced_images.add(img)

orphaned_images = []
for gf in all_gorsel_files:
    if gf not in all_referenced_images:
        orphaned_images.append(gf)

print(f"  - Referans verilen benzersiz görsel sayısı: {len(all_referenced_images)}")
if orphaned_images:
    print(f"  [BİLGİ] Kullanılmayan (Yetim) Görseller ({len(orphaned_images)}):")
    for oi in orphaned_images[:10]:
        print(f"     - {oi}")
    if len(orphaned_images) > 10:
        print(f"     ... ve {len(orphaned_images)-10} tane daha.")
else:
    print("  [OK] Tüm görseller metinlerde veya kodlarda aktif kullanılıyor.")

# 5. Check Simulations Integrity
print("\n[5] Simülasyon Dosyaları Denetimi")
sim_files = []
if os.path.exists(simulasyon_dir):
    for root, dirs, files in os.walk(simulasyon_dir):
        for file in files:
            if file.endswith('.html'):
                rel_p = os.path.relpath(os.path.join(root, file), base_dir).replace('\\', '/')
                sim_files.append(rel_p)

print(f"  - Simulasyon klasöründeki toplam HTML dosyası sayısı: {len(sim_files)}")

sim_script_errors = []
for sf in sim_files:
    sf_full = os.path.join(base_dir, sf.replace('/', os.sep))
    with open(sf_full, 'r', encoding='utf-8', errors='replace') as f:
        html_c = f.read()
    
    script_srcs = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', html_c)
    for src in script_srcs:
        if src.startswith('http') or src.startswith('//'):
            continue
        sf_dir = os.path.dirname(sf_full)
        script_full = os.path.normpath(os.path.join(sf_dir, src))
        if not os.path.exists(script_full):
            sim_script_errors.append(f"{sf} -> Eksik script: {src}")

if sim_script_errors:
    print(f"  [HATA] Simülasyonlarda eksik script/kütüphane bağımlılığı ({len(sim_script_errors)}):")
    for err in sim_script_errors:
        print(f"     - {err}")
else:
    print("  [OK] Tüm simülasyonların yerel script/kütüphane bağımlılıkları mevcut.")

print("\n==================================================")
print("               DENETİM TAMAMLANDI                 ")
print("==================================================")
