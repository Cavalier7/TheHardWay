name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_metric = height * 2.54 # centimeters
weight = 180 # lbs
weight_metric = weight * 0.45 # kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches (%r centimeters) tall." % (height, height_metric)
print "He's %d pounds (%r kilograms) heavy." % (weight, weight_metric)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

# Study Drill 1: Done
# Study Drill 2: Done
# Study Drill 4: Done
