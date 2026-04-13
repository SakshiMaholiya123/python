n = int(input("Enter a number: "))

if n <= 1:
    print("No prime factors")
else:
    print("Prime factors are:")

    while n % 2 == 0:
        print(2, end=" ")
        n = n // 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            print(i, end=" ")
            n = n // i
        i += 2
    if n > 2:
        print(n, end=" ")