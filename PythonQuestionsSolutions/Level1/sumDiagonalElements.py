#User function Template for python3

class Solution:
    def DiagonalSum(self, matrix):
        # Code here
        sum = 0
        for i in range(len(matrix)):
            sum = sum + matrix[i][i] + matrix[i][len(matrix)-1-i]
        

	return sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int,input().split())))
        ob = Solution()
        ans = ob.DiagonalSum(matrix)
        print(ans)
# } Driver Code Ends