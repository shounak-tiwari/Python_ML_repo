'''
Constructor construct the memory when object is init with class 
'''
class Student:
    def __init__(self):
        self.__name = ""
        self.__rollNo = 0
        self.__marks1 = 0
        self.__marks2 = 0
        self.__marks3 = 0
        self.__total = 0
        self.__percentage = 0.0
        self.__grade = 'F'
        print("Memory allocation created")
    #1 .set rollnumber
    def set_RollNo(self,r):
        self.__rollNo = r
    def set_Name(self,n):
        self.__name = n
    def set_Marks(self,m1,m2,m3):
        self.__marks1= m1
        self.__marks2= m2
        self.__marks3= m3
    
    def calculateTotal(self):
        self.__total = self.__marks1+self.__marks2+self.__marks3
    
    def calculatePercentage(self):
        self.__percentage = self.__total/3 
    
    def calculateGrade(self):
        if self.__percentage >=90:
            self.__grade = 'A'
        elif self.__percentage >=75:
            self.__grade = "B"
        elif self.__percentage >=60:
            self.__grade = "C"
        elif self.__percentage >=50:
            self.__grade = "D"
        else:
            self.__grade = "F"
    
    def display(self):
        print("Roll Number : ",self.__rollNo)
        print("Name : ",self.__name)
        print("marks 1 ",self.__marks1)
        print("marks 2 ",self.__marks2)
        print("marks 3 ",self.__marks3)
        print("total : ",self.__total)
        print("percentage : ",self.__percentage)
        print("Grade : ",self.__grade)


# setter function
s1 = Student()
s1.set_RollNo(22133454)
s1.set_Name("Akash")
s1.set_Marks(85,90,88)
s1.calculateTotal()
s1.calculatePercentage()
s1.calculateGrade()
# get 
s1.display()