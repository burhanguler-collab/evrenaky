import re

with open('c:/Users/ASUS/Desktop/EvrenAKI/KITAP4/websitesi/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace chapters array
chapters_pattern = re.compile(r'const chapters = \[\s*(.*?)\s*\];', re.DOTALL)
generic_chapters = '''const chapters = [
    { id: 'ozet', title: 'Kitap Özeti', file: 'Metin/ozet.md' },
    { id: 'bolum_01', title: 'Bölüm 1: Giriş', file: 'Metin/bolum_01.md' },
    { id: 'duzeltme', title: 'Hakem Değerlendirmeleri ve Düzeltmeler', file: 'Metin/duzeltme.md' }
];'''
js = chapters_pattern.sub(generic_chapters, js)

# Replace MOCK_SEEDS
mock_seeds_pattern = re.compile(r'const MOCK_SEEDS = \{(.*?)\};\n', re.DOTALL)
generic_mock_seeds = '''const MOCK_SEEDS = {
    users: [
        { id: '1', email: 'kullanici1@mail.com', username: 'Okuyucu_1' },
        { id: '2', email: 'kullanici2@mail.com', username: 'Okuyucu_2' }
    ],
    comments: [
        { id: '1', chapter_id: 'bolum_01', username: 'Okuyucu_1', content: 'Bu bölüm çok açıklayıcı olmuş.', created_at: '2026-06-29T14:24:00Z' }
    ],
    posts: [
        { id: '1', category: 'genel', title: 'Kitap Hakkında Genel Düşüncelerim', content: 'Projenin altyapısını ve tasarımını çok beğendim.', username: 'Okuyucu_2', created_at: '2026-06-28T09:12:00Z' }
    ],
    replies: [
        { id: '1', post_id: '1', username: 'Okuyucu_1', content: 'Kesinlikle katılıyorum.', created_at: '2026-06-28T11:30:00Z' }
    ]
};
'''
js = mock_seeds_pattern.sub(generic_mock_seeds, js)

# Replace generic domain string
js = js.replace('admin@evrenaki.com', 'admin@proje.com')
js = js.replace('evrenaky_mock_', 'proje_mock_')

with open('c:/Users/ASUS/Desktop/EvrenAKI/KITAP4/websitesi/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("app.js updated successfully")
