import pygame
import sys
import math
import random
import re
from time import sleep

# Инициализация Pygame
pygame.init()

# добавление дилея
clock = pygame.time.Clock()

# Определение цветов
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

square_white = pygame.Surface((155,110))
square_white.fill(WHITE)
square_black = pygame.Surface((160,120))
square_black.fill((0,20,0))


# цены
skin_2_cost = 20


# загрузка сохранений      
pattern_skin = r'skin:\d+:'
find_skin = 'skin'
pattern_money = r'money:\d+:'
find_money = 'money'
pattern_bought_skin_2 = r'bought_skin_2:\d+:'
find_bought_skin_2 = 'bought_skin_2'
pattern_best_score = r'best_score:\d+:'
find_best_score = 'best_score'

your_score = 0
  
with open("C:\dz\DZ\python\Dominator\save\save.txt", "r+") as file:                         
    content = file.read()                    
    content = content.replace('\n','')
    content = content.split(':')

    skin = content.index(find_skin) + 1
    skin = content[skin]
    money = content.index(find_money) + 1
    money = int(content[money])
    bought_skin_2 = content.index(find_bought_skin_2) + 1
    bought_skin_2 = content[bought_skin_2]
    best_score = content.index(find_best_score) + 1
    best_score = int(content[best_score])


# Установка ширины и высоты экрана
WIDTH = 1025
HEIGHT = 1025
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Dominator")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

# шрифты
label = pygame.font.Font('fonts/Rye-Regular.ttf', 50)
small_label = pygame.font.Font('fonts/Rye-Regular.ttf', 30)
cost_label = pygame.font.Font('fonts/Rye-Regular.ttf', 20)

# текста меню
lose_label = label.render('You lose', False, (219, 67, 2))

restart_label = label.render('Restart game', False, (219, 42, 2))
restart_label_rect = restart_label.get_rect(topleft=(WIDTH // 2 - restart_label.get_width() // 2,500))

start_label = label.render('Start game', True, (219, 67, 2))
start_label_rect = start_label.get_rect(topleft=(WIDTH // 2 - start_label.get_width() // 2, 300))

shop_label = small_label.render('Shop', True, (219, 67, 2))
shop_label_rect = shop_label.get_rect(topleft=(WIDTH // 2 - shop_label.get_width() // 2, 400))

in_shop_label = label.render('Skin shop', True, (219, 67, 2))

in_shop_back_label = small_label.render('Back', False, (219, 67, 2))
in_shop_back_label_rect = in_shop_back_label.get_rect(topleft=(100,150))

skin_2_cost_label = cost_label.render(f'{skin_2_cost}', True, (219, 42, 2))


# картинки меню
red_demon_skin = pygame.image.load('images/shop_skins/red_demon.png').convert_alpha()
red_demon_skin_rect = red_demon_skin.get_rect(topleft=(250,550))

green_demon_skin = pygame.image.load('images/shop_skins/green_demon.png').convert_alpha()
green_demon_skin_rect = green_demon_skin.get_rect(topleft=(600,550))

frame_grey = pygame.image.load('images/icons/frame_grey.png').convert_alpha()

shotgun_icon = pygame.image.load('images/icons/shotgun.png').convert_alpha()

fireball_icon = pygame.image.load('images/icons/fireball.png').convert_alpha()

boomerang_icon = pygame.image.load('images/icons/boomerang.png').convert_alpha()

main_menu_img = pygame.image.load('images/hell.png').convert_alpha()

lose_bg_img = pygame.image.load('images/lose_bg.png').convert_alpha()

shop_bg_img = pygame.image.load('images/shop_bg.png').convert_alpha()

chain_img = pygame.image.load('images/shop_skins/chain.png').convert_alpha()

button_img = pygame.image.load('images/shop_skins/buy_button.png').convert_alpha()
button_img_rect = button_img.get_rect(topleft = (625, 680))


# Загрузка изображений спрайтов для каждого направления

if skin == '1':
    sprite_left = [pygame.image.load("images/demon_walk/left1.png").convert_alpha(), 
                   pygame.image.load("images/demon_walk/left2.png").convert_alpha(), 
                   pygame.image.load("images/demon_walk/left3.png").convert_alpha(), 
                   pygame.image.load("images/demon_walk/left4.png").convert_alpha()
                   ]
    sprite_right = [pygame.image.load("images/demon_walk/right1.png").convert_alpha(),
                    pygame.image.load("images/demon_walk/right2.png").convert_alpha(),
                    pygame.image.load("images/demon_walk/right3.png").convert_alpha(),
                    pygame.image.load("images/demon_walk/right4.png").convert_alpha()
                    ]
    sprite_up = [pygame.image.load("images/demon_walk/up1.png").convert_alpha(),
                 pygame.image.load("images/demon_walk/up2.png").convert_alpha(),
                 pygame.image.load("images/demon_walk/up3.png").convert_alpha(),
                 pygame.image.load("images/demon_walk/up4.png").convert_alpha()
                 ]
    sprite_down = [pygame.image.load("images/demon_walk/down1.png").convert_alpha(),
                   pygame.image.load("images/demon_walk/down2.png").convert_alpha(),
                   pygame.image.load("images/demon_walk/down3.png").convert_alpha(),
                   pygame.image.load("images/demon_walk/down4.png").convert_alpha()
                   ]
    sprite_dead = [pygame.image.load("images/demon_dead/death1.png").convert_alpha(),
                   pygame.image.load("images/demon_dead/death2.png").convert_alpha(),
                   pygame.image.load("images/demon_dead/death3.png").convert_alpha(),
                   pygame.image.load("images/demon_dead/death4.png").convert_alpha(),
                   pygame.image.load("images/demon_dead/death5.png").convert_alpha(),
                   pygame.image.load("images/demon_dead/death6.png").convert_alpha()
                   ]
elif skin == '2':
    sprite_left = [pygame.image.load("images/green_demon_walk/left1.png").convert_alpha(), 
                   pygame.image.load("images/green_demon_walk/left2.png").convert_alpha(), 
                   pygame.image.load("images/green_demon_walk/left3.png").convert_alpha(), 
                   pygame.image.load("images/green_demon_walk/left4.png").convert_alpha()
                   ]
    sprite_right = [pygame.image.load("images/green_demon_walk/right1.png").convert_alpha(),
                    pygame.image.load("images/green_demon_walk/right2.png").convert_alpha(),
                    pygame.image.load("images/green_demon_walk/right3.png").convert_alpha(),
                    pygame.image.load("images/green_demon_walk/right4.png").convert_alpha()
                    ]
    sprite_up = [pygame.image.load("images/green_demon_walk/up1.png").convert_alpha(),
                 pygame.image.load("images/green_demon_walk/up2.png").convert_alpha(),
                 pygame.image.load("images/green_demon_walk/up3.png").convert_alpha(),
                 pygame.image.load("images/green_demon_walk/up4.png").convert_alpha()
                 ]
    sprite_down = [pygame.image.load("images/green_demon_walk/down1.png").convert_alpha(),
                   pygame.image.load("images/green_demon_walk/down2.png").convert_alpha(),
                   pygame.image.load("images/green_demon_walk/down3.png").convert_alpha(),
                   pygame.image.load("images/green_demon_walk/down4.png").convert_alpha()
                   ]
    sprite_dead = [pygame.image.load("images/green_demon_dead/death1.png").convert_alpha(),
                   pygame.image.load("images/green_demon_dead/death2.png").convert_alpha(),
                   pygame.image.load("images/green_demon_dead/death3.png").convert_alpha(),
                   pygame.image.load("images/green_demon_dead/death4.png").convert_alpha(),
                   pygame.image.load("images/green_demon_dead/death5.png").convert_alpha(),
                   pygame.image.load("images/green_demon_dead/death6.png").convert_alpha()
                   ]
saved = sprite_down[0]
# Установка начальной позиции спрайта
sprite_x = WIDTH // 2 - sprite_down[0].get_width() // 2
sprite_y = HEIGHT // 2 - sprite_down[0].get_height() // 2 

enemy_sarah_img = [pygame.image.load("images/sarah_walk/down1.png").convert_alpha(),
                   pygame.image.load("images/sarah_walk/down2.png").convert_alpha(),
                   pygame.image.load("images/sarah_walk/down3.png").convert_alpha(),
                   pygame.image.load("images/sarah_walk/down4.png").convert_alpha()
                   ]

enemy_vika_img = [pygame.image.load("images/vika_walk/down1.png").convert_alpha(),
                  pygame.image.load("images/vika_walk/down2.png").convert_alpha(),
                  pygame.image.load("images/vika_walk/down3.png").convert_alpha(),
                  pygame.image.load("images/vika_walk/down4.png").convert_alpha()
                  ]

enemy_amanda_img = [pygame.image.load("images/amanda_walk/down1.png").convert_alpha(),
                    pygame.image.load("images/amanda_walk/down2.png").convert_alpha(),
                    pygame.image.load("images/amanda_walk/down3.png").convert_alpha(),
                    pygame.image.load("images/amanda_walk/down4.png").convert_alpha()
                    ]

bullet_img = [pygame.image.load("images/fireball/fireball1.png").convert_alpha(),
              pygame.image.load("images/fireball/fireball2.png").convert_alpha()
              ]
 
shotgun_img = [pygame.image.load("images/shotgun_bullet/shotgun_bullet1.png").convert_alpha(),
               pygame.image.load("images/shotgun_bullet/shotgun_bullet1.png").convert_alpha()
               ]

boomerang_img = [pygame.image.load("images/boomerang_bullet/boomerang1.png"),
                 pygame.image.load("images/boomerang_bullet/boomerang2.png"),
                 pygame.image.load("images/boomerang_bullet/boomerang3.png"),
                 pygame.image.load("images/boomerang_bullet/boomerang4.png"),
                 pygame.image.load("images/boomerang_bullet/boomerang5.png"),
                 ]

bg = pygame.image.load("images/stonebg.png").convert_alpha()

coin_img = [pygame.image.load("images/coin/Coin1.png").convert_alpha(),
            pygame.image.load("images/coin/Coin2.png").convert_alpha(),
            pygame.image.load("images/coin/Coin3.png").convert_alpha(),
            pygame.image.load("images/coin/Coin4.png").convert_alpha(),
            pygame.image.load("images/coin/Coin5.png").convert_alpha(),
            pygame.image.load("images/coin/Coin6.png").convert_alpha()
            ]

heart_img = [pygame.image.load("images/heart/heart1.png").convert_alpha(),
             pygame.image.load("images/heart/heart2.png").convert_alpha()
             ]

# Создание списка для хранения врагов
enemies_sarah = []
enemies_vika = []
enemies_amanda = []

# Создание списка для хранения пуль
bullets = []

bullets_boomerang = []

# Создание массива для хранения монет
coins = []

# Создание массива для хранения сердец
hearts = []

# Класс для представления врагов
class Enemy:
    def __init__(self, x, y, speed, hp, target, side):
        self.x = x
        self.y = y
        self.hp = hp
        self.side = side
        self.target = target
        self.speed = speed  # Скорость движения врага

    def update(self, x, y):
            # Движение врага в сторону игрока
            if self.target == 1:
                direction = math.atan2(sprite_y - self.y, sprite_x - self.x)
                self.x += self.speed * math.cos(direction) - x
                self.y += self.speed * math.sin(direction) - y
            else:
                self.x += self.speed * math.cos(self.side) - x
                self.y += self.speed * math.sin(self.side) - y

    def draw(self, cnt, img):
            screen.blit(img, (self.x, self.y))

# Класс для представления пуль
class Bullet:
    def __init__(self, x, y, angle, speed):
        self.x = x
        self.y = y
        self.speed = speed  # Скорость полета пули
        self.angle = angle

    def update(self, x, y):
        # Движение пули в направлении указанного угла
        self.x += self.speed * math.cos(self.angle) - x
        self.y += self.speed * math.sin(self.angle) - y

    def draw(self, cnt, gun_type):
        if gun_type == 1:
            screen.blit(bullet_img[cnt], (self.x, self.y))

        elif gun_type == 2:
            screen.blit(shotgun_img[cnt], (self.x, self.y))

class Bullet_boomerang:
    def __init__(self, x, y, angle1, speed, return_bullet, delta):
        self.x = x
        self.y = y
        self.speed = speed  # Скорость полета пули
        self.angle1 = angle1
        self.return_bullet = return_bullet
        self.delta = delta

    def update(self, x, y):
        if self.return_bullet <= 30:
            self.x += self.speed * math.cos(self.angle1) - x
            self.y += self.speed * math.sin(self.angle1) - y
        elif self.return_bullet > 30:
            angle2 = math.atan2(sprite_y - self.y, sprite_x - self.x)
            self.x += self.speed * math.cos(angle2) - x
            self.y += self.speed * math.sin(angle2) - y
        

    def draw(self, cnt):
            screen.blit(boomerang_img[cnt], (self.x, self.y))

class Coin:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, x, y):
        self.x += -x
        self.y += -y

    def draw(self, cnt):
        screen.blit(coin_img[cnt], (self.x, self.y))

class Heart:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, x, y):
        self.x += -x
        self.y += -y

    def draw(self, cnt):
        screen.blit(heart_img[cnt], (self.x, self.y))

#таймер для измерения скорости выстрелов 
return_bullet = 0
bullet_timer = pygame.USEREVENT + 1 
death_timer = pygame.USEREVENT + 1 
fireball_cnt = 0
fireball_ready = False 
shotgun_cnt = 0
shotgun_ready = False 
boomerang_cnt = 0
boomerang_ready = False 
fireball_icon_cnt = 0
shotgun_icon_cnt = 0
delta = 0
boomerang_icon_cnt = 0
pygame.time.set_timer(bullet_timer, 100)
pygame.time.set_timer(death_timer, 100)

bg_x = 0
death_check = True
bg_y = 0
count = 0
count_id = 0
count_id2 = 0
coin_cnt = 0
boom_cnt = 0

coins_score = 0

sarah_amount = 20
sarah_spawn_chance = 2
sarah_speed = 3
sarah_hp = 1

vika_amount = 10
vika_spawn_chance = 2
vika_speed = 2.5
vika_hp = 1

amanda_amount = 10
amanda_spawn_chance = 2
amanda_speed = 1.5
amanda_hp = 3

# Установка скорости перемещения спрайта
speed = 5

# Основной цикл программы
running = True
clock = pygame.time.Clock()

press = False
saved = sprite_down[0]

rungame = True 
start_game = False 
main_menu = True
shop_menu = False
fireball_icon_trigger = False
shotgun_icon_trigger = False
boomerang_icon_trigger = False


score = 0

gun_type = 1

fireball_speed = 30
shotgun_speed = 40
boomerang_speed = 20

# Жизни персонажа
lives = 3

change_x = 0
change_y = 0

cnt = 0

while running:

    mouse = pygame.mouse.get_pos() 
    keys = pygame.key.get_pressed()
    # Получение текущих координат мыши
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Расчет угла между башней и курсором
    angle = math.atan2(mouse_y - sprite_y, mouse_x - sprite_x)

    if keys[pygame.K_1]:
        gun_type = 1
        fireball_icon_trigger = True
        shotgun_icon_trigger = False
        boomerang_icon_trigger = False
        shotgun_icon_cnt = 0
        fireball_icon_cnt = 0
        boomerang_icon_cnt = 0

    elif keys[pygame.K_2]:
        gun_type = 2
        shotgun_icon_trigger = True
        fireball_icon_trigger = False
        boomerang_icon_trigger = False
        shotgun_icon_cnt = 0
        fireball_icon_cnt = 0
        boomerang_icon_cnt = 0

    elif keys[pygame.K_3]:
        gun_type = 3
        return_bullet = 0
        shotgun_icon_trigger = False
        fireball_icon_trigger = False
        boomerang_icon_trigger = True
        shotgun_icon_cnt = 0
        fireball_icon_cnt = 0
        boomerang_icon_cnt = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == bullet_timer: 
            fireball_cnt += 1 
            shotgun_cnt += 1
            boomerang_cnt += 1

            if shotgun_cnt == 7:
                shotgun_ready = True
            if fireball_cnt == 2: 
                fireball_ready = True 
            if boomerang_cnt == 10:
                boomerang_ready = True

 
        if start_game: 
            if rungame: 
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    # Создание пули при нажатии левой кнопки мыши 
                    # Фаербол
                    if event.button == 1 and fireball_ready and gun_type == 1:  # Левая кнопка мыши 
                        bullet = Bullet(sprite_x, sprite_y, angle, fireball_speed) 
                        bullets.append(bullet) 
                        fireball_ready = False 
                        fireball_cnt = 0
                        
                    # Дробовик
                    if event.button == 1 and shotgun_ready and gun_type == 2:  # Левая кнопка мыши 
                        bullet = Bullet(sprite_x, sprite_y, angle, shotgun_speed) 
                        bullets.append(bullet) 
                        degree = math.degrees(angle)
                        degree -= 10
                        bullet = Bullet(sprite_x, sprite_y, math.radians(degree), shotgun_speed) 
                        bullets.append(bullet) 
                        degree = math.degrees(angle)
                        degree += 10
                        bullet = Bullet(sprite_x, sprite_y, math.radians(degree), shotgun_speed) 
                        bullets.append(bullet) 
                        shotgun_ready = False 
                        shotgun_cnt = 0

                    # Бумеранг
                    if event.button == 1 and boomerang_ready and gun_type == 3:  # Левая кнопка мыши 
                        angle1 = math.atan2(mouse_y - sprite_y, mouse_x - sprite_x)
                        bullet_boomerang = Bullet_boomerang(sprite_x, sprite_y, angle1, boomerang_speed, return_bullet, delta) 
                        bullets_boomerang.append(bullet_boomerang) 
                        boomerang_ready = False 
                        boomerang_cnt = 0

    if main_menu:
        screen.blit(main_menu_img, (0,0))
        screen.blit(start_label,start_label_rect)
        screen.blit(shop_label,shop_label_rect)

        if shop_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            main_menu = False
            shop_menu = True
            count_shop_frame = True
            if skin =='1':
                red_demon_shop_frame = True
                green_demon_shop_frame = False
            if skin =='2':
                red_demon_shop_frame = False
                green_demon_shop_frame = True

        if start_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            main_menu = False
            start_game = True
            death_check = True
            rungame = True


    if shop_menu:
        shop_money_label = small_label.render(f'{money}', True, (179, 2, 2))
        screen.blit(shop_bg_img, (0,0))
        screen.blit(in_shop_label, (WIDTH // 2 - in_shop_label.get_width() // 2, 250))     
        screen.blit(in_shop_back_label, in_shop_back_label_rect)
        screen.blit(red_demon_skin, red_demon_skin_rect)
        screen.blit(green_demon_skin, green_demon_skin_rect)
        screen.blit(coin_img[0], (WIDTH - 200 , 100)) 
        screen.blit(shop_money_label, (WIDTH - 160, 95))
        
        
            
        if bought_skin_2 == '1':
            if red_demon_skin_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                skin = '1'
                with open('save/save.txt', "r+") as file:
                    content = file.read()
                    replace_content = re.sub(pattern_skin,f'skin:{skin}:', content)
                    file.seek(0)
                    file.write(replace_content)
                    file.truncate()
                red_demon_shop_frame = True
                green_demon_shop_frame = False

                # Загрузка изображений спрайтов для каждого направления
                
                sprite_left = [pygame.image.load("images/demon_walk/left1.png").convert_alpha(), 
                            pygame.image.load("images/demon_walk/left2.png").convert_alpha(), 
                            pygame.image.load("images/demon_walk/left3.png").convert_alpha(), 
                            pygame.image.load("images/demon_walk/left4.png").convert_alpha()
                            ]
                sprite_right = [pygame.image.load("images/demon_walk/right1.png").convert_alpha(),
                                pygame.image.load("images/demon_walk/right2.png").convert_alpha(),
                                pygame.image.load("images/demon_walk/right3.png").convert_alpha(),
                                pygame.image.load("images/demon_walk/right4.png").convert_alpha()
                                ]
                sprite_up = [pygame.image.load("images/demon_walk/up1.png").convert_alpha(),
                            pygame.image.load("images/demon_walk/up2.png").convert_alpha(),
                            pygame.image.load("images/demon_walk/up3.png").convert_alpha(),
                            pygame.image.load("images/demon_walk/up4.png").convert_alpha()
                            ]
                sprite_down = [pygame.image.load("images/demon_walk/down1.png").convert_alpha(),
                            pygame.image.load("images/demon_walk/down2.png").convert_alpha(),
                            pygame.image.load("images/demon_walk/down3.png").convert_alpha(),
                            pygame.image.load("images/demon_walk/down4.png").convert_alpha()
                            ]
                saved = sprite_down[0]

                sprite_dead = [pygame.image.load("images/demon_dead/death1.png").convert_alpha(),
                            pygame.image.load("images/demon_dead/death2.png").convert_alpha(),
                            pygame.image.load("images/demon_dead/death3.png").convert_alpha(),
                            pygame.image.load("images/demon_dead/death4.png").convert_alpha(),
                            pygame.image.load("images/demon_dead/death5.png").convert_alpha(),
                            pygame.image.load("images/demon_dead/death6.png").convert_alpha()
                            ]
    
            
        
            if green_demon_skin_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                skin = '2'
                with open('save/save.txt', "r+") as file:
                    content = file.read()
                    replace_content = re.sub(pattern_skin,f'skin:{skin}:', content)
                    file.seek(0)
                    file.write(replace_content)
                    file.truncate()
                
                green_demon_shop_frame = True
                red_demon_shop_frame = False
            # Загрузка изображений спрайтов для каждого направления
            
                sprite_left = [pygame.image.load("images/green_demon_walk/left1.png").convert_alpha(), 
                            pygame.image.load("images/green_demon_walk/left2.png").convert_alpha(), 
                            pygame.image.load("images/green_demon_walk/left3.png").convert_alpha(), 
                            pygame.image.load("images/green_demon_walk/left4.png").convert_alpha()
                            ]
                sprite_right = [pygame.image.load("images/green_demon_walk/right1.png").convert_alpha(),
                                pygame.image.load("images/green_demon_walk/right2.png").convert_alpha(),
                                pygame.image.load("images/green_demon_walk/right3.png").convert_alpha(),
                                pygame.image.load("images/green_demon_walk/right4.png").convert_alpha()
                                ]
                sprite_up = [pygame.image.load("images/green_demon_walk/up1.png").convert_alpha(),
                            pygame.image.load("images/green_demon_walk/up2.png").convert_alpha(),
                            pygame.image.load("images/green_demon_walk/up3.png").convert_alpha(),
                            pygame.image.load("images/green_demon_walk/up4.png").convert_alpha()
                            ]
                sprite_down = [pygame.image.load("images/green_demon_walk/down1.png").convert_alpha(),
                            pygame.image.load("images/green_demon_walk/down2.png").convert_alpha(),
                            pygame.image.load("images/green_demon_walk/down3.png").convert_alpha(),
                            pygame.image.load("images/green_demon_walk/down4.png").convert_alpha()
                            ]
                saved = sprite_down[0]

                sprite_dead = [pygame.image.load("images/green_demon_dead/death1.png").convert_alpha(),
                            pygame.image.load("images/green_demon_dead/death2.png").convert_alpha(),
                            pygame.image.load("images/green_demon_dead/death3.png").convert_alpha(),
                            pygame.image.load("images/green_demon_dead/death4.png").convert_alpha(),
                            pygame.image.load("images/green_demon_dead/death5.png").convert_alpha(),
                            pygame.image.load("images/green_demon_dead/death6.png").convert_alpha()
                            ]
        
        if bought_skin_2 == '0':
            screen.blit(chain_img, (600,550))
            screen.blit(button_img, button_img_rect)
            screen.blit(skin_2_cost_label, (660, 700))

            if button_img_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] and money >= skin_2_cost:
                bought_skin_2 = '1'
                with open('save/save.txt', "r+") as file:
                    money -= skin_2_cost 
                    content = file.read()
                    replace_content = re.sub(pattern_money,f'money:{money}:', content)
                    file.seek(0)
                    file.write(replace_content)
                    file.truncate()
                    replace_content = re.sub(pattern_bought_skin_2,f'bought_skin_2:{bought_skin_2}:', content)
                    file.seek(0)
                    file.write(replace_content)
                    file.truncate()

        if red_demon_shop_frame:
            
            screen.blit(red_demon_skin, (250,550))
            screen.blit(frame_grey, (250,550))
        if green_demon_shop_frame:
            
            screen.blit(green_demon_skin, (600, 550))
            screen.blit(frame_grey, (600,550))


        if in_shop_back_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            shop_menu = False
            main_menu = True



    if start_game:
        if rungame:
            
            screen.blit(bg, (bg_x, bg_y))
            screen.blit(bg, (bg_x + 1025, bg_y))
            screen.blit(bg, (bg_x - 1025, bg_y))
            screen.blit(bg, (bg_x, bg_y + 1025))
            screen.blit(bg, (bg_x, bg_y - 1025))
            screen.blit(bg, (bg_x + 1025, bg_y + 1025))
            screen.blit(bg, (bg_x - 1025, bg_y + 1025))
            screen.blit(bg, (bg_x + 1025, bg_y - 1025))
            screen.blit(bg, (bg_x - 1025, bg_y - 1025))

            # Усложнение игры с полученными очками
            if score > 500 and score < 1500:
                sarah_speed = 4
                vika_speed = 3.5
                amanda_speed = 2.5

                sarah_spawn_chance = 4
                vika_spawn_chance = 4
                amanda_spawn_chance = 4

                sarah_amount = 30
                vika_amount = 15
                amanda_amount = 15

            if score >= 1500 and score < 2500:
                sarah_speed = 5
                vika_speed = 5.5
                amanda_speed = 3.5

                sarah_spawn_chance = 8
                vika_spawn_chance = 8
                amanda_spawn_chance = 8

                sarah_amount = 40
                vika_amount = 20
                amanda_amount = 20

            if score >= 2500:
                sarah_speed = 6.5
                vika_speed = 6
                amanda_speed = 4.5

                sarah_spawn_chance = 8
                vika_spawn_chance = 8
                amanda_spawn_chance = 8

                sarah_amount = 40
                vika_amount = 30
                amanda_amount = 25

                vika_hp = 2
                amanda_hp = 4

            
            # Создание врагов №1
            if len(enemies_sarah) < sarah_amount and random.randint(0, 100) < sarah_spawn_chance:
                side = random.randint(1, 4)  # Генерация случайной стороны появления врага
                if side == 1:  # Сверху
                    x = random.randint(0, WIDTH)
                    y = -50
                elif side == 2:  # Справа
                    x = WIDTH + 50
                    y = random.randint(0, HEIGHT)
                elif side == 3:  # Снизу
                    x = random.randint(0, WIDTH)
                    y = HEIGHT + 50
                else:  # Слева
                    x = -50
                    y = random.randint(0, HEIGHT)
                side_enemy = math.atan2(random.randint(sprite_y - 50, sprite_y + 50) - y, random.randint(sprite_x - 50, sprite_x + 50) - x)
                enemy_sarah = Enemy(x, y, sarah_speed, sarah_hp, 2, side_enemy)
                enemies_sarah.append(enemy_sarah)

            # Создание врагов №2
            if len(enemies_vika) < vika_amount and random.randint(0, 100) < vika_spawn_chance:
                side = random.randint(1, 4)  # Генерация случайной стороны появления врага
                if side == 1:  # Сверху
                    x = random.randint(0, WIDTH)
                    y = -50
                elif side == 2:  # Справа
                    x = WIDTH + 50
                    y = random.randint(0, HEIGHT)
                elif side == 3:  # Снизу
                    x = random.randint(0, WIDTH)
                    y = HEIGHT + 50
                else:  # Слева
                    x = -50
                    y = random.randint(0, HEIGHT)
                side_enemy = math.atan2(random.randint(sprite_y - 50, sprite_y + 50) - y, random.randint(sprite_x - 50, sprite_x + 50) - x)
                enemy_vika = Enemy(x, y, vika_speed, vika_hp, 1, side_enemy)
                enemies_vika.append(enemy_vika)

            # Создание врагов №3
            if len(enemies_amanda) < amanda_amount and random.randint(0, 100) < amanda_spawn_chance:
                side = random.randint(1, 4)  # Генерация случайной стороны появления врага
                if side == 1:  # Сверху
                    x = random.randint(0, WIDTH)
                    y = -50
                elif side == 2:  # Справа
                    x = WIDTH + 50
                    y = random.randint(0, HEIGHT)
                elif side == 3:  # Снизу
                    x = random.randint(0, WIDTH)
                    y = HEIGHT + 50
                else:  # Слева
                    x = -50
                    y = random.randint(0, HEIGHT)
                side_enemy = math.atan2(random.randint(sprite_y - 50, sprite_y + 50) - y, random.randint(sprite_x - 50, sprite_x + 50) - x)
                enemy_amanda = Enemy(x, y, amanda_speed, amanda_hp, 1, side_enemy)
                enemies_amanda.append(enemy_amanda)
            
            
            # Обновление позиции спрайта в соответствии с нажатыми клавишами
            if keys[pygame.K_a] and keys[pygame.K_w]:
                bg_x += speed
                bg_y += speed
                change_x = -speed
                change_y = -speed
                screen.blit(sprite_up[count], (sprite_x, sprite_y))
                press = True
                saved = sprite_up[0]
            elif keys[pygame.K_a] and keys[pygame.K_s]:
                bg_x += speed
                bg_y -= speed
                change_x = -speed
                change_y = speed
                screen.blit(sprite_down[count], (sprite_x, sprite_y))
                press = True
                saved = sprite_down[0]
            elif keys[pygame.K_d] and keys[pygame.K_s]:
                bg_x -= speed
                bg_y -= speed
                change_x = speed
                change_y = speed
                screen.blit(sprite_down[count], (sprite_x, sprite_y))
                press = True
                saved = sprite_down[0]
            elif keys[pygame.K_d] and keys[pygame.K_w]:
                bg_x -= speed
                bg_y += speed
                change_x = speed
                change_y = -speed
                screen.blit(sprite_up[count], (sprite_x, sprite_y))
                press = True
                saved = sprite_up[0]
            elif keys[pygame.K_a]:
                bg_x += speed
                change_x = -speed
                change_y = 0
                screen.blit(sprite_left[count], (sprite_x, sprite_y))
                press = True
                saved = sprite_left[0]
            elif keys[pygame.K_d]:
                bg_x -= speed
                change_x = speed
                change_y = 0
                screen.blit(sprite_right[count], (sprite_x, sprite_y))
                press = True
                saved = sprite_right[0]
            elif keys[pygame.K_w]:
                bg_y += speed
                change_y = -speed
                change_x = 0
                screen.blit(sprite_up[count], (sprite_x, sprite_y))
                press = True
                saved = sprite_up[0]
            elif keys[pygame.K_s]:
                bg_y -= speed
                change_y = speed
                change_x = 0
                screen.blit(sprite_down[count], (sprite_x, sprite_y))
                press = True
                saved = sprite_down[0]
            else:
                press = False
                change_x = 0
                change_y = 0
            
            if not press:
                screen.blit(saved, (sprite_x, sprite_y))

            # Частота изменения анимаций
            if count_id == 10:
                if count == 3:
                    count = 0
                else:
                    count += 1

                if cnt == 1:
                    cnt = 0
                else:
                    cnt += 1

                if coin_cnt == 5:
                    coin_cnt = 0

                else:
                    coin_cnt += 1
                
                if boom_cnt == 4:
                    boom_cnt = 0

                else:
                    boom_cnt += 1

                count_id = 0

            else: 
                count_id += 1

            if count_id2 == 1:
                if boom_cnt == 4:
                    boom_cnt = 0

                else:
                    boom_cnt += 1

                count_id2 = 0

            else: 
                count_id2 += 1
            
            # Чтобы карта была бесконечной
            if bg_x == -1025 or bg_x == 1025:
                bg_x = 0
            if bg_y == -1025 or bg_y == 1025:
                bg_y = 0

            # Обновление и отрисовка монет
            for coin in coins:
                coin.update(change_x, change_y)
                coin.draw(coin_cnt)
                if sprite_down[count].get_rect(topleft=(sprite_x, sprite_y)).colliderect(coin_img[coin_cnt].get_rect(topleft=(coin.x, coin.y))):
                    coins.remove(coin)
                    coins_score += 1
            
            # Обновление и отрисовка сердец
            for heart in hearts:
                heart.update(change_x, change_y)
                heart.draw(cnt)
                if sprite_down[count].get_rect(topleft=(sprite_x, sprite_y)).colliderect(heart_img[cnt].get_rect(topleft=(heart.x, heart.y))):
                    hearts.remove(heart)
                    if lives < 3:
                        lives += 1

            # Обновление и отрисовка врагов
            for enemy in enemies_sarah:
                enemy.update(change_x, change_y)
                enemy.draw(count, enemy_sarah_img[cnt])

                # Проверка столкновения врага с спрайтом
                if sprite_down[count].get_rect(topleft=(sprite_x, sprite_y)).colliderect(enemy_sarah_img[count].get_rect(topleft=(enemy.x, enemy.y))):
                    enemies_sarah.remove(enemy)
                    lives -= 1

                if enemy.x < -150 or enemy.x > WIDTH + 150 or enemy.y < -150 or enemy.y > HEIGHT + 150:
                    enemies_sarah.remove(enemy)

            for enemy in enemies_vika:
                enemy.update(change_x, change_y)
                enemy.draw(count, enemy_vika_img[cnt])

                # Проверка столкновения врага с спрайтом
                if sprite_down[count].get_rect(topleft=(sprite_x, sprite_y)).colliderect(enemy_vika_img[count].get_rect(topleft=(enemy.x, enemy.y))):
                    enemies_vika.remove(enemy)
                    lives -= 1

                if enemy.x < -150 or enemy.x > WIDTH + 150 or enemy.y < -150 or enemy.y > HEIGHT + 150:
                    enemies_vika.remove(enemy)

            for enemy in enemies_amanda:
                enemy.update(change_x, change_y)
                enemy.draw(count, enemy_amanda_img[cnt])
            

                # Проверка столкновения врага с спрайтом
                if sprite_down[count].get_rect(topleft=(sprite_x, sprite_y)).colliderect(enemy_amanda_img[count].get_rect(topleft=(enemy.x, enemy.y))):
                    enemies_amanda.remove(enemy)
                    lives -= 1

                if enemy.x < -150 or enemy.x > WIDTH + 150 or enemy.y < -150 or enemy.y > HEIGHT + 150:
                    enemies_amanda.remove(enemy)
            
            # Обновление и отрисовка пуль бумеранга
            for bullet_boomerang in bullets_boomerang:
                bullet_boomerang.return_bullet += 1
                bullet_boomerang.update(change_x, change_y)
                bullet_boomerang.draw(boom_cnt)

                if sprite_down[count].get_rect(topleft=(sprite_x, sprite_y)).colliderect(boomerang_img[boom_cnt].get_rect(topleft=(bullet_boomerang.x, bullet_boomerang.y))):
                    if bullet_boomerang.delta == 5:
                        bullets_boomerang.remove(bullet_boomerang)
                        bullet_boomerang.return_bullet = 0
                        bullet_boomerang.delta = 0
                    bullet_boomerang.delta += 1
                    

                # Проверка столкновения пули с врагом
                for enemy in enemies_sarah:
                    if boomerang_img[boom_cnt].get_rect(topleft=(bullet_boomerang.x, bullet_boomerang.y)).colliderect(enemy_sarah_img[count].get_rect(topleft=(enemy.x, enemy.y))):
                        try: 
                            enemy.hp -= 1
                            if enemy.hp <= 0:
                                enemies_sarah.remove(enemy)
                                score += 10
                                # Создание монеты при смерти врага
                                if random.randint(0, 5) == 2:
                                    coin = Coin(enemy.x, enemy.y)
                                    coins.append(coin)
                                # Создание сердец при смерти врага
                                elif random.randint(0, 10) == 2:
                                    heart = Heart(enemy.x, enemy.y)
                                    hearts.append(heart)
                        except ValueError:
                            pass                  

                # Проверка столкновения пули с врагом
                for enemy in enemies_vika:
                    if boomerang_img[boom_cnt].get_rect(topleft=(bullet_boomerang.x, bullet_boomerang.y)).colliderect(enemy_vika_img[count].get_rect(topleft=(enemy.x, enemy.y))):
                        try: 
                            enemy.hp -= 1
                            if enemy.hp <= 0:
                                enemies_vika.remove(enemy)
                                score += 15
                                # Создание монеты при смерти врага
                                if random.randint(0, 5) == 2:
                                    coin = Coin(enemy.x, enemy.y)
                                    coins.append(coin)
                                # Создание сердец при смерти врага
                                elif random.randint(0, 10) == 2:
                                    heart = Heart(enemy.x, enemy.y)
                                    hearts.append(heart)
                        except ValueError:
                            pass

                # Проверка столкновения пули с врагом
                for enemy in enemies_amanda:
                    if boomerang_img[boom_cnt].get_rect(topleft=(bullet_boomerang.x, bullet_boomerang.y)).colliderect(enemy_amanda_img[count].get_rect(topleft=(enemy.x, enemy.y))):
                        try: 
                            enemy.hp -= 1
                            if enemy.hp <= 0:
                                enemies_amanda.remove(enemy)
                                score += 15
                                # Создание монеты при смерти врага
                                if random.randint(0, 5) == 2:
                                    coin = Coin(enemy.x, enemy.y)
                                    coins.append(coin)
                                # Создание сердец при смерти врага
                                elif random.randint(0, 10) == 2:
                                    heart = Heart(enemy.x, enemy.y)
                                    hearts.append(heart)

                        except ValueError:
                            pass

            # Обновление и отрисовка пуль
            for bullet in bullets:
                bullet.update(change_x, change_y)
                bullet.draw(cnt, gun_type)

                # Удаление пуль, вышедших за границы экрана
                if bullet.x < 0 or bullet.x > WIDTH or bullet.y < 0 or bullet.y > HEIGHT:
                    bullets.remove(bullet)

                # Проверка столкновения пули с врагом
                for enemy in enemies_sarah:
                    if bullet_img[cnt].get_rect(topleft=(bullet.x, bullet.y)).colliderect(enemy_sarah_img[count].get_rect(topleft=(enemy.x, enemy.y))):
                        try: 
                            bullets.remove(bullet)
                            enemy.hp -= 1
                            if enemy.hp <= 0:
                                enemies_sarah.remove(enemy)
                                score += 10
                                # Создание монеты при смерти врага
                                if random.randint(0, 5) == 2:
                                    coin = Coin(enemy.x, enemy.y)
                                    coins.append(coin)
                                # Создание сердец при смерти врага
                                elif random.randint(0, 10) == 2:
                                    heart = Heart(enemy.x, enemy.y)
                                    hearts.append(heart)
                        except ValueError:
                            pass                  

                # Проверка столкновения пули с врагом
                for enemy in enemies_vika:
                    if bullet_img[cnt].get_rect(topleft=(bullet.x, bullet.y)).colliderect(enemy_vika_img[count].get_rect(topleft=(enemy.x, enemy.y))):
                        try: 
                            bullets.remove(bullet)
                            enemy.hp -= 1
                            if enemy.hp <= 0:
                                enemies_vika.remove(enemy)
                                score += 15
                                # Создание монеты при смерти врага
                                if random.randint(0, 5) == 2:
                                    coin = Coin(enemy.x, enemy.y)
                                    coins.append(coin)
                                # Создание сердец при смерти врага
                                elif random.randint(0, 10) == 2:
                                    heart = Heart(enemy.x, enemy.y)
                                    hearts.append(heart)
                        except ValueError:
                            pass

                # Проверка столкновения пули с врагом
                for enemy in enemies_amanda:
                    if bullet_img[cnt].get_rect(topleft=(bullet.x, bullet.y)).colliderect(enemy_amanda_img[count].get_rect(topleft=(enemy.x, enemy.y))):
                        try: 
                            bullets.remove(bullet)
                            enemy.hp -= 1
                            if enemy.hp <= 0:
                                enemies_amanda.remove(enemy)
                                score += 15
                                # Создание монеты при смерти врага
                                if random.randint(0, 5) == 2:
                                    coin = Coin(enemy.x, enemy.y)
                                    coins.append(coin)
                                # Создание сердец при смерти врага
                                elif random.randint(0, 10) == 2:
                                    heart = Heart(enemy.x, enemy.y)
                                    hearts.append(heart)

                        except ValueError:
                            pass
                
            # Отрисовка жизней
            font = pygame.font.SysFont(None, 30)
            lives_text = font.render("Lives: " + str(lives), True, RED)
            screen.blit(lives_text, (10, 10))

            score_text = font.render("Score: " + str(score), True, WHITE)
            screen.blit(score_text, (10, 40))

            coin_text = font.render("Coins: " + str(coins_score), True, WHITE)
            screen.blit(coin_text, (10, 70))

            # Ограничение FPS
            clock.tick(60)

            if fireball_icon_trigger and fireball_icon_cnt < 60:
                fireball_icon_cnt += 1
                shotgun_icon_trigger = False
                boomerang_icon_trigger = False
                screen.blit(fireball_icon, (30, HEIGHT-175))
                screen.blit(frame_grey, (30, HEIGHT-175))
            elif fireball_cnt > 60:
                fireball_icon_cnt = 0
                fireball_icon_trigger = False    

            if shotgun_icon_trigger and shotgun_icon_cnt < 60 :
                fireball_icon_trigger = False  
                boomerang_icon_trigger = False  
                shotgun_icon_cnt += 1
                screen.blit(shotgun_icon, (30, HEIGHT-175))
                screen.blit(frame_grey, (30, HEIGHT-175))
            elif shotgun_icon_cnt > 60:
                shotgun_icon_cnt = 0
                shotgun_icon_trigger = False   


            if boomerang_icon_trigger and boomerang_icon_cnt < 60 :
                fireball_icon_trigger = False  
                shotgun_icon_trigger = False  
                boomerang_icon_cnt += 1
                screen.blit(boomerang_icon, (30, HEIGHT-175))
                screen.blit(frame_grey, (30, HEIGHT-175))
            elif boomerang_icon_cnt > 60:
                boomerang_icon_cnt = 0
                boomerang_icon_trigger = False   

            if keys[pygame.K_l] or lives <= 0:
                rungame = False     

        # Экран проигрыша 
          
        else:
            if death_check == True:
                your_score = score
                if best_score < your_score:
                    with open('save/save.txt', "r+") as file:
                        best_score = your_score
                        content = file.read()
                        replace_content = re.sub(pattern_best_score,f'best_score:{best_score}:', content)
                        file.seek(0)
                        file.write(replace_content)
                        file.truncate()
                your_score_label = label.render(f'Score: {your_score}', True, (219, 42, 2))
                best_score_label = small_label.render(f'Best Score: {best_score}', True,(219, 42, 2))
            
                for i1 in range(6):
                    screen.blit(bg, (bg_x, bg_y))
                    screen.blit(bg, (bg_x + 1025, bg_y))
                    screen.blit(bg, (bg_x - 1025, bg_y))
                    screen.blit(bg, (bg_x, bg_y + 1025))
                    screen.blit(bg, (bg_x, bg_y - 1025))
                    screen.blit(bg, (bg_x + 1025, bg_y + 1025))
                    screen.blit(bg, (bg_x - 1025, bg_y + 1025))
                    screen.blit(bg, (bg_x + 1025, bg_y - 1025))
                    screen.blit(bg, (bg_x - 1025, bg_y - 1025))

                    # Отрисовка жизней
                    font = pygame.font.SysFont(None, 30)
                    lives_text = font.render("Lives: " + str(lives), True, RED)
                    screen.blit(lives_text, (10, 10))

                    score_text = font.render("Score: " + str(score), True, WHITE)
                    screen.blit(score_text, (10, 40))

                    coin_text = font.render("Coins: " + str(coins_score), True, WHITE)
                    screen.blit(coin_text, (10, 70))
                    if skin == '1':
                        screen.blit(sprite_dead[i1], (sprite_x, sprite_y))
                    elif skin == '2':
                        screen.blit(sprite_dead[i1], (sprite_x, sprite_y))
                    pygame.display.update()
                    sleep(0.1)
                screen.blit(bg, (bg_x, bg_y))
                screen.blit(bg, (bg_x + 1025, bg_y))
                screen.blit(bg, (bg_x - 1025, bg_y))
                screen.blit(bg, (bg_x, bg_y + 1025))
                screen.blit(bg, (bg_x, bg_y - 1025))
                screen.blit(bg, (bg_x + 1025, bg_y + 1025))
                screen.blit(bg, (bg_x - 1025, bg_y + 1025))
                screen.blit(bg, (bg_x + 1025, bg_y - 1025))
                screen.blit(bg, (bg_x - 1025, bg_y - 1025))

                # Отрисовка жизней
                font = pygame.font.SysFont(None, 30)
                lives_text = font.render("Lives: " + str(lives), True, RED)
                screen.blit(lives_text, (10, 10))

                score_text = font.render("Score: " + str(score), True, WHITE)
                screen.blit(score_text, (10, 40))

                coin_text = font.render("Coins: " + str(coins_score), True, WHITE)
                screen.blit(coin_text, (10, 70))
                pygame.display.update()
                sleep(0.5)
                death_check = False
            
            

                
            screen.blit(lose_bg_img, (0,0))
            screen.blit(lose_label, (WIDTH // 2 - lose_label.get_width() // 2,400))
            screen.blit(restart_label, restart_label_rect)
            screen.blit(your_score_label, (WIDTH // 2 - your_score_label.get_width() // 2, 600))
            screen.blit(best_score_label, (WIDTH - 300, 200))

            if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                # Обнуление значений после смерти
                enemies_sarah = []
                enemies_vika = []
                enemies_amanda = []
                bullets = []
                bullets_boomerang = []
                hearts = []
                coins = []
                sarah_amount = 20
                sarah_spawn_chance = 2
                sarah_speed = 2
                vika_amount = 10
                vika_spawn_chance = 2
                vika_speed = 2.5
                vika_hp = 1
                amanda_hp = 3
                amanda_amount = 10
                amanda_spawn_chance = 2
                amanda_speed = 1.5
                lives = 3
                score = 0
                with open('save/save.txt', "r+") as file:
                    money += coins_score 
                    content = file.read()
                    replace_content = re.sub(pattern_money,f'money:{money}:', content)
                    file.seek(0)
                    file.write(replace_content)
                    file.truncate()
                coins_score = 0
                main_menu = True
                start_game = False
    
    pygame.display.update()


    clock.tick(60)

# Завершение работы Pygame
pygame.quit()