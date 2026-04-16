# file handling in json 
import json
data={"name":"Sakshi",
      "age":21,
      "city":"Mathura"}
with open("file handling/data.json","w") as file:
    json.dump(data,file)