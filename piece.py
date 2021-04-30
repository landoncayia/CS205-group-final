from tile import Tile
from enum import IntEnum
from tile import Color
import numpy as np

# contains all possible pieces
class Shape(IntEnum):
    ONE = 1
    TWO = 2
    V3 = 3
    I3 = 4
    T4 = 5
    O = 6
    L4 = 7
    I4 = 8
    Z4 = 9
    F = 10
    X = 11
    P = 12
    W = 13
    Z5 = 14
    Y = 15
    L5 = 16
    U = 17
    T5 = 18
    V5 = 19
    N = 20
    I5 = 21


MAX_TILES_WIDTH = 5
TILE_WIDTH = 30

'''
A Piece is a list of tiles with a center tile and various connected tiles
The IntEnum Shape determines what kind of piece it is
'''
class Piece:
    def __init__(self, shape, x, y, color):
        self.shape = shape
        self.x = x
        self.y = y
        self.color = color
        # self.table_tiles = list()  # tiles used on board - incremented by 1
        # self.printing_tiles = list()  # tiles used to display on side - incremented by 30
        self.tiles_array = [[None] * MAX_TILES_WIDTH for _ in range(MAX_TILES_WIDTH)] # tiles will be added here
        # self.center = center
        self.set_tiles()
        self.selected = False

    def get_shape(self):
        return self.shape

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color
        for row in self.tiles_array:
            for tile in row:
                if tile is not None:
                    tile.set_color(color)

    def set_shape(self, shape):
        self.shape = shape

    def get_tiles(self):
        return self.tiles_array

    def select(self):
        self.selected = True
        for row in self.tiles_array:
            for tile in row:
                if tile is not None:
                    if tile.get_color() == Color.BLUE:
                        tile.set_color(Color.BLUE_SELECTED)
                    elif tile.get_color() == Color.YELLOW:
                        tile.set_color(Color.YELLOW_SELECTED)
                    elif tile.get_color() == Color.RED:
                        tile.set_color(Color.RED_SELECTED)
                    elif tile.get_color() == Color.GREEN:
                        tile.set_color(Color.GREEN_SELECTED)

    def deselect(self):
        self.selected = False
        for row in self.tiles_array:
            for tile in row:
                if tile is not None:
                    if tile.get_color() == Color.BLUE_SELECTED:
                        tile.set_color(Color.BLUE)
                    elif tile.get_color() == Color.YELLOW_SELECTED:
                        tile.set_color(Color.YELLOW)
                    elif tile.get_color() == Color.RED_SELECTED:
                        tile.set_color(Color.RED)
                    elif tile.get_color() == Color.GREEN_SELECTED:
                        tile.set_color(Color.GREEN)

    def is_selected(self):
        return self.selected

    '''
    Each piece is represented by an array of tiles, which are relative to the first entry in the array.
    The first entry is the top/left-most tile of the piece.
    Pieces are added in reading order.
    '''
    def set_tiles(self):
        if self.shape == Shape.ONE:
            self.set_shape_ONE()
        # 2 tiles
        elif self.shape == Shape.TWO:
            self.set_shape_TWO()

        # 3 tiles
        elif self.shape == Shape.V3:
            self.set_shape_V3()

        elif self.shape == Shape.I3:
            self.set_shape_I3()

        # 4 tiles
        elif self.shape == Shape.T4:
            self.set_shape_T4()

        elif self.shape == Shape.O:
            self.set_shape_O()

        elif self.shape == Shape.L4:
            self.set_shape_L4()

        elif self.shape == Shape.I4:
            self.set_shape_I4()

        elif self.shape == Shape.Z4:
            self.set_shape_Z4()

        # 5 tiles
        elif self.shape == Shape.F:
            self.set_shape_F()

        elif self.shape == Shape.X:
            self.set_shape_X()

        elif self.shape == Shape.P:
            self.set_shape_P()

        elif self.shape == Shape.W:
            self.set_shape_W()


        elif self.shape == Shape.Z5:
            self.set_shape_Z5()

        elif self.shape == Shape.Y:
            self.set_shape_Y()

        elif self.shape == Shape.L5:
            self.set_shape_L5()

        elif self.shape == Shape.U:
            self.set_shape_U()

        elif self.shape == Shape.T5:
            self.set_shape_T5()

        elif self.shape == Shape.V5:
            self.set_shape_V5()

        elif self.shape == Shape.N:
            self.set_shape_N()

        elif self.shape == Shape.I5:
            self.set_shape_I5()

    def set_shape_ONE(self):
        self.tiles_array[0][0] = Tile(self.x, self.y, self.color)

    def set_shape_TWO(self):
        self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
        self.tiles_array[0][1] = Tile(self.x + TILE_WIDTH, self.y, self.color)

    def set_shape_V3(self):
        self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
        self.tiles_array[0][1] = Tile(self.x + TILE_WIDTH, self.y, self.color)
        self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)

    def set_shape_I3(self):
        self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
        self.tiles_array[0][1] = Tile(self.x + TILE_WIDTH, self.y, self.color)
        self.tiles_array[0][2] = Tile(self.x + (2 * TILE_WIDTH), self.y, self.color)

    def set_shape_T4(self):
        self.tiles_array[0][1] = Tile(self.x + TILE_WIDTH, self.y, self.color)
        self.tiles_array[1][0] = Tile(self.x, self.y + TILE_WIDTH, self.color)
        self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)
        self.tiles_array[1][2] = Tile(self.x + (2 * TILE_WIDTH), self.y + TILE_WIDTH, self.color)

    def set_shape_O(self):
        self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
        self.tiles_array[0][1] = Tile(self.x + TILE_WIDTH, self.y, self.color)
        self.tiles_array[1][0] = Tile(self.x, self.y + TILE_WIDTH, self.color)
        self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)

    def set_shape_L4(self):
        self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
        self.tiles_array[1][0] = Tile(self.x, self.y + TILE_WIDTH, self.color)
        self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)
        self.tiles_array[1][2] = Tile(self.x + (2 * TILE_WIDTH), self.y + TILE_WIDTH, self.color)

    def set_shape_I4(self):
        self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
        self.tiles_array[0][1] = Tile(self.x + TILE_WIDTH, self.y, self.color)
        self.tiles_array[0][2] = Tile(self.x + (2 * TILE_WIDTH), self.y, self.color)
        self.tiles_array[0][3] = Tile(self.x + (3 * TILE_WIDTH), self.y, self.color)

    def set_shape_Z4(self):
        self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
        self.tiles_array[1][0] = Tile(self.x, self.y + TILE_WIDTH, self.color)
        self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)
        self.tiles_array[2][1] = Tile(self.x + TILE_WIDTH, self.y + (2 * TILE_WIDTH), self.color)

    def set_shape_F(self):
        self.tiles_array[1][0] = Tile(self.x, self.y + TILE_WIDTH, self.color)
        self.tiles_array[2][0] = Tile(self.x, self.y + (2 * TILE_WIDTH), self.color)
        self.tiles_array[0][1] = Tile(self.x + TILE_WIDTH, self.y, self.color)
        self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)
        self.tiles_array[1][2] = Tile(self.x + (2 * TILE_WIDTH), self.y + TILE_WIDTH, self.color)

    def set_shape_X(self):
        self.tiles_array[1][0] = Tile(self.x, self.y + TILE_WIDTH, self.color)
        self.tiles_array[0][1] = Tile(self.x + TILE_WIDTH, self.y, self.color)
        self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)
        self.tiles_array[2][1] = Tile(self.x + TILE_WIDTH, self.y + (2 * TILE_WIDTH), self.color)
        self.tiles_array[1][2] = Tile(self.x + (2 * TILE_WIDTH), self.y + TILE_WIDTH, self.color)

    def set_shape_P(self):
        self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
        self.tiles_array[1][0] = Tile(self.x, self.y + TILE_WIDTH, self.color)
        self.tiles_array[2][0] = Tile(self.x, self.y + (2 * TILE_WIDTH), self.color)
        self.tiles_array[0][1] = Tile(self.x + TILE_WIDTH, self.y, self.color)
        self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)

    def set_shape_W(self):
        self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
        self.tiles_array[1][0] = Tile(self.x, self.y + TILE_WIDTH, self.color)
        self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)
        self.tiles_array[2][1] = Tile(self.x + TILE_WIDTH, self.y + (2 * TILE_WIDTH), self.color)
        self.tiles_array[2][2] = Tile(self.x + (2 * TILE_WIDTH), self.y + (2 * TILE_WIDTH), self.color)

    def set_shape_Z5(self):
        self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
        self.tiles_array[1][0] = Tile(self.x, self.y + TILE_WIDTH, self.color)
        self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)
        self.tiles_array[1][2] = Tile(self.x + (2 * TILE_WIDTH), self.y + TILE_WIDTH, self.color)
        self.tiles_array[2][2] = Tile(self.x + (2 * TILE_WIDTH), self.y + (2 * TILE_WIDTH), self.color)

    def set_shape_Y(self):
        self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
        self.tiles_array[0][1] = Tile(self.x + TILE_WIDTH, self.y, self.color)
        self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)
        self.tiles_array[0][2] = Tile(self.x + (2 * TILE_WIDTH), self.y, self.color)
        self.tiles_array[0][3] = Tile(self.x + (3 * TILE_WIDTH), self.y, self.color)

    def set_shape_L5(self):
        self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
        self.tiles_array[1][0] = Tile(self.x, self.y + TILE_WIDTH, self.color)
        self.tiles_array[0][1] = Tile(self.x + TILE_WIDTH, self.y, self.color)
        self.tiles_array[0][2] = Tile(self.x + (2 * TILE_WIDTH), self.y, self.color)
        self.tiles_array[0][3] = Tile(self.x + (3 * TILE_WIDTH), self.y, self.color)

    def set_shape_U(self):
        self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
        self.tiles_array[1][0] = Tile(self.x, self.y + TILE_WIDTH, self.color)
        self.tiles_array[0][1] = Tile(self.x + TILE_WIDTH, self.y, self.color)
        self.tiles_array[0][2] = Tile(self.x + (2 * TILE_WIDTH), self.y, self.color)
        self.tiles_array[1][2] = Tile(self.x + (2 * TILE_WIDTH), self.y + TILE_WIDTH, self.color)

    def set_shape_T5(self):
        self.tiles_array[2][1] = Tile(self.x, self.y + (2 * TILE_WIDTH), self.color)
        self.tiles_array[0][1] = Tile(self.x + TILE_WIDTH, self.y, self.color)
        self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)
        self.tiles_array[2][1] = Tile(self.x + TILE_WIDTH, self.y + (2 * TILE_WIDTH), self.color)
        self.tiles_array[2][2] = Tile(self.x + (2 * TILE_WIDTH), self.y + (2 * TILE_WIDTH), self.color)

    def set_shape_V5(self):
        self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
        self.tiles_array[1][0] = Tile(self.x, self.y + TILE_WIDTH, self.color)
        self.tiles_array[2][0] = Tile(self.x, self.y + (2 * TILE_WIDTH), self.color)
        self.tiles_array[2][1] = Tile(self.x + TILE_WIDTH, self.y + (2 * TILE_WIDTH), self.color)
        self.tiles_array[2][2] = Tile(self.x + (2 * TILE_WIDTH), self.y + (2 * TILE_WIDTH), self.color)

    def set_shape_N(self):
        self.tiles_array[1][0] = Tile(self.x, self.y + TILE_WIDTH, self.color)
        self.tiles_array[0][1] = Tile(self.x + TILE_WIDTH, self.y, self.color)
        self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)
        self.tiles_array[0][2] = Tile(self.x + (2 * TILE_WIDTH), self.y, self.color)
        self.tiles_array[0][3] = Tile(self.x + (3 * TILE_WIDTH), self.y, self.color)

    def set_shape_I5(self):
        self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
        self.tiles_array[0][1] = Tile(self.x + TILE_WIDTH, self.y, self.color)
        self.tiles_array[0][2] = Tile(self.x + (2 * TILE_WIDTH), self.y, self.color)
        self.tiles_array[0][3] = Tile(self.x + (3 * TILE_WIDTH), self.y, self.color)
        self.tiles_array[0][4] = Tile(self.x + (4 * TILE_WIDTH), self.y, self.color)

    def get_num_tiles(self):
        if self.shape == Shape.ONE:
            return 1
        elif self.shape == Shape.TWO:
            return 2
        elif self.shape == 3 or self.shape == 4:
            return 3
        elif self.shape >= 5 and self.shape < 10:
            return 4
        else:
            return 5

    #when a piece is rotated or flipped, the tiles move in the array but the pixel values have to change as well
    def reset_distances(self, orig_x, orig_y):
        row = 0
        col = 0
        shift_rows = self.get_first_row()
        shift_cols = self.get_first_col()
        #moves the tiles as far up and to the left as they can go
        self.tiles_array = np.roll(self.tiles_array, -shift_rows, axis=0).tolist()
        self.tiles_array = np.roll(self.tiles_array, -shift_cols, axis=1).tolist()
        # orig_x = self.get_first_tile().get_location()[0]-30*self.get_first_row()
        # orig_y = self.get_first_tile().get_location()[1]-30*self.get_first_col()
        #all pixel values are relative to first tile in the array
        while (row < MAX_TILES_WIDTH):
            while (col < MAX_TILES_WIDTH):
                if (self.tiles_array[row][col] != None):
                    new_x = orig_x + 30*col
                    new_y = orig_y + 30*row
                    self.tiles_array[row][col].set_location(new_x,new_y)
                col += 1
            row += 1
            col = 0

    #draws each tile in the piece
    def draw_piece(self, surface):
        row = 0
        col = 0
        while (row < MAX_TILES_WIDTH):
            while (col < MAX_TILES_WIDTH):
                if (self.tiles_array[row][col] != None):
                    self.tiles_array[row][col].draw_tile(surface)
                col += 1
            row += 1
            col = 0

    #returns the first row that has a tile in it (topmost tile)
    def get_first_row(self):
        i = 0;
        j = 0;
        while i < MAX_TILES_WIDTH:
            while j < MAX_TILES_WIDTH:
                if self.tiles_array[i][j] != None:
                    return i
                else:
                    j += 1;
            i += 1;
            j = 0;

    #returns the first column that has a tile in it (leftmost tile)
    def get_first_col(self):
        i = 0;
        j = 0;
        while j < MAX_TILES_WIDTH:
            while i < MAX_TILES_WIDTH:
                if self.tiles_array[i][j] != None:
                    return j
                else:
                    i += 1;
            j += 1;
            i = 0;
    
    #returns the first tile in the array
    def get_first_tile(self):
        i = 0;
        j = 0;
        while i < MAX_TILES_WIDTH:
            while j < MAX_TILES_WIDTH:
                if self.tiles_array[i][j] != None:
                    return self.tiles_array[i][j]
                else:
                    j += 1;
            i += 1;
            j = 0;
        

    # rotates the piece clockwise
    def rotate_cw(self):
        orig_x = self.get_first_tile().get_location()[0]-30*self.get_first_row()
        orig_y = self.get_first_tile().get_location()[1]-30*self.get_first_col()
        self.tiles_array = np.rot90(self.tiles_array).tolist()
        self.reset_distances(orig_x, orig_y)
        

    # rotates the piece counterclockwise
    def rotate_ccw(self):
        self.tiles_array = np.rot90(self.tiles_array, 3).tolist()
        self.reset_distances()
    
    #flips the piece vertically
    #this rotates them for some reason too???
    def flip_vert(self):
        self.tiles_array = np.flip(self.tiles_array, 0).tolist()
        self.reset_distances()

    #flips the piece horizontally
    def flip_horiz(self):
        self.tiles_array = np.flip(self.tiles_array, 1).tolist()
        self.reset_distances()
