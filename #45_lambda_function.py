# lambda function = function written in one line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
# lambda parameters:expression

double = lambda x: x * 2
multiply = lambda x,y : x * y
add = lambda x,y,z : x+y+z
full_name = lambda f_name, l_name : f_name + " " + l_name
age_check = lambda age : True if (age>=18) else False

print(double(2))
print(multiply(2,4))
print(add(1,2,3))
print("Ishtiaq", "Mahmood")
print(19)