# M     M
# MM   MM
# M M M M
# M  M  M
# M     M
# M     M
# M     M

for row in range(7):
  for col in range(7):
    if (col==0) or (col==6):
      print("M", end="")
    elif (row==col and (col>0 and col<4)):
      print("M",end="")
    elif (row==2 and col==4) or (row ==1 and col==5):
      print("M",end="")
    else:
      print(end=" ")
  print()