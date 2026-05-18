import numpy as np
arr=[1,2,3,4,5]   #instead of looping , to perform same operation on each element of array  we use Vectorization 
numpy_arr=np.array(arr)
new_arr=numpy_arr+10
print(new_arr)

new_arr=numpy_arr*10
print(new_arr)

new_arr=numpy_arr/10
print(new_arr)


new_arr=numpy_arr//10
print(new_arr)