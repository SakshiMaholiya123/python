import numpy as np
data=np.random.randint(100,500,size=(10,90))
print(data)

daily_returns = (data[: ,1:] - data[:, :-1]) / data[:,:-1]
print(f'daily return {daily_returns}')

deviation=np.std(data,axis=1)
print(f"standard deviation per stock{deviation}")

highest_risk=np.argmax(deviation)
print(f"highest risk stock {highest_risk}")