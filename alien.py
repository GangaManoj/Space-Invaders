#step three
#added a moving enemy alien

import pygame
import random

#initialise pygame
pygame.init()

#creating the screen
screen = pygame.display.set_mode((800, 600))

#setting the title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
player_dx = 0

#alien
alienImg = pygame.image.load('alien.png')
alienX = random.randint(0,736)
alienY = random.randint(50,150)
alien_dx = 0.3
alien_dy = 40

def player(x,y):
    screen.blit(playerImg, (x,y))

def alien(x,y):
    screen.blit(alienImg, (x,y))

#game loop
running = True
while running:
    #changing the display color
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:  #checks if any key was pressed
            if event.key == pygame.K_LEFT:  #checks if the key pressed was the left arrow key
                player_dx = -0.3
            if event.key == pygame.K_RIGHT:  #checks if the key pressed was the right arrow key
                player_dx = 0.3

        if event.type == pygame.KEYUP:  #checks if key was just released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_dx = 0

    playerX += player_dx
    #setting boundaries for the player
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    player(playerX, playerY)

    alienX += alien_dx
    if alienX <= 0:
        alien_dx = 0.3
        alienY += alien_dy
    elif alienX >= 736:
        alien_dx = -0.3
        alienY += alien_dy
    alien(alienX, alienY)
    pygame.display.update() #mandatory line - updates the display continuously

