#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        # print("k",k)
        # print("n",n)
        # print(len(arr)-1)
        count = 0
        for i in range(len(arr)):#0,1,2,3
            # print("i",i)
            x = 0
            x = x+i
            for j in range(x+1,len(arr),1):
                # print("j",j)
                if arr[i]+arr[j]==k:
                    count = count+1
                else:
                    continue
        return count
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends