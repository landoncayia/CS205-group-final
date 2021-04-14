import sys
import pygame
import pygame.locals
from board import Board
from board import create_set
from piece import Piece
from piece import Shape
from tile import Color
from tile import Tile

BOARD_WIDTH, BOARD_HEIGHT = 800, 800
NEXT_PLAYER = {'b': 'y', 'y': 'r', 'r': 'g', 'g': 'b'}  # dict used to go to next player in order of play: Blue -> Yellow -> Red -> Green
NEXT_COLOR = {Color.BLUE: Color.YELLOW, Color.YELLOW: Color.RED,  # dict used to go to next color in order of play, as above
              Color.RED: Color.GREEN, Color.GREEN: Color.BLUE}

if __name__ == '__main__':
    pygame.init()
    window = (1200, 800)
    screen = pygame.display.set_mode(window)
    pygame.display.set_caption('Blokus')
    screen.fill(Color.BG_GREY.value)
    pieces_surface = pygame.Surface((400, 800))

    # Create and draw a board, then put it on the screen
    board = Board(window)

    board.draw()
    screen.blit(board.get_surface(), (BOARD_WIDTH//2-board.get_surface().get_width()//2,
                                      BOARD_HEIGHT//2-board.get_surface().get_height()//2))
    # END TESTING

    # DISPLAY PIECES
    pieces_surface.fill(Color.BG_GREY.value)

    start_x = 10
    start_y = 30
    set_color = Color.BLUE
    tiles_set = create_set(start_x, start_y, set_color)

    for piece in tiles_set:
        piece.draw_piece(pieces_surface)

    screen.blit(pieces_surface, (800, 0))

    pygame.display.flip()
    
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
    state = 'waiting'   # NOTE: This should be changed to 'start' later, this is just for testing
    player = 'b'        # NOTE: Blue player goes first
    selected = None 

    # Game loop
    while True:
        # Update the board every frame
        # Add frame rate here
        board.draw()
        screen.blit(board.get_surface(), (BOARD_WIDTH//2-board.get_surface().get_width()//2,
                                    BOARD_HEIGHT//2-board.get_surface().get_height()//2))
        for piece in tiles_set:
            piece.draw_piece_outside_board(pieces_surface)
        screen.blit(pieces_surface, (800, 0))
        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                raise SystemExit

        keys = pygame.key.get_pressed() # This is a dictionary, where each key has a value of 0 or 1 for pressed/not pressed.
        mouse = pygame.mouse.get_pressed() # This is a dictionary, where each mouse button has a value of 0 or 1 for pressed/not pressed.
        # mouse[0] is the left-click, mouse[1] is the middle click (scroll wheel), mouse[2] is the right-click

        if state == 'start':
            '''
            Beginning of game, in which number of players is specified. This will be part of Sprint Two
            We could ask the player to use the number keys on their keyboard to select the number of players; this will highlight squares on-screen
            Once they have selected their number of players, space could begin the game
            For now, ignore this
            '''
            pass

        elif state == 'waiting':
            '''
            We are waiting on whomever's turn it currently is to select a piece for placement on the board
            Allow players to select pieces by clicking on them; we will have to figure this out geometrically with Echo's code
            '''
            if mouse[0]:
                # Left-click; get position
                x, y = pygame.mouse.get_pos() # (x, y), where x and y are the number of pixels away from the top-left corner
                for piece in tiles_set: # Go through each piece in the tile set that is currently on-screen
                    for tile in piece.printing_tiles: # Go through each tile in the piece
                        tile_x, tile_y = tile.get_location() # Get the x, y coordinates of the tile (top-left)
                        if 800+tile_x < x < 800+tile_x+30 and tile_y < y < tile_y+30: # Check if the mouse click location matches the range of this tile
                            piece.select() # If so, select the piece, change state to turn, and end the loop
                            selected = piece
                            state = 'turn'
                            break

        elif state == 'turn':
            '''
            We are waiting on whomever's turn it currently is to place their piece somewhere on the board
            This will involve a calculation as to whether a move is legal or not; perhaps in board we could have 'verify_legal'?
            Additionally, players can right-click to put their piece back and select another.
            '''
            if mouse[0]:
                while state == 'turn':
                    # Left-click; get position
                    x, y = pygame.mouse.get_pos()
                    # Mouse over board hover
                    for piece in tiles_set:
                        if (piece.is_selected() == True):
                            current_piece = piece

                    selected_color = current_piece.get_tiles()[0].get_color()

                    board_tiles = board.get_tiles()
                    for tile in range(len(board_tiles)):
                        while board_tiles[tile].get_x() < x < board_tiles[
                            tile].get_x() + 30 and tile.get_y() < y < tile.get_y() + 30:
                            tile.set_color(selected_color)
                            screen.blit(board.get_surface(), (BOARD_WIDTH // 2 - board.get_surface().get_width() // 2,
                                                              BOARD_HEIGHT // 2 - board.get_surface().get_height() // 2))

                    # Place piece
                    # Remove piece from player's pieces
                    player = NEXT_PLAYER[player]  # Go to next player
                    set_color = NEXT_COLOR[set_color]  # Set next color
            
            elif mouse[2]:
                # Right-click; unselect current piece and go back to waiting state
                for piece in tiles_set: # Go through each piece in the tile set that is currently on-screen
                    for tile in piece.printing_tiles: # Go through each tile in the piece
                        if piece.selected: # Check if the piece is selected
                            piece.deselect() # If so, deselect the piece, change state to waiting, and end the loop
                            selected = None
                            state = 'waiting'
                            break

            elif keys[pygame.K_LEFT]:
                # Use the left arrow key to rotate counterclockwise
                selected.rotate_ccw()
            elif keys[pygame.K_RIGHT]:
                # Use the right arrow key to rotate clockwise
                selected.rotate_cw()
        
        elif state == 'end':
            '''
            The game has ended; display the winner
            '''
            pass
    
    pygame.quit()
