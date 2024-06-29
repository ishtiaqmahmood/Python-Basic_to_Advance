'''
With descriptors, you can customize the attribute access.
It enables you to define custom behavior when getting, setting & deleting attributes 
by defining specific methods.

'''

class ReversedStringDescriptor:
    def __get__(self, instance, owner):
        print("Get method invoked")
        return self.value[::-1]
    def __set__(self, instance, value):
        print("Set method invoked")
        self.value = value
    def __delete__(self, instance):
        print("Delete method invoked")
        del self.value

class MyClass:
    my_attribute = ReversedStringDescriptor()


my_object = MyClass()
my_object.my_attribute = "Hello"
print(my_object.my_attribute)
del my_object.my_attribute