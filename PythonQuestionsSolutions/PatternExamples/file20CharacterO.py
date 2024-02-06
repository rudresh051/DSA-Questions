#  OOOOO 
# O     O
# O     O
# O     O
# O     O
# O     O
#  OOOOO

for row in range(7):
  for col in range(7):
    if (col==0 and (row!=0 and row!=6)) or (col==6 and (row!=0 and row!=6)):
      print("O",end="")
    elif (row==0 and (col!=0 and col!=6)) or (row==6 and (col!=0 and col!=6)):
      print("O",end="")
    else:
      print(end=" ")
  print()