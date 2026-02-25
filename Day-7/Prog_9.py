class Employee:
    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary
    def get_details(self):
        return f"Name {self.name} ,Salary : {self.salary}"
    
class Trainer(Employee):
    def __init__(self, name, salary,department):
        print(name)
        print(salary)
        print(department)

    
T1 = Trainer("Akash","Null","Information tech.. ")

print(T1.get_details())