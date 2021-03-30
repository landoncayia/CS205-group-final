# from tile import Tile
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

class Piece:
    def __init__(self, shape, tiles):
        self.shape = shape
        self.tiles = tiles
    def get_shape(self):
        return self.shape
    def set_shape(self, shape):
        self.shape = shape
    def get_num_tiles(self):
        if(self.shape == Shape.ONE){
            return 1
        }
        elif(self.shape == Shape.TWO){
            return 2
        }
        elif(self.shape == 3 or self.shape == 4){
            return 3
        }
        elif(self.shape >= 5 and self.shape < 10){
            return 4
        }
        else{
            return 5
        }

