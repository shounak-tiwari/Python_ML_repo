def read_files():
    with open(r"C:\Users\Akash\Desktop\CDGI\Day-8\student.txt","r") as A:
        for line in  A:
            yield line

if __name__ =="__main__":
    x = read_files()
    for i in x:
        print(i)