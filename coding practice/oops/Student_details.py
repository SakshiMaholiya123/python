# Create a Student class
# Attributes: name, marks
# Method: display details

class Student_Details:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    # def display(self):
    #     return f"name of the student is {self.name} and the marks is {self.marks}"

student=Student_Details('sakshi',87)
print(student.display())



