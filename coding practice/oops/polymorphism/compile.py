# we can't achive the complite time polymorphism as python is dynamic in nature so we can achieve this similar behaviour 
# using args (variable length arguments)

class Cal:
    def multiply(self,num1=1,num2=2,*args):
        res=num1*num2

        for i in args:
            res*=i
        return res
    
obj=Cal()
print(obj.multiply())
print(obj.multiply(1,2,3,4,5,6))