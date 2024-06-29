# variable - a container for a value. Behaves as the value that it contains

name = ' Ishtiaq'
print("Hello"+name)

data_type = type(name)

#string
f_str = 'First '
s_str = 'Second'

full_str = f_str + s_str
print(full_str)

# int
age = 32
age +=1
print(age)
print(type(age))
#print("Your age is : " + age) # error - can only concatenate str to str
print("Your age is : " + str(age))

# float
height = 270.6
print(height)
print(type(height))
print("Your height is : "+ str(height) + " cm")

# boolean
human = True
print(human)
print(type(human))
print("Are you a human ? -> "+ str(human))

# example - 1
car = 'Volvo'
truck = 'Cybertruck'
color_c = 'red'
color_t = 'silver'

print(car + " is " + color_c + " and " + truck + " is " + color_t)

# combining multiple variable

a, b, c, d = 10, 11, 12, 13
print(a)
print(b)
print(c)
print(d)

x = y = z = 10
print(x)
print(y)
print(z)