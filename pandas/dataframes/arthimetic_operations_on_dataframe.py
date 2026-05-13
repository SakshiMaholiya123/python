import pandas as pd

var=pd.DataFrame({'A':[1,2,3,4],'B':[5,6,7,8]})
print(var)


#addition
var['C']=var['A']+var['B']
print(var)

#subtraction
var['C']=var['A']-var['B']
print(var)

#multiplication
var['C']=var['A']*var['B']
print(var)

#division
var['C']=var['A']/var['B']
print(var)