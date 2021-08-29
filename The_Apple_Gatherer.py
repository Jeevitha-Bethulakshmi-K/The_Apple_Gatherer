import time
import pygame
import random
import math
from pygame import mixer

# initializing

pygame.init()

#  creating window

window = pygame.display.set_mode((1200, 700))
background = pygame.image.load('background.png')

# game name and game icon

pygame.display.set_caption(" The Apple Gatherer")
icon = pygame.image.load('apple.png')
pygame.display.set_icon(icon)

# background music

mixer.music.load("background_music.wav")
mixer.music.play(-1)

# designing player

playerImg = pygame.image.load('player.png')
playerImg=pygame.transform.scale(playerImg,(150,250))
playerX = 600
playerY = 450
playerX_change = 0

# designing apple

appleImg = []
appleX = []
appleY = []
appleY_change = []
num_of_apple= 4

for i in range(num_of_apple):
    appleImg.append(pygame.image.load('apple.png'))
    appleX.append(random.randint(50,1150) )
    appleY.append(random.randint(0,150))
    appleY_change.append(4)

# score font

score_val = 0
score_font = pygame.font.Font('freesansbold.ttf', 32)

# life font

life_remaining=5
life_font=pygame.font.Font('freesansbold.ttf',30)

# title font

title_font=pygame.font.Font('freesansbold.ttf',36)

# display title

def show_title():
    title=title_font.render("The Apple Gatherer",True,(255,0,0))
    window.blit(title,(420,10))

# display life

def show_life():
    life=life_font.render("Life : "+str(life_remaining), True,(255,255,51))
    window.blit(life,(0,10))

# display score

def show_score():
    score = score_font.render("Score : " + str(score_val), True, (255,255,51))
    window.blit(score, (1000, 10))

# display player

def player(x, y):
    window.blit(playerImg, (x, y))

# display apple

def apple(x, y,i):
    window.blit(appleImg[i], (x, y))

# apple gathering

def isTouch(appleX, appleY, playerX, playerY):
    box_X=playerX+75
    box_Y=playerY+50
    distance = math.sqrt(math.pow(appleX - box_X,2) + (math.pow(appleY - box_Y, 2)))
    if distance <50:
        return True
    else:
        return False
# main loop

run = True
while run:
    pygame.time.delay(100)

    window.fill((0, 0, 0))

    window.blit(background, (0, 0))

    # events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -10
        if event.key == pygame.K_RIGHT:
            playerX_change = 10

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 1050:
        playerX = 1050

    player(playerX, playerY)

    for i in range(num_of_apple):

        if appleY[i]<644:
            appleY[i]+=appleY_change[i]

        touch = isTouch(appleX[i], appleY[i], playerX, playerY)
        # increasing score
        if touch:

            score_val += 1

            appleX[i] = 2000
            appleY[i] = 2000
            # apple collecting sound
            appleSound = mixer.Sound("apple.wav")
            appleSound.play()

        if appleY[i] >=644:
            appleY[i]=2000

            appleX[i] = random.randint(50, 1150)
            appleY[i] = random.randint(0, 150)
            if touch == False:
                life_remaining -= 1

                if life_remaining <= 0:
                    run=False

        apple(appleX[i], appleY[i], i)

    show_score()
    show_life()
    show_title()
    pygame.display.update()

pygame.quit()