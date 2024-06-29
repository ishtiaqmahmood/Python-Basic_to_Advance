# some string methods

name = ' ishtiaq mahmood '

print(len(name)) # string length
print(name.find('s')) # find index of char in string
print(name.capitalize()) # capitalize the first char of the string
print(name.lower()) # convert to lower case
print(name.upper()) # convert to upper case
print(name.isdigit()) # check for digit, if digit returns true
print(name.isalpha()) # if alfanumeric, and without space between letters, returns true
print(name.count('i')) # count the number of letters
print('.'.join(['ab', 'pq', 'rs'])) # iterable, The string whose method is called is inserted in between each given string. The result is returned as a new string.
print(name.split(' ',2)) # split() method splits a string into a list of strings after breaking the given string by the specified separator
print(name.replace('q', 'a')) #replace q by a
print(name * 3) # print name 3 times