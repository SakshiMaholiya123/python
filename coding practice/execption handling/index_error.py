# Access an index from list and handle IndexError
list=[1,2,3,"Sakshi",0.8]

try:
   print(list[len(list)])

except IndexError:
  print("Index out of bound error,Enter a proper index value")

finally:
  print("programm ends")
  