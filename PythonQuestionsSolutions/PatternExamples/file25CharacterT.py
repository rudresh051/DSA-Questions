# TTTTT
#   T
#   T
#   T
#   T
#   T
#   T

for row in range(7):
  for col in range(5):
    if (row==0) or (col==2 and row>0):
      print("T", end="")
    else:
      print(end=" ")
  print()