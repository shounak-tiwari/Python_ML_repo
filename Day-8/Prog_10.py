# hide imple deatils and show neccessary 

from abc import ABC ,abstractmethod

class Area(ABC):
    @abstractmethod
    def area(awlf,l,b):
        return f"area of ract is : {l*b}"

class Necc(Area):
    def area(awlf,l,b):
        return Area.area(awlf,l,b)
    
necobj = Necc()
print(necobj.area(10,20))