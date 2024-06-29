# set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin") # add element
utensils.remove("spoon") # remove element
#utensils.clear() # clear set
utensils.update(dishes) # join two set

dinner_table = utensils.union(dishes) # collection of all items in utensils and dishes

for x in dinner_table:
    print(x)

print(utensils.difference(dishes)) # items that present in the utensils but not in dishes
print(utensils.intersection(dishes)) # return items that dishes have
