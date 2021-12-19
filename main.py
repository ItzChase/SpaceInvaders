# Last week I created collisions with the enemy and bullet i also created bullets
# this week i are creating mutiple enemy 1:47:56

import pygame

import math

import random
# Init
pygame.init()

# CREATE THE SCREEN
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('items/background.png')

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
enemyImg = pygame.image.load('items/enemy.png')
enemyX = random.randint(0, 735)
enemyY = random.randint(50, 150)
enemyX_change = 1.5
enemyY_change = 20

# Bullet boi

# REady boi - You cant see the bullet on the screen
# Fire noi - the bullet is curently moving

bulletX = 0
bulletY = 480
bulletImg = pygame.image.load('items/bullet.png')
bulletX_change = 0
bulletY_change = 3
bullet_state = "ready"

score = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


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

    enemyX += enemyX_change

    # This sets the border so the enemy doesn't disappear from the screen:
    if enemyX <= 0:
        # stop at left wall
        enemyX = 0
        # makes enemy go the other way
        enemyX_change = enemyX_change * (-1)
        # makes enemy drop 1 level
        enemyY = enemyY + enemyY_change

    elif enemyX >= 736:
        # stop at right wall
        enemyX = 736
        # makes enemy go the other way
        enemyX_change = enemyX_change * (-1)
        #  makes the enemy drop 1 level
        enemyY = enemyY + enemyY_change

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        bullery(bulletX, bulletY)
        bulletY -= bulletY_change

    # Collision
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
