# User function Template for python3

class Solution:
    def splitString(ob, S):
        # code here
        letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        numbers = set('1234567890')
        sp = set("!@#$%^&*():;+_?\/'-")

        s1 = []
        s2 = []
        s3 = []

        for i in range(len(S)):
            if S[i] in letters:
                s1.append(S[i])
            elif S[i] in numbers:
                s2.append(S[i])
            else:
                s3.append(S[i])
        return "".join(s1), "".join(s2), "".join(s3)


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        S = input()
        ob = Solution()
        ans = ob.splitString(S)
        for i in ans:
            if (i == ""):
                print(-1)
            else:
                print(i)

# } Driver Code Ends