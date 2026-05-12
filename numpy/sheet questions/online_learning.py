import numpy as np
data=np.random.randint(0,300,size=(6,14))

print(data)
for i in range(len(data)):
    print(f"time spent on {i+1} course {np.sum(data[i])}")

avg=data.mean(axis=1)
threshold=120
list=[]
for i in range(len(avg)):
    if avg[i]>threshold:
        list.append(i+1)

print(f"courses whose mean exceeds threshold{list}")

rank=np.argsort(avg)
print(f"it gives the rank of the courses from highest to lowest{rank+1}")
