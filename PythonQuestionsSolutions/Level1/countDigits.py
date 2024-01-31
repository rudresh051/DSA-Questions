# User function Template for python3


class Solution:
    def evenlyDivides(self, N):
        # code here
        res = []
        num1 = str(N)
        for i in range(len(num1)):
            res.append(num1[i])

        count = 0

        for i in range(len(res)):
            temp = int(res[i])
            if int(res[i]) == 0:
                continue
            elif N % temp == 0:
                count = count + 1
            else:
                continue

        return count


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends