import sys
import pygame
import pygame.locals
from board import Board
from board import create_set, clear_set
from piece import Piece
from piece import Shape
from tile import Color
from tile import Tile

#  dimensions of the board
BOARD_WIDTH, BOARD_HEIGHT = 800, 800
#  order of play: 1 (Blue) -> 2 (Yellow) -> 3 (Red) -> 4 (Green)
#  dict used to go to next color in order of play, as above
NEXT_COLOR = {Color.BLUE: Color.YELLOW, Color.YELLOW: Color.RED,
              Color.RED: Color.GREEN, Color.GREEN: Color.BLUE}


class Player:
    def __init__(self, number, color):
        """
        An instance of a player; each player has a number, a color, and a set of tiles that they can place on the board
        1: Blue, 2: Yellow, 3: Red, 4: Green
        """
        #  These are the starting positions (in pixels) for the set of pieces that the player can select from
        start_x = 10
        start_y = 30
        self.number = number
        self.color = color
        self.tiles_set = create_set(start_x, start_y, color)


class GameState:
    def __init__(self):
        """
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
        """
        self.state = 'waiting'          # NOTE: This should be changed to 'start' later, this is just for testing
        self.player = None              # The current player
        self.selected = None            # currently selected piece, if any

    def start_loop(self, events):
        """
        Beginning of game, in which number of players is specified. This will be part of Sprint Two
        We could ask the player to use the number keys on their keyboard to select the number of players; this will highlight squares on-screen
        Once they have selected their number of players, space could begin the game
        For now, ignore this
        """
        pass

    def waiting_loop(self, events):
        """
        We are waiting on whomever's turn it currently is to select a piece for placement on the board
        Allow players to select pieces by clicking on them; we will have to figure this out geometrically with Echo's code
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Left mouse button pressed, get mouse position
            x, y = pygame.mouse.get_pos()  # (x, y) where x and y are the number of pixels away from the top-left corner
            for piece in self.player.tiles_set:  # Go through each piece in the tile set that is currently on-screen
                for row in piece.tiles_array:  # Go through each row in the tile array
                    for tile in row:
                        if tile is not None:
                            tile_x, tile_y = tile.get_location() # Get the x, y coordinates of the tile (top-left)
                            if 800+tile_x < x < 800+tile_x+30 and tile_y < y < tile_y+30:
                                # Check if the mouse click location matches the range of this tile
                                # If so, select the piece, change state to turn, and end the loop
                                piece.select()
                                self.selected = piece
                                self.state = 'turn'
                            break

    def turn_loop(self, events):
        """
        We are waiting on whomever's turn it currently is to place their piece somewhere on the board
        This will involve a calculation as to whether a move is legal or not
        Additionally, players can right-click to put their piece back and select another.
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Left mouse button pressed, get position
            x, y = pygame.mouse.get_pos()
            # Place piece
            for row in board.tiles:
                for tile in row:
                    if 30+tile.x < x < 60+tile.x and 30+tile.y < y < 60+tile.y:
                        board.add_piece(self.selected, tile.board_x, tile.board_y)
                        self.player.tiles_set.remove(self.selected)
                        self.selected.deselect()
                        self.state = 'waiting'
                        self.next_player()  # Go to next player

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            # Right mouse button pressed; unselect current piece and go back to waiting state
            for piece in self.player.tiles_set:  # Go through each piece in the tile set that is currently on-screen
                if piece.selected:  # Check if the piece is selected
                    piece.deselect()  # If so, deselect the piece, change state to waiting, and end the loop
                    self.selected = None
                    self.state = 'waiting'
                    break

        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT:
                self.selected.rotate_ccw()
            if event.key == pygame.K_RIGHT:
                self.selected.rotate_cw()
            

    def end_loop(self, events):
        """
        The game has ended; display the winner
        """
        pass


    """
    Advances to the next player
    """
    def next_player(self):
        if self.player.number == 1:
            self.player = player_2
        elif self.player.number == 2:
            self.player = player_3
        elif self.player.number == 3:
            self.player = player_4
        elif self.player.number == 4:
            self.player = player_1


    """
    This function will call other helper functions to handle input events accordingly, depending on the game state
    """
    def handle_events(self, events):
        # Call the proper function, depending on the game state
        if self.state == 'start':
            self.start_loop(events)
        elif self.state == 'waiting':
            self.waiting_loop(events)
        elif self.state == 'turn':
            self.turn_loop(events)
        elif self.state == 'end':
            self.end_loop(events)


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

    # Create players
    player_1 = Player(1, Color.BLUE)
    player_2 = Player(2, Color.YELLOW)
    player_3 = Player(3, Color.RED)
    player_4 = Player(4, Color.GREEN)

    # The player whose turn it currently is
    game_state.player = player_1

    # Draw player 1's pieces; they go first
    for piece in game_state.player.tiles_set:
        piece.draw_piece(pieces_surface)

    screen.blit(pieces_surface, (800, 0))

    pygame.display.flip()

    # Game loop
    while True:
        # Update the board every frame
        timer.tick(60)
        board.draw()
        screen.blit(board.get_surface(), (BOARD_WIDTH//2-board.get_surface().get_width()//2,
                                          BOARD_HEIGHT//2-board.get_surface().get_height()//2))
        clear_set(pieces_surface)  # clear any already-placed pieces before drawing again
        for piece in game_state.player.tiles_set:
            piece.draw_piece(pieces_surface)
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
