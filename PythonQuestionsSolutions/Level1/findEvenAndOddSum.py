#User function Template for python3

class Solution:
	def find_sum(self, n):
		# Code here
		evenSum = 0
		oddSum = 0
		
		for i in range(1,n+1):
		  #  print(i)
		    if i%2==0:
		        evenSum = evenSum+i
	        else:
	            oddSum = oddSum+i
        return oddSum,evenSum



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.find_sum(n)
		for _ in ans:
			print(_, end=" ")
		print()
# } Driver Code Ends