import pygame


class Board:
    # init function
    # window is the game window
    # board is the game board object
    # tiles is a 2-D list (20 x 20) of tile objects
    def __init__(self, window):
        self.board = pygame.Surface(window)
        self.tiles = [[] * 20] * 20  # tiles will be added here

    # draw() will draw the board in the game window
    def draw(self):
        font = pygame.font.SysFont('Ubuntu', 18, bold=True)
        col_letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K',
                       11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T'}
        self.board.fill((50, 50, 50))
        pygame.draw.rect(self.board, (172, 175, 181), (32, 32, 730, 730), 3)
        for row in range(20):
            for col in range(20):
                # these represent the top-left pixel of each tile
                tile_x, tile_y = 40 + col + (35 * col), 40 + row + (35 * row)
                # Once merged with Echo's Tile class, create Tile objects and use the line below for positioning/color
                pygame.draw.rect(self.board, (172, 175, 181), (tile_x, tile_y, 30, 30))
                if row == 0:
                    text = font.render(col_letters[col], True, (172, 175, 181))
                    self.board.blit(text, (tile_x + 10, tile_y - 35))
                if col == 0:
                    # row + 1 will be the row number
                    if row < 9:
                        # change position slightly for vertical alignment of numbers
                        text = font.render(str(row + 1), True, (172, 175, 181))
                        self.board.blit(text, (tile_x - 25, tile_y + 5))
                    else:
                        text = font.render(str(row + 1), True, (172, 175, 181))
                        self.board.blit(text, (tile_x - 30, tile_y + 5))

    # Getters
    def get_board(self):
        return self.board
