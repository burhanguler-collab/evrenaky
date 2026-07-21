import shutil

source = r'C:\Users\ASUS\.gemini\antigravity-ide\brain\f0440324-2db8-4b45-8aed-33c33a7243da\attometer_schematic_dark_1784301048302.png'
dest = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Gorseller\attometer_schematic_dark.png'

shutil.copyfile(source, dest)
print("Attometer dark mode image copied.")
