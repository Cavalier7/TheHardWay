# imports the argv object from the sys module
from sys import argv

# assigns the two command line values to script and filename
script , filename = argv

# opens the previously defined file with the open() function
txt = open(filename)

# prints the filename
print "Here's your file %r:" % filename

# reads the contents of the text() object and prints it
print txt.read()

# prompts and defines a second filename
print "Type the filename again:"
file_again = raw_input("> ")

# again open the second filename
txt_again = open(file_again)

# prints the contents of the second filename
print txt_again.read()

# study drill #1: done
