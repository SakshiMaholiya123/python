year = int(input("Enter a 4-digit year: "))
if year < 1000 or year > 9999:
    print("Please enter a valid 4-digit year")
else:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("not a Leap Year")