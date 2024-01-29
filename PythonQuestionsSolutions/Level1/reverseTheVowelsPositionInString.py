#User function Template for python3

class Solution:
    def modify(self, s):
        # code here
        # print(s)
        res = []
        vowels = []
        rev_vowels=[]
        final = []
        
        for i in range(len(s)):
            res.append(s[i])
        # print("res",res)
        
        for i in range(len(res)):
            if (res[i]=='a' or res[i]=='e' or res[i]=='i' or res[i]=='o' or res[i]=='u'):
                vowels.append(res[i])
                
        # print("vowels",vowels)
        # Now reverse the vowels value
        for i in range(len(vowels)-1,-1,-1):
            rev_vowels.append(vowels[i])
        # print("rev_vowels",rev_vowels)
        
        
        count = 0
        for i in range(len(res)):
            # print(res[i])
            if (res[i]=='a' or res[i]=='e' or res[i]=='i' or res[i]=='o' or res[i]=='u'):
                temp = rev_vowels[count]
                # print(temp,count)
                final.append(temp)
                count = count+1
            else:
                final.append(res[i])
            
        # print("final",final)
        finalString = "".join(final)
        return finalString
        
                
            
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.modify(s)
        print(ans)
# } Driver Code Ends