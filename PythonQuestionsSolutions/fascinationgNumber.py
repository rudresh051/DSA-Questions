# User function Template for python3
class Solution:

    def fascinating(self, n):
        # code here
        s1 = n * 2
        # print("s1",s1)
        s2 = n * 3
        # print("s2",s2)

        s3 = str(n) + str(s1) + str(s2)
        # print("s3",s3)

        s4 = sorted(s3)
        # print("s4",s4)

        s5 = set(s4)
        # print("s5",s5)

        s6 = list(s5)
        # print("s6",s6)

        s7 = sorted(s6)
        print("s7", s7)

        s8 = "".join(map(str, s7))
        # print(s8)

        if s8 == "123456789":
            return True
        else:
            return False


# {
# Driver Code Starts
# Initial Template for Python 3


if __name__ == "__main__":
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
