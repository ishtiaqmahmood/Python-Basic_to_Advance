# reduce() = apply a function to an iterable and reduce it to a single cumulative value
#            performs function on first two elements and repeat process until 1 value returns
# reduce(function, iterable)

import functools

letters = ["H", "E", "L", "L", "O"]

word = functools.reduce(lambda x,y : x+y, letters)
print(word)

numbers = [5,4,3,2,1]
result = functools.reduce(lambda x,y:x*y, numbers)
print(result)

