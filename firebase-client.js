import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js";
import { getFirestore, collection, addDoc, doc, setDoc, increment, getDocs, deleteDoc, query, orderBy, where } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";

const firebaseConfig = {
  apiKey: "AIzaSyAppAEZ5Q8RiR8NePuYXYvrM3OOAgKiRss",
  authDomain: "evrenaky-1f2a0.firebaseapp.com",
  projectId: "evrenaky-1f2a0",
  storageBucket: "evrenaky-1f2a0.firebasestorage.app",
  messagingSenderId: "717050093311",
  appId: "1:717050093311:web:8d8e29be23ddf112eef6ca",
  measurementId: "G-JMCPXZPLFF"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

window.firebaseClient = {
    async submitReview(reviewData) {
        try {
            await addDoc(collection(db, "submissions"), reviewData);
            return true;
        } catch(e) {
            console.error("Firebase submit error:", e);
            return false;
        }
    },

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

    async getReviews() {
        try {
            const q = query(collection(db, "submissions"), where("status", "==", "approved"));
            const querySnapshot = await getDocs(q);
            const reviews = [];
            querySnapshot.forEach((doc) => {
                reviews.push({ id: doc.id, ...doc.data() });
            });
            reviews.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));
            return reviews;
        } catch(e) {
            console.error("Error fetching reviews", e);
            return [];
        }
    },

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

    async trackPageView() {
        try {
            const statsRef = doc(db, 'stats', 'global');
            await setDoc(statsRef, {
                pageViews: increment(1)
            }, { merge: true });
        } catch(e) {
            console.error("Firebase stats update error:", e);
        }
    }
};

// Sayfa yüklendiğinde ziyareti Firebase'e kaydet
setTimeout(() => {
    if (window.firebaseClient) {
        window.firebaseClient.trackPageView();
    }
}, 1000);
