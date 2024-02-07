#   *  
#  * *
# *   *
#  * *
#   *

for row in range(0,5):
  for col in range(0,5):
    if (row+col==2):
      print("*",end="")
    elif (row-col==2):
      print("*",end="")
    elif (col-row==2):
      print("*",end="")
    elif (row+col==6):
      print("*",end="")
    else:
      print(end=" ")
  print()