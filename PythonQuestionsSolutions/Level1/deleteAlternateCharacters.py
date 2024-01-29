#User function Template for python3
class Solution:
    def delAlternate (ob, S):
        # code here 
        arr = []
        res = []
        for i in range(len(S)):
            arr.append(S[i])
        # print(arr)
        
        for i in range(len(arr)):
            # print(arr[i],i)
            if (i%2==0):
                res.append(arr[i])
            else:
                continue
        # print(res)
        
        res_str = "".join(res)
        return res_str
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S = input()
        
        ob = Solution()
        print(ob.delAlternate(S))
# } Driver Code Ends