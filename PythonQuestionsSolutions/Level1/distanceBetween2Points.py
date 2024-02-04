#User function Template for python3
import math
class Solution:
	def distance(self, x1, y1, x2, y2):
		# Code here
		
		x = (x2-x1)*(x2-x1)
		y = (y2-y1)*(y2-y1)
		
		sum = x+y
		return round(math.sqrt(sum))
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		x1, y1, x2, y2 = input().split()
		x1 = int(x1);
		y1 = int(y1);
		x2 = int(x2);
		y2 = int(y2);
		ob = Solution();
		ans = ob.distance(x1, y1, x2, y2)
		print(ans)
# } Driver Code Ends