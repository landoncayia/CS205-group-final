import pygame
from tile import Color
from piece import Piece
from tile import Tile
from piece import Shape

COL_LETTERS = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K',
                       11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T'}
TILE_WIDTH = 30

class Board:
    # init function
    # window is the game window
    # surface is the game surface object
    # tiles is a 2-D list (20 x 20) of tile objects
    def __init__(self, window):
        self.surface = pygame.Surface((750, 750))
        self.tiles = [[None]*20 for _ in range(20)]  # initialize board 2-D list
        for x in range(20):
            for y in range(20):
                # x and y are the board locations; so convert the first parameters to pixel values for the surface
                self.tiles[x][y] = Tile(40+(35*x), 40+(35*y), Color.EMPTY_GREY, x, y)

    def draw_labels(self):
        font = pygame.font.SysFont('Ubuntu', 18, bold=True)
        # Draw letters along the top of the board (above each column)
        for col in range(20):
            text = font.render(COL_LETTERS[col], True, Color.EMPTY_GREY.value)
            self.surface.blit(text, (50+(35*col), 5))
        # Draw numbers along the side of the board, left of each row
        # row + 1 will be the row number
        # change position slightly for vertical alignment of numbers
        for row in range(9):
            text = font.render(str(row+1), True, Color.EMPTY_GREY.value)
            self.surface.blit(text, (15, 45+(35*row)))
        for row in range(9, 20):
            text = font.render(str(row+1), True, Color.EMPTY_GREY.value)
            self.surface.blit(text, (10, 45+(35*row)))

    # draw() will draw the surface in the game window
    def draw(self):
        # Need .value for an enum to get the actual tuple, not the enum object
        self.surface.fill(Color.BG_GREY.value)
        pygame.draw.rect(self.surface, Color.EMPTY_GREY.value, (35, 35, 705, 705), 3)
        for row in range(20):
            for col in range(20):
                self.tiles[row][col].draw_tile(self.surface)
        self.draw_labels()

    # Getters
    def get_surface(self):
        return self.surface

    def get_tiles(self):
        return self.tiles

    # Setters
    def set_tiles(self, tiles):
        self.tiles = tiles

    '''
    add_piece(): adds a piece to the tiles
    origin: tuple(int, int) - contains the origin [0-19] of the placed piece; e.g., (1, 1)
    tiles: list(Tile) - contains the tiles that make up a piece
        NOTE: the first value in tiles should be (0, 0); e.g., [(0, 0), (1, 0), (2, 0), (0, 1), (-1, 1)] will make this shape:
          ■ ■ ■
        ■ ■
    '''
    def add_piece(self, selected, x, y):
        for tile in selected.get_tiles():
            # Piece needs a change; currently, there are no coordinates relative to the origin, so drawing a piece won't work.
            pass


# creates a set of pieces for player using a start x and y, and a color
# each set has one piece with each shape
def create_set(start_x, start_y, set_color):
    # set the distance each piece will be apart from each other
    MAX_PIECE_WIDTH = 150
    GAP = 10
    MAX_PIECE_DISTANCE = MAX_PIECE_WIDTH + GAP

    # get the x values for each column
    first_col_val = start_x
    second_col_val = first_col_val + MAX_PIECE_DISTANCE
    third_col_val = second_col_val + MAX_PIECE_DISTANCE

    # get the y values for each row
    first_row_val = start_y
    second_row_val = first_row_val + MAX_PIECE_DISTANCE
    third_row_val = second_row_val + MAX_PIECE_DISTANCE
    fourth_row_val = third_row_val + MAX_PIECE_DISTANCE

    set_of_pieces = list()

    # first row
    set_of_pieces.append(Piece(Shape.ONE, first_col_val, first_row_val, set_color))
    set_of_pieces.append(Piece(Shape.TWO, second_col_val, first_row_val, set_color))
    set_of_pieces.append(Piece(Shape.V3, third_col_val, first_row_val, set_color))
    # second row
    set_of_pieces.append(Piece(Shape.I3, first_col_val, second_row_val, set_color))
    set_of_pieces.append(Piece(Shape.T4, second_col_val, second_row_val, set_color))
    set_of_pieces.append(Piece(Shape.O, third_col_val, second_row_val, set_color))
    # third row
    set_of_pieces.append(Piece(Shape.L4, first_col_val, third_row_val, set_color))
    set_of_pieces.append(Piece(Shape.I4, second_col_val, third_row_val, set_color))
    set_of_pieces.append(Piece(Shape.Z4, third_col_val, third_row_val, set_color))
    # fourth row
    set_of_pieces.append(Piece(Shape.F, first_col_val, fourth_row_val, set_color))
    set_of_pieces.append(Piece(Shape.X, second_col_val, fourth_row_val, set_color))
    set_of_pieces.append(Piece(Shape.P, third_col_val, fourth_row_val, set_color))

    # tiles for second page
    # back to first row
    set_of_pieces.append(Piece(Shape.W, first_col_val, first_row_val, set_color))
    set_of_pieces.append(Piece(Shape.Z5, second_col_val, first_row_val, set_color))
    set_of_pieces.append(Piece(Shape.Y, third_col_val, first_row_val, set_color))
    # second row
    set_of_pieces.append(Piece(Shape.L5, first_col_val, second_row_val, set_color))
    set_of_pieces.append(Piece(Shape.U, second_col_val, second_row_val, set_color))
    set_of_pieces.append(Piece(Shape.T5, third_row_val, second_row_val, set_color))
    # third row
    set_of_pieces.append(Piece(Shape.V5, first_col_val, third_row_val, set_color))
    set_of_pieces.append(Piece(Shape.N, second_col_val, third_row_val, set_color))
    set_of_pieces.append(Piece(Shape.I5, third_col_val, third_row_val, set_color))
    return set_of_pieces
