# loop control statements = change a loop execution from its normal sequence

# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

# break

name = ""

while True:
    name = input("Enter your name: ")
    if(name != ""):
        break

print("Name: " + name)

# continue

phone_number = "123_4567_9101"

for i in phone_number:
    if i == '_':
        continue
    print(i, end="")
print()

# pass

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)