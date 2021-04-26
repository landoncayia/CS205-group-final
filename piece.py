from tile import Tile
from enum import IntEnum
from tile import Color


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

# A Piece is a list of tiles with a center tile and various connected tiles
# The IntEnum Shape determines what kind of piece it is
# The top-leftmost tile is the center tile and connected tiles are added based on relative position to the center
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

    def set_shape(self, shape):
        self.shape = shape

    def get_tiles(self):
        return self.table_tiles

    def select(self):
        self.selected = True
        if self.color == Color.BLUE:
            self.color = Color.BLUE_SELECTED
        elif self.color == Color.YELLOW:
            self.color = Color.YELLOW_SELECTED
        elif self.color == Color.RED:
            self.color = Color.RED_SELECTED
        elif self.color == Color.GREEN:
            self.color = Color.GREEN_SELECTED

    def deselect(self):
        self.selected = False
        if self.color == Color.BLUE_SELECTED:
            self.color = Color.BLUE
        elif self.color == Color.YELLOW_SELECTED:
            self.color = Color.YELLOW
        elif self.color == Color.RED_SELECTED:
            self.color = Color.RED
        elif self.color == Color.GREEN_SELECTED:
            self.color = Color.GREEN


    def is_selected(self):
        return self.selected

    def set_tiles(self):
        # All tiles have a center piece
        # Connected pieces are added in reading order relative to center piece, left to right and top to bottom
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


    # rotates the piece clockwise
    # 90 degree rotation: T(x,y) -> T(-y,x)
    def rotate_cw(self):
        for tile in self.table_tiles:
            tile.set_location(-1 * tile.get_location()[1], tile.get_location()[0])

    # rotates the piece counterclockwise
    # 270 degree rotation: T(x,y) -> T(y,-x)
    def rotate_ccw(self):
        for tile in self.table_tiles:
            tile.set_location(tile.get_location()[1], -1 * tile.get_location()[0])
