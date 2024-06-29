# 2d list = list of lists

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

utility = ["cigar", "beer"]

food = [drinks, dinner, dessert]

# print 2 item of drinks
print(food[0][1])

# print 3 item of dinner
print(food[1][2])

# print 1 item of dessert
print(food[2][0])

# add a new list 
food.append(utility)

# print all food item
print(food)
