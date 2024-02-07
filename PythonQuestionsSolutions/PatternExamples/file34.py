# 12345
# 1234
# 123
# 12
# 1
n = int(input("enter the number of rows"))

for row in range(n,0,-1):
  for col in range(1,row+1):
    print(col,end="")
  print()


for row in range(n,0,-1):
  for col in range(1,row+1):
    print(row,end="")
  print()

# 55555
# 4444
# 333
# 22
# 1