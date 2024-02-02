#User function Template for python3
import math
class Solution:
    def gcd(self, A, B):
        # code here
        
        temp = math.gcd(A,B)
        return temp
    

        # Method 2
        # if A>B:
        #     min = B
        # else:
        #     min=A
            
        # for i in range(1,min+1):
        #     if A%i==0 and B%i==0:
        #         hcf=i
        
        # return hcf


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