# Take 2 numbers and handle division by zero
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
try:
  print(num1/num2)
except ZeroDivisionError:
  print("num2 cant be zero")

finally:
  print("program executed successfully")
1