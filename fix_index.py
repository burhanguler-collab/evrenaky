import re

fb_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\firebase-client.js'
with open(fb_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Avoid Firebase composite index error by just using where and sorting locally
content = content.replace(
    'const q = query(collection(db, "submissions"), where("status", "==", "approved"), orderBy("created_at", "desc"));',
    'const q = query(collection(db, "submissions"), where("status", "==", "approved"));'
)

# And sort locally
old_sort_logic = '''            querySnapshot.forEach((doc) => {
                reviews.push({ id: doc.id, ...doc.data() });
            });
            return reviews;'''

new_sort_logic = '''            querySnapshot.forEach((doc) => {
                reviews.push({ id: doc.id, ...doc.data() });
            });
            reviews.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));
            return reviews;'''

content = content.replace(old_sort_logic, new_sort_logic)

with open(fb_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Avoided index requirement")
