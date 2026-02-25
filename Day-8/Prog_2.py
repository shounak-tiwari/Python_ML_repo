# compile time polymorphisms
    # a. function overloading : multiple behaviour in class with same name but their parms is different
from multipledispatch import dispatch
class Poly:
    @dispatch(int)
    def Fun(self,x:int):
        return f"Function with single args :{x}"
    @dispatch(int,int)
    def Fun(self,x:int,y:int):
        return f"Function with two args :{x},{y}"

# Object declare
p1 = Poly()
print(p1.Fun(10))
print(p1.Fun(10,20))