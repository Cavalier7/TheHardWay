i = 0
numbers = []

def iterator(num):
    i = 0
    while i < num:
        print "At the top i is %d" % i
        numbers.append(i)
    
        i += 1
        print "Numbers now: " , numbers
        print "At the bottom i is %d" % i

iterator(6)

print "The numbers: "

for num in numbers:
    print num

# 1: done
