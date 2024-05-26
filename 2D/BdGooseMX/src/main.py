import asyncio
import random
import sys
import os
import time
import pygame
from os.path import abspath
path = (os.path.dirname(os.path.abspath(__file__))) 
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT, K_SPACE, K_ESCAPE, K_RETURN
pygame.init()
FPS = pygame.time.Clock()
TIMER_show = pygame.font.SysFont('Verdana', 72)
HIT_show = pygame.font.SysFont('Verdana', 72)
GameOVER = -1
timer_interval = 0
timer = 20
timer_clock = pygame.time.Clock()
text_place = 'tHIT SPOT'
text_place2 = 'tHIT SPOT'
text_place3 = 'tHIT SPOT'
sysfont = pygame.font.get_default_font()
font = pygame.font.SysFont(None, 78)
global HIT
HIT = 0
HEIGHT = 660
WIDTH = 800
IMAGE_PATH = path+"//"+"Goose"
PLAYER_IMAGES = os.listdir(IMAGE_PATH)
player_imagenext = 1
FONT = pygame.font.SysFont('Verdana', 72)
WIN = pygame.font.SysFont('Verdana', 72)
WIN1 = pygame.font.SysFont('Verdana', 72)
WIN2 = pygame.font.SysFont('Verdana', 72)
BONUS_ROUND = pygame.font.SysFont('Verdana', 72)
BONUS_RNDtxt = ' '
info =  pygame.font.SysFont('Verdana', 52)
info_text = 'Numo! GADUTI !!! - SPACE -' 
info_DONE = 0
score = 0
scoreAll = 0
image_index = 0
score_increment = 10
spacebtn = -40
RED = (255, 0, 0)
WHITE = (155, 155, 255)
COLOR_GREEN = (0, 255, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREY = (125, 125, 125)
COLOR_BLACK = (0, 0, 0)
COLOR_BLY = (255, 255, 0)
COLOR_RED = (255, 0, 0)
COLOR_YELLOW = (0, 0, 255)
sysfont = pygame.font.get_default_font()
main_display = pygame.display.set_mode((WIDTH,HEIGHT))
bg = pygame.transform.scale(pygame.image.load(path+'//'+'image/background.png'),(WIDTH,HEIGHT))
bg_X1 = 0
bg_X2 = bg.get_width()
bg_move = 3
player_size = (20, 20)
player = pygame.transform.scale(pygame.image.load(path+'//'+'image/player.png').convert_alpha(),(160,80))
player_rect = player.get_rect()
player_move_down = [0, 7] 
player_move_right = [6, 0]
player_move_up = [0, -6] 
player_move_left = [-5, 0]
keys = pygame.key.get_pressed()
playing = True
enemy_speed=3
inMainGame=False
list_of_mainplay = []
up_ui_size =(400,200)
up_ui = pygame.Surface(up_ui_size, pygame.SRCALPHA)
up_ui_rect = pygame.Rect((WIDTH/2-200), HEIGHT-HEIGHT, *up_ui_size)
up_ui.fill((255,255,255,18))
down_ui_size =(400,200)
down_ui = pygame.Surface(down_ui_size, pygame.SRCALPHA)
down_ui_rect = pygame.Rect((WIDTH/2-200), (HEIGHT/2-100), *down_ui_size)
down_ui.fill((255,255,255,18))
left_ui_size =(150,400)
left_ui = pygame.Surface(left_ui_size, pygame.SRCALPHA)
left_ui_rect = pygame.Rect((WIDTH-WIDTH+20), (HEIGHT/2-250), *left_ui_size)
left_ui.fill((255,255,255,18))
right_ui_size =(150,400)
right_ui = pygame.Surface(right_ui_size, pygame.SRCALPHA)
right_ui_rect = pygame.Rect(WIDTH-170, (HEIGHT/2-250), *right_ui_size)
right_ui.fill((255,255,255,18))
esc_ui_size =(100,100)
esc_ui = pygame.Surface(esc_ui_size, pygame.SRCALPHA)
esc_ui_rect = pygame.Rect((WIDTH-WIDTH), (HEIGHT-HEIGHT), *esc_ui_size)
esc_ui.fill((255,255,255,18))
space_ui_size =(400,120) 
space_ui = pygame.Surface(space_ui_size, pygame.SRCALPHA)
space_ui_rect = pygame.Rect((WIDTH/2-200), (HEIGHT-150), *space_ui_size)
space_ui.fill((255,255,255,18))
up_ui_pressed=False
down_ui_pressed=False
left_ui_pressed=False
right_ui_pressed=False
player_sz= (player.get_rect().width,player.get_rect().height)
def text_objects(text, font):
    textSurface = font.render(text, True, (0,200,0))
    return textSurface, textSurface.get_rect()
def create_enemy (): 
    enemy_size = (30, 30)
    enemy = pygame.transform.scale(pygame.image.load(path+'//'+'image/enemy.png').convert_alpha(),(140,60))
    enemy_width =  enemy.get_width()
    enemy_height = enemy.get_height()
    enemy_rect = pygame.Rect((WIDTH + enemy.get_width()), random.randint(150 + enemy.get_height(), ((HEIGHT - enemy.get_height()) - 200)), *enemy_size)                                       
    enemy_move = [random.randint (-enemy_speed*2, -enemy_speed), 0]
    return [enemy, enemy_rect, enemy_move, enemy_width, enemy_height] 
def create_bonus ():
    bonus_size = (40, 40)
    bonus = pygame.transform.scale(pygame.image.load(path+'//'+'image/bonus.png').convert_alpha(),(100,120))
    bonus_width =  bonus.get_width()
    bonus_height = bonus.get_height()
    bonus_rect = pygame.Rect(random.randint(100, (WIDTH - bonus.get_width())), ((HEIGHT - HEIGHT) - bonus.get_height()), *bonus_size)                                                  
    bonus_move = [0, random.randint (4, 7)]
    return [bonus, bonus_rect, bonus_move, bonus_height, bonus_width] 
def create_torpeda():
    global score
    torpeda_size = (20, random.randint(10, 20))
    torpeda = pygame.Surface(torpeda_size)
    torpeda_rect = pygame.Rect(player_rect.left, player_rect.bottom, *torpeda_size)                                       
    torpeda.fill(COLOR_GREEN)
    #torpeda_rect = pygame.Rect(player_rect.left, player_rect.bottom, *torpeda_size)                                       
    torpeda_move = [0, random.randint (6, 14)]    
    torpeda_width = torpeda.get_size()[0]
    torpeda_heigth = torpeda.get_size()[1]
    return [torpeda, torpeda_rect, torpeda_move, torpeda_heigth, torpeda_width] 
    
def MainPlay(torpediX, bonusies, enemies, minusScore, SpeedUP, ScoreSpeedUP, ScoreSpeedUPamount, CREATE_ENEMY, CREATE_BONUS, CREATE_TORPEDA, CHANGE_IMAGE):
    global inMainGame 
    global FPS
    global TIMER_show
    global HIT_show
    global GameOVER
    global timer_interval
    global timer
    global timer_clock
    global text_place
    global text_place2
    global text_place3
    global sysfont
    global font
    global HIT
    global HEIGHT 
    global WIDTH
    global IMAGE_PATH
    global PLAYER_IMAGES
    global player_imagenext
    global FONT
    global WIN
    global WIN1
    global WIN2
    global BONUS_ROUND
    global BONUS_RNDtxt
    global info
    global info_text
    global info_DONE
    global score
    global scoreAll
    global image_index
    global score_increment
    global spacebtn
    global RED
    global WHITE
    global COLOR_GREEN
    global COLOR_WHITE
    global COLOR_GREY
    global COLOR_BLACK
    global COLOR_BLY
    global COLOR_RED
    global COLOR_YELLOW
    global main_display
    global bg
    global bg_X1
    global bg_X2
    global bg_move
    global player_size
    global player
    global player_rect
    global player_move_down
    global player_move_right
    global player_move_up 
    global player_move_left 
    global path
    global playing
    global keys
    global ESCAPE_text
    global ESCAPE_MENU
    global HIT
    if GameOVER!=1:
        global inMainGame 
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if GameOVER != 1 and GameOVER != 2:
            bg_X1 -= bg_move
            bg_X2 -= bg_move
        if bg_X1 < -bg.get_width() and GameOVER != 1 and GameOVER != 2:
            bg_X1 = bg.get_width()
        if bg_X2 < -bg.get_width() and GameOVER != 1 and GameOVER != 2:
            bg_X2 = bg.get_width()
        if GameOVER != 1 and GameOVER != 2:
            main_display.blit(bg, (bg_X1, 0))
            main_display.blit(bg, (bg_X2, 0))
        if keys[K_DOWN] and player_rect.bottom < HEIGHT and GameOVER != 1 and GameOVER != 2:
            player_rect = player_rect.move(player_move_down)
        if keys[K_UP] and player_rect.top > (HEIGHT - HEIGHT) and GameOVER != 1 and GameOVER != 2:
            player_rect = player_rect.move(player_move_up)
        if keys[K_RIGHT] and player_rect.right < WIDTH and GameOVER != 1 and GameOVER != 2:
            player_rect =  player_rect.move(player_move_right)
        if keys[K_LEFT] and player_rect.left > (WIDTH - WIDTH) and GameOVER != 1 and GameOVER != 2:
            player_rect =  player_rect.move(player_move_left)
        if keys[K_SPACE] and score > 0  and GameOVER != 1 and GameOVER != 2:
            spacebtn = 0
            spacebtn += 30
            if ESCAPE_MENU==False:
                create_torpeda()
        if len(torpediX)<=0 and minusScore==True:
            minusScore = False        
        if len(torpediX)>=1 and minusScore==True:
            score =-1
            minusScore = False
        for torpeda in torpediX:
            if GameOVER != 1 and GameOVER != 2:
                torpeda[1] = torpeda[1].move(torpeda[2])
                main_display.blit(torpeda[0], torpeda[1])
        for enemy in enemies:
            if GameOVER != 1 and GameOVER != 2:
                enemy[1] = enemy[1].move(enemy[2])
                main_display.blit(enemy[0], enemy[1])
            for torpeda in torpediX:
                speedADD = False
                if torpeda[1].colliderect(enemy[1]) and HIT >= 0 and GameOVER != 1 and GameOVER != 2:
                    HIT+= 1
                    enemies.pop(enemies.index (enemy))
                    torpediX.pop(torpediX.index (torpeda))
                    minusScore = True
                    speedADD = True
                if HIT>=ScoreSpeedUP:
                    if speedADD:
                        global enemy_speed
                        enemy_speed=enemy_speed+round(HIT*0.4)
                        speedADD = False
                if HIT>ScoreSpeedUP+1:
                    ScoreSpeedUP=HIT+ScoreSpeedUPamount
                    enemy_speed=4
            if player_rect.colliderect(enemy[1]) and GameOVER != 1 and GameOVER != 2:
                GameOVER = 1
                inMainGame=False
        for bonus in bonusies:
            if GameOVER != 1 and GameOVER != 2:
                bonus[1] = bonus[1].move(bonus[2])
                main_display.blit(bonus[0], bonus[1])
            if player_rect.colliderect(bonus[1]) and GameOVER != 1 and GameOVER != 2:
                score+= 1
                global scoreAll
                scoreAll+= 1
                bonusies.pop(bonusies.index (bonus))
        if  info_DONE != 1 and spacebtn < 3 :
            info_text = 'Numo! GADUTI !!! - SPACE -' 
            main_display.blit(info.render(str(info_text), True, COLOR_YELLOW), (WIDTH/2-320, (HEIGHT - 90)))
            if spacebtn > 4 :
                info_DONE = 1
        if  info_DONE == 1 and spacebtn > 4 :
            info_text = '' 
            main_display.blit(info.render(str(info_text), True, COLOR_YELLOW), (WIDTH/2-60, (HEIGHT - 70)))
        for enemy in enemies:
            if enemy[1].left <= (WIDTH - WIDTH) - enemy[3]  or enemy[1].right >= (WIDTH + (2 * enemy[3])) or enemy[1].top <= ((HEIGHT - HEIGHT) + enemy[4])  or enemy[1].top >= (HEIGHT - enemy[4]) :
                enemies.pop(enemies.index(enemy))
        for bonus in bonusies:
            if bonus[1].left < ((WIDTH - WIDTH) + (bonus[3] * 2)) or bonus[1].right >= (WIDTH - bonus[3]) or bonus[1].top >= (HEIGHT) or bonus[1].top <= ((HEIGHT - HEIGHT) - (bonus[4] * 2)):
                bonusies.pop(bonusies.index(bonus))
        for torpeda in torpediX:
            if torpeda[1].left < ((WIDTH - WIDTH) - (torpeda[3] * 3)) or torpeda[1].right >= (WIDTH - torpeda[3]) or torpeda[1].top >= (HEIGHT - torpeda[4]) or torpeda[1].top <= ((HEIGHT - HEIGHT) - (torpeda[4] * 2)):
                torpediX.pop(torpediX.index(torpeda))
                minusScore = True
        if ESCAPE_MENU==False:
            main_display.blit(FONT.render(str(score), True, COLOR_BLACK), (WIDTH-80, 20))
            main_display.blit(FONT.render(str(scoreAll), True, COLOR_GREY), (WIDTH-(165+scoreAll*0.2), 20))
            main_display.blit(HIT_show.render(str(HIT), True, COLOR_RED), ((WIDTH-WIDTH) + 50, 20))    
            main_display.blit(player, player_rect)
            main_display.blit(up_ui, up_ui_rect)
            main_display.blit(down_ui, down_ui_rect)
            main_display.blit(left_ui, left_ui_rect)
            main_display.blit(right_ui, right_ui_rect)
            main_display.blit(esc_ui, esc_ui_rect)
            main_display.blit(space_ui, space_ui_rect)
        if SpeedUP==True:
            ScoreSpeedUP = HIT + ScoreSpeedUPamount
            SpeedUP==False
        if keys[K_ESCAPE] and ESCAPE_MENU==False:
            ESCAPE_MENU = True
            GameOVER=2
        if ESCAPE_MENU==True:
            ESCAPE_text = ' PLAY - Enter' 
            main_display.blit(info.render(str(ESCAPE_text), True, COLOR_RED), (WIDTH/2-260, (HEIGHT - 140)))
            keys = pygame.key.get_pressed()
            if keys[K_RETURN] and ESCAPE_MENU==True:
                main_display.blit(info.render(str(ESCAPE_text), True, COLOR_RED), (WIDTH/2-260, (HEIGHT - 140)))
                pygame.display.update()
                GameOVER=0
                ESCAPE_text = '' 
                pygame.display.update()
                ESCAPE_MENU=False
        global list_of_mainplay
        list_of_mainplay = [torpediX, bonusies, enemies, minusScore, SpeedUP, ScoreSpeedUP, ScoreSpeedUPamount, list_of_mainplay[7], list_of_mainplay[8], list_of_mainplay[9], list_of_mainplay[10] ]

    
def PLAYING_GAME ():
    global inMainGame 
    global FPS
    global TIMER_show
    global HIT_show
    global GameOVER
    global timer_interval
    global timer
    global timer_clock
    global text_place
    global text_place2
    global text_place3
    global sysfont
    global font
    global HIT
    global HEIGHT 
    global WIDTH
    global IMAGE_PATH
    global PLAYER_IMAGES
    global player_imagenext
    global FONT
    global WIN
    global WIN1
    global WIN2
    global BONUS_ROUND
    global BONUS_RNDtxt
    global info
    global info_text
    global info_DONE
    global score
    global scoreAll
    global image_index
    global score_increment
    global spacebtn
    global RED
    global WHITE
    global COLOR_GREEN
    global COLOR_WHITE
    global COLOR_GREY
    global COLOR_BLACK
    global COLOR_BLY
    global COLOR_RED
    global COLOR_YELLOW
    global main_display
    global bg
    global bg_X1
    global bg_X2
    global bg_move
    global player_size
    global player
    global player_rect
    global player_move_down
    global player_move_right
    global player_move_up 
    global player_move_left 
    global path
    global playing
    global keys
    global ESCAPE_text
    ESCAPE_text=''
    keys = pygame.key.get_pressed()
    global ESCAPE_MENU
    ESCAPE_MENU = False
    global minusScore
    minusScore = True
    global ScoreSpeedUP
    ScoreSpeedUP = 0
    global ScoreSpeedUPamount
    ScoreSpeedUPamount = 3
    global SpeedUP
    SpeedUP = False
    enemies = []
    bonusies= []
    torpediX= []
    timer_clock = 20
    FPS.tick (20)
    timer = 20
    global enemy_speed
    enemy_speed=3
    pygame.display.update()
    global list_of_mainplay
    list_of_mainplay = [torpediX, bonusies, enemies, minusScore, SpeedUP, ScoreSpeedUP, ScoreSpeedUPamount, 0, 0, 0, 0]
    inMainGame=True
    global player_rect
    global player_sz
    player_rect = pygame.Rect((WIDTH-WIDTH), (HEIGHT-HEIGHT), *player_sz)

    
async def main():
    global playing
    playing = True
    global FPS
    global TIMER_show
    global HIT_show
    global GameOVER
    global timer_interval
    global timer
    global timer_clock
    global text_place
    global text_place2
    global text_place3
    global sysfont
    global font
    global HIT
    global HEIGHT 
    global WIDTH
    global IMAGE_PATH
    global PLAYER_IMAGES
    global player_imagenext
    global FONT
    global WIN
    global WIN1
    global WIN2
    global BONUS_ROUND
    global BONUS_RNDtxt
    global info
    global info_text
    global info_DONE
    global score
    global scoreAll
    global image_index
    global score_increment
    global spacebtn
    global RED
    global WHITE
    global COLOR_GREEN
    global COLOR_WHITE
    global COLOR_GREY
    global COLOR_BLACK
    global COLOR_BLY
    global COLOR_RED
    global COLOR_YELLOW
    global main_display
    global bg
    global bg_X1
    global bg_X2
    global bg_move
    global player_size
    global player
    global player_rect
    global player_move_down
    global player_move_right
    global player_move_up 
    global player_move_left 
    global path
    global keys
    global up_ui_pressed
    global down_ui_pressed
    global left_ui_pressed
    global right_ui_pressed

    global ESCAPE_text
    ESCAPE_text=''
    global ESCAPE_MENU
    ESCAPE_MENU = False
    minusScore = True
    info_DONE = 0
    score = 0
    scoreAll = 0
    HIT = 0
    HEIGHT = 660
    WIDTH = 800
    GameOVER = -1
    timer_interval = 0
    timer = 10
    IMAGE_PATH = path+"//"+"Goose"
    PLAYER_IMAGES = os.listdir(IMAGE_PATH)
    player_imagenext = 1
    FONT = pygame.font.SysFont('Verdana', 72)
    WIN = pygame.font.SysFont('Verdana', 72)
    WIN1 = pygame.font.SysFont('Verdana', 72)
    WIN2 = pygame.font.SysFont('Verdana', 72)
    BONUS_ROUND = pygame.font.SysFont('Verdana', 72)
    BONUS_RNDtxt = ' '
    info =  pygame.font.SysFont('Verdana', 52)
    info_text = 'Numo! GADUTI !!! - SPACE -' 
    info_DONE = 0
    score = 0
    scoreAll = 0
    image_index = 0
    score_increment = 10
    spacebtn = -40
    RED = (255, 0, 0)
    WHITE = (155, 155, 255)
    COLOR_GREEN = (0, 255, 0)
    COLOR_WHITE = (255, 255, 255)
    COLOR_GREY = (125, 125, 125)
    COLOR_BLACK = (0, 0, 0)
    COLOR_BLY = (255, 255, 0)
    COLOR_RED = (255, 0, 0)
    COLOR_YELLOW = (0, 0, 255)
    sysfont = pygame.font.get_default_font()
    main_display = pygame.display.set_mode((WIDTH,HEIGHT))
    bg = pygame.transform.scale(pygame.image.load(path+'//'+'image/background.png'),(WIDTH,HEIGHT))
    bg_X1 = 0
    bg_X2 = bg.get_width()
    bg_move = 3
    player_size = (20, 20)
    player = pygame.transform.scale(pygame.image.load(path+'//'+'image/player.png').convert_alpha(),(160,80))
    player_rect = player.get_rect()
    player_move_down = [0, 7] 
    player_move_right = [6, 0]
    player_move_up = [0, -6] 
    player_move_left = [-5, 0]
    enemy_speed=3                
    CREATE_ENEMY = pygame.USEREVENT+1
    pygame.time.set_timer(CREATE_ENEMY, 1200)
    CREATE_BONUS = pygame.USEREVENT+2
    pygame.time.set_timer(CREATE_BONUS, 1400)
    CREATE_TORPEDA = pygame.USEREVENT+3
    pygame.time.set_timer(CREATE_TORPEDA, 950)
    timer_event = pygame.USEREVENT +4
    pygame.time.set_timer(timer_event, timer_interval)
    CHANGE_IMAGE = pygame.USEREVENT +5
    pygame.time.set_timer(CHANGE_IMAGE, 140)
    FPS.tick (10)
    timer_clock = 10
    timer=10
    while playing:
        global inMainGame
        if inMainGame!=True:
            FPS.tick (10)
            timer_clock = 10
            timer=10
        keys = pygame.key.get_pressed()
        for event in pygame.event.get ():
            if event.type == QUIT:
                playing = False
                pygame.quit()
                sys.exit
            if inMainGame==False: 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    GameOVER = 0
                    Info_DONE = 0      
                    HIT = 0
                    score = 0
                    scoreAll = 0
                    inMainGame=True
                    PLAYING_GAME()
                    list_of_mainplay[7]=CREATE_ENEMY
                    list_of_mainplay[8]=CREATE_BONUS
                    list_of_mainplay[9]=CREATE_TORPEDA
                    list_of_mainplay[10]=CHANGE_IMAGE
            elif inMainGame==True:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()  
                    if up_ui_rect.collidepoint(pos) and player_rect.top > (HEIGHT - HEIGHT) and GameOVER != 1 and GameOVER != 2:
                        up_ui_pressed=True
                        down_ui_pressed=False
                        left_ui_pressed=False
                        right_ui_pressed=False
                    elif down_ui_rect.collidepoint(pos) and player_rect.bottom < HEIGHT and GameOVER != 1 and GameOVER != 2:
                        down_ui_pressed=True
                        up_ui_pressed=False
                        left_ui_pressed=False
                        right_ui_pressed=False
                    elif left_ui_rect.collidepoint(pos) and player_rect.left > (WIDTH - WIDTH) and GameOVER != 1 and GameOVER != 2:
                        left_ui_pressed=True
                        up_ui_pressed=False
                        down_ui_pressed=False
                        right_ui_pressed=False
                    elif right_ui_rect.collidepoint(pos) and player_rect.right < WIDTH and GameOVER != 1 and GameOVER != 2:
                        right_ui_pressed=True
                        up_ui_pressed=False
                        down_ui_pressed=False
                        left_ui_pressed=False
                    if space_ui_rect.collidepoint(pos):
                        up_ui_pressed=False
                        down_ui_pressed=False
                        left_ui_pressed=False
                        right_ui_pressed=False
                        if score > 0  and GameOVER != 1 and GameOVER != 2:
                            spacebtn = 0
                            spacebtn += 30
                            if ESCAPE_MENU==False:
                                create_torpeda()                  
                        elif ESCAPE_MENU==True:
                            main_display.blit(info.render(str(ESCAPE_text), True, COLOR_RED), (WIDTH/2-260, (HEIGHT - 140)))
                            pygame.display.update()
                            GameOVER=0
                            ESCAPE_text = '' 
                            pygame.display.update()
                            ESCAPE_MENU=False      
                    elif esc_ui_rect.collidepoint(pos) and ESCAPE_MENU==False:
                        up_ui_pressed=False
                        down_ui_pressed=False
                        left_ui_pressed=False
                        right_ui_pressed=False
                        ESCAPE_MENU = True
                        GameOVER=2
                if up_ui_pressed==True:
                    player_rect = player_rect.move(player_move_up)
                    down_ui_pressed=False
                    left_ui_pressed=False
                    right_ui_pressed=False
                elif down_ui_pressed==True:
                    player_rect = player_rect.move(player_move_down)                
                    up_ui_pressed=False
                    left_ui_pressed=False
                    right_ui_pressed=False
                elif left_ui_pressed==True:
                    player_rect =  player_rect.move(player_move_left)            
                    up_ui_pressed=False
                    down_ui_pressed=False
                    right_ui_pressed=False
                elif right_ui_pressed==True:
                    player_rect =  player_rect.move(player_move_right)     
                    up_ui_pressed=False
                    down_ui_pressed=False
                    left_ui_pressed=False
                if event.type == pygame.MOUSEBUTTONUP:
                    up_ui_pressed=False
                    down_ui_pressed=False
                    left_ui_pressed=False
                    right_ui_pressed=False
                if event.type == CREATE_ENEMY and HIT >=-1  and GameOVER != 1 and GameOVER != 2:
                    list_of_mainplay[2].append (create_enemy())
                if event.type == CREATE_BONUS and GameOVER != 1 and GameOVER != 2:
                    list_of_mainplay[1].append (create_bonus())
                if event.type == CREATE_TORPEDA and ESCAPE_MENU!=True and spacebtn >= 0 and score > 0 and GameOVER != 1 and GameOVER != 2:
                    list_of_mainplay[0].append (create_torpeda())
                    spacebtn -= 100
                if event.type == CHANGE_IMAGE and GameOVER != 2:
                    if image_index <= len(PLAYER_IMAGES) and player_imagenext == 1:            
                        player = pygame.image.load(os.path.join(IMAGE_PATH, PLAYER_IMAGES[image_index]))
                        image_index+= 1
                    if image_index >= len(PLAYER_IMAGES) and player_imagenext == 1:
                        image_index-= 1
                        player = pygame.image.load(os.path.join(IMAGE_PATH, PLAYER_IMAGES[image_index]))                              
                        player_imagenext = 0
                    if player_imagenext == 0 and image_index < len(PLAYER_IMAGES) and image_index != 0 :
                        player = pygame.image.load(os.path.join(IMAGE_PATH, PLAYER_IMAGES[image_index]))
                        image_index-= 1
                    if player_imagenext == 0 and image_index < len(PLAYER_IMAGES) and image_index == 0 :
                        image_index = 0
                        player_imagenext = 1
                        player = pygame.image.load(os.path.join(IMAGE_PATH, PLAYER_IMAGES[image_index]))
                
        if GameOVER == -1 and inMainGame!=True:
            inMainGame=False        
            main_display.fill((0, 0, 0))
            largeText = pygame.font.SysFont("tahoma",20)
            TextSurf, TextRect = text_objects("Space or Enter for START", largeText)
            TextRect.center = ((WIDTH/2),(HEIGHT/2))
            main_display.blit(TextSurf, TextRect)
            pygame.display.update() 
            if keys[K_SPACE] or keys[K_RETURN]:
                GameOVER = 0
                Info_DONE = 0      
                HIT = 0
                score = 0
                scoreAll = 0
                inMainGame=True
                PLAYING_GAME()
                list_of_mainplay[7]=CREATE_ENEMY
                list_of_mainplay[8]=CREATE_BONUS
                list_of_mainplay[9]=CREATE_TORPEDA
                list_of_mainplay[10]=CHANGE_IMAGE

        if GameOVER == 1 and inMainGame!=True: 
            up_ui_pressed=False
            down_ui_pressed=False
            left_ui_pressed=False
            right_ui_pressed=False
            inMainGame=False
            FPS.tick(10)            
            timer_clock=20
            timer=20
            main_display.fill((0, 0, 0))
            largeText = pygame.font.SysFont("tahoma",20)
            TextSurf, TextRect = text_objects("Game Over. Press Enter to restart.", largeText)
            TextRect.center = ((WIDTH/2),(HEIGHT/2))
            main_display.blit(TextSurf, TextRect)
            pygame.display.update() 
            if keys[K_RETURN]:
                GameOVER = 0
                Info_DONE = 0
                enemy_speed = 3
                minusScore = True
                ScoreSpeedUP = 0
                ScoreSpeedUPamount = 3
                HIT = 0
                score = 0
                scoreAll = 0
                inMainGame=True
                PLAYING_GAME()
                list_of_mainplay[7]=CREATE_ENEMY
                list_of_mainplay[8]=CREATE_BONUS
                list_of_mainplay[9]=CREATE_TORPEDA
                list_of_mainplay[10]=CHANGE_IMAGE

        if GameOVER != 1 and inMainGame==True:
            MainPlay(list_of_mainplay[0], list_of_mainplay[1], list_of_mainplay[2], list_of_mainplay[3], list_of_mainplay[4], list_of_mainplay[5], list_of_mainplay[6], list_of_mainplay[7], list_of_mainplay[8], list_of_mainplay[9], list_of_mainplay[10] )        
            
        if inMainGame==False:
            main_display.blit(FONT.render(str(score), True, COLOR_BLACK), (WIDTH-80, 20))
            main_display.blit(FONT.render(str(scoreAll), True, COLOR_GREY), (WIDTH-(166+scoreAll*0.2), 20))
            main_display.blit(HIT_show.render(str(HIT), True, COLOR_RED), ((WIDTH-WIDTH) + 50, 20))    
            main_display.blit(player, player_rect)
            pygame.display.flip()
        await asyncio.sleep(0)
asyncio.run(main())