# nested loop = the "inner loop" will finish all of it's iteration before finishing one iteration of the "outer loop"

# pattern printing

rows = int(input("Number of rows: "))
columns = int(input("Number of columns: "))
symbol = input("Enter a symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end=" ")
    print()


# print 1-1000 using nested loop

for i in range(1,2):
    for j in range(1001):
        print(i * j, end=" ")
    print()