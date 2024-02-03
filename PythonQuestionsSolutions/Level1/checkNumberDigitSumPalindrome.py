#User function Template for python3

class Solution:
    def isDigitSumPalindrome(self,N):
        #code here
        str1 = str(N)

        sum = 0
        for i in range(len(str1)):
            # print("str1",str1[i])
            sum = sum + int(str1[i])
        # print("sum",sum)
        
        str2 = str(sum)
        arr2 = []
        
        for i in range(len(str2)-1,-1,-1):
            arr2.append(str2[i])
            
        # print("arr2",arr2)
        str3 = "".join(arr2)
        # print("str3",str3)
        if str2 == str3:
            return 1
        else:
            return 0
        
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.isDigitSumPalindrome(N))
# } Driver Code Ends