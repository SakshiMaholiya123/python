def sum_of_elements(arr):
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
    return sum

n=int(input("enter number"))

arr=[]
for i in range(n):
    arr.append(int(input()))

print("sum is",sum_of_elements(arr))
