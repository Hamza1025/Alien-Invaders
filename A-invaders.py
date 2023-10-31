import pygame
#import math
#import random
#import sys
from pygame import mixer

# Intialize the pygame
pygame.init()

# pygame.mixer.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# name of the applcation game and icon

pygame.display.set_caption("Alien Invaders")
icon = pygame.image.load("Alien-Invaders/Images/icon.png")
pygame.display.set_icon(icon)

#Background image and sound


background = pygame.image.load("Alien-Invaders/Images/backg.png")
mixer.music.load("Alien-Invaders/sounds/background.mp3")
mixer.music.play(-1)



#Game loop
running = True
while running:
    
    screen.fill((0, 0, 0))
    #screen open
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
pygame.display.update()

# me Hamza has added on code under this comment for the main game


