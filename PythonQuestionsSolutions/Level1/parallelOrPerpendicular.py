#User function Template for python3

class Solution:
    def find(self, A, B):
        # Code here
# 		print("A",A)
# 		print("B",B)

        dotValue = 0
        dotValue = A[0]*B[0] + A[1]*B[1] + A[2]*B[2]
# 		print("dotValue",dotValue)

        crossValue = 0
        crossValue = (A[1]*B[2]-A[2]*B[1])-(A[0]*B[2]-B[0]*A[2])+(A[0]*B[1]-A[1]*B[0])

        crossValueSquare = crossValue*crossValue

        if dotValue==0:
            return 2
        elif crossValueSquare==0:
            return 1
        else:
            return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        A = list(map(int, input().split()))
        B = list(map(int,input().split()))
        ob = Solution()
        ans = ob.find(A, B)
        print(ans)
# } Driver Code Ends