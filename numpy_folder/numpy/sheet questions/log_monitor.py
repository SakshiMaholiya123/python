import numpy as np
data=np.random.randint(0,100,size=1440)
print(data)

peak_minutes=np.max(data)
peak_hrs=peak_minutes//60
print(f" peak traffic hrs {peak_hrs}:00")

wnd_size=5
mvg_avg=np.convolve(data,np.ones(wnd_size)/wnd_size)

