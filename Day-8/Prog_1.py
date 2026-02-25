# Polymorphisms : polymorphisms , laten greek word ,poly -- many and morphisms -- forms
# Polymorphisms is genrally divide into two main parts 
'''
1. compile time polymorphisms
    a. function overloading : multiple behaviour in class with same name but their parms is different 
    b. operators overloading (task) youtube nhi dekhna )
2. run time polymorphisms
    a. function overriding 
'''

def len(x):
    count =0 
    for i in x:
        count+=1
    return f"The len of {x} is : {count}"

# Type : string
x = "Akash" 
print(f" {len(x)}")

lst = ["Akash","Aditya","Null"]
print(f" {len(lst)}")
