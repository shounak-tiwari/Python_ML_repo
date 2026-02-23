def nSum(n):
    if n == 0: 
        return 0
    elif n ==1:
        return 1
    else:
        return n+nSum(n-1)

