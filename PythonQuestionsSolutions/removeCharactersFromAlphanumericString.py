#User function Template for python3
class Solution:
    def removeCharacters(self, S):
        # code here
        '''res = []
        num = [1,2,3,4,5,6,7,8,9,0]
        num_str = ''.join(map(str, num))  # Convert each digit to string and concatenate


        for i in range(len(S)):
          #  print("type S[i]",type(S[i]))
            if S[i] in num_str:
                res.append(S[i])
            else:
                continue

       # return res
        return "".join(res)'''

            #Method 2
            res = []
            num_set = set('1234567890')

            for i in range(len(S)):
                if S[i] in num_set:
                    res.append(S[i])
                else:
                    continue

            return "".join(res)
    




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.removeCharacters(s)

        print(answer)


# } Driver Code Ends