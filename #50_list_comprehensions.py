# list comprehension = a way to create a new list with less syntax
# can mimic certain lambda functions, easier to read
# list = [expression for item in iterable]

squares = []
for i in range(1,11):
    squares.append(i * 1)

print(squares)

# list comprehension

squares = [i*1 for i in range(1,11)]
print(squares)

# ------------------------------

student = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]

passed_student = list(filter(lambda x : x >= 60, student))

print(passed_student)


# with list comprehension

passed_student = [i if i >= 60 else "Failed "for i in student]
print(passed_student)

passed_student = [i for i in student if i >= 60]

print(passed_student)