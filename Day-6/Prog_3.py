try:
    def Addition(*x):
        return sum(x)
except IndentationError as e:
    print(e)
finally:
    if __name__=='__main__':
        x = Addition(10,20,30,40,50)
        print(x)