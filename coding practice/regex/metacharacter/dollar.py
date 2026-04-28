
#Matches pattern only at the end of the string

import re
str="python is object oriented " 
res=re.match("python$",str)   # $ dollar symbol is used to to match the specific string at thr end
print(res.group())