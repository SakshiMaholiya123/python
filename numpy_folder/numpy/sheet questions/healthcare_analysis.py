import numpy as np

data=np.random.randint(40,120,size=(60,24))
print(data)

avg=data.mean(axis=0)
print(f"hourly average heart rate{avg}")

abnormal_reading=data[(data<60) | (data>100)]

print(f"abnormal reading {abnormal_reading}")

