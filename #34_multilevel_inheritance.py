class Life:
    alive = True

class Animal(Life):
    def eat(self):
        print("This animal is eating")

class Dog(Animal):
    def bark(self):
        print("This animal is barking")

dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()
