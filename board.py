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
MAX_PLAYER_PIECES = 21

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
                    selected.get_tiles()[row][col].x = self.tiles[board_x+col][board_y].x
                    selected.get_tiles()[row][col].y = self.tiles[board_x][board_y+row].y
                    selected.get_tiles()[row][col].board_x = board_x+col
                    selected.get_tiles()[row][col].board_y = board_y+row
                    self.tiles[board_x+col][board_y+row] = selected.get_tiles()[row][col]


    '''
    This function will implement the following rules:
    1) The first tile played by each player must be placed in one of the four corners
    2) After the first play, pieces must be placed so at least one of the corners touches another of the same color and there is no edge-to-edge contact
    3) Edge-to-edge contact is allowed between pieces of different colors
    4) Pieces cannot overlap
    '''
    '''
    def is_valid(self, player_pieces, selected, board_x, board_y):
        valid = False
        for i in range(len(selected.get_tiles())):
            for j in range(len(selected.get_tiles()[i])):
                if(selected.get_tiles()[i][j] is not None):
                    #first piece placed
                    if(len(player_pieces) == MAX_PLAYER_PIECES):
                        check_x = board_x+j
                        check_y = board_y+i
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
                        check_x = board_x+1+j
                        check_y = board_y+1+i
                        #check that nothing is out of bounds
                        if check_x < 0 or check_y < 0 or check_x > 21 or check_y > 21:
                            return False
                        #check that it doesn't overlap with anything
                        if check_tiles[check_x][check_y].get_color() != Color.EMPTY_GREY or check_tiles[check_x][check_y].get_color() != Color.GREY_VALID:
                            return False
                        #check that it does not touch a piece of same color edgewise
                        if selected.get_color() == check_tiles[check_x-1][check_y].get_color() or selected.get_color() == check_tiles[check_x+1][check_y].get_color() or selected.get_color() == check_tiles[check_x][check_y-1].get_color() or selected.get_color() == check_tiles[check_x][check_y+1].get_color():
                            return False
                        #check that it does touch piece of same color diagonally
                        if selected.get_color() == check_tiles[check_x-1][check_y-1].get_color() or selected.get_color() == check_tiles[check_x+1][check_y-1].get_color() or selected.get_color() == check_tiles[check_x-1][check_y+1].get_color() or selected.get_color() == check_tiles[check_x+1][check_y+1].get_color():
                            valid = True
        return valid
        '''

    def is_valid_tile(self, player_pieces, selected, tile_x, tile_y):
        #need to highlight top/leftmost point they can place relative to four corners
        #for top left: always 0,0
        #for top right: x = 19-last_col, y = 0
        #for bottom left: x = 0, y = 19-last_row
        #for bottom right: x = 19-last_col, y = 19,last_row
        valid = False;
        last_col = selected.get_last_col()
        last_row = selected.get_last_row()
        if len(player_pieces) == MAX_PLAYER_PIECES:
            if tile_x == 0:
                if tile_y == 0:
                    if selected.get_tiles()[0][0] is not None and (self.tiles[0][0].get_color() == Color.EMPTY_GREY or self.tiles[0][0].get_color() == Color.GREY_VALID):
                        valid = True
                if tile_y == 19-last_row:
                    if selected.get_tiles()[0][last_row] is not None and (self.tiles[0][19].get_color() == Color.EMPTY_GREY or self.tiles[0][19].get_color() == Color.GREY_VALID):
                        valid = True
            elif tile_x == 19-last_col:
                if tile_y == 0:
                    if selected.get_tiles()[0][last_col] is not None and (self.tiles[19][0].get_color() == Color.EMPTY_GREY or self.tiles[19][0].get_color() == Color.GREY_VALID):
                        valid = True
                if tile_y == 19-last_row:
                    if selected.get_tiles()[last_row][last_col] is not None and (self.tiles[19][19].get_color() == Color.EMPTY_GREY or self.tiles[19][19].get_color() == Color.GREY_VALID):
                        valid = True
        else:
            for piece_row in range(len(selected.get_tiles())):
                for piece_col in range(len(selected.get_tiles()[piece_row])):
                    if(selected.get_tiles()[piece_row][piece_col] is not None):
                    #create new array with extra rows and columns to prevent array out of bounds errors
                        check_tiles = [[Tile(0,0,Color.EMPTY_GREY)]*(NUM_COLS+2) for _ in range(NUM_ROWS+2)]
                        for row in range(1,NUM_ROWS+1):
                            for col in range(1, NUM_COLS+1):
                                check_tiles[row][col] = self.tiles[row-1][col-1]
                        check_x = tile_x+1+piece_col
                        check_y = tile_y+1+piece_row
                        #check that nothing is out of bounds
                        if check_x <= 0 or check_y <= 0 or check_x >= 21 or check_y >= 21:
                            return False
                        #check that it doesn't overlap with anything
                        if check_tiles[check_x][check_y].get_color() != Color.EMPTY_GREY and check_tiles[check_x][check_y].get_color() != Color.GREY_VALID:
                            return False
                        #check that it does not touch a piece of same color edgewise
                        if selected.get_color() == check_tiles[check_x-1][check_y].get_color() or selected.get_color() == check_tiles[check_x+1][check_y].get_color() or selected.get_color() == check_tiles[check_x][check_y-1].get_color() or selected.get_color() == check_tiles[check_x][check_y+1].get_color():
                            return False
                            #check that it does touch piece of same color diagonally
                        if selected.get_color() == check_tiles[check_x-1][check_y-1].get_color() or selected.get_color() == check_tiles[check_x+1][check_y-1].get_color() or selected.get_color() == check_tiles[check_x-1][check_y+1].get_color() or selected.get_color() == check_tiles[check_x+1][check_y+1].get_color():
                            valid = True   
        if not valid:
            self.tiles[tile_x][tile_y].deselect()
        return valid

        


def create_set(start_x, start_y, set_color):
    """
    creates a set of pieces for player using a start x and y, and a color
    each set has one piece with each shape
    """
    MAX_PIECE_WIDTH = 150
    THREE_TILE_WIDTH = 90
    FOUR_TILE_WIDTH = 120
    GAP = 10
    MAX_PIECE_DISTANCE = MAX_PIECE_WIDTH + GAP

    # get the x values for each column
    first_col_val = start_x
    second_col_val = first_col_val + MAX_PIECE_WIDTH
    third_col_val = second_col_val + MAX_PIECE_WIDTH
    fourth_col_val = third_col_val + MAX_PIECE_WIDTH

    # get the y values for each row
    first_row_val = start_y
    second_row_val = first_row_val + THREE_TILE_WIDTH + GAP
    third_row_val = second_row_val + FOUR_TILE_WIDTH + GAP
    fourth_row_val = third_row_val + FOUR_TILE_WIDTH + GAP
    fifth_row_val = fourth_row_val + FOUR_TILE_WIDTH + GAP
    sixth_row_val = fifth_row_val + MAX_PIECE_WIDTH

    set_of_pieces = list()

    # first row
    set_of_pieces.append(Piece(Shape.ONE, first_col_val, first_row_val, set_color))
    set_of_pieces.append(Piece(Shape.TWO, second_col_val, first_row_val, set_color))
    set_of_pieces.append(Piece(Shape.V3, third_col_val, first_row_val, set_color))
    set_of_pieces.append(Piece(Shape.I3, fourth_col_val, first_row_val, set_color))
    # second row
    set_of_pieces.append(Piece(Shape.T4, first_col_val, second_row_val, set_color))
    set_of_pieces.append(Piece(Shape.O, second_col_val, second_row_val, set_color))
    set_of_pieces.append(Piece(Shape.L4, third_col_val, second_row_val, set_color))
    set_of_pieces.append(Piece(Shape.I4, fourth_col_val, second_row_val, set_color))
    # third row
    set_of_pieces.append(Piece(Shape.Z4, first_col_val, third_row_val, set_color))
    set_of_pieces.append(Piece(Shape.F, second_col_val, third_row_val, set_color))
    set_of_pieces.append(Piece(Shape.X, third_col_val, third_row_val, set_color))
    set_of_pieces.append(Piece(Shape.P, fourth_col_val, third_row_val, set_color))
    # fourth row
    set_of_pieces.append(Piece(Shape.W, first_col_val, fourth_row_val, set_color))
    set_of_pieces.append(Piece(Shape.Z5, second_col_val, fourth_row_val, set_color))
    set_of_pieces.append(Piece(Shape.Y, third_col_val, fourth_row_val, set_color))
    set_of_pieces.append(Piece(Shape.L5, fourth_col_val, fourth_row_val, set_color))
    # fifth row
    set_of_pieces.append(Piece(Shape.U, first_col_val, fifth_row_val, set_color))
    set_of_pieces.append(Piece(Shape.T5, second_col_val, fifth_row_val, set_color))
    set_of_pieces.append(Piece(Shape.V5, third_col_val, fifth_row_val, set_color))
    set_of_pieces.append(Piece(Shape.N, fourth_col_val, fifth_row_val, set_color))
    # sixth row
    set_of_pieces.append(Piece(Shape.I5, first_col_val, sixth_row_val, set_color))
    return set_of_pieces
