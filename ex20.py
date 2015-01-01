# imports the argv method from the sys module
from sys import argv

# assigns two CLI variables to the argv method
script, input_file = argv

# creates a method that prints a string
def print_all(f):
    print f.read()

# creates a method that returns the read cursor to the beginning of a string
def rewind(f):
    f.seek(0)

# creates a method that prints line # + each line of a string
def print_a_line(line_count, f):
    print line_count, f.readline()

# open a text file as an input
current_file = open(input_file)

# tells the user that the whole file will be printed
print "First let's print the whole file: \n:"

# prints the entire contents of the input file
print_all(current_file)

# tells the user that the whole file will be printed again 
print "Now let's rewind, kind of like a tape."

# calls the rewind() method to start at the beginning of the file
rewind(current_file)

# tells the user that the whole file will be printed line by line
print "Let's print three lines:"

# creates a int variable to keep count of the current line
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

# 1: done
