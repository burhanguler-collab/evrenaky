import shutil
import os

source = r'C:\Users\ASUS\.gemini\antigravity-ide\brain\f0440324-2db8-4b45-8aed-33c33a7243da\michelson_schematic_linear_1784295677370.png'
dest = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Gorseller\michelson_schematic_linear.png'

shutil.copyfile(source, dest)
print("Image copied to linear version.")
