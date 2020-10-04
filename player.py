import pygame

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
dx = 0

def player(x,y):
    screen.blit(playerImg, (x,y))

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
                dx = -0.1
            if event.key == pygame.K_RIGHT:  #checks if the key pressed was the right arrow key
                dx = 0.1

        if event.type == pygame.KEYUP:  #checks if key was just released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                dx = 0

    #setting boundaries for the player
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    playerX += dx
    player(playerX, playerY)
    pygame.display.update() #mandatory line - updates the display continuously

