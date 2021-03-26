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
    GREY = (50, 50, 50)
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
    def getColor(self):
        return self.color

    # get location
    def getLocation(self):
        return self.x, self.y

    # SETTERS
    # set color
    def setColor(self, color):
        self.color = color

    # set location
    def setLocation(self, x, y):
        self.x = x
        self.y = y

    # OTHER FUNCTIONS
    def drawTile(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
