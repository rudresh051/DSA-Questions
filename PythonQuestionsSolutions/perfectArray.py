class Solution:
    def IsPerfect(self,arr,n):
        #Complete the function
        # print(arr)
        length = len(arr)
        y = []
        for i in range(length-1,-1,-1):
            # print("i",arr[i])
            y.append(arr[i])
        
        # print(y)
        
        #now let's use looping over two loops at same time
        flag = True # Assuming there is no different element in the array.
        for val1,val2 in zip(arr,y):
            # print(val1,val2)
            if val1==val2:
                continue
            elif val1!=val2:
                flag = False
                #now simply come out of the loop and return flag value based on it's status
                break
        
        # print(flag)
        if flag==True:
            return True
        elif flag == False:
            return False