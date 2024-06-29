# *args = parameter that pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments

def mul(*args):
    res = 1
    for i in args:
        res *= i
    return res

print(mul(1,2,3,4))

def sum(*args):
    res = 0
    args = list(args)
    args[0] = 0 # make 1st element 0 always
    for i in args:
        res+= i
    return res

print(sum(1,2,3,4))