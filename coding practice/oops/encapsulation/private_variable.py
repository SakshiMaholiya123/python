# in employee class we cant access thr salary because it is private in nature to make it private ,we use__(double underscore)

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
        print(" inside class", self.__salary) # inside a class it will give result

ob=Employee("Khushi",30000)
print(ob.name)
# print(ob.__salary)   #this line is giving error as salary is private and we are accessing it outside the class



# name mangling prevetns name conflict in classes and it is done by interpreter
# name is transfered into = _classname__identifier
#but we can acces it 

print(ob._Employee__salary)  #access using name mangling 

#name mangling is useful when we work with inheritence as it prevents subclass to accidently override the important methods
