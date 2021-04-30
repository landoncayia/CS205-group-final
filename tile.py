import pygame
import pygame.locals

# FOR REFERENCE
# grey color : 50, 50, 50
# red color: 160, 0, 0
# green color: 0, 160, 0
# yellow color: 220, 210, 0
# blue color: 0, 0, 160
# tiles 30 x 30

from enum import Enum


class Color(Enum):
    BG_GREY = (50, 50, 50)
    EMPTY_GREY = (172, 175, 181)
    RED = (160, 0, 0)
    GREEN = (0, 160, 0)
    YELLOW = (220, 210, 0)
    BLUE = (0, 0, 160)
    RED_SELECTED = (255, 100, 100)
    GREEN_SELECTED = (100, 255, 100)
    BLUE_SELECTED = (100, 100, 255)
    YELLOW_SELECTED = (255, 255, 170)
    GREY_VALID = (200,200,215)


# each tile will have left, top, color, width, height, location
# a rect will be made with left, top, height, width
class Tile:
    height = 30
    width = 30

    # Board x and board y are optional
    def __init__(self, x, y, color, board_x=None, board_y=None):
        self.x = x
        self.y = y
        #if board_x is not None:
        self.board_x = board_x
        #if board_y is not None:
        self.board_y = board_y
        self.color = color

    # GETTERS
    # get color
    def get_color(self):
        return self.color

    # get location
    def get_location(self):
        return self.x, self.y

    def get_board_location(self):
        return self.board_x, self.board_y

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    # SETTERS
    # set color
    def set_color(self, color):
        self.color = color

    # set location
    def set_location(self, x, y):
        self.x = x
        self.y = y

    def set_board_location(self, board_x, board_y):
        self.board_x = board_x
        self.board_y = board_y

    # OTHER FUNCTIONS
    def draw_tile(self, surface):
        pygame.draw.rect(surface, self.color.value, (self.x, self.y, self.width, self.height))

    def make_valid(self):
        if self.get_color() == Color.BLUE:
            self.set_color(Color.BLUE_SELECTED)
        elif self.get_color() == Color.YELLOW:
            self.set_color(Color.YELLOW_SELECTED)
        elif self.get_color() == Color.RED:
            self.set_color(Color.RED_SELECTED)
        elif self.get_color() == Color.GREEN:
            self.set_color(Color.GREEN_SELECTED)
        elif self.get_color() == Color.EMPTY_GREY:
            self.set_color(Color.GREY_VALID)
