#User function Template for python3

class Solution:
	def reverse_digit(self, n):
		# Code here
		str1 = str(n)
# 		print("str1",str1)
		list1 = list(str1)
# 		print("list1",list1)
		rev = []
		for i in range(len(list1)-1,-1,-1):
		    rev.append(list1[i])
	   # print("rev",rev)
	    
	    for i in range(len(rev)):
            if rev[i]=='0':
                continue
            elif rev[i]!='0':
                index = i
                break

        # print("index",i)
        
        result = rev[index:len(rev)]
        # print(rev[index:len(rev)-1])
        return "".join(result)
	    
	   
	            
	            
		    
	
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.reverse_digit(n)
		print(ans)
# } Driver Code Ends