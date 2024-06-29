# sort() method = used with lists
# sort() function = used with iterables

students_list = ["Alex", "Candy", "Brown", "Porter", "krabs"]
students_tuple = ("Alex", "Candy", "Brown", "Porter", "krabs")

students_list.sort()

for i in students_list:
    print(i)

students_list.sort(reverse=True)

print("---------------------------------")


for i in students_list:
    print(i)

print("---------------------------------")

sorted_tuple = sorted(students_tuple)

for i in sorted_tuple:
    print(i)


# list of tuples

list_tuples = [("Alex", "F", 60),
               ("Bunny", "A", 33),
               ("Roland", "B", 73),
               ("Jackson", "C", 45),
               ("Devon", "D", 90)
                ]

grade = lambda grades:grades[1]

list_tuples.sort(key=grade)

for i in list_tuples:
    print(i)

print("-----------------------")

age = lambda ages:ages[2]
list_tuples.sort(key=age, reverse=True)

for i in list_tuples:
    print(i)


# tuple of tuples

tuple_tuples = [("Alex", "F", 60),
               ("Bunny", "A", 33),
               ("Roland", "B", 73),
               ("Jackson", "C", 45),
               ("Devon", "D", 90)
                ]

print("--------------------------")
name = lambda names:names[0]

tuple_tuples.sort(key=name)

for i in tuple_tuples:
    print(i)