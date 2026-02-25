class Employee:
    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary
    def get_Details(self):
        return f"Name : {self.name} , Salary : {self.salary}"

class Trainer(Employee):
    def __init__(self,name,salary, department):
        Employee.__init__(self,name,salary)
        self.department = department
    def get_Details(self):
        return f"Name : {self.name}, Salary : {self.salary} , department : {self.department}"


T1 = Trainer("Akash","9000000","CS")
print(T1.get_Details())