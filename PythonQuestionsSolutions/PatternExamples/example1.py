# Example 1
# input n = 3
# output
# * * *
# * * *
# * * *
n = int(input("Enter number of rows:"))
# for i in range(n):
#     print("* " * n)

# Example 2
# input n = 3
# output
# 3 3 3
# 3 3 3
# 3 3 3
for i in range(n):
    print((str(n) + " ")*n)

# Example 3
# input n = 3
# output
# 1 1 1
# 2 2 2
# 3 3 3
for i in range(n):# 0,1,2
    print((str(i+1) + " ")*n)

# Example 4 Right Angle triangle pattern
# n=4
# output
# A
# B B
# C C C
# D D D D

for i in range(n):
    print(((65+i) + " ")*(i+1))

# Example 5 - Inverted Right triangle
# n=4
# output
# * * * *
# * * *
# * *
# *

for i in range(n):
    print("* "*(n-i))

# Exmaple 6 - Inverted right angle triangle with digits
# n=4
# output
# 1 2 3 4
# 1 2 3
# 1 2
# 1

for i in range(n):
    for j in range(n-i):
        print(j+1, end=" ")
    print()





















