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
        # for tile in self.table_tiles:
        #     if tile.get_color() == Color.BLUE:
        #         tile.set_color(Color.BLUE_SELECTED)
        #     elif tile.get_color() == Color.YELLOW:
        #         tile.set_color(Color.YELLOW_SELECTED)
        #     elif tile.get_color() == Color.RED:
        #         tile.set_color(Color.RED_SELECTED)
        #     elif tile.get_color() == Color.GREEN:
        #         tile.set_color(Color.GREEN_SELECTED)
        # for tile in self.printing_tiles:
        #     if tile.get_color() == Color.BLUE:
        #         tile.set_color(Color.BLUE_SELECTED)
        #     elif tile.get_color() == Color.YELLOW:
        #         tile.set_color(Color.YELLOW_SELECTED)
        #     elif tile.get_color() == Color.RED:
        #         tile.set_color(Color.RED_SELECTED)
        #     elif tile.get_color() == Color.GREEN:
        #         tile.set_color(Color.GREEN_SELECTED)
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
        for tile in self.table_tiles:
            if tile.get_color() == Color.BLUE_SELECTED:
                tile.set_color(Color.BLUE)
            elif tile.get_color() == Color.YELLOW_SELECTED:
                tile.set_color(Color.YELLOW)
            elif tile.get_color() == Color.RED_SELECTED:
                tile.set_color(Color.RED)
            elif tile.get_color() == Color.GREEN_SELECTED:
                tile.set_color(Color.GREEN)
        for tile in self.printing_tiles:
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

    def set_tiles(self):
        # All tiles have a center piece
        # Connected pieces are added in reading order relative to center piece, left to right and top to bottom
        # self.table_tiles.append(self.center)
        # self.printing_tiles.append(self.center)
        if self.shape == Shape.ONE:
            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
        # 2 tiles
        elif self.shape == Shape.TWO:
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 1, self.center.get_location()[1], self.center.get_color()))
            #
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0] + self.center.get_width(), self.center.get_location()[1],
            #          self.center.get_color()))
            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
            self.tiles_array[1][0] = Tile(self.x + TILE_WIDTH, self.y, self.color)

        # 3 tiles
        elif self.shape == Shape.V3:
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 1, self.center.get_location()[1], self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 1, self.center.get_color()))
            #
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0] + self.center.get_width(), self.center.get_location()[1],
            #          self.center.get_color()))
            # self.printing_tiles.append(Tile(self.center.get_location()[0] + self.center.get_width(),
            #                                 self.center.get_location()[1] + self.center.get_height(),
            #                                 self.center.get_color()))

            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
            self.tiles_array[1][0] = Tile(self.x + TILE_WIDTH, self.y, self.color)
            self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)

        elif self.shape == Shape.I3:
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 1, self.center.get_location()[1], self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 2, self.center.get_location()[1], self.center.get_color()))
            #
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0] + self.center.get_width(), self.center.get_location()[1],
            #          self.center.get_color()))
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0] + 2 * self.center.get_width(), self.center.get_location()[1],
            #          self.center.get_color()))

            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
            self.tiles_array[1][0] = Tile(self.x + TILE_WIDTH, self.y, self.color)
            self.tiles_array[2][0] = Tile(self.x + (2 * TILE_WIDTH), self.y, self.color)

        # 4 tiles
        elif self.shape == Shape.T4:
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] - 1, self.center.get_location()[1] + 1, self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + 1, self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 1, self.center.get_color()))
            #
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0] - self.center.get_height(),
            #          self.center.get_location()[1] + self.center.get_height(),
            #          self.center.get_color()))
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + self.center.get_height(),
            #          self.center.get_color()))
            # self.printing_tiles.append(Tile(self.center.get_location()[0] + self.center.get_width(),
            #                                 self.center.get_location()[1] + self.center.get_height(),
            #                                 self.center.get_color()))

            self.tiles_array[1][0] = Tile(self.x + TILE_WIDTH, self.y, self.color)
            self.tiles_array[0][1] = Tile(self.x, self.y + TILE_WIDTH, self.color)
            self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)
            self.tiles_array[2][1] = Tile(self.x + (2 * TILE_WIDTH), self.y + TILE_WIDTH, self.color)

        elif self.shape == Shape.O:
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 1, self.center.get_location()[1], self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + 1, self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 1, self.center.get_color()))
            #
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0] + self.center.get_height(),
            #          self.center.get_location()[1] + self.center.get_height(),
            #          self.center.get_color()))
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + self.center.get_height(),
            #          self.center.get_color()))
            # self.printing_tiles.append(Tile(self.center.get_location()[0] + self.center.get_width(),
            #                                 self.center.get_location()[1],
            #                                 self.center.get_color()))

            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
            self.tiles_array[1][0] = Tile(self.x + TILE_WIDTH, self.y, self.color)
            self.tiles_array[0][1] = Tile(self.x, self.y + TILE_WIDTH, self.color)
            self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)

        elif self.shape == Shape.L4:
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + self.center.get_height(),
            #          self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 1, self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 2, self.center.get_color()))
            #
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + self.center.get_height(),
            #          self.center.get_color()))
            # self.printing_tiles.append(Tile(self.center.get_location()[0] + self.center.get_width(),
            #                                 self.center.get_location()[1] + self.center.get_height(),
            #                                 self.center.get_color()))
            # self.printing_tiles.append(Tile(self.center.get_location()[0] + (2 * self.center.get_width()),
            #                                 self.center.get_location()[1] + self.center.get_height(),
            #                                 self.center.get_color()))

            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
            self.tiles_array[0][1] = Tile(self.x, self.y + TILE_WIDTH, self.color)
            self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)
            self.tiles_array[2][1] = Tile(self.x + (2 * TILE_WIDTH), self.y + TILE_WIDTH, self.color)

        elif self.shape == Shape.I4:
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 1, self.center.get_location()[1], self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 2, self.center.get_location()[1], self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 3, self.center.get_location()[1], self.center.get_color()))
            #
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0] + self.center.get_width(), self.center.get_location()[1],
            #          self.center.get_color()))
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0] + 2 * self.center.get_width(), self.center.get_location()[1],
            #          self.center.get_color()))
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0] + 3 * self.center.get_width(), self.center.get_location()[1],
            #          self.center.get_color()))

            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
            self.tiles_array[1][0] = Tile(self.x + TILE_WIDTH, self.y, self.color)
            self.tiles_array[2][0] = Tile(self.x + (2 * TILE_WIDTH), self.y, self.color)
            self.tiles_array[3][0] = Tile(self.x + (3 * TILE_WIDTH), self.y, self.color)

        elif self.shape == Shape.Z4:
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + 1, self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 1, self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 2, self.center.get_color()))
            #
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + self.center.get_height(),
            #          self.center.get_color()))
            # self.printing_tiles.append(Tile(self.center.get_location()[0] + self.center.get_width(),
            #                                 self.center.get_location()[1] + self.center.get_height(),
            #                                 self.center.get_color()))
            # self.printing_tiles.append(Tile(self.center.get_location()[0] + self.center.get_width(),
            #                                 self.center.get_location()[1] + 2 * self.center.get_height(),
            #                                 self.center.get_color()))

            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
            self.tiles_array[0][1] = Tile(self.x, self.y + TILE_WIDTH, self.color)
            self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y, self.color)
            self.tiles_array[1][2] = Tile(self.x + TILE_WIDTH, self.y + (2 * TILE_WIDTH), self.color)

        # 5 tiles
        elif self.shape == Shape.F:
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] - 1, self.center.get_location()[1] + 1, self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + 1, self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 1, self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] - 1, self.center.get_location()[1] + 2, self.center.get_color()))
            #
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0] - self.center.get_height(),
            #          self.center.get_location()[1] + self.center.get_height(),
            #          self.center.get_color()))
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + self.center.get_height(),
            #          self.center.get_color()))
            # self.printing_tiles.append(Tile(self.center.get_location()[0] + self.center.get_width(),
            #                                 self.center.get_location()[1] + self.center.get_height(),
            #                                 self.center.get_color()))
            # self.printing_tiles.append(Tile(self.center.get_location()[0] - self.center.get_height(),
            #                                 self.center.get_location()[1] + 2 * self.center.get_height(),
            #                                 self.center.get_color()))

            self.tiles_array[0][1] = Tile(self.x, self.y + TILE_WIDTH, self.color)
            self.tiles_array[0][2] = Tile(self.x, self.y + (2 * TILE_WIDTH), self.color)
            self.tiles_array[1][0] = Tile(self.x + TILE_WIDTH, self.y, self.color)
            self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)
            self.tiles_array[2][1] = Tile(self.x + (2 * TILE_WIDTH), self.y + TILE_WIDTH, self.color)

        elif self.shape == Shape.X:
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] - 1, self.center.get_location()[1] + 1, self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + 1, self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 1, self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + 2, self.center.get_color()))
            #
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0] - self.center.get_height(),
            #          self.center.get_location()[1] + self.center.get_height(),
            #          self.center.get_color()))
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + self.center.get_height(),
            #          self.center.get_color()))
            # self.printing_tiles.append(Tile(self.center.get_location()[0] + self.center.get_width(),
            #                                 self.center.get_location()[1] + self.center.get_height(),
            #                                 self.center.get_color()))
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + 2 * self.center.get_height(),
            #          self.center.get_color()))

            self.tiles_array[0][1] = Tile(self.x, self.y + TILE_WIDTH, self.color)
            self.tiles_array[1][0] = Tile(self.x + TILE_WIDTH, self.y, self.color)
            self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)
            self.tiles_array[1][2] = Tile(self.x + TILE_WIDTH, self.y + (2 * TILE_WIDTH), self.color)
            self.tiles_array[2][1] = Tile(self.x + (2 * TILE_WIDTH), self.y + TILE_WIDTH, self.color)

        elif self.shape == Shape.P:
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 1, self.center.get_location()[1], self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + 1, self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 1, self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + 2, self.center.get_color()))
            #
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0] + self.center.get_width(), self.center.get_location()[1],
            #          self.center.get_color()))
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + self.center.get_height(),
            #          self.center.get_color()))
            # self.printing_tiles.append(Tile(self.center.get_location()[0] + self.center.get_width(),
            #                                 self.center.get_location()[1] + self.center.get_height(),
            #                                 self.center.get_color()))
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + 2 * self.center.get_height(),
            #          self.center.get_color()))

            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
            self.tiles_array[0][1] = Tile(self.x, self.y + TILE_WIDTH, self.color)
            self.tiles_array[0][2] = Tile(self.x, self.y + (2 * TILE_WIDTH), self.color)
            self.tiles_array[1][0] = Tile(self.x + TILE_WIDTH, self.y, self.color)
            self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)

        elif self.shape == Shape.W:
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + 1, self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 1, self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 2, self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 2, self.center.get_location()[1] + 2, self.center.get_color()))
            #
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + self.center.get_height(),
            #          self.center.get_color()))
            # self.printing_tiles.append(Tile(self.center.get_location()[0] + self.center.get_width(),
            #                                 self.center.get_location()[1] + self.center.get_height(),
            #                                 self.center.get_color()))
            # self.printing_tiles.append(Tile(self.center.get_location()[0] + self.center.get_width(),
            #                                 self.center.get_location()[1] + 2 * self.center.get_height(),
            #                                 self.center.get_color()))
            # self.printing_tiles.append(Tile(self.center.get_location()[0] + 2 * self.center.get_width(),
            #                                 self.center.get_location()[1] + 2 * self.center.get_height(),
            #                                 self.center.get_color()))

            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
            self.tiles_array[0][1] = Tile(self.x, self.y + TILE_WIDTH, self.color)
            self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)
            self.tiles_array[1][2] = Tile(self.x + TILE_WIDTH, self.y + (2 * TILE_WIDTH), self.color)
            self.tiles_array[2][2] = Tile(self.x + (2 * TILE_WIDTH), self.y + (2 * TILE_WIDTH), self.color)


        elif self.shape == Shape.Z5:
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + 1, self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 1, self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 2, self.center.get_location()[1] + 1, self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 2, self.center.get_location()[1] + 2, self.center.get_color()))
            #
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + self.center.get_height(),
            #          self.center.get_color()))
            # self.printing_tiles.append(Tile(self.center.get_location()[0] + self.center.get_width(),
            #                                 self.center.get_location()[1] + self.center.get_height(),
            #                                 self.center.get_color()))
            # self.printing_tiles.append(Tile(self.center.get_location()[0] + 2 * self.center.get_width(),
            #                                 self.center.get_location()[1] + self.center.get_height(),
            #                                 self.center.get_color()))
            # self.printing_tiles.append(Tile(self.center.get_location()[0] + 2 * self.center.get_width(),
            #                                 self.center.get_location()[1] + 2 * self.center.get_height(),
            #                                 self.center.get_color()))

            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
            self.tiles_array[0][1] = Tile(self.x, self.y + TILE_WIDTH, self.color)
            self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)
            self.tiles_array[2][1] = Tile(self.x + (2 * TILE_WIDTH), self.y + TILE_WIDTH, self.color)
            self.tiles_array[2][2] = Tile(self.x + (2 * TILE_WIDTH), self.y + (2 * TILE_WIDTH), self.color)

        elif self.shape == Shape.Y:
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 1, self.center.get_location()[1], self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 2, self.center.get_location()[1], self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 3, self.center.get_location()[1], self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 1, self.center.get_color()))
            #
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0] + self.center.get_width(), self.center.get_location()[1],
            #          self.center.get_color()))
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0] + 2 * self.center.get_width(), self.center.get_location()[1],
            #          self.center.get_color()))
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0] + 3 * self.center.get_width(), self.center.get_location()[1],
            #          self.center.get_color()))
            # self.printing_tiles.append(Tile(self.center.get_location()[0] + self.center.get_width(),
            #                                 self.center.get_location()[1] + self.center.get_height(),
            #                                 self.center.get_color()))

            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
            self.tiles_array[1][0] = Tile(self.x + TILE_WIDTH, self.y, self.color)
            self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)
            self.tiles_array[2][0] = Tile(self.x + (2 * TILE_WIDTH), self.y, self.color)
            self.tiles_array[3][0] = Tile(self.x + (3 * TILE_WIDTH), self.y, self.color)

        elif self.shape == Shape.L5:
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 1, self.center.get_location()[1], self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 2, self.center.get_location()[1], self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 3, self.center.get_location()[1], self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 1, self.center.get_location()[1], self.center.get_color()))
            #
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0] + self.center.get_width(), self.center.get_location()[1],
            #          self.center.get_color()))
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0] + 2 * self.center.get_width(), self.center.get_location()[1],
            #          self.center.get_color()))
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0] + 3 * self.center.get_width(), self.center.get_location()[1],
            #          self.center.get_color()))
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + self.center.get_height(),
            #          self.center.get_color()))

            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
            self.tiles_array[0][1] = Tile(self.x, self.y + TILE_WIDTH, self.color)
            self.tiles_array[1][0] = Tile(self.x + TILE_WIDTH, self.y, self.color)
            self.tiles_array[2][0] = Tile(self.x + (2 * TILE_WIDTH), self.y, self.color)
            self.tiles_array[3][0] = Tile(self.x + (3 * TILE_WIDTH), self.y, self.color)

        elif self.shape == Shape.U:
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 1, self.center.get_location()[1], self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 2, self.center.get_location()[1], self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 1, self.center.get_location()[1], self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 2, self.center.get_color()))
            #
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0] + self.center.get_width(), self.center.get_location()[1],
            #          self.center.get_color()))
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0] + 2 * self.center.get_width(), self.center.get_location()[1],
            #          self.center.get_color()))
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + self.center.get_height(),
            #          self.center.get_color()))
            # self.printing_tiles.append(Tile(self.center.get_location()[0] + 2 * self.center.get_width(),
            #                                 self.center.get_location()[1] + self.center.get_height(),
            #                                 self.center.get_color()))

            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
            self.tiles_array[0][1] = Tile(self.x, self.y + TILE_WIDTH, self.color)
            self.tiles_array[1][0] = Tile(self.x + TILE_WIDTH, self.y, self.color)
            self.tiles_array[2][0] = Tile(self.x + (2 * TILE_WIDTH), self.y, self.color)
            self.tiles_array[2][1] = Tile(self.x + (2 * TILE_WIDTH), self.y + TILE_WIDTH, self.color)

        elif self.shape == Shape.T5:
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + 1, self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] - 1, self.center.get_location()[1] + 2, self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + 2, self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 2, self.center.get_color()))
            #
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + self.center.get_height(),
            #          self.center.get_color()))
            # self.printing_tiles.append(Tile(self.center.get_location()[0] - self.center.get_height(),
            #                                 self.center.get_location()[1] + 2 * self.center.get_height(),
            #                                 self.center.get_color()))
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + 2 * self.center.get_height(),
            #          self.center.get_color()))
            # self.printing_tiles.append(Tile(self.center.get_location()[0] + self.center.get_width(),
            #                                 self.center.get_location()[1] + 2 * self.center.get_height(),
            #                                 self.center.get_color()))

            self.tiles_array[0][2] = Tile(self.x, self.y + (2 * TILE_WIDTH), self.color)
            self.tiles_array[1][0] = Tile(self.x + TILE_WIDTH, self.y, self.color)
            self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)
            self.tiles_array[1][2] = Tile(self.x + TILE_WIDTH, self.y + (2 * TILE_WIDTH), self.color)
            self.tiles_array[2][2] = Tile(self.x + (2 * TILE_WIDTH), self.y + (2 * TILE_WIDTH), self.color)

        elif self.shape == Shape.V5:
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + 1, self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + 2, self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 2, self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 2, self.center.get_location()[1] + 2, self.center.get_color()))
            #
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + self.center.get_height(),
            #          self.center.get_color()))
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + 2 * self.center.get_height(),
            #          self.center.get_color()))
            # self.printing_tiles.append(Tile(self.center.get_location()[0] + self.center.get_width(),
            #                                 self.center.get_location()[1] + 2 * self.center.get_height(),
            #                                 self.center.get_color()))
            # self.printing_tiles.append(Tile(self.center.get_location()[0] + 2 * self.center.get_width(),
            #                                 self.center.get_location()[1] + 2 * self.center.get_height(),
            #                                 self.center.get_color()))

            self.tiles_array[0][0] = Tile(self.x, self.y, self.color)
            self.tiles_array[0][1] = Tile(self.x, self.y + TILE_WIDTH, self.color)
            self.tiles_array[0][2] = Tile(self.x, self.y + (2 * TILE_WIDTH), self.color)
            self.tiles_array[1][2] = Tile(self.x + TILE_WIDTH, self.y + (2 * TILE_WIDTH), self.color)
            self.tiles_array[2][2] = Tile(self.x + (2 * TILE_WIDTH), self.y + (2 * TILE_WIDTH), self.color)

        elif self.shape == Shape.N:
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 1, self.center.get_location()[1], self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 2, self.center.get_location()[1], self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] - 1, self.center.get_location()[1] + 1, self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + 1, self.center.get_color()))
            #
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0] + self.center.get_width(), self.center.get_location()[1],
            #          self.center.get_color()))
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0] + 2 * self.center.get_width(), self.center.get_location()[1],
            #          self.center.get_color()))
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0] - self.center.get_height(),
            #          self.center.get_location()[1] + self.center.get_height(),
            #          self.center.get_color()))
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0], self.center.get_location()[1] + self.center.get_height(),
            #          self.center.get_color()))

            self.tiles_array[0][1] = Tile(self.x, self.y + TILE_WIDTH, self.color)
            self.tiles_array[1][0] = Tile(self.x + TILE_WIDTH, self.y, self.color)
            self.tiles_array[1][1] = Tile(self.x + TILE_WIDTH, self.y + TILE_WIDTH, self.color)
            self.tiles_array[2][0] = Tile(self.x + (2 * TILE_WIDTH), self.y, self.color)
            self.tiles_array[3][0] = Tile(self.x + (3 * TILE_WIDTH), self.y, self.color)

        elif self.shape == Shape.I5:
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 1, self.center.get_location()[1], self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 2, self.center.get_location()[1], self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 3, self.center.get_location()[1], self.center.get_color()))
            # self.table_tiles.append(
            #     Tile(self.center.get_location()[0] + 4, self.center.get_location()[1], self.center.get_color()))
            #
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0] + self.center.get_width(), self.center.get_location()[1],
            #          self.center.get_color()))
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0] + 2 * self.center.get_width(), self.center.get_location()[1],
            #          self.center.get_color()))
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0] + 3 * self.center.get_width(), self.center.get_location()[1],
            #          self.center.get_color()))
            # self.printing_tiles.append(
            #     Tile(self.center.get_location()[0] + 4 * self.center.get_width(), self.center.get_location()[1],
            #          self.center.get_color()))

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

    def draw_piece(self, surface):
        # for t in self.table_tiles:
        #     # ask Echo about the surface?
        #     t.draw_tile(surface)
        row = 0
        col = 0
        while (row < MAX_TILES_WIDTH):
            while (col < MAX_TILES_WIDTH):
                if (self.tiles_array[row][col] != None):
                    self.tiles_array[row][col].draw_tile(surface)
                col += 1
            row += 1


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
