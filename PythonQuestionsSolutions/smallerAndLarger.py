	def getMoreAndLess(self,arr, n, x):
		# code here
		countLess = 0
		countGreater = 0
		for i in range(len(arr)):
		    if arr[i] <= x:
		        countLess = countLess + 1
	        if arr[i] >= x:
	            countGreater = countGreater+1
	   
	    return(countLess,countGreater)