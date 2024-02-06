# Y   Y
#  Y Y
#   Y
#   Y
#   Y
for row in range(5):
  for col in range(5):
    if (col==2 and row >1):
      print("Y", end="")
    elif (row==col and col<2) or (row+col==4 and col>1):
      print("Y", end="")
    else:
      print(end=" ")
  print()