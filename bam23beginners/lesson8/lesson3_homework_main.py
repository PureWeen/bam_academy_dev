import random

#define board with 9 spots/input squares
#
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def printBoard():
  for index,i in enumerate(board):
    if(index%3==2):
      print(i)
      print("----------")
    else:
      print(i, end=" | ")
printBoard()  

# 1. randomly pick O's or X's turn (e.g. 0 or 1 random number)
# 2. determine who is the first , is it X or O
# 3. loop through players, starting at the first player above
# 4. get an input square to enter for this player, now for the next player
# 5. update the board with the player (X or O) for board spot selected
# 6. printBoard again, over and over until all squares are selected or winner
