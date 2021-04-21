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
    selected: the currently selected piece, to be added
    board_x, board_y: clicked board location for piece to get added
        NOTE: the first value in tiles should be (0, 0); e.g., [(0, 0), (1, 0), (2, 0), (0, 1), (-1, 1)] will make this shape:
          ■ ■ ■
        ■ ■
    '''
    def add_piece(self, selected, board_x, board_y):
        for row in range(len(selected.get_tiles())):  # Should be 5
            for col in range(len(selected.get_tiles()[0])):  # Should be 5
                if selected.get_tiles()[row][col] is not None:
                    selected.get_tiles()[row][col].x = self.tiles[board_x][board_y].x
                    selected.get_tiles()[row][col].y = self.tiles[board_x][board_y].y
                    self.tiles[board_x][board_y] = selected.get_tiles()[row][col]


"""
Clears out any already-placed pieces from the set of selectable ones
"""
def clear_set(pieces_surface):
    pygame.draw.rect(pieces_surface, Color.BG_GREY.value, (0, 0, 400, 800))



# creates a set of pieces for player using a start x and y, and a color
# each set has one piece with each shape
def create_set(start_x, start_y, set_color):
    MAX_PIECE_WIDTH = 150
    GAP = 10
    set_of_pieces = list()
    set_of_pieces.append(Piece(Shape.ONE, start_x, start_y, set_color))
    set_of_pieces.append(Piece(Shape.TWO, start_x + MAX_PIECE_WIDTH, start_y, set_color))
    # set_of_pieces.append(Piece(Shape.V3, Tile(start_x + 210, start_y, set_color)))
    # set_of_pieces.append(Piece(Shape.I3, Tile(start_x, start_y + 90, set_color)))
    # set_of_pieces.append(Piece(Shape.T4, Tile(start_x + 150, start_y + 90, set_color)))
    # set_of_pieces.append(Piece(Shape.O, Tile(start_x, start_y + 180, set_color)))
    # set_of_pieces.append(Piece(Shape.L4, Tile(start_x + 120, start_y + 180, set_color)))
    # set_of_pieces.append(Piece(Shape.I4, Tile(start_x, start_y + 270, set_color)))
    # set_of_pieces.append(Piece(Shape.Z4, Tile(start_x + 180, start_y + 270, set_color)))
    # set_of_pieces.append(Piece(Shape.F, Tile(start_x + 30, start_y + 330, set_color)))
    # set_of_pieces.append(Piece(Shape.X, Tile(start_x + 300, start_y + 60, set_color)))
    # set_of_pieces.append(Piece(Shape.P, Tile(start_x + 300, start_y + 330, set_color)))
    # set_of_pieces.append(Piece(Shape.W, Tile(start_x + 270, start_y + 180, set_color)))
    # set_of_pieces.append(Piece(Shape.Z5, Tile(start_x + 120, start_y + 360, set_color)))
    # set_of_pieces.append(Piece(Shape.Y, Tile(start_x, start_y + 450, set_color)))
    # set_of_pieces.append(Piece(Shape.L5, Tile(start_x + 240, start_y + 450, set_color)))
    # set_of_pieces.append(Piece(Shape.U, Tile(start_x + 120, start_y + 510, set_color)))
    # set_of_pieces.append(Piece(Shape.T5, Tile(start_x + 30, start_y + 540, set_color)))
    # set_of_pieces.append(Piece(Shape.V5, Tile(start_x + 270, start_y + 540, set_color)))
    # set_of_pieces.append(Piece(Shape.N, Tile(start_x + 30, start_y + 660, set_color)))
    # set_of_pieces.append(Piece(Shape.I5, Tile(start_x + 180, start_y + 660, set_color)))
    return set_of_pieces
