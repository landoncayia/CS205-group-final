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
        self.tiles_array = [[None] * MAX_TILES_WIDTH for _ in range(MAX_TILES_WIDTH)] # tiles will be added here
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
            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
        # 2 tiles
        elif self.shape == Shape.TWO:
            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
            self.tiles_array[0][1] = Tile(self.x + TILE_WIDTH, self.y, self.color)

        # 3 tiles
        elif self.shape == Shape.V3:
            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
            self.tiles_array[1][0] = Tile(self.x + TILE_WIDTH, self.y, self.color)
            self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)

        elif self.shape == Shape.I3:
            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
            self.tiles_array[1][0] = Tile(self.x + TILE_WIDTH, self.y, self.color)
            self.tiles_array[2][0] = Tile(self.x + (2 * TILE_WIDTH), self.y, self.color)

        # 4 tiles
        elif self.shape == Shape.T4:
            self.tiles_array[1][0] = Tile(self.x + TILE_WIDTH, self.y, self.color)
            self.tiles_array[0][1] = Tile(self.x, self.y + TILE_WIDTH, self.color)
            self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)
            self.tiles_array[2][1] = Tile(self.x + (2 * TILE_WIDTH), self.y + TILE_WIDTH, self.color)

        elif self.shape == Shape.O:
            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
            self.tiles_array[1][0] = Tile(self.x + TILE_WIDTH, self.y, self.color)
            self.tiles_array[0][1] = Tile(self.x, self.y + TILE_WIDTH, self.color)
            self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)

        elif self.shape == Shape.L4:
            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
            self.tiles_array[0][1] = Tile(self.x, self.y + TILE_WIDTH, self.color)
            self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)
            self.tiles_array[2][1] = Tile(self.x + (2 * TILE_WIDTH), self.y + TILE_WIDTH, self.color)

        elif self.shape == Shape.I4:
            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
            self.tiles_array[1][0] = Tile(self.x + TILE_WIDTH, self.y, self.color)
            self.tiles_array[2][0] = Tile(self.x + (2 * TILE_WIDTH), self.y, self.color)
            self.tiles_array[3][0] = Tile(self.x + (3 * TILE_WIDTH), self.y, self.color)

        elif self.shape == Shape.Z4:
            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
            self.tiles_array[0][1] = Tile(self.x, self.y + TILE_WIDTH, self.color)
            self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y, self.color)
            self.tiles_array[1][2] = Tile(self.x + TILE_WIDTH, self.y + (2 * TILE_WIDTH), self.color)

        # 5 tiles
        elif self.shape == Shape.F:
            self.tiles_array[0][1] = Tile(self.x, self.y + TILE_WIDTH, self.color)
            self.tiles_array[0][2] = Tile(self.x, self.y + (2 * TILE_WIDTH), self.color)
            self.tiles_array[1][0] = Tile(self.x + TILE_WIDTH, self.y, self.color)
            self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)
            self.tiles_array[2][1] = Tile(self.x + (2 * TILE_WIDTH), self.y + TILE_WIDTH, self.color)

        elif self.shape == Shape.X:
            self.tiles_array[0][1] = Tile(self.x, self.y + TILE_WIDTH, self.color)
            self.tiles_array[1][0] = Tile(self.x + TILE_WIDTH, self.y, self.color)
            self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)
            self.tiles_array[1][2] = Tile(self.x + TILE_WIDTH, self.y + (2 * TILE_WIDTH), self.color)
            self.tiles_array[2][1] = Tile(self.x + (2 * TILE_WIDTH), self.y + TILE_WIDTH, self.color)

        elif self.shape == Shape.P:
            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
            self.tiles_array[0][1] = Tile(self.x, self.y + TILE_WIDTH, self.color)
            self.tiles_array[0][2] = Tile(self.x, self.y + (2 * TILE_WIDTH), self.color)
            self.tiles_array[1][0] = Tile(self.x + TILE_WIDTH, self.y, self.color)
            self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)

        elif self.shape == Shape.W:
            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
            self.tiles_array[0][1] = Tile(self.x, self.y + TILE_WIDTH, self.color)
            self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)
            self.tiles_array[1][2] = Tile(self.x + TILE_WIDTH, self.y + (2 * TILE_WIDTH), self.color)
            self.tiles_array[2][2] = Tile(self.x + (2 * TILE_WIDTH), self.y + (2 * TILE_WIDTH), self.color)


        elif self.shape == Shape.Z5:
            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
            self.tiles_array[0][1] = Tile(self.x, self.y + TILE_WIDTH, self.color)
            self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)
            self.tiles_array[2][1] = Tile(self.x + (2 * TILE_WIDTH), self.y + TILE_WIDTH, self.color)
            self.tiles_array[2][2] = Tile(self.x + (2 * TILE_WIDTH), self.y + (2 * TILE_WIDTH), self.color)

        elif self.shape == Shape.Y:
            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
            self.tiles_array[1][0] = Tile(self.x + TILE_WIDTH, self.y, self.color)
            self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)
            self.tiles_array[2][0] = Tile(self.x + (2 * TILE_WIDTH), self.y, self.color)
            self.tiles_array[3][0] = Tile(self.x + (3 * TILE_WIDTH), self.y, self.color)

        elif self.shape == Shape.L5:
            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
            self.tiles_array[0][1] = Tile(self.x, self.y + TILE_WIDTH, self.color)
            self.tiles_array[1][0] = Tile(self.x + TILE_WIDTH, self.y, self.color)
            self.tiles_array[2][0] = Tile(self.x + (2 * TILE_WIDTH), self.y, self.color)
            self.tiles_array[3][0] = Tile(self.x + (3 * TILE_WIDTH), self.y, self.color)

        elif self.shape == Shape.U:
            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
            self.tiles_array[0][1] = Tile(self.x, self.y + TILE_WIDTH, self.color)
            self.tiles_array[1][0] = Tile(self.x + TILE_WIDTH, self.y, self.color)
            self.tiles_array[2][0] = Tile(self.x + (2 * TILE_WIDTH), self.y, self.color)
            self.tiles_array[2][1] = Tile(self.x + (2 * TILE_WIDTH), self.y + TILE_WIDTH, self.color)

        elif self.shape == Shape.T5:
            self.tiles_array[0][2] = Tile(self.x, self.y + (2 * TILE_WIDTH), self.color)
            self.tiles_array[1][0] = Tile(self.x + TILE_WIDTH, self.y, self.color)
            self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)
            self.tiles_array[1][2] = Tile(self.x + TILE_WIDTH, self.y + (2 * TILE_WIDTH), self.color)
            self.tiles_array[2][2] = Tile(self.x + (2 * TILE_WIDTH), self.y + (2 * TILE_WIDTH), self.color)

        elif self.shape == Shape.V5:
            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
            self.tiles_array[0][1] = Tile(self.x, self.y + TILE_WIDTH, self.color)
            self.tiles_array[0][2] = Tile(self.x, self.y + (2 * TILE_WIDTH), self.color)
            self.tiles_array[1][2] = Tile(self.x + TILE_WIDTH, self.y + (2 * TILE_WIDTH), self.color)
            self.tiles_array[2][2] = Tile(self.x + (2 * TILE_WIDTH), self.y + (2 * TILE_WIDTH), self.color)

        elif self.shape == Shape.N:
            self.tiles_array[0][1] = Tile(self.x, self.y + TILE_WIDTH, self.color)
            self.tiles_array[1][0] = Tile(self.x + TILE_WIDTH, self.y, self.color)
            self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)
            self.tiles_array[2][0] = Tile(self.x + (2 * TILE_WIDTH), self.y, self.color)
            self.tiles_array[3][0] = Tile(self.x + (3 * TILE_WIDTH), self.y, self.color)

        elif self.shape == Shape.I5:
            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
            self.tiles_array[1][0] = Tile(self.x + TILE_WIDTH, self.y, self.color)
            self.tiles_array[2][0] = Tile(self.x + (2 * TILE_WIDTH), self.y, self.color)
            self.tiles_array[3][0] = Tile(self.x + (3 * TILE_WIDTH), self.y, self.color)
            self.tiles_array[4][0] = Tile(self.x + (4 * TILE_WIDTH), self.y, self.color)

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

    def reset_distances(self, orig_x, orig_y):
        row = 0
        col = 0
        while (row < MAX_TILES_WIDTH):
            while (col < MAX_TILES_WIDTH):
                if (self.tiles_array[row][col] != None):
                    x = self.tiles_array[row][col].get_location()[0]
                    y = self.tiles_array[row][col].get_location()[1]
                    x = x + 30*row
                    y = y + 30*col
                    self.tiles_array[row][col].set_location(x,y)
                col += 1
            row += 1
            col = 0


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

    def get_first_tile(self):
        #look for first entry in array
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
    # 90 degree rotation: T(x,y) -> T(-y,x)
    #A point (a, b) rotated around a point (x, y) 90 degrees will transform to point 
    # (-(b-y) + x, (a-x) + y)
    
    def rotate_cw(self):
        print("Original array:")
        print(self.tiles_array)
        self.tiles_array = np.rot90(self.tiles_array).tolist()
        self.reset_distances(self.get_first_tile().get_location()[0],self.get_first_tile().get_location()[1])
        print("Rotated array:")
        print(self.tiles_array)

    # rotates the piece counterclockwise
    # 270 degree rotation: T(x,y) -> T(y,-x)
    # 
    def rotate_ccw(self):
        self.tiles_array = np.rot90(self.tiles_array, 3).tolist()
        self.reset_distances(self.get_first_tile().get_location()[0],self.get_first_tile().get_location()[1])
