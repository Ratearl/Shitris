import pygame
from Form import Quadrat


def Screen():
    screen = pygame.display.set_mode((800, 1000))
    pygame.display.set_caption('Shitris')

    running = True

    Quadrat(screen)
    while running:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()

Screen()

