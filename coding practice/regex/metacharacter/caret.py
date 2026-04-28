import re
str="python is object oriented " 
res=re.match("^python",str)    # ^ caret symbol is used to to match the specific string at thr begininnng
print(res.group())
