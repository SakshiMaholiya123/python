import pandas as pd

arr=[10,20,30,40]
s=pd.Series(arr)
print(s)

#changing index of series
p=pd.Series(arr,index=['a','b','c','d'])
print(p)

#dtype
s=pd.Series(arr,dtype=float)
print(s)


x1=pd.Series(12,index=[1,2,3,4,5,6])
x2=pd.Series(12,index=[1,2,3])
print(x1+x2)