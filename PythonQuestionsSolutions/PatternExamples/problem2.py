#User function Template for python3

class Solution:
    def printPattern(self, N):
    	#code here 
    	for i in range(1,N+1):
    	    print("*"*i, end=" ")
    	


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printPattern(N)
        print()
# } Driver Code Ends