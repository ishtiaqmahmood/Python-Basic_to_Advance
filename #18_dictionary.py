# dictionary = A changeable, unordered collection of unique key:value pairs
#              fast because they use hashing, allow us to access a value quickly

capitals = {'USA': 'Washington DC',
            'India': 'New Delhi' ,
            'China': 'Beijing' , 
            'Russia': 'Moskow'
            }

capitals.update({'Germany': 'Berlin'}) # update dictionary with new item
capitals.update({'India': 'Kolkata'})  # update existing item
capitals.pop('India') # remove item from dictionary
#capitals.clear() # clear the dictionary
x = capitals.copy() # copy dictionary to a variable

# keys for the dictionary
alphabets = {'a', 'b', 'c'}
# value for the dictionary
number = 1
# creates a dictionary with keys and values
# the fromkeys() method returns a dictionary with the specified keys and the specified value.
dictionary = dict.fromkeys(alphabets, number)
print(dictionary)

print(capitals['Germany']) # print value using key
print(capitals.get('Russia')) # print value using key
print(capitals.keys()) # print all the keys
print(capitals.values()) # print all the value
print(capitals.items()) # print all keys and values

print(capitals)

for key, value in capitals.items():
    print(key, value)