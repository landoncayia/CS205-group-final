from tile import Tile
from enum import IntEnum

#contains all possible pieces
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
    def __init__(self, shape, center, color):
        self.shape = shape
        self.tiles = list()
        self.center = center
        self.color = color
    def get_shape(self):
        return self.shape
    def set_shape(self, shape):
        self.shape = shape
    def get_tiles(self):
        return self.tiles
    def set_tiles(self):
        #All tiles have a center piece
        #Connected pieces are added in reading order relative to center piece, left to right and top to bottom
        self.tiles.append(self.center)
        # 2 tiles
        if self.shape == Shape.TWO:
            tiles.append(Tile(center.getLocation()[0]+1, center.getLocation()[1], center.getColor()))
        # 3 tiles
        elif self.shape == Shape.V3:
            tiles.append(Tile(center.getLocation()[0]+1, center.getLocation()[1], center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+1, center.getLocation()[1]+1, center.getColor()))
        elif self.shape == Shape.I3:
            tiles.append(Tile(center.getLocation()[0]+1, center.getLocation()[1], center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+2, center.getLocation()[1], center.getColor()))
        # 4 tiles
        elif self.shape == Shape.T4:
            tiles.append(Tile(center.getLocation()[0]-1, center.getLocation()[1]+1, center.getColor()))
            tiles.append(Tile(center.getLocation()[0], center.getLocation()[1]+1, center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+1, center.getLocation()[1]+1, center.getColor()))
        elif self.shape == Shape.O:
            tiles.append(Tile(center.getLocation()[0]+1, center.getLocation()[1], center.getColor()))
            tiles.append(Tile(center.getLocation()[0], center.getLocation()[1]+1, center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+1, center.getLocation()[1]+1, center.getColor()))
        elif self.shape == Shape.L4:
            tiles.append(Tile(center.getLocation()[0], center.getLocation()[1]+1, center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+1, center.getLocation()[1]+1, center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+1, center.getLocation()[1]+2, center.getColor()))
        elif self.shape == Shape.I4:
            tiles.append(Tile(center.getLocation()[0]+1, center.getLocation()[1], center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+2, center.getLocation()[1], center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+3, center.getLocation()[1], center.getColor()))
        elif self.shape == Shape.Z4:
            tiles.append(Tile(center.getLocation()[0], center.getLocation()[1]+1, center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+1, center.getLocation()[1]+1, center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+1, center.getLocation()[1]+2, center.getColor()))
        # 5 tiles
        elif self.shape == Shape.F:
            tiles.append(Tile(center.getLocation()[0]-1, center.getLocation()[1]+1, center.getColor()))
            tiles.append(Tile(center.getLocation()[0], center.getLocation()[1]+1, center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+1, center.getLocation()[1]+1, center.getColor()))
            tiles.append(Tile(center.getLocation()[0]-1, center.getLocation()[1]+2, center.getColor()))
        elif self.shape == Shape.X:
            tiles.append(Tile(center.getLocation()[0]-1, center.getLocation()[1]+1, center.getColor()))
            tiles.append(Tile(center.getLocation()[0], center.getLocation()[1]+1, center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+1, center.getLocation()[1]+1, center.getColor()))
            tiles.append(Tile(center.getLocation()[0], center.getLocation()[1]+2, center.getColor()))
        elif self.shape == Shape.P:
            tiles.append(Tile(center.getLocation()[0]+1, center.getLocation()[1], center.getColor()))
            tiles.append(Tile(center.getLocation()[0], center.getLocation()[1]+1, center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+1, center.getLocation()[1]+1, center.getColor()))
            tiles.append(Tile(center.getLocation()[0], center.getLocation()[1]+2, center.getColor()))
        elif self.shape == Shape.W:
            tiles.append(Tile(center.getLocation()[0], center.getLocation()[1]+1, center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+1, center.getLocation()[1]+1, center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+1, center.getLocation()[1]+2, center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+2, center.getLocation()[1]+2, center.getColor()))
        elif self.shape == Shape.Z5:
            tiles.append(Tile(center.getLocation()[0], center.getLocation()[1]+1, center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+1, center.getLocation()[1]+1, center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+2, center.getLocation()[1]+1, center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+2, center.getLocation()[1]+2, center.getColor()))
        elif self.shape == Shape.Y:
            tiles.append(Tile(center.getLocation()[0]+1, center.getLocation()[1], center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+2, center.getLocation()[1], center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+3, center.getLocation()[1], center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+1, center.getLocation()[1]+1, center.getColor()))
        elif self.shape == Shape.L5:
            tiles.append(Tile(center.getLocation()[0]+1, center.getLocation()[1], center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+2, center.getLocation()[1], center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+3, center.getLocation()[1], center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+1, center.getLocation()[1], center.getColor()))
        elif self.shape == Shape.U:
            tiles.append(Tile(center.getLocation()[0]+1, center.getLocation()[1], center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+2, center.getLocation()[1], center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+1, center.getLocation()[1], center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+1, center.getLocation()[1]+2, center.getColor()))
        elif self.shape == Shape.T5:
            tiles.append(Tile(center.getLocation()[0], center.getLocation()[1]+1, center.getColor()))
            tiles.append(Tile(center.getLocation()[0]-1, center.getLocation()[1]+2, center.getColor()))
            tiles.append(Tile(center.getLocation()[0], center.getLocation()[1]+2, center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+1, center.getLocation()[1]+2, center.getColor()))
        elif self.shape == Shape.V5:
            tiles.append(Tile(center.getLocation()[0], center.getLocation()[1]+1, center.getColor()))
            tiles.append(Tile(center.getLocation()[0], center.getLocation()[1]+2, center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+1, center.getLocation()[1]+2, center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+2, center.getLocation()[1]+2, center.getColor()))
        elif self.shape == Shape.N:
            tiles.append(Tile(center.getLocation()[0]+1, center.getLocation()[1], center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+2, center.getLocation()[1], center.getColor()))
            tiles.append(Tile(center.getLocation()[0]-1, center.getLocation()[1]+1, center.getColor()))
            tiles.append(Tile(center.getLocation()[0], center.getLocation()[1]+1, center.getColor()))
        elif self.shape == Shape.I5:
            tiles.append(Tile(center.getLocation()[0]+1, center.getLocation()[1], center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+2, center.getLocation()[1], center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+3, center.getLocation()[1], center.getColor()))
            tiles.append(Tile(center.getLocation()[0]+4, center.getLocation()[1], center.getColor()))

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
            
    def draw_piece(self):
        for t in self.tiles:
            # ask Echo about the surface?
            t.drawTile()

