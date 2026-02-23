# concept 1 : class and object 
'''
A class in Python is a user-defined template for creating objects. 
It bundles data and functions together, making it easier to manage and use them.
 When we create a new class, we define a new type of object.
 We can then create multiple instances of this object type.
'''
# create class : class is created by class keyword 
class Employee:
    # attribute of class
    # Name = str()
    pass
obj = Employee
obj.Name = "Akash Tiwari"
obj.Address = "Maihar mp"
print(obj.Name)
print(obj.Address) 
print(type(obj.Address)) 
print(type(obj)) 
