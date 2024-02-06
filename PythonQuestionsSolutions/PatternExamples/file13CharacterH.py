# HHHHH
#   H
#   H
#   H
#   H
#   H
# HHHHH

for row in range(7):
  for col in range(5):
    if (col==2) or ((row==0 or row==6) and (col==0 or col==1 or col==3 or col==4)):
      print("H", end="")
    else:
      print(end=" ")
  print()