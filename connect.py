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

# check to see if input is an integer 1 through 7

#def check_input(move):
    # try:
        

# check to see if a move is a valid integer move
def check_board(move):
    for row in range(height):
        try: 
            board[row][int(move)-1] == '0'
            return True
        except:
            pass

print check_board(0)
print check_board(10)
print check_board('a')
print check_board(True)

# prompt user for a move
#while True:
    #print "Welcome to Connect Four!  You get to move first - which column would you like?"
    #move = raw_input('> ')
    #if Column:
        
