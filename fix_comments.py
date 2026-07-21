import re

# 1. UPDATE firebase-client.js
fb_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\firebase-client.js'
with open(fb_path, 'r', encoding='utf-8') as f:
    fb_content = f.read()

new_methods = '''
    async submitComment(commentData) {
        try {
            const docRef = await addDoc(collection(db, "chapter_comments"), commentData);
            return { success: true, id: docRef.id };
        } catch(e) {
            console.error("Firebase submit comment error:", e);
            return { success: false };
        }
    },
    async getComments(chapterId) {
        try {
            const q = query(collection(db, "chapter_comments"), where("chapter_id", "==", chapterId));
            const querySnapshot = await getDocs(q);
            const comments = [];
            querySnapshot.forEach((doc) => {
                comments.push({ id: doc.id, ...doc.data() });
            });
            comments.sort((a, b) => new Date(a.created_at) - new Date(b.created_at));
            return comments;
        } catch(e) {
            console.error("Error fetching comments", e);
            return [];
        }
    },
    async getAllComments() {
        try {
            const querySnapshot = await getDocs(collection(db, "chapter_comments"));
            const comments = [];
            querySnapshot.forEach((doc) => {
                comments.push({ id: doc.id, ...doc.data() });
            });
            comments.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));
            return comments;
        } catch(e) {
            return [];
        }
    },
'''

if 'submitComment(' not in fb_content:
    fb_content = fb_content.replace('    async getThreads() {', new_methods + '    async getThreads() {')
    with open(fb_path, 'w', encoding='utf-8') as f:
        f.write(fb_content)

# 2. UPDATE app.js
app_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\app.js'
with open(app_path, 'r', encoding='utf-8') as f:
    app_content = f.read()

old_load_comments = '''    if (useMockBackend) {
        const allComments = JSON.parse(safeStorage.getItem('evrenaky_mock_comments') || '[]');
        comments = allComments.filter(c => c.chapter_id === chapterId);
    } else {
        const { data, error } = await supabase
            .from('comments')
            .select('*')
            .eq('chapter_id', chapterId)
            .order('created_at', { ascending: true });

        if (!error && data) {
            comments = data;
        }
    }'''

new_load_comments = '''    if (window.firebaseClient) {
        comments = await window.firebaseClient.getComments(chapterId);
    } else {
        const allComments = JSON.parse(safeStorage.getItem('evrenaky_mock_comments') || '[]');
        comments = allComments.filter(c => c.chapter_id === chapterId);
    }'''
app_content = app_content.replace(old_load_comments, new_load_comments)

old_submit_comment = '''    if (useMockBackend) {
        const allComments = JSON.parse(safeStorage.getItem('evrenaky_mock_comments') || '[]');
        const newComment = {
            id: String(Date.now()),
            chapter_id: activeChapterId,
            username: currentUser.username,
            content: content,
            created_at: new Date().toISOString()
        };
        allComments.push(newComment);
        safeStorage.setItem('evrenaky_mock_comments', JSON.stringify(allComments));
        textarea.value = '';
        loadComments(activeChapterId);
    } else {
        const { error } = await supabaseClient.from('comments').insert({
            chapter_id: activeChapterId,
            user_id: currentUser.id,
            username: currentUser.username,
            content: content
        });
        if (error) {
            alert(error.message);
        } else {
            textarea.value = '';
            loadComments(activeChapterId);
        }
    }'''

new_submit_comment = '''    const username = currentUser ? currentUser.username : "Ziyaretçi";
    if (window.firebaseClient) {
        await window.firebaseClient.submitComment({
            chapter_id: activeChapterId,
            username: username,
            content: content,
            created_at: new Date().toISOString()
        });
        textarea.value = '';
        loadComments(activeChapterId);
    } else {
        const allComments = JSON.parse(safeStorage.getItem('evrenaky_mock_comments') || '[]');
        const newComment = {
            id: String(Date.now()),
            chapter_id: activeChapterId,
            username: username,
            content: content,
            created_at: new Date().toISOString()
        };
        allComments.push(newComment);
        safeStorage.setItem('evrenaky_mock_comments', JSON.stringify(allComments));
        textarea.value = '';
        loadComments(activeChapterId);
    }'''
app_content = app_content.replace(old_submit_comment, new_submit_comment)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(app_content)

# 3. UPDATE blgr.html to show both Threads and Comments in the Forum tab
blgr_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\blgr.html'
with open(blgr_path, 'r', encoding='utf-8') as f:
    blgr_content = f.read()

# We need to modify loadDiscussions to fetch chapter_comments as well.
old_load_discussions = '''        const querySnapshot = await getDocs(collection(db, "forum_threads"));
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
'''

new_load_discussions = '''        const threadsSnap = await getDocs(collection(db, "forum_threads"));
        const commentsSnap = await getDocs(collection(db, "chapter_comments"));
        let html = '';
        
        threadsSnap.forEach((docSnap) => {
          let data = docSnap.data();
          let dateStr = data.created_at ? new Date(data.created_at).toLocaleString('tr-TR') : 'Tarih Yok';
          let cleanUser = data.username ? data.username.replace(/[&<>'"]/g, '') : 'Ziyaretçi';
          let cleanTitle = data.title ? data.title.replace(/[&<>'"]/g, '') : '';
          let cleanContent = data.content ? data.content.replace(/[&<>'"]/g, '') : '';
          let cleanCat = data.category ? data.category.replace(/[&<>'"]/g, '') : '';
          
          html += <div class="submission-item" id="thread-">
            <div class="sub-header">
              <span class="sub-author"><i class="fas fa-user-circle"></i>  <span style="font-size:12px;color:var(--text-muted);">(Forum Konusu: )</span></span>
              <span class="sub-date"></span>
            </div>
            <div style="margin-top: 5px; font-size: 16px; font-weight: bold; color: var(--neon-blue);"></div>
            <div class="sub-content"></div>
            <div class="sub-actions">
              <button class="btn-reject" onclick="deleteThread('')"><i class="fas fa-trash"></i> Siteden Sil</button>
            </div>
          </div>;
        });
        
        commentsSnap.forEach((docSnap) => {
          let data = docSnap.data();
          let dateStr = data.created_at ? new Date(data.created_at).toLocaleString('tr-TR') : 'Tarih Yok';
          let cleanUser = data.username ? data.username.replace(/[&<>'"]/g, '') : 'Ziyaretçi';
          let cleanContent = data.content ? data.content.replace(/[&<>'"]/g, '') : '';
          let cleanChap = data.chapter_id ? data.chapter_id.replace(/[&<>'"]/g, '') : '';
          
          html += <div class="submission-item" id="comment-">
            <div class="sub-header">
              <span class="sub-author"><i class="fas fa-comment-dots"></i>  <span style="font-size:12px;color:var(--text-muted);">(Bölüm Yorumu: )</span></span>
              <span class="sub-date"></span>
            </div>
            <div class="sub-content"></div>
            <div class="sub-actions">
              <button class="btn-reject" onclick="deleteComment('')"><i class="fas fa-trash"></i> Siteden Sil</button>
            </div>
          </div>;
        });
        
        document.getElementById('discussionsList').innerHTML = html !== '' ? html : '<p style="color:var(--text-muted); text-align:center; padding: 20px;">Henüz sistemde kayıtlı bir forum başlığı veya bölüm yorumu bulunmamaktadır.</p>';
'''
blgr_content = blgr_content.replace(old_load_discussions, new_load_discussions)

new_delete_comment = '''    window.deleteComment = async function(id) {
        if(confirm("Bu bölüm yorumunu silmek istediğinize emin misiniz?")) {
            try {
                await deleteDoc(doc(db, "chapter_comments", id));
                const el = document.getElementById('comment-' + id);
                if (el) el.remove();
            } catch(e) {
                alert("Silme hatası: " + e.message);
            }
        }
    };
'''

if 'window.deleteComment =' not in blgr_content:
    blgr_content = blgr_content.replace('window.deleteThread = async function', new_delete_comment + '\n    window.deleteThread = async function')
    
with open(blgr_path, 'w', encoding='utf-8') as f:
    f.write(blgr_content)

print("Chapter comments migrated to Firebase.")
