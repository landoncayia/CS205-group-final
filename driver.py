import pygame
import pygame.locals
from board import Board


if __name__ == '__main__':
    pygame.init()
    window = (800, 800)
    screen = pygame.display.set_mode(window)
    screen.fill((255, 255, 255))

    # Create and draw a board, then put it on the screen
    board = Board(window)
    board.draw()
    screen.blit(board.board, (0, 0))

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
