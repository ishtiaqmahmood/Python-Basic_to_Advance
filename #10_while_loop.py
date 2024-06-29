# while loop - a statement that will execute it's block of code,
#              as long as it's condition remains true

name = None

while not name:
    name = (input("Enter your name: "))

print("Hello " + name)

# print 0-100

i = 0;
while (i < 101):
    print(i)
    i += 1

# infinite loop

while (True):
    print("I will jam your system")