import re

file_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\blgr.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's clean up the bottom of the script block entirely and re-write it correctly.
# Find where loadSubmissions() ends.
end_marker = "window.loadSubmissions = loadSubmissions;"
parts = content.split(end_marker)

if len(parts) >= 2:
    base_content = parts[0] + end_marker + "\n    loadSubmissions();\n"
    
    js_logic = '''
    import { deleteDoc } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";
    
    async function loadDiscussions() {
      try {
        const querySnapshot = await getDocs(collection(db, "forum_threads"));
        let html = '';
        querySnapshot.forEach((docSnap) => {
          let data = docSnap.data();
          let dateStr = data.created_at ? new Date(data.created_at).toLocaleString('tr-TR') : 'Tarih Yok';
          
          let cleanUser = data.username ? data.username.replace(/[&<>'"]/g, '') : 'Ziyaretçi';
          let cleanTitle = data.title ? data.title.replace(/[&<>'"]/g, '') : '';
          let cleanContent = data.content ? data.content.replace(/[&<>'"]/g, '') : '';
          let cleanCat = data.category ? data.category.replace(/[&<>'"]/g, '') : '';
          
          html += <div class="submission-item" id="thread-">
            <div class="sub-header">
              <span class="sub-author"><i class="fas fa-user-circle"></i>  <span style="font-size:12px;color:var(--text-muted);">(Kategori: )</span></span>
              <span class="sub-date"></span>
            </div>
            <div style="margin-top: 5px; font-size: 16px; font-weight: bold; color: var(--neon-blue);"></div>
            <div class="sub-content"></div>
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
        if(confirm("Bu tartışma konusunu tamamen silmek istediğinize emin misiniz? Siteden anında kaldırılacaktır.")) {
            try {
                await deleteDoc(doc(db, "forum_threads", id));
                const el = document.getElementById('thread-' + id);
                if (el) el.remove();
                alert("Başarıyla silindi.");
            } catch(e) {
                alert("Silme hatası: " + e.message);
            }
        }
    };
    
    window.loadDiscussions = loadDiscussions;
    loadDiscussions();

  </script>
</body>
</html>
'''
    final_content = base_content + js_logic
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print("Fixed blgr.html")
else:
    print("Could not find marker")

