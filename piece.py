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


# A Piece is a list of tiles with a center tile and various connected tiles
# The IntEnum Shape determines what kind of piece it is
# The top-leftmost tile is the center tile and connected tiles are added based on relative position to the center
class Piece:
    def __init__(self, shape, center):
        self.shape = shape
        self.table_tiles = list()
        self.printing_tiles = list()
        self.center = center
        self.set_tiles()
        self.selected = False
        # used to determine the spacing of pieces displayed on the side of the board, determined by what type of piece it is
        self.set_display_start

    def get_shape(self):
        return self.shape

    def set_shape(self, shape):
        self.shape = shape

    def get_tiles(self):
        return self.table_tiles

    def select(self):
        self.selected = True
        for tile in self.table_tiles:
            if tile.get_color() == Color.BLUE:
                tile.set_color(Color.BLUE_SELECTED)
            elif tile.get_color() == Color.YELLOW:
                tile.set_color(Color.YELLOW_SELECTED)
            elif tile.get_color() == Color.RED:
                tile.set_color(Color.RED_SELECTED)
            elif tile.get_color() == Color.GREEN:
                tile.set_color(Color.GREEN_SELECTED)
        for tile in self.printing_tiles:
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

    def set_display_start(self):
        if self.shape == Shape.TWO:
            self.display_start_x = 90
        elif self.shape == Shape.V3:
            self.display_start_x = 210
        elif self.shape == Shape.I3:
            self.display_start_y = 90
        elif self.shape == Shape.T4:
            self.display_start_x = 150
            self.display_start_y = 90
        elif self.shape == Shape.O:
            self.display_start_y = 180
        elif self.shape == Shape.L4:
            self.display_start_x = 120
            self.display_start_y = 180
        elif self.shape == Shape.I4:
            self.display_start_y = 270
        elif self.shape == Shape.Z4:
            self.display_start_x = 180
            self.display_start_y = 270
        elif self.shape == Shape.F:
            self.display_start_x = 30
            self.display_start_y = 330
        elif self.shape == Shape.X:
            self.display_start_x = 300
            self.display_start_y = 60
        elif self.shape == Shape.P:
            self.display_start_x = 300
            self.display_start_y = 330
        elif self.shape == Shape.W:
            self.display_start_x = 270
            self.display_start_y = 180
        elif self.shape == Shape.Z5:
            self.display_start_x = 120
            self.display_start_y = 360
        elif self.shape == Shape.Y:
            self.display_start_y = 450
        elif self.shape == Shape.L5:
            self.display_start_x = 240
            self.display_start_y = 450
        elif self.shape == Shape.U:
            self.display_start_x = 120
            self.display_start_y = 510
        elif self.shape == Shape.T5:
            self.display_start_x = 30
            self.display_start_y = 540
        elif self.shape == Shape.V5:
            self.display_start_x = 270
            self.display_start_y = 540
        elif self.shape == Shape.N:
            self.display_start_x = 30
            self.display_start_y = 660
        elif self.shape == Shape.I5:
            self.display_start_x = 180
            self.display_start_y = 660

    def set_tiles(self):
        # All tiles have a center piece
        # Connected pieces are added in reading order relative to center piece, left to right and top to bottom
        self.table_tiles.append(self.center)
        self.printing_tiles.append(self.center)
        # 2 tiles
        if self.shape == Shape.TWO:
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 1, self.center.get_location()[1], self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0] + self.center.get_width(), self.center.get_location()[1],
                     self.center.get_color()))
        # 3 tiles
        elif self.shape == Shape.V3:
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 1, self.center.get_location()[1], self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 1, self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0] + self.center.get_width(), self.center.get_location()[1],
                     self.center.get_color()))
            self.printing_tiles.append(Tile(self.center.get_location()[0] + self.center.get_width(),
                                            self.center.get_location()[1] + self.center.get_height(),
                                            self.center.get_color()))
        elif self.shape == Shape.I3:
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 1, self.center.get_location()[1], self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 2, self.center.get_location()[1], self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0] + self.center.get_width(), self.center.get_location()[1],
                     self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0] + 2 * self.center.get_width(), self.center.get_location()[1],
                     self.center.get_color()))
        # 4 tiles
        elif self.shape == Shape.T4:
            self.table_tiles.append(
                Tile(self.center.get_location()[0] - 1, self.center.get_location()[1] + 1, self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + 1, self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 1, self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0] - self.center.get_height(),
                     self.center.get_location()[1] + self.center.get_height(),
                     self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + self.center.get_height(),
                     self.center.get_color()))
            self.printing_tiles.append(Tile(self.center.get_location()[0] + self.center.get_width(),
                                            self.center.get_location()[1] + self.center.get_height(),
                                            self.center.get_color()))
        elif self.shape == Shape.O:
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 1, self.center.get_location()[1], self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + 1, self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 1, self.center.get_color()))

            self.printing_tiles.append(
                Tile(self.center.get_location()[0] + self.center.get_height(),
                     self.center.get_location()[1] + self.center.get_height(),
                     self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + self.center.get_height(),
                     self.center.get_color()))
            self.printing_tiles.append(Tile(self.center.get_location()[0] + self.center.get_width(),
                                            self.center.get_location()[1],
                                            self.center.get_color()))
        elif self.shape == Shape.L4:
            self.table_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + self.center.get_height(),
                     self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 1, self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 2, self.center.get_color()))

            self.printing_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + self.center.get_height(),
                     self.center.get_color()))
            self.printing_tiles.append(Tile(self.center.get_location()[0] + self.center.get_width(),
                                            self.center.get_location()[1] + self.center.get_height(),
                                            self.center.get_color()))
            self.printing_tiles.append(Tile(self.center.get_location()[0] + (2 * self.center.get_width()),
                                            self.center.get_location()[1] + self.center.get_height(),
                                            self.center.get_color()))

        elif self.shape == Shape.I4:
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 1, self.center.get_location()[1], self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 2, self.center.get_location()[1], self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 3, self.center.get_location()[1], self.center.get_color()))

            self.printing_tiles.append(
                Tile(self.center.get_location()[0] + self.center.get_width(), self.center.get_location()[1],
                     self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0] + 2 * self.center.get_width(), self.center.get_location()[1],
                     self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0] + 3 * self.center.get_width(), self.center.get_location()[1],
                     self.center.get_color()))

        elif self.shape == Shape.Z4:
            self.table_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + 1, self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 1, self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 2, self.center.get_color()))

            self.printing_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + self.center.get_height(),
                     self.center.get_color()))
            self.printing_tiles.append(Tile(self.center.get_location()[0] + self.center.get_width(),
                                            self.center.get_location()[1] + self.center.get_height(),
                                            self.center.get_color()))
            self.printing_tiles.append(Tile(self.center.get_location()[0] + self.center.get_width(),
                                            self.center.get_location()[1] + 2 * self.center.get_height(),
                                            self.center.get_color()))

        # 5 tiles
        elif self.shape == Shape.F:
            self.table_tiles.append(
                Tile(self.center.get_location()[0] - 1, self.center.get_location()[1] + 1, self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + 1, self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 1, self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] - 1, self.center.get_location()[1] + 2, self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0] - self.center.get_height(),
                     self.center.get_location()[1] + self.center.get_height(),
                     self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + self.center.get_height(),
                     self.center.get_color()))
            self.printing_tiles.append(Tile(self.center.get_location()[0] + self.center.get_width(),
                                            self.center.get_location()[1] + self.center.get_height(),
                                            self.center.get_color()))
            self.printing_tiles.append(Tile(self.center.get_location()[0] - self.center.get_height(),
                                            self.center.get_location()[1] + 2 * self.center.get_height(),
                                            self.center.get_color()))

        elif self.shape == Shape.X:
            self.table_tiles.append(
                Tile(self.center.get_location()[0] - 1, self.center.get_location()[1] + 1, self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + 1, self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 1, self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + 2, self.center.get_color()))

            self.printing_tiles.append(
                Tile(self.center.get_location()[0] - self.center.get_height(),
                     self.center.get_location()[1] + self.center.get_height(),
                     self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + self.center.get_height(),
                     self.center.get_color()))
            self.printing_tiles.append(Tile(self.center.get_location()[0] + self.center.get_width(),
                                            self.center.get_location()[1] + self.center.get_height(),
                                            self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + 2 * self.center.get_height(),
                     self.center.get_color()))

        elif self.shape == Shape.P:
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 1, self.center.get_location()[1], self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + 1, self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 1, self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + 2, self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0] + self.center.get_width(), self.center.get_location()[1],
                     self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + self.center.get_height(),
                     self.center.get_color()))
            self.printing_tiles.append(Tile(self.center.get_location()[0] + self.center.get_width(),
                                            self.center.get_location()[1] + self.center.get_height(),
                                            self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + 2 * self.center.get_height(),
                     self.center.get_color()))

        elif self.shape == Shape.W:
            self.table_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + 1, self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 1, self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 2, self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 2, self.center.get_location()[1] + 2, self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + self.center.get_height(),
                     self.center.get_color()))
            self.printing_tiles.append(Tile(self.center.get_location()[0] + self.center.get_width(),
                                            self.center.get_location()[1] + self.center.get_height(),
                                            self.center.get_color()))
            self.printing_tiles.append(Tile(self.center.get_location()[0] + self.center.get_width(),
                                            self.center.get_location()[1] + 2 * self.center.get_height(),
                                            self.center.get_color()))
            self.printing_tiles.append(Tile(self.center.get_location()[0] + 2 * self.center.get_width(),
                                            self.center.get_location()[1] + 2 * self.center.get_height(),
                                            self.center.get_color()))

        elif self.shape == Shape.Z5:
            self.table_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + 1, self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 1, self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 2, self.center.get_location()[1] + 1, self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 2, self.center.get_location()[1] + 2, self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + self.center.get_height(),
                     self.center.get_color()))
            self.printing_tiles.append(Tile(self.center.get_location()[0] + self.center.get_width(),
                                            self.center.get_location()[1] + self.center.get_height(),
                                            self.center.get_color()))
            self.printing_tiles.append(Tile(self.center.get_location()[0] + 2 * self.center.get_width(),
                                            self.center.get_location()[1] + self.center.get_height(),
                                            self.center.get_color()))
            self.printing_tiles.append(Tile(self.center.get_location()[0] + 2 * self.center.get_width(),
                                            self.center.get_location()[1] + 2 * self.center.get_height(),
                                            self.center.get_color()))

        elif self.shape == Shape.Y:
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 1, self.center.get_location()[1], self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 2, self.center.get_location()[1], self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 3, self.center.get_location()[1], self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 1, self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0] + self.center.get_width(), self.center.get_location()[1],
                     self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0] + 2 * self.center.get_width(), self.center.get_location()[1],
                     self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0] + 3 * self.center.get_width(), self.center.get_location()[1],
                     self.center.get_color()))
            self.printing_tiles.append(Tile(self.center.get_location()[0] + self.center.get_width(),
                                            self.center.get_location()[1] + self.center.get_height(),
                                            self.center.get_color()))

        elif self.shape == Shape.L5:
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 1, self.center.get_location()[1], self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 2, self.center.get_location()[1], self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 3, self.center.get_location()[1], self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 1, self.center.get_location()[1], self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0] + self.center.get_width(), self.center.get_location()[1],
                     self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0] + 2 * self.center.get_width(), self.center.get_location()[1],
                     self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0] + 3 * self.center.get_width(), self.center.get_location()[1],
                     self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + self.center.get_height(),
                     self.center.get_color()))

        elif self.shape == Shape.U:
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 1, self.center.get_location()[1], self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 2, self.center.get_location()[1], self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 1, self.center.get_location()[1], self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 2, self.center.get_color()))

            self.printing_tiles.append(
                Tile(self.center.get_location()[0] + self.center.get_width(), self.center.get_location()[1],
                     self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0] + 2 * self.center.get_width(), self.center.get_location()[1],
                     self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + self.center.get_height(),
                     self.center.get_color()))
            self.printing_tiles.append(Tile(self.center.get_location()[0] + 2 * self.center.get_width(),
                                            self.center.get_location()[1] + self.center.get_height(),
                                            self.center.get_color()))

        elif self.shape == Shape.T5:
            self.table_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + 1, self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] - 1, self.center.get_location()[1] + 2, self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + 2, self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 2, self.center.get_color()))

            self.printing_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + self.center.get_height(),
                     self.center.get_color()))
            self.printing_tiles.append(Tile(self.center.get_location()[0] - self.center.get_height(),
                                            self.center.get_location()[1] + 2 * self.center.get_height(),
                                            self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + 2 * self.center.get_height(),
                     self.center.get_color()))
            self.printing_tiles.append(Tile(self.center.get_location()[0] + self.center.get_width(),
                                            self.center.get_location()[1] + 2 * self.center.get_height(),
                                            self.center.get_color()))

        elif self.shape == Shape.V5:
            self.table_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + 1, self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + 2, self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 1, self.center.get_location()[1] + 2, self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 2, self.center.get_location()[1] + 2, self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + self.center.get_height(),
                     self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + 2 * self.center.get_height(),
                     self.center.get_color()))
            self.printing_tiles.append(Tile(self.center.get_location()[0] + self.center.get_width(),
                                            self.center.get_location()[1] + 2 * self.center.get_height(),
                                            self.center.get_color()))
            self.printing_tiles.append(Tile(self.center.get_location()[0] + 2 * self.center.get_width(),
                                            self.center.get_location()[1] + 2 * self.center.get_height(),
                                            self.center.get_color()))

        elif self.shape == Shape.N:
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 1, self.center.get_location()[1], self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 2, self.center.get_location()[1], self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] - 1, self.center.get_location()[1] + 1, self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + 1, self.center.get_color()))

            self.printing_tiles.append(
                Tile(self.center.get_location()[0] + self.center.get_width(), self.center.get_location()[1],
                     self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0] + 2 * self.center.get_width(), self.center.get_location()[1],
                     self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0] - self.center.get_height(),
                     self.center.get_location()[1] + self.center.get_height(),
                     self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0], self.center.get_location()[1] + self.center.get_height(),
                     self.center.get_color()))

        elif self.shape == Shape.I5:
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 1, self.center.get_location()[1], self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 2, self.center.get_location()[1], self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 3, self.center.get_location()[1], self.center.get_color()))
            self.table_tiles.append(
                Tile(self.center.get_location()[0] + 4, self.center.get_location()[1], self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0] + self.center.get_width(), self.center.get_location()[1],
                     self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0] + 2 * self.center.get_width(), self.center.get_location()[1],
                     self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0] + 3 * self.center.get_width(), self.center.get_location()[1],
                     self.center.get_color()))
            self.printing_tiles.append(
                Tile(self.center.get_location()[0] + 4 * self.center.get_width(), self.center.get_location()[1],
                     self.center.get_color()))

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
        for t in self.table_tiles:
            # ask Echo about the surface?
            t.draw_tile(surface)

    def draw_piece_outside_board(self, surface):
        for t in self.printing_tiles:
            t.draw_tile(surface)

    # rotates the piece clockwise
    # 90 degree rotation: T(x,y) -> T(-y,x)
    #A point (a, b) rotated around a point (x, y) 90 degrees will transform to point 
    # (-(b-y) + x, (a-x) + y)
    
    def rotate_cw(self):
        a = self.printing_tiles[0].get_location()[0]
        b = self.printing_tiles[0].get_location()[1]
        for tile in self.printing_tiles:
            #new_origin_x = tile.get_location[0]-self.display_start_x
            #new_origin_y = tile.get_location[1]-self.display_start_y
            
            x = tile.get_location()[0]
            y = tile.get_location()[1]
            #print(tile.get_location()[0])
            #print(tile.get_location()[1])
            
            #print(len(self.printing_tiles))
            #tile.set_location(-1 * (tile.get_location()[1]-180)+180, (tile.get_location()[0]-180)+180)
            print("Original location Tile # ", self.printing_tiles.index(tile))
            print("a: ", a)
            print("b: ", b)
            print("x: ", x)
            print("y: ", y)
            tile.set_location((-1*(b-y)), ((a-x)+y))
            print("Tile #", self.printing_tiles.index(tile))
            print("a: ", a)
            print("b: ", b)
            print("x: ", x)
            print("y: ", y)
            print()

    # rotates the piece counterclockwise
    # 270 degree rotation: T(x,y) -> T(y,-x)
    def rotate_ccw(self):
        for tile in self.printing_tiles:
            original_location = tile.get_location()
            tile.set_location(tile.get_location()[1]+180, -1 * tile.get_location()[0]+180)
