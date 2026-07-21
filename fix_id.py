import re

file_path = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\blgr.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("rejectSubmission('')", "rejectSubmission('')")
content = content.replace("approveSubmission('')", "approveSubmission('')")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("ID bug fixed.")
