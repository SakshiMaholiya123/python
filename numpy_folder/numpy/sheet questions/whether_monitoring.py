import numpy as np
temp=np.random.randint(10,50,size=(7,24))
print(temp)
max_variation=0
day=0
for i in range(len(temp)):
    print(f"maximum temp of {i+1} day {temp[i].max()}")
    print(f"minimum temp of {i+1} day {temp[i].min()}")
    variation=temp[i].max()-temp[i].min()
    if variation>max_variation:
        max_variation=variation
        day+=1

print(f"day {day} with highest variation in temp {max_variation}")

mean=np.mean(temp)
std=np.std(temp)
lower_bound=mean-2*std
upper_bound=mean+2*std
data=np.where((temp<lower_bound) | (temp>upper_bound),mean,temp)
print(f"data after replace the outliers with mean{data}")



