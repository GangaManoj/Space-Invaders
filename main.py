import pygame
import random
import math

from pygame import mixer

# initialise pygame
pygame.init()

# creating the screen
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('bg.jpeg')

# setting the title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#background music
mixer.music.load('background.wav')
mixer.music.play(-1)

# player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
player_dx = 0

# alien
alienImg = []
alienX = []
alienY = []
alien_dx = []
alien_dy = []
num_of_aliens = 6

for i in range(num_of_aliens):
    alienImg.append(pygame.image.load('alien.png'))
    alienX.append(random.randint(0, 736))
    alienY.append(random.randint(50, 150))
    alien_dx.append(1)
    alien_dy.append(40)

# bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bullet_dy = 10
bullet_state = "ready"

# score
score_value = 0
font = pygame.font.Font('score.ttf', 32)
textX = 10
textY = 10

def score(x, y):
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))

def player(x, y):
    screen.blit(playerImg, (x, y))


def alien(x, y, i):
    screen.blit(alienImg[i], (x, y))


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
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
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
    
    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fired":
        fire_bullet(bulletX, bulletY)
        bulletY -= bullet_dy

    # alien movement
    for i in range(num_of_aliens):
        alienX[i] += alien_dx[i]
        if alienX[i] <= 0:
            alien_dx[i] = 1
            alienY[i] += alien_dy[i]
        elif alienX[i] > 736:
            alien_dx[i] = -1
            alienY[i] += alien_dy[i]
        alien(alienX[i], alienY[i], i)

        # collision
        if collision(bulletX, bulletY, alienX[i], alienY[i]):
            collision_sound = mixer.Sound('explosion.wav')
            collision_sound.play()
            score_value += 100
            bulletY = 480
            bullet_state = "ready"
            alienX[i] = random.randint(0, 736)
            alienY[i] = random.randint(50, 150)

    score(textX, textY)
    pygame.display.update() 