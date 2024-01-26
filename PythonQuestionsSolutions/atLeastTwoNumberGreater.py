def findElements(self,a, n):
  # Your code goes here
  sorted_a = sorted(a)
  ans = []
  for i in range(0,len(sorted_a)-2,1):
      ans.append(sorted_a[i])
      
  return ans