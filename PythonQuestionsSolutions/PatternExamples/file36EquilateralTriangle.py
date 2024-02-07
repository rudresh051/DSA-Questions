#    *   
#   * *
#  *   *
# *******
for row in range(1,5):
  for col in range(1,8):
    if (row==4) or (row+col==5 and row < 4):
      print("*", end="")
    # elif (row==2 and col==5) or (row==3) and (col==6):
    #   print("*", end="")
    elif (col-row==3):
      print("*", end="")
    else:
      print(end=" ")
  print()
