import os
import re

file_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\blgr.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

firebase_script = '''
  <script type="module">
    import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js";
    import { getFirestore, collection, getDocs } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";

    const firebaseConfig = {
      apiKey: "AIzaSyAppAEZ5Q8RiR8NePuyXYvrM3OOAgKiRss",
      authDomain: "evrenaky-1f2a0.firebaseapp.com",
      projectId: "evrenaky-1f2a0",
      storageBucket: "evrenaky-1f2a0.firebasestorage.app",
      messagingSenderId: "717050093311",
      appId: "1:717050093311:web:8d8e29be23ddf112eef6ca",
      measurementId: "G-JMCPXZPLFF"
    };

    const app = initializeApp(firebaseConfig);
    const db = getFirestore(app);
    
    document.getElementById("firebaseNotice").innerHTML = "<i class='fas fa-check-circle'></i> <strong>Sistem Uyarı:</strong> Firebase bağlantısı başarıyla kuruldu! Gerçek veritabanı aktif.";
    document.getElementById("firebaseNotice").style.borderColor = "#00ff88";
    document.getElementById("firebaseNotice").style.color = "#00ff88";
    document.getElementById("firebaseNotice").style.background = "rgba(0, 255, 136, 0.1)";

    // Fetch submissions example (if you create a 'submissions' collection in Firestore)
    async function loadSubmissions() {
      try {
        const querySnapshot = await getDocs(collection(db, "submissions"));
        let html = '';
        querySnapshot.forEach((doc) => {
          let data = doc.data();
          html += <div class="submission-item">
            <div class="sub-header">
              <span class="sub-author"><i class="fas fa-user-circle"></i>  + (data.name || 'Bilinmeyen') + </span>
              <span class="sub-date"> + (data.date || '') + </span>
            </div>
            <div class="sub-content"> + (data.text || '') + </div>
            <div class="sub-actions">
              <button class="btn-reject"><i class="fas fa-times"></i> Reddet</button>
              <button class="btn-approve"><i class="fas fa-check"></i> Onayla & Yayınla</button>
            </div>
          </div>;
        });
        if(html !== '') {
            document.getElementById('submissionsList').innerHTML = html;
        }
      } catch (e) {
        console.log("Henüz 'submissions' koleksiyonu yok veya veri çekilemedi:", e);
      }
    }
    
    // Auto load when dashboard opens
    window.loadSubmissions = loadSubmissions;
  </script>
'''

# Insert the script before closing body tag
content = content.replace('</body>', firebase_script + '\n</body>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("blgr.html Firebase entegrasyonu tamamlandi.")
