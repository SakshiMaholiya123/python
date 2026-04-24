# protected variable or metheds can be accessed in the same class and subclass (child class )and we use _(single underscore )
# for making it protected

class Employee:
    def __init__(self,name,age):
        self.name=name
        self._age=age

class SubEmp(Employee):
    def display_age(self):
        print(self._age)
    
obj=SubEmp("Rose",21)
print(obj.name)
print(obj.display_age())