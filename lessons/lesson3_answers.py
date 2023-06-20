board = [1,2,3,4,5,6,7,8,9]
player = "x"



def display_board():
  print(board[0], " | ", board[1], " | ", board[2])
  print("-"*14)
  print(board[3], " | ", board[4], " | ", board[5])
  print("-"*14)
  print(board[6], " | ", board[7], " | ", board[8])



for x in range(len(board)):
  pick = int(input("Player"+player+": pick a tic tac toe position 1-9: "))
  print("player pick: ", pick)


  #update the game board with the player pick
  board[pick-1] = player
  #print(board)
  display_board()
  
  if player == "x":
    player = "o"
  else:
    player = "x"