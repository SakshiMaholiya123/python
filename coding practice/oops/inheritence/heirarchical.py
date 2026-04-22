class Parent:
    def show(self):
        print("parent class method")

class Child_1(Parent):
    def fun1(self):
        print("child_1 class method")


class Child_2(Parent):
    def fun2(self):
        print("child_2 class method")

obj1=Child_1()
obj2=Child_2()

obj1.fun1()
obj1.show()
print("-------------")
obj2.show()
obj2.fun2()