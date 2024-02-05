# *
# * * *
# * * * * *

# here we can see there is no change in rows
# There is change in columns

num = int(input("Enter the number of rows"))
k=1
for i in range(1,num+1):
  for j in range(1,k+1):
    print("*",end=" ")
  k=k+2
  print()