import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js";
import { getFirestore, collection, addDoc, doc, setDoc, increment, getDocs, deleteDoc, query, orderBy, where } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";
import {
    getAuth,
    createUserWithEmailAndPassword,
    signInWithEmailAndPassword,
    signInWithPopup,
    GoogleAuthProvider,
    updateProfile,
    signOut,
    onAuthStateChanged,
    sendPasswordResetEmail
} from "https://www.gstatic.com/firebasejs/10.12.2/firebase-auth.js";

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
const auth = getAuth(app);

// Firebase hata kodlarını okunabilir Türkçe mesaja çevirir
function authHataMesaji(code) {
    if (!code) return 'Bilinmeyen bir hata oluştu.';
    const map = {
        'auth/email-already-in-use': 'Bu e-posta adresiyle zaten bir üyelik var. Giriş yapmayı deneyin.',
        'auth/invalid-email': 'Geçersiz e-posta adresi.',
        'auth/weak-password': 'Şifre en az 6 karakter olmalı.',
        'auth/missing-password': 'Lütfen şifrenizi girin.',
        'auth/invalid-credential': 'E-posta veya şifre hatalı.',
        'auth/wrong-password': 'E-posta veya şifre hatalı.',
        'auth/user-not-found': 'Bu e-postayla kayıtlı üye bulunamadı.',
        'auth/too-many-requests': 'Çok fazla deneme yapıldı. Lütfen biraz sonra tekrar deneyin.',
        'auth/popup-closed-by-user': 'Google penceresi kapatıldı, giriş tamamlanmadı.',
        'auth/operation-not-allowed': 'Bu giriş yöntemi Firebase Console\'da etkinleştirilmemiş.',
        'auth/network-request-failed': 'İnternet bağlantısı kurulamadı.',
        'auth/unauthorized-domain': 'Bu alan adı Firebase Console\'da yetkilendirilmemiş. Lütfen Authentication > Settings > Authorized domains listesine ekleyin.'
    };
    if (typeof code === 'string' && (code.includes('api-key-not-valid') || code.includes('invalid-api-key'))) {
        return 'auth/api-key-not-valid';
    }
    return map[code] || ('Hata: ' + code);
}

// Firebase kullanıcı nesnesini uygulamanın kullandığı sade biçime çevirir
function kullaniciBicimle(user) {
    if (!user) return null;
    return {
        id: user.uid,
        email: user.email,
        username: user.displayName || (user.email ? user.email.split('@')[0] : 'Üye')
    };
}

// Firestore kullanıcı belgesi oluşturma/güncelleme yardımcısı
async function kaydetVeyaGuncelleKullanici(user, extraData = {}) {
    if (!user) return;
    try {
        const userRef = doc(db, "users", user.uid);
        await setDoc(userRef, {
            uid: user.uid,
            email: user.email || '',
            username: user.displayName || (user.email ? user.email.split('@')[0] : 'Üye'),
            last_login: new Date().toISOString(),
            ...extraData
        }, { merge: true });
    } catch(e) {
        console.error("Firestore user doc save error:", e);
    }
}

window.firebaseAuth = {
    async kayitOl(email, password, username) {
        try {
            const cred = await createUserWithEmailAndPassword(auth, email, password);
            if (username) {
                await updateProfile(cred.user, { displayName: username });
            }
            await kaydetVeyaGuncelleKullanici(cred.user, { created_at: new Date().toISOString() });
            return { success: true, user: kullaniciBicimle(cred.user) };
        } catch (e) {
            return { success: false, message: authHataMesaji(e.code) };
        }
    },

    async girisYap(email, password) {
        try {
            const cred = await signInWithEmailAndPassword(auth, email, password);
            await kaydetVeyaGuncelleKullanici(cred.user);
            return { success: true, user: kullaniciBicimle(cred.user) };
        } catch (e) {
            return { success: false, message: authHataMesaji(e.code) };
        }
    },

    async googleIleGiris() {
        try {
            const cred = await signInWithPopup(auth, new GoogleAuthProvider());
            await kaydetVeyaGuncelleKullanici(cred.user, { created_at: new Date().toISOString() });
            return { success: true, user: kullaniciBicimle(cred.user) };
        } catch (e) {
            return { success: false, message: authHataMesaji(e.code) };
        }
    },

    async sifreSifirla(email) {
        try {
            await sendPasswordResetEmail(auth, email);
            return { success: true };
        } catch (e) {
            return { success: false, message: authHataMesaji(e.code) };
        }
    },

    async cikisYap() {
        await signOut(auth);
    },

    // Oturum değiştiğinde (giriş/çıkış/sayfa yenileme) çağrılır
    oturumIzle(callback) {
        onAuthStateChanged(auth, (user) => {
            if (user) {
                kaydetVeyaGuncelleKullanici(user);
            }
            callback(kullaniciBicimle(user));
        });
    },

    aktifKullanici() {
        return kullaniciBicimle(auth.currentUser);
    }
};

window.firebaseClient = {
    async getUsersCount() {
        try {
            const querySnapshot = await getDocs(collection(db, "users"));
            return querySnapshot.size;
        } catch(e) {
            console.error("Error fetching users count:", e);
            return 0;
        }
    },
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

    async getPendingReviews() {
        try {
            const q = query(collection(db, "submissions"), where("status", "==", "pending"));
            const querySnapshot = await getDocs(q);
            const reviews = [];
            querySnapshot.forEach((d) => {
                reviews.push({ id: d.id, ...d.data() });
            });
            reviews.sort((a, b) => new Date(a.created_at) - new Date(b.created_at));
            return reviews;
        } catch(e) {
            console.error("Error fetching pending reviews", e);
            return [];
        }
    },

    async approveReview(docId) {
        try {
            await setDoc(doc(db, "submissions", docId), { status: 'approved' }, { merge: true });
            return true;
        } catch(e) {
            console.error("Error approving review", e);
            return false;
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
            const querySnapshot = await getDocs(collection(db, "chapter_comments"));
            const comments = [];
            querySnapshot.forEach((doc) => {
                const data = doc.data();
                if (!chapterId || String(data.chapter_id).toLowerCase() === String(chapterId).toLowerCase()) {
                    comments.push({ id: doc.id, ...data });
                }
            });
            comments.sort((a, b) => new Date(b.created_at || 0) - new Date(a.created_at || 0));
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
            comments.sort((a, b) => new Date(b.created_at || 0) - new Date(a.created_at || 0));
            return comments;
        } catch(e) {
            return [];
        }
    },
    async getThreads() {
        try {
            const querySnapshot = await getDocs(collection(db, "forum_threads"));
            const threads = [];
            querySnapshot.forEach((doc) => {
                threads.push({ id: doc.id, ...doc.data() });
            });
            threads.sort((a, b) => new Date(b.created_at || 0) - new Date(a.created_at || 0));
            return threads;
        } catch(e) {
            console.error("Error fetching threads", e);
            return [];
        }
    },
    async getReplies(threadId) {
        try {
            const querySnapshot = await getDocs(collection(db, "forum_replies"));
            const replies = [];
            querySnapshot.forEach((doc) => {
                const data = doc.data();
                if (String(data.thread_id) === String(threadId) || String(data.post_id) === String(threadId)) {
                    replies.push({ id: doc.id, ...data });
                }
            });
            replies.sort((a, b) => new Date(a.created_at || 0) - new Date(b.created_at || 0));
            return replies;
        } catch(e) {
            console.warn("Error fetching replies:", e);
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

// app.js, Firebase geç yüklenirse üyelik sistemini bu olayla devreye alır
window.dispatchEvent(new Event('firebase-hazir'));

// Sayfa yüklendiğinde ziyareti Firebase'e kaydet
setTimeout(() => {
    if (window.firebaseClient) {
        window.firebaseClient.trackPageView();
    }
}, 1000);
