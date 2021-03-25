import pygame


class Board:
    # init function
    # window is the game window
    # board is the game board object
    # tiles is a 2-D list (20 x 20) of tile objects
    def __init__(self, window):
        self.board = pygame.Surface(window)
        self.tiles = [[] * 20] * 20

    # draw() will draw the board in the game window
    def draw(self):
        self.board.fill((50, 50, 50))
        for row in range(20):
            for col in range(20):
                pygame.draw.rect(self.board, (172, 175, 181), (40 + col + (35 * col), 40 + row + (35 * row), 30, 30))
