# slicing = create a substring by extracting elements from another string
# indexing[] or slice()
# [start, stop, step]

string = "Alice is a good programmer"

# now we will extract name and profession

name = string[:5] # extract the name - Alice, start is empty and stop is 5, python assume that start is the first element or 0 index
name = string[0:5] # extract the name - Alice, start at 0 index and stop at 4
name = string[0:-21] # using negative index, negative index start from the right side, right most element is -1

job = string[16:] # extract the profession, here stop is empty, pythom assume that stop is the last element of the string

print(name)
print(job)


# step
# default step is 1
# we can change step manually

number = "123456789"

even = number[1:10:2] # start at index 1 , step is 2 - so index 1, then 3, then 5 and so on, until stop
odd = number[0::2] # start at index 1, step is 2 - so index 0, then 2, then 4 ad so on, until stop
reverse = number[::-1] # reverse the string

print(even)
print(odd)
print(reverse)

# slice() method
# similar to indexing
# (start, stop, step)

website = "http://google.com"

slice = slice(7,-4)

print(website[slice])