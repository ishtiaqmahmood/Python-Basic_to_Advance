import random

x = random.randint(1,6) # between 1-6
y = random.random() # between 0-1
 
print(x)
print(y)

# using random choice method
myList = ["rock", "paper", "seissors"]
z = random.choice(myList)

print(z)

# using random shuffle method
cards = [1,2,3,4,5,6,7,8,9,"J","K","Q","A"]
random.shuffle(cards)
print(cards)