# Part 1: Registration
# Write a program that takes the following input from the user:
# Student name
# Student address
# Student ID
# Password
# The program must validate each field using regex before registration is successful.

# Registration rules
# Student name: Must contain only letters and spaces, and length should be 3 to 30 characters.
# Address: Must contain letters, numbers, spaces, commas, periods, hyphens, and slashes, and length should be 10 to 100 characters.
# Student ID: Must start with STU followed by exactly 4 digits, for example STU1024.
# Password: Must be 8 to 16 characters long and contain at least one uppercase letter, one lowercase letter, one digit, one special character, and no spaces.
# If all fields are valid, store the student ID and password in variables and print:
# Registration successful
# Otherwise, print the correct error message for the invalid field.
import re
student_name=(input("Enter your name "))
student_address=input("Enter address ")
student_id=input("enter your id ")
password=input("enter password ")

name_pattern=r"^[a-zA-Z ]{3,30}$"
address_match=r"^[0-9a-zA-Z, -/.]{10,100}$"
studentid_match=r"^STU\d{4}"
password_match=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$"

if  not re.match(name_pattern,student_name):
    print("invalid name")

elif  not re.match(studentid_match,student_id):
    print("invalid id")

elif  not re.match(address_match,student_address):
    print("invalid adress")

elif  not re.match(password_match,password):
    print("invalid password")

else:
    id=student_id
    password_stored=password
    print(f"Registration successful")


print("for login ")
id=input("enter your id ")
check_password=input("enter the password ")

if   re.match(id,student_id) and re.match(check_password,password):
    print('Login Successful')

else:
    print("Invalid student ID or password")
