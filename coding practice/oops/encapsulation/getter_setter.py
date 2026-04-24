# class Employee:
#     def __init__(self):
#         self.__salary=1000      its not pythonic in nature


#     def get_salary(self):
#          return self.__salary
    
#     def set_salary(self,amt):
#         if amt>0:
#             self.__salary+=amt

#         else:
#             print("invalid amount")


# obj=Employee()
# print(obj.get_salary())

# obj.set_salary(540)

# print(obj.get_salary())


class Employee:
    def __init__(self):
        self.__salary=1000

    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self,amt):
        if amt>0:
            self.__salary+=amt

        else:
            print("invalid amt")

obj=Employee()
print(obj.salary)
obj.salary=4000
print(obj.salary)
