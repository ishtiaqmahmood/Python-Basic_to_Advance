# abstract class = a class which cointains one or more abstract methods
# abstract methods = a method that has a declaration but does not have any implementation

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass
    

class Car(Vehicle):

    def go(self):
        print("The car is running")

    def stop(self):
        print("The car is stopped")

    
class Motorcycle(Vehicle):

    def go(self):
        print("The bike is running")

    def stop(self):
        print("The bike is stopped")


car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.go()

car.stop()
motorcycle.stop()