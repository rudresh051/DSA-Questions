#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,s):
        # Code here
        res = []
        
        for i in range(len(s)):
            # print(s[i])
            res.append(s[i])
        
        
        set1 = set("'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+\/'[]{};:?<>,.~`")
        
        for i in range(len(res)):
            if s[i] in set1:
                return -1
            else:
                continue
        

        for i in range(len(res)):
            if res[i]=='0':
                continue
            elif res[i]!='0':
                index = i
                break
            
        num = res[index:len(res)]
        # print("num",num)
        return "".join(num)


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends