#     * 
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
# first for loop for upper pyramid and second for loop for lower pyramid
def pyramid(rows):
  for i in range(rows):
    print(' '*(rows-i-1)+'* '*(i+1))
  for j in range(rows-1,0,-1):
    print(' '*(rows-j)+'* '*(j))

pyramid(5)