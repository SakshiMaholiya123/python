class Parent:
    def display(self):
        return "parent method"

class Child(Parent):
    def display(self):
        return Parent.display(self) ,"child class method"  # we can do it using super also

        return f"{super().display()} child method"
    

obj=Child()
print(obj.display())