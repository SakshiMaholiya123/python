import re
# text = "cat cot cut c9t"
# res = re.findall("c.t", text)
# print(res)

text="sakshi"
print(re.findall(r"...i",text))

print(re.findall(r".{2}i",text))
print(re.findall(r"h.$",text))