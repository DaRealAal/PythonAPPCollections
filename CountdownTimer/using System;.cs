import pygame
from pygame.locals import *

pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Plateformer')

run = True
while run:
    
    for event in pygame.event.get():
        if event.type ** pygame.
