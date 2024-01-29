# User function Template for python3
class Solution:

    def fascinating(self, n):
        # code here
        s1 = n * 2
        s2 = n * 3
        s3 = str(n) + str(s1) + str(s2)

        if len(s3) > 9:
            return False

        elif set(s3) == set('123456789'):
            return True


# {
# Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input().strip())
        ob = Solution()
        ans = ob.fascinating(n)
        if ans:
            print("Fascinating")
        else:
            print("Not Fascinating")
        tc -= 1

# } Driver Code Ends