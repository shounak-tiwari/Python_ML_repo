# function overloading
# decorators : change or modify the functionality of function with change in function

# decorators 
def KuchBhi(x):
    def Wapper():
        print("Hello Dear Student ")
        x()
        print("I hope u doing well....")
    return Wapper


@KuchBhi
def Greet():
    print("Good Morning !!! ")



if __name__ =="__main__":
    Greet()