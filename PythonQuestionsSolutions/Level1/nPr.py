#User function Template for python3

class Solution:
    def nPr(self, n, r):
        # code here
        
        nFactorial = 1
        for i in range(1,n+1,1):
            nFactorial = nFactorial*i
            
        nMinusR = n-r
        # print("nMinusR",nMinusR)
        
        nMinusR_Factorial=1
        for i in range(1,nMinusR+1,1):
            nMinusR_Factorial = nMinusR_Factorial*i
        
            
        # print("nMinusR_Factorial",nMinusR_Factorial)
        # print("nFactorial",nFactorial)
        
        return nFactorial//nMinusR_Factorial


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nPr(n, r))
# } Driver Code Ends