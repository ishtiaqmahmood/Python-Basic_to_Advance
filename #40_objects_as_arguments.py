class Toyota:
    color = "Black"
    def run(self):
        print("My {} Toyota is running fine".format(self.color))


car = Toyota()

print("Before Changing color: ")
car.run()

# creating a function that takes objects as arguments

def change_color(object, color):
    object.color = color


change_color(car, "While")

print("After changing color: ")
car.run()