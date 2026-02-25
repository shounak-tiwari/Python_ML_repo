# file handling :file handling refers to the mechnisms or process to perform operations on a file like opening, CURD and close it...
 
class Arithmetic:
    def __init__(self,num1,num2) -> None:
        self.number1 = num1
        self.number2 = num2
    def addition(self):
        return self.number1+self.number2
    def substraction(self):
        return self.number1 - self.number2
    def multipliction(self):
        return self.number1 * self.number2
    
obj1 = Arithmetic(10,20)
print(obj1.multipliction())

# Create file
# open(): create new file if file is not exists in give path , if it already exists it open the existing file 

# file = open(r"C:\Users\Akash\Desktop\CDGI\Day-8\student.txt","r")


def read_large_file(file_path):
    with open(file_path) as f:
        for line in f:
            yield line
    

for x in read_large_file(r"C:\Users\Akash\Desktop\CDGI\Day-8\student.txt"):
    print(x)
