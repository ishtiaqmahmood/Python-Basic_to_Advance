# if statement = a block of code that will execute if it's condition is true
# order matters

age = int(input("Enter your age : "))

if (age == 100):
    print("You are century old!!!")
elif(age >= 18):
    print("You are adult.")
elif(age < 0):
    print("You haven't been born yet!!")
else:
    print("You are so young.")

