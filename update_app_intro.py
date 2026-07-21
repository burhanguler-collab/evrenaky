import re

with open('c:/Users/ASUS/Desktop/EvrenAKI/KITAP4/websitesi/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Replace chapters array
chapters_pattern = re.compile(r'const chapters = \[\s*(.*?)\s*\];', re.DOTALL)
new_chapters = '''const chapters = [
    { id: 'akademik_01', title: 'Akademik Sürüm: Bölüm 1', file: 'Metin/akademik_01.md', group: 'akademik' },
    { id: 'populer_01', title: 'Popüler Sürüm: Bölüm 1', file: 'Metin/populer_01.md', group: 'populer' },
    { id: 'duzeltme', title: 'Hakem Değerlendirmeleri', file: 'Metin/duzeltme.md', group: 'all' }
];'''
js = chapters_pattern.sub(new_chapters, js)

# 2. Add global version state and functions at the top after ADMIN_EMAILS
version_state = '''
// Global Version State
let activeVersion = safeStorage ? (safeStorage.getItem('selectedVersion') || 'akademik') : 'akademik';

window.selectVersion = function(version) {
    activeVersion = version;
    if (safeStorage) safeStorage.setItem('selectedVersion', version);
    
    // Build TOC for selected version
    buildTOC();
    
    // Close splash
    const splash = document.getElementById('splash-screen');
    if (splash && !splash.classList.contains('fade-out')) {
        splash.classList.add('fade-out');
        setTimeout(() => {
            splash.style.display = 'none';
        }, 600);
    }
    
    // Load first chapter of selected version
    loadChapter(version === 'akademik' ? 'akademik_01_01' : 'populer_01');
};

window.continueReading = function() {
    loadChapter(activeVersion === 'akademik' ? 'akademik_01_01' : 'populer_01');
};
'''
js = js.replace('let activeChapterId = null;', version_state + '\nlet activeChapterId = null;')

# 3. Update buildTOC
old_build_toc = '''    chapters.forEach(chap => {
        const li = document.createElement('li');
        li.className = 'toc-item';
        li.setAttribute('data-title', chap.title);
        li.innerHTML = 
            <a href="#" class="toc-link" id="link-">
                
            </a>
        ;
        list.appendChild(li);
    });'''
new_build_toc = '''    const filteredChapters = chapters.filter(c => c.group === activeVersion || c.group === 'all');
    filteredChapters.forEach(chap => {
        const li = document.createElement('li');
        li.className = 'toc-item';
        li.setAttribute('data-title', chap.title);
        li.innerHTML = 
            <a href="#" class="toc-link" id="link-">
                
            </a>
        ;
        list.appendChild(li);
    });
    if (typeof lucide !== 'undefined') lucide.createIcons();'''
js = js.replace(old_build_toc, new_build_toc)

# 4. Remove splash screen auto-close and skip button logic
old_splash_logic = '''    if (skipBtn) {
        skipBtn.onclick = closeSplash;
    }

    // Auto-close splash screen after 5.2 seconds
    setTimeout(closeSplash, 5200);'''
new_splash_logic = '''    // Splash screen will now wait for user to select version. No auto-close.'''
js = js.replace(old_splash_logic, new_splash_logic)

# Remove introPlayed logic from closing Splash directly on load, so they can always pick version, OR we skip if already picked.
old_intro_check = '''    if (introPlayed && !playIntroAlways) {
        if (splash) splash.style.display = 'none';
        return;
    }'''
new_intro_check = '''    if (introPlayed && !playIntroAlways) {
        if (splash) splash.style.display = 'none';
        // Ensure TOC is built with saved version
        buildTOC();
        return;
    }'''
js = js.replace(old_intro_check, new_intro_check)

with open('c:/Users/ASUS/Desktop/EvrenAKI/KITAP4/websitesi/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("app.js updated successfully")
