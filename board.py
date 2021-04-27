import pygame
from tile import Color
from piece import Piece
from tile import Tile
from piece import Shape

COL_LETTERS = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K',
               11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T'}
TILE_WIDTH = 30
NUM_ROWS = 20
NUM_COLS = 20
#TODO: update when more pieces are available from create_set
MAX_PLAYER_PIECES = 2

class Board:
    def __init__(self):
        """
        init function
        window is the game window
        surface is the game surface object
        tiles is a 2-D list (20 x 20) of tile objects
        """
        self.surface = pygame.Surface((750, 750))
        self.tiles = [[None]*NUM_COLS for _ in range(NUM_ROWS)]  # initialize board 2-D list
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
                    selected.get_tiles()[row][col].x = self.tiles[board_x+row][board_y].x
                    selected.get_tiles()[row][col].y = self.tiles[board_x][board_y+col].y
                    selected.get_tiles()[row][col].board_x = board_x+row
                    selected.get_tiles()[row][col].board_y = board_y+col
                    self.tiles[board_x+row][board_y+col] = selected.get_tiles()[row][col]


    '''
    This function will implement the following rules:
    1) The first tile played by each player must be placed in one of the four corners
    2) After the first play, pieces must be placed so at least one of the corners touches another of the same color and there is no edge-to-edge contact
    3) Edge-to-edge contact is allowed between pieces of different colors
    4) Pieces cannot overlap
    '''
    def is_valid(self, player_pieces, selected, board_x, board_y):
        valid = False
        for i in range(len(selected.get_tiles())):
            for j in range(len(selected.get_tiles()[i])):
                if(selected.get_tiles()[i][j] is not None):
                    #first piece placed
                    if(len(player_pieces) == MAX_PLAYER_PIECES):
                        check_x = board_x+i
                        check_y = board_y+j
                        #check that nothing is out of bounds
                        if check_x < 0 or check_y < 0 or check_x > 19 or check_y > 19:
                            return False
                        #check each corner
                        if check_x == 0:
                            if check_y == 0:
                                valid = True
                            elif check_y == 19:
                                valid = True
                        elif check_x == 19:
                            if check_y == 0:
                                valid = True
                            elif check_y == 19:
                                valid = True
                    #all pieces afterward
                    else:
                        #create new array with extra rows and columns to prevent array out of bounds errors
                        check_tiles = [[Tile(0,0,Color.EMPTY_GREY)]*(NUM_COLS+2) for _ in range(NUM_ROWS+2)]
                        for row in range(1,NUM_ROWS+1):
                            for col in range(1, NUM_COLS+1):
                                check_tiles[row][col] = self.tiles[row-1][col-1]
                        check_x = board_x+1+i
                        check_y = board_y+1+j
                        #check that nothing is out of bounds
                        if check_x < 0 or check_y < 0 or check_x > 21 or check_y > 21:
                            return False
                        #check that it doesn't overlap with anything
                        if check_tiles[check_x][check_y].get_color() != Color.EMPTY_GREY:
                            return False
                        #check that it does not touch a piece of same color edgewise
                        if selected.get_color() == check_tiles[check_x-1][check_y].get_color() or selected.get_color() == check_tiles[check_x+1][check_y].get_color() or selected.get_color() == check_tiles[check_x][check_y-1].get_color() or selected.get_color() == check_tiles[check_x][check_y+1].get_color():
                            return False
                        #check that it does touch piece of same color diagonally
                        if selected.get_color() == check_tiles[check_x-1][check_y-1].get_color() or selected.get_color() == check_tiles[check_x+1][check_y-1].get_color() or selected.get_color() == check_tiles[check_x-1][check_y+1].get_color() or selected.get_color() == check_tiles[check_x+1][check_y+1].get_color():
                            valid = True
        return valid


def create_set(start_x, start_y, set_color):
    """
    creates a set of pieces for player using a start x and y, and a color
    each set has one piece with each shape
    """
    max_piece_width = 150
    gap = 10
    set_of_pieces = list()
    set_of_pieces.append(Piece(Shape.ONE, start_x, start_y, set_color))
    set_of_pieces.append(Piece(Shape.TWO, start_x + max_piece_width, start_y, set_color))
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
