import pandas as pd
data={'name':['sakshi','nisha','khushi'],
      'marks':[87,89,90]}
d=pd.DataFrame(data)
print(d)

k=pd.DataFrame(data.keys())
print(k)

v=pd.DataFrame(data.values())
print(v)


# data frames attributes
print(d.shape)    #gives number of rows and columns

print(f"columns are {d.columns}")    #

print(f"index are {d.index}")

print(f"datatypes are {d.dtypes}")    

print(len(d))

