#User function Template for python3
class Solution:
    def to_upper(self, str):
        # code here
        str1 = str.upper()
        return str1
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        str = input().strip()
        ob = Solution()
        print(ob.to_upper(str))
# } Driver Code Ends