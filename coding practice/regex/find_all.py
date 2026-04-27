import re
text = "I have 2 apples and 5 bananas"
result = re.findall(r"\d+", text)
print(result)