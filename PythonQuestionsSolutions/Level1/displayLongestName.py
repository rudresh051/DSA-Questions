class Solution:
    def longest(self, names, n):
    	# code here
    	result = []
    	for i in range(n):
    	    result.append(len(names[i]))
	    
	    max_index = result.index(max(result))
	   # print(max_index)
    	return names[max_index]