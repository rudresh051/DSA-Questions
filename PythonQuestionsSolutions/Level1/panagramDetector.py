#User function Template for python3

class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        #code here
        alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        s1 = s.upper()
        # print("s1",s1)
        list1 = []
        for i in range(len(s1)):
            if s1[i] in alphabet:
                list1.append(s1[i])
            else:
                continue
        # print("list1",list1)
        #Now let's make a set from above
        set_list1 = set(list1)
        # print("set_list1",set_list1)
        #Now let's make a list for above set
        list2 = list(set_list1)
        # print("list2",list2)
        
        if len(list2)==26:
            return True
        else:
            return False
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        obj = Solution()
        if(obj.checkPangram(s)):
            print(1)
        else:
            print(0)
# } Driver Code Ends