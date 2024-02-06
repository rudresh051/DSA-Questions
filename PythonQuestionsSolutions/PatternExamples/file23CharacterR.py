# RRRR 
# R   R
# R   R
# RRRR
# R   R
# R   R
# R   R

for row in range(7):
  for col in range(5):
    if (col==0) or (col==4 and (row!=0 and row!=3)):
      print("R", end="")
    elif(row==0 and (col>0 and col<4)) or (row==3 and (col>0 and col<4)):
      print("R", end="")
    else:
      print(end=" ")
  print()