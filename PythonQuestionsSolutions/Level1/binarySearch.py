# User function template for Python
import math


class Solution:
    def binarysearch(self, arr, n, k):
        # code here
        # print(arr)
        low = 0
        high = n - 1
        # initialize low and high for the array start the while loop
        while low <= high:
            mid = math.floor((low + high) / 2)
            if arr[mid] == k:
                return mid
            elif arr[mid] > k:
                high = mid - 1
            else:
                low = mid + 1

        return -1
