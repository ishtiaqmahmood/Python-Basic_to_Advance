# index operator [] = give access to a sequence's element (str, list, tuple)

name = "ishtiaq Mahmood_"

if (name[0].islower()):
    name = name.capitalize()

print(name)

first_name = name[:7].upper()
last_name = name[8:15].lower()
char = name[-1]

print(first_name)
print(last_name)
print(char)