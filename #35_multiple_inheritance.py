# multiple inheritance

class Prey:

    def flee(self):
        print("This animal flees")

class Predator:

    def hunt(self):
        print("This animal hunts")


class Rabbit(Prey):

    def about(self):
        print("Rabbit")

class Hawk(Predator):

    def about(self):
        print("Hawk")

class Fish(Prey, Predator):

    def about(self):
        print("Fish")

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

# Rabbit object - inherit only Prey class
rabbit.about()
rabbit.flee()

# Hawk object - inherit only Predator class
hawk.about()
hawk.hunt()

# Fish object - inherit both Prey and Predator class
fish.about()
fish.flee()
fish.hunt()