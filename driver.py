import pygame
import pygame.locals
from board import Board
from piece import Piece
from piece import Shape
from tile import Color
from tile import Tile


BOARD_WIDTH, BOARD_HEIGHT = 1200, 1000


if __name__ == '__main__':
    pygame.init()
    window = (BOARD_WIDTH,BOARD_HEIGHT)
    screen = pygame.display.set_mode(window)
    screen.fill(Color.BG_GREY.value)

    # Create and draw a board, then put it on the screen
    board = Board(window)
    # TESTING - REMOVE AFTER
    testpiece = Piece(Shape.Z4, Tile(10,10,Color.BLUE))
    board.add_piece(testpiece)
    board.draw()
    screen.blit(board.get_surface(), (BOARD_WIDTH//2-board.get_surface().get_width()//2,
                                      BOARD_HEIGHT//2-board.get_surface().get_height()//2))

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

# echos thread
