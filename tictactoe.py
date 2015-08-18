# TicTacToe Exercise for Quiqup
# Maria Stylianou @marsty5
# 16/8/2015
#
# Version 1: Computer does a random move (it was pretty dumb)
# Version 2: Computer does 'smart' moves
#
# What I would change - to discuss:
# --------------------------------
# - Put more logic in the step 4: Make a corner move (for the computer)
# - Is a list with 9 elements better than a list with three 3-element lists?
# - See if I can/should merge the methods "is_win_*" with the methods get_cell_to_complete_*
# -- where * = {horizontally, vertically, diagonally}
# - Testing is missing
#
# I can jump on a call/skype anytime to discuss it.
# It was fun! Thank you!

import random

DIMENSION = 3
MAX_CELL_NUMBER = 9
USER_LETTER = 'X'
COMPUTER_LETTER = 'O'
CENTERED_CELL = 5

def init_board():
  # Why a list of 3 rows/lists?
  # It makes it easier when I want to check for winning rows/columns
  board = []
  begin = end = 1
  for dim in range(1, DIMENSION+1):
    begin = end
    end = DIMENSION * dim + 1
    row = [x for x in range(begin, end)]
    board.append(row)
  return board

def print_instructions():
  print "\n---------------- TIC TAC TOE ----------------"
  print "Yo! Let's play. You are X and I am O."
  print "Choose a cell to put X by entering its number."
  print "I'm not totally dumb, so pay attention :p"
  print "You go first. Good luck!"
  print "\n"

def print_board(board):
  print "\t"
  for row in board:
    print '\t',' | '.join(map(str,row))
    print '\t', '---------'

def exit_if_board_full(board):
  if is_board_full(board) == True:
    print "Game over. We are both too cool for school B-) (or just lame...)"
    exit()

def is_board_full(board):
  for row in board:
    for cell in row:
      if cell != 'X' and cell != 'O':
        return False
  return True

def get_user_move(board):
  while True:
    move = get_int_cell_value()
    exit_upon_request(move)
    if is_cell_available(board, move) == True:
      return move
    else:
      print "This position is taken!"

def get_int_cell_value():
  while True:
    try:
      intCell = int(input("Your turn (1-9): "))
    except NameError:
      continue
    else:
      if intCell < 0 or intCell > MAX_CELL_NUMBER:
        continue
      else:
        return intCell

def exit_upon_request(cell):
  if cell == 0:
    print "Bye :)"
    exit()

def is_cell_available(board, cell):
  for row in board:
    if cell in row:
      return True
  return False

def get_row(board, move):
  for row in board:
    if move in row:
      return board.index(row)
  return -1

def get_column(board, move):
  for row in board:
    if move in row:
      return row.index(move)
  return -1

def make_move(board, row, column, letter):
  board[row][column] = letter

def is_winner_move(board, currentRow, currentColumn, letter):
  takenCells = 0
  winHorizontal = is_win_horizontally(board, currentRow, letter)
  winVertical = is_win_vertically(board, currentColumn, letter)
  winDiagonal = is_win_diagonally(board, letter)
  if winHorizontal == True or winVertical == True or winDiagonal == True:
    return True

def is_win_horizontally(board, currentRow, letter):
  takenCells = 0
  for cell in board[currentRow]:
    if cell == letter:
      takenCells += 1
  if takenCells == DIMENSION:
    return True
  return False

def is_win_vertically(board, currentColumn, letter):
  takenCells = 0
  for row in board:
    if row[currentColumn] == letter:
      takenCells += 1
  if takenCells == DIMENSION:
    return True
  return False

# It can be improved
def is_win_diagonally(board, letter):
  diagonalOne = [board[0][0], board[1][1], board[2][2]]
  diagonalTwo = [board[0][2], board[1][1], board[2][0]]

  takenCells = 0
  for cell in diagonalOne:
    if cell == letter:
      takenCells += 1
  if takenCells == DIMENSION:
    return True

  takenCells = 0
  for cell in diagonalTwo:
    if cell == letter:
      takenCells += 1
  if takenCells == DIMENSION:
    return True

  return False

def get_computer_random_move(board):
  while True:
    move = random.randint(1, MAX_CELL_NUMBER)
    if is_cell_available(board, move) == True:
      return move

# It can be improved :p
def get_computer_move(board):
  # How can I make it a bit smarter than totally random?
  # 1. Check for winner moves; aka, a move that can make me win - DONE
  # 2. Check for defence moves; aka, don't let the user win - DONE
  # 3. Make a move in a corner, if available - DONE
  # 4. Make a move in the center, if available - DONE
  # 5. Random - DONE

  while True:
    move = get_winner_move(board) # Step 1 - winner
    if move == 0:
      move = get_defence_move(board) # Step 2 - defence
      if move == 0:
        move = get_corner_move(board) # Step 3 - corner
        if move == 0:
          move = get_center_move(board) # Step 4 - center
          if move == 0:
            move = get_random_move(board) # Step 5 - random
            if is_cell_available(board, move) == True:
              return move
    return move

def get_winner_move(board):
  move = get_cell_to_complete_horizontally(board, COMPUTER_LETTER, USER_LETTER)
  if move == 0:
    move = get_cell_to_complete_vertically(board, COMPUTER_LETTER, USER_LETTER)
    if move == 0:
      move = get_cell_to_complete_diagonally(board, COMPUTER_LETTER, USER_LETTER)
  if move != 0:
    print "Going for my winner move."
  return move

def get_cell_to_complete_horizontally(board, myLetter, opponentLetter):
  for row in board:
    if row.count(myLetter) == 2:
      for cell in row:
        if cell != myLetter and cell != opponentLetter:
          return cell
  return 0

def get_cell_to_complete_vertically(board, myLetter, opponentLetter):
  for column in range(0,3):
    takenCells = 0
    cell = 0
    for row in board:
      if row[column] == myLetter:
        takenCells+=1
      else:
        cell = row[column]
    if takenCells == 2 and cell != opponentLetter:
      return cell
  return 0

def get_cell_to_complete_diagonally(board, myLetter, opponentLetter):
  diagonalOne = [board[0][0], board[1][1], board[2][2]]
  diagonalTwo = [board[0][2], board[1][1], board[2][0]]

  takenCells = 0
  for cell in diagonalOne:
    if cell == myLetter:
      takenCells += 1
    else:
      move = cell
  if takenCells == 2 and move != opponentLetter:
    return move

  takenCells = 0
  for cell in diagonalTwo:
    if cell == myLetter:
      takenCells += 1
    else:
      move = cell
  if takenCells == 2 and move != opponentLetter:
    return move

  return 0

def get_defence_move(board):
  move = get_cell_to_complete_horizontally(board, USER_LETTER, COMPUTER_LETTER)
  if move == 0:
    move = get_cell_to_complete_vertically(board, USER_LETTER, COMPUTER_LETTER)
    if move == 0:
      move = get_cell_to_complete_diagonally(board, USER_LETTER, COMPUTER_LETTER)
  if move != 0:
    print "Going for my defence move."
  return move

def get_corner_move(board):
  for corner in [1,3,7,9]:
    if is_cell_available(board, corner) == True:
      print "Going for my corner move."
      return corner
  return 0

def get_center_move(board):
  if is_cell_available(board, 5) == True:
    print "Going for my center move."
    return 5
  return 0

def get_random_move(board):
  while True:
    move = random.randint(1, MAX_CELL_NUMBER)
    if is_cell_available(board,move) == True:
      print "Going for my random move."
      return move

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Let's go!
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
board = init_board()
print_instructions()
iteration = 0

while True:
  iteration += 1
  print "\nRound", iteration, "(Type 0 or Ctrl+C to exit)."
  print_board(board)

  userMove = get_user_move(board)
  userMoveRow = get_row(board, userMove)
  userMoveColumn = get_column(board, userMove)
  make_move(board, userMoveRow, userMoveColumn, USER_LETTER)

  if is_winner_move(board, userMoveRow, userMoveColumn, USER_LETTER) == True:
    print_board(board)
    print "*** Good one - Congrats! ***"
    exit()

  exit_if_board_full(board)
  # computerMove = get_computer_random_move(board)
  computerMove = get_computer_move(board)
  computerMoveRow = get_row(board, computerMove)
  computerMoveColumn = get_column(board, computerMove)
  make_move(board, computerMoveRow, computerMoveColumn, COMPUTER_LETTER)
  print "My turn:", computerMove
  if is_winner_move(board, computerMoveRow, computerMoveColumn, COMPUTER_LETTER) == True:
    print_board(board)
    print "*** Sorry for that - Congrats to me! ***"
    exit()

### THE END
