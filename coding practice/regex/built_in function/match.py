import re
str="python is object oriented "  #it gives the result only when the target string is present at the begining of the string
res=re.match("python",str)
print(res.group())

