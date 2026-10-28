import tkinter as tk
import random
import time

WIDTH, HEIGHT = 480, 720
BG = "#111316"
GRID = "#22252a"
PLAYER_COLOR = "#4ea1ff"
OBST_COLORS = ["#e14c4c", "#f4b942", "#55c68d"]

class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Dodger - Tkinter")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT, bg=BG, highlightthickness=0)
        self.canvas.pack()

        # وضعیت‌ها
        self.running = True
        self.paused = False
        self.game_over = False

        # ورودی‌ها
        self.keys = {"Left": False, "Right": False, "Up": False, "Down": False}

        # UI
        self.score = 0.0
        self.last_time = time.time()
        self.info_text = None
        self.score_text = None

        # تنظیمات گیم‌پلی
        self.player_speed = 6
        self.obstacles = []
        self.spawn_timer = 0
        self.spawn_interval = 700  # ms
        self.obstacle_speed = 4
        self.difficulty_timer = 0

        # آبجکت‌ها
        self.player = None

        # بایندینگ‌ها
        self.root.bind("<KeyPress>", self.on_key_down)
        self.root.bind("<KeyRelease>", self.on_key_up)

        self.draw_grid()
        self.reset()

        self.loop()
        self.root.mainloop()

    def draw_grid(self):
        # شبکه‌ی سبک
        for y in range(0, HEIGHT, 40):
            self.canvas.create_line(0, y, WIDTH, y, fill=GRID)
        for x in range(0, WIDTH, 40):
            self.canvas.create_line(x, 0, x, HEIGHT, fill=GRID)

    def reset(self):
        # پاک‌سازی و شروع تازه
        self.canvas.delete("all")
        self.draw_grid()
        self.running = True
        self.paused = False
        self.game_over = False
        self.obstacles.clear()
        self.score = 0.0
        self.spawn_timer = 0
        self.spawn_interval = 700
        self.obstacle_speed = 4
        self.difficulty_timer = 0

        # بازیکن
        size = 36
        x = WIDTH // 2 - size // 2
        y = HEIGHT - 80
        self.player = self.canvas.create_rectangle(x, y, x + size, y + size, fill=PLAYER_COLOR, width=0)

        # متن‌ها
        self.score_text = self.canvas.create_text(12, 12, anchor="nw", fill="#ffffff", font=("Segoe UI", 14),
                                                  text="Score: 0")
        self.info_text = self.canvas.create_text(12, 36, anchor="nw", fill="#8a8d91", font=("Segoe UI", 12),
                                                 text="Move: Arrows | Pause: P")

    def on_key_down(self, event):
        key = event.keysym
        if key in self.keys:
            self.keys[key] = True
        if key.lower() == "p":
            if not self.game_over:
                self.paused = not self.paused
                self.draw_pause()
        if self.game_over:
            if key.lower() == "r":
                self.reset()
            elif key == "Escape":
                self.root.destroy()

    def on_key_up(self, event):
        key = event.keysym
        if key in self.keys:
            self.keys[key] = False

    def loop(self):
        # حلقه‌ی اصلی
        now = time.time()
        dt = (now - self.last_time) * 1000.0  # ms
        self.last_time = now

        if self.running and not self.paused and not self.game_over:
            self.update(dt)

        self.root.after(16, self.loop)  # ~60 FPS

    def update(self, dt):
        # حرکت بازیکن
        px1, py1, px2, py2 = self.canvas.coords(self.player)
        dx = dy = 0
        if self.keys["Left"]:  dx -= self.player_speed
        if self.keys["Right"]: dx += self.player_speed
        if self.keys["Up"]:    dy -= self.player_speed
        if self.keys["Down"]:  dy += self.player_speed

        # اعمال حرکت
        px1 += dx; px2 += dx
        py1 += dy; py2 += dy

        # محدود کردن داخل صفحه
        if px1 < 0: px2 -= px1; px1 = 0
        if px2 > WIDTH: px1 -= (px2 - WIDTH); px2 = WIDTH
        if py1 < 0: py2 -= py1; py1 = 0
        if py2 > HEIGHT: py1 -= (py2 - HEIGHT); py2 = HEIGHT

        self.canvas.coords(self.player, px1, py1, px2, py2)
        # اسپاون موانع
        self.spawn_timer += dt
        self.difficulty_timer += dt
        if self.spawn_timer >= self.spawn_interval:
            self.spawn_timer = 0
            for _ in range(random.randint(1, 3)):
                w = random.randint(30, 70)
                h = random.randint(20, 60)
                x = random.randint(0, WIDTH - w)
                y = -h
                color = random.choice(OBST_COLORS)
                oid = self.canvas.create_rectangle(x, y, x + w, y + h, fill=color, width=0)
                speed = self.obstacle_speed + random.uniform(-0.8, 1.6)
                self.obstacles.append({"id": oid, "speed": speed})

        # افزایش سختی
        if self.difficulty_timer >= 3000:
            self.difficulty_timer = 0
            self.obstacle_speed += 0.3
            self.spawn_interval = max(280, self.spawn_interval - 20)

        # آپدیت موانع
        alive = []
        for obs in self.obstacles:
            x1, y1, x2, y2 = self.canvas.coords(obs["id"])
            y1 += obs["speed"]; y2 += obs["speed"]
            self.canvas.coords(obs["id"], x1, y1, x2, y2)
            if y1 <= HEIGHT + 40:
                alive.append(obs)
            else:
                self.canvas.delete(obs["id"])
        self.obstacles = alive

        # برخورد
        px1, py1, px2, py2 = self.canvas.coords(self.player)
        for obs in self.obstacles:
            ox1, oy1, ox2, oy2 = self.canvas.coords(obs["id"])
            if not (px2 < ox1 or px1 > ox2 or py2 < oy1 or py1 > oy2):
                self.end_game()
                return

        # امتیاز
        self.score += dt / 1000.0
        self.canvas.itemconfigure(self.score_text, text=f"Score: {int(self.score)}")

        # افکت وینیت سبک گوشه‌ها
        self.draw_vignette()

    def draw_vignette(self):
        # حذف وینیت قبلی
        self.canvas.delete("vignette")
        # ترسیم چهار مستطیل نیمه‌شفاف در گوشه‌ها
        alpha = 40  # شفافیت تقریبی با رنگ تیره
        # Tkinter alpha مستقیم ندارد؛ با رنگ نزدیک به پس‌زمینه کار