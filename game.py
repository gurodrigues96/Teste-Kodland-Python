import pgzrun
import random
from pygame import Rect

WIDTH = 800
HEIGHT = 600
TITLE = "Platformer Tutor Test"

class GameSprite:
    def __init__(self, x, y, images_idle, images_move):
        self.x = x
        self.y = y
        self.images_idle = images_idle
        self.images_move = images_move
        self.current_images = self.images_idle
        self.frame_index = 0
        self.animation_timer = 0
        self.animation_speed = 0.1
        self.actor = Actor(self.images_idle[0], (x, y))
        self.width = self.actor.width
        self.height = self.actor.height

    def animate(self, dt, is_moving):
        self.animation_timer += dt
        
        if is_moving:
            self.current_images = self.images_move
        else:
            self.current_images = self.images_idle

        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.frame_index = (self.frame_index + 1) % len(self.current_images)
            self.actor.image = self.current_images[self.frame_index]

    def draw(self):
        self.actor.draw()

class Player(GameSprite):
    def __init__(self, x, y):
        super().__init__(x, y, ['p1_idle1', 'p1_idle2'], ['p1_walk1', 'p1_walk2'])
        self.velocity_y = 0
        self.speed = 5
        self.gravity = 0.5
        self.jump_strength = -12
        self.is_jumping = False
        self.facing_right = True

    def update(self, dt, platforms):
        is_moving = False
        
        if keyboard.left:
            self.actor.x -= self.speed
            self.facing_right = False
            is_moving = True
        elif keyboard.right:
            self.actor.x += self.speed
            self.facing_right = True
            is_moving = True

        if keyboard.space and not self.is_jumping:
            self.velocity_y = self.jump_strength
            self.is_jumping = True
            if sound_enabled:
                sounds.jump.play()

        self.velocity_y += self.gravity
        self.actor.y += self.velocity_y

        self.check_collisions(platforms)
        self.animate(dt, is_moving)

    def check_collisions(self, platforms):
        if self.actor.bottom >= HEIGHT:
            self.actor.bottom = HEIGHT
            self.velocity_y = 0
            self.is_jumping = False

        for platform in platforms:
            if self.actor.colliderect(platform):
                if self.velocity_y > 0 and self.actor.bottom <= platform.bottom:
                    self.actor.bottom = platform.top
                    self.velocity_y = 0
                    self.is_jumping = False

class Enemy(GameSprite):
    def __init__(self, x, y, min_x, max_x):
        super().__init__(x, y, ['enemy1'], ['enemy1', 'enemy2'])
        self.min_x = min_x
        self.max_x = max_x
        self.speed = 2
        self.direction = 1 

    def update(self, dt):
        self.actor.x += self.speed * self.direction
        
        if self.actor.x >= self.max_x:
            self.direction = -1
        elif self.actor.x <= self.min_x:
            self.direction = 1

        self.animate(dt, True)

game_state = "MENU" 
sound_enabled = True
music_playing = False

level_layout = [
    "....................",
    "....................",
    "....................",
    "....I...............",
    "BBBBBB.......BBBB...",
    "....................",
    "........BBBB........",
    "....................",
    "....BB..............",
    "..........I.........",
    "......BBBBBBBB......",
    "....................",
    "P...................",
    "BBBB...BBBBBB...BBBB",
    "BBBB...BBBBBB...BBBB"
]

hero = Player(0, 0)
platforms = []
enemies = []

def setup_level():
    global platforms, enemies, hero
    
    platforms = []
    enemies = []
    
    for row_index, row in enumerate(level_layout):
        for col_index, char in enumerate(row):
            x = col_index * 40
            y = row_index * 40
            
            if char == "B":
                p = Actor('platform', topleft=(x, y))
                platforms.append(p)
            
            elif char == "I":
                enemy = Enemy(x, y, x - 100, x + 100)
                enemies.append(enemy)
            
            elif char == "P":
                hero.actor.topleft = (x, y)
                hero.velocity_y = 0

setup_level()

btn_start = Actor('btn_start', (WIDTH//2, 200))
btn_sound = Actor('btn_sound_on', (WIDTH//2, 300))
btn_exit = Actor('btn_exit', (WIDTH//2, 400))

def draw():
    screen.fill((135, 206, 235))
    
    if game_state == "MENU":
        screen.draw.text("PLATFORMER ADVENTURE", center=(WIDTH//2, 100), fontsize=50)
        btn_start.draw()
        btn_sound.draw()
        btn_exit.draw()
        screen.draw.text("Sound: " + ("ON" if sound_enabled else "OFF"), 
                         topleft=(btn_sound.right + 10, btn_sound.y - 10))

    elif game_state == "GAME":
        for platform in platforms:
            platform.draw()
        
        hero.draw()
        for enemy in enemies:
            enemy.draw()
            
        screen.draw.text("Controls: Arrows to move, Space to jump", (10, 10))

    elif game_state == "GAMEOVER":
        screen.draw.text("GAME OVER", center=(WIDTH//2, HEIGHT//2), fontsize=60, color="red")
        screen.draw.text("Click to return to menu", center=(WIDTH//2, HEIGHT//2 + 50))

def update(dt):
    global game_state, music_playing
    
    if sound_enabled and not music_playing:
        try:
            music.play('bg_music')
            music.set_volume(0.3)
            music_playing = True
        except:
            pass 
    elif not sound_enabled:
        music.stop()
        music_playing = False

    if game_state == "GAME":
        hero.update(dt, platforms)
        
        for enemy in enemies:
            enemy.update(dt)
            if hero.actor.colliderect(enemy.actor):
                game_state = "GAMEOVER"

def on_mouse_down(pos):
    global game_state, sound_enabled
    
    if game_state == "MENU":
        if btn_start.collidepoint(pos):
            reset_game()
            game_state = "GAME"
        elif btn_sound.collidepoint(pos):
            sound_enabled = not sound_enabled
            btn_sound.image = 'btn_sound_on' if sound_enabled else 'btn_sound_off'
        elif btn_exit.collidepoint(pos):
            quit()
            
    elif game_state == "GAMEOVER":
        game_state = "MENU"

def reset_game():
    setup_level()
    
pgzrun.go()