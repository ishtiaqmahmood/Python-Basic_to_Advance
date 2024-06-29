# if __name__ == '__main__'

# module can be run as a standalone program 
# or
# module can be imported or used to other program

# python interpreter sets "special variables", one of which is __name__
# python will assign the __name__ variable a value of '__main__' if its the initial module being run
from car_class import Car

car = Car("BMW", "V-100", 2000, "Black")


def main():
    print("Hello")
    print(__name__)

if __name__ == '__main__':
    main()
    car.about()
    print("Running from main module")
else:
    car.about()
    print("Running from other module indirectly")



