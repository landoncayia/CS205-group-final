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


# each tile will have left, top, color, width, height, location
# a rect will be made with left, top, height, width
class Tile:
    height = 30
    width = 30

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    # GETTERS
    # get color
    def get_color(self):
        return self.color

    # get location
    def get_location(self):
        return self.x, self.y

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

    # OTHER FUNCTIONS
    def draw_tile(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
