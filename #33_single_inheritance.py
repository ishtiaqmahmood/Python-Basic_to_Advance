class Animal:
    def eat(self):
        print("The animal is eating")
    def sleep(self):
        print("The animal is sleeping")
    def alive(self):
        print("The animal is alive")

    
class Rabbit(Animal): # Rabbit -> Children class, Animal -> Parent class
    def run(self):
        print("The rabbit is running")

class Fish(Animal):
    def swim(self):
        print("The fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("The hawk is flying")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()


print("Rabbit: ")
rabbit.alive()
rabbit.eat()
rabbit.sleep()
rabbit.run()

print("Fish: ")
fish.alive()
fish.eat()
fish.sleep()
fish.swim()

print("Hawk: ")
hawk.alive()
hawk.eat()
hawk.sleep()
hawk.fly()