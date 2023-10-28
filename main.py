#Imports
import pygame
from pygame.locals import (KEYDOWN, K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_UP)

# Initialize pygame lib
pygame.init()
screen = pygame.display.set_mode([1920, 1080])


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #white background
    screen.fill([255, 255, 255])
    pygame.display.flip()

pygame.quit()

