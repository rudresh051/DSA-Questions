#  SSS 
# S
# S
#  SSS
#     S
#     S
#  SSS
for row in range(7):
  for col in range(5):
    if (col==0 and (row>0 and row<3)) or (col==4 and (row>3 and row<6)):
      print("S",end="")
    elif (row==0 and (col>0 and col<4)) or (row==3 and (col>0 and col<4)) or (row==6 and (col>0 and col<4)) :
      print("S",end="")
    else:
      print(end=" ")
  print()