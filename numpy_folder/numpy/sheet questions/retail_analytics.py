import numpy as np

data=np.random.randint(-50,500,size=(30,5))
print(data)

data[data<0]=0
print(f"after replacing the neagative val with 0 {data}")

week_data=data[:28]
r=week_data.reshape(4,7,5)
average=r.mean(axis=1)
print(f"week average is {average}")

overall_aver=r.mean(axis=0)
print(f"overall average is{overall_aver}")

highest=np.argmax(overall_aver)
print(f"highest average is {highest}")