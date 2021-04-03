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
    def __init__(self, shape, center):
        self.shape = shape
        self.tiles = list()
        self.center = center
        self.set_tiles()
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
            self.tiles.append(Tile(self.center.get_location()[0]+1, self.center.get_location()[1], self.center.get_color()))
        # 3 tiles
        elif self.shape == Shape.V3:
            self.tiles.append(Tile(self.center.get_location()[0]+1, self.center.get_location()[1], self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+1, self.center.get_location()[1]+1, self.center.get_color()))
        elif self.shape == Shape.I3:
            self.tiles.append(Tile(self.center.get_location()[0]+1, self.center.get_location()[1], self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+2, self.center.get_location()[1], self.center.get_color()))
        # 4 tiles
        elif self.shape == Shape.T4:
            self.tiles.append(Tile(self.center.get_location()[0]-1, self.center.get_location()[1]+1, self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0], self.center.get_location()[1]+1, self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+1, self.center.get_location()[1]+1, self.center.get_color()))
        elif self.shape == Shape.O:
            self.tiles.append(Tile(self.center.get_location()[0]+1, self.center.get_location()[1], self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0], self.center.get_location()[1]+1, self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+1, self.center.get_location()[1]+1, self.center.get_color()))
        elif self.shape == Shape.L4:
            self.tiles.append(Tile(self.center.get_location()[0], self.center.get_location()[1]+1, self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+1, self.center.get_location()[1]+1, self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+1, self.center.get_location()[1]+2, self.center.get_color()))
        elif self.shape == Shape.I4:
            self.tiles.append(Tile(self.center.get_location()[0]+1, self.center.get_location()[1], self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+2, self.center.get_location()[1], self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+3, self.center.get_location()[1], self.center.get_color()))
        elif self.shape == Shape.Z4:
            self.tiles.append(Tile(self.center.get_location()[0], self.center.get_location()[1]+1, self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+1, self.center.get_location()[1]+1, self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+1, self.center.get_location()[1]+2, self.center.get_color()))
        # 5 tiles
        elif self.shape == Shape.F:
            self.tiles.append(Tile(self.center.get_location()[0]-1, self.center.get_location()[1]+1, self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0], self.center.get_location()[1]+1, self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+1, self.center.get_location()[1]+1, self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]-1, self.center.get_location()[1]+2, self.center.get_color()))
        elif self.shape == Shape.X:
            self.tiles.append(Tile(self.center.get_location()[0]-1, self.center.get_location()[1]+1, self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0], self.center.get_location()[1]+1, self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+1, self.center.get_location()[1]+1, self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0], self.center.get_location()[1]+2, self.center.get_color()))
        elif self.shape == Shape.P:
            self.tiles.append(Tile(self.center.get_location()[0]+1, self.center.get_location()[1], self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0], self.center.get_location()[1]+1, self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+1, self.center.get_location()[1]+1, self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0], self.center.get_location()[1]+2, self.center.get_color()))
        elif self.shape == Shape.W:
            self.tiles.append(Tile(self.center.get_location()[0], self.center.get_location()[1]+1, self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+1, self.center.get_location()[1]+1, self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+1, self.center.get_location()[1]+2, self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+2, self.center.get_location()[1]+2, self.center.get_color()))
        elif self.shape == Shape.Z5:
            self.tiles.append(Tile(self.center.get_location()[0], self.center.get_location()[1]+1, self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+1, self.center.get_location()[1]+1, self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+2, self.center.get_location()[1]+1, self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+2, self.center.get_location()[1]+2, self.center.get_color()))
        elif self.shape == Shape.Y:
            self.tiles.append(Tile(self.center.get_location()[0]+1, self.center.get_location()[1], self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+2, self.center.get_location()[1], self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+3, self.center.get_location()[1], self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+1, self.center.get_location()[1]+1, self.center.get_color()))
        elif self.shape == Shape.L5:
            self.tiles.append(Tile(self.center.get_location()[0]+1, self.center.get_location()[1], self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+2, self.center.get_location()[1], self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+3, self.center.get_location()[1], self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+1, self.center.get_location()[1], self.center.get_color()))
        elif self.shape == Shape.U:
            self.tiles.append(Tile(self.center.get_location()[0]+1, self.center.get_location()[1], self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+2, self.center.get_location()[1], self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+1, self.center.get_location()[1], self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+1, self.center.get_location()[1]+2, self.center.get_color()))
        elif self.shape == Shape.T5:
            self.tiles.append(Tile(self.center.get_location()[0], self.center.get_location()[1]+1, self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]-1, self.center.get_location()[1]+2, self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0], self.center.get_location()[1]+2, self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+1, self.center.get_location()[1]+2, self.center.get_color()))
        elif self.shape == Shape.V5:
            self.tiles.append(Tile(self.center.get_location()[0], self.center.get_location()[1]+1, self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0], self.center.get_location()[1]+2, self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+1, self.center.get_location()[1]+2, self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+2, self.center.get_location()[1]+2, self.center.get_color()))
        elif self.shape == Shape.N:
            self.tiles.append(Tile(self.center.get_location()[0]+1, self.center.get_location()[1], self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+2, self.center.get_location()[1], self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]-1, self.center.get_location()[1]+1, self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0], self.center.get_location()[1]+1, self.center.get_color()))
        elif self.shape == Shape.I5:
            self.tiles.append(Tile(self.center.get_location()[0]+1, self.center.get_location()[1], self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+2, self.center.get_location()[1], self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+3, self.center.get_location()[1], self.center.get_color()))
            self.tiles.append(Tile(self.center.get_location()[0]+4, self.center.get_location()[1], self.center.get_color()))

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

