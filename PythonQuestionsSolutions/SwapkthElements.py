class Solution:
	
	def swapKth(self,arr, n, k):
		# code here
# 		print(arr[k-1])
# 		print(len(arr)-k)
		arr[k-1]
		arr[len(arr)-k]
		#Now swap using temp variable
		temp = arr[k-1]
		arr[k-1] = arr[len(arr)-k]
		arr[len(arr)-k] = temp
		return arr