# Access key from dictionary and handle KeyError
dict={"1":"Sakshi","2":"Maholiya"}
try:
  key=input("Enter key")
  print(dict[key])
except KeyError:
  print("Key not found in the dictionary")