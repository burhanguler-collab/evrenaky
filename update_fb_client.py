import re

file_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\firebase-client.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace imports
content = content.replace(
    'import { getFirestore, collection, addDoc, doc, setDoc, increment } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";',
    'import { getFirestore, collection, addDoc, doc, setDoc, increment, getDocs, deleteDoc, query, orderBy, where } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";'
)

new_methods = '''
    async submitThread(threadData) {
        try {
            const docRef = await addDoc(collection(db, "forum_threads"), threadData);
            return { success: true, id: docRef.id };
        } catch(e) {
            console.error("Firebase submit thread error:", e);
            return { success: false };
        }
    },
    async submitReply(replyData) {
        try {
            const docRef = await addDoc(collection(db, "forum_replies"), replyData);
            return { success: true, id: docRef.id };
        } catch(e) {
            console.error("Firebase submit reply error:", e);
            return { success: false };
        }
    },
    async getThreads() {
        try {
            const q = query(collection(db, "forum_threads"), orderBy("created_at", "desc"));
            const querySnapshot = await getDocs(q);
            const threads = [];
            querySnapshot.forEach((doc) => {
                threads.push({ id: doc.id, ...doc.data() });
            });
            return threads;
        } catch(e) {
            console.error("Error fetching threads", e);
            return [];
        }
    },
    async getReplies(threadId) {
        try {
            const q = query(collection(db, "forum_replies"), where("thread_id", "==", threadId), orderBy("created_at", "asc"));
            const querySnapshot = await getDocs(q);
            const replies = [];
            querySnapshot.forEach((doc) => {
                replies.push({ id: doc.id, ...doc.data() });
            });
            return replies;
        } catch(e) {
            console.error("Error fetching replies", e);
            return [];
        }
    },
    async deleteDocument(collectionName, docId) {
        try {
            await deleteDoc(doc(db, collectionName, docId));
            return true;
        } catch(e) {
            console.error("Error deleting doc", e);
            return false;
        }
    },
'''

content = content.replace('    async trackPageView() {', new_methods + '\n    async trackPageView() {')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("firebase-client.js guncellendi.")
