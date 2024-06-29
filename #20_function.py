# function = a block of code which is executed only when it is called

# function with no return value

def hello(first_name, last_name, age):
    print("Hello " + first_name + " " + last_name)
    text = ("You are {} years old!!").format(age)
    print(text)
    print("Have a nice day!")

hello("Ishtiaq", "Mahmood", 32)


# function with return value


# return statement = Function send python values/object back to the caller. 
# these values/objects are known as the function's return value


def sum(a, b):
    return a+b

x = sum(6,6)
print(x)


# keyword arguments = arguments preceded by an identifier when we pass them to a function
#                     the order of the arguments doesn't matter, unlike positional argument
#                     python knows the names of the arguments that our function receives


def delta(first, second, last):
    print("Hello " + first + " " + second + " " + last)

delta(last="_", second="Mahmood", first="Ishtiaq")


# nested function call = function calls inside other function calls
#                        innermost function calls are resolve first
#                        returned value is used as argument for the next outer function



print(round(abs(float(input("Enter a whole positive number: ")))))