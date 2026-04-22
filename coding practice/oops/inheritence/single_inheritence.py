class Parent:
    def show(self):
        print("parent class method")

class Child(Parent):    #child class contains the parent class method also
    def fun(self):
        print("child class method")
    

obj=Child()
obj.show()
obj.fun()