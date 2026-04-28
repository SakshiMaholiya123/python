import re
text="a ab acd abbd acdb"   #0 or 1
print(re.findall("ab?",text))