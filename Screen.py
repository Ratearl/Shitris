import pygame
from Form import Quadrat

class Screen():
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Shitris')

    running = True

    while running:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        Quadrat()

        pygame.display.flip()

    pygame.quit()

