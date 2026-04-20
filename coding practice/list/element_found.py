def element(arr, key):
    for num in arr:
        if num == key:
            return True
    return False

arr = [1, 2, 3, 4]
print("Found", element(arr, 3))