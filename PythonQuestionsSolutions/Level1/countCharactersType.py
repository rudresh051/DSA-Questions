#User function Template for python3

class Solution:
    def count (self,s):
        # your code here
        low=set('abcdefghijklmnopqrstuvwxyz')
        up=set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        sp = set('!@#$%&^*()')
        num = set('123456789')
        
        countLow = 0
        countUp = 0
        countSp = 0
        countNum = 0
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    res = ob.count (s)
    
    for i in res:
        print (i)
    
# Contributed By: Pranay Bansal

# } Driver Code Ends