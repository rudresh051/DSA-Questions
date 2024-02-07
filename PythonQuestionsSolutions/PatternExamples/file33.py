# p
# p y
# p y t
# p y t h
# p y t h o
# p y t h o n

string = input("Enter the string: ")
length = len(string)
# length will be equal to number of rows
for row in range(length):
  for col in range(row+1):
    print(string[col],end="")
  print()
