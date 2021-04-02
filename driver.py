import pygame
import pygame.locals
from board import Board
from piece import Piece
from piece import Shape
from piece import create_set
from tile import Color
from tile import Tile

BOARD_WIDTH, BOARD_HEIGHT = 800, 800


if __name__ == '__main__':
    pygame.init()
    window = (1200, 800)
    screen = pygame.display.set_mode(window)
    screen.fill(Color.BG_GREY.value)
    piecesSurface = pygame.Surface((200, 200))

    # Create and draw a board, then put it on the screen
    board = Board(window)
    # TESTING - REMOVE AFTER
    testpiece = Piece(Shape.Z4, Tile(10,10,Color.BLUE))
    board.add_piece(testpiece)
    board.draw()
    screen.blit(board.get_surface(), (BOARD_WIDTH//2-board.get_surface().get_width()//2,
                                      BOARD_HEIGHT//2-board.get_surface().get_height()//2))

    # DISPLAY PIECES
    piecesSurface.fill(Color.BG_GREY.value)
    testpiece.draw_piece(piecesSurface)
    screen.blit(piecesSurface, (800, 200))
    # full_set = create_set(Color.BLUE, 900, 50)

    # testpiece.draw(piecesSurface)
    # while (i < (len(full_set) / 2)):
    #     full_set[i].draw(piecesSurface)

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
