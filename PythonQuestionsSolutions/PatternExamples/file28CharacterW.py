# W  W  W
# W W W W
# WW   WW
# W     W

i=0
j=3

for row in range(7):
  for col in range(7):
    if (col==0 and row<4) or (col==6 and row<4) or (row==1 and col==4) or (row==2 and col==5):
      print("W", end="")
    elif (row==i and col==j):
      print("W",end="")
      i=i+1
      j=j-1
    else:
      print(end=" ")
  print()