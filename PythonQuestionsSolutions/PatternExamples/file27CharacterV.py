# V     V
#  V   V
#   V V
#    V
for row in range(7):
  for col in range(7):
    if (row==col and (col<4)):
      print("V", end="")
    elif (row+col==6 and (col>2)):
      print("V",end="")
    else:
      print(end=" ")
  print()