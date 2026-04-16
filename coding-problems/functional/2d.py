
def array(arr, m, n):
    for i in range(m):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()  

m = int(input("Enter number of rows" ))
n = int(input("Enter number of columns" ))

arr = []


for i in range(m):
    row = []
    for j in range(n):
        value = int(input())
        row.append(value)
    arr.append(row)
    
array(arr, m, n)