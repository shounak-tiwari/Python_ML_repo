# Inheritance : it is major piller of oops that allows derived class to inherit attirbutes and methods from base class ... inherit means reuse 
# and  inheritance perform reuse the properties of base or parent class into child class

class Animal:
    def __init__(self,name):
        self.name = name
    def details(self):
        print("Animal Name  : ",self.name)
    
class DogeshBhai(Animal):
    def Sound(self):
        print(f"{self.name} Barks (Bhow Bhow)")

d = DogeshBhai("Buddy")
d.Sound()