import re
email = input("enter mail")
pattern = r"^\w+@\w+\.\w+$"

if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")