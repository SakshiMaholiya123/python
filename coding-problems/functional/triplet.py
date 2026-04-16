
def find_triplets(arr, n):
    count = 0
    print("Triplets that sum to 0:")
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):

                if arr[i] + arr[j] + arr[k] == 0:
                    print(arr[i], arr[j], arr[k])
                    count += 1

    return count


n = int(input("Enter number of elements (N): "))
arr = []

for i in range(n):
    arr.append(int(input()))

result = find_triplets(arr, n)

print("Total number of triplets:", result)