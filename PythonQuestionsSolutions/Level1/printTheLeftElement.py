# User function Template for python3
import math


class Solution:
    def leftElement(self, arr, n):
        # Your code goes here
        arr_sorted = sorted(arr)
        # print(arr_sorted)
        # for i in range(len(arr_sorted)-1):
        #     if i%2==0:
        #         arr_sorted.pop()
        #     else:
        #         arr_sorted.pop(0)

        # s1 = "".join(map(str,arr_sorted))
        # return s1

        # Method 2 - Optimized
        size = (len(arr_sorted))

        if size % 2 == 0:
            return arr_sorted[(size // 2) - 1]
        else:
            return arr_sorted[math.floor(size / 2)]


# {
# Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())

    while (T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.leftElement(a, n))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends