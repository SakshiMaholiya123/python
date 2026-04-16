# writing binary file
with open("file handling/data.bin","wb") as file:
    file.write(b"Hello, World!, this is a binary file that contains the data in 0 and 1 format")

# reading binary file
with open("file handling/data.bin","rb") as file:
    print(file.read())
