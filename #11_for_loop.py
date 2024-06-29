import time

# for loop = a statement that will execute it's block of code
#            a limited amount of times
#            while loop = unlimited
#            for loop = limited

# print 10 times - 0 to 9
for i in range(10):
    print(i)

# print 51 times - 50 to 100
for i in range(50,101):
    print(i)

# print even number from 0-101
for i in range(0,101,2):
    print(i)

# print odd number from 0-101
for i in range(1,101,2):
    print(i)

# print string elements with for loop
for letters in "Hello programmer":
    print(letters)

# counter program
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)

print("Start Programming again!!!!")