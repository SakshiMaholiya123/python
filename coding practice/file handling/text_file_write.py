# writing file content
# method 1
# f = open("file handling/text.txt", "w")
# f.write("Hello world")
# f.close()

# method 2
# with open ("file handling/text.txt","w") as f:
#     f.write("Hello world")



with open("file handling/text.txt","a") as file:
    file.write("hello this is the text file")


# with open("file handling/data.json","r") as file:
#     print(file.read())

