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

# check to see if a move is a valid integer move
def check_guess(move):
    try:
        int(move)
    except:
        return False
    else:
        for column in range(width):
            if column == int(move)-1:
                return True
            else:
                pass
        else:
            return False
        
# make the move on the board
def make_move(move):
    for row in range(height-1,-1,-1): # this range iterates backwards from 5 (the bottom row) to 0 (the top row)
        if board[row][int(move)-1] == space:
            board[row][int(move)-1] = player
            break
    else:
        print "That column is full, please try another."

test_values = ['0', 'Abraham', '7', 'True']

#for each in test_values:
    #print "%s is a valid entry? " % each, check_guess(each)

make_move('7')
make_move('7')
make_move('7')
make_move('7')
make_move('7')
make_move('7')
make_move('7')
make_move('7')
make_move('7')

print_board()

# prompt user for a move
#while True:
    #print "Welcome to Connect Four!  You get to move first - which column would you like?"
    #move = raw_input('> ')
    #if Column:
        
