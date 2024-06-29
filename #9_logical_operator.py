# logical operator - (and,or,not) -> used to check if two or more conditional statement is true

temp = float(input("Please enter the temperature: "))

if(temp >= 0 and temp <= 30): # both condition must be true
    print("The temperature is good today. ")
elif(temp < 0 or temp > 30): # atleast one condition have to be true
    print("The temperature is bad today.")
elif not(temp < 0 or temp > 30): # not - makes the true -> false or false -> true
    print("The temperature is good today.")
else:
    print("Please enter a valid temperature.")

