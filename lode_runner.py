import tkinter as tk

CELL = 40
COLS = 20
ROWS = 15

# Harita Efsanesi:
# . : Boşluk
# X : Tuğla (Kazılabilir)
# S : Beton (Kazılamaz - alt sınır için)
# H : Merdiven
# - : İp / Bar
# * : Altın
LEVEL = [
    "....................",
    "....................",
    "...*...........*....",
    "XXXXXXHHXXXXXXX-XXXX",
    ".....XHHX.....X.X...",
    "...*.XHHX..*..X.X...",
    "XXXXXXHHXXXXXXX.XXXX",
    "...*.XHHX.......X...",
    ".....XHHX...*...X...",
    "XXXXXXHHXXXXXXXXX...",
    ".....XHHX.......X...",
    ".....XHHX.......X...",
    "XXXXXXXXXXXXXXXXXXXX",
    "SSSSSSSSSSSSSSSSSSSS",
    "SSSSSSSSSSSSSSSSSSSS",
]

class LodeRunner:
    def __init__(self, root):
        self.root = root
        self.root.title("Nostaljik Lode Runner (Mini)")
        self.root.resizable(False, False)
        
        self.canvas = tk.Canvas(root, width=COLS*CELL, height=ROWS*CELL, bg="#0b0f19")
        self.canvas.pack()
        
        self.grid = [list(row) for row in LEVEL]
        self.gold_total = sum(row.count('*') for row in LEVEL)
        self.gold_collected = 0
        
        # Oyuncu (Px, Py)
        self.px = 2
        self.py = 2
        
        # Düşman (Muhafız)
        self.gx = 18
        self.gy = 2
        self.gdir = -1
        
        self.holes = {} # (x, y) -> kalan_zaman
        
        self.root.bind("<Left>", lambda e: self.try_move(-1, 0))
        self.root.bind("<Right>", lambda e: self.try_move(1, 0))
        self.root.bind("<Up>", lambda e: self.try_move(0, -1))
        self.root.bind("<Down>", lambda e: self.try_move(0, 1))
        self.root.bind("z", lambda e: self.dig(-1))
        self.root.bind("x", lambda e: self.dig(1))
        
        self.is_running = True
        self.draw()
        self.tick()
        
    def get_tile(self, x, y):
        if 0 <= x < COLS and 0 <= y < ROWS:
            return self.grid[y][x]
        return 'S' # Dışarısı beton
        
    def can_stand(self, x, y):
        # Üzerinde durduğumuz yer ip veya merdiven mi?
        t = self.get_tile(x, y)
        if t in ['H', '-']: return True
        # Altımız dolu mu?
        b = self.get_tile(x, y+1)
        if b in ['X', 'S', 'H']: return True
        return False
        
    def try_move(self, dx, dy):
        if not self.is_running: return
        # Düşüyorsak sağa sola gidemeyiz
        if not self.can_stand(self.px, self.py) and dy == 0:
            return
            
        nx, ny = self.px + dx, self.py + dy
        if 0 <= nx < COLS and 0 <= ny < ROWS:
            t = self.get_tile(nx, ny)
            if t not in ['X', 'S']:
                if dy == -1: # Yukarı çıkma
                    if self.get_tile(self.px, self.py) == 'H' or t == 'H':
                        self.px, self.py = nx, ny
                elif dy == 1: # Aşağı inme
                    if t == 'H' or self.get_tile(self.px, self.py) == 'H' or t == '.':
                        self.px, self.py = nx, ny
                else: # Sağa Sola
                    self.px, self.py = nx, ny
                    
        self.check_collect()
        self.draw()
        
    def dig(self, dx):
        if not self.is_running: return
        # Sadece yere basarken kazabiliriz
        if not self.can_stand(self.px, self.py): return
        
        tx, ty = self.px + dx, self.py + 1
        # Hedef X (Tuğla) olmalı ve üstü boş olmalı
        if self.get_tile(tx, ty) == 'X' and self.get_tile(tx, ty-1) in ['.', '*']:
            self.grid[ty][tx] = '.'
            self.holes[(tx, ty)] = 40 # Yaklaşık 6 saniye (150ms * 40)
        self.draw()
        
    def check_collect(self):
        if self.get_tile(self.px, self.py) == '*':
            self.grid[self.py][self.px] = '.'
            self.gold_collected += 1
            if self.gold_collected == self.gold_total:
                self.is_running = False
                self.draw()
                self.canvas.create_text(COLS*CELL/2, ROWS*CELL/2, text="KAZANDINIZ!", fill="#34d399", font=("Arial", 40, "bold"))
                
    def tick(self):
        if not self.is_running: return
        
        # 1. Oyuncu Yerçekimi
        if not self.can_stand(self.px, self.py):
            self.py += 1
            self.check_collect()
            
        # 2. Düşman Yapay Zekası
        if not self.can_stand(self.gx, self.gy):
            self.gy += 1 # Düşer
        else:
            if (self.gx, self.gy) in self.holes:
                pass # Çukurda sıkıştı
            else:
                nx = self.gx + self.gdir
                t = self.get_tile(nx, self.gy)
                if t not in ['X', 'S']:
                    self.gx = nx
                else:
                    self.gdir *= -1 # Duvara çarpınca dön
                    
        # 3. Çarpışma Kontrolü
        if self.px == self.gx and self.py == self.gy:
            self.is_running = False
            self.draw()
            self.canvas.create_text(COLS*CELL/2, ROWS*CELL/2, text="YAKALANDIN!", fill="#f87171", font=("Arial", 40, "bold"))
            return
            
        # 4. Çukurların Kapanması
        to_remove = []
        for (hx, hy) in self.holes.keys():
            self.holes[(hx, hy)] -= 1
            if self.holes[(hx, hy)] <= 0:
                self.grid[hy][hx] = 'X'
                to_remove.append((hx, hy))
                # Çukur kapanırken içindeysek ölürüz
                if self.px == hx and self.py == hy:
                    self.is_running = False
                    self.draw()
                    self.canvas.create_text(COLS*CELL/2, ROWS*CELL/2, text="ÇUKURDA KALDIN!", fill="#f87171", font=("Arial", 40, "bold"))
                    return
                # Düşman içindeyse yeniden doğar
                if self.gx == hx and self.gy == hy:
                    self.gx, self.gy = 18, 2
                    
        for k in to_remove:
            del self.holes[k]
            
        self.draw()
        self.root.after(150, self.tick) # Her 150ms'de bir "Turn"
        
    def draw(self):
        self.canvas.delete("all")
        for y in range(ROWS):
            for x in range(COLS):
                t = self.grid[y][x]
                cx, cy = x*CELL, y*CELL
                
                if t == 'X': # Tuğla
                    self.canvas.create_rectangle(cx, cy, cx+CELL, cy+CELL, fill="#b22222", outline="#8b0000")
                elif t == 'S': # Beton
                    self.canvas.create_rectangle(cx, cy, cx+CELL, cy+CELL, fill="#696969", outline="#404040")
                elif t == 'H': # Merdiven
                    self.canvas.create_line(cx+10, cy, cx+10, cy+CELL, fill="#fff8dc", width=2)
                    self.canvas.create_line(cx+30, cy, cx+30, cy+CELL, fill="#fff8dc", width=2)
                    for i in range(4):
                        self.canvas.create_line(cx+10, cy+10*i+5, cx+30, cy+10*i+5, fill="#fff8dc", width=2)
                elif t == '-': # İp
                    self.canvas.create_line(cx, cy+10, cx+CELL, cy+10, fill="white", width=2)
                elif t == '*': # Altın
                    self.canvas.create_oval(cx+10, cy+15, cx+30, cy+35, fill="gold")
                    
        # Kapanmak üzere olan çukurları uyar (Kırmızı yanıp sönme)
        for (hx, hy), timer in self.holes.items():
            cx, cy = hx*CELL, hy*CELL
            if timer < 10 and timer % 2 == 0:
                self.canvas.create_rectangle(cx, cy, cx+CELL, cy+CELL, fill="#ffb020", outline="")
                
        # Düşman Çizimi (Kırmızı Adam)
        gx, gy = self.gx*CELL, self.gy*CELL
        self.canvas.create_oval(gx+5, gy+5, gx+CELL-5, gy+CELL-5, fill="#f87171")
        
        # Oyuncu Çizimi (Beyaz/Açık Mavi Adam)
        px, py = self.px*CELL, self.py*CELL
        self.canvas.create_oval(px+5, py+5, px+CELL-5, py+CELL-5, fill="#00e5ff")
        
        # Skor/UI
        self.canvas.create_text(80, 15, text=f"Altınlar: {self.gold_collected} / {self.gold_total}", fill="white", font=("Arial", 12, "bold"))
        self.canvas.create_text(COLS*CELL - 150, 15, text="Z: Sola Kaz | X: Sağa Kaz", fill="white", font=("Arial", 10))

if __name__ == "__main__":
    root = tk.Tk()
    app = LodeRunner(root)
    root.mainloop()
