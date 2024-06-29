# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword arguments

def name(**kwargs):
    print("Hello " + kwargs['title'] + " " + kwargs['first'] + " " + kwargs['middle'] + " " + kwargs['last'])
    print("Hello ", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")
    print()


name(title="Mr.", first="Ishtiaq", middle="Mahmood", last="_")
