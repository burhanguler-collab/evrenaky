import shutil

source = r'C:\Users\ASUS\.gemini\antigravity-ide\brain\f0440324-2db8-4b45-8aed-33c33a7243da\ring_oscillator_schematic_dark_1784299617907.png'
dest = r'c:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Gorseller\ring_oscillator_schematic_dark.png'

shutil.copyfile(source, dest)
print("Ring oscillator dark mode image copied.")
