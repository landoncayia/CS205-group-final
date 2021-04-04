import sys
import pygame
import pygame.locals
from board import Board
from piece import Piece
from piece import Shape
from tile import Color
from tile import Tile

BOARD_WIDTH, BOARD_HEIGHT = 800, 800
NEXT_PLAYER = {'b': 'y', 'y': 'r', 'r': 'g', 'g': 'b'} # dict used to go to next player in order of play: Blue -> Yellow -> Red -> Green


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


if __name__ == '__main__':
    pygame.init()
    window = (1200, 800)
    screen = pygame.display.set_mode(window)
    pygame.display.set_caption('Blokus')
    screen.fill(Color.BG_GREY.value)
    piecesSurface = pygame.Surface((400, 800))

    # Create and draw a board, then put it on the screen
    board = Board(window)
    # TESTING - REMOVE AFTER
    testpiece = Piece(Shape.Z4, Tile(10,10,Color.BLUE))
    board.add_piece(testpiece)
    board.draw()
    screen.blit(board.get_surface(), (BOARD_WIDTH//2-board.get_surface().get_width()//2,
                                      BOARD_HEIGHT//2-board.get_surface().get_height()//2))

    # DISPLAY PIECES
    piecesSurface.fill(Color.BG_GREY.value)

    # create set of pieces to display
    # tiles_set = create_set(0, 50, Color.BLUE)
    # # testpiece.draw_piece_outside_board(piecesSurface)

    start_x = 10
    start_y = 30
    set_color = Color.BLUE
    tiles_set = create_set(start_x, start_y, set_color)

    for piece in tiles_set:
        piece.draw_piece_outside_board(piecesSurface)

    screen.blit(piecesSurface, (800, 0))
    # full_set = create_set(Color.BLUE, 900, 50)

    # testpiece.draw(piecesSurface)
    # while (i < (len(full_set) / 2)):
    #     full_set[i].draw(piecesSurface)

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
    '''
    state = 'waiting'   # NOTE: This should be changed to 'start' later, this is just for testing
    player = 'b'        # NOTE: Blue player goes first

    # Game loop
    while True:
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
                # TODO: Find out which piece the player has clicked on and highlight it

        elif state == 'turn':
            '''
            We are waiting on whomever's turn it currently is to place their piece somewhere on the board
            This will involve a calculation as to whether a move is legal or not; perhaps in board we could have 'verify_legal'?
            Additionally, players can right-click to put their piece back and select another.
            '''
            if mouse[0]:
                # Left-click; get position
                x, y = pygame.mouse.get_pos()
                # Place piece
                # Remove piece from player's pieces
                player = NEXT_PLAYER[player] # Go to next player
            
            elif mouse[2]:
                # Right-click; unselect current piece and go back to waiting state
                # unselect function
                state = 'waiting'

            elif keys[pygame.K_R]:
                # Rotate piece for Isabelle
                pass
        
        elif state == 'end':
            '''
            The game has ended; display the winner
            '''
            pass
    
    pygame.quit()
