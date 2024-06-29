# scope = the region that a variable is recognized
#         A variable is only available from inside the region it is created
#         A global and local scoped version of variable can be created

lang = "Java" # global variable (availabe inside & outside functions)

def display():
    name = "Python" # local variable (availabe only inside this function)
    print("From inside function - " + name)
    print("From inside function - " + lang)

display()
print("From outside function - " + lang) # global
#print("From outside function - " + name) # error , local