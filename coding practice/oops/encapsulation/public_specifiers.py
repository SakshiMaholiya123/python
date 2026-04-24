#public specifier can be accessed from anywhere ,from outside of class and from other module and in python by default
#  all the variables and methods are public in nature 

class Student:
    def __init__(self,name):
        self.name=name

    def display_name(self):
        return self.name

obj=Student("Sakshi")
print(obj.display_name())

        
