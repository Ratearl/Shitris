import pygame

class MObject():
    pygame.init()

    screen = pygame.display.set_mode((700, 1000))
    pygame.display.set_caption("Shitris")

    x = 200
    y = 200
    width = 40
    height = 40
    vel = 2.5

    run = True

    while run:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        #if keys[pygame.K_LEFT] and x>0:
         #   x -= vel
        #if keys[pygame.K_RIGHT] and x<700-width:
         #   x += vel
        #if keys[pygame.K_UP] and y>0:
         #   y -= vel
        if keys[pygame.K_DOWN] and y<1000-height:
            y += vel

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
        pygame.display.update()

    pygame.quit()