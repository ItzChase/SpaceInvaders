# Last week I created collisions with the enemy and bullet i also created bullets
# this week i are creating mutiple enemy 1:47:56

import pygame

import math

import random

from pygame import mixer

# Init
pygame.init()

# CREATE THE SCREEN
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('items/background.png')

# backround sound
mixer.music.load('items/background.wav')
mixer.music.play(-1)

# title and icon
pygame.display.set_caption(" Space Game boi")
icon = pygame.image.load('items/ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('items/player.png')
playerX = 370
playerY = 480
playerX_change = 0

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 10

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('items/enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(1.5)
    enemyY_change.append(20)

# Bullet boi

# REady boi - You cant see the bullet on the screen
# Fire noi - the bullet is curently moving

bulletX = 0
bulletY = 480
bulletImg = pygame.image.load('items/bullet.png')
bulletX_change = 0
bulletY_change = 3
bullet_state = "ready"

# SCore

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# Game over tetx boi
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over = over_font.render(
        "GaMe OvEr :" + str(score_value), True, (255, 255, 255))
    screen.blit(over, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def bullery(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX)**2 + (enemyY - bulletY)**2)
    if distance < 27:
        return True
    else:
        return False


# game loop
running = True
while running:

    # RGB red - blue - green
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1.5
            if event.key == pygame.K_RIGHT:
                playerX_change = +1.5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('items/laser.wav')
                    bullet_sound.play()
                    # Get Current x coordinate of the spaceship
                    bulletX = playerX
                    bullery(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0.0

    # 370 = 370 + -0.1 -> 370 = 370 - 0.1
    # 370 = 370 + 0.1
    # This changes the coordinates of the ship when we press the LEFT or RIGHT arrows:
    playerX += playerX_change

    # This sets the border so the ship doesn't disappear from the screen:
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    for i in range(num_of_enemies):

        # game over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]

    # This sets the border so the enemy doesn't disappear from the screen:
        if enemyX[i] <= 0:
            # stop at left wall
            enemyX[i] = 0
            # makes enemy go the other way
            enemyX_change[i] = enemyX_change[i] * (-1)
            # makes enemy drop 1 level
            enemyY[i] = enemyY[i] + enemyY_change[i]

        elif enemyX[i] >= 736:
            # stop at right wall
            enemyX[i] = 736
            # makes enemy go the other way
            enemyX_change[i] = enemyX_change[i] * (-1)
            #  makes the enemy drop 1 level
            enemyY[i] = enemyY[i] + enemyY_change[i]

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound('items/explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        bullery(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
