import numpy as np
arr=[1,2,3,4,5]
print(f"average {np.mean(arr)}")   # Average
print(f"maximum value {np.max(arr)}")    # Maximum value
print("reshape of an array")
print(np.reshape(arr, (5, 1))) # Change the shape of the data

zeros = np.zeros((2, 3))    #give the zero in 2 rows and 3 columns
print(zeros)
ones = np.ones((2, 3))      #give the one in 2 rows and 3 columns
print(ones)

identity = np.eye(3)   # gives identity matrix
print(identity)

ranges = np.arange(0, 11, 2)   #start is inclusive but end is exclusive
print(f"array from 0 to 10 with stepping 2 {ranges}")

linear = np.linspace(0, 1, 7)
print(linear)

arr = np.array([[1, 2, 3], [4, 5, 6]])   # gives the number of rows and no. of columns
print(arr.shape) 