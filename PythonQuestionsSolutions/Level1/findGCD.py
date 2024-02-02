#User function Template for python3
import math
class Solution:
    def gcd(self, A, B):
        # code here
        
        temp = math.gcd(A,B)
        return temp


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        A,B = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.gcd(A,B))
# } Driver Code Ends