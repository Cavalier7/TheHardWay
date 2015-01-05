numbers = []

def iterator(num, inc):
    i = 0
    while i < num:
        print "At the top i is %d" % i
        numbers.append(i)
        i += int(inc)
        print "Numbers now: " , numbers
        print "At the bottom i is %d" % i
    else:
        break

numero = raw_input("How high would you like to iterate?  ")
inc = raw_input("By what increment would you like to iterate?  ")

iterator(numero, inc)

print "The numbers: "

for num in numbers:
    print num

# 1: done
