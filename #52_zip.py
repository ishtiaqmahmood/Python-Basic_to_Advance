# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
# creates a zip object with paired elements stored in tuples for each elements

usernames = ["Alex", "Zoe", "Nick"]
passwords = ("1234", "password", "admin1234")
login_day = ["1/1/2001", "24/5/2013", "4/12/2023"]

# dictionary
users = dict(zip(usernames, passwords))

print(type(users))

for key, value in users.items():
    print(key + " : " + value )

# list

users = list(zip(usernames, passwords, login_day))

print(type(users))

for i in users:
    print(i)