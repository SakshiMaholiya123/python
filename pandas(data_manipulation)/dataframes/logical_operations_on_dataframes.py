import pandas as pd

data={"A":[10,20,30,40],'B':[11,12,13,14]}
df=pd.DataFrame(data)
print(df)

df['C']=df['A']<=20
print(df['C'])
print(df)


mask=df['A']==10
print(mask)

print(df[mask]) #gives the only row that satisfied this condition


