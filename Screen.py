import pygame
from Form import Quadrat



class Screen():
    screen = pygame.display.set_mode((800, 1000))
    pygame.display.set_caption('Shitris')
    x= 400
    y= 400
    width = 60
    height = 60
    vel = 5

    running = True

    while running:
        pygame.time.delay(100)
        Quadrat()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))

        pygame.display.flip()





    pygame.quit()



