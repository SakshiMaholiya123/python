#method overriding

class Parent:
    def show(self):
        return "parent class"
class Child(Parent):
    def show(self):
        return "child class"
    
obj1=Parent()
print(obj1.show())
print("----")
obj2=Child()
print(obj2.show())