import tkinter as tk
import random
import threading
import winsound
import math

def play_sound(freq, duration):
    try:
        threading.Thread(target=winsound.Beep, args=(int(freq), int(duration)), daemon=True).start()
    except:
        pass

WIDTH, HEIGHT = 700, 900
SLICE_H = 25
NUM_SLICES = int(HEIGHT / SLICE_H) + 2

class RiverRaidPro:
    def __init__(self, root):
        self.root = root
        self.root.title("River Raid - Professional Edition")
        self.root.resizable(False, False)
        
        # Daha derin ve profesyonel bir nehir rengi
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT, bg="#0d2e52")
        self.canvas.pack()
        
        self.is_running = False
        self.game_started = False
        
        self.canvas.bind("<Button-1>", self.on_click)
        self.root.bind("<Left>", lambda e: self.set_dx(-1))
        self.root.bind("<Right>", lambda e: self.set_dx(1))
        self.root.bind("<KeyRelease-Left>", lambda e: self.set_dx(0))
        self.root.bind("<KeyRelease-Right>", lambda e: self.set_dx(0))
        self.root.bind("<Up>", lambda e: self.set_speed(10))
        self.root.bind("<KeyRelease-Up>", lambda e: self.set_speed(5))
        self.root.bind("<Down>", lambda e: self.set_speed(3))
        self.root.bind("<KeyRelease-Down>", lambda e: self.set_speed(5))
        self.root.bind("<space>", lambda e: self.shoot())
        
        self.show_start_screen()
        self.update_game()
        
    def show_start_screen(self):
        self.start_btn = self.canvas.create_rectangle(WIDTH/2-120, HEIGHT/2-30, WIDTH/2+120, HEIGHT/2+40, fill="#2c9c69", outline="#5cfcba", width=3)
        self.start_txt = self.canvas.create_text(WIDTH/2, HEIGHT/2+5, text="GÖREVE BAŞLA", fill="white", font=("Segoe UI", 22, "bold"))
        
        self.title_bg = self.canvas.create_text(WIDTH/2+3, HEIGHT/2 - 117, text="RIVER RAID PRO", fill="black", font=("Segoe UI", 48, "bold"))
        self.title_txt = self.canvas.create_text(WIDTH/2, HEIGHT/2 - 120, text="RIVER RAID PRO", fill="#f1c40f", font=("Segoe UI", 48, "bold"))
        
        self.controls_txt = self.canvas.create_text(WIDTH/2, HEIGHT/2 + 100, text="YÖN TUŞLARI: Uçuş | BOŞLUK: Füze", fill="#bdc3c7", font=("Segoe UI", 12, "bold"))

    def full_reset(self):
        self.canvas.delete("all")
        
        self.jet_x = WIDTH / 2
        self.jet_y = HEIGHT - 150
        self.jet_dx = 0
        self.speed = 5
        
        self.fuel = 100.0
        self.score = 0
        self.tick_count = 0
        
        self.slices = []
        self.enemies = []
        self.fuels = []
        self.bullets = []
        self.particles = []
        self.waves = []
        
        # Haritayı oluştur (Daha detaylı kara parçaları)
        lx, rx = 200, 500
        for i in range(NUM_SLICES):
            y = HEIGHT - i * SLICE_H
            # İki renkli 3D görünümlü kara parçaları
            id1_base = self.canvas.create_rectangle(0, y, lx, y+SLICE_H, fill="#1e5c2b", outline="")
            id1_edge = self.canvas.create_rectangle(lx-10, y, lx, y+SLICE_H, fill="#2ba343", outline="")
            
            id2_base = self.canvas.create_rectangle(rx, y, WIDTH, y+SLICE_H, fill="#1e5c2b", outline="")
            id2_edge = self.canvas.create_rectangle(rx, y, rx+10, y+SLICE_H, fill="#2ba343", outline="")
            
            self.slices.append({'y': y, 'lx': lx, 'rx': rx, 'id1b': id1_base, 'id1e': id1_edge, 'id2b': id2_base, 'id2e': id2_edge})
            
        # UI Elemanları
        self.score_bg = self.canvas.create_text(82, 32, text="SKOR: 0", fill="black", font=("Consolas", 20, "bold"))
        self.score_text = self.canvas.create_text(80, 30, text="SKOR: 0", fill="#ffffff", font=("Consolas", 20, "bold"))
        
        self.canvas.create_text(WIDTH - 220, 30, text="YAKIT", fill="white", font=("Consolas", 16, "bold"))
        self.fuel_bar_bg = self.canvas.create_rectangle(WIDTH - 170, 20, WIDTH - 20, 40, fill="#333333", outline="white", width=2)
        self.fuel_bar = self.canvas.create_rectangle(WIDTH - 170, 20, WIDTH - 20, 40, fill="#f1c40f", outline="")
        
        # Jet (Daha detaylı çokgen çizimi)
        self.jet_shadow = self.canvas.create_polygon(0,0, 0,0, 0,0, fill="#081e36")
        self.jet_wings = self.canvas.create_polygon(0,0, 0,0, 0,0, fill="#bdc3c7")
        self.jet_body = self.canvas.create_polygon(0,0, 0,0, 0,0, fill="#ffffff")
        self.jet_cockpit = self.canvas.create_polygon(0,0, 0,0, 0,0, fill="#3498db")
        self.jet_exhaust = self.canvas.create_polygon(0,0, 0,0, 0,0, fill="#e74c3c")
        
        self.is_running = True

    def set_dx(self, val):
        # Yumuşak hızlanma için hedef hız belirle (basitleştirilmiş)
        self.jet_dx = val * 7
        
    def set_speed(self, val):
        self.speed = val
            
    def on_click(self, event):
        x, y = event.x, event.y
        if not self.game_started:
            if WIDTH/2-120 <= x <= WIDTH/2+120 and HEIGHT/2-30 <= y <= HEIGHT/2+40:
                self.game_started = True
                self.full_reset()
        elif not self.is_running:
            if WIDTH/2-120 <= x <= WIDTH/2+120 and HEIGHT/2+110 <= y <= HEIGHT/2+160:
                self.full_reset()
                
    def shoot(self):
        if not self.is_running: return
        if len(self.bullets) < 4:
            play_sound(1800, 30)
            # Daha güzel mermi (lazer)
            bid = self.canvas.create_line(self.jet_x, self.jet_y-30, self.jet_x, self.jet_y-50, fill="#00ffff", width=5)
            self.bullets.append({'x': self.jet_x, 'y': self.jet_y-50, 'id': bid})
            
    def spawn_particles(self, x, y, color, count=15):
        for _ in range(count):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(2, 8)
            vx = math.cos(angle) * speed
            vy = math.sin(angle) * speed
            size = random.uniform(3, 8)
            pid = self.canvas.create_rectangle(x-size, y-size, x+size, y+size, fill=color, outline="")
            self.particles.append({'x': x, 'y': y, 'vx': vx, 'vy': vy, 'life': 20, 'id': pid})
        
    def update_game(self):
        if not self.is_running:
            if not self.game_started:
                self.root.after(16, self.update_game)
            return
            
        self.tick_count += 1
            
        # Yakıt (Hıza orantılı biraz artar ama sabit tüketim de var)
        self.fuel -= 0.05 + (self.speed * 0.005)
        if self.fuel <= 0:
            self.game_over("YAKIT BİTTİ!")
            return
            
        # Jet Hareketi (Sınırları aşmasını yumuşatılmış şekilde engelle)
        self.jet_x += self.jet_dx
        
        # Arkaplan Dalgaları
        if random.random() < 0.2:
            wx = random.randint(200, 500)
            wid = self.canvas.create_line(wx, -10, wx+random.randint(10, 30), -10, fill="#154a87", width=2)
            self.waves.append({'y': -10, 'id': wid})
            
        for w in self.waves[:]:
            w['y'] += self.speed
            self.canvas.move(w['id'], 0, self.speed)
            if w['y'] > HEIGHT:
                self.canvas.delete(w['id'])
                self.waves.remove(w)
        
        # Nehir Kaydırması
        for s in self.slices:
            s['y'] += self.speed
            
        while self.slices[0]['y'] >= HEIGHT:
            s = self.slices.pop(0)
            top_y = self.slices[-1]['y']
            lx = self.slices[-1]['lx']
            rx = self.slices[-1]['rx']
            
            # Daha pürüzsüz kara oluşumu
            if random.random() < 0.4: lx += random.choice([-SLICE_H, SLICE_H])
            if random.random() < 0.4: rx += random.choice([-SLICE_H, SLICE_H])
            
            lx = max(30, min(lx, WIDTH/2 - 70))
            rx = min(WIDTH - 30, max(rx, WIDTH/2 + 70))
            if rx - lx < 180: # Min genişlik
                lx -= SLICE_H; rx += SLICE_H
                
            s['y'] = top_y - SLICE_H
            s['lx'] = lx
            s['rx'] = rx
            self.slices.append(s)
            
            # Nesne Üretimi (Daha gelişmiş)
            if random.random() < 0.06:
                fx = random.randint(int(lx)+40, int(rx)-40)
                # 3D görünümlü yakıt varili
                fid1 = self.canvas.create_rectangle(fx-12, s['y']-18, fx+12, s['y']+18, fill="#e67e22", outline="black")
                fid2 = self.canvas.create_rectangle(fx-12, s['y']-18, fx+12, s['y']-10, fill="#d35400", outline="")
                tid = self.canvas.create_text(fx, s['y'], text="FUEL", fill="white", font=("Arial", 7, "bold"))
                self.fuels.append({'x': fx, 'y': s['y'], 'ids': [fid1, fid2, tid]})
            elif random.random() < 0.09:
                ex = random.randint(int(lx)+40, int(rx)-40)
                # Gemi (Savaş Gemisi Görünümü)
                eid1 = self.canvas.create_polygon(ex-25, s['y']-10, ex+25, s['y']-10, ex+15, s['y']+10, ex-15, s['y']+10, fill="#7f8c8d", outline="black")
                eid2 = self.canvas.create_rectangle(ex-10, s['y']-15, ex+10, s['y'], fill="#95a5a6", outline="black")
                edx = random.choice([-2, 2]) if random.random() < 0.6 else 0
                self.enemies.append({'x': ex, 'y': s['y'], 'ids': [eid1, eid2], 'dx': edx})
                
        # Çizimleri Güncelle ve Duvar Çarpışması
        for s in self.slices:
            self.canvas.coords(s['id1b'], 0, s['y'], s['lx']-10, s['y']+SLICE_H+2)
            self.canvas.coords(s['id1e'], s['lx']-10, s['y'], s['lx'], s['y']+SLICE_H+2)
            self.canvas.coords(s['id2b'], s['rx']+10, s['y'], WIDTH, s['y']+SLICE_H+2)
            self.canvas.coords(s['id2e'], s['rx'], s['y'], s['rx']+10, s['y']+SLICE_H+2)
            
            if abs(s['y'] - self.jet_y) < SLICE_H:
                if self.jet_x - 20 < s['lx'] or self.jet_x + 20 > s['rx']:
                    self.spawn_particles(self.jet_x, self.jet_y, "#e74c3c", 40)
                    self.game_over("KARA'YA ÇARPTIN!")
                    return
                    
        # Yakıt Varilleri
        for f in self.fuels[:]:
            f['y'] += self.speed
            for i in f['ids']: self.canvas.move(i, 0, self.speed)
            
            if abs(f['y'] - self.jet_y) < 35 and abs(f['x'] - self.jet_x) < 30:
                play_sound(2200, 60)
                self.spawn_particles(f['x'], f['y'], "#f1c40f", 10)
                self.fuel = min(100.0, self.fuel + 40.0)
                for i in f['ids']: self.canvas.delete(i)
                self.fuels.remove(f)
            elif f['y'] > HEIGHT + 50:
                for i in f['ids']: self.canvas.delete(i)
                self.fuels.remove(f)
                
        # Düşmanlar
        for e in self.enemies[:]:
            e['y'] += self.speed
            e['x'] += e['dx']
            for i in e['ids']: self.canvas.move(i, e['dx'], self.speed)
            
            if abs(e['y'] - self.jet_y) < 30 and abs(e['x'] - self.jet_x) < 35:
                self.spawn_particles(self.jet_x, self.jet_y, "#e74c3c", 50)
                self.game_over("DÜŞMANA ÇARPTIN!")
                return
            elif e['y'] > HEIGHT + 50:
                for i in e['ids']: self.canvas.delete(i)
                self.enemies.remove(e)
                
        # Mermiler
        for b in self.bullets[:]:
            b['y'] -= 20
            self.canvas.move(b['id'], 0, -20)
            
            hit = False
            for e in self.enemies[:]:
                if abs(b['x'] - e['x']) < 30 and abs(b['y'] - e['y']) < 20:
                    play_sound(300, 100)
                    self.spawn_particles(e['x'], e['y'], "#e74c3c", 20)
                    self.score += 50
                    for i in e['ids']: self.canvas.delete(i)
                    self.enemies.remove(e)
                    hit = True
                    break
                    
            if not hit:
                for f in self.fuels[:]:
                    if abs(b['x'] - f['x']) < 25 and abs(b['y'] - f['y']) < 25:
                        play_sound(250, 150)
                        self.spawn_particles(f['x'], f['y'], "#e67e22", 20)
                        self.score += 80
                        for i in f['ids']: self.canvas.delete(i)
                        self.fuels.remove(f)
                        hit = True
                        break
                        
            if hit or b['y'] < 0:
                self.canvas.delete(b['id'])
                self.bullets.remove(b)
                
        # Partiküller (Patlama Efektleri)
        for p in self.particles[:]:
            p['x'] += p['vx']
            p['y'] += p['vy']
            p['life'] -= 1
            self.canvas.move(p['id'], p['vx'], p['vy'])
            if p['life'] <= 0:
                self.canvas.delete(p['id'])
                self.particles.remove(p)
                
        # Arayüzü Güncelle
        self.canvas.itemconfig(self.score_text, text=f"SKOR: {self.score}")
        self.canvas.itemconfig(self.score_bg, text=f"SKOR: {self.score}")
        
        # Yakıt Barı
        fw = (self.fuel / 100.0) * 150
        color = "#f1c40f" if self.fuel > 30 else "#e74c3c"
        self.canvas.coords(self.fuel_bar, WIDTH - 170, 20, WIDTH - 170 + fw, 40)
        self.canvas.itemconfig(self.fuel_bar, fill=color)
        
        # Profesyonel Jet Çizimi
        jx, jy = self.jet_x, self.jet_y
        # Gölge
        self.canvas.coords(self.jet_shadow, jx-25, jy+15, jx, jy-25, jx+35, jy+25, jx, jy+35)
        # Kanatlar
        self.canvas.coords(self.jet_wings, jx-30, jy+10, jx, jy-5, jx+30, jy+10, jx, jy+20)
        # Gövde
        self.canvas.coords(self.jet_body, jx-8, jy+25, jx-5, jy-25, jx, jy-35, jx+5, jy-25, jx+8, jy+25)
        # Kokpit
        self.canvas.coords(self.jet_cockpit, jx-4, jy-5, jx, jy-15, jx+4, jy-5, jx, jy+5)
        # Egzoz Ateşi (Titreşimli)
        if self.tick_count % 4 < 2:
            self.canvas.coords(self.jet_exhaust, jx-5, jy+25, jx, jy+40, jx+5, jy+25)
        else:
            self.canvas.coords(self.jet_exhaust, jx-4, jy+25, jx, jy+35, jx+4, jy+25)
        
        # Z-Index ayarlamaları
        self.canvas.tag_raise(self.score_bg)
        self.canvas.tag_raise(self.score_text)
        self.canvas.tag_raise(self.fuel_bar_bg)
        self.canvas.tag_raise(self.fuel_bar)
        
        self.canvas.tag_raise(self.jet_shadow)
        self.canvas.tag_raise(self.jet_wings)
        self.canvas.tag_raise(self.jet_body)
        self.canvas.tag_raise(self.jet_cockpit)
        self.canvas.tag_raise(self.jet_exhaust)
        
        self.root.after(16, self.update_game)
        
    def game_over(self, reason):
        self.is_running = False
        play_sound(120, 800)
        
        # Siyah filtre
        self.canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="black", stipple="gray50")
        
        self.canvas.create_text(WIDTH/2+3, HEIGHT/2 - 17, text=reason, fill="black", font=("Segoe UI", 48, "bold"))
        self.canvas.create_text(WIDTH/2, HEIGHT/2 - 20, text=reason, fill="#e74c3c", font=("Segoe UI", 48, "bold"))
        
        self.canvas.create_text(WIDTH/2, HEIGHT/2 + 40, text=f"SON SKOR: {self.score}", fill="#f1c40f", font=("Consolas", 30, "bold"))
        
        self.restart_btn = self.canvas.create_rectangle(WIDTH/2-120, HEIGHT/2+110, WIDTH/2+120, HEIGHT/2+160, fill="#3498db", outline="white", width=3)
        self.restart_txt = self.canvas.create_text(WIDTH/2, HEIGHT/2+135, text="YENİDEN BAŞLAT", fill="white", font=("Segoe UI", 16, "bold"))

if __name__ == "__main__":
    root = tk.Tk()
    app = RiverRaidPro(root)
    root.mainloop()
