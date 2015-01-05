numbers = []

def iterator(num, inc):
    for i in range(0, int(num), int(inc)):
        print "At the top i is %d" % i
        numbers.append(i)
        print "Numbers now: " , numbers
        print "At the bottom i is %d" % i

num = raw_input("How high would you like to iterate?  ")
inc = raw_input("By what increment would you like to iterate?  ")

iterator(num, inc)

print "The numbers: "

for num in numbers:
    print num

# 1: done
