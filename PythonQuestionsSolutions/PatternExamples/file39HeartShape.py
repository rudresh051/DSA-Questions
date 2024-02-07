#  ** ** 
# *  *  *
# *     *
#  *   *
#   * *
#    *

for row in range(6):
  for col in range(7):
    if (row-col==2 and row > 1):
      print("*", end="")
    elif (row+col==8 and col > 3):
      print("*", end="")
    elif (row+col==1 and row < 2):
      print("*", end="")
    elif (col-row==5 and row < 2):
      print("*", end="")
    # elif (row==0 and col==2) or (row==1 and col==3) or (row==0 and col==4):
    #   print("*", end="")
    elif (row==0 and col%3!=0) or (row==1 and col%3==0):
      print("*",end="")
    else:
      print(end=" ")
  print()