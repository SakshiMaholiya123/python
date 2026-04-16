# reading json file content
import json
with open("file handling/data.json","r") as file:
    data=json.load(file)
    print(data)