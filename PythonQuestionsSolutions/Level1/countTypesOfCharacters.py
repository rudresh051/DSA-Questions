#User function Template for python3

class Solution:
    def count (self,s):
        # your code here
        low=set('abcdefghijklmnopqrstuvwxyz')
        up=set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        sp = set("!@#$%&^*(),;:'_?{}[]<>=+-")
        num = set('1234567890')
        
        countLow = 0
        countUp = 0
        countSp = 0
        countNum = 0
        
        for i in range(len(s)):
            if s[i] in low:
                countLow = countLow+1
            elif s[i] in up:
                countUp = countUp+1
            elif s[i] in num:
                countNum = countNum+1
            else:
                countSp = countSp +1

                
        
        return (countUp,countLow,countNum,countSp)
        

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