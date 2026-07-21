import shutil
import os

src_dir = r'C:\Users\ASUS\Desktop\EvrenAKI\KITAP3\scratch_docx\word\media'
dest_dir = r'C:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Gorseller'

images_to_copy = {
    'image23.png': 'eksenel_itim_sema.png',
    'image24.png': 'eksenel_itim_vakum1.png',
    'image25.png': 'eksenel_itim_vakum2.png',
    'image26.png': 'eksenel_itim_grafik.png'
}

for src_name, dest_name in images_to_copy.items():
    src_path = os.path.join(src_dir, src_name)
    dest_path = os.path.join(dest_dir, dest_name)
    if os.path.exists(src_path):
        shutil.copyfile(src_path, dest_path)
        print(f"Copied {src_name} to {dest_name}")
    else:
        print(f"File {src_name} not found!")

