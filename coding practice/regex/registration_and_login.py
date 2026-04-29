import re
import json
import os

class Student:
    filename = "students.json"

    def __init__(self):
        self.name = None
        self.address = None
        self.sid = None
        self.password = None

    def register(self):
        name = input("Enter name: ")
        if not re.match(r"^[a-zA-Z ]{3,30}$", name):
            print("Invalid Name")
            return False
        self.name = name

        address = input("Enter address: ")
        if not re.match(r"^[0-9a-zA-Z,./\- ]{10,100}$", address):
            print("Invalid Address")
            return False
        self.address = address

        sid = input("Enter ID: ")
        if not re.match(r"^STU\d{4}$", sid):
            print("Invalid ID")
            return False
        self.sid = sid

        password = input("Enter password: ")
        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[^\s]{8,16}$", password):
            print("Invalid Password")
            return False
        self.password = password

        data = {}
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                try:
                    data = json.load(f)
                except:
                    data = {}

        if self.sid in data:
            print("User already exists")
            return False

        data[self.sid] = self.password

        with open(self.filename, "w") as f:
            json.dump(data, f)

        print("registration Successful")
        return True

    def login(self):
        if not os.path.exists(self.filename):
            print("no users found")
            return

        sid = input("enter ID: ")
        password = input("enter password: ")

        with open(self.filename, "r") as f:
            data = json.load(f)

        if sid in data and data[sid] == password:
            print("login successful")
        else:
            print("invalid ID or password")

user = Student()
success = user.register()

if success:
    print("login")
    user.login()