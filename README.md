# LC-EN-IF-cs205-final

We are implementing the board game "Blokus" in Python, primarily using the pygame module.

## Game Rules

This will contain the rules of the game, once we actually implement them - this was not a Sprint One goal.

## How to Play Our Implementation (Sprint One)

Our game is run using 'driver.py'. Simply run this file, while ensuring that 'board.py', 'piece.py', and 'tile.py' are all in the same directory as it is. This should happen automatically if this repository is cloned.

Currently, our game only has the functionality of being able to run it, and see the board. The game should normally begin in a state so that the user can select how many people will be playing, but we have not made it there yet in Sprint One. For the purpose of demonstration, we have set the state as if blue, the first player, is taking his or her turn. The player is able to left-click any square of any piece on the right side of the window to select the entire piece, which highlights it. This only works for one piece, as this is the piece that the player would be placing on the board. If the player wishes to cancel his or her move, they can simply right-click anywhere to deselect the piece.

## Goals for Sprint Two:

- Refine the UI
- Game rules
- Enable players to rotate their selected piece with the left and right arrow keys
- Actually implement true turns for each player color
- Multiple numbers of players
- Clean up redundant parts of the code
- Create a simple AI for computer players