import re

file_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\blgr.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add Menu Item
menu_html = '''
      <li onclick="showTab('discussionsTab', this)">
        <i class="fas fa-comments"></i> Forum/Yorumlar
      </li>
'''
content = content.replace('<li onclick="showTab(\'submissionsTab\', this)">', menu_html + '<li onclick="showTab(\'submissionsTab\', this)">')

# Add Tab Content
tab_html = '''
    <div id="discussionsTab" class="tab-content">
      <h2>Forum ve Okuyucu Yorumları</h2>
      <p>Sitede anında yayınlanan tartışma başlıklarını buradan yönetebilir ve silebilirsiniz.</p>
      <div id="discussionsList" class="submissions-list">
        <div style="text-align:center; padding:20px; color:var(--text-muted);">Yükleniyor...</div>
      </div>
    </div>
'''
content = content.replace('<div id="submissionsTab"', tab_html + '\n    <div id="submissionsTab"')

# Add JS logic for fetching and deleting
js_logic = '''
    // Fetch Discussions
    import { deleteDoc } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";
    async function loadDiscussions() {
      try {
        const querySnapshot = await getDocs(collection(db, "forum_threads"));
        let html = '';
        querySnapshot.forEach((docSnap) => {
          let data = docSnap.data();
          let dateStr = data.created_at ? new Date(data.created_at).toLocaleString('tr-TR') : 'Tarih Yok';
          
          html += <div class="submission-item" id="thread-">
            <div class="sub-header">
              <span class="sub-author"><i class="fas fa-user-circle"></i>  + (data.username || 'Ziyaretçi') +  (Kategori:  + (data.category || '') + )</span>
              <span class="sub-date"> + dateStr + </span>
            </div>
            <div style="margin-top: 5px; font-weight: bold; color: var(--neon-blue);"> + (data.title || '') + </div>
            <div class="sub-content"> + (data.content || '') + </div>
            <div class="sub-actions">
              <button class="btn-reject" onclick="deleteThread('')"><i class="fas fa-trash"></i> Siteden Sil</button>
            </div>
          </div>;
        });
        
        document.getElementById('discussionsList').innerHTML = html !== '' ? html : '<p style="color:var(--text-muted); text-align:center; padding: 20px;">Henüz sistemde kayıtlı bir forum başlığı bulunmamaktadır.</p>';
      } catch (e) {
        console.log("Forum başlıkları çekilemedi:", e);
      }
    }

    window.deleteThread = async function(id) {
        if(confirm("Bu forum başlığını silmek istediğinize emin misiniz? Siteden anında kalkacaktır.")) {
            try {
                await deleteDoc(doc(db, "forum_threads", id));
                document.getElementById('thread-' + id).remove();
                alert("Silindi.");
            } catch(e) {
                alert("Silme hatası: " + e.message);
            }
        }
    };
    window.loadDiscussions = loadDiscussions;
'''

# Find the end of module script to inject
content = content.replace('window.loadSubmissions = loadSubmissions;\n    loadSubmissions();\n  </script>', 'window.loadSubmissions = loadSubmissions;\n    loadSubmissions();\n' + js_logic + '\n    loadDiscussions();\n  </script>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("blgr.html guncellendi.")
