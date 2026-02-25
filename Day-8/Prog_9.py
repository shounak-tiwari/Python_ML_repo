from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def area(self):
        return "Hello"



obj = A()
print(obj.area())