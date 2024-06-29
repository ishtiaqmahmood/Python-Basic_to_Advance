'''

In Python, we can indicate that a variable should be treated as internal or private by prefixing 
its name with a single underscore or double underscore respectively.

When we add a single underscore ( _ ) before a variable name, we specify that the attribute 
is intended for internal use within the class. Please note that this does not enforce privacy 
or prevent access to the attribute from outside the class. It is still possible to 
access and modify the attribute from outside the class. The use of this convention is to 
encourage encapsulation and proper abstraction.

'''


class Car:
    def __init__(self):
        self._internal_variable = "Internal"
        self.__private_variable = "Private"

c = Car()
print(c._internal_variable)

# Checking the attributes of the class to see the renamed private variable
print(dir(c))

print(c._Car__private_variable)