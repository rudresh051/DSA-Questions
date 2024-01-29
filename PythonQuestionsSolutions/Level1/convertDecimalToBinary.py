# User function Template for python3
import math


class Solution:
    def getBinaryRep(self, n):
        # code here
        binary = ""

        if n == 0:
            return 0

    while n > 0:
        remainder = math.floor(n % 2)
        # print("remainder",remainder)
        binary = str(remainder) + binary
        n = n // 2

    # print(len(binary))
    size = len(binary)
    # return binary

    rep = "0"
    if len(binary) == 30:
        return binary
    else:
        for i in range(30 - size - 1):
            rep = "0" + rep
    # print(rep)

    return rep + binary


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution();
        ans = ob.getBinaryRep(n)
        print(ans)

# } Driver Code Ends