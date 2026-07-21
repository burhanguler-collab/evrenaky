import re

with open('c:/Users/ASUS/Desktop/EvrenAKI/KITAP4/websitesi/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace splash screen button
old_splash_btn = '''<button id="btn-skip-intro" class="btn">
                Girişi Atla <i data-lucide="chevron-right"></i>
            </button>'''
new_splash_options = '''<div class="intro-options" style="display: flex; gap: 16px; margin-top: 24px; z-index: 10;">
                <button id="btn-academic" class="btn btn-primary" onclick="selectVersion('akademik')">
                    <i data-lucide="book-open"></i> Akademik Sürüm
                </button>
                <button id="btn-popular" class="btn btn-peer-review" onclick="selectVersion('populer')">
                    <i data-lucide="sparkles"></i> Popüler Sürüm
                </button>
            </div>'''
html = html.replace(old_splash_btn, new_splash_options)

# Replace home view buttons
old_hero_actions = '''<div class="hero-actions">
                                    <button class="btn btn-primary" onclick="loadChapter('ozet')" style="background-color: var(--neon-magenta); border-color: var(--neon-magenta);">
                                        <i data-lucide="book"></i> Kitabın Özeti
                                    </button>
                                    <button class="btn btn-primary" onclick="loadChapter('bolum_01')">
                                        <i data-lucide="book-open"></i> Okumaya Başla
                                    </button>
                                    <button class="btn btn-peer-review" onclick="loadChapter('duzeltme')">
                                        <i data-lucide="shield-check"></i> Hakem Değerlendirmeleri
                                    </button>
                                    <button class="btn btn-secondary" onclick="switchTab('sim')">
                                        <i data-lucide="cpu"></i> Simülasyonu Çalıştır
                                    </button>
                                </div>'''
new_hero_actions = '''<div class="hero-actions">
                                    <button class="btn btn-primary" onclick="continueReading()">
                                        <i data-lucide="book-open"></i> Okumaya Başla
                                    </button>
                                    <button class="btn btn-peer-review" onclick="loadChapter('duzeltme')">
                                        <i data-lucide="shield-check"></i> Hakem Değerlendirmeleri
                                    </button>
                                    <button class="btn btn-secondary" onclick="switchTab('sim')">
                                        <i data-lucide="cpu"></i> Simülasyonu Çalıştır
                                    </button>
                                </div>'''
html = html.replace(old_hero_actions, new_hero_actions)

with open('c:/Users/ASUS/Desktop/EvrenAKI/KITAP4/websitesi/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html updated successfully")
