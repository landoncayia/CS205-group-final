import sys
import pygame
import pygame.locals
import random
from board import Board
from board import create_set
from piece import Piece
from piece import Shape
from tile import Color
from tile import Tile

# dimensions of the board
BOARD_WIDTH, BOARD_HEIGHT = 800, 800
# order of play: 1 (Blue) -> 2 (Yellow) -> 3 (Red) -> 4 (Green)
# dict used to go to next color in order of play, as above
NEXT_COLOR = {Color.BLUE: Color.YELLOW, Color.YELLOW: Color.RED,
              Color.RED: Color.GREEN, Color.GREEN: Color.BLUE}


class Player:
    def __init__(self, number, color, is_human):
        """
        An instance of a player; each player has:
        * Number
        * Color
            1: Blue, 2: Yellow, 3: Red, 4: Green if there are four players
        * Set of tiles that they can place on the board
        * Score
        * Human vs. Computer: if True, player is a human; if False, controlled by our "A.I" function
        """
        #  These are the starting positions (in pixels) for the set of pieces that the player can select from
        start_x = 10
        start_y = 30
        self.number = number
        self.color = color
        self.tiles_set = create_set(start_x, start_y, color)
        self.piece_class_rem = {1: 1, 2: 1, 3: 2, 4: 5, 5: 12}
        self.score = -89  # Players start with -89 points, which goes up as pieces are played
        self.is_human = is_human  # Defaults to human, because there is always at least one human player
        self.placeable_pieces = 5
        self.passed_last = False
    
    # selects piece randomly from top 1/2 of the list
    # since pieces are ordered by number of tiles, it's picking from the pieces with the most tiles
    # after 10 tries if it can't find one with a valid move, it goes through the entire list and searches for a piece that works
    def select_piece(self):
        placed = False
        found = False
        num_tries = 0
        
        while not found and num_tries < 10:
            # Choose piece randomly from the top 1/2 in size
            choice_idx = random.randint(len(self.tiles_set)//2, len(self.tiles_set)-1)
            game_state.selected = self.tiles_set[choice_idx]
            game_state.selected.select()
            found = self.place_tile(choice_idx)
            game_state.selected.deselect()
            game_state.selected = None
            num_tries += 1
        
        piece_option = len(self.tiles_set)-1
        while piece_option >= 0 and not found:
            #go through the rest of the list and find one that works
            game_state.selected = self.tiles_set[piece_option]
            game_state.selected.select()
            found = self.place_tile(piece_option)
            game_state.selected.deselect()
            game_state.selected = None
            piece_option -= 1

        if not found:
            # If no piece was placed, the A.I. passes
            self.passed_last = True
            pygame.time.delay(1500)
            game_state.next_player()

    def place_tile(self, selected_idx):
        found = False
        for row in board.get_tiles():
            for tile in row:
                if not found:
                    if board.is_valid_tile(self.tiles_set, game_state.selected, tile.board_x, tile.board_y):
                        found = True
                        board.add_piece(game_state.selected, tile.board_x, tile.board_y)
                        self.piece_class_rem[game_state.selected.get_num_tiles()] -= 1
                        self.score += game_state.selected.get_num_tiles()
                        self.tiles_set.pop(selected_idx)
                         # Below are some additional scoring rules
                        if not self.tiles_set:
                            # If player has placed all their pieces (list empty), +15 points
                            self.score += 15
                            if game_state.selected.shape == Shape.ONE:
                                # If the last piece played is the single square piece, +5 points
                                self.score += 5
                        game_state.selected.deselect()
                        game_state.state = 'waiting'
                        self.passed_last = False  # Player did not pass; ensure game does not end
                        game_state.next_player()  # Go to next player
                        placed = True
                    tile.deselect()
        return found


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
        self.state = 'start'            # 'start' is our initial state, where the number of players is selected
        self.num_players = 0            # 2 or 4 for our implementation; some combination of humans and computers
        self.num_humans = 0             # 1, 2, or 4 human players
        self.player = None              # The current player
        self.selected = None            # currently selected piece, if any
        self.valid_moves = True

    def start_loop(self):
        """
        Beginning of game, in which the title is displayed and the number of human players is specified
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Left mouse button pressed, get mouse position
            x, y = pygame.mouse.get_pos()  # (x, y) where x and y are the number of pixels away from the top-left corner
            # Button coordinates and size
            x_one, y_one = 400, 550
            x_two, y_two = 675, 550
            x_four, y_four = 950, 550
            size = 150
            if x_one < x < x_one+size and y_one < y < y_one+size:
                # 1 human + 1 computer = 2 players
                self.num_humans = 1
                self.num_players = 2
            if x_two < x < x_two+size and y_two < y < y_two+size:
                # 2 humans + 0 computers = 2 players
                self.num_humans = 2
                self.num_players = 2
            if x_four < x < x_four+size and y_four < y < y_four+size:
                # 4 humans + 0 computers = 4 players
                self.num_humans = 4
                self.num_players = 4
            self.state = 'waiting'

    def waiting_loop(self):
        """
        We are waiting on whomever's turn it currently is to select a piece for placement on the board
        Allow players to select pieces by clicking on them; we will have to figure this out geometrically with Echo's code
        """
        if self.player != None:
            if not self.player.is_human:
                # A.I. here; stay in waiting state
                self.player.select_piece()
            else:
                if self.valid_moves_left():
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        # Left mouse button pressed, get mouse position
                        x, y = pygame.mouse.get_pos()  # (x, y) where x and y are the number of pixels away from the top-left corner
                        for piece in self.player.tiles_set:  # Go through each piece in the tile set that is currently on-screen
                            for row in piece.tiles_array:  # Go through each row in the tile array
                                for tile in row:
                                    if tile is not None:
                                        tile_x, tile_y = tile.get_location()  # Get the x, y coordinates of the tile (top-left)
                                        if 800 + tile_x < x < 800 + tile_x + 30 and tile_y < y < tile_y + 30:
                                            # Check if the mouse click location matches the range of this tile
                                            # If so, select the piece, change state to turn, and end the loop
                                            piece.select()
                                            self.selected = piece
                                            self.display_valid_moves()
                                            self.state = 'turn'
                        if 1050 < x < 1150 and 675 < y < 725:
                            # Pass button was pressed
                            self.player.passed_last = True  # Player passed, so set this to reflect that for game-end purposes
                            self.next_player()
                else:
                    self.state = 'end'

    def turn_loop(self):
        """
        We are waiting on whomever's turn it currently is to place their piece somewhere on the board
        This will involve a calculation as to whether a move is legal or not
        Additionally, players can right-click to put their piece back and select another.
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Left mouse button pressed, get position
            x, y = pygame.mouse.get_pos()
            # Place piece
            placed = False
            for row in board.tiles:
                for tile in row:
                    if 30+tile.x < x < 60+tile.x and 30+tile.y < y < 60+tile.y and not placed:
                        if board.is_valid_tile(self.player.tiles_set, self.selected, tile.board_x, tile.board_y):
                            board.add_piece(self.selected, tile.board_x, tile.board_y)
                            self.player.piece_class_rem[self.selected.get_num_tiles()] -= 1
                            self.player.score += self.selected.get_num_tiles()
                            self.player.tiles_set.remove(self.selected)
                            # Below are some additional scoring rules
                            if not self.player.tiles_set:
                                # If player has placed all their pieces (list empty), +15 points
                                self.player.score += 15
                                if self.selected.shape == Shape.ONE:
                                    # If the last piece played is the single square piece, +5 points
                                    self.player.score += 5
                            self.selected.deselect()
                            self.state = 'waiting'
                            self.player.passed_last = False  # Player did not pass; ensure game does not end
                            self.next_player()  # Go to next player
                            placed = True
                    tile.deselect()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            # Right mouse button pressed; unselect current piece and go back to waiting state
            for piece in self.player.tiles_set:  # Go through each piece in the tile set that is currently on-screen
                if piece.selected:  # Check if the piece is selected
                    piece.deselect()  # If so, deselect the piece, change state to waiting, and end the loop
                    self.selected = None
                    self.state = 'waiting'
                    break

        # flip and rotate keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.selected.rotate_ccw()
                self.display_valid_moves()
            if event.key == pygame.K_RIGHT:
                self.selected.rotate_cw()
                self.display_valid_moves()
            if event.key == pygame.K_UP:
                self.selected.flip_vert()
                self.display_valid_moves()
            if event.key == pygame.K_DOWN:
                self.selected.flip_horiz()
                self.display_valid_moves()

    def next_player(self):
        # Advances to the next player
        if self.player == player_1:
            self.player = player_2
        elif self.player == player_2:
            self.player = player_3
        elif self.player == player_3:
            self.player = player_4
        elif self.player == player_4:
            self.player = player_1

    def handle_events(self):
        # This function will call other helper functions to handle input events accordingly, depending on the game state
        # Call the proper function, depending on the game state
        if self.state == 'start':
            self.start_loop()
        elif self.state == 'waiting':
            self.waiting_loop()
        elif self.state == 'turn':
            self.turn_loop()
        # If state is end, no need to have a loop here, just wait for user to quit

    def valid_moves_left(self):
        """
        This function will determine if there are any valid moves left for the player
        """
        for piece in self.player.tiles_set:
            for row in board.get_tiles():
                for tile in row:
                    if board.is_valid_tile(self.player.tiles_set, piece, tile.board_x, tile.board_y):
                        return True
        return False

    def display_valid_moves(self):
        for board_row in board.tiles:
            for tile in board_row:
                if(board.is_valid_tile(self.player.tiles_set, self.selected, tile.board_x, tile.board_y)):
                    tile.select()
                else:
                    tile.deselect()


def draw_start_screen():
    start_surface.fill(Color.BG_GREY.value)
    title_font = pygame.font.SysFont('Ubuntu', 72, bold=True)
    subtitle_font = pygame.font.SysFont('Ubuntu', 48, bold=True)
    regular_font = pygame.font.SysFont('Ubuntu', 28, bold=True)
    title_text = title_font.render('Blokus', True, Color.EMPTY_GREY.value)
    subtitle_text = subtitle_font.render('Landon Cayia, Isabelle Francke, and Echo Norcott',
                                         True, Color.EMPTY_GREY.value)
    start_surface.blit(title_text, (650, 200))
    start_surface.blit(subtitle_text, (260, 300))
    select_players_msg = regular_font.render('Select the number of (human) players:', True, Color.EMPTY_GREY.value)
    start_surface.blit(select_players_msg, (500, 450))
    pygame.draw.rect(start_surface, Color.EMPTY_GREY.value, (400, 550, 150, 150))
    text_one_p = title_font.render('1', True, Color.BG_GREY.value)
    start_surface.blit(text_one_p, (460, 580))
    pygame.draw.rect(start_surface, Color.EMPTY_GREY.value, (675, 550, 150, 150))
    text_two_p = title_font.render('2', True, Color.BG_GREY.value)
    start_surface.blit(text_two_p, (735, 580))
    pygame.draw.rect(start_surface, Color.EMPTY_GREY.value, (950, 550, 150, 150))
    text_four_p = title_font.render('4', True, Color.BG_GREY.value)
    start_surface.blit(text_four_p, (1010, 580))
    text_one_p_color = regular_font.render('Player: blue and yellow', True, Color.EMPTY_GREY.value)
    start_surface.blit(text_one_p_color, (250, 720))
    text_two_p_color = regular_font.render('Player 1: blue and yellow', True, Color.EMPTY_GREY.value)
    start_surface.blit(text_two_p_color, (600, 720))
    text_two_p_color_2 = regular_font.render('Player 2: red and green', True, Color.EMPTY_GREY.value)
    start_surface.blit(text_two_p_color_2, (600, 770))


def draw_end_screen():
    """
    The game has ended; display the winner
    """
    font = pygame.font.SysFont('Ubuntu', 30, bold=True)
    text_game_over = font.render('GAME OVER', True, Color.EMPTY_GREY.value)
    score_surface.blit(text_game_over, (800, 0))
    player_index = {0: 'Player 1', 1: 'Player 2', 2: 'Player 3', 3: 'Player 4'}
    final_scores = [player_1.score, player_2.score, player_3.score, player_4.score]
    highest_score = max(final_scores)
    if final_scores.count(highest_score) == 1:
        winning_player_idx = final_scores.index(highest_score)
        text_winner = font.render(player_index[winning_player_idx] + ' wins, with ' + str(highest_score) + ' points!',
                                  True, Color.EMPTY_GREY.value)
        score_surface.blit(text_winner, (1000, 0))


def create_players():
    """
    This function creates human/computer players, depending on what the user selected in the beginning
    In our implementation, a "player" represents one of the colored sets of pieces; the game can be played
    in such a way that one player controls multiple "players"
    Options include:
        * 1 Player:  1 human vs 1 computer
        * 2 Players: 2 humans
        * 4 Players: 4 humans
    :return: p1, p2, p3, p4: four player instances, some mix of human(s)/computer(s)
    """
    if game_state.num_humans == 1:
        #  Blue and yellow are the human's (1) colors; red and green are the computer's (2) colors
        p1 = Player(1, Color.BLUE, is_human=True)
        p2 = Player(1, Color.YELLOW, is_human=True)
        p3 = Player(2, Color.RED, is_human=False)
        p4 = Player(2, Color.GREEN, is_human=False)
    elif game_state.num_humans == 2:
        #  Blue and yellow are the human's (1) colors; red and green are the other human's (2) colors
        p1 = Player(1, Color.BLUE, is_human=True)
        p2 = Player(1, Color.YELLOW, is_human=True)
        p3 = Player(2, Color.RED, is_human=True)
        p4 = Player(2, Color.GREEN, is_human=True)
    else:  # 4 players
        #  If there are four human players each player gets a separate color
        p1 = Player(1, Color.BLUE, is_human=True)
        p2 = Player(2, Color.YELLOW, is_human=True)
        p3 = Player(3, Color.RED, is_human=True)
        p4 = Player(4, Color.GREEN, is_human=True)
    return p1, p2, p3, p4


def draw_scores():
    """
    This function draws each player's scores above the board
    """
    font = pygame.font.SysFont('Ubuntu', 24)
    total_scores = {}  # dictionary, where keys are player numbers and values are their total scores
    # Go through each player, and if necessary, sum up the scores (necessary in two player mode, since one person
    #                                                              controls multiple players)
    if game_state.num_players == 2:
        # P1's score is blue, P2's score is red
        player_colors = [Color.BLUE.value, Color.RED.value]
    else:  # num_players == 4
        player_colors = [Color.BLUE.value, Color.YELLOW.value, Color.RED.value, Color.GREEN.value]
    for player in all_players:
        if player.number not in total_scores:
            total_scores[player.number] = 0
        total_scores[player.number] += player.score
    for p in range(game_state.num_players):
        #  Should run four times, because there are four players
        text_score = font.render("Player "+str(p+1)+": "+str(total_scores[p+1]), True, player_colors[p])
        #  Draw along the bottom of the board, moving 200 pixels for each player
        score_surface.blit(text_score, (p*200, 0))


def draw_pass_button():
    """
    Draws the pass button after all the pieces, so that a player may choose to pass.
    """
    font = pygame.font.SysFont('Ubuntu', 28, bold=True)
    button_text = font.render('PASS', True, game_state.player.color.value)
    pygame.draw.rect(pieces_surface, Color.EMPTY_GREY.value, (250, 675, 100, 50))
    pieces_surface.blit(button_text, (270, 685))


def clear_window():
    """
    This function runs every frame to wipe out what was on the board before with a grey rectangle
    """
    pygame.draw.rect(screen, Color.BG_GREY.value, (0, 0, 1450, 900))
    pygame.draw.rect(pieces_surface, Color.BG_GREY.value, (0, 0, 700, 800))
    pygame.draw.rect(score_surface, Color.BG_GREY.value, (0, 0, 1400, 50))


if __name__ == '__main__':
    pygame.init()
    window = (1450, 900)
    screen = pygame.display.set_mode(window)
    pygame.display.set_caption('Blokus')

    #  Main screen
    screen.fill(Color.BG_GREY.value)

    #  Create the game state object
    game_state = GameState()

    # Start surface
    start_surface = pygame.Surface((1450, 900))
    draw_start_screen()

    #  Create other surfaces
    pieces_surface = pygame.Surface((700, 800))
    score_surface = pygame.Surface((1400, 50))

    #  Fill surfaces with grey color
    pieces_surface.fill(Color.BG_GREY.value)
    score_surface.fill(Color.BG_GREY.value)

    timer = pygame.time.Clock()

    #  Create and draw a board, then put it on the screen
    board = Board()
    board.draw()

    # Initialization loop
    while game_state.num_players == 0:  # this is the initial value, so loop with this until it is modified
        timer.tick(60)
        clear_window()
        screen.blit(start_surface, (0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                raise SystemExit
            if event.type == pygame.QUIT:
                raise SystemExit
            game_state.handle_events()

    # Initializes players, based on the user's selection
    player_1, player_2, player_3, player_4 = create_players()
    #  The player whose turn it currently is
    game_state.player = player_1
    all_players = [player_1, player_2, player_3, player_4]  # list of all players to make score updating simpler

    # Game loop, after players are initialized (this is 'waiting', 'turn', or 'end')
    while True:
        # Update the board every frame
        timer.tick(60)
        clear_window()  # clear the board every frame
        # If all players passed on their last turn, assume no further moves are possible and end the game
        if all([p.passed_last for p in all_players]):
            game_state.state = 'end'
        if game_state.state == 'end':
            # Final scores are contained within score surface
            draw_end_screen()
        # waiting or turn
        board.draw()
        screen.blit(board.get_surface(), (25, 25))
        for piece in game_state.player.tiles_set:
            piece.draw_piece(pieces_surface)
        draw_scores()
        draw_pass_button()
        screen.blit(pieces_surface, (800, 0))
        screen.blit(score_surface, (30, 825))  # Scores below board

        pygame.display.flip()

        # Escape quits the game
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                raise SystemExit
            if event.type == pygame.QUIT:
                raise SystemExit
            game_state.handle_events()
