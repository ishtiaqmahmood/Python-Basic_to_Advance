'''
Python Generators

In Python, a generator is a function that returns an iterator that produces a sequence of 
values when iterated over.
Generators are useful when we want to produce a large sequence of values, 
but we don't want to store all of them in memory at once.

Use of Python Generators

1. Easy to Implement
2. Memory Efficient
3. Represent Infinite Stream
4. Pipelining Generators


'''


list = [1,2,3,4,5]

def multiply_list(list):
    for i in list:
        yield (i * 2)

res = multiply_list(list)

#print(next(res))
#print(next(res))
#print(next(res))
#print(next(res))
#print(next(res))

for i in res:
    print(i)


# ------------------------

def fibo_num(nums):
    x, y = 0, 1
    for i in range(nums):
        x,y = y, x+y
        yield x

def power(nums):
    for i in nums:
        yield i ** 2

res = sum(power(fibo_num(10)))

print(res)