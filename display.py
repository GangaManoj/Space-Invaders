#step one
#created display with custom title and icon

import pygame

#initialise pygame
pygame.init()

#creating the screen
screen = pygame.display.set_mode((800, 500))

#setting the title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #changing the display color
    screen.fill((0,0,0))
    #mandatory line - updates the display continuously
    pygame.display.update() 
