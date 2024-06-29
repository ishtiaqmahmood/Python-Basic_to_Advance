# exception = events detected during execution that interrupt the flow of program

try:
    numerator = int(input("Enter a number to devide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divided by zero!!")
except ValueError as e:
    print(e)
    print("Enter only number!!")
except Exception as e:
    print(e)
    print("Something went wrong!!")
else : 
    print(result)
finally:
    print("This will always executed!!")