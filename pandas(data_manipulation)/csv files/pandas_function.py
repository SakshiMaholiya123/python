import pandas as pd
import numpy as np

csv_file=pd.read_csv("C:\\Users\\DELL\\Downloads\\sample_data_25x5.csv")
# print(csv_file)

print(type(csv_file))
# to get index
print(csv_file.index)

#to get column
print(csv_file.columns)

print(csv_file.shape) #give number of rows and columns


#to get all the values like min ,max ,count etc(works on numerical columns)
print(csv_file.describe())

#to get the starting 5 rows data
print(csv_file.head())

print(csv_file.head(15))   #give the starting 15 rows data

print(csv_file.tail())  #to get the last rows data

print(csv_file.info()) #gives all the information related to it

print(csv_file.index.array)  #returns the array containg index

print(csv_file.to_numpy())  #convert the csv file data into numpy array

print(np.asarray(csv_file))


#sorting based on index (ascending or descending)
print(csv_file.sort_index(axis=0,ascending=False))

