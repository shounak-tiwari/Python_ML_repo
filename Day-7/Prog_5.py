class Employee:
        # behaviour of class : EmployeeDetails
        def EmployeeDetails(self):
            # ref scope is inside the function
            print("Id of self : ",id(self))
            self.Name = str(input("Enter the name of employee : "))
        

Obj1 = Employee()