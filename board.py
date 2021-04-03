import pygame
from tile import Color

COL_LETTERS = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K',
                       11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T'}

class Board:
    # init function
    # window is the game window
    # surface is the game surface object
    # tiles is a 2-D list (20 x 20) of tile objects
    def __init__(self, window):
        self.surface = pygame.Surface((750,750))
        self.tiles = [[None for _ in range(20)] for _ in range(20)]  # tiles will be added here

    def draw_tile(self, row, col):
        # these represent the top-left pixel of each tile
        tile_x, tile_y = 40+(35*col), 40+(35*row)
        if self.tiles[row][col] is None:
            # if the position in tiles contains None, then draw an empty gray tile (30x30 pixels)
            pygame.draw.rect(self.surface, Color.EMPTY_GREY.value, (tile_x,tile_y,30,30))
        else:
            pygame.draw.rect(self.surface, self.tiles[row][col].get_color().value, (tile_x,tile_y,30,30))

    def draw_labels(self):
        font = pygame.font.SysFont('Ubuntu', 18, bold=True)
        # Draw letters along the top of the board (above each column)
        for col in range(20):
            text = font.render(COL_LETTERS[col], True, Color.EMPTY_GREY.value)
            self.surface.blit(text, (50+(35*col),5))
        # Draw numbers along the side of the board, left of each row
        # row + 1 will be the row number
        # change position slightly for vertical alignment of numbers
        for row in range(9):
            text = font.render(str(row+1), True, Color.EMPTY_GREY.value)
            self.surface.blit(text, (15,45+(35*row)))
        for row in range(9,20):
            text = font.render(str(row+1), True, Color.EMPTY_GREY.value)
            self.surface.blit(text, (10,45+(35*row)))

    # draw() will draw the surface in the game window
    def draw(self):
        # Need .value for an enum to get the actual tuple, not the enum object
        self.surface.fill(Color.BG_GREY.value)
        pygame.draw.rect(self.surface, Color.EMPTY_GREY.value, (35,35,705,705), 3)
        for row in range(20):
            for col in range(20):
                self.draw_tile(row, col)
        self.draw_labels()

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
    tiles: list(Tile) - contains the tiles that make up a piece
        NOTE: the first value in tiles should be (0, 0); e.g., [(0, 0), (1, 0), (2, 0), (0, 1), (-1, 1)] will make this shape:
          ■ ■ ■
        ■ ■
    '''
    def add_piece(self, piece):
        for tile in piece.get_tiles():
            self.tiles[tile.get_location()[0]][tile.get_location()[1]] = tile