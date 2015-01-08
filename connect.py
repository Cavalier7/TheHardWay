# constants

height = 6
width = 7
player = 'X'
computer = '%'
space = 'O'
board = []

# create the board
def create_board():
    for each in range(height):
        board.append(width * [space],)

# format the board to print
def print_board():
    for each in range(height):
        print board[each]  #come back and format this to look pretty

create_board()

print board

print_board()

# prompt user for a move
