import math
def quadratic(a,b,c):
    delta= b*b-4*a*c
    root1= (-b+ math.sqrt(delta))/(2*a)
    root2= (-b - math.sqrt(delta))/(2*a)
    return root1,root2

a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
print(quadratic(a,b,c))