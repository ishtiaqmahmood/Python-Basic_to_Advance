# tuple = collection which is ordered and unchangeable
#         used to group together related data

student = ("Ishtiaq", 32, "male")

number = (2,3,4,1,5,6)

print(student.count("Ishtiaq")) # count how many times the item appear in the tuple
print(student.index(32)) # get index of selective item

print(student) # print student tuple
print(number)

for x in student:
    print(student)

if "male" in student:
    print("Male")