class Employee:
    def inputdetails():
        name = input("Enter the name : ")
        title = input("Enter the title : ")
    def output():
        print(f"Name of employee : {name} ")
        print(f"Title of employee : {title} ")
obj = Employee
obj.inputdetails()
obj.output()