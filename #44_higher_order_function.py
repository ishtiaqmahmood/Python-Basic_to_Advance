# higher order function = a function that either:
#                          1. accept a function as an argument
#                          2. returns a function
#                           (In python functions are also treated as objects)


def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

# higher order function can accept function as argument

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)

# higher order function can return a function

def divisor(x):
    def divident(y):
        return y / x
    return divident

divide = divisor(2)
print(divide(10))