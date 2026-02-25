# 2. run time polymorphisms
    # a. function overriding 
class A:
    def greet(self):
        print("Wellcome in world of python ")

class B(A):
    def greet(self):
        print("Wellcome in world of python with machine learning ")
    
obj_B = B()
obj_B.greet()