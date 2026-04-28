import re
# text=input("enter text")
# res=re.sub("sakshi","khushi",text)  #replace the match pattern with the another string
# print(res)



string="sakshi maholiya,sakshi singh,sakshi jha"
pattern="sakshi"
replace="khushi"
res=re.sub(pattern,replace,string,count=2)  #count will change only that number of matching string
print(res)