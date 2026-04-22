class Parent:
    def show(self):
        print("this is parent class method")

class Child(Parent):
    def show(self):
        super().show()
        print("this is child class method")



obj_1=Parent()
obj_1.show()
print("--------------------------------------")


#child class obj ,and will execute the child class method

obj=Child()
obj.show()