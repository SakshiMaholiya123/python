# import re
# text = "My number is 123456789"

# result = re.search(r"\d+", text)

# print(result.group())

import re
str=str(input("enter text"))

res=re.search(r"\d+",str)    #GIVETHE first occurence of the matching string
print(f"result is {res.group()}")