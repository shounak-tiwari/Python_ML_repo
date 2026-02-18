# Control statements when even we have multipe conditions 
# Create a simple calculator 
num1 = int(input("Enter the number 1 : "))
op = str(input("Enter the operators : ")) 
num2 = int(input("Enter the number 2 : "))
match op:
    case '+':
        print(num1+num2)
    case '-':
        print(num1-num2)
    case '*':
        print(num1*num2)
    case '%':
        print(num1%num2)
    case '/':
        print(num1/num2)
    case '//':
        print(num1//num2)
match = 10
print(match) 