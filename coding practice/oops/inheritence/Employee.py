class Employee:
    def details(self,id,name):
        self.id=id
        self.name=name
        return f"employee id is {self.id} and  name is {self.name}"

class Fun(Employee):
    def details(self, id, name,email):
        self.email=email
        return super().details(id, name),self.email

obj1=Employee()  
print(obj1.details(1,"sakshi"))  
print("--------------------------------")

obj=Fun()
print(obj.details(1,"sakshi","sakshi@gmail.com"))
        