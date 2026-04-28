import re
text=str(input("enter text"))
str=str(input("enter string"))
res=re.search(str,text)
print(res)