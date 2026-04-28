import re
text=str(input("enter text"))
target_str=str(input("enter text"))
res=re.finditer(target_str,text)
for i in res:
    print(i)