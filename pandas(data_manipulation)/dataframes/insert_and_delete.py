import pandas as pd

data={'a':[1,2,3,45],'b':[3,4,5,6]}
d=pd.DataFrame(data)
print(d)

d.insert(1,'c',['s','d','q','w'])
print(d)


d.insert(1,'column_1',d['a'])
print(d)

d['column_2']=d['a'][:3]
print(d)


#delete
d.pop('b')
print(d)

d.drop('c',axis=0)
print(d)

del d['a']
print(d)