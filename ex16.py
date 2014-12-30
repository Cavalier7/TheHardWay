from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want to do that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.close()

print "Now we'll print the new contents of the file that you just input."

new_target = open(filename)
print new_target.read()

print "And now we'll close it."
new_target.close()

# 2: done
