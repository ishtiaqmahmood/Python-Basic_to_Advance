# object oriented programming (oop)

from  car_class import Car

toyota = Car("Mitsubishi", "Lancer", "2002", "Black")
ford = Car("Ford", "Mustang", "2006", "Red")

print("Toyota : ")
toyota.about()
toyota.drive()
toyota.stop()

print("Ford : ")
ford.about()
ford.drive()
ford.stop()

# accessing class variable

print("Toyota : ")
print("Wheels: {}".format(toyota.wheels))
toyota.wheels = 3
print("Wheels: {}".format(toyota.wheels)) # changing class variable

print("Ford : ")
print("Wheels: {}".format(ford.wheels))


# change class variable for all instance
# Car.wheels = 4