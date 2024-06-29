# lists = used to store multiple items in a single variable

food = ["Pizza", "Apple", "Banana", "Beef", "Rice"]
food2 = ["Cocacola"]

food[0] = "Sushi" # change the value of 0 index

print(food) # print all item in the list
print(food[3]) # print selected item
food.append("Chicken") # add new items
print(food.count("Rice")) # count any items in the list
print(food.index("Apple")) # getting index of an item
food.insert(1, "Cake") # inserting an item at index 1
x = food.copy() # copy food list into x
food.pop() # remove the last element
food.extend(food2) # food list extended by food2 list
food.sort() # sorting the list
food.remove("Beef") # remove particular item
food.reverse() # reverse the position of the list item

for i in food:
    print (i)

food.clear() # clear the list, no item

for i in food:
    print (i)
