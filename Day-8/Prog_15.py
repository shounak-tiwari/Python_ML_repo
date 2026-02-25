'''
w : write mode 
r : read mode 
a : append mode 
x : create (error if exists)
b : binary mode
'''
import json
data = {
    "name":"Akash",
    "role":"Trainer",
    "address":"IndoreMP"
}
with open("data.json","a") as file:
    json.dump(data,file)
    print("Done")
'''
Uses in 
a. APIs
b. Configuration files 
c. exports 
'''