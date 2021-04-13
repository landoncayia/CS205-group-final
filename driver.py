import sys
import pygame
import pygame.locals
from board import Board
from piece import Piece
from piece import Shape
from tile import Color
from tile import Tile

BOARD_WIDTH, BOARD_HEIGHT = 800, 800
NEXT_PLAYER = {'b': 'y', 'y': 'r', 'r': 'g', 'g': 'b'}  # dict used to go to next player in order of play: Blue -> Yellow -> Red -> Green
NEXT_COLOR = {Color.BLUE: Color.YELLOW, Color.YELLOW: Color.RED,  # dict used to go to next color in order of play, as above
              Color.RED: Color.GREEN, Color.GREEN: Color.BLUE}


def create_set(start_x, start_y, set_color):
    set_of_tiles = list()
    set_of_tiles.append(Piece(Shape.ONE, Tile(start_x, start_y, set_color)))
    set_of_tiles.append(Piece(Shape.TWO, Tile(start_x + 90, start_y, set_color)))
    set_of_tiles.append(Piece(Shape.V3, Tile(start_x + 210, start_y, set_color)))
    set_of_tiles.append(Piece(Shape.I3, Tile(start_x, start_y + 90, set_color)))
    set_of_tiles.append(Piece(Shape.T4, Tile(start_x + 150, start_y + 90, set_color)))
    set_of_tiles.append(Piece(Shape.O, Tile(start_x, start_y + 180, set_color)))
    set_of_tiles.append(Piece(Shape.L4, Tile(start_x + 120, start_y + 180, set_color)))
    set_of_tiles.append(Piece(Shape.I4, Tile(start_x, start_y + 270, set_color)))
    set_of_tiles.append(Piece(Shape.Z4, Tile(start_x + 180, start_y + 270, set_color)))
    set_of_tiles.append(Piece(Shape.F, Tile(start_x + 30, start_y + 330, set_color)))
    set_of_tiles.append(Piece(Shape.X, Tile(start_x + 300, start_y + 60, set_color)))
    set_of_tiles.append(Piece(Shape.P, Tile(start_x + 300, start_y + 330, set_color)))
    set_of_tiles.append(Piece(Shape.W, Tile(start_x + 270, start_y + 180, set_color)))
    set_of_tiles.append(Piece(Shape.Z5, Tile(start_x + 120, start_y + 360, set_color)))
    set_of_tiles.append(Piece(Shape.Y, Tile(start_x, start_y + 450, set_color)))
    set_of_tiles.append(Piece(Shape.L5, Tile(start_x + 240, start_y + 450, set_color)))
    set_of_tiles.append(Piece(Shape.U, Tile(start_x + 120, start_y + 510, set_color)))
    set_of_tiles.append(Piece(Shape.T5, Tile(start_x + 30, start_y + 540, set_color)))
    set_of_tiles.append(Piece(Shape.V5, Tile(start_x + 270, start_y + 540, set_color)))
    set_of_tiles.append(Piece(Shape.N, Tile(start_x + 30, start_y + 660, set_color)))
    set_of_tiles.append(Piece(Shape.I5, Tile(start_x + 180, start_y + 660, set_color)))
    return set_of_tiles


class GameState:
    def __init__(self):
        '''
        States: start, waiting, turn, end
            start: game should begin in this state
            waiting: waiting for a player to select a piece
            turn: player has selected a piece, and we are waiting for them to place it on the board
            end: the game has ended, and a player has won
        Player: determined which player's turn it is
            'b': Blue
            'y': Yellow
            'r': Red
            'g': Green
        Selected: represents the piece the player will place on the board
        '''
        self.state = 'waiting'          # NOTE: This should be changed to 'start' later, this is just for testing
        self.player = 'b'               # NOTE: Blue player goes first
        self.set_color = Color.BLUE     # The color value of the current player
        self.selected = None            # currently selected piece, if any

    '''
    This function will call other helper functions to handle input events accordingly, depending on the game state
    '''
    def handle_events(self, events):
        def start_loop(events):
            '''
            Beginning of game, in which number of players is specified. This will be part of Sprint Two
            We could ask the player to use the number keys on their keyboard to select the number of players; this will highlight squares on-screen
            Once they have selected their number of players, space could begin the game
            For now, ignore this
            '''
            pass
        
        def waiting_loop(events):
            '''
            We are waiting on whomever's turn it currently is to select a piece for placement on the board
            Allow players to select pieces by clicking on them; we will have to figure this out geometrically with Echo's code
            '''
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Left mouse button pressed, get mouse position
                x, y = pygame.mouse.get_pos() # (x, y), where x and y are the number of pixels away from the top-left corner
                for piece in tiles_set: # Go through each piece in the tile set that is currently on-screen
                    for tile in piece.printing_tiles: # Go through each tile in the piece
                        tile_x, tile_y = tile.get_location() # Get the x, y coordinates of the tile (top-left)
                        if 800+tile_x < x < 800+tile_x+30 and tile_y < y < tile_y+30: # Check if the mouse click location matches the range of this tile
                            piece.select() # If so, select the piece, change state to turn, and end the loop
                            self.selected = piece
                            self.state = 'turn'
                        break
        
        def turn_loop(events):
            '''
            We are waiting on whomever's turn it currently is to place their piece somewhere on the board
            This will involve a calculation as to whether a move is legal or not; perhaps in board we could have 'verify_legal'?
            Additionally, players can right-click to put their piece back and select another.
            '''
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Left mouse button pressed, get position
                    x, y = pygame.mouse.get_pos()
                    # Place piece
                    # Remove piece from player's pieces
                    self.player = NEXT_PLAYER[self.player] # Go to next player
                    self.set_color = NEXT_COLOR[self.set_color] # Set next color
            
                if event.button == 3:
                    # Right mouse button pressed; unselect current piece and go back to waiting state
                    for piece in tiles_set: # Go through each piece in the tile set that is currently on-screen
                        if piece.selected: # Check if the piece is selected
                            piece.deselect() # If so, deselect the piece, change state to waiting, and end the loop
                            self.selected = None
                            self.state = 'waiting'
                            break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.selected.rotate_ccw()
                if event.key == pygame.K_RIGHT:
                    self.selected.rotate_cw()
        
        def end_loop(events):
            '''
            The game has ended; display the winner
            '''
            pass
        
        # Call the proper function, depending on the game state
        if self.state == 'start':
            start_loop(events)
        elif self.state == 'waiting':
            waiting_loop(events)
        elif self.state == 'turn':
            turn_loop(events)
        elif self.state == 'end':
            end_loop(events)


if __name__ == '__main__':
    pygame.init()
    window = (1200, 800)
    screen = pygame.display.set_mode(window)
    pygame.display.set_caption('Blokus')
    screen.fill(Color.BG_GREY.value)
    pieces_surface = pygame.Surface((400, 800))
    timer = pygame.time.Clock()

    # Create the game state object
    game_state = GameState()

    # Create and draw a board, then put it on the screen
    board = Board(window)

    board.draw()
    screen.blit(board.get_surface(), (BOARD_WIDTH//2-board.get_surface().get_width()//2,
                                      BOARD_HEIGHT//2-board.get_surface().get_height()//2))

    # DISPLAY PIECES
    pieces_surface.fill(Color.BG_GREY.value)

    start_x = 10
    start_y = 30
    set_color = Color.BLUE
    tiles_set = create_set(start_x, start_y, set_color)

    for piece in tiles_set:
        piece.draw_piece_outside_board(pieces_surface)

    screen.blit(pieces_surface, (800, 0))

    pygame.display.flip()

    # Game loop
    while True:
        # Update the board every frame
        timer.tick(60)
        board.draw()
        screen.blit(board.get_surface(), (BOARD_WIDTH//2-board.get_surface().get_width()//2,
                                    BOARD_HEIGHT//2-board.get_surface().get_height()//2))
        for piece in tiles_set:
            piece.draw_piece_outside_board(pieces_surface)
        screen.blit(pieces_surface, (800, 0))
        pygame.display.flip()

        # Escape quits the game
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                raise SystemExit
            if event.type == pygame.QUIT:
                raise SystemExit

        game_state.handle_events(pygame.event.get())
    
    pygame.quit()
