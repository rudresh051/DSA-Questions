# User function Template for python3

# User function Template for python3
class Solution:
    def armstrongNumber(self, n):
        # code here
        s1 = str(n)
        num = []
        for i in range(len(s1)):
            num.append(s1[i])

        d1 = int(num[0])
        d2 = int(num[1])
        d3 = int(num[2])

        c1 = d1 * d1 * d1
        c2 = d2 * d2 * d2
        c3 = d3 * d3 * d3

        check = c1 + c2 + c3

        if check == n:
            return 'Yes'
        else:
            return 'No'


# {
# Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends