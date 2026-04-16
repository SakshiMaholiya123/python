import random
num=int(input("Enter number: "))
if(num<=0):
    print("Enter a positive number")
heads=0
tails=0
for i in range(num):
    random_num=random.random()
    if(random_num<0.5):
        tails+=1
    else:
        heads+=1
print("heads percent",(heads/num)*100)
print("tails percent ",(tails/num)*100)

        
