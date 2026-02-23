# create and return n Odd Numbers in a List.. using functions 
def OddList(n:int)->list:
    lst = list(range(1,n+1,2))
    return lst

if __name__ =='__main__':
    print(OddList(100))