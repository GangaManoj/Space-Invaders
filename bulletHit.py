#step six
#increasing score and respawning alien on collision with bullet

import pygame
import random
import math

# initialise pygame
pygame.init()

# creating the screen
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('bg.jpeg')

# setting the title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
player_dx = 0

# alien
alienImg = pygame.image.load('alien.png')
alienX = random.randint(0, 736)
alienY = random.randint(50, 150)
alien_dx = 1
alien_dy = 40

# bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bullet_dy = 10
bullet_state = "ready"

score = 0

def player(x, y):
    screen.blit(playerImg, (x, y))


def alien(x, y):
    screen.blit(alienImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fired"
    screen.blit(bulletImg, (x + 16, y + 10))

def collision(bulletX, bulletY, alienX, alienY):
    distance = math.sqrt(math.pow(bulletX - alienX, 2) + math.pow(bulletY - alienY, 2))
    if distance < 27:
        return True
    return False

# game loop
running = True
while running:
    # changing the display color
    screen.fill((0, 0, 0))
    # setting the background
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:  # checks if any key was pressed
            if event.key == pygame.K_LEFT:  # checks if the key pressed was the left arrow key
                player_dx = -3
            if event.key == pygame.K_RIGHT:  # checks if the key pressed was the right arrow key
                player_dx = 3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:  # checks if key was just released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_dx = 0

    playerX += player_dx
    # setting boundaries for the player
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    player(playerX, playerY)

    # alien movement
    alienX += alien_dx
    if alienX <= 0:
        alien_dx = 1
        alienY += alien_dy
    elif alienX > 736:
        alien_dx = -1
        alienY += alien_dy
    alien(alienX, alienY)

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fired":
        fire_bullet(bulletX, bulletY)
        bulletY -= bullet_dy

    # collision
    if collision(bulletX, bulletY, alienX, alienY):
        score += 100
        bulletY = 480
        bullet_state = "ready"
        alienX = random.randint(0, 736)
        alienY = random.randint(50, 150)
        print(score)

    pygame.display.update()
