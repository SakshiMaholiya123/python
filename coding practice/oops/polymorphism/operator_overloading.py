# class A:
#     def __init__(self,num):
#         self.num=num
    
#     def  __add__(self, num2):
#         return self.num+num2.num

# print("with numbers")  
# obj1=A(2)
# obj2=A(6)

# print("with string")
# obj3=A("Sakshi")
# obj4=A("Maholiya")
# print(obj1+obj2)
# print(obj3+ obj4)


class A:
    def __init__(self,num):
        self.num=num
    
    def  __mul__(self, num2):
        return self.num*num2.num

print("with numbers")  
obj1=A(2)
obj2=A(6)
obj3=A("Sakshi ")
print(obj1*obj2)
print(obj2*obj3)
