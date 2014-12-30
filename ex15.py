# imports the argv commands from the sys library
#from sys import argv

# assigns the variables 'script' and 'filename' to the command line
#script, filename = argv

# prompts for the filename

filename = raw_input("Type the filename: ")

# creates 'txt' that represents the opened file
txt = open(filename)

# prints the name of opened file"
print "Here's your file %r:" % filename

# reads the file
print txt.read()

# closes the file
txt.close()

# prompts the user to input the name of the file again
print "Type the filename again:"
file_again = raw_input(">")

# opens the inputted filename
txt_again = open(file_again)

# prints the contents of the second file
print txt_again.read()

# closes the second file

txt_again.close()

# study drill #1: done
# 4: done
# 5: done
