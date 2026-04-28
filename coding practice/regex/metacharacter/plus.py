import re
text="a ab abb acd abbfg"
print(re.findall("ab+",text))