# str.format() = optional method that gives users more control when displaying output

animal = "cow"
item = "moon"

print("The {} jumped over the {}".format(animal, item))
print("The {0} jumped over the {1}".format(animal, item)) # positional argument
print("The {animal} jumped over the {item}".format(animal="monkey", item="tree")) # keyword arguments

text = "The {} jumped over the {}"
print(text.format("cow", "moon"))

# padding and alignment

name = "Ishtiaq"
vortex = "king vortex"

print("Hello {}, Have a nice day.".format(name))
print("Hello {:10}, Have a nice day.".format(name)) # adding some padding
print("Hello {:<10}, Have a nice day.".format(name)) # left aligb
print("Hello {:>10}, Have a nice day.".format(name)) # right align
print("Hello {:^10}, Have a nice day.".format(name)) # center align
print("Hello {vortex:^10}, Have a nice day.".format(vortex="Lua"))

# formating number

pi = 3.1416
number = 1000

print("The number pi is {:.2f}.".format(pi)) # changing floating point to 2
print("The number is {:,}.".format(number)) # adding a commma after 1 -> 1,000
print("The number is {:b}.".format(number)) # represent binary of 1000
print("The number is {:o}.".format(number)) # represent octal of 1000
print("The number is {:x}.".format(number)) # represent hexadecimal of 1000
print("The number is {:E}.".format(number)) # represent scientific representation of 1000