# Take input and divide 100 by it
# Handle both ValueError and ZeroDivisionError
num=int(input("Enter a value:"))
try:
  res=100/num
  print(res)
except TypeError:
  print("Enter a valid input,number should be integer")
except ZeroDivisionError:
  print("number cant be zero")
