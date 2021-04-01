import pygame

COL_LETTERS = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K',
                       11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T'}
BG_GREY = (50, 50, 50)
EMPTY_GREY = (172, 175, 181)
RED = (160, 0, 0)
GREEN = (0, 160, 0)
YELLOW = (220, 210, 0)
BLUE = (0, 0, 160)

class Board:
    # init function
    # window is the game window
    # surface is the game surface object
    # tiles is a 2-D list (20 x 20) of tile objects
    def __init__(self, window):
        self.surface = pygame.Surface(window)
        self.tiles = [[None for _ in range(20)] for _ in range(20)]  # tiles will be added here

    # draw() will draw the surface in the game window
    def draw(self):
        font = pygame.font.SysFont('Ubuntu', 18, bold=True)
        self.surface.fill(BG_GREY)
        pygame.draw.rect(self.surface, EMPTY_GREY, (32, 32, 730, 730), 3)
        for row in range(20):
            for col in range(20):
                    # these represent the top-left pixel of each tile
                    tile_x, tile_y = 40 + col + (35 * col), 40 + row + (35 * row)
                    if self.tiles[row][col] is None:
                        # if the position in tiles contains None, then draw a gray (empty) tile
                        pygame.draw.rect(self.surface, EMPTY_GREY, (tile_x, tile_y, 30, 30))
                    elif self.tiles[row][col].get_color() == 'red':
                        pygame.draw.rect(self.surface, RED, (tile_x, tile_y, 30, 30))
                    elif self.tiles[row][col].get_color() == 'green':
                        pygame.draw.rect(self.surface, GREEN, (tile_x, tile_y, 30, 30))
                    elif self.tiles[row][col].get_color() == 'yellow':
                        pygame.draw.rect(self.surface, YELLOW, (tile_x, tile_y, 30, 30))
                    elif self.tiles[row][col].get_color() == 'blue':
                        pygame.draw.rect(self.surface, BLUE, (tile_x, tile_y, 30, 30))
                    if row == 0:
                        text = font.render(COL_LETTERS[col], True, EMPTY_GREY)
                        self.surface.blit(text, (tile_x + 10, tile_y - 35))
                    if col == 0 and row < 9:
                        # row + 1 will be the row number
                        # change position slightly for vertical alignment of numbers
                        text = font.render(str(row + 1), True, EMPTY_GREY)
                        self.surface.blit(text, (tile_x - 25, tile_y + 5))
                    elif col == 0 and row >= 9:
                        text = font.render(str(row + 1), True, EMPTY_GREY)
                        self.surface.blit(text, (tile_x - 30, tile_y + 5))

    # Getters
    def get_surface(self):
        return self.surface

    def get_tiles(self):
        return self.tiles

    # Setters
    def set_tiles(self, tiles):
        self.tiles = tiles

    '''
    add_piece(): adds a piece to the tiles
    origin: tuple(int, int) - contains the origin [0-19] of the placed piece; e.g., (1, 1)
    tiles: list(tuple(int, int)) - contains the coordinates of the tiles that make up a piece, relative to its origin (x+ is right, y+ is down)
        NOTE: the first value in tiles should be (0, 0); e.g., [(0, 0), (1, 0), (2, 0), (0, 1), (-1, 1)] will make this shape:
          ■ ■ ■
        ■ ■
    '''
    def add_piece(self, origin, tiles):
        # waiting for other classes/discussion to write this
        pass
