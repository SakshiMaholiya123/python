import random

n=int(input("Enter number"))
Set=set()
count=0
while len(Set)<n:
    random_number=random.randint(1,n)
    Set.add(random_number)
    count+=1
    

print(count)

