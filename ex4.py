cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are" , cars , "cars available."
print "There are only" , drivers , "drivers available."
print "There will be" , cars_not_driven , "empty cars today."
print "We can transport" , carpool_capacity , "people today."
print "We have" , passengers , "to carpool today."
print "We need to put about" , average_passengers_per_car , "in each car."

# Study Drill 1:  the error demonstrates that the coder had mistakenly represented the variable "carpool_capacity" as "car_pool_capacity".  The later variable had not yet been defined, so the program could not use it when defining "average_passengers_per_car".
# Study Drill 2:  it is not necessary to make "space_in_a_car" a Float variable because it represents an integer unit, i.e. there is no way to fit any percentage of a person in a car, they must be all in.
