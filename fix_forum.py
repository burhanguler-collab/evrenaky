import re

app_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\app.js'
with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update loadForumThreads
old_load_threads = '''    if (useMockBackend) {
        const allPosts = JSON.parse(safeStorage.getItem('evrenaky_mock_posts') || '[]');
        posts = category === 'all' ? allPosts : allPosts.filter(p => p.category === category);
    } else {
        let query = supabaseClient.from('forum_posts').select('*');
        if (category !== 'all') {
            query = query.eq('category', category);
        }
        const { data, error } = await query.order('created_at', { ascending: false });
        if (!error && data) posts = data;
    }'''

new_load_threads = '''    if (window.firebaseClient) {
        const allPosts = await window.firebaseClient.getThreads();
        posts = category === 'all' ? allPosts : allPosts.filter(p => p.category === category);
    } else {
        const allPosts = JSON.parse(safeStorage.getItem('evrenaky_mock_posts') || '[]');
        posts = category === 'all' ? allPosts : allPosts.filter(p => p.category === category);
    }'''
content = content.replace(old_load_threads, new_load_threads)

# 2. Update openThreadDetail
old_open_thread = '''    if (useMockBackend) {
        const allPosts = JSON.parse(safeStorage.getItem('evrenaky_mock_posts') || '[]');
        post = allPosts.find(p => p.id === threadId);
    } else {
        const { data, error } = await supabaseClient.from('forum_posts').select('*').eq('id', threadId).single();
        if (!error && data) post = data;
    }'''

new_open_thread = '''    if (window.firebaseClient) {
        const allPosts = await window.firebaseClient.getThreads();
        post = allPosts.find(p => p.id === threadId);
    } else {
        const allPosts = JSON.parse(safeStorage.getItem('evrenaky_mock_posts') || '[]');
        post = allPosts.find(p => p.id === threadId);
    }'''
content = content.replace(old_open_thread, new_open_thread)

# 3. Update loadReplies
old_load_replies = '''    if (useMockBackend) {
        const allReplies = JSON.parse(safeStorage.getItem('evrenaky_mock_replies') || '[]');
        replies = allReplies.filter(r => r.post_id === threadId);
    } else {
        const { data, error } = await supabaseClient
            .from('forum_replies')
            .select('*')
            .eq('post_id', threadId)
            .order('created_at', { ascending: true });
        if (!error && data) replies = data;
    }'''

new_load_replies = '''    if (window.firebaseClient) {
        replies = await window.firebaseClient.getReplies(threadId);
    } else {
        const allReplies = JSON.parse(safeStorage.getItem('evrenaky_mock_replies') || '[]');
        replies = allReplies.filter(r => r.post_id === threadId);
    }'''
content = content.replace(old_load_replies, new_load_replies)

# 4. Update submitReply
old_submit_reply = '''    if (useMockBackend) {
        const allReplies = JSON.parse(safeStorage.getItem('evrenaky_mock_replies') || '[]');
        const newReply = {
            id: String(Date.now()),
            post_id: activeThreadId,
            username: currentUser.username,
            content: content,
            created_at: new Date().toISOString()
        };
        allReplies.push(newReply);
        safeStorage.setItem('evrenaky_mock_replies', JSON.stringify(allReplies));
        textarea.value = '';
        loadReplies(activeThreadId);
    } else {
        const { error } = await supabaseClient.from('forum_replies').insert({
            post_id: activeThreadId,
            user_id: currentUser.id,
            username: currentUser.username,
            content: content
        });
        if (error) {
            alert(error.message);
        } else {
            textarea.value = '';
            loadReplies(activeThreadId);
        }
    }'''

new_submit_reply = '''    const username = currentUser ? currentUser.username : "Ziyaretçi";
    if (window.firebaseClient) {
        await window.firebaseClient.submitReply({
            thread_id: activeThreadId,
            username: username,
            content: content,
            created_at: new Date().toISOString()
        });
        textarea.value = '';
        loadReplies(activeThreadId);
    } else {
        const allReplies = JSON.parse(safeStorage.getItem('evrenaky_mock_replies') || '[]');
        const newReply = {
            id: String(Date.now()),
            post_id: activeThreadId,
            username: username,
            content: content,
            created_at: new Date().toISOString()
        };
        allReplies.push(newReply);
        safeStorage.setItem('evrenaky_mock_replies', JSON.stringify(allReplies));
        textarea.value = '';
        loadReplies(activeThreadId);
    }'''
content = content.replace(old_submit_reply, new_submit_reply)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Forum logic completely updated for Firebase.")
