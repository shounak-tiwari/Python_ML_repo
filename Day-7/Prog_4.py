# instance is use for track the current active object 
class Employee:
        # behaviour of class : EmployeeDetails
        def EmployeeDetails(self):
            # ref scope is inside the function
            print("Id of self : ",id(self))
            self.Name = str(input("Enter the name of employee : "))
        def EmployeePrint(self):
              print("Name of : ",self.Name)

# object -1 
Obj1 = Employee()
print("Id of object 1 : ",id(Obj1))
Obj1.EmployeeDetails()
Obj1.EmployeePrint()


# object -2 
Obj2 = Employee()
print("Id of object 2 : ",id(Obj2))
Obj2.EmployeeDetails()
Obj2.EmployeePrint()


