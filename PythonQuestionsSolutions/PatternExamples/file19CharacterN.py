# N     N
# NN    N
# N N   N
# N  N  N
# N   N N
# N    NN
# N     N
for row in range(7):
  for col in range(7):
    if (col==0) or (col==6):
      print("N",end="")
    elif (row==col):
      print("N", end="")
    else:
      print(end=" ")
  print()