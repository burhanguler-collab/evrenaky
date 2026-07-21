import shutil

source = r'C:\Users\ASUS\.gemini\antigravity-ide\brain\f0440324-2db8-4b45-8aed-33c33a7243da\michelson_schematic_dark_fixed_1784295936641.png'
dest = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Gorseller\michelson_schematic_dark.png'

shutil.copyfile(source, dest)
print("Dark mode image with single line copied.")
