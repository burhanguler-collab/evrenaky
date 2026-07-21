import re

file_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\blgr.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update import to include updateDoc
content = content.replace(
    'import { getFirestore, collection, getDocs, doc, getDoc, deleteDoc } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";',
    'import { getFirestore, collection, getDocs, doc, getDoc, deleteDoc, updateDoc } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";'
)

# 2. Update the buttons inside loadSubmissions
bad_buttons = '''            <div class="sub-actions">
              <button class="btn-reject"><i class="fas fa-times"></i> Reddet</button>
              <button class="btn-approve"><i class="fas fa-check"></i> Onayla & Yayınla</button>
            </div>'''
            
good_buttons = '''            <div class="sub-actions">
              <button class="btn-reject" onclick="rejectSubmission('')"><i class="fas fa-times"></i> Reddet</button>
              <button class="btn-approve" onclick="approveSubmission('')"><i class="fas fa-check"></i> Onayla & Yayınla</button>
            </div>'''

content = content.replace(bad_buttons, good_buttons)

# 3. Add the logic functions
js_logic = '''
    window.approveSubmission = async function(id) {
        try {
            await updateDoc(doc(db, "submissions", id), {
                status: 'approved'
            });
            alert("Başarıyla onaylandı! Artık sitede yayınlanıyor.");
            loadSubmissions(); // Refresh list
        } catch (e) {
            alert("Onaylama sırasında hata oluştu: " + e.message);
        }
    };

    window.rejectSubmission = async function(id) {
        if(confirm("Bu gönderiyi reddedip tamamen silmek istediğinize emin misiniz?")) {
            try {
                await deleteDoc(doc(db, "submissions", id));
                alert("Başarıyla reddedildi ve silindi.");
                loadSubmissions(); // Refresh list
            } catch (e) {
                alert("Silme sırasında hata oluştu: " + e.message);
            }
        }
    };
    
    // Auto load when dashboard opens
'''

content = content.replace('    // Auto load when dashboard opens', js_logic)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Approve/Reject logic added.")
