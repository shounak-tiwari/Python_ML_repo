# Name = "Akash"
# /\//\\
import re
# match
phoneType = r"^\d{3}-\d{3}-\d{4}$"
type  = "^[A-Z][a-z]{2,}$"
Name ="Akash122"
Phone = "871-882-8288"
if re.match(type,Name):
    if re.match(phoneType,Phone):
        print("All valid")
    else:
        print("Contact is invalid")
else:
    print("Invalid name")