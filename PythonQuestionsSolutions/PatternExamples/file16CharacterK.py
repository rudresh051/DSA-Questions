# K   K
# K  K
# K K
# KK
# K K
# K  K
# K   K
# Method1
# for row in range(7):
#   for col in range(5):
#     if (col==0) or (row==3 and col==1) or (row==2 and col==2) or (row==1 and col==3) or (row==0 and col==4) or (row==4 and col==2) or (row==5 and col==3) or (row==6 and col==4):
#       print("K", end="")
#     else:
#       print(end=" ")
#   print()

#Method 2

i=0
j=4
for row in range(7):
  for col in range(5):
    if (col==0) or (row ==col+2 and col>1):
      print("K", end="")
    elif (row==i and col==j):
      print("K",end="")
      i = i+1
      j= j-1
    else:
      print(end=" ")
  print()
