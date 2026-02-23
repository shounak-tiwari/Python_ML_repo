'''
1. position args 
'''
# position args in function 
# keywords args in functions or default args
#  positional len args 
try:
    def postionargs(x=0,y=0):
        print(f"The value of x is : {x}")
        print(f"The value of y is : {y}")
except TypeError as e :
    print(e)
finally:
    if __name__ =='__main__':
        postionargs(y=190)