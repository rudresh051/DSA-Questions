#  QQQ 
# Q   Q
# Q   Q
# Q   Q
# QQ  Q
# QQQQQ
#    Q

for row in range(7):
  for col in range(5):
    if (col==0 and (row>0 and row <6)) or (col==4 and (row>0 and row <6)):
      print("Q",end="")
    elif (row==0 and (col>0 and col<4)) or (row==5 and (col>0 and col<4)):
      print("Q",end="")
    elif (row==4 and col==1) or (row==6 and col==3):
      print("Q",end="")
    else:
      print(end=" ")
  print()