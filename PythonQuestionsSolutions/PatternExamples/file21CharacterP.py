# PPPPP
# P   P
# P   P
# PPPPP
# P
# P
# P
for row in range(7):
  for col in range(5):
    if (col==0) or (col==4 and row<4):
      print("P",end="")
    elif (row==0 and (col>0 and col<4)) or (row==3 and (col>0 and col<4)):
      print("P", end="")
    else:
      print(end=" ")
  print()