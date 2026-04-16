#exceptional handling in file handling
try:
    file=open("file handling/text.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Program executed ")
