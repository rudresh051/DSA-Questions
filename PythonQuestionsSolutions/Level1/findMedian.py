#User function Template for python3
from math import floor
class Solution:
    def find_median(self, v):
        # Code here
# 		print(v)
        v_sorted = sorted(v)
# 		print(v_sorted)
        size = len(v_sorted)
# 		print(size)

        if size%2==1:
            medianIndex = floor((size)//2)
          #  print("medianIndex",medianIndex)
            value = v_sorted[medianIndex]
            return (value)
        elif size%2==0:
            medianIndex1 = (size-1)//2
            medianIndex2 = (size+1)//2
            value = (v_sorted[medianIndex1]+v_sorted[medianIndex2])/2
            return floor(value)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        v = list(map(int,input().split()))
        ob = Solution();
        ans = ob.find_median(v)
        print(ans)
# } Driver Code Ends