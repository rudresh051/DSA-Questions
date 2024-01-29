# User function Template for python3

class Solution:
    def DiagonalSum(self, matrix):
        # Code here
        row = n

    # 		print("row",row)
    # 		print("matlen",len(matrix))
    col = n
    sum = 0
    for row in range(len(matrix)):
        print("row", row)
        for val in row:
            print("val", val)
            if row == col:
                sum = sum + val

    return sum


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        ob = Solution()
        ans = ob.DiagonalSum(matrix)
        print(ans)
# } Driver Code Ends