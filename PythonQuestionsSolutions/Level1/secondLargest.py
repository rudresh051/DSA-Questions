# User function Template for python3
class Solution:
    def print2largest(self, arr, n):
        # code here
        # 		print("arr",arr)
        set1 = set(arr)
        list1 = list(set1)
        # 		print("list1",list1)
        sorted_list1 = sorted(list1)
        # 		print("sorted_list1",sorted_list1)

        if len(sorted_list1) >= 2:
            return sorted_list1[len(sorted_list1) - 2]
        else:
            return -1


# {
# Driver Code Starts
# Initial Template for Python 3
if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
