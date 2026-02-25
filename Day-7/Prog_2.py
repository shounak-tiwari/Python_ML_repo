try: 
    class Employee:
        # behaviour of class : EmployeeDetails
        def EmployeeDetails():
            # ref scope is inside the function 
            Name = str(input("Enter the name of employee : "))
        # behaviour of class : PrintDetails 
        def PrintDetails():
            print(f"Name of employee : {Name}")
    
    Obj = Employee
    Obj.EmployeeDetails()
    Obj.PrintDetails()

except NameError as e:
    print(e)

except classmethod as e :
    print(e)

except:
    print("Some error found")

finally:
   print("Happy coding")