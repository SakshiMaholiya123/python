n=int(input("Enter number"))

arr=[]
for i in range(n):
    arr.append(int(input()))


arr.sort()
print("larget element is",arr[-1])

print("smallest element",arr[0])