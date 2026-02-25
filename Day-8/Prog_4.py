# decorators defination
def KuchBhi(x):
    def Wapper(name):
        print("Hello Dear Student ")
        x(name)
        print("I hope u doing well....")
    return Wapper

# calling of decor
@KuchBhi
# defination of function
def Greet(Name):
    print("Good Morning !!! ",Name)

# calling of function 
if __name__ =="__main__":
    Greet("Harsh Babu")