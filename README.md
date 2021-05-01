# LC-EN-IF CS205 Final Project: Blokus

We implemented the board game "Blokus" in Python, primarily using the pygame module. We hope you enjoy it!

[Trello board link](https://trello.com/b/i069mBvd/final-project)

## Program Structure

* Module `driver.py`
    * `Player` class: contains information about the players; we implemented these in a way such that there are always
    four players, one for each color; if there are only two actual players, they each control two of the player
    instances, and the scores are summed.
    * `GameState` class: contains information about the current state of the game, as well as loops for what the game
    should do depending on the current state of the game.
    * "Helper" functions for displaying elements and performing functions
    * `main` function, which contains the game loops that wait for user interaction
* Module `board.py`
    * `Board` class: contains necessary details and functions for controlling the game board
    * `create_set` function: creates the set of pieces that each player can select, displayed to the right of the board
* Module `piece.py`
    * `Shape` class (enum): an enumerated data type used to represent piece shapes in a clearer manner
    * `Piece` class: contains necessary details and functions for pieces, which are collections of tiles that players can
    select and place on the board
        * This class contains methods to rotate and flip pieces using the four arrow keys; these are called `rotate_cw`,
        `rotate_ccw`, `flip_vert`, and `flip_horiz`
* Module `tile.py`
    * `Color` class (enum): an enumerated data type used to name colors that we want to reuse many times
    * `Tile` class: contains necessary details and functions for tiles, which are 30 x 30 squares that make up pieces,
    and the board
      
## Game Rules

Source: [UltraBoardGames.com | Blokus Game Rules](https://www.ultraboardgames.com/blokus/game-rules.php)

### Game Components

* a board of 400 squares
* 84 pieces in four different colors (21 pieces per color)
    * each of the 21 pieces for a color is of a different shape
        * 1 piece has one square
        * 1 piece has two squares
        * 2 pieces have three squares
        * 5 pieces have four squares
        * 12 pieces have five squares
    
### Object of the Game

Each player has to fit as many of his/her 21 pieces on the board as possible.

### Gameplay

Each player chooses a color and places that set of 21 pieces in front of his/her side of the board. The order of play
is as follows: blue, yellow, red, green.
* The first piece played by each player must cover a corner square.
* Each new piece must touch at least one other piece of the same color, but only at the corners; pieces of the same
color cannot be in contact along an edge.
* There are no restrictions on how many pieces of different colors may be in contact with each other.
* Once a piece has been placed on the board it cannot be moved during subsequent turns.
* A player may choose to pass on any turn, without placing a piece.

### End of the Game

The game ends when all players are blocked from laying down any more of their pieces. This also includes any players
who may have placed all of their pieces on the board.

Scores are tallied, and the player with the highest score is the winner.

#### Scoring

* Each square unit of a player's remaining pieces at the end of the game counts as -1 point. It follows that whoever
has the negative value of points closest to zero wins. To make it easier to keep track of scores, we implemented score
counters that begin at -89 (1x1 + 1x2 + 2x3 + 5x4 + 12x5) = 1 + 2 + 6 + 20 + 60 = 89.
* A player earns +15 points if all his/her pieces have been placed on the board.
* A player earns +5 points if the last piece placed on the board was the smallest piece (one square).
    * The maximum score that a player can earn is +20, if both bonuses are earned.
    * If there are two players rather than four, the initial scores are -89*2 = -178, and the maximum points possible
    is +40 for each player.

## How to Play Our Implementation

To play our game,

1. Ensure that all files, including `driver.py`, `board.py`, `piece.py`, and `tile.py` are all in the
same directory (this should happen automatically if this repository is cloned), and then run `driver.py`.
2. You will be presented with the title screen, and three options for players; these represent the following scenarios:
    * **1 Player**: 1 human player and 1 computer/bot player, where the person controls blue and yellow, and the
      computer controls red and green
    * **2 Players**: 2 human players, where one person controls blue and yellow, and the other controls red and green
    * **4 Players**: 4 human players, where each person controls a different color
3. Once the number of players is selected, you will be presented with an empty board, all player scores, the first
player's (blue's) pieces, and a pass button. Players can select pieces and place them on the board, and can rotate or
flip pieces to place them on the board as they wish. Details on how to control the game can be found below.
4. After a player makes his/her move, gameplay moves to the next player. This continues until every player has placed
all their pieces or every player passes.

### Controls

* *Selecting pieces, pass a turn, player number selection*: **Left-click** (piece is highlighted when selected)
  * To pass a turn, **left-click** the pass button once
* *Deselecting a piece*: **Right-click** (***NOTE***: only one piece may be selected at a time; in order to select another
piece, players must deselect the currently-selected piece)
* *Rotate the selected piece clockwise by 90°*: **Right arrow key**
* *Rotate the selected piece counterclockwise by 90°*: **Left arrow key**
* *Flip the selected piece vertically*: **Up arrow key**
* *Flip the selected piece horizontally*: **Down arrow key**
