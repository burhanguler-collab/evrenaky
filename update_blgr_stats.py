import re

file_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\blgr.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add logic to fetch real stats
# I will replace document.getElementById("firebaseNotice").innerHTML part
# and add fetching logic.

new_js = '''
    document.getElementById("firebaseNotice").innerHTML = "<i class='fas fa-check-circle'></i> <strong>Sistem Uyarı:</strong> Firebase bağlantısı başarıyla kuruldu! Gerçek veritabanı aktif.";
    document.getElementById("firebaseNotice").style.borderColor = "#00ff88";
    document.getElementById("firebaseNotice").style.color = "#00ff88";
    document.getElementById("firebaseNotice").style.background = "rgba(0, 255, 136, 0.1)";

    // Fetch real stats
    import { doc, getDoc } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";
    async function loadStats() {
      try {
        const statsRef = doc(db, 'stats', 'global');
        const statsSnap = await getDoc(statsRef);
        if (statsSnap.exists()) {
          document.getElementById('totalViews').innerText = statsSnap.data().pageViews || 0;
          document.getElementById('totalPageViews').innerText = statsSnap.data().pageViews || 0;
        }
      } catch (e) {
        console.log("Stats fetch error", e);
      }
    }
    loadStats();
'''

content = content.replace('document.getElementById("firebaseNotice").innerHTML = "<i class=\'fas fa-check-circle\'></i> <strong>Sistem Uyarı:</strong> Firebase bağlantısı başarıyla kuruldu! Gerçek veritabanı aktif.";\n    document.getElementById("firebaseNotice").style.borderColor = "#00ff88";\n    document.getElementById("firebaseNotice").style.color = "#00ff88";\n    document.getElementById("firebaseNotice").style.background = "rgba(0, 255, 136, 0.1)";', new_js)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("blgr.html stats fetching eklendi.")
