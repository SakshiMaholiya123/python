import pandas as pd
data={'name':['sakshi','nisha','khushi'],    #if the data is unbalanced in dataframe using dictionary ,it will give error
      'marks':[87,89,90]}
d=pd.DataFrame(data)
print(d)

k=pd.DataFrame(data.keys())
print(k)

v=pd.DataFrame(data.values())
print(v)



# data frames attributes
print(d.shape)    #gives number of rows and columns

print(f"columns are {d.columns}")   # to get the columns names

var=pd.DataFrame(data,columns=['name'])   #get the all data of the specific column
print(var)

print(f"index are {d.index}")  #gives the index range

var1=pd.DataFrame(data,index=['a','b','c'])  #index value gets changed 
print(var1)

#to get the data of specific position
print(d["name"][1])

print(f"datatypes are {d.dtypes}")    

print(len(d))

print(d.iloc[1])  #to fetch the row from data frame

print(d.iloc[:,1])
