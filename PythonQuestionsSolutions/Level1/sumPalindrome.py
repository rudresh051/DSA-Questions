#User function Template for python3

class Solution:
    def isSumPalindrome (self, n):
        # code here 
        # print("n",n)
        
        
        str1 = str(n)
        rev1 = ''
        for i in range(len(str1)-1,-1,-1):
            rev1 = rev1 + str1[i]
        # print('rev1',rev1)
        
        if n==int(rev1):
            return rev1
        else:
            pass
        
        n1 = int(rev1)
        sum1 = n1+n
        # print("sum1",sum1)
        revSum1 = str(sum1)
        checkPalindrome1 = ''
        count = 0
        for i in range(len(revSum1)-1,-1,-1):
            checkPalindrome1 = checkPalindrome1+revSum1[i]
        if checkPalindrome1==revSum1:
            return checkPalindrome1
        else:
            count=1
            pass
        
        #Now my revSum1 becomes new number for checking
        # print("revSum1",revSum1)
        # print("checkPalindrome1",checkPalindrome1)
        revSum2 = int(revSum1)+int(checkPalindrome1)
        strRevSum2 = str(revSum2)
        checkPalindrome2 =''
        for i in range(len(strRevSum2)-1,-1,-1):
            checkPalindrome2 = checkPalindrome2+strRevSum2[i]
        # print("checkPalindrome2",checkPalindrome2)    
        if checkPalindrome2==strRevSum2:
            return checkPalindrome2
        else:
            count=2
            pass        
        
        #Now my revSum2 becomes new number for checking
        # print("revSum2",revSum2)
        # print("checkPalindrome2",checkPalindrome2)
        revSum3 = int(revSum2)+int(checkPalindrome2)
        # print("revSum3",revSum3)
        strRevSum3 = str(revSum3)
        checkPalindrome3 =''
        for i in range(len(strRevSum3)-1,-1,-1):
            checkPalindrome3 = checkPalindrome3+strRevSum3[i]
        # print("checkPalindrome3",checkPalindrome3)    
        if checkPalindrome3==strRevSum3:
            return checkPalindrome3
        else:
            count=3
            pass 
        
        #Now my revSum3 becomes new number for checking
        # print("revSum3",revSum3)
        # print("checkPalindrome3",checkPalindrome3)
        revSum4 = int(revSum3)+int(checkPalindrome3)
        # print("revSum4",revSum4)
        strRevSum4 = str(revSum4)
        checkPalindrome4 =''
        for i in range(len(strRevSum4)-1,-1,-1):
            checkPalindrome4 = checkPalindrome4+strRevSum4[i]
        # print("checkPalindrome4",checkPalindrome4)    
        if checkPalindrome4==strRevSum4:
            return checkPalindrome4
        else:
            count=4
            pass 
        
        #Now my revSum4 becomes new number for checking
        # print("revSum4",revSum4)
        # print("checkPalindrome3",checkPalindrome4)
        revSum5 = int(revSum4)+int(checkPalindrome4)
        # print("revSum5",revSum5)
        strRevSum5 = str(revSum5)
        checkPalindrome5 =''
        for i in range(len(strRevSum5)-1,-1,-1):
            checkPalindrome5 = checkPalindrome5+strRevSum5[i]
        # print("checkPalindrome5",checkPalindrome5)    
        if checkPalindrome5==strRevSum5:
            return checkPalindrome5
        else:
            count=5
            pass 
        
        return -1
        
        
        
        
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.isSumPalindrome(n))
# } Driver Code Ends