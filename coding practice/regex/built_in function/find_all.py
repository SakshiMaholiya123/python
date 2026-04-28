import re
text = "I have 2 apples and 5 bananas"   # find all matches in the string ans return them as list
result = re.findall(r"\d+", text)
print(result)