n = int(input("Enter value of N (0 <= N < 31): "))

if n < 0 or n >= 31:
    print("Please enter N in range 0 to 30")
else:
    for i in range(n + 1):
        print(f"2^{i} = {2 ** i}")