import pygame
import pygame.locals

if __name__ == '__main__':
    pygame.init()
    window = (800, 800)
    screen = pygame.display.set_mode(window)
    screen.fill((255, 255, 255))

    background = pygame.Surface(window)
    background.fill((50, 50, 50))

    for row in range(20):
        for col in range(20):
            pygame.draw.rect(background, (172, 175, 181), (40+col+(35*col), 40+row+(35*row), 30, 30))

    screen.blit(background, (0, 0))

    # background = background.convert()

    pygame.display.flip()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # Exit game with escape key
                if event.key == pygame.locals.K_ESCAPE:
                    done = True
            if event.type == pygame.QUIT:
                done = True

    pygame.quit()
