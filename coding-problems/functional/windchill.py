import math
def windchill(t,v):
    wind=35.74 + 0.6215*t+((0.4275*t)-35.75)*math.pow(v,0.16)
    return wind

t=float(input("Enter value less than or equal to 50"))
v=float(input("enter value between 3 to 200"))

print(windchill(t,v))