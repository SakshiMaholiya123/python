
import math
def euclidian_distance(x,y):
    return math.sqrt(math.pow(x,2)+math.pow(y,2))

x=int(input("enter value of x"))
y=int(input("enter value of y"))

print("eucildian distance is ",int(euclidian_distance(x,y)))
