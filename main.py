import numpy as np

ROW = 6
COL = 7

def create_board():
  board = np.zeros((ROW,COL))
  return board

def drop_piece(board, row, col, piece):
  board[row][col] = piece

def is_valid_location(board, col):
  return board[ROW-1][col] == 0

def get_next_open_row(board, col):#hello
  for r in range(ROW):
    if board[r][col] == 0:
      return r

def print_board(board):
  print(np.flip(board, 0))
  
def winning_move(board, piece):
  # Check horizontal locations for win
  for c in range(COL-3):
    for r in range(ROW):
      if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
        return True
      
  # Check for Vertical locations for win
  for c in range(COL):
    for r in range(ROW-3):
      if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
        return True
      
board = create_board()
print_board(board)
game_over = False
turn = 0

while not game_over:
  # Player 1 input
  if turn == 0:
    col = int(input("Player 1 make your move:"))
    
    if(is_valid_location(board, col)):
      row = get_next_open_row(board, col)
      drop_piece(board, row, col, 1)
      
      if winning_move(board, 1):
        print("Congratulations Player 1!!!")
        game_over = True
    
  # Player 2 input
  else:
    col = int(input("Player 2 make your move:"))
    
    if(is_valid_location(board, col)):
      row = get_next_open_row(board, col)
      drop_piece(board, row, col, 2)
    
  print_board(board)
  
  turn += 1
  turn = turn % 2
   
