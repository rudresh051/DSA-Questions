#User function Template for python3

class Solution:
    def streamAvg(self, arr, n):
        # code here
        res = []
        count = 1
        sum = 0
        for i in range(len(arr)):
            sum = sum+arr[i]
            mean = sum/count
            res.append(mean)
            count = count+1

        return res

#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.streamAvg(arr, n)
        for x in ans:
            print('%.2f'%x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends