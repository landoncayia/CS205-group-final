import pygame
import pygame.locals
from board import Board
from piece import Piece
from piece import Shape
from tile import Color
from tile import Tile


def create_set(set_color):
    i = 1
    piece_list = []
    tile_x_start = 900
    tile_y_start = 50
    while (i < 22):
        piece_list.append(Piece(Shape(i), Tile(tile_x_start, tile_y_start, set_color)))
    return piece_list

if __name__ == '__main__':
    pygame.init()
    window = (1200, 800)
    screen = pygame.display.set_mode(window)
    screen.fill((255, 255, 255))

    # Create and draw a board, then put it on the screen
    board = Board(window)
    # TESTING - REMOVE AFTER
    testpiece = Piece(Shape.Z4, Tile(10, 10, 'blue'))
    board.add_piece(testpiece)
    board.draw()
    screen.blit(board.get_surface(), (0, 0))

    # DISPLAY PIECES
    full_set = create_set(Color.BLUE)
    i = 0

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
