# *****
#  *  *
#   * *
#    **
#     *
n = int(input("enter the number of row"))

for row in range(0,n):
  for col in range(0,n):
    if (row==0) or (col==n-1) or (row==col and (col>0 and col<n)):
      print("*", end="")
    else:
      print(end=" ")
  print()