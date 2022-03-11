import pygame

class Quadrat():

    screen = pygame.display.set_mode((800, 800))

    x= 400
    y= 400
    width = 60
    height = 60
    vel = 5

    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))