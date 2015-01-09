# constants
height = 6
width = 7
human = 'X'
computer = '%'
space = 'O'
board = []
checklist = range(1,4)

# create the board
def create_board():
    for each in range(height):
        board.append(width * [space])

# format the board to print
def print_board():
    for each in range(height):
        print board[each]  #come back and format this to look pretty

create_board()   


# check to see if input is a valid move, i.e. an integer between 1 and 7
def check_guess(move):
    try:
        int(move)
    except:
        print "That is not a valid guess, please try another."
        start()
    else:
        for column in range(width):
            if column == int(move) - 1:
                return True
        else:
            print "That is not a valid guess, please try another."
            start()
            
# make the move on the board
def make_move(move):
    adjusted_move = int(move) - 1 # need to convert move to int() and adjust it -1 because numbering starts at 0
    for row in range(height-1, -1, -1): # this range iterates backwards from 5 (the bottom row) to 0 (the top row)
        if board[row][adjusted_move] == space:
            board[row][adjusted_move] = human
            return row, adjusted_move
    else:
        print "That column is full, please choose another."
        start()

# checks in each diagonal direction for any matching pieces

def check_left(row, col):
    connected = 1  # if this number reaches 4, the player wins
    while connected < 4:
        for each in checklist:  # need to add an error catch for numbers outside the range
            try:
                if board[row - each][col - each] == human: # checks to lower-left
                    connected += 1
            except:
                break
        for each in checklist:
            try:
                if board[row + each][col + each] == space: # checks to upper-right
                    connected += 1
            except:
                break
        for each in checklist:
            try:
                if board[row + each][col - each] == space: # checks to lower-right
                    connected += 1
            except:
                break
        for each in checklist:
            try:
                if board[row - each][col + each] == space: # checks to upper-left
                    connected += 1
            except:
                break
    print "You have %s pieces in a row." % connected
    if connected >= 4:
        print "Congrats, you win!"
        break
    else:
        print "Sorry, you haven't won yet"
        return False

while True:
    print_board()
    print "Which column would you like?",
    guess = raw_input("> ")
    
    if check_guess(guess):
        make_move(guess)
    
    if check(row, adjusted_move) == False:  # player has not won yet, so computer moves
        

print "Welcome to Connect Four!  You get to move first."
        
start()
        
