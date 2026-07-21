import re

# 1. UPDATE firebase-client.js
fb_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\firebase-client.js'
with open(fb_path, 'r', encoding='utf-8') as f:
    fb_content = f.read()

new_method = '''
    async getReviews() {
        try {
            const q = query(collection(db, "submissions"), where("status", "==", "approved"), orderBy("created_at", "desc"));
            const querySnapshot = await getDocs(q);
            const reviews = [];
            querySnapshot.forEach((doc) => {
                reviews.push({ id: doc.id, ...doc.data() });
            });
            return reviews;
        } catch(e) {
            console.error("Error fetching reviews", e);
            return [];
        }
    },
'''

if 'getReviews()' not in fb_content:
    fb_content = fb_content.replace('    async getThreads() {', new_method + '    async getThreads() {')
    with open(fb_path, 'w', encoding='utf-8') as f:
        f.write(fb_content)
    print("firebase-client.js updated.")

# 2. UPDATE app.js
app_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\app.js'
with open(app_path, 'r', encoding='utf-8') as f:
    app_content = f.read()

old_load_logic = '''    if (supabaseClient) {
        try {
            const { data, error } = await supabaseClient
                .from('peer_reviews')
                .select('*')
                .eq('status', 'approved')
                .order('created_at', { ascending: false });
            if (error) throw error;
            approvedReviews = data || [];
        } catch (err) {
            console.error("Supabase load approved reviews error:", err);
        }
    } else {
        // Local Mock DB
        initPeerReviewsMockData();
        const allReviews = JSON.parse(safeStorage.getItem('evrenaky_mock_peer_reviews') || '[]');
        approvedReviews = allReviews.filter(r => r.status === 'approved');
        // sort by date desc
        approvedReviews.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));
    }'''

new_load_logic = '''    if (window.firebaseClient) {
        approvedReviews = await window.firebaseClient.getReviews();
    } else {
        initPeerReviewsMockData();
        const allReviews = JSON.parse(safeStorage.getItem('evrenaky_mock_peer_reviews') || '[]');
        approvedReviews = allReviews.filter(r => r.status === 'approved');
        approvedReviews.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));
    }'''

app_content = app_content.replace(old_load_logic, new_load_logic)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(app_content)

print("app.js updated.")
