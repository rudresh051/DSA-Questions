#User function Template for python3

class Solution:
    def mean(self, N , A):
        # code here 
        sum = 0
        
        for elem in range(len(A)):
            sum = sum+A[elem]
        # print(sum)
        
        return sum//N
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        A = list(map(int,input().split()))
        
        ob = Solution()
        print(ob.mean(N,A))
# } Driver Code Ends