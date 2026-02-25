class Vechile:
    def __init__(self,price):
        self.price = price
    def getprice(self):
        print("parent function ")
        print(f"Price of vechile : {self.price}")
    
class Tvs(Vechile):
    def __init__(self,modelname ,price):
        self.modelname = modelname
        Vechile.__init__(self,price)
    def showprice(self):
        print(f"Price of vechile {self.price}")
    
class Honda(Vechile):
    def __init__(self,modelname ,price):
        self.modelname = modelname
        Vechile.__init__(self,price)
    def showprice(self):
        print(f"Price of vechile {self.price}")
    
class Bike(Honda,Tvs):
    def functionbike():
        print("Function of bike ")

B1 = Bike("pulsar",110000)

B1.getprice()