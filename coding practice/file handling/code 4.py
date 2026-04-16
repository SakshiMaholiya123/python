# csv file
# create file and write the data into it
import csv
with open ("file handling/data.csv", "w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["Name","Age"])
    writer.writerow(["Sakshi",21])