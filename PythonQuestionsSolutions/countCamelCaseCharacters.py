#User function Template for python3

class Solution:
    def countCamelCase (self,s):
        # your code here
        
        # count = 0
        # for i in range(len(s)):
        #     if s[i] in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 
        #     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
        #         count = count+1
        #     else:
        #         pass
        # return count
        
        # Method2 - Optimized
        set1 = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        # print(set(s))
        count = 0
        for i in range(len(s)):
            if s[i] in set1:
                count=count+1
            else:
                continue
        return (count)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    print (ob.countCamelCase (s))

# Contributed By: Pranay Bansal

# } Driver Code Ends