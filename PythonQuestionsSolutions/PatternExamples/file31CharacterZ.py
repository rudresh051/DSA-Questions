# ZZZZZZ
#     Z
#    Z
#   Z
#  Z
# ZZZZZZ

for row in range(6):
  for col in range(6):
    if (row==0) or (row==5) or (row+col==5 and (col>0 and col<5)):
      print("Z", end="")
    else:
      print(end=" ")
  print()