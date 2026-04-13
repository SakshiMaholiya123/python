n = int(input("Enter value of N: "))

if n == 0:
    print("N should not be 0")
else:
    harmonic = 0.0

    for i in range(1, n + 1):
        harmonic+=1/i

    print(f"{n}th Harmonic Value = {harmonic}")