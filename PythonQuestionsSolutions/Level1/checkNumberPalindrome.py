# User function Template for python3

class Solution:
    def is_palindrome(self, n):
        # Code here

        s1 = str(n)
        s2 = []

    # print(type(s1))

    for i in range(len(s1) - 1, -1, -1):
        s2.append(s1[i])

    # print("s2",s2)

    s3 = "".join(map(str, s2))
    # print("s3",s3)
    # print(type(s3))

    n1 = int(s3)
    # print(type(n1))

    if n == n1:
        return "Yes"
    else:
        return "No"


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution();
        ans = ob.is_palindrome(n)
        print(ans)
# } Driver Code Ends