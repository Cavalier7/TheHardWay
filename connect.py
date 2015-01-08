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
        board.append(width * [space])

# format the board to print
def print_board():
    for each in range(height):
        print board[each]  #come back and format this to look pretty

create_board()

print board

print_board()   

# check to see if a move is a valid integer move
def check_board(move):
    for row in range(height,0,-1):
        try:
            guess = board[row][int(move)-1]
            if  guess == '0'
                guess = player
        except:
            pass
            
# make the move on the board
def make_move(move):
    board[row]

print check_board('0')
print check_board('10')
print check_board('7')
print check_board('2')

print_board()

# prompt user for a move
#while True:
    #print "Welcome to Connect Four!  You get to move first - which column would you like?"
    #move = raw_input('> ')
    #if Column:
        
