import re
text = "My number is 123456789"

result = re.search(r"\d+", text)

print(result.group())