#User function Template for python3
# class Solution:
    def scores(self, a, b, cc):
        # Update list cc of length 2 with cc[0] = ca and cc[1] = cb
        # Your code goes here
        # print(a)
        # print(b)
        # print(len(cc))
        cc[0] = 0
        cc[1] = 0
        for val1,val2 in zip(a,b):
            # print(val1,val2)
            if val1>val2:
                cc[0] = cc[0]+ 1
            elif val2 > val1:
                cc[1] = cc[1] + 1
            else:
                continue
            
        return cc[0],cc[1]
        

#{ 
# Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
    	a = [int(x) for x in input().strip().split()]
    	b = [int(x) for x in input().strip().split()]
    	
    	cc = [0, 0]
    	ob = Solution()
    	ob.scores(a, b, cc)
    	print(*cc)
    	
    	T -= 1

if __name__ == "__main__":
    main()

# } Driver Code Ends