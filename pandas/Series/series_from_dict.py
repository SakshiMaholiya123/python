import pandas as pd

data={'a':100,'b':200,'c':300}
s=pd.Series(data)               # printing series of dictionary
print(s)
k=pd.Series(data.keys())      # printing keys from dictionary using series
print(k)

v=pd.Series(data.values())     # printing values from dictionary using series
print(v)