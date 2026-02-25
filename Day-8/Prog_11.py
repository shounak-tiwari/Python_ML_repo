# encapsulatin : wrapping the data into single unit 
class A:
    def __init__(self):
        self.__name = str()
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name

obj = A()

obj.set_name("akash")
print(obj.get_name())