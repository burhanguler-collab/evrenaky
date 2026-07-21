import re

file_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\blgr.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the import
content = content.replace(
    'import { getFirestore, collection, getDocs, doc, getDoc } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";',
    'import { getFirestore, collection, getDocs, doc, getDoc, deleteDoc } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";'
)
# Remove the stray import
content = content.replace('    import { deleteDoc } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";\n', '')

# Fix the mangled template literal
bad_block = '''          html += <div class="submission-item" id="thread-">
            <div class="sub-header">
              <span class="sub-author"><i class="fas fa-user-circle"></i>  <span style="font-size:12px;color:var(--text-muted);">(Kategori: )</span></span>
              <span class="sub-date"></span>
            </div>
            <div style="margin-top: 5px; font-size: 16px; font-weight: bold; color: var(--neon-blue);"></div>
            <div class="sub-content"></div>
            <div class="sub-actions">
              <button class="btn-reject" onclick="deleteThread('')"><i class="fas fa-trash"></i> Siteden Sil</button>
            </div>
          </div>;'''

good_block = '''          html += <div class="submission-item" id="thread-">
            <div class="sub-header">
              <span class="sub-author"><i class="fas fa-user-circle"></i>  <span style="font-size:12px;color:var(--text-muted);">(Kategori: )</span></span>
              <span class="sub-date"></span>
            </div>
            <div style="margin-top: 5px; font-size: 16px; font-weight: bold; color: var(--neon-blue);"></div>
            <div class="sub-content"></div>
            <div class="sub-actions">
              <button class="btn-reject" onclick="deleteThread('')"><i class="fas fa-trash"></i> Siteden Sil</button>
            </div>
          </div>;'''

if bad_block in content:
    content = content.replace(bad_block, good_block)
else:
    # Just to be sure, regex replace everything from html += <div to </div>\n          </div>;
    import re
    content = re.sub(r'html \+= <div class="submission-item".*?</div>\n          </div>;', good_block, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Mangled literal fixed.")
