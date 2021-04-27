import pygame
from tile import Color
from piece import Piece
from tile import Tile
from piece import Shape

COL_LETTERS = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K',
               11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T'}
TILE_WIDTH = 30


class Board:
    def __init__(self):
        """
        init function
        window is the game window
        surface is the game surface object
        tiles is a 2-D list (20 x 20) of tile objects
        """
        self.surface = pygame.Surface((750, 750))
        self.tiles = [[None]*20 for _ in range(20)]  # initialize board 2-D list
        for x in range(20):
            for y in range(20):
                # x and y are the board locations; so convert the first parameters to pixel values for the surface
                self.tiles[x][y] = Tile(40+(35*x), 40+(35*y), Color.EMPTY_GREY, x, y)

    def draw_labels(self):
        """
        This function draws the letter and number labels along the axes of the board
        """
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

    def draw(self):
        # draw() will draw the surface in the game window
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

    def get_score(self):
        blue_count = 0
        red_count = 0
        green_count = 0
        yellow_count = 0
        for x in range(20):
            for y in range(20):
                current_tile = self.tiles[x][y]
                if current_tile.get_color() == Color.BLUE:
                    blue_count += 1
                elif current_tile.get_color() == Color.RED:
                    red_count += 1
                elif current_tile.get_color() == Color.GREEN:
                    green_count += 1
                elif current_tile.get_color() == Color.YELLOW:
                    yellow_count += 1
        # may want to get rid of 4 - tuple in future
        return blue_count, yellow_count, red_count, green_count

    # Setters
    def set_tiles(self, tiles):
        self.tiles = tiles

    def add_piece(self, selected, board_x, board_y):
        """
        add_piece(): adds a piece to the tiles
        selected: the currently selected piece, to be added
        board_x, board_y: clicked board location for piece to get added
            NOTE: the first value in tiles should be (0, 0); e.g., [(0, 0), (1, 0), (2, 0), (0, 1), (-1, 1)] will make
            this shape:
              ■ ■ ■
            ■ ■
        """
        for row in range(len(selected.get_tiles())):  # Should be 5
            for col in range(len(selected.get_tiles()[0])):  # Should be 5
                if selected.get_tiles()[row][col] is not None:
                    selected.get_tiles()[row][col].x = self.tiles[board_x+row][board_y+row].x
                    selected.get_tiles()[row][col].y = self.tiles[board_x][board_y].y
                    selected.get_tiles()[row][col].board_x = board_x+row
                    selected.get_tiles()[row][col].board_y = board_y+col
                    self.tiles[board_x+row][board_y+col] = selected.get_tiles()[row][col]


def create_set(start_x, start_y, set_color):
    """
    creates a set of pieces for player using a start x and y, and a color
    each set has one piece with each shape
    """
    max_piece_width = 150
    gap = 10
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
