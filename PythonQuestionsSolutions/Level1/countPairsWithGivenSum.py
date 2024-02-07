#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        # print("k",k)
        
        i=0
        j=i+1
        count = 0
        for i in range(len(arr)):
            # print("arr[i]",arr[i])
            for j in range(len(arr)-2):
                if arr[i]+arr[j]==k:
                    print("arr[i] an arr[j] values are", arr[i],arr[j])
                    count=count+1
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