import numpy as np

data=np.random.randint(1,6,size=(100,4))
print(data)

#min max normalisation

normalisation=(data-data.min())/(data.max()-data.min())

print(f"min max normalisation{normalisation}")

average=data.mean(axis=1)
print(f"average per employee {average}")

company_avg=average.mean()
list=[]
for i in range(len(average)):
    if average[i]>company_avg:
        list.append(float(average[i]))

print(f"employee having more average than company mean{list}")